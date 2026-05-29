"""
Candidate validation tests for Notion mirror root packets.

STATUS: CANDIDATE TESTS — NOT CANON — NOT DEPLOYABLE
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid_mirrored_root_packet() -> dict:
    return {
        "source_id": "notion-root-001",
        "title": "Candidate source root",
        "source_url": "https://notion.example.invalid/source-root",
        "raw_export_pointer": None,
        "raw_export_status": "not_exported",
        "access_scope": "unknown",
        "canon_status": "not_canon",
        "deployment_status": "not_deployable",
        "authority": "none",
        "claims": [],
        "ratification_event_id": None,
    }


def missing_raw_export_status_fixture() -> dict:
    packet = valid_mirrored_root_packet()
    packet.pop("raw_export_status")
    return packet


def missing_access_scope_fixture() -> dict:
    packet = valid_mirrored_root_packet()
    packet.pop("access_scope")
    return packet


def summary_only_claiming_source_completeness_fixture() -> dict:
    packet = valid_mirrored_root_packet()
    packet["raw_export_status"] = "summary_only"
    packet["claims"] = ["This summary is source complete."]
    return packet


def stale_canon_language_fixture() -> dict:
    packet = valid_mirrored_root_packet()
    packet["claims"] = ["This legacy Notion page is canon."]
    return packet


def unsupported_authority_claim_fixture() -> dict:
    packet = valid_mirrored_root_packet()
    packet["authority"] = "approved"
    packet["claims"] = ["Approved by location in Notion."]
    return packet


def validate_root_packet(packet: dict) -> list[str]:
    errors: list[str] = []
    for field in ("raw_export_status", "access_scope"):
        if field not in packet:
            errors.append(f"missing required field: {field}")

    if packet.get("canon_status") != "not_canon":
        errors.append("canon_status must remain not_canon")
    if packet.get("deployment_status") != "not_deployable":
        errors.append("deployment_status must remain not_deployable")
    if not (packet.get("source_url") or packet.get("raw_export_pointer")):
        errors.append("source URL or raw export pointer is required")
    if packet.get("canon_status") == "ratified" and not packet.get("ratification_event_id"):
        errors.append("ratification requires ratification_event_id")

    claim_text = " ".join(str(claim).lower() for claim in packet.get("claims", []))
    if packet.get("raw_export_status") == "summary_only" and "source complete" in claim_text:
        errors.append("summary-only packet cannot claim source completeness")
    if "is canon" in claim_text or "canon." in claim_text:
        errors.append("stale or unsupported canon language requires review")
    if packet.get("authority") not in {None, "none", "candidate_only"}:
        errors.append("unsupported authority claim")
    return errors


def test_required_candidate_artifacts_exist() -> None:
    required = [
        ROOT / "archive/notion_mirror/NOTION_SOURCE_ROOT_INVENTORY_v0.1.yaml",
        ROOT / "archive/notion_mirror/NOTION_TO_GITHUB_MIRROR_PROTOCOL_v0.1.md",
        ROOT / "archive/notion_mirror/NOTION_GITHUB_SYNC_DOCKET_v0.1.yaml",
        ROOT / "archive/notion_mirror/NOTION_CONTAMINATION_RULESET_v0.1.md",
        ROOT / "archive/knowledge_graph/lattice_kg/v0_5/SOURCE_GROUNDED_KNOWLEDGE_GRAPH_SCHEMA_v0.1.yaml",
        ROOT / "archive/knowledge_graph/lattice_kg/v0_5/lattice_ontology_v0.5.yaml",
        ROOT / "archive/knowledge_graph/lattice_kg/v0_5/TIDELOCK_HANDOFF_PACKET_SCHEMA_v0.1.yaml",
    ]
    for path in required:
        assert path.exists(), f"missing file: {path}"
        text = path.read_text(encoding="utf-8")
        assert "CANON: no" in text or "canon_status: not_canon" in text
        assert "DEPLOYMENT: no" in text or "deployment_status: not_deployable" in text


def test_valid_root_packet_passes_local_guardrails() -> None:
    assert validate_root_packet(valid_mirrored_root_packet()) == []


def test_missing_raw_export_status_fails() -> None:
    errors = validate_root_packet(missing_raw_export_status_fixture())
    assert "missing required field: raw_export_status" in errors


def test_missing_access_scope_fails() -> None:
    errors = validate_root_packet(missing_access_scope_fixture())
    assert "missing required field: access_scope" in errors


def test_summary_only_cannot_claim_source_completeness() -> None:
    errors = validate_root_packet(summary_only_claiming_source_completeness_fixture())
    assert "summary-only packet cannot claim source completeness" in errors


def test_stale_canon_language_fails_review_gate() -> None:
    errors = validate_root_packet(stale_canon_language_fixture())
    assert "stale or unsupported canon language requires review" in errors


def test_unsupported_authority_claim_fails() -> None:
    errors = validate_root_packet(unsupported_authority_claim_fixture())
    assert "unsupported authority claim" in errors


def test_requires_source_url_or_raw_export_pointer() -> None:
    packet = valid_mirrored_root_packet()
    packet["source_url"] = None
    packet["raw_export_pointer"] = None
    assert "source URL or raw export pointer is required" in validate_root_packet(packet)


def test_blocks_ratification_without_event() -> None:
    packet = valid_mirrored_root_packet()
    packet["canon_status"] = "ratified"
    packet["ratification_event_id"] = None
    errors = validate_root_packet(packet)
    assert "canon_status must remain not_canon" in errors
    assert "ratification requires ratification_event_id" in errors
