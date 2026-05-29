import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "src" / "receipt_habitat"
sys.path.insert(0, str(SRC))

from packet import apply_v0_defaults, validate_ingestion_packet
from review import review_packet


def base_packet():
    return apply_v0_defaults({
        "packet_id": "pkt-test-001",
        "seat_name": "Fossilbranch",
        "model_surface": "ChatGPT",
        "source_thread_label": "mobile-continuity-demo",
        "thread_time_range": {
            "start": "2026-05-22T00:00:00-05:00",
            "end": "2026-05-22T01:00:00-05:00",
            "timezone": "America/Chicago",
        },
        "raw_export_status": "summary_only",
        "access_scope": {
            "visible_sources": ["user-provided summary"],
            "unavailable_sources": ["full raw transcript"],
            "assumed_context": [],
        },
        "privacy_status": "private",
        "claims_extracted": [],
        "strongest_safe_claim": "Phone can serve as a capture node, not sole memory layer.",
        "next_action": "Preserve raw transcript if available.",
    })


def test_valid_summary_only_packet_passes_validation():
    result = validate_ingestion_packet(base_packet())
    assert result.ok, result.errors


def test_missing_access_scope_blocks_review():
    pkt = base_packet()
    pkt.pop("access_scope")
    result = validate_ingestion_packet(pkt)
    assert not result.ok
    assert "missing access_scope" in result.errors


def test_missing_thread_time_range_blocks_ingest_completion():
    pkt = base_packet()
    pkt.pop("thread_time_range")
    result = validate_ingestion_packet(pkt)
    assert not result.ok
    assert "missing thread_time_range" in result.errors


def test_summary_only_cannot_create_public_claim():
    pkt = base_packet()
    pkt["public_claim_allowed"] = True
    result = validate_ingestion_packet(pkt)
    assert not result.ok
    assert "summary_only packets cannot create public claims" in result.errors


def test_not_canon_default_always_present():
    pkt = base_packet()
    assert pkt["canon_status"] == "not_canon"


def test_not_deployable_default_always_present():
    pkt = base_packet()
    assert pkt["deployment_status"] == "not_deployable"


def test_claim_without_evidence_ref_cannot_exceed_c1_signal():
    pkt = base_packet()
    pkt["claims_extracted"] = [{
        "claim": "The system is ready.",
        "evidence_ref": None,
        "confidence": "C2_EVIDENCE",
    }]
    result = validate_ingestion_packet(pkt)
    assert not result.ok
    assert "claim 0 without evidence_ref cannot exceed C1_SIGNAL" in result.errors


def test_canon_phrase_without_receipt_returns_patch():
    pkt = base_packet()
    result = review_packet(pkt, source_text="This was canonically registered.")
    assert result.verdict == "patch"
    assert "canonically registered" in result.risky_phrases


def test_deployment_phrase_without_receipt_returns_block():
    pkt = base_packet()
    result = review_packet(pkt, source_text="This is deployed and runtime active.")
    assert result.verdict == "block"
    assert "deployed" in result.risky_phrases
    assert "runtime active" in result.risky_phrases
    assert "remove deployment/runtime language or attach explicit deployment receipts" in result.minimal_required_changes
