"""
Native Thread Ingestion — validator and packet builder.

STATUS: CANDIDATE IMPLEMENTATION — NOT CANON
DEPLOYMENT: NOT DEPLOYABLE
AUTHORITY: NONE
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional


RAW_EXPORT_VALUES = {"full_raw", "partial_raw", "summary_only", "unavailable"}
SUMMARY_STATUSES = {"summary_only", "unavailable"}


@dataclass
class ThreadTimeRange:
    start: str
    end: str
    timezone: str


@dataclass
class AccessScope:
    visible_sources: List[str]
    unavailable_sources: List[str]
    assumed_context: List[str]


@dataclass
class NativeThreadIngestionPacket:
    """Native thread ingestion packet for Children of the Swarm."""
    seat_name: str
    model_surface: str
    thread_time_range: ThreadTimeRange
    raw_export_status: str
    access_scope: AccessScope

    source_thread_label: Optional[str] = None
    source_refs: List[str] = field(default_factory=list)
    sha256_if_available: Optional[str] = None
    privacy_status: Optional[str] = None

    key_events: List[str] = field(default_factory=list)
    artifacts_created: List[str] = field(default_factory=list)
    claims_extracted: List[str] = field(default_factory=list)
    contradictions_or_uncertainties: List[str] = field(default_factory=list)
    overclaims_to_avoid: List[str] = field(default_factory=list)
    identity_drift_events: List[str] = field(default_factory=list)

    canon_status: str = "not_canon"
    deployment_status: str = "not_deployable"
    strongest_safe_claim: Optional[str] = None
    next_action: Optional[str] = None


class ValidationError(ValueError):
    pass


def validate_packet(packet: NativeThreadIngestionPacket) -> List[str]:
    """
    Validate a native thread ingestion packet.
    Returns list of error strings (empty = valid).
    """
    errors: List[str] = []

    # C-NT-1: raw_export_status required
    if not packet.raw_export_status:
        errors.append("C-NT-1: raw_export_status is required")
    elif packet.raw_export_status not in RAW_EXPORT_VALUES:
        errors.append(
            f"C-NT-1: raw_export_status must be one of {RAW_EXPORT_VALUES}"
        )

    # C-NT-2: thread_time_range required
    if packet.thread_time_range is None:
        errors.append("C-NT-2: thread_time_range is required")
    else:
        ttr = packet.thread_time_range
        if not ttr.start:
            errors.append("C-NT-2: thread_time_range.start is required")
        if not ttr.end:
            errors.append("C-NT-2: thread_time_range.end is required")
        if not ttr.timezone:
            errors.append("C-NT-2: thread_time_range.timezone is required")

    # C-NT-3: access_scope required
    if packet.access_scope is None:
        errors.append("C-NT-3: access_scope is required")
    else:
        scope = packet.access_scope
        # C-NT-5: unavailable_sources must be explicit (not None)
        if scope.unavailable_sources is None:
            errors.append("C-NT-5: access_scope.unavailable_sources must be explicit (use [] if empty)")
        # C-NT-6: assumed_context must be explicit
        if scope.assumed_context is None:
            errors.append("C-NT-6: access_scope.assumed_context must be explicit (use [] if empty)")

    # C-NT-4: summary_only cannot claim full ingestion
    # C-NT-7: strongest_safe_claim with caveat required when raw absent
    if packet.raw_export_status in SUMMARY_STATUSES:
        if not packet.strongest_safe_claim:
            errors.append(
                "C-NT-7: strongest_safe_claim is required when raw_export_status "
                f"is '{packet.raw_export_status}'"
            )
        elif "caveat" not in packet.strongest_safe_claim.lower() and \
             "cannot" not in packet.strongest_safe_claim.lower() and \
             "summary" not in packet.strongest_safe_claim.lower() and \
             "partial" not in packet.strongest_safe_claim.lower():
            errors.append(
                "C-NT-4/C-NT-7: strongest_safe_claim must include explicit caveat "
                "when raw_export_status is summary_only or unavailable"
            )

    return errors


def build_packet_with_caveat(
    seat_name: str,
    model_surface: str,
    raw_export_status: str,
    thread_time_range: ThreadTimeRange,
    access_scope: AccessScope,
    claims: Optional[List[str]] = None,
    **kwargs,
) -> NativeThreadIngestionPacket:
    """
    Build a packet, automatically attaching caveat to strongest_safe_claim
    when raw is absent.
    """
    strongest = kwargs.pop("strongest_safe_claim", None)
    if raw_export_status in SUMMARY_STATUSES:
        caveat = (
            f"[CAVEAT: raw_export_status={raw_export_status}; "
            "source completeness cannot be verified] "
        )
        strongest = caveat + (strongest or "Claims based on summary only.")

    return NativeThreadIngestionPacket(
        seat_name=seat_name,
        model_surface=model_surface,
        raw_export_status=raw_export_status,
        thread_time_range=thread_time_range,
        access_scope=access_scope,
        claims_extracted=claims or [],
        strongest_safe_claim=strongest,
        **kwargs,
    )
