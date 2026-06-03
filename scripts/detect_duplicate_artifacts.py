#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Detect duplicate artifacts by slug/date and content hash."""

from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))

import argparse
import json
from collections import defaultdict
from pathlib import Path

from scripts.lattice_kg_lib import find_date_string, iter_files, sha256_file, slugify


def detect_duplicates(repo_root: Path) -> dict:
    by_slug_date = defaultdict(list)
    by_hash = defaultdict(list)
    for path in iter_files(repo_root, extensions={".md", ".yaml", ".yml"}):
        rel = path.relative_to(repo_root).as_posix()
        key = (find_date_string(rel), slugify(path.stem))
        by_slug_date[key].append(rel)
        by_hash[sha256_file(path)].append(rel)
    return {
        "same_slug_date": [paths for paths in by_slug_date.values() if len(paths) > 1],
        "content_hash_similarity": [paths for paths in by_hash.values() if len(paths) > 1],
        "exact_path_match": [],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    payload = detect_duplicates(Path(args.repo_root).resolve())
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
