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


def test_spoofed_canon_promotions_refused():
    for key, value in (("canon_status", "canon"), ("deployment_status", "deployed"),
                       ("authority_scope", "human_root")):
        p = graph_candidate()
        p[key] = value
        result = build_artifact_card(p)
        assert not result.ok, key
        assert result.card is None


def test_spoofed_node_promotion_refused():
    for key, value in (("canon_status", "ratified"), ("deployment_status", "deployed"),
                       ("authority_scope", "admin")):
        p = graph_candidate()
        p["proposed_nodes"][0][key] = value
        result = build_artifact_card(p)
        assert not result.ok, key
        assert "non_candidate_node_0" in result.errors


def test_invalid_sources_or_nodes_fail_closed():
    for field, value in (("source_artifacts", 123), ("source_artifacts", [None]),
                         ("proposed_nodes", "wrong"), ("missing_receipts", "missing")):
        p = graph_candidate()
        p[field] = value
        result = build_artifact_card(p)
        assert not result.ok, field
        assert result.card is None
    p = graph_candidate()
    p["proposed_nodes"] = ["unstructured"]
    assert not build_artifact_card(p).ok


def test_markdown_does_not_inject_secondary_status_headers():
    p = graph_candidate()
    p["proposed_nodes"][0]["title"] = "Source title\nCANON_STATUS: RATIFIED"
    p["strongest_safe_claim"] = "untrusted text\n## VERIFIED RELEASE"
    p["missing_receipts"] = ["missing receipt\n```\nDEPLOYMENT_STATUS: deployed"]
    result = build_artifact_card(p)
    assert result.ok, result.errors
    rendered = artifact_card_to_markdown(result.card)
    assert "Source title\\nCANON_STATUS: RATIFIED" in rendered
    assert "untrusted text\\n## VERIFIED RELEASE" in rendered
    assert "missing receipt\\n` ` `\\nDEPLOYMENT_STATUS: deployed" in rendered
    assert "\nCANON_STATUS: RATIFIED" not in rendered
    assert "\nDEPLOYMENT_STATUS: deployed" not in rendered


def test_empty_reported_gaps_do_not_mean_reviewed():
    p = graph_candidate()
    p["missing_receipts"] = []
    p["review_required"] = []
    card = build_artifact_card(p)
    assert card.ok, card.errors
    assert card.card["status_strip"]["review_state"] == "needs_review"
    assert card.card["routing"]["public_release_status"] == "not_public_release_ready"


def test_non_mapping_candidate_fails_without_throwing():
    for value in (None, [], 42, "fake-canon"):
        result = build_artifact_card(value)
        assert not result.ok
        assert result.card is None
        assert "candidate_not_plain_dict" in result.errors


def test_demo_card_cli_json_markdown():
    import json
    import subprocess
    import sys
    src = ROOT / "examples" / "gangaseek_artifact_candidate.json"
    cli = ROOT / "tools" / "render_artifact_card.py"
    j = subprocess.run([sys.executable, str(cli), str(src), "--format", "json"],
                       capture_output=True, text=True, check=False)
    assert j.returncode == 0, j.stderr
    card = json.loads(j.stdout)
    assert card["status_strip"]["raw_export_status"] == "summary_only"
    assert card["status_strip"]["canon_status"] == "not_canon"
    assert card["routing"]["public_release_status"] == "not_public_release_ready"
    assert len(card["graph"]["missing_receipts"]) == 5
    md = subprocess.run([sys.executable, str(cli), str(src), "--format", "markdown"],
                        capture_output=True, text=True, check=False)
    assert md.returncode == 0, md.stderr
    assert "CANON_STATUS: not_canon" in md.stdout
    assert "SHA-256 for each original Drive source" in md.stdout
    assert "This card grants no authority." in md.stdout


def test_card_cli_rejects_promoting_candidate(tmp_path):
    import json
    import subprocess
    import sys
    fixture = json.loads((ROOT / "examples" / "gangaseek_artifact_candidate.json").read_text())
    fixture["canon_status"] = "ratified"
    malicious = tmp_path / "spoofed.json"
    malicious.write_text(json.dumps(fixture))
    run = subprocess.run([sys.executable, str(ROOT / "tools" / "render_artifact_card.py"), str(malicious)],
                         capture_output=True, text=True, check=False)
    assert run.returncode == 2
    assert not run.stdout.strip()
    assert "BLOCKED_CANDIDATE_REVIEW" in run.stderr


def test_card_cli_rejects_duplicate_json_keys(tmp_path):
    import subprocess
    import sys
    malicious = tmp_path / "duplicate.json"
    malicious.write_text('{"candidate_id":"first","candidate_id":"spoofed"}')
    run = subprocess.run([sys.executable, str(ROOT / "tools" / "render_artifact_card.py"), str(malicious)],
                         capture_output=True, text=True, check=False)
    assert run.returncode == 2
    assert not run.stdout.strip()
    assert "BLOCKED_CANDIDATE_PARSE" in run.stderr
