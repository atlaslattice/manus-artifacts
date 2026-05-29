"""Candidate tests for GPTDream++ Drive→GitHub promotion gate enforcement."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_gptdreampp_promotion_gate.py"
PACKAGE = ROOT / "archive" / "aetherforge" / "gptdreampp-openai"
MAP_PATH = PACKAGE / "ruleset" / "artifact_class_validation_map.json"
VALID_FIXTURE = PACKAGE / "eval_fixtures" / "promotion_gate.valid.noncanon.json"
INVALID_FIXTURE = PACKAGE / "eval_fixtures" / "promotion_gate.invalid.canon_missing_adjudication.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_validation_script_file_exists() -> None:
    assert SCRIPT.exists()


def test_artifact_class_map_contains_three_required_classes() -> None:
    class_map = load_json(MAP_PATH)
    assert set(class_map.keys()) == {"dream", "play", "work"}


def test_valid_fixture_non_canon_default() -> None:
    record = load_json(VALID_FIXTURE)
    assert record["canon_status"] == "NOT_CANON"
    assert record["reviewer"] is None
    assert record["ratification_event"] is None


def test_invalid_fixture_requires_adjudication_for_ratified_canon() -> None:
    record = load_json(INVALID_FIXTURE)
    assert record["canon_status"] == "RATIFIED_CANON"
    assert record["reviewer"] is None
    assert record["ratification_event"] is None


def test_script_passes_on_current_fixture_set() -> None:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
