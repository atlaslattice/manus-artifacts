#!/usr/bin/env python3
"""Validate governance metadata across markdown artifacts."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

REQUIRED_FRONTMATTER_KEYS = {
    "title",
    "artifact_id",
    "status",
    "canon_status",
    "lifecycle_state",
    "ratification_event_id",
    "trust_state",
    "owner",
    "last_updated",
    "provenance",
}
STATUS_VALUES = {"candidate", "canonical", "deprecated", "superseded", "archived", "ratified"}
CANON_VALUES = {"candidate", "ratified", "canonical", "deprecated", "superseded", "archived"}
LIFECYCLE_VALUES = {"draft", "review", "active", "maintenance", "deprecated", "archived"}
TRUST_VALUES = {"WORK", "CANDIDATE", "VERIFIED", "BLOCKED"}
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")

GOVERNANCE_GLOBS = [
    "docs/CANON_*.md",
    "docs/RATIFICATION_WORKFLOW.md",
    "docs/PROVENANCE_REQUIREMENTS.md",
    "docs/ARTIFACT_LIFECYCLE_STATES.md",
    "docs/UNIVERSAL_FRONTMATTER_SCHEMA.md",
]
LEGACY_GLOBS = [
    "docs/README.md",
    "projects/README.md",
    "reference_impl/README.md",
    "schemas/README.md",
    "tests/README.md",
]


def parse_frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    block = text[4:end]
    data: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def has_legacy_status(text: str) -> bool:
    return any(line.strip().startswith("status:") for line in text.splitlines()[:30])


def validate_frontmatter(path: Path, data: dict[str, str]) -> list[str]:
    errors: list[str] = []
    missing = REQUIRED_FRONTMATTER_KEYS - set(data)
    if missing:
        errors.append(f"{path}: missing frontmatter keys: {sorted(missing)}")
    if "status" in data and data["status"] not in STATUS_VALUES:
        errors.append(f"{path}: invalid status={data['status']}")
    if "canon_status" in data and data["canon_status"] not in CANON_VALUES:
        errors.append(f"{path}: invalid canon_status={data['canon_status']}")
    if "lifecycle_state" in data and data["lifecycle_state"] not in LIFECYCLE_VALUES:
        errors.append(f"{path}: invalid lifecycle_state={data['lifecycle_state']}")
    if "trust_state" in data and data["trust_state"] not in TRUST_VALUES:
        errors.append(f"{path}: invalid trust_state={data['trust_state']}")
    if "last_updated" in data and not DATE_PATTERN.match(data["last_updated"]):
        errors.append(f"{path}: invalid last_updated format (expected YYYY-MM-DD)")
    return errors


def collect_files(root: Path, globs: list[str]) -> set[Path]:
    files: set[Path] = set()
    for pattern in globs:
        files.update(root.glob(pattern))
    return files


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()

    governance_files = collect_files(root, GOVERNANCE_GLOBS)
    legacy_files = collect_files(root, LEGACY_GLOBS)

    errors: list[str] = []

    for file_path in sorted(governance_files):
        text = file_path.read_text(encoding="utf-8", errors="ignore")
        frontmatter = parse_frontmatter(text)
        if frontmatter is None:
            errors.append(f"{file_path.relative_to(root)}: missing YAML frontmatter")
            continue
        errors.extend(validate_frontmatter(file_path.relative_to(root), frontmatter))

    for file_path in sorted(legacy_files):
        text = file_path.read_text(encoding="utf-8", errors="ignore")
        if parse_frontmatter(text) is not None:
            continue
        if not has_legacy_status(text):
            errors.append(f"{file_path.relative_to(root)}: missing status metadata")

    if errors:
        print("Metadata validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print(
        f"Metadata validation passed: {len(governance_files)} governance files and "
        f"{len(legacy_files)} tracked markdown files checked."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
