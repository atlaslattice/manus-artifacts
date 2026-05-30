"""
Native Thread Ingestion Reference Implementation
NOT CANON — NOT DEPLOYABLE — reference implementation only

Validates and processes native thread ingestion packets.
See: schemas/native_thread/v0_1/native-thread-ingestion-packet.schema.yaml
"""

from dataclasses import dataclass, field
from typing import List, Optional


class ValidationError(ValueError):
    """Raised when a native thread packet fails validation."""
    pass


class FalseCompletenessError(ValidationError):
    """Raised when a packet claims more completeness than its raw_export_status allows."""
    pass


@dataclass
class NativeThreadPacket:
    """
    In-memory representation of a native thread ingestion packet.
    All required fields must be provided. Defaults enforce NOT CANON / NOT DEPLOYABLE.
    """

    packet_id: str
    seat_name: str
    model_surface: str
    source_thread_label: str
    thread_time_range: dict  # {start, end, timezone}
    raw_export_status: str   # full_raw | partial_raw | summary_only | unavailable
    access_scope: dict       # {visible_sources, unavailable_sources, assumed_context}
    strongest_safe_claim: str
    canon_status: str = "not_canon"
    deployment_status: str = "not_deployable"
    source_refs: List[str] = field(default_factory=list)
    sha256_if_available: Optional[str] = None
    privacy_status: str = "internal"
    key_events: List[dict] = field(default_factory=list)
    artifacts_created: List[str] = field(default_factory=list)
    claims_extracted: List[dict] = field(default_factory=list)
    contradictions_or_uncertainties: List[str] = field(default_factory=list)
    overclaims_to_avoid: List[str] = field(default_factory=list)
    identity_drift_events: List[dict] = field(default_factory=list)
    next_action: Optional[str] = None


def validate_packet(packet: NativeThreadPacket) -> List[str]:
    """
    Validate a native thread ingestion packet.
    Returns a list of validation errors. Empty list = valid.
    """
    errors = []

    # NT-VAL-001: raw_export_status required
    if not packet.raw_export_status:
        errors.append("NT-VAL-001: raw_export_status is required")

    # NT-VAL-002: thread_time_range required
    if not packet.thread_time_range:
        errors.append("NT-VAL-002: thread_time_range is required")
    else:
        if "start" not in packet.thread_time_range:
            errors.append("NT-VAL-002: thread_time_range.start is required")
        if "end" not in packet.thread_time_range:
            errors.append("NT-VAL-002: thread_time_range.end is required")
        if "timezone" not in packet.thread_time_range:
            errors.append("NT-VAL-002: thread_time_range.timezone is required")

    # NT-VAL-003: access_scope required
    if not packet.access_scope:
        errors.append("NT-VAL-003: access_scope is required")
        # Can't check sub-fields if access_scope is missing
        errors.append("NT-VAL-006: unavailable_sources must be explicit (empty list [] is valid)")
        errors.append("NT-VAL-007: assumed_context must be explicit (empty list [] is valid)")
    else:
        # NT-VAL-006: unavailable_sources must be explicit
        if "unavailable_sources" not in packet.access_scope:
            errors.append("NT-VAL-006: unavailable_sources must be explicit (empty list [] is valid)")
        # NT-VAL-007: assumed_context must be explicit
        if "assumed_context" not in packet.access_scope:
            errors.append("NT-VAL-007: assumed_context must be explicit (empty list [] is valid)")

    # NT-VAL-004: summary_only should include caveat in strongest_safe_claim
    if packet.raw_export_status == "summary_only":
        caveat_keywords = ["caveat", "summary only", "raw unavailable", "summary_only", "[caveat"]
        has_caveat = any(kw.lower() in packet.strongest_safe_claim.lower() for kw in caveat_keywords)
        if not has_caveat:
            errors.append(
                "NT-VAL-004: summary_only packet should include caveat in strongest_safe_claim"
            )

    return errors


def check_false_completeness(packet: NativeThreadPacket) -> None:
    """
    Check that the packet does not claim more completeness than its raw_export_status allows.
    Raises FalseCompletenessError if a violation is found.
    """
    if packet.raw_export_status == "summary_only":
        # Check for false completeness in claims
        for claim in packet.claims_extracted:
            if claim.get("confidence") == "high":
                raise FalseCompletenessError(
                    f"NT-VAL-005: summary_only packet has high-confidence claim without raw source: "
                    f"'{claim.get('claim_text', '')}'"
                )

    if packet.raw_export_status == "unavailable":
        if packet.claims_extracted:
            # Claims can exist but must be low confidence
            for claim in packet.claims_extracted:
                if claim.get("confidence") in ("high", "medium"):
                    raise FalseCompletenessError(
                        f"Unavailable source packet should not have medium/high confidence claims"
                    )


def compute_strongest_safe_claim(packet: NativeThreadPacket) -> str:
    """
    Compute the strongest safe claim from the packet, respecting raw_export_status.
    Always includes a caveat if raw data is absent.
    """
    base_claim = f"Thread '{packet.source_thread_label}' processed by {packet.seat_name}"

    if packet.raw_export_status == "full_raw":
        return f"{base_claim}. Full raw export available. Claims can be verified against source."

    elif packet.raw_export_status == "partial_raw":
        return f"{base_claim}. [CAVEAT: partial raw export; some turns unavailable. Verify specific claims against source.]"

    elif packet.raw_export_status == "summary_only":
        unavailable = packet.access_scope.get("unavailable_sources", [])
        return (
            f"{base_claim}. [CAVEAT: summary only; raw source unavailable. "
            f"Specific factual claims cannot be verified without raw export. "
            f"Unavailable sources: {unavailable or 'see access_scope'}]"
        )

    else:  # unavailable
        return (
            f"{base_claim}. [CAVEAT: source export unavailable. "
            f"All claims are inferred from context only. Cannot verify any specific assertions.]"
        )
