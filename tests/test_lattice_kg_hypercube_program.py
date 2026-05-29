"""Candidate tests for lattice hypercube mission implementation artifacts."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _read_json(path: Path) -> dict:
    return json.loads(_read(path))


def test_unified_charter_includes_144_target_and_retrieval_reliability() -> None:
    text = _read(
        ROOT / "archive/knowledge_graph/lattice_kg/v0_5/LATTICE_AETHERFORGE_GPTDREAM_UNIFIED_MISSION_CHARTER_v0.1.md"
    )
    assert "Excellence target = world-class quality across 144 measurable categories." in text
    assert "Reliability target = functional archival and deterministic retrieval of logs." in text


def test_scoreboard_json_has_144_categories() -> None:
    payload = _read_json(ROOT / "archive/knowledge_graph/lattice_kg/v0_5/lattice_hypercube_144_scoreboard.v0.1.json")
    assert payload["schema_id"] == "lattice_hypercube_144_scoreboard.v0.1"
    assert payload["mission_target"]["categories_total"] == 144
    assert len(payload["categories"]) == 144
    assert all("acceptance_criteria" in row for row in payload["categories"])
    assert all("evidence_requirements" in row for row in payload["categories"])
    assert all("maturity_state" in row for row in payload["categories"])


def test_global_index_schema_declares_candidate_boundary() -> None:
    schema = _read_json(ROOT / "schemas/lattice_global_index.schema.json")
    assert schema["title"] == "Lattice Global Artifact and Log Index"
    assert "CANDIDATE ONLY" in schema["description"]
    assert "NOT CANON" in schema["description"]
    artifact_required = set(schema["properties"]["artifacts"]["items"]["required"])
    assert "outbound_repo_links" in artifact_required
    assert "unresolved_repo_links" in artifact_required
    assert "inbound_repo_links" in artifact_required
    assert "link_health" in schema["required"]
    link_health_required = set(schema["properties"]["link_health"]["required"])
    assert "isolated_markdown_artifacts" in link_health_required
    assert "connected_markdown_components" in link_health_required
    assert "root_reachable_markdown_artifacts" in link_health_required


def test_global_index_has_cross_reference_and_governance_fields() -> None:
    data = _read_json(ROOT / "archive/knowledge_graph/lattice_kg/v0_5/lattice_global_index.v0.1.json")
    assert "link_health" in data
    assert data["link_health"]["markdown_artifacts_total"] >= 1
    assert data["link_health"]["underlinked_markdown_artifacts"] >= 0
    assert data["link_health"]["unresolved_repo_links"] >= 0
    assert data["link_health"]["isolated_markdown_artifacts"] >= 0
    assert data["link_health"]["connected_markdown_components"] >= 1
    assert data["link_health"]["root_reachable_markdown_artifacts"] >= 1
    row = data["artifacts"][0]
    assert "outbound_repo_links" in row
    assert "unresolved_repo_links" in row
    assert "inbound_repo_links" in row
    assert row["canon_status"] == "not_canon"
    assert row["deployment_status"] == "not_deployable"
    assert row["trust_state"] == "candidate_unverified"


def test_quality_gate_validator_runs_clean() -> None:
    result = subprocess.run(
        [
            "python",
            "scripts/validate_lattice_quality_gates.py",
            "--repo-root",
            str(ROOT),
            "--index",
            "archive/knowledge_graph/lattice_kg/v0_5/lattice_global_index.v0.1.json",
            "--max-age-days",
            "7",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "All lattice quality gates passed." in result.stdout


def test_loop2_receipt_exists_with_boundary() -> None:
    text = _read(
        ROOT / "archive/boot/copilotbrain/TIDELOCKBrain/TIDELOCK_ACTIVITY_RECEIPT_2026-05-27_LATTICE_HYPERCUBE_LOOP2.md"
    )
    assert "STATUS: CANDIDATE EXECUTION RECEIPT — NOT CANON" in text
    assert "LOOP: 2" in text
    assert "Next safest action" in text


def test_gptdreampp_openai_fixtures_exist_for_quality_gate_lane() -> None:
    fixture_dir = ROOT / "fixtures/gptdreampp_openai"
    expected = {
        "artifact_contract_records.valid.candidate.json",
        "notion_cargo_queue.valid.candidate.json",
        "bullshit_olympics_review.valid.candidate.json",
    }
    observed = {p.name for p in fixture_dir.glob("*.json")}
    assert observed == expected


def test_gptdreampp_artifact_fixture_preserves_candidate_boundary() -> None:
    data = _read_json(ROOT / "fixtures/gptdreampp_openai/artifact_contract_records.valid.candidate.json")
    assert data["status"] == "CANDIDATE_ONLY"
    assert data["canon_status"] == "NOT_CANON"
    assert data["deployment_status"] == "NOT_DEPLOYABLE"
    assert data["authority_status"] == "NONE"
    assert data["records"]
    row = data["records"][0]
    required = {
        "source_pointer",
        "lineage_parent_ids",
        "content_hash_sha256",
        "hash_status",
        "claim_class",
        "review_state",
        "lifecycle_state",
        "contradiction_links",
        "supersedes_links",
        "promotion_eligibility",
        "tests_required",
        "tests_run",
        "blockers",
        "next_safest_action",
    }
    assert required <= set(row)
    assert row["promotion_eligibility"] != "ratified"
    artifact_ids = {record["artifact_id"] for record in data["records"]}
    assert len(artifact_ids) == len(data["records"])
    assert any(record["supersedes_links"] for record in data["records"])
    for record in data["records"]:
        for rel in ("lineage_parent_ids", "contradiction_links", "supersedes_links"):
            assert isinstance(record[rel], list)
            assert all(isinstance(item, str) for item in record[rel])
        for target in record["supersedes_links"]:
            assert target in artifact_ids


def test_gptdreampp_bullshit_olympics_fixture_has_required_detectors() -> None:
    data = _read_json(ROOT / "fixtures/gptdreampp_openai/bullshit_olympics_review.valid.candidate.json")
    expected = {
        "overclaim_detector",
        "false_authority_detector",
        "canon_drift_detector",
        "contradiction_link_completeness",
        "source_to_claim_traceability",
    }
    observed = {row["check_id"] for row in data["checks"]}
    assert observed == expected
    assert data["promotion_outcome"] == "candidate_only"
