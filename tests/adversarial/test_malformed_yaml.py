"""STATUS: CANDIDATE — NOT CANON\nAUTHORITY: NONE\nDEPLOYMENT: NONE"""
import pytest

from scripts.lattice_kg_lib import load_yaml_strict


@pytest.mark.parametrize('payload', [
    'a: [1,2',
    'a: : b',
    '- just\n- list\n: nope',
    'a\n  b: c',
    'a: "unterminated',
    'a: {b: 1',
    'a: [1, 2}}',
    'a: |\n\tbad',
    'a: 1\nb: [',
    'a:\n - 1\n - : 2',
    'a: !!python/object/apply:os.system ["echo nope"]',
    'a: 1\na: 2',
])
def test_malformed_yaml_fails_gracefully(payload: str) -> None:
    _, error = load_yaml_strict(payload)
    assert error is not None
