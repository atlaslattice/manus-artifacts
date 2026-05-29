#!/usr/bin/env python3
"""
review_state_fsm.py
===================
Atlas Lattice Review-State Finite State Machine.

States (in order):
    raw → candidate → reviewed → canon-gate → canon

Transitions:
    raw        → candidate   (any contributor via PR)
    candidate  → reviewed    (council member review)
    reviewed   → canon-gate  (council vote triggers)
    canon-gate → canon       (@atlaslattice adjudication only)
    any        → archived    (admin only)

Usage:
    # Check current review state of an artifact
    python scripts/review_state_fsm.py --file path/to/artifact.md

    # Advance state (writes back to file)
    python scripts/review_state_fsm.py --file path/to/artifact.md --advance

    # Check if transition is valid without writing
    python scripts/review_state_fsm.py --file path/to/artifact.md --advance --dry-run

    # Force a specific state (admin only)
    python scripts/review_state_fsm.py --file path/to/artifact.md --set-state reviewed

    # Validate all states in a directory
    python scripts/review_state_fsm.py --validate-dir archive/
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

# FSM definition
STATES = ["raw", "candidate", "reviewed", "canon-gate", "canon", "archived"]
TRANSITIONS: dict[str, list[str]] = {
    "raw":        ["candidate"],
    "candidate":  ["reviewed"],
    "reviewed":   ["canon-gate"],
    "canon-gate": ["canon"],
    "canon":      ["archived"],   # only via admin action
    "archived":   [],
}


class FSMError(Exception):
    pass


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


def render_frontmatter_update(original_yaml: str, updates: dict[str, str]) -> str:
    """Apply updates to YAML block string, preserving other fields."""
    lines = original_yaml.splitlines()
    updated_keys: set[str] = set()
    new_lines = []
    for line in lines:
        if ":" in line:
            key = line.split(":")[0].strip()
            if key in updates:
                val = updates[key]
                if any(c in str(val) for c in (':', '#', "'", '"', '\n')):
                    new_lines.append(f'{key}: "{val}"')
                else:
                    new_lines.append(f"{key}: {val}")
                updated_keys.add(key)
                continue
        new_lines.append(line)
    # add any new keys not found
    for key, val in updates.items():
        if key not in updated_keys:
            if any(c in str(val) for c in (':', '#', "'", '"', '\n')):
                new_lines.append(f'{key}: "{val}"')
            else:
                new_lines.append(f"{key}: {val}")
    return "\n".join(new_lines)


def load_artifact_state(path: Path) -> tuple[dict[str, str], str]:
    """Return (meta, body_text)."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    meta = parse_simple_yaml(m.group(1))
    return meta, text


def advance_state(current: str) -> str:
    """Return the next state or raise FSMError."""
    if current not in TRANSITIONS:
        raise FSMError(f"Unknown review_state: '{current}'")
    nexts = TRANSITIONS[current]
    if not nexts:
        raise FSMError(f"State '{current}' has no further transitions (terminal state).")
    return nexts[0]


def validate_state(state: str) -> bool:
    return state in STATES


def cmd_check(path: Path) -> int:
    meta, _ = load_artifact_state(path)
    current = meta.get("review_state", "(not set)")
    artifact_id = meta.get("artifact_id", path.stem)
    canon = meta.get("canon", "NO")
    print(f"\nArtifact:     {artifact_id}")
    print(f"File:         {path}")
    print(f"review_state: {current}")
    print(f"canon:        {canon}")
    if current in TRANSITIONS:
        nexts = TRANSITIONS[current]
        print(f"Next states:  {nexts if nexts else '(terminal)'}")
    print()
    return 0


def cmd_advance(path: Path, dry_run: bool = False) -> int:
    text = path.read_text(encoding="utf-8", errors="ignore")
    m = FRONTMATTER_RE.match(text)
    if not m:
        print(f"ERROR: No frontmatter found in {path}", file=sys.stderr)
        return 1

    meta = parse_simple_yaml(m.group(1))
    current = meta.get("review_state", "raw")

    try:
        next_state = advance_state(current)
    except FSMError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    print(f"  {path.name}: {current} → {next_state}")

    if not dry_run:
        new_yaml = render_frontmatter_update(m.group(1), {
            "review_state": next_state,
            "last_updated": date.today().isoformat(),
        })
        new_text = f"---\n{new_yaml}\n---\n" + text[m.end():]
        path.write_text(new_text, encoding="utf-8")
        print(f"  Written.")
    else:
        print(f"  (dry-run — not written)")

    return 0


def cmd_set_state(path: Path, new_state: str, dry_run: bool = False) -> int:
    if not validate_state(new_state):
        print(f"ERROR: Invalid state '{new_state}'. Valid: {STATES}", file=sys.stderr)
        return 1

    text = path.read_text(encoding="utf-8", errors="ignore")
    m = FRONTMATTER_RE.match(text)
    if not m:
        print(f"ERROR: No frontmatter in {path}", file=sys.stderr)
        return 1

    meta = parse_simple_yaml(m.group(1))
    current = meta.get("review_state", "(not set)")

    print(f"  {path.name}: {current} → {new_state} (forced)")

    if not dry_run:
        new_yaml = render_frontmatter_update(m.group(1), {
            "review_state": new_state,
            "last_updated": date.today().isoformat(),
        })
        new_text = f"---\n{new_yaml}\n---\n" + text[m.end():]
        path.write_text(new_text, encoding="utf-8")
    else:
        print("  (dry-run — not written)")

    return 0


def cmd_validate_dir(scan_dir: Path, root: Path) -> int:
    invalid = []
    state_counts: dict[str, int] = {}

    for md_file in sorted(scan_dir.rglob("*.md")):
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
        state = meta.get("review_state", "")
        if not state:
            continue
        if not validate_state(state):
            invalid.append((rel, state))
        state_counts[state] = state_counts.get(state, 0) + 1

    print(f"\nReview state counts in {scan_dir}:")
    for s in STATES:
        count = state_counts.get(s, 0)
        if count:
            print(f"  {s:<12} {count}")

    if invalid:
        print(f"\nINVALID review_state values ({len(invalid)}):")
        for path, state in invalid:
            print(f"  {path}: '{state}'")
        return 1
    else:
        print("\nAll review_state values are valid.")
        return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Atlas Lattice review-state FSM")
    parser.add_argument("--file", metavar="PATH", help="Target artifact file")
    parser.add_argument("--advance", action="store_true", help="Advance state to next")
    parser.add_argument("--set-state", metavar="STATE", help="Force a specific state (admin)")
    parser.add_argument("--dry-run", action="store_true", help="Don't write changes")
    parser.add_argument("--validate-dir", metavar="DIR", help="Validate all states in a dir")
    parser.add_argument("--list-states", action="store_true", help="List all valid states")
    parser.add_argument("--root", default=str(ROOT))
    args = parser.parse_args(argv)

    root = Path(args.root)

    if args.list_states:
        print("\nAtlas Lattice review_state FSM:\n")
        for state in STATES:
            nexts = TRANSITIONS.get(state, [])
            arrow = f" → {nexts[0]}" if nexts else " (terminal)"
            print(f"  {state}{arrow}")
        print()
        return 0

    if args.validate_dir:
        scan_dir = Path(args.validate_dir)
        if not scan_dir.is_absolute():
            scan_dir = root / scan_dir
        return cmd_validate_dir(scan_dir, root)

    if not args.file:
        parser.print_help()
        return 1

    target = Path(args.file)
    if not target.is_absolute():
        target = root / target
    if not target.exists():
        print(f"ERROR: File not found: {target}", file=sys.stderr)
        return 1

    if args.advance:
        return cmd_advance(target, dry_run=args.dry_run)
    elif args.set_state:
        return cmd_set_state(target, args.set_state, dry_run=args.dry_run)
    else:
        return cmd_check(target)


if __name__ == "__main__":
    sys.exit(main())
