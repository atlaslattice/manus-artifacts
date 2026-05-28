#!/usr/bin/env python3
"""Validate artifact metadata and graph consistency."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "docs" / "knowledge-graph" / "artifact_registry.v0_1.json"
GRAPH = ROOT / "graph.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []

    if not REGISTRY.exists():
        errors.append(f"Missing registry: {REGISTRY}")
    if not GRAPH.exists():
        errors.append(f"Missing graph: {GRAPH}")
    if errors:
        print("\n".join(errors))
        return 1

    registry = load_json(REGISTRY)
    graph = load_json(GRAPH)

    artifacts = registry.get("artifacts", [])
    if not artifacts:
        errors.append("Registry has no artifacts")

    ids = set()
    for idx, artifact in enumerate(artifacts, start=1):
        for field in ("artifact_id", "title", "path", "artifact_type", "canon_status"):
            if field not in artifact or not artifact[field]:
                errors.append(f"artifact[{idx}] missing required field: {field}")
        artifact_id = artifact.get("artifact_id")
        if artifact_id in ids:
            errors.append(f"duplicate artifact_id: {artifact_id}")
        ids.add(artifact_id)
        target = ROOT / artifact.get("path", "")
        if not target.exists():
            errors.append(f"artifact path does not exist: {artifact.get('path')}")

    graph_nodes = set(graph.get("nodes", []))
    if not graph_nodes:
        errors.append("graph.json has no nodes")

    if ids - graph_nodes:
        errors.append(f"registry IDs missing from graph nodes: {sorted(ids - graph_nodes)}")

    for edge in graph.get("edges", []):
        src = edge.get("from")
        dst = edge.get("to")
        rel = edge.get("relation")
        if not src or not dst or not rel:
            errors.append(f"invalid edge record: {edge}")
            continue
        if src not in graph_nodes:
            errors.append(f"edge source not in graph nodes: {src}")
        if dst not in graph_nodes:
            errors.append(f"edge target not in graph nodes: {dst}")

    if errors:
        print("Artifact metadata validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print(f"Artifact metadata validation passed: {len(artifacts)} artifacts, {len(graph.get('edges', []))} edges")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
