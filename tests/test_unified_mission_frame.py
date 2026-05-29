"""
Candidate tests for unified mission frame and quality-gate artifacts.

STATUS: CANDIDATE TESTS — NOT CANON — NOT DEPLOYABLE
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_unified_mission_charter_exists_with_boundary() -> None:
    path = (
        ROOT
        / "archive/knowledge_graph/lattice_kg/v0_5/LATTICE_AETHERFORGE_GPTDREAM_UNIFIED_MISSION_CHARTER_v0.1.md"
    )
    text = _read(path)
    assert "CANON: no" in text
    assert "DEPLOYMENT: no" in text
    assert "AUTHORITY: none" in text
    assert "Lattice = functional source-grounded knowledge graph." in text
    assert "Aetherforge = playable archive game" in text
    assert "GPTDream++ = reproducible open-source protocol gift for the public." in text


def test_kg_runbook_has_source_grounded_admission_gate() -> None:
    text = _read(
        ROOT
        / "archive/knowledge_graph/lattice_kg/v0_5/NOTION_GITHUB_KNOWLEDGE_GRAPH_RUNBOOK_v0.1.md"
    )
    assert "## Source-grounded graph admission gate" in text
    assert "Confirm `derived_from` lineage is explicit and traversable." in text
    assert "## Provenance receipt minimums" in text
    assert "`sha256_if_available`" in text


def test_quest_quality_gate_ties_play_to_tests() -> None:
    text = _read(
        ROOT / "archive/knowledge_graph/lattice_kg/v0_5/AETHERFORGE_QUEST_QUALITY_GATE_v0.1.md"
    )
    assert "Fun framing does not replace acceptance criteria, tests, or receipts." in text
    assert "Required quest acceptance criteria" in text
    assert "python -m pytest -q tests" in text


def test_gptdream_public_release_protocol_has_reproducible_checks() -> None:
    text = _read(
        ROOT / "archive/spec/gptdream/GPTDREAM_PLUSPLUS_PUBLIC_RELEASE_PROTOCOL_v0.1.md"
    )
    assert "NOT CANON" in text
    assert "python -m pytest -q tests" in text
    assert "bash run_checks.sh" in text
    assert "A protocol draft is not a ratification event." in text


def test_tidelock_activity_receipt_logged_for_loop1() -> None:
    text = _read(
        ROOT
        / "archive/boot/copilotbrain/TIDELOCKBrain/TIDELOCK_ACTIVITY_RECEIPT_2026-05-27_UNIFIED_MISSION_FRAME_LOOP1.md"
    )
    assert "LOOP: 1" in text
    assert "STATUS: CANDIDATE EXECUTION RECEIPT — NOT CANON" in text
    assert "Next safest action" in text
