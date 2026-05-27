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
