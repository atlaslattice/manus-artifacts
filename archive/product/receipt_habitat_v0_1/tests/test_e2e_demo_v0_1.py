import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "src" / "receipt_habitat"
sys.path.insert(0, str(SRC))

from graph import packet_to_graph_candidate
from ingest import build_ingestion_packet
from review import review_packet
from serialize import to_stable_json, write_packet


def test_gangaseek_hash_gap_demo_e2e(tmp_path):
    source = ROOT / "examples" / "gangaseek_hash_gap_summary.md"

    packet = build_ingestion_packet(
        str(source),
        raw_status="summary_only",
        timezone="America/Chicago",
        seat_name="Hashlight",
        model_surface="ChatGPT",
        source_thread_label="gangaseek-hash-gap-demo",
    )
    packet["claims_extracted"] = [
        {
            "claim": "GangaSeek candidate files are visible and need hashes before stronger claims.",
            "evidence_ref": str(source),
            "confidence": "C2_EVIDENCE",
        }
    ]
    packet["overclaims_to_avoid"] = [
        "ratified namespace",
        "canon catalog",
        "deployed standard",
        "verified release",
        "complete GangaSeek corpus",
    ]
    packet["strongest_safe_claim"] = (
        "GangaSeek candidate files are source-visible in summary form and require hashing, "
        "mirroring review, and claim extraction before public/canon/deployment claims."
    )

    review = review_packet(packet, source_text=source.read_text(encoding="utf-8"))
    assert review.verdict == "block"
    assert "deployed" in review.risky_phrases
    assert "verified" in review.risky_phrases

    graph_result = packet_to_graph_candidate(packet)
    assert graph_result.ok, graph_result.errors
    candidate = graph_result.candidate
    assert candidate["canon_status"] == "not_canon"
    assert candidate["deployment_status"] == "not_deployed"
    assert candidate["authority_scope"] == "none"
    assert "full_raw_export" in candidate["missing_receipts"]

    rendered = to_stable_json(candidate)
    loaded = json.loads(rendered)
    assert loaded["candidate_id"].startswith("gwc-")
    assert loaded["proposed_nodes"]
    assert loaded["proposed_edges"]

    out = tmp_path / "gangaseek_graph_candidate.json"
    write_packet(candidate, str(out))
    assert out.exists()
    assert json.loads(out.read_text(encoding="utf-8"))["canon_status"] == "not_canon"
