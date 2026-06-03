#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Generate a domain × lane coverage report from the v2 index."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def build_markdown(index: dict) -> str:
    domains = sorted(index.get("coverage", {}))
    lanes = sorted({lane for lanes in index.get("coverage", {}).values() for lane in lanes})
    lines = [
        "| Domain | " + " | ".join(lanes) + " |",
        "|---|" + "|".join(["---"] * len(lanes)) + "|",
    ]
    for domain in domains:
        cells = []
        for lane in lanes:
            item = index["coverage"].get(domain, {}).get(lane)
            if item:
                cells.append(f"{item['artifact_count']} / {item['avg_completeness']:.2f}")
            else:
                cells.append("0 / 0.00")
        lines.append("| " + domain + " | " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", default="archive/knowledge_graph/lattice_kg/v1_0/lattice_global_index.v1.0.json")
    parser.add_argument("--output", default="docs/CROSS_LANE_COVERAGE_REPORT.md")
    args = parser.parse_args()
    index = json.loads(Path(args.index).read_text(encoding="utf-8"))
    rendered = build_markdown(index)
    Path(args.output).write_text(rendered, encoding="utf-8")
    print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
