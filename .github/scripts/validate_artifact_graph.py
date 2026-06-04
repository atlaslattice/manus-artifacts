#!/usr/bin/env python3
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = REPO_ROOT / "docs/knowledge-graph/artifact_registry.v0_1.json"
TAXONOMY_PATH = REPO_ROOT / "docs/knowledge-graph/artifact_taxonomy.v0_1.json"


def fail(message: str) -> None:
    print(f"❌ {message}")
    sys.exit(1)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"Missing file: {path}")
    except json.JSONDecodeError as exc:
        fail(f"Invalid JSON in {path}: {exc}")


def main() -> None:
    taxonomy = load_json(TAXONOMY_PATH)
    registry = load_json(REGISTRY_PATH)

    allowed_types = {item["type"] for item in taxonomy.get("taxonomy", []) if isinstance(item, dict) and "type" in item}
    allowed_states = set(taxonomy.get("lifecycle_states", []))
    required_fields = taxonomy.get("required_metadata_fields", [])

    artifacts = registry.get("artifacts", [])
    if not artifacts:
        fail("Registry has no artifacts")

    ids = []
    id_set = set()

    for artifact in artifacts:
        for field in required_fields:
            if field not in artifact:
                fail(f"Artifact missing required field '{field}': {artifact}")

        artifact_id = artifact["id"]
        if artifact_id in id_set:
            fail(f"Duplicate artifact id: {artifact_id}")
        id_set.add(artifact_id)
        ids.append(artifact_id)

        if artifact["artifact_type"] not in allowed_types:
            fail(f"Invalid artifact_type '{artifact['artifact_type']}' for {artifact_id}")

        if artifact["status"] not in allowed_states:
            fail(f"Invalid lifecycle state '{artifact['status']}' for {artifact_id}")

        rel_path = REPO_ROOT / artifact["path"]
        if not rel_path.exists():
            fail(f"Artifact path does not exist for {artifact_id}: {artifact['path']}")

        links = artifact.get("links", [])
        if not isinstance(links, list) or not links:
            fail(f"Artifact {artifact_id} must include at least one link")

        for link in links:
            if not isinstance(link, dict) or "relation" not in link or "target_id" not in link:
                fail(f"Invalid link in {artifact_id}: {link}")

    for artifact in artifacts:
        for link in artifact["links"]:
            if link["target_id"] not in id_set:
                fail(
                    f"Artifact {artifact['id']} references unknown target_id {link['target_id']}"
                )

    declared_count = registry.get("artifact_count")
    if declared_count != len(artifacts):
        fail(f"artifact_count={declared_count} does not match actual={len(artifacts)}")

    print("✅ Artifact graph checks passed")
    print(f"   Artifacts validated: {len(artifacts)}")
    print(f"   Unique IDs: {len(ids)}")


if __name__ == "__main__":
    main()
