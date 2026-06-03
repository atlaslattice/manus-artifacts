"""STATUS: CANDIDATE — NOT CANON\nAUTHORITY: NONE\nDEPLOYMENT: NONE"""
from pathlib import Path

from scripts.validate_markdown_links import validate_links_in_text


def test_missing_internal_link_is_flagged() -> None:
    payload = validate_links_in_text(Path('.').resolve(), 'README.md', '[broken](docs/does-not-exist.md)')
    assert payload['broken_links']
