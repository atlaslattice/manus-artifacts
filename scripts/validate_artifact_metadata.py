#!/usr/bin/env python3
"""
validate_artifact_metadata.py

Checks that key archive markdown files carry the expected metadata fields
needed for indexing in the KG hypercube.

Required fields (checked in the first 20 lines of each file):
  - STATUS:  (candidate / ratified / deprecated / draft)
  - A heading (# Title)

Optional but scored:
  - ratification_event_id
  - canon_status
  - trust_state
  - created / updated / ratified timestamps

Exit codes:
  0 — all checked files pass minimum requirements
  1 — one or more files missing required fields
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Directories to audit for metadata completeness
AUDIT_DIRS = [
    "archive/boot",
    "archive/spec",
    "docs",
    "projects",
]

# Minimum number of top lines to inspect per file
HEADER_LINES = 40

REQUIRED_PATTERNS = ["STATUS:", "#"]
SCORED_FIELDS = [
    "ratification_event_id",
    "canon_status",
    "trust_state",
    "created",
    "updated",
]


def collect_files() -> list[Path]:
    files = []
    for d in AUDIT_DIRS:
        target = REPO_ROOT / d
        if target.exists():
            files.extend(
                p
                for p in target.rglob("*.md")
                if ".git" not in p.parts and p.name != "README.md"
            )
    return sorted(files)


def check_file(f: Path) -> tuple[list[str], int]:
    """Return (missing_required, score)."""
    lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
    header = "\n".join(lines[:HEADER_LINES]).lower()

    missing = []
    for req in REQUIRED_PATTERNS:
        if req.lower() not in header:
            missing.append(req)

    score = sum(1 for field in SCORED_FIELDS if field.lower() in header)
    return missing, score


def main() -> int:
    files = collect_files()
    failures: list[str] = []
    scores: list[int] = []

    for f in files:
        missing, score = check_file(f)
        scores.append(score)
        rel = f.relative_to(REPO_ROOT)
        if missing:
            failures.append(f"  MISSING {missing}  in  {rel}")

    total = len(files)
    avg_score = sum(scores) / total if total else 0

    print(f"Artifact metadata audit: {total} files checked")
    print(f"  Average optional-field coverage: {avg_score:.1f}/{len(SCORED_FIELDS)}")

    if failures:
        print(f"\n{len(failures)} file(s) missing required fields:\n")
        for line in failures:
            print(line)
        return 1

    print("  All files pass minimum metadata requirements.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
