import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "src" / "receipt_habitat"
sys.path.insert(0, str(SRC))

from graph import packet_to_graph_candidate
from packet import apply_v0_defaults


def base_packet():
    return apply_v0_defaults({
        "packet_id": "pkt-graph-001",
        "seat_name": "Fossilbranch",
        "model_surface": "ChatGPT",
        "source_thread_label": "mobile-continuity-demo",
        "thread_time_range": {
            "start": "2026-05-28T00:00:00-05:00",
            "end": "2026-05-28T01:00:00-05:00",
            "timezone": "America/Chicago",
        },
        "raw_export_status": "summary_only",
        "access_scope": {
            "visible_sources": ["examples/mobile_continuity_summary.md"],
            "unavailable_sources": ["full raw transcript"],
            "assumed_context": [],
        },
        "source_refs": ["examples/mobile_continuity_summary.md"],
        "sha256_if_available": "abc123",
        "privacy_status": "private",
        "claims_extracted": [
            {
                "claim": "Phone can serve as a capture node.",
                "evidence_ref": "examples/mobile_continuity_summary.md",
                "confidence": "C2_EVIDENCE",
            }
        ],
        "contradictions_or_uncertainties": [],
        "overclaims_to_avoid": ["canon", "deployment"],
        "strongest_safe_claim": "Phone can serve as a capture node, not sole memory layer.",
        "next_action": "Review packet before synthesis or routing.",
        "public_claim_allowed": False,
    })


def test_packet_to_graph_candidate_emits_candidate_only():
    result = packet_to_graph_candidate(base_packet())
    assert result.ok, result.errors
    candidate = result.candidate
    assert candidate["canon_status"] == "not_canon"
    assert candidate["deployment_status"] == "not_deployed"
    assert candidate["authority_scope"] == "none"
    assert candidate["generated_by"] == "Receipt Habitat v0.1"


def test_candidate_nodes_are_non_authoritative():
    candidate = packet_to_graph_candidate(base_packet()).candidate
    for node in candidate["proposed_nodes"]:
        assert node["status"] == "candidate"
        assert node["canon_status"] == "not_canon"
        assert node["deployment_status"] == "not_deployed"
        assert node["authority_scope"] == "none"


def test_summary_only_packet_marks_full_raw_missing():
    candidate = packet_to_graph_candidate(base_packet()).candidate
    assert "full_raw_export" in candidate["missing_receipts"]


def test_claim_without_evidence_routes_missing_receipt():
    packet = base_packet()
    packet["claims_extracted"] = [
        {
            "claim": "A claim without a receipt.",
            "evidence_ref": None,
            "confidence": "C1_SIGNAL",
        }
    ]
    candidate = packet_to_graph_candidate(packet).candidate
    assert "claim_0_evidence_ref" in candidate["missing_receipts"]
    assert "Hashlight" in candidate["review_required"]


def test_invalid_packet_blocks_graph_candidate():
    packet = base_packet()
    packet.pop("access_scope")
    result = packet_to_graph_candidate(packet)
    assert not result.ok
    assert result.candidate is None
    assert "missing access_scope" in result.errors
