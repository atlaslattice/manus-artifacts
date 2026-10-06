#!/usr/bin/env python3
"""
Atlas Lattice physics ingestion contract fixture validator.

Validates synthetic property fixtures against physics_profile_v0.1.1.json
and applies a small set of Source-Per-Field Policy v0.1 semantic checks.

This script does not fetch scientific data and does not validate scientific truth.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:
    print("ERROR: jsonschema is required (pip install jsonschema)", file=sys.stderr)
    sys.exit(2)


ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = ROOT / "public_candidate_bundle_0001" / "schemas" / "physics_profile_v0.1.1.json"
FIXTURE_PATH = ROOT / "public_candidate_bundle_0001" / "fixtures" / "physics_ingestion" / "CONTRACT_FIXTURES_v0.1.json"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def policy_errors(prop: dict) -> list[str]:
    errors: list[str] = []

    # Unknown must not be represented as an unsupported theory.
    if prop.get("evidence_status") == "PROPOSED" and prop.get("value") is None:
        errors.append("PROPOSED with null value violates 'unknown stays unknown' policy")

    # Limits/ranges belong in value_relation, not uncertainty dictionaries.
    unc = prop.get("uncertainty")
    if isinstance(unc, dict) and any(k in unc for k in ("limit", "lower", "upper", "symmetric")):
        errors.append("legacy/limit uncertainty shape is not allowed by v0.1.1")

    return errors


def main() -> int:
    schema = load_json(SCHEMA_PATH)
    fixtures = load_json(FIXTURE_PATH)

    property_schema = {
        "$schema": schema["$schema"],
        "$defs": schema["$defs"],
        "$ref": "#/$defs/property",
    }
    validator = Draft202012Validator(property_schema)

    failures = 0

    for case in fixtures["cases"]:
        case_id = case["case_id"]
        expected = case["expected"]
        prop = case["property"]

        schema_errors = sorted(validator.iter_errors(prop), key=lambda e: list(e.path))
        semantic_errors = policy_errors(prop)
        actual = "VALID" if not schema_errors and not semantic_errors else "INVALID"

        print(f"{case_id}: expected={expected} actual={actual}")

        if schema_errors:
            for error in schema_errors:
                print(f"  schema: {error.message}")
        if semantic_errors:
            for error in semantic_errors:
                print(f"  policy: {error}")

        if actual != expected:
            failures += 1

    if failures:
        print(f"FAIL: {failures} fixture expectation(s) mismatched")
        return 1

    print("PASS: all synthetic contract fixtures matched expected validity")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
