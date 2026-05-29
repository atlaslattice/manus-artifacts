#!/usr/bin/env python3
"""Validate artifact registry, governance truth, and graph coverage."""

from __future__ import annotations

import json
from pathlib import Path

from build_artifact_registry import (
    DOCS_WITH_GOVERNANCE_LANGUAGE,
    GRAPH_PATH,
    RATIFICATION_LOG_PATH,
    REGISTRY_PATH,
    ROOT,
    SCORECARD_PATH,
    build_registry_bundle,
    git_tracked_files,
)

ALLOWED_CANON_STATUSES = {"candidate", "reviewed", "ratified", "superseded", "deprecated"}
REQUIRED_ARTIFACT_FIELDS = {
    "artifact_id",
    "title",
    "path",
    "artifact_type",
    "owner",
    "canon_status",
    "lifecycle_state",
    "provenance",
    "governance",
    "links_to",
}
REQUIRED_PROVENANCE_FIELDS = {"source", "tracked_by_git", "path"}
REQUIRED_GOVERNANCE_FIELDS = {"status_authority", "event_log"}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def compare_generated_outputs(errors: list[str]) -> tuple[dict, dict, dict]:
    registry = load_json(REGISTRY_PATH)
    graph = load_json(GRAPH_PATH)
    scorecard = load_json(SCORECARD_PATH)
    generated_utc = registry.get("generated_utc")
    expected_registry, expected_graph, expected_scorecard = build_registry_bundle(
        ROOT, generated_utc=generated_utc
    )

    if registry != expected_registry:
        errors.append(
            "artifact registry is out of date; run python3 scripts/build_artifact_registry.py"
        )
    if graph != expected_graph:
        errors.append("graph.json is out of date; run python3 scripts/build_artifact_registry.py")
    if scorecard != expected_scorecard:
        errors.append(
            "repo quality scorecard is out of date; run python3 scripts/build_artifact_registry.py"
        )
    return registry, graph, scorecard


def validate_registry_fields(registry: dict, graph: dict, scorecard: dict, errors: list[str]) -> None:
    artifacts = registry.get("artifacts", [])
    tracked_paths = {path.as_posix() for path in git_tracked_files(ROOT)}
    ids = set()

    if not artifacts:
        errors.append("artifact registry has no artifacts")
        return

    for idx, artifact in enumerate(artifacts, start=1):
        missing = REQUIRED_ARTIFACT_FIELDS - artifact.keys()
        if missing:
            errors.append(f"artifact[{idx}] missing required fields: {sorted(missing)}")
            continue

        artifact_id = artifact["artifact_id"]
        rel_path = artifact["path"]
        canon_status = artifact["canon_status"]
        provenance = artifact["provenance"]
        governance = artifact["governance"]

        if artifact_id in ids:
            errors.append(f"duplicate artifact_id: {artifact_id}")
        ids.add(artifact_id)

        if canon_status not in ALLOWED_CANON_STATUSES:
            errors.append(f"artifact[{idx}] has invalid canon_status: {canon_status}")

        if rel_path not in tracked_paths:
            errors.append(f"artifact path is not a tracked eligible file: {rel_path}")

        if REQUIRED_PROVENANCE_FIELDS - provenance.keys():
            errors.append(f"artifact[{idx}] missing provenance fields: {sorted(REQUIRED_PROVENANCE_FIELDS - provenance.keys())}")
        if REQUIRED_GOVERNANCE_FIELDS - governance.keys():
            errors.append(f"artifact[{idx}] missing governance fields: {sorted(REQUIRED_GOVERNANCE_FIELDS - governance.keys())}")

        if provenance.get("path") != rel_path:
            errors.append(f"artifact[{idx}] provenance path mismatch: {rel_path}")

        if canon_status in {"ratified", "superseded"} and not artifact.get("ratification_event_id"):
            errors.append(f"artifact[{idx}] missing ratification_event_id for {canon_status}")

    if len(artifacts) != len(tracked_paths):
        errors.append(
            "artifact coverage mismatch:"
            f" registry has {len(artifacts)} entries for {len(tracked_paths)} tracked eligible files"
        )

    graph_nodes = set(graph.get("nodes", []))
    if ids != graph_nodes:
        errors.append("graph nodes do not exactly match registry artifact IDs")

    for edge in graph.get("edges", []):
        if not {"from", "to", "relation"} <= edge.keys():
            errors.append(f"invalid edge record: {edge}")
            continue
        if edge["from"] not in graph_nodes:
            errors.append(f"edge source not in graph nodes: {edge['from']}")
        if edge["to"] not in graph_nodes:
            errors.append(f"edge target not in graph nodes: {edge['to']}")

    totals = scorecard.get("totals", {})
    if totals.get("tracked_artifact_files") != len(tracked_paths):
        errors.append("scorecard tracked_artifact_files count mismatch")
    if totals.get("registry_artifacts") != len(artifacts):
        errors.append("scorecard registry_artifacts count mismatch")
    if totals.get("graph_nodes") != len(graph.get("nodes", [])):
        errors.append("scorecard graph_nodes count mismatch")
    if totals.get("graph_coverage_pct") != 100.0:
        errors.append("graph coverage is expected to be 100.0%")


def validate_governance_language(registry: dict, errors: list[str]) -> None:
    ratified_count = sum(1 for artifact in registry.get("artifacts", []) if artifact["canon_status"] == "ratified")
    for path in DOCS_WITH_GOVERNANCE_LANGUAGE:
        text = path.read_text(encoding="utf-8", errors="replace")
        rel_path = path.relative_to(ROOT).as_posix()
        if ratified_count == 0 and "✅ Canonical" in text:
            errors.append(f"{rel_path} still claims canonical artifacts despite zero ratified entries")
        if "canonical public archive" in text:
            errors.append(f"{rel_path} still uses ambiguous 'canonical public archive' language")
        if "docs/knowledge-graph/artifact_registry.v0_1.json" not in text:
            errors.append(f"{rel_path} must link to the artifact registry source of truth")

    if "docs/knowledge-graph/artifact_registry.v0_1.json" not in RATIFICATION_LOG_PATH.read_text(
        encoding="utf-8", errors="replace"
    ):
        errors.append("RATIFICATION_LOG.md must point to the artifact registry status authority")


def main() -> int:
    errors: list[str] = []

    for path in (REGISTRY_PATH, GRAPH_PATH, SCORECARD_PATH):
        if not path.exists():
            errors.append(f"missing required output: {path.relative_to(ROOT).as_posix()}")

    if errors:
        print("\n".join(errors))
        return 1

    registry, graph, scorecard = compare_generated_outputs(errors)
    validate_registry_fields(registry, graph, scorecard, errors)
    validate_governance_language(registry, errors)

    if errors:
        print("Artifact metadata validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Artifact metadata validation passed:"
        f" {scorecard['totals']['registry_artifacts']} artifacts,"
        f" {scorecard['totals']['graph_edges']} edges,"
        f" {scorecard['totals']['graph_coverage_pct']}% coverage"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
