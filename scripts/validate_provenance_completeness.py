#!/usr/bin/env python3
"""
validate_provenance_completeness.py
=====================================
Checks that every Markdown artifact in the archive has the minimum required
frontmatter fields for the Atlas Lattice provenance model.

Required fields (all artifacts):
    artifact_id, title, status, owner, created, last_updated, source_of_truth

Additional required for public-candidate artifacts:
    canon (must be "YES" or "NO")

Exit code 0 = pass, 1 = fail.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

REQUIRED_BASE = {"artifact_id", "title", "status", "owner", "created", "last_updated", "source_of_truth"}
REQUIRED_CANON = {"canon"}

VALID_STATUSES = {"DRAFT", "CANDIDATE", "CANONICAL", "ARCHIVED", "PUBLIC-CANDIDATE"}
VALID_CANON = {"YES", "NO"}

# Directories to check (relative to root)
SCAN_DIRS = [
    "archive",
    "docs",
    "projects",
    "schemas",
    "reference_impl",
]

# Paths to skip
SKIP_PREFIXES = {
    ".git/",
    "archive/synthesis/data/",  # JSON seed files, not Markdown artifacts
}


def parse_simple_yaml(text: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in text.splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if key and val:
            result[key] = val
    return result


def check_file(md_file: Path, root: Path) -> list[str]:
    """Return list of violation strings, or empty if clean."""
    rel = md_file.relative_to(root).as_posix()
    for prefix in SKIP_PREFIXES:
        if rel.startswith(prefix):
            return []

    try:
        text = md_file.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return []

    m = FRONTMATTER_RE.match(text)
    if not m:
        return []  # no frontmatter — not an indexed artifact

    meta = parse_simple_yaml(m.group(1))
    if not meta.get("artifact_id"):
        return []  # not indexed — not yet ingested

    issues = []

    # Check required base fields
    for field in sorted(REQUIRED_BASE):
        if not meta.get(field):
            issues.append(f"missing field '{field}'")

    # Check status validity
    status = meta.get("status", "").upper()
    if status and status not in VALID_STATUSES:
        issues.append(f"invalid status '{status}' (valid: {sorted(VALID_STATUSES)})")

    # Check canon field
    canon = meta.get("canon", "").upper()
    if not canon:
        issues.append("missing field 'canon'")
    elif canon not in VALID_CANON:
        issues.append(f"invalid canon value '{canon}' (must be YES or NO)")

    if issues:
        return [f"{rel}: {issue}" for issue in issues]
    return []


def main() -> int:
    all_issues: list[str] = []
    checked = 0

    for scan_dir_name in SCAN_DIRS:
        scan_dir = ROOT / scan_dir_name
        if not scan_dir.exists():
            continue
        for md_file in sorted(scan_dir.rglob("*.md")):
            rel = md_file.relative_to(ROOT).as_posix()
            skip = any(rel.startswith(p) for p in SKIP_PREFIXES)
            if skip:
                continue
            issues = check_file(md_file, ROOT)
            all_issues.extend(issues)
            checked += 1

    passed = len(all_issues) == 0
    print(f"=== Provenance Completeness Check ===")
    print(f"  Files checked: {checked}")
    if all_issues:
        print(f"  Issues found: {len(all_issues)}")
        for issue in all_issues[:50]:
            print(f"  - {issue}")
        if len(all_issues) > 50:
            print(f"  … {len(all_issues) - 50} more")
    else:
        print("  All indexed artifacts have required provenance fields.")
    print(f"\nprovenance completeness: {'PASS' if passed else 'FAIL'}")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
