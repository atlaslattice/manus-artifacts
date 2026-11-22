#!/usr/bin/env python3
"""Offline ORCS route seed checker; source paths are references, not accessible content."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

from krakoa_index_common import IndexHold, load_jsonl, text, unique_words, safe_pointer

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "LATTICE_ORCS_ROUTE_INDEX.seed.jsonl"
FIELDS = {"artifact_id", "title", "project_domain", "orcs_route_class", "source_paths",
          "claim_class", "confidence", "runtime_label", "privacy_status",
          "human_root_required", "notes"}
CLAIM_CLASSES = {"parsed_artifact", "raw_user_report", "raw_model_output", "candidate"}
CONFIDENCE = {"C0", "C1", "C2", "C3", "C4", "C5"}
RUNTIME = {"WORK", "MODEL_ASSESSMENT"}


def inspect_route(row: dict) -> dict:
    problems: list[str] = []
    if set(row) != FIELDS:
        problems.append("FIELDS_MISMATCH")
    identity = row.get("artifact_id")
    if not text(identity) or not identity.startswith("ORCS-ROUTE-"):
        problems.append("INVALID_ROUTE_ID")
    if not text(row.get("title")) or not text(row.get("project_domain")):
        problems.append("MISSING_TITLE_OR_DOMAIN")
    classes = row.get("orcs_route_class")
    if not unique_words(classes) or not all(re.fullmatch(r"[A-Z0-9_]+", x) for x in classes):
        problems.append("INVALID_ROUTE_CLASSES")
    paths = row.get("source_paths")
    if not unique_words(paths) or not all(safe_pointer(p) for p in paths):
        problems.append("UNSAFE_OR_MISSING_SOURCE_POINTER")
    if not isinstance(row.get("claim_class"), str) or row["claim_class"] not in CLAIM_CLASSES:
        problems.append("INVALID_CLAIM_CLASS")
    if not isinstance(row.get("confidence"), str) or row["confidence"] not in CONFIDENCE:
        problems.append("INVALID_CONFIDENCE")
    if not isinstance(row.get("runtime_label"), str) or row["runtime_label"] not in RUNTIME:
        problems.append("PRIVATE_MODE_OR_UNKNOWN_RUNTIME")
    if row.get("privacy_status") != "public":
        problems.append("NON_PUBLIC_SOURCE_CANNOT_ENTER_PUBLIC_ROUTE")
    if row.get("human_root_required") is not True:
        problems.append("HUMAN_ROOT_REQUIRED")
    if not text(row.get("notes")):
        problems.append("MISSING_BOUNDARY_NOTE")
    return {
        "id": identity if text(identity) else None,
        "status": "HOLD" if problems else "CANDIDATE_POINTER_ONLY",
        "problems": problems,
        "source_paths_accessed": False,
        "source_rights_verified": False,
        "permission_granted": False,
        "executed": False,
    }


def validate_index(path: Path) -> dict:
    try:
        rows = load_jsonl(path)
    except (OSError, IndexHold) as exc:
        return {"status": "HOLD", "reason": str(exc), "route_count": 0,
                "permission_granted": False, "executed": False}
    entries = [inspect_route(x) for x in rows]
    ids = [x["id"] for x in entries]
    duplicate = len(set(ids)) != len(ids)
    held = duplicate or any(x["status"] == "HOLD" for x in entries)
    return {
        "status": "HOLD" if held else "CANDIDATE_INDEX_ONLY",
        "route_count": len(entries),
        "duplicate_ids": duplicate,
        "entries": entries,
        "source_paths_accessed": False,
        "source_rights_verified": False,
        "permission_granted": False,
        "executed": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=Path, default=DEFAULT)
    result = validate_index(parser.parse_args().index)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 2 if result["status"] == "HOLD" else 0


if __name__ == "__main__":
    raise SystemExit(main())
