from __future__ import annotations

import sys
from metadata_inventory import (
    ALLOWED_STATUS,
    REQUIRED_KEYS,
    ROOT,
    TOP50_PATHS,
    artifact_id_collisions,
    records_by_path,
)


def main() -> int:
    errors: list[str] = []
    records = records_by_path()

    for rel in TOP50_PATHS:
        record = records.get(rel)
        file_path = ROOT / rel
        if record is None:
            errors.append(f"{file_path}: file missing")
            continue
        data = record["frontmatter"]
        if not data:
            errors.append(f"{file_path}: missing frontmatter")
            continue

        missing = sorted(REQUIRED_KEYS - data.keys())
        if missing:
            errors.append(f"{file_path}: missing keys {missing}")

        status = data.get("status")
        if status and status not in ALLOWED_STATUS:
            errors.append(f"{file_path}: invalid status {status}")

        if data.get("source_of_truth") and data["source_of_truth"] != "GitHub":
            errors.append(f"{file_path}: source_of_truth must be GitHub")

    top50_collisions = {
        artifact_id: paths
        for artifact_id, paths in artifact_id_collisions(list(records.values())).items()
        if any(path in TOP50_PATHS for path in paths)
    }
    for artifact_id, paths in sorted(top50_collisions.items()):
        errors.append(f"duplicate artifact_id {artifact_id}: {sorted(paths)}")

    if errors:
        print("metadata validation: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("metadata validation: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
