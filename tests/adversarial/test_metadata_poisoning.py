"""STATUS: CANDIDATE — NOT CANON\nAUTHORITY: NONE\nDEPLOYMENT: NONE"""
from scripts.normalize_metadata import detect_unexpected_fields


def test_unexpected_frontmatter_fields_are_quarantined() -> None:
    fields = detect_unexpected_fields({'artifact_id': 'X', 'rm_rf': True}, {'artifact_id'})
    assert fields == ['rm_rf']
