"""
Candidate Notion mirror packet validation.

NOT CANON — NOT DEPLOYABLE.
Bad mirror packets must fail safely before they are treated as source-complete,
ratified, or deployable.
"""

from __future__ import annotations

import re
from typing import Any

import pytest


class MirrorPacketValidationError(ValueError):
    """Actionable validation error for unsafe mirror packets."""


STALE_CANON_PATTERNS = (
    re.compile(r"\bsource of truth\b", re.IGNORECASE),
    re.compile(r"\bcanonical\b", re.IGNORECASE),
    re.compile(r"\bratified\b", re.IGNORECASE),
)

UNSUPPORTED_AUTHORITY_PATTERNS = (
    re.compile(r"\bapproved by title\b", re.IGNORECASE),
    re.compile(r"\bauthoritative because it is in notion\b", re.IGNORECASE),
    re.compile(r"\bgithub mirror makes this canon\b", re.IGNORECASE),
)


def validate_root_packet(packet: dict[str, Any]) -> None:
    """Validate a candidate mirrored root packet with no authority promotion."""
    required_fields = (
        "packet_id",
        "title",
        "canon_status",
        "deployment_status",
        "raw_export_status",
        "access_scope",
    )
    missing = [field for field in required_fields if field not in packet]
    if missing:
        raise MirrorPacketValidationError(f"missing required fields: {', '.join(missing)}")

    if packet["canon_status"] != "not_canon":
        raise MirrorPacketValidationError("canon_status must be not_canon")

    if packet["deployment_status"] != "not_deployable":
        raise MirrorPacketValidationError("deployment_status must be not_deployable")

    has_source_url = bool(packet.get("source_url"))
    has_raw_pointer = bool(packet.get("raw_export_pointer"))
    if not (has_source_url or has_raw_pointer):
        raise MirrorPacketValidationError("packet requires source_url or raw_export_pointer")

    access_scope = packet["access_scope"]
    if not isinstance(access_scope, dict):
        raise MirrorPacketValidationError("access_scope must describe visible and unavailable sources")

    if packet.get("ratification_event_id") is None and packet.get("orcs_state") == "ratified":
        raise MirrorPacketValidationError("ratified state requires ratification_event_id")

    content = "\n".join(
        str(packet.get(field, ""))
        for field in ("title", "summary", "authority_claim", "notes")
    )
    if packet["raw_export_status"] == "summary_only" and re.search(
        r"\b(complete|all sources|source completeness)\b", content, re.IGNORECASE
    ):
        raise MirrorPacketValidationError("summary_only packet cannot claim source completeness")

    for pattern in STALE_CANON_PATTERNS:
        if pattern.search(content):
            raise MirrorPacketValidationError("stale canon language must be quarantined or reviewed")

    for pattern in UNSUPPORTED_AUTHORITY_PATTERNS:
        if pattern.search(content):
            raise MirrorPacketValidationError("unsupported authority claim must be rejected")


@pytest.fixture
def valid_mirrored_root_packet() -> dict[str, Any]:
    return {
        "packet_id": "notion-root-valid-v0-1",
        "title": "Candidate Notion Root",
        "source_url": "https://www.notion.so/example",
        "raw_export_pointer": None,
        "canon_status": "not_canon",
        "deployment_status": "not_deployable",
        "raw_export_status": "discovered_not_fetched",
        "access_scope": {
            "visible_sources": ["title", "url"],
            "unavailable_sources": ["full page content"],
            "assumed_context": [],
        },
        "orcs_state": "raw",
        "claims_requiring_verification": ["full page content not yet fetched"],
    }


@pytest.fixture
def missing_raw_export_status(valid_mirrored_root_packet: dict[str, Any]) -> dict[str, Any]:
    packet = dict(valid_mirrored_root_packet)
    packet.pop("raw_export_status")
    return packet


@pytest.fixture
def missing_access_scope(valid_mirrored_root_packet: dict[str, Any]) -> dict[str, Any]:
    packet = dict(valid_mirrored_root_packet)
    packet.pop("access_scope")
    return packet


@pytest.fixture
def summary_only_claiming_source_completeness(
    valid_mirrored_root_packet: dict[str, Any],
) -> dict[str, Any]:
    packet = dict(valid_mirrored_root_packet)
    packet.update(
        {
            "raw_export_status": "summary_only",
            "summary": "This summary captures all sources and is complete.",
        }
    )
    return packet


@pytest.fixture
def stale_canon_language(valid_mirrored_root_packet: dict[str, Any]) -> dict[str, Any]:
    packet = dict(valid_mirrored_root_packet)
    packet["notes"] = "Legacy note calls this the source of truth."
    return packet


@pytest.fixture
def unsupported_authority_claim(valid_mirrored_root_packet: dict[str, Any]) -> dict[str, Any]:
    packet = dict(valid_mirrored_root_packet)
    packet["authority_claim"] = "Authoritative because it is in Notion."
    return packet


def test_valid_mirrored_root_packet_passes(valid_mirrored_root_packet: dict[str, Any]) -> None:
    validate_root_packet(valid_mirrored_root_packet)


def test_missing_raw_export_status_fails(missing_raw_export_status: dict[str, Any]) -> None:
    with pytest.raises(MirrorPacketValidationError, match="raw_export_status"):
        validate_root_packet(missing_raw_export_status)


def test_missing_access_scope_fails(missing_access_scope: dict[str, Any]) -> None:
    with pytest.raises(MirrorPacketValidationError, match="access_scope"):
        validate_root_packet(missing_access_scope)


def test_summary_only_claiming_source_completeness_fails(
    summary_only_claiming_source_completeness: dict[str, Any],
) -> None:
    with pytest.raises(MirrorPacketValidationError, match="source completeness"):
        validate_root_packet(summary_only_claiming_source_completeness)


def test_stale_canon_language_fails(stale_canon_language: dict[str, Any]) -> None:
    with pytest.raises(MirrorPacketValidationError, match="stale canon"):
        validate_root_packet(stale_canon_language)


def test_unsupported_authority_claim_fails(unsupported_authority_claim: dict[str, Any]) -> None:
    with pytest.raises(MirrorPacketValidationError, match="unsupported authority"):
        validate_root_packet(unsupported_authority_claim)


def test_non_not_canon_status_fails(valid_mirrored_root_packet: dict[str, Any]) -> None:
    packet = dict(valid_mirrored_root_packet)
    packet["canon_status"] = "ratified_canon"
    with pytest.raises(MirrorPacketValidationError, match="canon_status"):
        validate_root_packet(packet)


def test_non_not_deployable_status_fails(valid_mirrored_root_packet: dict[str, Any]) -> None:
    packet = dict(valid_mirrored_root_packet)
    packet["deployment_status"] = "deployable"
    with pytest.raises(MirrorPacketValidationError, match="deployment_status"):
        validate_root_packet(packet)


def test_source_url_or_raw_export_pointer_required(
    valid_mirrored_root_packet: dict[str, Any],
) -> None:
    packet = dict(valid_mirrored_root_packet)
    packet["source_url"] = None
    packet["raw_export_pointer"] = None
    with pytest.raises(MirrorPacketValidationError, match="source_url or raw_export_pointer"):
        validate_root_packet(packet)


def test_ratification_requires_ratification_event(
    valid_mirrored_root_packet: dict[str, Any],
) -> None:
    packet = dict(valid_mirrored_root_packet)
    packet["orcs_state"] = "ratified"
    packet["ratification_event_id"] = None
    with pytest.raises(MirrorPacketValidationError, match="ratification_event_id"):
        validate_root_packet(packet)
