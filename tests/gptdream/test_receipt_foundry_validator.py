from pathlib import Path

import yaml

from reference_impl.receipt_foundry.validator import validate_receipt_habitat_claim


ROOT = Path(__file__).resolve().parents[2]
RECEIPT_SCHEMA = ROOT / "schemas/receipt_habitat/v0_1/receipt-habitat-claim.schema.yaml"
ATLAS_CLAIM_SCHEMA = ROOT / "schemas/atlas_orcs/v0_1/atlas-claim.schema.yaml"


def test_receipt_habitat_schema_normalized_to_v01():
    data = yaml.safe_load(RECEIPT_SCHEMA.read_text(encoding="utf-8"))
    assert data["properties"]["schema_version"]["const"] == "0.1"
    assert "claim_state" in data["required"]
    assert "evidence_refs" in data["required"]


def test_atlas_claim_requires_claim_state_and_evidence_refs():
    data = yaml.safe_load(ATLAS_CLAIM_SCHEMA.read_text(encoding="utf-8"))
    assert "claim_state" in data["required"]
    assert "evidence_refs" in data["required"]


def test_candidate_to_reviewed_requires_receipt_metadata():
    claim = {
        "previous_claim_state": "candidate",
        "claim_state": "reviewed",
        "evidence_refs": ["ref-1"],
    }
    errors = validate_receipt_habitat_claim(claim)
    assert "candidate_to_reviewed_requires_receipt_metadata" in errors


def test_reviewed_to_ratified_requires_governance_event():
    claim = {
        "previous_claim_state": "reviewed",
        "claim_state": "ratified",
        "evidence_refs": ["ref-1"],
        "receipt_metadata": {
            "receipt_id": "rcp-1",
            "receipt_type": "trace",
            "receipt_hash": "hash-1",
        },
    }
    errors = validate_receipt_habitat_claim(claim)
    assert "reviewed_to_ratified_requires_governance_event" in errors


def test_summary_cannot_become_source():
    claim = {
        "claim_state": "reviewed",
        "evidence_refs": ["thread-summary"],
        "source_basis": "summary_only",
        "source_status": "source",
    }
    errors = validate_receipt_habitat_claim(claim)
    assert "summary_cannot_become_source" in errors


def test_receipt_not_truth_without_verification_event():
    claim = {
        "claim_state": "reviewed",
        "evidence_refs": ["ref-1"],
        "receipt_metadata": {
            "receipt_id": "rcp-2",
            "receipt_type": "trace",
            "receipt_hash": "hash-2",
        },
        "truth_status": "verified",
    }
    errors = validate_receipt_habitat_claim(claim)
    assert "receipt_not_truth_requires_verification_event" in errors


def test_claim_state_and_evidence_refs_required():
    errors = validate_receipt_habitat_claim({})
    assert "missing:claim_state" in errors
    assert "missing:evidence_refs" in errors
