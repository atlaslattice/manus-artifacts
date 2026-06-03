#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Generate a shields.io endpoint badge for lattice index health."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def badge_color(score: float) -> str:
    if score >= 0.9:
        return "brightgreen"
    if score >= 0.75:
        return "green"
    if score >= 0.5:
        return "yellow"
    return "red"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", default="archive/knowledge_graph/lattice_kg/v1_0/lattice_global_index.v1.0.json")
    parser.add_argument("--output", default="docs/badges/index-health.json")
    args = parser.parse_args()
    index = json.loads(Path(args.index).read_text(encoding="utf-8"))
    score = float(index.get("average_completeness_score", 0.0))
    payload = {
        "STATUS": "CANDIDATE — NOT CANON",
        "AUTHORITY": "NONE",
        "DEPLOYMENT": "NONE",
        "schemaVersion": 1,
        "label": "index health",
        "message": f"{score:.0%}",
        "color": badge_color(score),
    }
    Path(args.output).write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
