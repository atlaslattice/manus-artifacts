#!/usr/bin/env python3
"""
check_docs_layout_structure.py

Axis #36 docs-layout linter:
- verifies required docs IA/security artifacts exist
- verifies docs/index.md contains key navigation sections
- verifies every docs/**/*.md file has an H1 heading

Exit codes:
  0 — layout checks pass
  1 — one or more layout checks fail
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_ROOT = REPO_ROOT / "docs"

REQUIRED_DOC_PATHS = [
    "docs/index.md",
    "docs/mission-vision.md",
    "docs/owner-settings-action-list.md",
    "docs/known-issues-errata.md",
    "docs/security/INCIDENT_RESPONSE_RUNBOOK_LEAKS.md",
    "docs/security/SIGNED_TAG_RELEASE_POLICY.md",
    "docs/security/DEPENDENCY_VULNERABILITY_TRIAGE_SLA.md",
    "docs/security/LICENSE_COMPLIANCE_SCAN_POLICY.md",
    "docs/security/ARTIFACT_INTEGRITY_CHECKSUM_POLICY.md",
    "docs/security/REPO_PUBLICATION_THREAT_MODEL.md",
]

REQUIRED_INDEX_SECTION_HEADERS = [
    "## Start Here",
    "## Core Domains",
    "## Program and Execution Boards",
    "## Information Architecture Standards",
    "## Pre-Flight Security and Publication Artifacts",
]


def has_h1_heading(md_file: Path) -> bool:
    text = md_file.read_text(encoding="utf-8", errors="replace")
    return any(line.startswith("# ") for line in text.splitlines())


def main() -> int:
    failures: list[str] = []

    if not DOCS_ROOT.exists():
        print("FAIL: docs/ directory not found")
        return 1

    for rel in REQUIRED_DOC_PATHS:
        target = REPO_ROOT / rel
        if not target.exists():
            failures.append(f"missing required docs artifact: {rel}")

    index_file = REPO_ROOT / "docs/index.md"
    if index_file.exists():
        index_text = index_file.read_text(encoding="utf-8", errors="replace")
        for section in REQUIRED_INDEX_SECTION_HEADERS:
            if section not in index_text:
                failures.append(f"docs/index.md missing section header: {section}")
    else:
        failures.append("missing required docs artifact: docs/index.md")

    docs_md_files = sorted(DOCS_ROOT.rglob("*.md"))
    for md_file in docs_md_files:
        if not has_h1_heading(md_file):
            failures.append(
                f"missing H1 heading in {md_file.relative_to(REPO_ROOT)}"
            )

    print(f"Docs layout lint: {len(docs_md_files)} docs markdown files scanned")
    if failures:
        print(f"  FAILURES: {len(failures)}\n")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    print("  PASS: docs layout structure checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
