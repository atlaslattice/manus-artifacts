"""Packet validation for Receipt Habitat v0.1.

Local dry-run only. Defaults preserve non-canon and non-deployable status.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

ALLOWED_RAW_STATUS = {"full_raw", "partial_raw", "summary_only", "unavailable"}
ALLOWED_PRIVACY = {"public", "private", "mixed", "redacted"}
MAX_CONFIDENCE_WITHOUT_EVIDENCE = {"C0_UNSUPPORTED", "C1_SIGNAL"}


class ValidationError(ValueError):
    pass


@dataclass
class PacketValidationResult:
    ok: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def validate_ingestion_packet(packet: dict[str, Any]) -> PacketValidationResult:
    """Validate minimal native_thread_ingestion_packet.v0.1 constraints."""
    errors: list[str] = []
    warnings: list[str] = []

    require(bool(packet.get("raw_export_status")), "missing raw_export_status", errors)
    require(packet.get("raw_export_status") in ALLOWED_RAW_STATUS, "invalid raw_export_status", errors)

    tr = packet.get("thread_time_range")
    require(isinstance(tr, dict), "missing thread_time_range", errors)
    if isinstance(tr, dict):
        for key in ("start", "end", "timezone"):
            require(bool(tr.get(key)), f"missing thread_time_range.{key}", errors)

    scope = packet.get("access_scope")
    require(isinstance(scope, dict), "missing access_scope", errors)
    if isinstance(scope, dict):
        for key in ("visible_sources", "unavailable_sources", "assumed_context"):
            require(key in scope, f"missing access_scope.{key}", errors)
        if packet.get("raw_export_status") == "unavailable" and not scope.get("unavailable_sources"):
            errors.append("unavailable raw exports must list unavailable_sources")

    require(packet.get("canon_status", "not_canon") == "not_canon", "canon_status must be not_canon", errors)
    require(packet.get("deployment_status", "not_deployable") == "not_deployable", "deployment_status must be not_deployable", errors)

    privacy = packet.get("privacy_status")
    require(privacy in ALLOWED_PRIVACY, "invalid or missing privacy_status", errors)

    for idx, claim in enumerate(packet.get("claims_extracted", []) or []):
        evidence_ref = claim.get("evidence_ref") if isinstance(claim, dict) else None
        confidence = claim.get("confidence") if isinstance(claim, dict) else None
        if not evidence_ref and confidence not in MAX_CONFIDENCE_WITHOUT_EVIDENCE:
            errors.append(f"claim {idx} without evidence_ref cannot exceed C1_SIGNAL")

    if packet.get("raw_export_status") == "summary_only" and packet.get("public_claim_allowed") is True:
        errors.append("summary_only packets cannot create public claims")

    return PacketValidationResult(ok=not errors, errors=errors, warnings=warnings)


def apply_v0_defaults(packet: dict[str, Any]) -> dict[str, Any]:
    """Apply safe v0.1 defaults."""
    out = dict(packet)
    out.setdefault("canon_status", "not_canon")
    out.setdefault("deployment_status", "not_deployable")
    out.setdefault("authority_scope", "none")
    out.setdefault("runtime_status", "local_dry_run_only")
    return out
