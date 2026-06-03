"""
STATUS: CANDIDATE — NOT CANON
AUTHORITY: NONE
DEPLOYMENT: NONE
"""
from scripts.gptdream_packet_validation import strict_validate_packet

SCHEMA = {
    'schema_version': '1.0',
    'required': ['id', 'kind', 'created_at'],
    'properties': {
        'id': {'type': 'string'},
        'kind': {'type': 'string', 'enum': ['wake', 'dream']},
        'created_at': {'type': 'string', 'format': 'date-time'},
    },
}


def test_extra_fields_rejected() -> None:
    packet = {'id': '1', 'kind': 'wake', 'created_at': '2026-06-03T00:00:00Z', 'extra': True}
    errors = strict_validate_packet(packet, SCHEMA)
    assert errors == ['unexpected fields: extra']


def test_missing_required_fields_fail_with_clear_errors() -> None:
    packet = {'id': '1', 'kind': 'wake'}
    errors = strict_validate_packet(packet, SCHEMA)
    assert 'missing required field: created_at' in errors
