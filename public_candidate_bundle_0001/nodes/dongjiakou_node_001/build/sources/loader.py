"""Load the sibling Node-001 evidence artifacts, read-only, with hash checks.

The build package never edits the evidence it consumes. It reads the flat
artifacts sitting next to it in the node directory and records their SHA-256
digests in ``source_manifest.json`` so that a reproduction run can prove it read
exactly the bytes it claims to have read.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

#: build/sources/loader.py -> build/ -> dongjiakou_node_001/
PACKAGE_DIR = Path(__file__).resolve().parents[1]
NODE_DIR = PACKAGE_DIR.parent

#: run_id -> evidence artifact filename
ARTIFACT_FILES: dict[str, str] = {
    "RUN_0": "RUN_0_BASELINE_v0_1.json",
    "RUN_0.2": "RUN_0_OPERATING_2025_v0_2.json",
    "RUN_1": "RUN_1_SOLAR_v0_1.json",
    "RUN_2": "RUN_2_HYDRO_v0_1.json",
    "RUN_3": "RUN_3_COMPUTE_v0_2.json",
    "RUN_4A": "RUN_4A_BIOMETABOLIC_v0_1.json",
    "S02": "S02_BESS_TRANSFER_FUNCTION_v0_1.json",
    "NODE_001_PROFILE": "NODE_001_PROFILE_v0_2.json",
    "INTEGRATED_NODE_PROFILE": "INTEGRATED_NODE_PROFILE_v0_2.json",
    "C01_MODEL_ROUTING_POLICY": "C01_MODEL_ROUTING_POLICY_v0_2.json",
    "C01_MODEL_SOURCE_SNAPSHOT": "C01_MODEL_SOURCE_SNAPSHOT_v0_2.json",
    "DOWNSTREAM_SYMBIOSIS_COMPONENTS": "DOWNSTREAM_SYMBIOSIS_COMPONENTS_v0_1.json",
    "SOURCE_RECORD_CHAIN": "SOURCE_RECORD_CHAIN_v0_1.json",
}

#: Source-record deltas, in order.
SOURCE_DELTA_FILES: tuple[str, ...] = tuple(
    f"SOURCE_RECORD_DELTA_v0_{n}.json" for n in range(2, 8)
)

MANIFEST_PATH = PACKAGE_DIR / "sources" / "source_manifest.json"


class SourceError(RuntimeError):
    """Raised when a source artifact is missing or has changed."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_artifact(filename: str) -> dict[str, Any]:
    """Load one evidence artifact by filename from the node directory."""
    path = NODE_DIR / filename
    if not path.exists():
        raise SourceError(f"missing source artifact: {path}")
    return load_json(path)


def load_all() -> dict[str, Any]:
    """Load every registered artifact, keyed by run/artifact id."""
    return {key: load_artifact(name) for key, name in ARTIFACT_FILES.items()}


def build_manifest() -> dict[str, Any]:
    """Compute the current source manifest from disk."""
    entries = []
    for key, name in ARTIFACT_FILES.items():
        path = NODE_DIR / name
        if not path.exists():
            raise SourceError(f"missing source artifact: {path}")
        entries.append({
            "artifact_key": key,
            "filename": name,
            "sha256": sha256_file(path),
            "bytes": path.stat().st_size,
        })
    deltas = []
    for name in SOURCE_DELTA_FILES:
        path = NODE_DIR / name
        if path.exists():
            deltas.append({"filename": name, "sha256": sha256_file(path),
                           "bytes": path.stat().st_size})
    return {
        "manifest_id": "DJK-NODE-001-SOURCE-MANIFEST",
        "node_directory": str(NODE_DIR.relative_to(NODE_DIR.parent.parent.parent.parent)),
        "hash_algorithm": "sha256",
        "read_only": True,
        "artifacts": entries,
        "source_record_deltas": deltas,
    }


def write_manifest() -> Path:
    """Regenerate ``source_manifest.json`` from the artifacts on disk."""
    manifest = build_manifest()
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    with MANIFEST_PATH.open("w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2, sort_keys=False)
        handle.write("\n")
    return MANIFEST_PATH


def verify_manifest() -> list[dict[str, Any]]:
    """Compare artifacts on disk against the recorded manifest.

    Returns a list of drift records; an empty list means the evidence is
    byte-identical to what the manifest recorded.
    """
    if not MANIFEST_PATH.exists():
        raise SourceError(f"manifest not found: {MANIFEST_PATH}")
    recorded = load_json(MANIFEST_PATH)
    drift: list[dict[str, Any]] = []

    for entry in recorded.get("artifacts", []):
        path = NODE_DIR / entry["filename"]
        if not path.exists():
            drift.append({"filename": entry["filename"], "kind": "MISSING"})
            continue
        actual = sha256_file(path)
        if actual != entry["sha256"]:
            drift.append({
                "filename": entry["filename"],
                "kind": "HASH_MISMATCH",
                "recorded": entry["sha256"],
                "actual": actual,
            })

    for entry in recorded.get("source_record_deltas", []):
        path = NODE_DIR / entry["filename"]
        if not path.exists():
            drift.append({"filename": entry["filename"], "kind": "MISSING"})
            continue
        actual = sha256_file(path)
        if actual != entry["sha256"]:
            drift.append({
                "filename": entry["filename"],
                "kind": "HASH_MISMATCH",
                "recorded": entry["sha256"],
                "actual": actual,
            })

    return drift
