from __future__ import annotations

import json
from pathlib import Path

from scripts.aetherforge_cli import play
from scripts.build_acoustic_color_seed import build_seed_payload
from scripts.export_lattice_jsonld import build_hsn_cells, export_jsonld
from scripts.ingest_ip_archive import ingest_archive
from scripts.kg_search import ranked_search
from scripts.riemann_s_operator import SpectralPoint, rank_spectrum

ROOT = Path(__file__).resolve().parents[1]


def test_hsn_grid_has_1728_cells():
    cells = build_hsn_cells()
    assert len(cells) == 12 * 12 * 12
    assert cells[0]["hsn"].startswith("H")


def test_export_jsonld_writes_graph(tmp_path: Path):
    output = tmp_path / "kg.jsonld"
    stats = export_jsonld(output)
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert "@graph" in payload
    assert stats.cells == 1728
    assert stats.nodes > 0


def test_ingest_archive_pipeline_emits_candidate_records(tmp_path: Path):
    source = tmp_path / "ip"
    source.mkdir()
    (source / "artifact1.txt").write_text("alpha resonance", encoding="utf-8")
    (source / "artifact2.txt").write_text("beta isotope", encoding="utf-8")
    output = tmp_path / "ingested.jsonl"

    records = ingest_archive(source, output_path=output, max_files=10)
    assert len(records) == 2
    text = output.read_text(encoding="utf-8")
    assert '"review_state": "candidate"' in text
    assert '"route_gate": "human-root-review"' in text


def test_ranked_search_returns_results():
    results = ranked_search("graph index", limit=5)
    assert results
    assert "score" in results[0]


def test_aetherforge_play_returns_score():
    result = play("governance_route", seed=1)
    assert result["status"] in {"candidate_selected", "no-artifacts-found"}
    if result["status"] == "candidate_selected":
        assert result["score"] >= 80


def test_riemann_s_ranking_orders_points():
    ranked = rank_spectrum([SpectralPoint(440.0, 0.8), SpectralPoint(880.0, 1.1)])
    assert len(ranked) == 2
    assert ranked[0]["score"] >= ranked[1]["score"]


def test_acoustic_color_seed_payload_is_candidate():
    payload = build_seed_payload()
    assert payload["status"] == "candidate"
    assert len(payload["bands"]) >= 7
