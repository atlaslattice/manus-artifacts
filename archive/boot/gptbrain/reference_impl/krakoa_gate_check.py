#!/usr/bin/env python3
"""Offline Krakoa gate seed checker; a flag never proves actual authority."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from krakoa_index_common import IndexHold, load_jsonl, text, unique_words, safe_pointer

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "KRAKOA_GATE_INDEX.seed.jsonl"
FIELDS = {"gate_id", "title", "gate_type", "source", "allowed_runtime_labels",
          "purpose", "canon_authority", "human_root_required", "notes"}
TYPES = {"issue", "protocol_file", "template_file", "seed_index", "code_anchor", "governance_gate"}
LABELS = {"WORK", "PLAY", "DREAM", "MODEL_ASSESSMENT", "CANDIDATE_CANON", "RATIFIED_CANON"}


def inspect_gate(row: dict) -> dict:
    problems: list[str] = []
    if set(row) != FIELDS:
        problems.append("FIELDS_MISMATCH")
    identity = row.get("gate_id")
    if not text(identity) or not identity.startswith("KRAKOA-GATE-"):
        problems.append("INVALID_ID")
    if not text(row.get("title")) or not text(row.get("purpose")):
        problems.append("MISSING_LABEL_OR_PURPOSE")
    kind = row.get("gate_type")
    if not isinstance(kind, str) or kind not in TYPES:
        problems.append("INVALID_GATE_TYPE")
    source = row.get("source")
    if kind == "issue":
        if not text(source) or not source.startswith("https://github.com/atlaslattice/manus-artifacts/issues/"):
            problems.append("ISSUE_SOURCE_POINTER_INVALID")
    elif kind in {"protocol_file", "template_file", "seed_index", "code_anchor"}:
        if not safe_pointer(source):
            problems.append("FILE_SOURCE_POINTER_INVALID")
    elif kind == "governance_gate":
        if not text(source):
            problems.append("GOVERNANCE_SOURCE_UNVERIFIED")
    labels = row.get("allowed_runtime_labels")
    if not unique_words(labels) or not set(labels).issubset(LABELS):
        problems.append("INVALID_LABELS")
    if row.get("human_root_required") is not True:
        problems.append("HUMAN_ROOT_REQUIRED")
    canon = row.get("canon_authority")
    if type(canon) is not bool:
        problems.append("CANON_FLAG_MUST_BE_BOOL")
    if canon is True and kind != "governance_gate":
        problems.append("NON_GOVERNANCE_CANON_FLAG")
    if not text(row.get("notes")):
        problems.append("MISSING_REVIEW_NOTE")
    return {
        "id": identity if text(identity) else None,
        "status": "HOLD" if problems else ("REVIEW_REQUIRED" if canon is True else "CANDIDATE_POINTER_ONLY"),
        "problems": problems,
        "authority_verified": False,
        "source_rights_verified": False,
        "private_body_loaded": False,
        "executed": False,
    }


def validate_index(path: Path) -> dict:
    try:
        entries = load_jsonl(path)
    except (OSError, IndexHold) as exc:
        return {"status": "HOLD", "reason": str(exc), "gate_count": 0,
                "authority_verified": False, "executed": False}
    inspected = [inspect_gate(x) for x in entries]
    ids = [x["id"] for x in inspected]
    duplicates = len(set(ids)) != len(ids)
    held = duplicates or any(x["status"] == "HOLD" for x in inspected)
    return {
        "status": "HOLD" if held else "REVIEW_REQUIRED",
        "gate_count": len(inspected),
        "canon_flags_for_review": sum(x.get("canon_authority") is True for x in entries),
        "duplicate_ids": duplicates,
        "entries": inspected,
        "authority_verified": False,
        "no_tool_authorization": True,
        "private_body_loaded": False,
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
