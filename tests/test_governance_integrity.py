"""
STATUS: CANDIDATE — NOT CANON
AUTHORITY: NONE
DEPLOYMENT: NONE
"""
from scripts.detect_authority_leakage import find_authority_leakage
from scripts.detect_canon_claim_contradictions import detect_conflicting_claims
from scripts.validate_deployment_state import deployment_state_error
from scripts.validate_no_self_promotion import validate_record
from scripts.validate_ratification_requirements import validate_ratification_record
from scripts.validate_trust_state import trust_state_error


def test_candidate_vs_canon_guardrails() -> None:
    record = {"canon_status": "ratified", "authority": "NONE", "ratification_event_id": None}
    errors = validate_record(record)
    assert any("ratification_event_id" in error for error in errors)


def test_no_self_promotion_and_authority_leakage() -> None:
    record = {"artifact_id": "A-1", "canon_status": "candidate", "authority": "council"}
    errors = validate_record(record)
    assert any("authority claimed" in error for error in errors)
    leakage = find_authority_leakage([record])
    assert leakage == [{"artifact_id": "A-1", "authority": "council"}]


def test_trust_state_validity() -> None:
    assert trust_state_error({"trust_state": "candidate_reviewed"}) is None
    assert trust_state_error({"trust_state": "bogus"}) == "invalid trust_state: bogus"


def test_deployment_state_validity() -> None:
    assert deployment_state_error({"canon_status": "candidate", "deployment_status": "deployable"})
    assert deployment_state_error({"canon_status": "ratified", "deployment_status": "deployable", "ratification_event_id": None})
    assert deployment_state_error({"canon_status": "candidate", "deployment_status": "not_deployable"}) is None


def test_ratification_requirements_and_canon_contradictions() -> None:
    errors = validate_ratification_record({"canon_status": "ratified", "ratification_event_id": "RAT-1", "council_signatures": [], "adjudication_date": None})
    assert "missing council_signatures" in errors
    conflicts = detect_conflicting_claims([
        {"artifact_id": "A", "concept_id": "same", "canon_status": "ratified"},
        {"artifact_id": "B", "concept_id": "same", "canon_status": "approved"},
    ])
    assert conflicts == [{"concept": "same", "artifact_ids": ["A", "B"]}]
