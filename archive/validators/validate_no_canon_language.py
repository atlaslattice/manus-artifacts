#!/usr/bin/env python3
"""
validate_no_canon_language.py

Candidate validator stub.

Scans text files for canon-like language that should not appear unless the
artifact also carries an explicit ratification receipt.

STATUS: scaffold only — not deployed CI.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

FORBIDDEN_PATTERNS = [
    r"\bratified\b",
    r"\bcanonical\b",
    r"\bcanonized\b",
    r"\bsource of truth\b",
    r"\bofficial\b",
    r"\bmaster entry lock\b",
    r"\bproduction ready\b",
]

ALLOWING_PATTERNS = [
    r"not canon",
    r"canon_status:\s*not_canon",
    r"candidate",
    r"non-deployable",
    r"not ratified",
    r"ratification required",
]


def scan_text(path: pathlib.Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    lowered = text.lower()
    has_allowing_boundary = any(re.search(p, lowered) for p in ALLOWING_PATTERNS)
    findings: list[str] = []
    for pattern in FORBIDDEN_PATTERNS:
        if re.search(pattern, lowered) and not has_allowing_boundary:
            findings.append(pattern)
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan for canon-like language without boundary markers.")
    parser.add_argument("paths", nargs="+", help="Files or directories to scan")
    args = parser.parse_args()

    failed = False
    for raw_path in args.paths:
        path = pathlib.Path(raw_path)
        files = [path] if path.is_file() else list(path.rglob("*.md")) + list(path.rglob("*.yaml"))
        for file_path in files:
            findings = scan_text(file_path)
            if findings:
                failed = True
                print(f"[CANON-LANGUAGE] {file_path}: {findings}")

    if failed:
        print("Canon-like language found without sufficient boundary markers.")
        return 1
    print("No unbounded canon-like language found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
