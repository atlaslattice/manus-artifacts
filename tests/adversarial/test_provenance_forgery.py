"""STATUS: CANDIDATE — NOT CANON\nAUTHORITY: NONE\nDEPLOYMENT: NONE"""
from scripts.lattice_kg_lib import validate_provenance_bit


def test_tampered_provenance_is_rejected() -> None:
    errors = validate_provenance_bit({'source_receipt': '', 'sha256': 'bad', 'generated_at_utc': 'nope', 'tool_chain': []})
    assert 'missing source_receipt' in errors
    assert 'invalid sha256' in errors
    assert 'invalid generated_at_utc' in errors
