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
    assert "aetherforge-world-class-authoritative-roadmap-v0.1.md" in root_readme
    assert "aetherforge-world-class-authoritative-roadmap-v0.1.md" in projects_readme
    assert "Historical board preserved for lineage" in projects_readme


def test_contributor_ux_surfaces_exist_and_are_linked() -> None:
    kg_readme = _read("archive/knowledge_graph/lattice_kg/v0_5/README.md")
    assert "LATTICE_WORLD_CLASS_CONTRIBUTOR_START_HERE_v0.1.md" in kg_readme
    assert "LATTICE_KG_GLOSSARY_v0.1.md" in kg_readme
    assert "LATTICE_KG_QUERY_COOKBOOK_v0.1.md" in kg_readme
    assert "LATTICE_STATE_OF_GRAPH_WEEKLY_REPORT_2026-05-27.md" in kg_readme


def test_weekly_state_report_contains_required_receipt_sections() -> None:
    weekly = _read("archive/knowledge_graph/lattice_kg/v0_5/LATTICE_STATE_OF_GRAPH_WEEKLY_REPORT_2026-05-27.md")
    assert "Scope delivered this week" in weekly
    assert "Validation result" in weekly
    assert "Risks / blockers" in weekly
    assert "Next safest action" in weekly
