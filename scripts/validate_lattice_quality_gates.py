#!/usr/bin/env python3
"""Validate lattice route and positron review integrity."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def read_jsonl(path: Path) -> list[dict]:
    records: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        records.append(json.loads(line))
    return records


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()

    route_index = root / "archive/boot/gptbrain/LATTICE_ORCS_ROUTE_INDEX.seed.jsonl"
    positron_index = root / "archive/boot/gptbrain/LATTICE_POSITRON_REVIEW_INDEX.seed.jsonl"

    failures: list[str] = []
    if not route_index.exists():
        failures.append(f"Missing route index: {route_index.relative_to(root)}")
    if not positron_index.exists():
        failures.append(f"Missing positron index: {positron_index.relative_to(root)}")
    if failures:
        for failure in failures:
            print(f"- {failure}")
        return 1

    routes = read_jsonl(route_index)
    positrons = read_jsonl(positron_index)
    positron_by_route = {row["route_artifact_id"]: row for row in positrons}

    for route in routes:
        route_id = route["artifact_id"]
        if route_id not in positron_by_route:
            failures.append(f"Missing positron review for route {route_id}")
        for source_path in route.get("source_paths", []):
            if not (root / source_path).exists():
                failures.append(f"Route {route_id} references missing source path: {source_path}")

    for route_id, review in positron_by_route.items():
        review_path = review.get("review_artifact_path")
        if review_path and not (root / review_path).exists():
            failures.append(f"Positron entry {route_id} references missing review path: {review_path}")

    if failures:
        print("Lattice KG quality gates failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        "Lattice KG quality gates passed: "
        f"{len(routes)} routes with positron counterparts validated."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
