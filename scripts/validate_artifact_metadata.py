from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_KEYS = {
    "artifact_id",
    "title",
    "status",
    "owner",
    "created",
    "last_updated",
    "source_of_truth",
}
ALLOWED_STATUS = {"DRAFT", "CANDIDATE", "CANONICAL", "ARCHIVED"}
TARGET_FILES = [
    "docs/ARCHITECTURE_MAP.md",
    "docs/FAQ.md",
    "docs/FOLDER_TAXONOMY_AUDIT_2026-05-27.md",
    "docs/ARTIFACT_RELATIONSHIP_TYPES.md",
    "docs/CONTRIBUTOR_QUICKSTART.md",
    "docs/ROADMAP.md",
]


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        return {}

    frontmatter = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip()
    return frontmatter


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    data = parse_frontmatter(text)
    if not data:
        return [f"{path}: missing frontmatter"]

    missing = sorted(REQUIRED_KEYS - data.keys())
    if missing:
        errors.append(f"{path}: missing keys {missing}")

    status = data.get("status")
    if status and status not in ALLOWED_STATUS:
        errors.append(f"{path}: invalid status {status}")

    if data.get("source_of_truth") and data["source_of_truth"] != "GitHub":
        errors.append(f"{path}: source_of_truth must be GitHub")

    return errors


def main() -> int:
    errors: list[str] = []
    for rel in TARGET_FILES:
        file_path = ROOT / rel
        if not file_path.exists():
            errors.append(f"{file_path}: file missing")
            continue
        errors.extend(validate_file(file_path))

    if errors:
        print("metadata validation: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("metadata validation: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
