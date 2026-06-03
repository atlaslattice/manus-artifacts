#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Report or backfill missing artifact_id fields for markdown and YAML artifacts."""

from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))

import argparse
import json
from datetime import UTC, datetime
from pathlib import Path

from scripts.lattice_kg_lib import generate_artifact_id, iter_files, load_metadata, read_text, split_frontmatter, dump_frontmatter


def scan(repo_root: Path) -> list[dict[str, str]]:
    rows = []
    for path in iter_files(repo_root):
        rel = path.relative_to(repo_root).as_posix()
        meta = load_metadata(path)
        if meta.get("artifact_id"):
            continue
        stamp = datetime.fromtimestamp(path.stat().st_mtime, tz=UTC)
        rows.append({"path": rel, "artifact_id": generate_artifact_id(rel, stamp)})
    return rows


def apply_backfill(repo_root: Path, rows: list[dict[str, str]]) -> None:
    for row in rows:
        path = repo_root / row["path"]
        artifact_id = row["artifact_id"]
        if path.suffix == ".md":
            text = read_text(path)
            meta, body = split_frontmatter(text)
            meta["artifact_id"] = artifact_id
            path.write_text(dump_frontmatter(meta, body), encoding="utf-8")
        else:
            text = read_text(path)
            path.write_text(f"artifact_id: {artifact_id}\n{text}", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--write", action="store_true", help="Apply the backfill in-place.")
    args = parser.parse_args()
    repo_root = Path(args.repo_root).resolve()
    rows = scan(repo_root)
    if args.write:
        apply_backfill(repo_root, rows)
    print(json.dumps({"dry_run": not args.write, "missing_artifact_ids": rows}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
