"""Wave 3 frontmatter backfill script.

Injects standard YAML frontmatter into markdown files that are missing it.
Normalises source_of_truth to "GitHub" on files that already have partial
frontmatter. Skips quarantine-flagged and exception paths.

Usage:
    python scripts/backfill_frontmatter.py [--batch 1|2|all] [--dry-run]

Batch 1  → next 100 paths (Task 25)
Batch 2  → next 200 paths after batch 1 (Task 26)
all      → both batches in one pass
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Allow running from repo root or scripts/ directory
sys.path.insert(0, str(Path(__file__).resolve().parent))

from metadata_inventory import (
    BACKFILL_DATE,
    EXCEPTION_PATHS,
    ROOT,
    TOP50_PATHS,
    domain_priority,
    extract_title,
    inventory_records,
    next100_paths,
    normalize_artifact_id,
    parse_frontmatter,
)

# These paths require owner action (quarantine routing) before public backfill.
QUARANTINE_PENDING: set[str] = {
    "projects/free-bank/banking-revolution-archive.md",
}

BACKFILL_DATE_WAVE3 = "2026-05-29"


def build_frontmatter_block(artifact_id: str, title: str) -> str:
    lines = [
        "---",
        f"artifact_id: {artifact_id}",
        f"title: {title}",
        "status: CANDIDATE",
        "owner: atlaslattice",
        f"created: {BACKFILL_DATE_WAVE3}",
        f"last_updated: {BACKFILL_DATE_WAVE3}",
        "source_of_truth: GitHub",
        "---",
        "",
    ]
    return "\n".join(lines)


def inject_frontmatter(path: Path) -> bool:
    """Inject frontmatter if missing; normalize source_of_truth if needed.

    Returns True if the file was modified.
    """
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)

    if fm:
        # File already has frontmatter — just normalise source_of_truth if wrong.
        if fm.get("source_of_truth") and fm["source_of_truth"] != "GitHub":
            new_text = re.sub(
                r"^(source_of_truth:\s*).*$",
                r"\1GitHub",
                text,
                flags=re.MULTILINE,
            )
            if new_text != text:
                path.write_text(new_text, encoding="utf-8")
                return True
        return False

    # No frontmatter — inject it.
    rel = path.relative_to(ROOT).as_posix()
    title = extract_title(path, text)
    artifact_id = normalize_artifact_id(path).replace(BACKFILL_DATE, BACKFILL_DATE_WAVE3)
    block = build_frontmatter_block(artifact_id, title)
    path.write_text(block + text, encoding="utf-8")
    return True


def next200_paths(records: list[dict], n100: list[str]) -> list[str]:
    """Return the 200 paths immediately after the first-100 batch."""
    seen = set(TOP50_PATHS) | set(EXCEPTION_PATHS) | set(n100)
    candidates = [r for r in records if r["path"] not in seen]
    candidates.sort(
        key=lambda r: (
            0 if r["missing_keys"] else 1,
            domain_priority(str(r["path"])),
        )
    )
    return [str(r["path"]) for r in candidates[:200]]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--batch",
        choices=["1", "2", "all"],
        default="all",
        help="Which batch to process (default: all)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report what would change without writing files",
    )
    args = parser.parse_args(argv)

    records = inventory_records()
    n100 = next100_paths(records)
    n200 = next200_paths(records, n100)

    target_paths: list[str] = []
    if args.batch in ("1", "all"):
        target_paths += n100
    if args.batch in ("2", "all"):
        target_paths += n200

    modified = 0
    skipped_quarantine = 0
    skipped_exception = 0
    already_complete = 0

    for rel in target_paths:
        if rel in QUARANTINE_PENDING:
            print(f"  [QUARANTINE-SKIP] {rel}")
            skipped_quarantine += 1
            continue
        if rel in EXCEPTION_PATHS:
            print(f"  [EXCEPTION-SKIP] {rel}")
            skipped_exception += 1
            continue

        path = ROOT / rel
        if not path.exists():
            print(f"  [MISSING] {rel}")
            continue

        if args.dry_run:
            text = path.read_text(encoding="utf-8")
            fm = parse_frontmatter(text)
            if not fm:
                print(f"  [WOULD-ADD] {rel}")
                modified += 1
            elif fm.get("source_of_truth") and fm["source_of_truth"] != "GitHub":
                print(f"  [WOULD-FIX-SOURCE] {rel}")
                modified += 1
            else:
                already_complete += 1
        else:
            changed = inject_frontmatter(path)
            if changed:
                print(f"  [BACKFILLED] {rel}")
                modified += 1
            else:
                already_complete += 1

    action = "Would modify" if args.dry_run else "Modified"
    print(
        f"\n{action} {modified} files "
        f"({skipped_quarantine} quarantine-skipped, "
        f"{skipped_exception} exception-skipped, "
        f"{already_complete} already complete)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
