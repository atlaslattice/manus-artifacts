"""Integration tests: the whole pipeline, end to end.

These are the tests that answer the handoff's requirement that a plant engineer
or researcher can load source receipts, execute the runs deterministically,
reproduce every derived number, and see violations fail validation.
"""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import pytest

import simulator
from sources import loader

PACKAGE_DIR = Path(__file__).resolve().parents[1]
SCHEMA_DIR = PACKAGE_DIR / "schemas"


@pytest.fixture(scope="module")
def reproduction():
    return simulator.reproduce()


@pytest.fixture(scope="module")
def validation():
    return simulator.validate_all()


def test_reproduction_has_no_unexplained_divergence(reproduction):
    assert reproduction["totals"]["mismatched"] == 0, [
        (r["run_id"], [c for c in r["checks"] if c["status"] == "MISMATCH"])
        for r in reproduction["runs"]
    ]


def test_reproduction_covers_all_seven_runs(reproduction):
    assert {r["run_id"] for r in reproduction["runs"]} == {
        "RUN_0", "RUN_0.2", "RUN_1", "RUN_2", "RUN_3", "RUN_4A", "S02"
    }


def test_reproduction_checks_a_meaningful_number_of_values(reproduction):
    assert reproduction["totals"]["checks"] >= 100
    assert reproduction["totals"]["matched"] >= 100


def test_run_2_divergence_is_annotated_not_hidden(reproduction):
    """The committed Run 2 flow defect must be surfaced, not silently tolerated."""
    run2 = next(r for r in reproduction["runs"] if r["run_id"] == "RUN_2")
    annotated = [c for c in run2["checks"] if c["status"] == "ANNOTATED_DIVERGENCE"]
    assert annotated, "the known Run 2 defect must appear as an annotated divergence"
    annotation = annotated[0]["annotation"]
    assert annotation["kind"] == "DEFECT_IN_COMMITTED_ARTIFACT"
    assert "preserve" in annotation["resolution"].lower()


def test_validation_passes(validation):
    as_dict, report = validation
    assert report.passed, [(r.gate_id, r.status, r.detail) for r in report.failures]
    assert as_dict["status"] == "VALIDATION_PASSED"


def test_validation_reports_every_gate(validation):
    as_dict, _ = validation
    assert as_dict["gate_count"] == 16
    assert {g["gate_id"] for g in as_dict["gates"]} == {
        f"G{n:02d}" for n in range(1, 17)
    }


def test_credit_ledger_is_populated_and_clean(validation):
    as_dict, _ = validation
    assert as_dict["ledger_entries"] > 0
    assert as_dict["ledger_violations"] == []


def test_unknown_ledger_enumerates_open_questions():
    ledger = simulator.unknown_ledger()
    assert ledger["counts"]["desalination_unknowns"] == 10
    assert ledger["counts"]["compute_unknown_parameters"] == 11
    assert ledger["counts"]["components"] == 8
    assert ledger["explicit_zero_credit_baselines"]


def test_source_manifest_verifies_without_drift():
    assert loader.verify_manifest() == []


def test_every_registered_artifact_has_a_hash():
    manifest = loader.build_manifest()
    assert len(manifest["artifacts"]) == len(loader.ARTIFACT_FILES)
    for entry in manifest["artifacts"]:
        assert len(entry["sha256"]) == 64
        assert entry["bytes"] > 0


# ---------------------------------------------------------------------------
# Schema conformance of the emitted reports
# ---------------------------------------------------------------------------
def _schema(name: str) -> dict:
    return json.loads((SCHEMA_DIR / name).read_text(encoding="utf-8"))


def test_validation_report_conforms_to_schema(validation):
    as_dict, _ = validation
    jsonschema.validate(instance=as_dict, schema=_schema("validation_report.schema.json"))


def test_source_manifest_conforms_to_schema():
    jsonschema.validate(instance=loader.build_manifest(), schema=_schema("source_manifest.schema.json"))


def test_run_results_conform_to_schema():
    schema = _schema("run_result.schema.json")
    for run_id, fn in simulator.RUN_REGISTRY.items():
        result = json.loads(json.dumps(simulator.to_jsonable(fn())))
        jsonschema.validate(instance=result, schema=schema)


def test_evidence_class_schema_enum_matches_the_code():
    from models.common import EvidenceClass

    schema = _schema("evidence_class.schema.json")
    assert set(schema["enum"]) == {c.value for c in EvidenceClass}
