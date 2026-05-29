#!/usr/bin/env python3
"""
ingest_artifact.py
==================
Batch metadata ingest pipeline for the Atlas Lattice archive.

For each input file (Markdown or JSON), this script:
  1. Reads existing YAML frontmatter (if present)
  2. Generates a new artifact_id if missing
  3. Assigns a candidate H-S-N coordinate based on the file's path/domain
  4. Sets review_state = "raw" if not already set
  5. Writes back the updated frontmatter

Usage:
    # Ingest a single file
    python scripts/ingest_artifact.py path/to/artifact.md

    # Ingest all un-ingested Markdown files in a directory
    python scripts/ingest_artifact.py --scan archive/

    # Dry-run (show what would change, don't write)
    python scripts/ingest_artifact.py --scan archive/ --dry-run

    # Show the H-S-N domain map
    python scripts/ingest_artifact.py --list-domains
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

# Path-prefix → (house, sphere, default_status) mapping
# House numbers correspond to the 12-House schema in docs/LATTICE_HYPERCUBE_12x12x12.md
PATH_DOMAIN_MAP: list[tuple[str, int, int, str]] = [
    # (path_prefix, house, sphere, label)
    ("archive/synthesis/data",  1, 12, "CANDIDATE"),   # seed data → H01-S12
    ("archive/spec",            9,  1, "CANDIDATE"),   # specs     → H09-S01
    ("archive/architecture",    9,  2, "CANDIDATE"),
    ("archive/governance",     11,  1, "CANDIDATE"),
    ("archive/boot",            9,  3, "CANDIDATE"),
    ("archive/deployments",     9,  4, "CANDIDATE"),
    ("archive/integrations",    9,  5, "CANDIDATE"),
    ("archive/play",           12, 11, "CANDIDATE"),   # play/dream → H12-S11
    ("archive/simulation",     12, 10, "CANDIDATE"),
    ("archive/culture",         8,  1, "CANDIDATE"),   # culture → H08 human knowledge
    ("archive/assessments",    11,  2, "CANDIDATE"),
    ("archive/chatlogs",        9,  6, "CANDIDATE"),
    ("archive/provenance",     10,  1, "CANDIDATE"),   # IP lineage → H10
    ("archive/knowledge_graph", 9,  7, "CANDIDATE"),
    ("docs/governance",        11,  3, "CANDIDATE"),
    ("docs/security",          11,  4, "CANDIDATE"),
    ("docs",                    9,  8, "CANDIDATE"),
    ("projects",                9,  9, "CANDIDATE"),
    ("council",                11,  5, "CANDIDATE"),
    ("council-reviews",        11,  6, "CANDIDATE"),
    ("research",                8,  2, "CANDIDATE"),
    ("health",                  8,  3, "CANDIDATE"),
    ("schemas",                 9, 10, "CANDIDATE"),
    ("reference_impl",          9, 11, "CANDIDATE"),
    ("tests",                  11,  7, "CANDIDATE"),
    ("codebases",               9, 12, "CANDIDATE"),
    ("manus-vault",            10,  2, "CANDIDATE"),
]

REVIEW_STATES = ["raw", "candidate", "reviewed", "canon-gate", "canon"]


def path_to_domain(rel_path: str) -> tuple[int, int, str]:
    """Return (house, sphere, status) for a repo-relative path."""
    for prefix, h, s, status in PATH_DOMAIN_MAP:
        if rel_path.startswith(prefix):
            return h, s, status
    return 12, 12, "CANDIDATE"  # fallback: H12-S12 (meta/uncategorised)


def next_node_for_cell(h: int, s: int, existing_coords: set[str]) -> int:
    """Find the next free N slot for a given H-S cell."""
    for n in range(1, 13):
        coord = f"H{h:02d}-S{s:02d}-N{n:02d}"
        if coord not in existing_coords:
            return n
    return 12  # all slots taken, reuse N12 (addresses are not unique ownership)


def slug_from_path(path: Path) -> str:
    """Generate a clean artifact_id slug from a file path."""
    stem = path.stem.upper()
    # Remove date suffixes like _2026-05-29
    stem = re.sub(r"_\d{4}-\d{2}-\d{2}$", "", stem)
    # Replace non-alphanumeric with -
    slug = re.sub(r"[^A-Z0-9]+", "-", stem).strip("-")
    today = date.today().isoformat()
    return f"ARTIFACT-{slug}-{today}"


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


def render_frontmatter(meta: dict[str, Any]) -> str:
    """Render a YAML frontmatter block (simple key: value only)."""
    lines = ["---"]
    field_order = [
        "artifact_id", "title", "status", "owner", "created", "last_updated",
        "source_of_truth", "canon", "domain", "hsn_coordinate", "review_state",
    ]
    written = set()
    for key in field_order:
        if key in meta:
            val = meta[key]
            if any(c in str(val) for c in (':', '#', "'", '"', '\n')):
                lines.append(f'{key}: "{val}"')
            else:
                lines.append(f"{key}: {val}")
            written.add(key)
    # remaining keys
    for key, val in meta.items():
        if key not in written:
            if any(c in str(val) for c in (':', '#', "'", '"', '\n')):
                lines.append(f'{key}: "{val}"')
            else:
                lines.append(f"{key}: {val}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def ingest_file(
    md_file: Path,
    root: Path,
    existing_coords: set[str],
    dry_run: bool = False,
) -> tuple[bool, str]:
    """
    Ingest a single Markdown file.

    Returns (changed: bool, message: str).
    """
    rel = md_file.relative_to(root).as_posix()
    try:
        text = md_file.read_text(encoding="utf-8", errors="ignore")
    except OSError as e:
        return False, f"ERROR reading {rel}: {e}"

    m = FRONTMATTER_RE.match(text)
    body = text[m.end():] if m else text
    meta: dict[str, Any] = {}
    if m:
        meta = dict(parse_simple_yaml(m.group(1)))

    changed = False

    # 1. artifact_id
    if not meta.get("artifact_id"):
        meta["artifact_id"] = slug_from_path(md_file)
        changed = True

    # 2. status
    if not meta.get("status"):
        _, _, status = path_to_domain(rel)
        meta["status"] = status
        changed = True

    # 3. owner
    if not meta.get("owner"):
        meta["owner"] = "atlaslattice"
        changed = True

    # 4. created
    if not meta.get("created"):
        meta["created"] = date.today().isoformat()
        changed = True

    # 5. last_updated
    meta["last_updated"] = date.today().isoformat()

    # 6. source_of_truth
    if not meta.get("source_of_truth"):
        meta["source_of_truth"] = "GitHub"
        changed = True

    # 7. canon
    if "canon" not in meta:
        meta["canon"] = "NO"
        changed = True

    # 8. review_state
    if not meta.get("review_state"):
        meta["review_state"] = "raw"
        changed = True

    # 9. hsn_coordinate
    if not meta.get("hsn_coordinate"):
        h, s, _ = path_to_domain(rel)
        n = next_node_for_cell(h, s, existing_coords)
        coord = f"H{h:02d}-S{s:02d}-N{n:02d}"
        meta["hsn_coordinate"] = coord
        existing_coords.add(coord)
        changed = True

    if not changed:
        return False, f"  skip (already ingested): {rel}"

    # Rebuild file
    new_text = render_frontmatter(meta) + body

    if not dry_run:
        md_file.write_text(new_text, encoding="utf-8")

    return True, f"  {'[dry]' if dry_run else 'ingested'}: {rel}  →  {meta.get('hsn_coordinate','')} [{meta.get('review_state','')}]"


def collect_existing_coords(root: Path) -> set[str]:
    """Scan repo for all existing H-S-N coordinates."""
    coords: set[str] = set()
    hsn_re = re.compile(r"H\d{2}-S\d{2}-N\d{2}")
    for md_file in root.rglob("*.md"):
        rel = md_file.relative_to(root).as_posix()
        if rel.startswith(".git/"):
            continue
        try:
            text = md_file.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        m = FRONTMATTER_RE.match(text)
        if m:
            parsed = parse_simple_yaml(m.group(1))
            coord = parsed.get("hsn_coordinate", "")
            if coord and hsn_re.match(coord):
                coords.add(coord)
    return set(coords)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Ingest artifacts into the Atlas Lattice")
    parser.add_argument("files", nargs="*", help="Specific Markdown files to ingest")
    parser.add_argument("--scan", metavar="DIR", help="Scan a directory recursively")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without writing")
    parser.add_argument("--list-domains", action="store_true", help="Print the H-S-N domain map")
    parser.add_argument("--root", default=str(ROOT))
    args = parser.parse_args(argv)

    root = Path(args.root)

    if args.list_domains:
        print("\n=== Ingest Domain Map (path prefix → H-S-N) ===\n")
        for prefix, h, s, status in PATH_DOMAIN_MAP:
            print(f"  {prefix:<35} → H{h:02d}-S{s:02d}  ({status})")
        print()
        return 0

    existing_coords = collect_existing_coords(root)
    print(f"Pre-scan: {len(existing_coords)} existing H-S-N coordinates found\n")

    target_files: list[Path] = []

    if args.scan:
        scan_dir = Path(args.scan)
        if not scan_dir.is_absolute():
            scan_dir = root / scan_dir
        for f in scan_dir.rglob("*.md"):
            if not f.relative_to(root).as_posix().startswith(".git/"):
                target_files.append(f)
    else:
        for fp in args.files:
            p = Path(fp)
            if not p.is_absolute():
                p = root / p
            target_files.append(p)

    if not target_files:
        parser.print_help()
        return 1

    ingested = 0
    skipped = 0
    for f in sorted(target_files):
        changed, msg = ingest_file(f, root, existing_coords, dry_run=args.dry_run)
        print(msg)
        if changed:
            ingested += 1
        else:
            skipped += 1

    print(f"\nDone: {ingested} ingested, {skipped} already complete.")
    if args.dry_run:
        print("(dry-run — no files written)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
