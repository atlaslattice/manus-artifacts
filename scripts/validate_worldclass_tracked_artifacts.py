from __future__ import annotations

import sys
from metadata_inventory import REQUIRED_KEYS, ROOT, records_by_path

TRACKED_PATHS = [
    "projects/aetherforge-next144-taskboard-2026-05-28.md",
    "projects/aetherforge-next12-worldclass-github-issue-seeding-pack-2026-05-29.md",
    "docs/ARTIFACT_SOURCE_OF_TRUTH_INDEX.md",
    "docs/CONTRIBUTOR_PLAYBOOK.md",
    "docs/ARCHITECTURE_CROSSWALK.md",
    "docs/QUALITY_GATES_DASHBOARD.md",
    "docs/EVIDENCE_AND_DEMONSTRATIONS.md",
    "docs/AETHERFORGE_PLAYABLE_ONBOARDING.md",
    "docs/RELEASE_RHYTHM.md",
]


def main() -> int:
    records = records_by_path()
    errors: list[str] = []

    for rel in TRACKED_PATHS:
        record = records.get(rel)
        file_path = ROOT / rel
        if record is None:
            errors.append(f"{file_path}: file missing")
            continue

        frontmatter = record["frontmatter"]
        if not frontmatter:
            errors.append(f"{file_path}: missing frontmatter")
            continue

        missing = sorted(REQUIRED_KEYS - frontmatter.keys())
        if missing:
            errors.append(f"{file_path}: missing keys {missing}")

        if frontmatter.get("source_of_truth") != "GitHub":
            errors.append(f"{file_path}: source_of_truth must be GitHub")

    if errors:
        print("worldclass tracked metadata coverage: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"worldclass tracked metadata coverage: PASS ({len(TRACKED_PATHS)}/{len(TRACKED_PATHS)} complete)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
