"""STATUS: CANDIDATE — NOT CANON\nAUTHORITY: NONE\nDEPLOYMENT: NONE"""
from scripts.detect_canon_claim_contradictions import detect_conflicting_claims


def test_conflicting_canon_claims_are_detected() -> None:
    rows = detect_conflicting_claims([
        {'artifact_id': 'C1', 'concept_id': 'topic', 'canon_status': 'ratified'},
        {'artifact_id': 'C2', 'concept_id': 'topic', 'canon_status': 'approved'},
    ])
    assert rows
