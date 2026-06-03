"""STATUS: CANDIDATE — NOT CANON\nAUTHORITY: NONE\nDEPLOYMENT: NONE"""
from scripts.validate_no_self_promotion import validate_record


def test_fake_ratification_and_canon_status_are_rejected() -> None:
    errors = validate_record({'canon_status': 'ratified', 'ratification_event_id': 'PENDING', 'authority': 'council'})
    assert len(errors) == 2
