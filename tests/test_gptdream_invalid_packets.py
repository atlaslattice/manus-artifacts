"""
STATUS: CANDIDATE — NOT CANON
AUTHORITY: NONE
DEPLOYMENT: NONE
"""
import pytest

from scripts.gptdream_packet_validation import parse_packet_yaml, strict_validate_packet

SCHEMA = {
    'schema_version': '1.0',
    'required': ['id', 'schema_version', 'kind', 'created_at', 'value', 'ref'],
    'properties': {
        'id': {'type': 'string', 'non_empty': True},
        'schema_version': {'type': 'string'},
        'kind': {'type': 'string', 'enum': ['wake', 'dream']},
        'created_at': {'type': 'string', 'format': 'date-time'},
        'value': {'type': 'integer', 'max': 10},
        'ref': {'type': 'string', 'forbid_self_ref': True},
        'authority': {'type': 'string'},
        'ratification_event_id': {'type': 'string', 'nullable': True},
    },
}

VALID = {'id': 'pkt-1', 'schema_version': '1.0', 'kind': 'wake', 'created_at': '2026-06-03T00:00:00Z', 'value': 1, 'ref': 'pkt-2'}


@pytest.mark.parametrize(
    ('label', 'packet', 'expected'),
    [
        ('wrong type', {**VALID, 'value': 'x'}, 'wrong type for value'),
        ('missing required', {'id': 'pkt-1'}, 'missing required field: schema_version'),
        ('invalid enum', {**VALID, 'kind': 'other'}, 'invalid enum for kind'),
        ('invalid format', {**VALID, 'created_at': 'bad'}, 'invalid format for created_at'),
        ('circular ref', {**VALID, 'ref': 'pkt-1'}, 'circular ref for ref'),
        ('overflow', {**VALID, 'value': 99}, 'overflow for value'),
        ('null injection', {**VALID, 'kind': None}, 'null not allowed: kind'),
        ('schema mismatch', {**VALID, 'extra': True}, 'unexpected fields: extra'),
        ('version conflict', {**VALID, 'schema_version': '0.9'}, 'version conflict'),
        ('auth escalation', {**VALID, 'authority': 'council', 'ratification_event_id': 'PENDING'}, 'auth escalation'),
        ('empty payload', {**VALID, 'id': ''}, 'empty payload for id'),
    ],
)
def test_invalid_packets(label: str, packet: dict, expected: str) -> None:
    errors = strict_validate_packet(packet, SCHEMA)
    assert any(expected in error for error in errors), (label, errors)


def test_duplicate_keys_rejected() -> None:
    payload, error = parse_packet_yaml('id: one\nid: two\n')
    assert payload is None
    assert 'duplicate key' in error
