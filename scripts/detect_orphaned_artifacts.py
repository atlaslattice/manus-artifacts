#!/usr/bin/env python3
"""
detect_orphaned_artifacts.py

An artifact is "orphaned" if no other markdown file in the repository
links to it (i.e., it has no inbound edges in the link graph).

README.md files and files listed in the global index are excluded from
the orphan check, as they are discovery entry points by convention.

Exit codes:
  0 — no orphans (or only expected root-level orphans)
  1 — orphaned artifacts found above threshold
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Files we never count as orphans (they are roots/discovery points)
EXEMPT_NAMES = {"README.md", "LATTICE_GLOBAL_INDEX.md"}
EXEMPT_DIRS = {".git", "node_modules", "__pycache__"}

# Fraction of total files allowed to be orphans before we fail (0.90 = 90%)
# NOTE: current repo baseline is ~82%; set threshold to 90% to allow headroom
# while catching any regression that dramatically increases orphan count.
ORPHAN_THRESHOLD = 0.90

LINK_RE = re.compile(
    r"\[(?:[^\]]*)\]\((?!https?://)(?!mailto:)([^)#\s]+)(?:#[^)]*)?\)"
)


def collect_markdown_files() -> list[Path]:
    return [
        p
        for p in REPO_ROOT.rglob("*.md")
        if not any(part in EXEMPT_DIRS for part in p.parts)
    ]


def build_link_graph(files: list[Path]) -> dict[Path, set[Path]]:
    """Return {source: {resolved_target, ...}} for all local links."""
    graph: dict[Path, set[Path]] = {f: set() for f in files}
    for f in files:
        text = f.read_text(encoding="utf-8", errors="replace")
        for match in LINK_RE.finditer(text):
            raw = match.group(1)
            if raw.startswith("/"):
                resolved = (REPO_ROOT / raw.lstrip("/")).resolve()
            else:
                resolved = (f.parent / raw).resolve()
            if resolved.suffix == ".md" and resolved in graph:
                graph[f].add(resolved)
    return graph


def find_orphans(files: list[Path], graph: dict[Path, set[Path]]) -> list[Path]:
    linked_to: set[Path] = set()
    for targets in graph.values():
        linked_to.update(targets)

    orphans = []
    for f in files:
        if f.name in EXEMPT_NAMES:
            continue
        # Top-level files are exempt from orphan check (they are roots)
        if f.parent == REPO_ROOT:
            continue
        if f not in linked_to:
            orphans.append(f)
    return sorted(orphans)


def main() -> int:
    files = collect_markdown_files()
    graph = build_link_graph(files)
    orphans = find_orphans(files, graph)

    eligible = [
        f for f in files
        if f.name not in EXEMPT_NAMES and f.parent != REPO_ROOT
    ]
    total_eligible = len(eligible)
    orphan_count = len(orphans)
    ratio = orphan_count / total_eligible if total_eligible else 0

    print(f"Orphan detection: {total_eligible} eligible files checked")
    print(f"  Orphans: {orphan_count} ({ratio:.0%})")

    if orphans:
        print("\n  Orphaned artifacts (no inbound links):")
        for o in orphans:
            print(f"    {o.relative_to(REPO_ROOT)}")

    if ratio > ORPHAN_THRESHOLD:
        print(
            f"\nFAIL: orphan ratio {ratio:.0%} exceeds threshold {ORPHAN_THRESHOLD:.0%}"
        )
        return 1

    print(
        f"\nPASS: orphan ratio {ratio:.0%} within threshold {ORPHAN_THRESHOLD:.0%}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
