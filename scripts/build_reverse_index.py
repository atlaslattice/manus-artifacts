#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Build a reverse path -> artifact_id JSON index."""

from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))

import argparse
import json
from pathlib import Path

from scripts.build_lattice_global_index_v2 import build_index


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output", default="archive/knowledge_graph/lattice_kg/v1_0/reverse_index.v1.0.json")
    args = parser.parse_args()
    repo_root = Path(args.repo_root).resolve()
    index = build_index(repo_root)
    reverse = {
        "STATUS": "CANDIDATE — NOT CANON",
        "AUTHORITY": "NONE",
        "DEPLOYMENT": "NONE",
        "reverse_index": {row["path"]: row["artifact_id"] for row in index["artifacts"]},
    }
    Path(args.output).write_text(json.dumps(reverse, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"count": len(reverse['reverse_index']), "output": args.output}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
