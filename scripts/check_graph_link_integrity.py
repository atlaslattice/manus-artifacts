#!/usr/bin/env python3
"""
check_graph_link_integrity.py

Validates that every internal cross-link declared in docs/cross-reference-map.md
resolves to a real file in the repository.  Also scans markdown files for
`](./...)` style relative links and verifies them.

Exit codes:
  0 — all links resolve
  1 — one or more broken links detected
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Patterns that look like local markdown links: [text](path) or [text](path#anchor)
LINK_RE = re.compile(r"\[(?:[^\]]*)\]\((?!https?://)([^)#\s]+)(?:#[^)]*)?\)")


def collect_markdown_files() -> list[Path]:
    return [
        p
        for p in REPO_ROOT.rglob("*.md")
        if ".git" not in p.parts
    ]


def check_file(md_file: Path, errors: list[str]) -> None:
    text = md_file.read_text(encoding="utf-8", errors="replace")
    for match in LINK_RE.finditer(text):
        raw_target = match.group(1)
        # Resolve relative to file's directory; handle repo-root-absolute paths
        if raw_target.startswith("/"):
            resolved = REPO_ROOT / raw_target.lstrip("/")
        else:
            resolved = (md_file.parent / raw_target).resolve()

        if not resolved.exists():
            rel_src = md_file.relative_to(REPO_ROOT)
            errors.append(f"  BROKEN  {rel_src}  →  {raw_target}")


def main() -> int:
    files = collect_markdown_files()
    errors: list[str] = []

    for f in sorted(files):
        check_file(f, errors)

    if errors:
        print(f"Graph link integrity: {len(errors)} broken link(s) found:\n")
        for e in errors:
            print(e)
        return 1

    print(f"Graph link integrity: OK ({len(files)} files checked, 0 broken links)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
