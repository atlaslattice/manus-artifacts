"""STATUS: CANDIDATE — NOT CANON\nAUTHORITY: NONE\nDEPLOYMENT: NONE"""
from scripts.lattice_kg_lib import classify_external_link


def test_unsafe_external_links_are_flagged() -> None:
    assert classify_external_link('http://example.com') == 'non_https'
    assert classify_external_link('https://localhost/test') == 'private_host'
    assert classify_external_link('https://127.0.0.1/test') == 'private_host'
