"""Tests for world-class execution roadmap and contributor UX surfaces."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def test_authoritative_roadmap_exists_and_declares_authority() -> None:
    text = _read("projects/aetherforge-world-class-authoritative-roadmap-v0.1.md")
    assert "AUTHORITATIVE ROADMAP: true" in text
    assert "single authoritative roadmap" in text
    assert "Next 10 sprint tasks (authoritative)" in text


def test_navigation_points_to_authoritative_roadmap() -> None:
    root_readme = _read("README.md")
    projects_readme = _read("projects/README.md")
    archive_readme = _read("archive/README.md")
    assert "aetherforge-world-class-authoritative-roadmap-v0.1.md" in root_readme
    assert "aetherforge-144-task-campaign-2026-05-27.md" in root_readme
    assert "aetherforge-top10-taskboard-2026-05-28.md" in root_readme
    assert "projects/README.md" in root_readme
    assert "archive/README.md" in root_readme
    assert "GPTDREAM_PLUSPLUS_PUBLIC_RELEASE_PROTOCOL_v0.1.md" in root_readme
    assert "aetherforge-world-class-authoritative-roadmap-v0.1.md" in projects_readme
    assert "aetherforge-144-task-campaign-2026-05-27.md" in projects_readme
    assert "aetherforge-top10-taskboard-2026-05-28.md" in projects_readme
    assert "Historical board preserved for lineage" in projects_readme
    assert "Board hierarchy" in projects_readme
    assert "aetherforge/gptdreampp-openai/README.md" in archive_readme
    assert "knowledge_graph/lattice_kg/v0_5/README.md" in archive_readme
    assert "GPTDREAM_PLUSPLUS_PUBLIC_RELEASE_PROTOCOL_v0.1.md" in archive_readme


def test_top10_board_maps_to_campaign_and_roadmap() -> None:
    text = _read("projects/aetherforge-top10-taskboard-2026-05-28.md")
    assert "AX-11 (Wave 01)" in text
    assert "AX-20 (Wave 07)" in text
    assert "aetherforge-144-task-campaign-2026-05-27.md" in text
    assert "aetherforge-world-class-authoritative-roadmap-v0.1.md" in text


def test_144_campaign_board_declares_wave_map() -> None:
    text = _read("projects/aetherforge-144-task-campaign-2026-05-27.md")
    assert "12 waves × 12 tasks (144 total)" in text
    assert "Wave 12" in text
    assert "aetherforge-top10-taskboard-2026-05-28.md" in text


def test_contributor_ux_surfaces_exist_and_are_linked() -> None:
    kg_readme = _read("archive/knowledge_graph/lattice_kg/v0_5/README.md")
    assert "LATTICE_WORLD_CLASS_CONTRIBUTOR_START_HERE_v0.1.md" in kg_readme
    assert "LATTICE_KG_GLOSSARY_v0.1.md" in kg_readme
    assert "LATTICE_KG_QUERY_COOKBOOK_v0.1.md" in kg_readme
    assert "LATTICE_STATE_OF_GRAPH_WEEKLY_REPORT_2026-05-27.md" in kg_readme
    assert "../../../../README.md" in kg_readme
    assert "../../../aetherforge/gptdreampp-openai/README.md" in kg_readme
    protocol = _read("archive/spec/gptdream/GPTDREAM_PLUSPLUS_PUBLIC_RELEASE_PROTOCOL_v0.1.md")
    assert "knowledge_graph/lattice_kg/v0_5/README.md" in protocol
    assert "LATTICE_WORLD_CLASS_CONTRIBUTOR_START_HERE_v0.1.md" in protocol
    assert "LATTICE_KG_QUERY_COOKBOOK_v0.1.md" in protocol
    assert "aetherforge/gptdreampp-openai/README.md" in protocol


def test_weekly_state_report_contains_required_receipt_sections() -> None:
    weekly = _read("archive/knowledge_graph/lattice_kg/v0_5/LATTICE_STATE_OF_GRAPH_WEEKLY_REPORT_2026-05-27.md")
    assert "Scope delivered this week" in weekly
    assert "Validation result" in weekly
    assert "Risks / blockers" in weekly
    assert "Next safest action" in weekly
