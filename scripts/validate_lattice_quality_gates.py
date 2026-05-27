#!/usr/bin/env python3
"""Validate lattice global index completeness, freshness, and retrieval behavior."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path

EXCLUDE_PARTS = {".git", ".pytest_cache", "__pycache__"}
EXCLUDE_PATHS = {"archive/knowledge_graph/lattice_kg/v0_5/lattice_global_index.v0.1.json"}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def iter_repo_files(repo_root: Path) -> list[str]:
    files = []
    for path in repo_root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(repo_root)
        if any(part in EXCLUDE_PARTS for part in rel.parts):
            continue
        rel_posix = rel.as_posix()
        if rel_posix in EXCLUDE_PATHS:
            continue
        files.append(rel_posix)
    return sorted(files)


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def compute_fingerprint(repo_root: Path, files: list[str]) -> str:
    lines = []
    for rel in files:
        digest = file_sha256(repo_root / rel)
        lines.append(f"{rel}:{digest}")
    return hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest()


def validate_index(repo_root: Path, index_path: Path, max_age_days: int) -> list[str]:
    errors: list[str] = []
    index = load_json(index_path)
    repo_files = iter_repo_files(repo_root)

    indexed_artifacts = index.get("artifacts", [])
    indexed_paths = sorted(item["path"] for item in indexed_artifacts)

    missing = sorted(set(repo_files) - set(indexed_paths))
    extra = sorted(set(indexed_paths) - set(repo_files))

    if missing:
        errors.append(f"completeness check failed: {len(missing)} repository files missing from index")
    if extra:
        errors.append(f"stale-index check failed: {len(extra)} indexed paths not present in repository")

    for item in indexed_artifacts:
        candidate_path = repo_root / item["path"]
        if not candidate_path.exists():
            errors.append(f"broken-link check failed: indexed path does not exist: {item['path']}")
            break

    expected_fingerprint = compute_fingerprint(repo_root, repo_files)
    if index.get("snapshot_fingerprint") != expected_fingerprint:
        errors.append("stale-index check failed: snapshot_fingerprint mismatch")

    generated = datetime.fromisoformat(index["generated_at_utc"].replace("Z", "+00:00"))
    age_days = (datetime.now(UTC) - generated).days
    if age_days > max_age_days:
        errors.append(f"stale-index check failed: index is {age_days} days old (max {max_age_days})")

    required_paths = {
        "README.md",
        "archive/knowledge_graph/lattice_kg/v0_5/LATTICE_AETHERFORGE_GPTDREAM_UNIFIED_MISSION_CHARTER_v0.1.md",
        "archive/knowledge_graph/lattice_kg/v0_5/lattice_hypercube_144_scoreboard.v0.1.json",
    }
    index_by_path = {item["path"]: item for item in indexed_artifacts}
    index_by_id = {item["artifact_id"]: item for item in indexed_artifacts}

    for required in required_paths:
        record = index_by_path.get(required)
        if record is None:
            errors.append(f"retrieval check failed: required path not indexed: {required}")
            continue
        if record["artifact_id"] not in index_by_id:
            errors.append(f"retrieval check failed: artifact_id lookup missing for {required}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".", help="Repository root directory")
    parser.add_argument(
        "--index",
        default="archive/knowledge_graph/lattice_kg/v0_5/lattice_global_index.v0.1.json",
        help="Path to index JSON",
    )
    parser.add_argument("--max-age-days", type=int, default=7)
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    index_path = (repo_root / args.index).resolve() if not Path(args.index).is_absolute() else Path(args.index)

    errors = validate_index(repo_root, index_path, max_age_days=args.max_age_days)
    if errors:
        for err in errors:
            print(f"ERROR: {err}")
        return 1

    print("All lattice quality gates passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
