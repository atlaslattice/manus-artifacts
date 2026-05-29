#!/usr/bin/env python3
"""
validate_raw_export_status.py

Candidate validator stub.

Checks YAML-like files for raw_export_status values outside the approved set.

STATUS: scaffold only — not deployed CI.
"""

from __future__ import annotations

import argparse
import pathlib
import re

ALLOWED = {
    "not_exported",
    "partial_export",
    "full_raw_export_attached",
    "full_raw_export_hashed",
    "redacted_raw_export_attached",
    "unavailable",
}

STATUS_RE = re.compile(r"raw_export_status:\s*([A-Za-z0-9_\-]+)")


def scan_file(path: pathlib.Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    findings: list[str] = []
    for match in STATUS_RE.finditer(text):
        value = match.group(1).strip()
        if value not in ALLOWED:
            findings.append(value)
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate raw_export_status values.")
    parser.add_argument("paths", nargs="+", help="Files or directories to scan")
    args = parser.parse_args()

    failed = False
    for raw_path in args.paths:
        path = pathlib.Path(raw_path)
        files = [path] if path.is_file() else list(path.rglob("*.md")) + list(path.rglob("*.yaml"))
        for file_path in files:
            findings = scan_file(file_path)
            if findings:
                failed = True
                print(f"[RAW-EXPORT-STATUS] {file_path}: invalid values {findings}")

    if failed:
        return 1
    print("All raw_export_status values are approved or absent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
