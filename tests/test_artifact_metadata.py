"""Tests for repo-wide artifact registry generation and validation."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
REGISTRY_PATH = ROOT / "docs" / "knowledge-graph" / "artifact_registry.v0_1.json"
GRAPH_PATH = ROOT / "graph.json"
SCORECARD_PATH = ROOT / "docs" / "knowledge-graph" / "repo_quality_scorecard.v0_1.json"

sys.path.insert(0, str(SCRIPTS))

from build_artifact_registry import build_registry_bundle  # noqa: E402


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_registry_bundle_covers_all_tracked_artifacts() -> None:
    registry, graph, scorecard = build_registry_bundle(ROOT, generated_utc="2026-05-29T00:00:00Z")

    assert scorecard["totals"]["tracked_artifact_files"] == len(registry["artifacts"])
    assert scorecard["totals"]["registry_artifacts"] == len(registry["artifacts"])
    assert scorecard["totals"]["graph_nodes"] == len(graph["nodes"])
    assert scorecard["totals"]["graph_coverage_pct"] == 100.0


def test_generated_outputs_match_builder() -> None:
    registry_on_disk = load_json(REGISTRY_PATH)
    graph_on_disk = load_json(GRAPH_PATH)
    scorecard_on_disk = load_json(SCORECARD_PATH)

    expected_registry, expected_graph, expected_scorecard = build_registry_bundle(
        ROOT, generated_utc=registry_on_disk["generated_utc"]
    )

    assert registry_on_disk == expected_registry
    assert graph_on_disk == expected_graph
    assert scorecard_on_disk == expected_scorecard


def test_validation_script_passes() -> None:
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / "validate_artifact_metadata.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
