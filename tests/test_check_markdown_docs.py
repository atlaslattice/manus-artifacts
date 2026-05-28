from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "scripts" / "check_markdown_docs.py"
MODULE_SPEC = importlib.util.spec_from_file_location("check_markdown_docs", MODULE_PATH)
assert MODULE_SPEC is not None and MODULE_SPEC.loader is not None
MODULE = importlib.util.module_from_spec(MODULE_SPEC)
sys.modules[MODULE_SPEC.name] = MODULE
MODULE_SPEC.loader.exec_module(MODULE)
validate_files = MODULE.validate_files


def test_validate_files_accepts_well_formed_markdown(tmp_path: Path) -> None:
    target = tmp_path / "guide.md"
    target.write_text(
        "# Guide\n\n"
        "## Overview\n\n"
        "See [Details](#details).\n\n"
        "```bash\n"
        "echo ok\n"
        "```\n\n"
        "## Details\n",
        encoding="utf-8",
    )

    assert validate_files([target]) == []


def test_validate_files_reports_links_anchors_headings_and_code_fences(
    tmp_path: Path,
) -> None:
    target = tmp_path / "guide.md"
    target.write_text(
        "# Guide\n\n"
        "### Skipped level\n\n"
        "See [Missing](./missing.md) and [Bad anchor](#nope).\n\n"
        "```\n"
        "echo missing language\n"
        "```\n",
        encoding="utf-8",
    )

    issues = validate_files([target])
    messages = [issue.message for issue in issues]

    assert "heading level jumps from H1 to H3" in messages
    assert "broken relative link: ./missing.md" in messages
    assert "broken anchor target: #nope" in messages
    assert "code fence is missing a language tag" in messages
