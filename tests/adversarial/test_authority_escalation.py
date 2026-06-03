"""STATUS: CANDIDATE — NOT CANON\nAUTHORITY: NONE\nDEPLOYMENT: NONE"""
from scripts.detect_authority_leakage import find_authority_leakage


def test_authority_escalation_without_ratification_is_detected() -> None:
    rows = find_authority_leakage([{'artifact_id': 'A', 'authority': 'council', 'canon_status': 'candidate'}])
    assert rows == [{'artifact_id': 'A', 'authority': 'council'}]
