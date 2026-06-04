import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "src" / "receipt_habitat"
sys.path.insert(0, str(SRC))

from artifact_card import artifact_card_to_markdown, build_artifact_card


def graph_candidate():
    return {
        "candidate_id": "gwc-test-001",
        "generated_by": "Receipt Habitat v0.1",
        "source_packet_id": "pkt-test-001",
        "source_artifacts": ["https://drive.google.com/file/d/example"],
        "proposed_nodes": [
            {
                "node_id": "source-001",
                "node_type": "SourceArtifact",
                "title": "GangaSeek namespace packet",
                "status": "candidate",
                "raw_export_status": "summary_only",
                "canon_status": "not_canon",
                "deployment_status": "not_deployed",
                "authority_scope": "none",
                "evidence_refs": ["https://drive.google.com/file/d/example"],
            },
            {
                "node_id": "claim-001",
                "node_type": "Claim",
                "title": "Visible source candidate requires hashing.",
                "status": "candidate",
                "raw_export_status": "summary_only",
                "canon_status": "not_canon",
                "deployment_status": "not_deployed",
                "authority_scope": "none",
                "evidence_refs": [],
            },
        ],
        "proposed_edges": [
            {
                "edge_id": "edge-001",
                "edge_type": "derived_from",
                "from_node": "claim-001",
                "to_node": "source-001",
                "evidence_ref": None,
                "status": "candidate",
            }
        ],
        "contradictions_or_uncertainties": [],
        "missing_receipts": ["sha256_if_available", "full_raw_export"],
        "review_required": ["Lucerna", "Hashlight"],
        "strongest_safe_claim": "This is a visible source candidate requiring hash and review.",
        "forbidden_claims": ["canon-promotion", "release-claim", "verification-claim"],
        "canon_status": "not_canon",
        "deployment_status": "not_deployed",
        "authority_scope": "none",
    }


def test_artifact_card_preserves_status_strip():
    result = build_artifact_card(graph_candidate())
    assert result.ok, result.errors
    card = result.card
    assert card["status_strip"]["canon_status"] == "not_canon"
    assert card["status_strip"]["deployment_status"] == "not_deployed"
    assert card["status_strip"]["authority_scope"] == "none"
    assert card["status_strip"]["review_state"] == "needs_review"


def test_artifact_card_surfaces_missing_receipts_and_forbidden_claims():
    card = build_artifact_card(graph_candidate()).card
    assert "sha256_if_available" in card["graph"]["missing_receipts"]
    assert "full_raw_export" in card["graph"]["missing_receipts"]
    assert "canon-promotion" in card["claims"]["forbidden_claims"]
    assert "release-claim" in card["claims"]["forbidden_claims"]


def test_artifact_card_renders_markdown_with_boundary():
    card = build_artifact_card(graph_candidate()).card
    markdown = artifact_card_to_markdown(card)
    assert "CANON_STATUS: not_canon" in markdown
    assert "DEPLOYMENT_STATUS: not_deployed" in markdown
    assert "AUTHORITY_SCOPE: none" in markdown
    assert "sha256_if_available" in markdown
    assert "This card grants no authority." in markdown


def test_invalid_candidate_blocks_card():
    result = build_artifact_card({"candidate_id": "bad"})
    assert not result.ok
    assert result.card is None
    assert "missing source_packet_id" in result.errors
