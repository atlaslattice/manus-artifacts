#!/usr/bin/env python3
"""
ip_boundary_check.py
====================
Automated IP boundary checker for the Atlas Lattice archive.

Scans files for:
  - PII patterns (email addresses, phone numbers, SSN-like patterns)
  - Secret/credential patterns (API keys, tokens, passwords in YAML)
  - Third-party copyright markers

Does NOT write any changes. Reports only. Human review required before public release.

Usage:
    python scripts/ip_boundary_check.py
    python scripts/ip_boundary_check.py --path archive/
    python scripts/ip_boundary_check.py --path docs/ --format json
    python scripts/ip_boundary_check.py --fail-on-high  # exit 1 if HIGH severity found
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

# Regex patterns: (name, severity, regex)
PATTERNS: list[tuple[str, str, re.Pattern]] = [
    # PII
    ("email_address",        "HIGH",   re.compile(r"\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b")),
    ("phone_us",             "HIGH",   re.compile(r"\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b")),
    ("ssn_pattern",          "HIGH",   re.compile(r"\b\d{3}[-\s]\d{2}[-\s]\d{4}\b")),
    ("credit_card",          "HIGH",   re.compile(r"\b(?:4\d{3}|5[1-5]\d{2}|6011|65\d{2}|3[47]\d{2})[\s\-]?\d{4}[\s\-]?\d{4}[\s\-]?\d{4}\b")),
    # Secrets
    ("github_pat",           "HIGH",   re.compile(r"ghp_[A-Za-z0-9]{36}")),
    ("github_oauth",         "HIGH",   re.compile(r"gho_[A-Za-z0-9]{36}")),
    ("github_actions_token", "HIGH",   re.compile(r"ghs_[A-Za-z0-9]{36}")),
    ("openai_key",           "HIGH",   re.compile(r"sk-[A-Za-z0-9\-_]{32,}")),
    ("aws_access_key",       "HIGH",   re.compile(r"AKIA[A-Z0-9]{16}")),
    ("aws_secret_key",       "HIGH",   re.compile(r"(?i)aws.{0,20}secret.{0,20}['\"]?[A-Za-z0-9/+=]{40}")),
    ("private_key_header",   "HIGH",   re.compile(r"-----BEGIN (?:RSA |EC )?PRIVATE KEY-----")),
    ("password_in_yaml",     "MEDIUM", re.compile(r"(?i)password\s*:\s*['\"]?[^\s'\"]{6,}")),
    ("token_in_yaml",        "MEDIUM", re.compile(r"(?i)(?:token|secret|api_key)\s*:\s*['\"]?[A-Za-z0-9\-_\.]{16,}")),
    # IP/copyright markers
    ("copyright_notice",     "LOW",    re.compile(r"©|Copyright\s+\d{4}|All Rights Reserved", re.IGNORECASE)),
    ("proprietary_marker",   "LOW",    re.compile(r"PROPRIETARY|CONFIDENTIAL|NOT FOR DISTRIBUTION", re.IGNORECASE)),
    ("third_party_license",  "LOW",    re.compile(r"(?:Apache License|GNU GPL|Creative Commons)[^,\n]{0,80}", re.IGNORECASE)),
]

SKIP_DIRS = {".git", "node_modules", "__pycache__", ".pytest_cache"}
SKIP_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico", ".bin", ".zip", ".whl"}


def should_scan(path: Path) -> bool:
    for part in path.parts:
        if part in SKIP_DIRS:
            return False
    return path.suffix.lower() not in SKIP_EXTS


def scan_file(path: Path) -> list[dict[str, Any]]:
    """Return list of findings for a file."""
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return []

    findings = []
    lines = text.splitlines()
    for lineno, line in enumerate(lines, 1):
        for name, severity, pattern in PATTERNS:
            for m in pattern.finditer(line):
                matched = m.group()
                # Redact middle of matched value for safety
                if len(matched) > 8:
                    redacted = matched[:4] + "***" + matched[-4:]
                else:
                    redacted = "***"
                findings.append({
                    "file": str(path),
                    "line": lineno,
                    "pattern": name,
                    "severity": severity,
                    "match_redacted": redacted,
                })
    return findings


def scan_directory(scan_dir: Path, root: Path) -> list[dict[str, Any]]:
    all_findings = []
    for path in sorted(scan_dir.rglob("*")):
        if path.is_file() and should_scan(path.relative_to(root) if root in path.parents else path):
            all_findings.extend(scan_file(path))
    return all_findings


def print_report(findings: list[dict[str, Any]], scan_path: Path) -> None:
    by_severity: dict[str, list] = {"HIGH": [], "MEDIUM": [], "LOW": []}
    for f in findings:
        by_severity.setdefault(f["severity"], []).append(f)

    print(f"\n=== IP Boundary Check Report ===")
    print(f"Scanned: {scan_path}")
    print(f"Total findings: {len(findings)}")
    print(f"  HIGH:   {len(by_severity['HIGH'])}")
    print(f"  MEDIUM: {len(by_severity['MEDIUM'])}")
    print(f"  LOW:    {len(by_severity['LOW'])}")

    for sev in ["HIGH", "MEDIUM", "LOW"]:
        if by_severity[sev]:
            print(f"\n--- {sev} severity ---")
            for f in by_severity[sev]:
                rel = Path(f["file"])
                try:
                    rel = rel.relative_to(ROOT)
                except ValueError:
                    pass
                print(f"  {rel}:{f['line']}  [{f['pattern']}]  match: {f['match_redacted']}")

    if not findings:
        print("\nNo findings. Path appears clean.")
    else:
        print(f"\n⚠  Review required before public release.")
        print("   Human root must approve any public action on flagged files.")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Atlas Lattice IP boundary checker")
    parser.add_argument("--path", default=".", help="Directory or file to scan (default: repo root)")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--fail-on-high", action="store_true", help="Exit 1 if any HIGH findings")
    parser.add_argument("--fail-on-any", action="store_true", help="Exit 1 if any findings")
    parser.add_argument("--root", default=str(ROOT))
    args = parser.parse_args(argv)

    root = Path(args.root)
    scan_path = Path(args.path)
    if not scan_path.is_absolute():
        scan_path = root / scan_path

    if scan_path.is_file():
        findings = scan_file(scan_path)
    else:
        findings = scan_directory(scan_path, root)

    if args.format == "json":
        print(json.dumps(findings, indent=2))
    else:
        print_report(findings, scan_path)

    has_high = any(f["severity"] == "HIGH" for f in findings)

    if args.fail_on_any and findings:
        return 1
    if args.fail_on_high and has_high:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
