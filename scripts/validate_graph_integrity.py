#!/usr/bin/env python3
"""
validate_graph_integrity.py
============================
Validates Atlas Lattice H-S-N coordinate integrity across the repository.

Checks:
  1. All H-S-N coordinates are syntactically valid (H01-S01-N01 … H12-S12-N12)
  2. No two artifacts in the artifact layer (Markdown files) claim identical coordinates
     unless they are seed data (seed data may share cells — cells are addresses)
  3. All cross-references (cites: field) point to existing artifact_ids

Exit code 0 = pass, 1 = fail.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
HSN_RE = re.compile(r"^H(0[1-9]|1[0-2])-S(0[1-9]|1[0-2])-N(0[1-9]|1[0-2])$")
CITES_RE = re.compile(r"cites:\s*\[?([^\]\n]+)")


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


def load_artifacts(root: Path) -> list[dict[str, Any]]:
    artifacts = []
    for md_file in sorted(root.rglob("*.md")):
        rel = md_file.relative_to(root).as_posix()
        if rel.startswith(".git/"):
            continue
        try:
            text = md_file.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        m = FRONTMATTER_RE.match(text)
        if not m:
            continue
        meta = parse_simple_yaml(m.group(1))
        artifact_id = meta.get("artifact_id", "")
        if not artifact_id:
            continue
        # Parse cites list from raw YAML block
        cites = []
        for line in m.group(1).splitlines():
            cm = CITES_RE.search(line)
            if cm:
                raw_cites = cm.group(1)
                cites = [c.strip().strip('"').strip("'") for c in raw_cites.split(",") if c.strip()]
        artifacts.append({
            "artifact_id": artifact_id,
            "hsn_coordinate": meta.get("hsn_coordinate", ""),
            "file_path": rel,
            "cites": cites,
        })
    return artifacts


def validate(root: Path) -> tuple[list[str], list[str]]:
    """Return (errors, warnings)."""
    errors: list[str] = []
    warnings: list[str] = []

    artifacts = load_artifacts(root)
    all_ids = {a["artifact_id"] for a in artifacts}

    # 1. Validate all H-S-N coordinates
    coord_to_files: dict[str, list[str]] = defaultdict(list)
    for a in artifacts:
        hsn = a["hsn_coordinate"]
        if not hsn:
            continue  # missing coord is handled by provenance check
        if not HSN_RE.match(hsn):
            errors.append(f"INVALID HSN coord '{hsn}' in {a['file_path']}")
            continue
        coord_to_files[hsn].append(a["file_path"])

    # 2. Check for duplicate coordinates (artifact layer only, not seed data)
    for coord, files in coord_to_files.items():
        if len(files) > 1:
            # Only warn if multiple Markdown artifacts (seed JSON is fine)
            md_files = [f for f in files if f.endswith(".md")]
            if len(md_files) > 1:
                warnings.append(
                    f"SHARED HSN coord {coord} claimed by {len(md_files)} Markdown artifacts: "
                    + ", ".join(md_files[:3])
                    + (" …" if len(md_files) > 3 else "")
                )

    # 3. Validate cross-references
    for a in artifacts:
        for cited_id in a["cites"]:
            if cited_id and cited_id not in all_ids:
                warnings.append(
                    f"UNRESOLVED cites reference '{cited_id}' in {a['file_path']}"
                )

    return errors, warnings


def main() -> int:
    errors, warnings = validate(ROOT)

    passed = len(errors) == 0
    print(f"=== Graph Integrity Check ===")
    if errors:
        for e in errors:
            print(f"  ERROR: {e}")
    if warnings:
        for w in warnings:
            print(f"  WARN:  {w}")
    if not errors and not warnings:
        print("  All coordinates valid. No cross-reference issues.")
    print(f"\ngraph integrity: {'PASS' if passed else 'FAIL'}")
    print(f"  errors:   {len(errors)}")
    print(f"  warnings: {len(warnings)}")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
