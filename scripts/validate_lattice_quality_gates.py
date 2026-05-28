#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX_JSON = ROOT / "docs" / "generated" / "LATTICE_GLOBAL_INDEX.json"

MIN_NODE_COUNT = 20
MIN_EDGE_DENSITY = 1.0
MAX_ORPHAN_RATIO = 0.15


def load_index() -> dict:
    if not INDEX_JSON.exists():
        subprocess.run([sys.executable, str(ROOT / "scripts" / "build_lattice_global_index.py")], check=True)
    return json.loads(INDEX_JSON.read_text(encoding="utf-8"))


def main() -> int:
    data = load_index()
    metrics = data.get("metrics", {})

    node_count = int(metrics.get("node_count", 0))
    edge_density = float(metrics.get("edge_density", 0.0))
    orphan_count = int(metrics.get("orphan_node_count", 0))
    orphan_ratio = orphan_count / max(node_count, 1)
    unknown_link_count = int(metrics.get("unknown_link_count", 0))

    failures: list[str] = []
    if node_count < MIN_NODE_COUNT:
        failures.append(f"node_count {node_count} < {MIN_NODE_COUNT}")
    if edge_density < MIN_EDGE_DENSITY:
        failures.append(f"edge_density {edge_density:.3f} < {MIN_EDGE_DENSITY:.3f}")
    if orphan_ratio > MAX_ORPHAN_RATIO:
        failures.append(f"orphan_ratio {orphan_ratio:.3f} > {MAX_ORPHAN_RATIO:.3f}")
    if unknown_link_count != 0:
        failures.append(f"unknown_link_count {unknown_link_count} != 0")

    if failures:
        print("lattice quality gates failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        "lattice quality gates passed "
        f"(nodes={node_count}, edge_density={edge_density:.3f}, orphan_ratio={orphan_ratio:.3f})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
