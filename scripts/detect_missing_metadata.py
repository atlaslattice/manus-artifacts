#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Report missing metadata fields by artifact family."""

from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))

import argparse
import json
from pathlib import Path

from scripts.lattice_kg_lib import infer_artifact_family, iter_files, load_metadata, required_fields_by_family


def detect_missing(repo_root: Path) -> list[dict]:
    required = required_fields_by_family()
    rows = []
    for path in iter_files(repo_root):
        rel = path.relative_to(repo_root).as_posix()
        family = infer_artifact_family(rel)
        metadata = load_metadata(path)
        missing = [field for field in required.get(family, []) if metadata.get(field) in (None, "", [], {})]
        if missing:
            rows.append({"path": rel, "family": family, "missing_fields": missing})
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    print(json.dumps({"rows": detect_missing(Path(args.repo_root).resolve())}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
