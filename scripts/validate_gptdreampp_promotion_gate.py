#!/usr/bin/env python3
"""Validate GPTDream++ Drive→GitHub promotion-gate fixtures and manifests."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "archive" / "aetherforge" / "gptdreampp-openai"
FIXTURES_DIR = PACKAGE / "eval_fixtures"
RULESET_MAP = PACKAGE / "ruleset" / "artifact_class_validation_map.json"
RECEIPTS = PACKAGE / "receipts" / "high_priority_drive_sync_receipts.json"
MANIFEST = PACKAGE / "manifests" / "high_priority_drive_sync_manifest.json"

REVIEW_BLOCKLIST = (
    "best in the world",
    "deployed authority",
    "canonical truth",
    "automatic canon",
)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def check_record_shape(record: dict[str, Any]) -> None:
    required_fields = {
        "record_id",
        "artifact_class",
        "source_uri",
        "source_hash",
        "receipt",
        "provenance",
        "canon_status",
        "reviewer",
        "ratification_event",
        "github_target_path",
        "required_validations",
        "completed_validations",
    }
    missing = required_fields - set(record)
    if missing:
        raise AssertionError(f"{record.get('record_id', '<unknown>')}: missing required fields {sorted(missing)}")


def check_non_canon_default(record: dict[str, Any]) -> None:
    canon_status = record["canon_status"]
    if canon_status == "RATIFIED_CANON":
        reviewer = record.get("reviewer")
        ratification_event = record.get("ratification_event")
        if not reviewer or not ratification_event:
            raise AssertionError(
                f"{record['record_id']}: RATIFIED_CANON requires reviewer and ratification_event"
            )


def check_class_validations(record: dict[str, Any], class_map: dict[str, list[str]]) -> None:
    klass = record["artifact_class"]
    required = class_map[klass]
    if sorted(record["required_validations"]) != sorted(required):
        raise AssertionError(
            f"{record['record_id']}: required_validations mismatch for class {klass}"
        )


def check_receipt_references(manifest: dict[str, Any], receipts: dict[str, Any]) -> None:
    receipt_ids = {r["receipt_id"] for r in receipts.get("receipts", [])}
    for item in manifest.get("items", []):
        if item["receipt_id"] not in receipt_ids:
            raise AssertionError(
                f"{item['record_id']}: receipt_id {item['receipt_id']} not found in receipts file"
            )


def check_review_lane(records: list[dict[str, Any]]) -> None:
    for record in records:
        review = record.get("bullshit_olympics_review") or {}
        notes = (review.get("notes") or "").lower()
        if review.get("status") == "FAIL" and not notes:
            raise AssertionError(f"{record['record_id']}: FAIL review must include notes")
        for phrase in REVIEW_BLOCKLIST:
            if phrase in notes:
                raise AssertionError(
                    f"{record['record_id']}: review note contains blocked overclaim phrase '{phrase}'"
                )


def main() -> None:
    class_map = load_json(RULESET_MAP)
    fixtures = sorted(FIXTURES_DIR.glob("promotion_gate.*.json"))
    if not fixtures:
        raise AssertionError("No promotion_gate fixtures found")

    records: list[dict[str, Any]] = []
    failures: list[str] = []

    for fixture in fixtures:
        record = load_json(fixture)
        if fixture.name.endswith("invalid.canon_missing_adjudication.json"):
            # This fixture must fail adjudication constraints.
            try:
                check_non_canon_default(record)
            except AssertionError:
                continue
            failures.append(f"{fixture.name}: expected adjudication failure but passed")
            continue

        records.append(record)
        try:
            check_record_shape(record)
            check_non_canon_default(record)
            check_class_validations(record, class_map)
        except AssertionError as exc:
            failures.append(f"{fixture.name}: {exc}")

    receipts = load_json(RECEIPTS)
    manifest = load_json(MANIFEST)
    try:
        check_receipt_references(manifest, receipts)
    except AssertionError as exc:
        failures.append(str(exc))

    try:
        check_review_lane(records)
    except AssertionError as exc:
        failures.append(str(exc))

    if failures:
        joined = "\n".join(f"- {e}" for e in failures)
        raise SystemExit(f"GPTDream++ promotion gate validation failed:\n{joined}")

    print("GPTDream++ promotion gate validation passed")


if __name__ == "__main__":
    main()
