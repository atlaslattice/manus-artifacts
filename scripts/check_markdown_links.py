#!/usr/bin/env python3
"""
check_markdown_links.py

Scans all markdown files in the repository for broken relative links.
Prints a report and exits non-zero if any broken links are found.

This is the surface-level link checker; check_graph_link_integrity.py
covers the semantic graph layer.

Exit codes:
  0 — no broken links
  1 — one or more broken links found
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

LINK_RE = re.compile(
    r"\[(?:[^\]]*)\]\((?!https?://)(?!mailto:)([^)#\s]+)(?:#[^)]*)?\)"
)

SKIP_DIRS = {".git", "node_modules", "__pycache__"}


def collect_markdown_files() -> list[Path]:
    return [
        p
        for p in REPO_ROOT.rglob("*.md")
        if not any(part in SKIP_DIRS for part in p.parts)
    ]


def check_file(md_file: Path) -> list[tuple[int, str]]:
    broken: list[tuple[int, str]] = []
    lines = md_file.read_text(encoding="utf-8", errors="replace").splitlines()
    for lineno, line in enumerate(lines, start=1):
        for match in LINK_RE.finditer(line):
            raw = match.group(1)
            if raw.startswith("/"):
                resolved = REPO_ROOT / raw.lstrip("/")
            else:
                resolved = (md_file.parent / raw).resolve()
            if not resolved.exists():
                broken.append((lineno, raw))
    return broken


def main() -> int:
    files = collect_markdown_files()
    total_broken = 0
    report_lines: list[str] = []

    for f in sorted(files):
        issues = check_file(f)
        if issues:
            rel = f.relative_to(REPO_ROOT)
            for lineno, target in issues:
                report_lines.append(f"  {rel}:{lineno}  →  {target}")
                total_broken += 1

    print(f"Markdown link check: {len(files)} files scanned")
    if total_broken:
        print(f"  {total_broken} broken link(s) found:\n")
        for line in report_lines:
            print(line)
        return 1

    print("  No broken links found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
