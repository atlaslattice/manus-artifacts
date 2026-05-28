#!/usr/bin/env python3
"""
build_lattice_global_index.py

Scans the repository and emits docs/LATTICE_GLOBAL_INDEX.md — a
machine-readable table of every indexed markdown artifact with its
detected metadata fields.

The index is regenerated on every CI run so it stays current.
"""
from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = REPO_ROOT / "docs" / "LATTICE_GLOBAL_INDEX.md"

INDEX_DIRS = [
    "archive/boot",
    "archive/spec",
    "docs",
    "projects",
    "schemas",
    "reference_impl",
]

STATUS_RE = re.compile(r"STATUS:\s*(.+)", re.IGNORECASE)
HEADING_RE = re.compile(r"^#\s+(.+)", re.MULTILINE)


def extract_meta(f: Path) -> dict:
    text = f.read_text(encoding="utf-8", errors="replace")
    header = "\n".join(text.splitlines()[:60])

    status_m = STATUS_RE.search(header)
    heading_m = HEADING_RE.search(text)

    return {
        "path": str(f.relative_to(REPO_ROOT)),
        "title": heading_m.group(1).strip() if heading_m else f.stem,
        "status": status_m.group(1).strip() if status_m else "unknown",
        "size_lines": len(text.splitlines()),
    }


def collect_files() -> list[Path]:
    files = []
    for d in INDEX_DIRS:
        target = REPO_ROOT / d
        if target.exists():
            files.extend(
                p
                for p in target.rglob("*.md")
                if ".git" not in p.parts
            )
    return sorted(files)


def build_index() -> str:
    files = collect_files()
    now = datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    rows = [extract_meta(f) for f in files]

    lines = [
        "# Lattice Global Index",
        "",
        "```",
        "STATUS: CANDIDATE — auto-generated, not canon",
        f"GENERATED: {now}",
        f"TOTAL_ARTIFACTS: {len(rows)}",
        "```",
        "",
        "This file is **auto-generated** by `scripts/build_lattice_global_index.py`.",
        "Do not edit manually.",
        "",
        "## Artifact Table",
        "",
        "| # | Path | Title | Status | Lines |",
        "|---|------|-------|--------|-------|",
    ]

    for i, row in enumerate(rows, start=1):
        lines.append(
            f"| {i} | `{row['path']}` | {row['title']} | {row['status']} | {row['size_lines']} |"
        )

    lines += [
        "",
        "---",
        "",
        f"*Auto-generated at {now}. Total artifacts indexed: {len(rows)}.*",
    ]

    return "\n".join(lines) + "\n"


def main() -> int:
    index_content = build_index()
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(index_content, encoding="utf-8")
    print(f"Lattice global index written to {OUTPUT_FILE.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
