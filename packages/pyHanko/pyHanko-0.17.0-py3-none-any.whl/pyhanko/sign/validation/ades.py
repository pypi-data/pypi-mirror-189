"""
This module contains a number of functions to handle AdES signature validation.


.. danger::
    This API is incubating, and not all features of the spec have been fully
    implemented at this stage. There will be bugs, and API changes may still
    occur.
"""
import asyncio
import dataclasses
import itertools
import logging
from copy import copy
from dataclasses import dataclass
from datetime import datetime
from typing import (
    Any,
    Dict,
    FrozenSet,
    Iterable,
    Iterator,
    List,
    Optional,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
)

import tzlocal
from asn1crypto import cms, keys
from asn1crypto import pdf as asn1_pdf
from asn1crypto import tsp, x509
from asn1crypto.crl import CertificateList
from asn1crypto.ocsp import OCSPResponse
from pyhanko_certvalidator import ValidationContext
from pyhanko_certvalidator.authority import CertTrustAnchor, TrustAnchor
from pyhanko_certvalidator.context import (
    CertValidationPolicySpec,
    ValidationDataHandlers,
)
from pyhanko_certvalidator.ltv.ades_past import past_validate
from pyhanko_certvalidator.ltv.poe import POEManager, digest_for_poe
from pyhanko_certvalidator.ltv.time_slide import ades_gather_prima_facie_revinfo
from pyhanko_certvalidator.ltv.types import ValidationTimingInfo
from pyhanko_certvalidator.path import ValidationPath
from pyhanko_certvalidator.policy_decl import (
    AlgorithmUsagePolicy,
    RevocationCheckingRule,
)
from pyhanko_certvalidator.registry import PathBuilder, TrustManager
from pyhanko_certvalidator.revinfo.archival import CRLContainer, OCSPContainer
from pyhanko_certvalidator.revinfo.validate_crl import CRLOfInterest
from pyhanko_certvalidator.revinfo.validate_ocsp import OCSPResponseOfInterest

from pyhanko.pdf_utils.reader import HistoricalResolver, PdfFileReader
from pyhanko.sign.ades.report import (
    AdESFailure,
    AdESIndeterminate,
    AdESPassed,
    AdESStatus,
    AdESSubIndic,
)
from pyhanko.sign.general import (
    CMSExtractionError,
    CMSStructuralError,
    MultivaluedAttributeError,
    NonexistentAttributeError,
    extract_certificate_info,
    find_cms_attribute,
    find_unique_cms_attribute,
)
from pyhanko.sign.validation import (
    DocumentSecurityStore,
    EmbeddedPdfSignature,
    errors,
    generic_cms,
)
from pyhanko.sign.validation.settings import KeyUsageConstraints
from pyhanko.sign.validation.status import (
    DocumentTimestampStatus,
    PdfSignatureStatus,
    RevocationDetails,
    SignatureCoverageLevel,
    SignatureStatus,
    SignerAttributeStatus,
    StandardCMSSignatureStatus,
    TimestampSignatureStatus,
)

from ..diff_analysis import DiffPolicy, DiffResult, SuspiciousModification
from .policy_decl import (
    LocalKnowledge,
    PdfSignatureValidationSpec,
    SignatureValidationSpec,
    bootstrap_validation_data_handlers,
)

__all__ = [
    'ades_basic_validation',
    'ades_with_time_validation',
    'ades_lta_validation',
    'ades_timestamp_validation',
    'AdESBasicValidationResult',
    'AdESWithTimeValidationResult',
    'AdESLTAValidationResult',
]

logger = logging.getLogger(__name__)

StatusType = TypeVar('StatusType', bound=SignatureStatus)


@dataclass(frozen=True)
class AdESBasicValidationResult:
    """
    Result of validation of basic signatures.

    ETSI EN 319 102-1, § 5.3
    """

    ades_subindic: AdESSubIndic
    """
    AdES subindication.
    """

    api_status: Optional[StatusType]
    """
    A status descriptor object from pyHanko's own validation API.
    Will be an instance of :class:`.SignatureStatus` or a subclass
    thereof.
    """

    failure_msg: Optional[str]
    """
    A string describing the reason why validation failed,
    if applicable.
    """


@dataclass
class _InternalBasicValidationResult:
    ades_subindic: AdESSubIndic
    signature_poe_time: Optional[datetime]
    signature_not_before_time: Optional[datetime]
    status_kwargs: Optional[dict] = None
    trust_subindic_update: Optional[AdESSubIndic] = None

    signature_ts_validity: Optional[TimestampSignatureStatus] = None
    content_ts_validity: Optional[TimestampSignatureStatus] = None

    signer_attr_status: Optional[SignerAttributeStatus] = None

    def update(self, status_cls, with_ts, with_attrs):
        status_kwargs = self.status_kwargs
        if self.trust_subindic_update:
            status_kwargs['trust_problem_indic'] = self.trust_subindic_update

        if with_ts and self.signature_ts_validity:
            status_kwargs['timestamp_validity'] = self.signature_ts_validity
        if with_ts and self.content_ts_validity:
            status_kwargs['content_timestamp_validity'] \
                = self.content_ts_validity
        if with_attrs and self.signer_attr_status:
            status_kwargs['ac_attrs'] = self.signer_attr_status.ac_attrs
            status_kwargs['cades_signer_attrs'] \
                = self.signer_attr_status.cades_signer_attrs
            status_kwargs['ac_validation_errs'] \
                = self.signer_attr_status.ac_validation_errs
        return status_cls(**status_kwargs)


async def ades_timestamp_validation(
        tst_signed_data: cms.SignedData,
        validation_spec: SignatureValidationSpec,
        expected_tst_imprint: bytes,
        timing_info: Optional[ValidationTimingInfo] = None,
        validation_data_handlers: Optional[ValidationDataHandlers] = None,
        extra_status_kwargs: Optional[Dict[str, Any]] = None,
        status_cls: Type[StatusType] = TimestampSignatureStatus) \
        -> AdESBasicValidationResult:
    """
    Validate a timestamp token according to ETSI EN 319 102-1 § 5.4.

    :param tst_signed_data:
        The ``SignedData`` value of the timestamp.
    :param validation_spec:
        Validation settings to apply.
    :param expected_tst_imprint:
        The expected message imprint in the timestamp token.
    :param timing_info:
        Data object describing the timing of the validation.
        Defaults to :meth:`.ValidationTimingInfo.now`.
    :param validation_data_handlers:
        Data handlers to manage validation data.
    :param extra_status_kwargs:
        Extra keyword arguments to pass to the signature status object's
        ``__init__`` function.
    :param status_cls:
        The class of the resulting status object in pyHanko's internal
        validation API.
    :return:
        A :class:`.AdESBasicValidationResult`.
    """

    timing_info = timing_info or ValidationTimingInfo.now()
    cert_validation_policy = (
        validation_spec.ts_cert_validation_policy
        or validation_spec.cert_validation_policy
    )

    if validation_data_handlers is None:
        validation_data_handlers = bootstrap_validation_data_handlers(
            spec=validation_spec,
            timing_info=timing_info
        )

    validation_context = cert_validation_policy.build_validation_context(
        timing_info=timing_info,
        handlers=validation_data_handlers
    )
    return await _ades_timestamp_validation_from_context(
        tst_signed_data, validation_context, expected_tst_imprint,
        extra_status_kwargs=extra_status_kwargs, status_cls=status_cls
    )


def _ades_signature_crypto_policy_check(
        signer_info: cms.SignerInfo,
        algo_policy: AlgorithmUsagePolicy,
        control_time: datetime,
        public_key: Optional[keys.PublicKeyInfo]):

    sig_algo: cms.SignedDigestAlgorithm = signer_info['signature_algorithm']
    sig_allowed = algo_policy.signature_algorithm_allowed(
        sig_algo, control_time, public_key=public_key
    )
    if not sig_allowed:
        msg = (
            f"Signature algorithm {sig_algo.signature_algo} not allowed as "
            f"of {control_time}, which is "
            f"the time of the earliest PoE for the signature."
        )
        raise errors.SignatureValidationError(
            msg,
            ades_subindication=(
                AdESIndeterminate.CRYPTO_CONSTRAINTS_FAILURE
                if sig_allowed.not_allowed_after is None
                else AdESIndeterminate.CRYPTO_CONSTRAINTS_FAILURE_NO_POE
            )
        )


async def _ades_timestamp_validation_from_context(
        tst_signed_data: cms.SignedData,
        validation_context: ValidationContext,
        expected_tst_imprint: bytes,
        extra_status_kwargs: Optional[Dict[str, Any]] = None,
        status_cls: Type[StatusType] = TimestampSignatureStatus) \
        -> AdESBasicValidationResult:
    status_kwargs = dict(extra_status_kwargs or {})
    status_kwargs_from_validation = await generic_cms.validate_tst_signed_data(
        tst_signed_data, validation_context=validation_context,
        expected_tst_imprint=expected_tst_imprint
    )
    status_kwargs.update(status_kwargs_from_validation)
    status = status_cls(**status_kwargs)
    if not status.intact:
        return AdESBasicValidationResult(
            ades_subindic=AdESFailure.HASH_FAILURE,
            api_status=status,
            failure_msg=None
        )
    elif not status.valid:
        return AdESBasicValidationResult(
            ades_subindic=AdESFailure.SIG_CRYPTO_FAILURE,
            api_status=status,
            failure_msg=None
        )

    interm_result = await _process_basic_validation(
        tst_signed_data, status, validation_context,
        ac_validation_context=None,
        signature_not_before_time=None,
    )
    interm_result.status_kwargs = status_kwargs
    return AdESBasicValidationResult(
        ades_subindic=interm_result.ades_subindic,
        api_status=interm_result.update(
            status_cls, with_ts=False, with_attrs=False
        ),
        failure_msg=None
    )


async def _ades_process_attached_ts(signer_info, validation_context,
                                    signed: bool, tst_digest: bytes) \
        -> AdESBasicValidationResult:
    tst_signed_data = generic_cms.extract_tst_data(signer_info, signed=signed)
    if tst_signed_data is not None:
        return await _ades_timestamp_validation_from_context(
            tst_signed_data, validation_context, tst_digest,
        )
    return AdESBasicValidationResult(
        ades_subindic=AdESIndeterminate.GENERIC,
        failure_msg=None, api_status=None
    )


async def _process_basic_validation(
        signed_data: cms.SignedData, temp_status: SignatureStatus,
        ts_validation_context: ValidationContext,
        ac_validation_context: Optional[ValidationContext],
        signature_not_before_time: Optional[datetime]):
    ades_trust_status: Optional[AdESSubIndic] = temp_status.trust_problem_indic
    signer_info = generic_cms.extract_signer_info(signed_data)
    ts_status: Optional[TimestampSignatureStatus] = None
    if ades_trust_status in (AdESIndeterminate.REVOKED_NO_POE,
                             AdESIndeterminate.OUT_OF_BOUNDS_NO_POE):
        # check content timestamp
        # TODO allow selecting one of multiple here
        # FIXME here and in a few other places we presume that the message
        #  imprint algorithm agrees with the TS's algorithm. This is a fairly
        #  safe assumption, but not an airtight one.
        content_ts_result = await _ades_process_attached_ts(
            signer_info, ts_validation_context, signed=True,
            tst_digest=generic_cms.find_unique_cms_attribute(
                signer_info['signed_attrs'], 'message_digest'
            ).native
        )
        if content_ts_result.ades_subindic == AdESPassed.OK:
            ts_status = content_ts_result.api_status

            if signature_not_before_time is not None:
                signature_not_before_time = max(
                    ts_status.timestamp, signature_not_before_time
                )
            else:
                signature_not_before_time = ts_status.timestamp

            # now we potentially have POE to know for sure that the signer's
            # certificate was in fact revoked/expired.
            # HOWEVER, according to the spec it is _not_ within this functions
            # remit to check the signature timestamp to reverse a positive
            # X_NO_POE judgement!!
            if ades_trust_status == AdESIndeterminate.REVOKED_NO_POE:
                revo_details: RevocationDetails = temp_status.revocation_details
                cutoff = revo_details.revocation_date
                perm_status = AdESFailure.REVOKED
            else:
                cutoff = temp_status.signing_cert.not_valid_after
                perm_status = AdESIndeterminate.EXPIRED

            if signature_not_before_time >= cutoff:
                ades_trust_status = perm_status

    # TODO process signature policy attr once we can

    cert_info = generic_cms.extract_certificate_info(signed_data)

    # FIXME this is not entirely correct, we need past validation
    #  for attr certs as well
    attr_status_kwargs = await generic_cms.collect_signer_attr_status(
        sd_attr_certificates=cert_info.attribute_certs,
        signer_cert=cert_info.signer_cert,
        validation_context=ac_validation_context,
        sd_signed_attrs=signer_info['signed_attrs']
    )
    ades_subindic = ades_trust_status or AdESPassed.OK
    return _InternalBasicValidationResult(
        ades_subindic=ades_subindic,
        trust_subindic_update=ades_trust_status,
        content_ts_validity=ts_status,
        signature_not_before_time=signature_not_before_time,
        signer_attr_status=SignerAttributeStatus(**attr_status_kwargs),
        signature_poe_time=None
    )


def _init_vcs(
        validation_spec: SignatureValidationSpec,
        timing_info: ValidationTimingInfo,
        validation_data_handlers: ValidationDataHandlers
):

    validation_context = validation_spec.cert_validation_policy\
        .build_validation_context(
            timing_info=timing_info,
            handlers=validation_data_handlers
        )
    if validation_spec.ts_cert_validation_policy is not None:
        ts_validation_context = validation_spec.ts_cert_validation_policy \
            .build_validation_context(
                timing_info=timing_info,
                handlers=validation_data_handlers
            )
    else:
        ts_validation_context = validation_context

    if validation_spec.ac_validation_policy is not None:
        ac_validation_context = validation_spec.ac_validation_policy \
            .build_validation_context(
                timing_info=timing_info,
                handlers=validation_data_handlers
            )
    else:
        ac_validation_context = None

    return validation_context, ts_validation_context, ac_validation_context


# ETSI EN 319 102-1 § 5.3


async def ades_basic_validation(
        signed_data: cms.SignedData,
        validation_spec: SignatureValidationSpec,
        timing_info: Optional[ValidationTimingInfo] = None,
        raw_digest: Optional[bytes] = None,
        validation_data_handlers: Optional[ValidationDataHandlers] = None,
        signature_not_before_time: Optional[datetime] = None,
        extra_status_kwargs: Optional[Dict[str, Any]] = None,
        status_cls: Type[StatusType] = StandardCMSSignatureStatus) \
        -> AdESBasicValidationResult:
    """
    Validate a CMS signature according to ETSI EN 319 102-1 § 5.3.

    :param signed_data:
        The ``SignedData`` value.
    :param validation_spec:
        Validation settings to apply.
    :param raw_digest:
        The expected message digest attribute value.
    :param timing_info:
        Data object describing the timing of the validation.
        Defaults to :meth:`.ValidationTimingInfo.now`.
    :param validation_data_handlers:
        Data handlers to manage validation data.
    :param extra_status_kwargs:
        Extra keyword arguments to pass to the signature status object's
        ``__init__`` function.
    :param status_cls:
        The class of the resulting status object in pyHanko's internal
        validation API.
    :param signature_not_before_time:
        Time when the signature was known _not_ to exist.
    :return:
        A :class:`.AdESBasicValidationResult`.
    """

    timing_info = timing_info or ValidationTimingInfo.now()
    if validation_data_handlers is None:
        validation_data_handlers = bootstrap_validation_data_handlers(
            spec=validation_spec,
            timing_info=timing_info
        )
    validation_context, ts_validation_context, ac_validation_context = \
        _init_vcs(validation_spec, timing_info, validation_data_handlers)

    interm_result = await _ades_basic_validation(
        signed_data=signed_data,
        validation_context=validation_context,
        ts_validation_context=ts_validation_context,
        ac_validation_context=ac_validation_context,
        key_usage_settings=validation_spec.key_usage_settings,
        raw_digest=raw_digest,
        signature_not_before_time=signature_not_before_time,
        extra_status_kwargs=extra_status_kwargs,
        status_cls=status_cls
    )
    if isinstance(interm_result, AdESBasicValidationResult):
        return interm_result

    return AdESBasicValidationResult(
        ades_subindic=interm_result.ades_subindic,
        api_status=interm_result.update(
            StandardCMSSignatureStatus, with_ts=False,
            with_attrs=True
        ),
        failure_msg=None
    )


async def _ades_basic_validation(
        signed_data: cms.SignedData,
        validation_context: ValidationContext,
        ts_validation_context: ValidationContext,
        ac_validation_context: Optional[ValidationContext],
        key_usage_settings: KeyUsageConstraints,
        raw_digest: Optional[bytes],
        signature_not_before_time: Optional[datetime],
        extra_status_kwargs: Optional[Dict[str, Any]],
        status_cls: Type[StatusType]) \
        -> Union[AdESBasicValidationResult, _InternalBasicValidationResult]:
    status_kwargs = dict(extra_status_kwargs or {})
    try:
        status_kwargs_from_validation = await generic_cms.cms_basic_validation(
            signed_data, raw_digest=raw_digest,
            validation_context=validation_context,
            key_usage_settings=key_usage_settings
        )
        status_kwargs.update(status_kwargs_from_validation)
    except errors.SignatureValidationError as e:
        return AdESBasicValidationResult(
            ades_subindic=e.ades_subindication, failure_msg=e.failure_message,
            api_status=None
        )

    # put the temp status into a SignatureStatus object for convenience
    status: SignatureStatus = status_cls(**status_kwargs)
    if not status.intact:
        return AdESBasicValidationResult(
            ades_subindic=AdESFailure.HASH_FAILURE,
            api_status=status,
            failure_msg=None
        )
    elif not status.valid:
        return AdESBasicValidationResult(
            ades_subindic=AdESFailure.SIG_CRYPTO_FAILURE,
            api_status=status,
            failure_msg=None
        )

    interm_result = await _process_basic_validation(
        signed_data, status, ts_validation_context,
        ac_validation_context=ac_validation_context,
        signature_not_before_time=signature_not_before_time,
    )
    interm_result.status_kwargs = status_kwargs
    return interm_result


@dataclass(frozen=True)
class AdESWithTimeValidationResult(AdESBasicValidationResult):
    best_signature_time: datetime
    signature_not_before_time: Optional[datetime]


_WITH_TIME_FURTHER_PROC = frozenset({
    AdESPassed.OK,
    AdESIndeterminate.CRYPTO_CONSTRAINTS_FAILURE_NO_POE,
    AdESIndeterminate.REVOKED_NO_POE,
    AdESIndeterminate.REVOKED_CA_NO_POE,
    # TODO process TRY_LATER
    # AdESIndeterminate.TRY_LATER,
    AdESIndeterminate.OUT_OF_BOUNDS_NO_POE
})


async def ades_with_time_validation(
        signed_data: cms.SignedData,
        validation_spec: SignatureValidationSpec,
        timing_info: Optional[ValidationTimingInfo] = None,
        raw_digest: Optional[bytes] = None,
        validation_data_handlers: Optional[ValidationDataHandlers] = None,
        signature_not_before_time: Optional[datetime] = None,
        extra_status_kwargs: Optional[Dict[str, Any]] = None,
        status_cls: Type[StatusType] = StandardCMSSignatureStatus) \
        -> AdESWithTimeValidationResult:
    """
    Validate a CMS signature with time according to ETSI EN 319 102-1 § 5.5.

    :param signed_data:
        The ``SignedData`` value.
    :param validation_spec:
        Validation settings to apply.
    :param raw_digest:
        The expected message digest attribute value.
    :param timing_info:
        Data object describing the timing of the validation.
        Defaults to :meth:`.ValidationTimingInfo.now`.
    :param validation_data_handlers:
        Data handlers to manage validation data.
    :param extra_status_kwargs:
        Extra keyword arguments to pass to the signature status object's
        ``__init__`` function.
    :param status_cls:
        The class of the resulting status object in pyHanko's internal
        validation API.
    :param signature_not_before_time:
        Time when the signature was known _not_ to exist.
    :return:
        A :class:`.AdESBasicValidationResult`.
    """

    timing_info = timing_info or ValidationTimingInfo.now()
    if validation_data_handlers is None:
        validation_data_handlers = bootstrap_validation_data_handlers(
            spec=validation_spec,
            timing_info=timing_info
        )

    validation_context, ts_validation_context, ac_validation_context = \
        _init_vcs(validation_spec, timing_info, validation_data_handlers)

    sig_bytes = signed_data['signer_infos'][0]['signature'].native
    signature_poe_time = validation_data_handlers.poe_manager[sig_bytes]

    interm_result = await _ades_basic_validation(
        signed_data, validation_context=validation_context,
        ts_validation_context=ts_validation_context,
        ac_validation_context=ac_validation_context,
        key_usage_settings=validation_spec.key_usage_settings,
        raw_digest=raw_digest,
        signature_not_before_time=signature_not_before_time,
        extra_status_kwargs=extra_status_kwargs,
        status_cls=status_cls
    )
    if isinstance(interm_result, AdESBasicValidationResult):
        return AdESWithTimeValidationResult(
            ades_subindic=interm_result.ades_subindic,
            api_status=interm_result.api_status,
            failure_msg=interm_result.failure_msg,
            best_signature_time=signature_poe_time,
            signature_not_before_time=signature_not_before_time
        )
    elif interm_result.ades_subindic not in _WITH_TIME_FURTHER_PROC:
        assert isinstance(interm_result, _InternalBasicValidationResult)
        signature_not_before_time = interm_result.signature_not_before_time
        api_status = interm_result.update(
            status_cls, with_ts=True, with_attrs=True
        )
        return AdESWithTimeValidationResult(
            ades_subindic=interm_result.ades_subindic,
            api_status=api_status,
            failure_msg=None,
            best_signature_time=signature_poe_time,
            signature_not_before_time=signature_not_before_time
        )

    signer_info = generic_cms.extract_signer_info(signed_data)

    # process signature timestamps
    # TODO allow selecting one of multiple timestamps here?
    sig_ts_result = await _ades_process_attached_ts(
        signer_info, validation_context, signed=False,
        tst_digest=generic_cms.compute_signature_tst_digest(signer_info)
    )
    temp_status = interm_result.update(
        status_cls, with_ts=False, with_attrs=True
    )

    if sig_ts_result.ades_subindic != AdESPassed.OK:
        return AdESWithTimeValidationResult(
            ades_subindic=interm_result.ades_subindic,
            api_status=temp_status,
            failure_msg=None,
            best_signature_time=signature_poe_time,
            signature_not_before_time=signature_not_before_time
        )

    ts_status = sig_ts_result.api_status

    if signature_poe_time is not None:
        signature_poe_time = min(ts_status.timestamp, signature_poe_time)
    else:
        signature_poe_time = ts_status.timestamp
    interm_result.signature_ts_validity = ts_status
    interm_result.signature_poe_time = signature_poe_time

    if interm_result.ades_subindic == AdESIndeterminate.REVOKED_NO_POE:
        revo_details: RevocationDetails = temp_status.revocation_details
        if signature_poe_time >= revo_details.revocation_date:
            # nothing we can do
            return AdESWithTimeValidationResult(
                ades_subindic=interm_result.ades_subindic,
                api_status=temp_status, failure_msg=None,
                best_signature_time=signature_poe_time,
                signature_not_before_time=signature_not_before_time
            )
    elif interm_result.ades_subindic == \
            AdESIndeterminate.OUT_OF_BOUNDS_NO_POE:
        # NOTE: we can't process expiration here since we don't have access
        #  to _timestamped_ revocation information
        if signature_poe_time < temp_status.signing_cert.not_valid_before:
            # FIXME replace temp_status as well
            return AdESWithTimeValidationResult(
                ades_subindic=AdESIndeterminate.NOT_YET_VALID,
                api_status=temp_status, failure_msg=None,
                best_signature_time=signature_poe_time,
                signature_not_before_time=signature_not_before_time
            )

    # TODO TSTInfo ordering/comparison check
    if signature_not_before_time is not None and \
            signature_not_before_time > signature_poe_time:
        return AdESWithTimeValidationResult(
            ades_subindic=AdESIndeterminate.TIMESTAMP_ORDER_FAILURE,
            api_status=temp_status, failure_msg=None,
            best_signature_time=signature_poe_time,
            signature_not_before_time=signature_not_before_time
        )
    # TODO handle time-stamp delay
    # TODO handle TRY_LATER  (now forcibly excluded)
    interm_result.trust_subindic_update = None
    interm_result.status_kwargs['trust_problem_indic'] = None

    status = interm_result.update(status_cls, with_ts=True, with_attrs=True)
    return AdESWithTimeValidationResult(
        ades_subindic=AdESPassed.OK,
        api_status=status, failure_msg=None,
        best_signature_time=signature_poe_time,
        signature_not_before_time=signature_not_before_time
    )


class _TrustNoOne(TrustManager):

    def is_root(self, cert: x509.Certificate) -> bool:
        return False

    def find_potential_issuers(self, cert: x509.Certificate) \
            -> Iterator[TrustAnchor]:
        return iter(())


def _crl_issuer_cert_poe_boundary(
        crl: CRLOfInterest, cutoff: datetime, poe_manager: POEManager
):
    return any(
        poe_manager[prov_path.path.leaf] <= cutoff
        for prov_path in crl.prov_paths
    )


def _ocsp_issuer_cert_poe_boundary(
        ocsp: OCSPResponseOfInterest, cutoff: datetime, poe_manager: POEManager
):
    return poe_manager[ocsp.prov_path.leaf] <= cutoff


async def _find_revinfo_data_for_leaf_in_past(
        cert: x509.Certificate,
        validation_data_handlers: ValidationDataHandlers,
        control_time: datetime,
        revocation_checking_rule: RevocationCheckingRule):
    # Need to find a piece of revinfo for the signing cert, for which we have
    # POE for the issuer cert, which must be dated before the expiration date of
    # the cert. (Standard is unclear as to which cert this refers to, but
    # it's probably the date on the signing cert. Not much point in requiring
    # PoE for a cert before its self-declared expiration date...)
    # Since our revinfo gathering logic is based on paths, we gather up all
    # candidate issuers and work with those "truncated" candidate paths.
    # Trust is not an issue at this stage.
    registry = validation_data_handlers.cert_registry
    candidate_issuers = registry.find_potential_issuers(
        cert=cert, trust_manager=_TrustNoOne()
    )

    def _for_candidate_issuer(iss: x509.Certificate):
        truncated_path = ValidationPath(
            trust_anchor=CertTrustAnchor(iss),
            interm=[],
            leaf=cert
        )
        return ades_gather_prima_facie_revinfo(
            path=truncated_path,
            revinfo_manager=validation_data_handlers.revinfo_manager,
            control_time=control_time,
            revocation_checking_rule=revocation_checking_rule
        )

    job_futures = asyncio.as_completed(
        [_for_candidate_issuer(iss) for iss in candidate_issuers]
    )

    poe_manager = validation_data_handlers.poe_manager

    crls: List[CRLOfInterest] = []
    ocsps: List[OCSPResponseOfInterest] = []
    new_crls: Iterable[CRLOfInterest]
    new_ocsps: Iterable[OCSPResponseOfInterest]
    to_evict: Set[bytes] = set()
    for fut_results in job_futures:
        new_crls, new_ocsps = await fut_results
        # Collect the revinfos for which we have POE for the issuer cert
        # predating the expiration of the signer cert
        for crl_oi in new_crls:
            if _crl_issuer_cert_poe_boundary(
                    crl_oi, cert.not_valid_after, poe_manager
            ):
                crls.append(crl_oi)
            else:
                revinfo_data = crl_oi.crl.crl_data.dump()
                to_evict.add(digest_for_poe(revinfo_data))

        for ocsp_oi in new_ocsps:
            if _ocsp_issuer_cert_poe_boundary(
                ocsp_oi, cert.not_valid_after, poe_manager
            ):
                ocsps.append(ocsp_oi)
            else:
                revinfo_data = ocsp_oi.ocsp_response.ocsp_response_data.dump()
                to_evict.add(digest_for_poe(revinfo_data))
    # we only run the eviction logic if we found at least one piece of revinfo
    # that we can actually use (that's what the spec says, shouldn't change
    # validation result, but the reported error probably makes more sense)
    if crls or ocsps:
        validation_data_handlers.revinfo_manager.evict_crls(to_evict)
        validation_data_handlers.revinfo_manager.evict_ocsps(to_evict)
    return crls, ocsps


async def _build_and_past_validate_cert(
        cert: x509.Certificate,
        validation_policy_spec: CertValidationPolicySpec,
        validation_data_handlers: ValidationDataHandlers,
        init_control_time: Optional[datetime] = None
) -> Tuple[ValidationPath, datetime]:

    path_builder = PathBuilder(
        trust_manager=validation_policy_spec.trust_manager,
        registry=validation_data_handlers.cert_registry
    )

    current_subindication = None
    paths = path_builder.async_build_paths_lazy(cert)
    try:
        async for cand_path in paths:
            current_subindication, revo_details, validation_time = \
                await generic_cms.handle_certvalidator_errors(
                    past_validate(
                        path=cand_path,
                        validation_policy_spec=validation_policy_spec,
                        validation_data_handlers=validation_data_handlers,
                        init_control_time=init_control_time,
                    )
                )
            if current_subindication is None:
                return cand_path, validation_time
    finally:
        await paths.cancel()

    msg = "Unable to construct plausible past validation path"
    if current_subindication is not None:
        raise errors.SignatureValidationError(
            failure_message=msg,
            ades_subindication=current_subindication
        )
    else:
        raise errors.SignatureValidationError(
            failure_message=f"{msg}: no prima facie paths constructed",
            ades_subindication=AdESIndeterminate.NO_CERTIFICATE_CHAIN_FOUND
        )


async def _ades_past_signature_validation(
        signed_data: cms.SignedData,
        validation_spec: SignatureValidationSpec,
        poe_manager: POEManager,
        current_time_sub_indic: Optional[AdESIndeterminate],
        init_control_time: Optional[datetime],
        is_timestamp: bool):

    validation_data_handlers = bootstrap_validation_data_handlers(
        validation_spec, is_historical=True,
        poe_manager_override=poe_manager
    )

    signature_bytes = signed_data['signer_infos'][0]['signature'].native
    best_signature_time = poe_manager[signature_bytes]

    try:
        cert_info = extract_certificate_info(signed_data)
        cert = cert_info.signer_cert
    except CMSExtractionError:
        raise errors.SignatureValidationError(
            'signer certificate not included in signature',
            ades_subindication=AdESIndeterminate.NO_SIGNING_CERTIFICATE_FOUND
        )

    if is_timestamp:
        cert_validation_policy = (
            validation_spec.ts_cert_validation_policy
            or validation_spec.cert_validation_policy
        )
    else:
        cert_validation_policy = validation_spec.cert_validation_policy
    leaf_crls, leaf_ocsps = await _find_revinfo_data_for_leaf_in_past(
        cert, validation_data_handlers,
        control_time=init_control_time,
        revocation_checking_rule=(
            cert_validation_policy
            .revinfo_policy
            .revocation_checking_policy
            .ee_certificate_rule
        )
    )

    # Key usage for the signer is not something that varies over time, so
    # we delegate that to the caller. This is justified both because it's
    # technically simpler, and because the past signature validation block
    # in AdES is predicated on delegating the basic integrity checks anyhow.
    cert_path, validation_time = await _build_and_past_validate_cert(
        cert, validation_policy_spec=cert_validation_policy,
        validation_data_handlers=validation_data_handlers,
    )

    # TODO revisit this once I have a clearer understanding of why this PoE
    #  issuance check is only applied to the EE cert.
    def _pass_contingent_on_revinfo_issuance_poe():
        if not bool(leaf_crls or leaf_ocsps):
            status = AdESIndeterminate.REVOCATION_OUT_OF_BOUNDS_NO_POE
            raise errors.SignatureValidationError(
                failure_message=(
                    "POE for signature available, but could not obtain "
                    "sufficient POE for the issuance of the "
                    "revocation information",
                ),
                ades_subindication=status
            )

    if best_signature_time <= validation_time:
        if current_time_sub_indic == AdESIndeterminate.REVOKED_NO_POE:
            _pass_contingent_on_revinfo_issuance_poe()
            return
        elif current_time_sub_indic in (
                AdESIndeterminate.REVOKED_CA_NO_POE,
                AdESIndeterminate.CRYPTO_CONSTRAINTS_FAILURE_NO_POE
        ):
            # This is an automatic pass given that certvalidator checks
            # these conditions for us as part of past_validate(...)
            return
        elif current_time_sub_indic in (
            AdESIndeterminate.OUT_OF_BOUNDS_NO_POE,
            AdESIndeterminate.OUT_OF_BOUNDS_NOT_REVOKED
        ):
            if best_signature_time < cert.not_valid_before:
                raise errors.SignatureValidationError(
                    failure_message="Signature predates cert validity period",
                    ades_subindication=AdESFailure.NOT_YET_VALID
                )
            elif best_signature_time <= cert.not_valid_after:
                _pass_contingent_on_revinfo_issuance_poe()
                return

    # TODO here, it would help to preserve more than the sub-indication
    #  from before
    raise errors.SigSeedValueValidationError(
        failure_message=(
            "Past signature validation did not manage "
            "to improve current time result."
        ),
        ades_subindication=current_time_sub_indic
    )


async def ades_past_signature_validation(
        signed_data: cms.SignedData,
        validation_spec: SignatureValidationSpec,
        poe_manager: POEManager,
        current_time_sub_indic: Optional[AdESIndeterminate],
        init_control_time: Optional[datetime] = None) -> AdESSubIndic:
    """
    Validate a CMS signature in the past according
    to ETSI EN 319 102-1 § 5.6.2.4.

    This is internal API.

    .. danger::
        The notion of "past validation" used here is only valid in the
        narrow technical sense in which it is used within AdES.
        It should _never_ be relied upon as a standalone validation routine.

    :param signed_data:
        The ``SignedData`` value.
    :param validation_spec:
        Validation settings to apply.
    :param poe_manager:
        The POE manager from which to source existence proofs.
    :param current_time_sub_indic:
        The AdES subindication from validating the signature
        at the current time with the relevant settings.
    :param init_control_time:
        Initial value for the control time parameter.
    :return:
        An AdES subindication indicating the validation result
        after going through the past validation process.
    """

    eci = signed_data['encap_content_info']
    is_timestamp = eci['content_type'].native == 'tst_info'

    try:
        await _ades_past_signature_validation(
            signed_data=signed_data,
            validation_spec=validation_spec,
            poe_manager=poe_manager,
            current_time_sub_indic=current_time_sub_indic,
            init_control_time=init_control_time,
            is_timestamp=is_timestamp
        )
        return AdESPassed.OK
    except errors.SignatureValidationError as e:
        logger.warning(e)
        return e.ades_subindication


@dataclass(frozen=True)
class PrimaFaciePOE:
    pdf_revision: int
    timestamp_dt: datetime
    digests_covered: FrozenSet[bytes]
    timestamp_token_signed_data: cms.SignedData
    doc_digest: bytes
    diff_result: Union[DiffResult, SuspiciousModification, None]

    def add_to_poe_manager(self, manager: POEManager):
        for thing in self.digests_covered:
            manager.register_by_digest(digest=thing, dt=self.timestamp_dt)


def _extract_cert_digests_from_signed_data(sd: cms.SignedData):
    cert_choice: cms.CertificateChoices
    for cert_choice in sd['certificates']:
        if cert_choice.name in ('certificate', 'v2_attr_set'):
            yield digest_for_poe(cert_choice.chosen.dump())


def _get_tst_timestamp(sd: cms.SignedData) -> datetime:
    tst_info: tsp.TSTInfo = sd['encap_content_info']['content'].parsed
    return tst_info['gen_time'].native


def _build_prima_facie_poe_index_from_pdf_timestamps(
        r: PdfFileReader,
        include_content_ts: bool,
        diff_policy: Optional[DiffPolicy]):
    # This subroutine implements the POE gathering part of the evidence record
    # processing algorithm in AdES as applied to PDF. For the purposes of this
    # function, the chain of document timestamps is treated as a single evidence
    # record, and all document data in the revision in which a timestamp is
    # contained is considered fair game.
    # Signature timestamps are not processed as such, but POE for the timestamps
    # themselves will be accumulated.
    # Content timestamps can optionally be included. This is not standard
    # in AdES, but since there's no cryptographic difference (in PDF!) between
    # a content TS in a signature and a document timestamp signature, they
    # can be taken into account at the caller's discretion

    # TODO take algorithm usage policy into account?

    # TODO when ingesting OCSP responses, make an effort to register
    #  POE for the embedded certs as well? Esp. potential responder certs.

    # timestamp -> hashes index. We haven't validated the chain of trust
    # of the timestamps yet, so we can't put them in an actual
    # POE manager immediately

    # Since the embedded signature context is necessary to validate the POE's
    # integrity, we do run the integrity checker for the TST data at this stage.
    # The actual trust validation is delegated

    collected_so_far: Set[bytes] = set()
    # Holds all digests of objects contained in _document_ content so far
    # (note: this is why it's important to traverse the revisions in order)

    for_next_ts: Set[bytes] = set()
    # Holds digests of objects that will be registered with POE on the next
    # document TS or content TS encountered.

    prima_facie_poe_sets: List[PrimaFaciePOE] = []
    # output array (to avoid having to work with async generators)

    embedded_sig: EmbeddedPdfSignature

    for ix, embedded_sig in enumerate(r.embedded_signatures):

        embedded_sig.compute_integrity_info(
            # different None handling convention
            diff_policy, skip_diff=diff_policy is None
        )

        hist_handler = HistoricalResolver(
            r, revision=embedded_sig.signed_revision
        )

        signed_data: cms.SignedData = embedded_sig.signed_data
        ts_signed_data: Optional[cms.SignedData] = None
        is_doc_ts = False
        if embedded_sig.sig_object_type == '/DocTimeStamp':
            ts_signed_data = signed_data
            is_doc_ts = True
        elif include_content_ts:
            ts_signed_data = generic_cms.extract_tst_data(
                embedded_sig.signer_info, signed=True
            )

        # Important remark: at this time, we do NOT consider signature
        # timestamps when evaluating POE data, only content timestamps &
        # document timestamps!
        # Rationale: the signature timestamp only indirectly protects
        # the document content, and wasn't designed for this purpose.
        # If we want to use signature TSes as well, we'd have to evaluate
        # the integrity of the signature, which requires selecting a certificate
        # (even if just for validation purposes), yada yada. Not doing any of
        # that for now.
        # (This approach might change in the future)

        if ts_signed_data is not None:
            # add DSS content
            dss = DocumentSecurityStore.read_dss(hist_handler)
            collected_so_far.update(
                digest_for_poe(item.get_object().data)
                for item in itertools.chain(
                    dss.crls, dss.ocsps, dss.certs.values()
                )
            )
            collected_so_far.update(for_next_ts)
            doc_digest = embedded_sig.compute_digest()
            coverage_normal = embedded_sig.evaluate_signature_coverage() \
                              >= SignatureCoverageLevel.ENTIRE_REVISION
            if coverage_normal:
                prima_facie_poe_sets.append(
                    PrimaFaciePOE(
                        pdf_revision=embedded_sig.signed_revision,
                        timestamp_dt=_get_tst_timestamp(ts_signed_data),
                        digests_covered=frozenset(collected_so_far),
                        timestamp_token_signed_data=ts_signed_data,
                        doc_digest=doc_digest,
                        diff_result=embedded_sig.diff_result
                    )
                )
                # reset for_next_ts
                for_next_ts = set()
            for_next_ts.update(
                _extract_cert_digests_from_signed_data(ts_signed_data)
            )

        # the certs in the signature container itself are not part of the
        # signed data in that revision, but they're covered
        # by whatever the next (content) TS covers -> keep 'em
        for_next_ts.update(_extract_cert_digests_from_signed_data(signed_data))

        # same for revinfo embedded Adobe-style:
        # part of the signed data, but not directly timestamped
        # => save for next TS
        signed_attrs = embedded_sig.signer_info['signed_attrs']
        if not is_doc_ts:
            try:
                revinfo_attr: asn1_pdf.RevocationInfoArchival = \
                    find_unique_cms_attribute(
                        signed_attrs,
                        'adobe_revocation_info_archival'
                    )

                for_next_ts.update(
                    digest_for_poe(item.dump())
                    for item in itertools.chain(
                        revinfo_attr['crl'], revinfo_attr['ocsp']
                    )
                )
            except (MultivaluedAttributeError, NonexistentAttributeError):
                pass

        # Prepare a POE entry for the signature itself (to be processed
        # with the next timestamp)
        sig_bytes = embedded_sig.signer_info['signature'].native
        for_next_ts.add(digest_for_poe(sig_bytes))

        # add POE entries for the timestamp(s) attached to this signature
        try:
            content_tses = find_cms_attribute(
                signed_attrs, 'content_time_stamp'
            )
        except (NonexistentAttributeError, CMSStructuralError):
            content_tses = ()

        try:
            signature_tses = find_cms_attribute(
                embedded_sig.signer_info['unsigned_attrs'],
                'signature_time_stamp'
            )
        except (NonexistentAttributeError, CMSStructuralError):
            signature_tses = ()

        for ts_data in itertools.chain(signature_tses, content_tses):
            for ts_signer_info in ts_data['content']['signer_infos']:
                ts_sig_bytes = ts_signer_info['signature'].native
                for_next_ts.add(digest_for_poe(ts_sig_bytes))

    return prima_facie_poe_sets


async def _validate_prima_facie_poe(
        prima_facie_poe_sets: List[PrimaFaciePOE],
        # we assume that the validation info extracted from the DSS
        # has been registered in the revinfo gathering policy object
        # and/or the known cert list, respectively
        validation_spec: SignatureValidationSpec,
        cur_timing_info: Optional[ValidationTimingInfo] = None) -> POEManager:

    # Sort by PDF revision, but in ascending order (!)
    # This is a consequence of the way the ER validation algorithm works
    candidate_poes = sorted(
        prima_facie_poe_sets, key=lambda p: p.pdf_revision
    )

    cur_timing_info = cur_timing_info or ValidationTimingInfo.now(
        tz=tzlocal.get_localzone()
    )

    resulting_poes = POEManager()
    validation_spec.local_knowledge.add_to_poe_manager(resulting_poes)

    for ix, poe in enumerate(candidate_poes):
        temporary_poes = copy(resulting_poes)
        if ix < len(candidate_poes) - 1:
            # perform temp POE initialisation as the AdES spec requires
            next_poe = candidate_poes[ix + 1]
            next_poe.add_to_poe_manager(temporary_poes)

        validation_data_handlers = bootstrap_validation_data_handlers(
            validation_spec, timing_info=cur_timing_info,
            poe_manager_override=temporary_poes
        )
        cur_time_result = await ades_timestamp_validation(
            tst_signed_data=poe.timestamp_token_signed_data,
            validation_spec=validation_spec,
            timing_info=cur_timing_info,
            expected_tst_imprint=poe.doc_digest,
            validation_data_handlers=validation_data_handlers,
            extra_status_kwargs={'diff_result': poe.diff_result},
            status_cls=DocumentTimestampStatus
        )
        sub_indic = cur_time_result.ades_subindic
        if sub_indic.status == AdESStatus.PASSED:
            # still valid at current time => ok
            # (AdES spec on ER validation is unclear about this, but this
            #  should mean that we can skip the past validation block)
            poe.add_to_poe_manager(resulting_poes)
        elif sub_indic.status == AdESStatus.FAILED:
            # TODO more informative reporting?
            raise errors.SignatureValidationError(
                "Permanent failure while evaluating timestamp in PoE chain",
                ades_subindication=sub_indic
            )
        else:
            # neither pass nor fail => try past validation procedure
            assert isinstance(sub_indic, AdESIndeterminate)
            past_result = await ades_past_signature_validation(
                signed_data=poe.timestamp_token_signed_data,
                validation_spec=validation_spec,
                poe_manager=temporary_poes,
                current_time_sub_indic=sub_indic,
                init_control_time=cur_timing_info.validation_time,
            )
            if past_result.status == AdESStatus.PASSED:
                poe.add_to_poe_manager(resulting_poes)
            else:
                raise errors.SignatureValidationError(
                    "Could not validate timestamp in PoE chain at current "
                    "time, and past validation also failed",
                    ades_subindication=sub_indic
                )
    return resulting_poes


_LTA_FURTHER_PROC = frozenset({
    AdESPassed.OK,
    AdESIndeterminate.REVOKED_NO_POE,
    AdESIndeterminate.REVOKED_CA_NO_POE,
    AdESIndeterminate.OUT_OF_BOUNDS_NO_POE,
    AdESIndeterminate.OUT_OF_BOUNDS_NOT_REVOKED,
    AdESIndeterminate.CRYPTO_CONSTRAINTS_FAILURE_NO_POE,
    AdESIndeterminate.REVOCATION_OUT_OF_BOUNDS_NO_POE
})

_LTA_TS_FURTHER_PROC = frozenset({
    AdESIndeterminate.REVOKED_CA_NO_POE,
    AdESIndeterminate.OUT_OF_BOUNDS_NO_POE,
    AdESIndeterminate.OUT_OF_BOUNDS_NOT_REVOKED,
    AdESIndeterminate.CRYPTO_CONSTRAINTS_FAILURE_NO_POE,
    AdESIndeterminate.REVOCATION_OUT_OF_BOUNDS_NO_POE
})


@dataclass(frozen=True)
class AdESLTAValidationResult(AdESWithTimeValidationResult):
    """
    Result of a PAdES validation for a signature providing long-term
    availability and integrity of validation material.
    See ETSI EN 319 102-1, § 5.6.3.
    """

    oldest_evidence_record_timestamp: Optional[datetime]
    """
    The oldest timestamp in the evidence record, after validation.

    .. note::
        For PAdES, this refers to the chain of document timestamp signatures
        after signing.
    """

    signature_timestamp_status: Optional[AdESBasicValidationResult]
    """
    The validation result for the signature time stamp, if applicable.
    """


async def _process_signature_ts(
        embedded_sig: EmbeddedPdfSignature,
        validation_spec: SignatureValidationSpec,
        poe_manager: POEManager,
        timing_info: Optional[ValidationTimingInfo]) \
        -> Optional[AdESBasicValidationResult]:

    signature_bytes = embedded_sig.signer_info['signature'].native
    signature_ts: cms.SignedData = embedded_sig.attached_timestamp_data
    cert_validation_policy = (
        validation_spec.ts_cert_validation_policy
        or validation_spec.cert_validation_policy
    )
    algo_policy = cert_validation_policy.algorithm_usage_policy
    if signature_ts is None:
        return None

    signature_ts_prelim_result = await ades_timestamp_validation(
        tst_signed_data=signature_ts,
        validation_spec=validation_spec,
        timing_info=timing_info,
        expected_tst_imprint=embedded_sig.compute_tst_digest(),
        validation_data_handlers=bootstrap_validation_data_handlers(
            validation_spec, timing_info=timing_info,
            poe_manager_override=poe_manager
        )
    )

    ts_current_time_sub_indic = signature_ts_prelim_result.ades_subindic
    if isinstance(ts_current_time_sub_indic, AdESIndeterminate) and \
            ts_current_time_sub_indic in _LTA_TS_FURTHER_PROC:
        try:
            # TODO: in principle, we should also run this if the status is
            #  PASSED already. Ensure that that is possible.
            await _ades_past_signature_validation(
                signed_data=signature_ts,
                validation_spec=validation_spec,
                poe_manager=poe_manager,
                current_time_sub_indic=ts_current_time_sub_indic,
                init_control_time=timing_info.validation_time,
                is_timestamp=True
            )
            signature_ts_result = AdESBasicValidationResult(
                ades_subindic=AdESPassed.OK,
                # TODO update pyHanko status object as well
                api_status=signature_ts_prelim_result.api_status,
                failure_msg=None
            )
        except errors.SignatureValidationError as e:
            signature_ts_result = AdESBasicValidationResult(
                ades_subindic=e.ades_subindication,
                failure_msg=e.failure_message,
                api_status=signature_ts_prelim_result.api_status
            )
    else:
        signature_ts_result = signature_ts_prelim_result

    tst_info = signature_ts['encap_content_info']['content'].parsed
    if algo_policy.digest_algorithm_allowed(
            tst_info['message_imprint']['hash_algorithm'],
            moment=timing_info.validation_time
    ):
        signature_ts_dt = tst_info['gen_time'].native
        poe_manager.register(
            signature_bytes, signature_ts_dt
        )
    # TODO if/when we fully support signature policies, we should check
    #  whether the policy requires a valid signature timestamp
    return signature_ts_result


async def ades_lta_validation(
        embedded_sig: EmbeddedPdfSignature,
        pdf_validation_spec: PdfSignatureValidationSpec,
        timing_info: Optional[ValidationTimingInfo] = None,
        signature_not_before_time: Optional[datetime] = None) \
        -> AdESLTAValidationResult:
    """
    Validate a PAdES signature providing long-term availability and integrity
    of validation material. See ETSI EN 319 102-1, § 5.6.3.

    For the purposes of PAdES validation, the chain of document time stamps
    in the document serves as the unique Evidence Record (ER).

    :param embedded_sig:
        The PDF signature to validate.
    :param pdf_validation_spec:
        PDF signature validation settings.
    :param timing_info:
        Data object describing the timing of the validation.
        Defaults to :meth:`.ValidationTimingInfo.now`.
    :param signature_not_before_time:
        Time when the signature was known _not_ to exist.
    :return:
        A validation result.
    """

    timing_info = timing_info or ValidationTimingInfo.now(
        tz=tzlocal.get_localzone()
    )

    # (1) process DocTSes as ER
    poe_list = _build_prima_facie_poe_index_from_pdf_timestamps(
        embedded_sig.reader, include_content_ts=True,
        diff_policy=pdf_validation_spec.diff_policy
    )

    validation_spec = pdf_validation_spec.signature_validation_spec
    init_local_knowledge = validation_spec.local_knowledge
    # Ingest CRLs, certs and OCSPs from the DSS
    # (POE info will be processed separately)
    dss = DocumentSecurityStore.read_dss(embedded_sig.reader)
    dss_ocsps = [
        cont for resp in dss.ocsps
        for cont in OCSPContainer.load_multi(
            OCSPResponse.load(resp.get_object().data)
        )
    ]
    dss_crls = [
        CRLContainer(
            crl_data=CertificateList.load(crl.get_object().data)
        ) for crl in dss.crls
    ]
    dss_certs = list(dss.load_certs())
    local_knowledge = LocalKnowledge(
        known_ocsps=init_local_knowledge.known_ocsps + dss_ocsps,
        known_crls=init_local_knowledge.known_crls + dss_crls,
        known_certs=init_local_knowledge.known_certs + dss_certs,
        known_poes=init_local_knowledge.known_poes
    )
    augmented_validation_spec = dataclasses.replace(
        validation_spec, local_knowledge=local_knowledge
    )

    updated_poe_manager = None
    oldest_evidence_record_timestamp = None
    try:
        updated_poe_manager = await _validate_prima_facie_poe(
            poe_list,
            validation_spec=augmented_validation_spec,
            cur_timing_info=timing_info
        )
        # The POE list has been validated at this point,
        # so we just pick out the oldest one
        oldest_docts_record = min(
            filter(
                lambda poe: poe.pdf_revision > embedded_sig.signed_revision,
                poe_list,
            ),
            key=lambda poe: poe.pdf_revision,
            default=None
        )
        if oldest_docts_record is not None:
            oldest_evidence_record_timestamp = oldest_docts_record.timestamp_dt
        else:
            logger.warning(
                "No document timestamps after signature; proceeding "
                "without past proof of existence"
            )
    except errors.SignatureValidationError as e:
        logger.warning(
            "Document timestamp chain failed to validate; proceeding "
            "without past proof of existence.",
            exc_info=e
        )
    if oldest_evidence_record_timestamp is None:
        updated_poe_manager = POEManager()
        local_knowledge.add_to_poe_manager(updated_poe_manager)

    assert updated_poe_manager is not None

    # (2) skipped, is automatic in our implementation

    # (3) Run validation for signatures with time

    with_time_data_handlers = bootstrap_validation_data_handlers(
        spec=augmented_validation_spec,
        timing_info=timing_info,
        poe_manager_override=updated_poe_manager
    )
    signature_prelim_result = await ades_with_time_validation(
        signed_data=embedded_sig.signed_data,
        validation_spec=augmented_validation_spec,
        timing_info=timing_info,
        validation_data_handlers=with_time_data_handlers,
        raw_digest=embedded_sig.compute_digest(),
        signature_not_before_time=signature_not_before_time,
        extra_status_kwargs={'diff_result': embedded_sig.diff_result},
        status_cls=PdfSignatureStatus
    )

    # don't branch on policy here, we always continue as if archival info
    # is present
    current_time_sub_indic = signature_prelim_result.ades_subindic
    if current_time_sub_indic not in _LTA_FURTHER_PROC:
        failure_msg = (
            "Validation of signature at current time failed with "
            f"indication {current_time_sub_indic}. Past validation not "
            f"applicable."
        )
        return AdESLTAValidationResult(
            ades_subindic=current_time_sub_indic,
            api_status=signature_prelim_result.api_status,
            failure_msg=failure_msg,
            best_signature_time=signature_prelim_result.best_signature_time,
            signature_not_before_time=(
                signature_prelim_result.signature_not_before_time
            ),
            oldest_evidence_record_timestamp=(
                oldest_evidence_record_timestamp
            ),
            signature_timestamp_status=None
        )

    # (4) Register PoE for the signature based on best_signature_time
    signature_bytes = embedded_sig.signer_info['signature'].native
    updated_poe_manager.register(
        signature_bytes, signature_prelim_result.best_signature_time
    )

    # (5) process signature TS if present
    signature_ts_result = await _process_signature_ts(
        embedded_sig,
        validation_spec=augmented_validation_spec,
        poe_manager=updated_poe_manager,
        timing_info=timing_info
    )

    # (6) past signature validation
    if isinstance(current_time_sub_indic, AdESIndeterminate):
        # TODO: in principle, we should also run this if the status is PASSED
        #  already. Ensure that that is possible.
        try:
            await _ades_past_signature_validation(
                signed_data=embedded_sig.signed_data,
                validation_spec=augmented_validation_spec,
                poe_manager=updated_poe_manager,
                current_time_sub_indic=current_time_sub_indic,
                init_control_time=timing_info.validation_time,
                is_timestamp=False
            )
        except errors.SignatureValidationError as e:
            sig_poe = updated_poe_manager[signature_bytes]
            return AdESLTAValidationResult(
                ades_subindic=e.ades_subindication,
                failure_msg=e.failure_message,
                # FIXME rewrite api_status!
                api_status=signature_prelim_result.api_status,
                best_signature_time=sig_poe,
                signature_not_before_time=(
                    signature_prelim_result.signature_not_before_time
                ),
                signature_timestamp_status=signature_ts_result,
                oldest_evidence_record_timestamp=(
                    oldest_evidence_record_timestamp
                )
            )

    # (7) get the oldest PoE for the signature
    signature_poe_time = updated_poe_manager[signature_bytes]

    # (8) perform SVA (=> only crypto checks)
    algo_policy = augmented_validation_spec\
        .cert_validation_policy.algorithm_usage_policy
    try:
        cert: x509.Certificate = embedded_sig.signer_cert
        _ades_signature_crypto_policy_check(
            embedded_sig.signer_info,
            algo_policy=algo_policy,
            control_time=signature_poe_time,
            public_key=cert.public_key
        )
        ades_subindic = AdESPassed.OK
        failure_msg = None
    except errors.SignatureValidationError as e:
        ades_subindic = e.ades_subindication
        failure_msg = e.failure_message

    return AdESLTAValidationResult(
        ades_subindic=ades_subindic,
        api_status=signature_prelim_result.api_status,
        failure_msg=failure_msg,
        best_signature_time=signature_poe_time,
        signature_not_before_time=(
            signature_prelim_result.signature_not_before_time
        ),
        signature_timestamp_status=signature_ts_result,
        oldest_evidence_record_timestamp=(
            oldest_evidence_record_timestamp
        )
    )
