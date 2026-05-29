from pathlib import Path

import pytest

from scripts.build_lattice_global_index import build_graph_index, load_graph_data, render_graph_index
from scripts.kg_query import run_query
from scripts.validate_lattice_quality_gates import ValidationError, validate_graph

ROOT = Path(__file__).resolve().parents[1]


def test_graph_seed_contains_nodes_edges_and_routes():
    graph = load_graph_data(ROOT)
    assert graph.nodes
    assert graph.edges
    assert graph.routes


def test_render_graph_index_mentions_generated_source_and_orcs_routes():
    graph = load_graph_data(ROOT)
    rendered = render_graph_index(graph)
    assert "SOURCE: scripts/build_lattice_global_index.py" in rendered
    assert "## ORCS route domains" in rendered
    assert "COUNCIL_BOOT" in rendered


def test_build_graph_index_writes_output(tmp_path: Path):
    repo = tmp_path / "repo"
    (repo / "archive/knowledge_graph").mkdir(parents=True)
    (repo / "archive/knowledge_graph/GRAPH_SEED.jsonl").write_text(
        '\n'.join([
            '{"record_type":"node","node_id":"doc:readme","kind":"document","label":"README","path":"README.md"}',
            '{"record_type":"edge","edge_id":"e1","from":"doc:readme","to":"doc:readme","relation":"references"}',
        ]),
        encoding="utf-8",
    )
    (repo / "archive/knowledge_graph/ORCS_ROUTE_INDEX.seed.jsonl").write_text(
        '{"route_id":"r1","domain":"docs","route_class":"README","source_path":"README.md","target_surface":"README.md","seat":"S1","trust_state":"candidate"}',
        encoding="utf-8",
    )
    (repo / "README.md").write_text("# temp\n", encoding="utf-8")

    content = build_graph_index(repo)

    output = repo / "archive/knowledge_graph/GRAPH_INDEX.md"
    assert output.exists()
    assert content == output.read_text(encoding="utf-8")
    assert "Nodes: **1**" in content


def test_validate_graph_passes_for_repo_state():
    validate_graph(ROOT)


def test_validate_graph_rejects_missing_edge_target(tmp_path: Path):
    repo = tmp_path / "repo"
    (repo / "archive/knowledge_graph").mkdir(parents=True)
    (repo / "archive/knowledge_graph/GRAPH_SEED.jsonl").write_text(
        '\n'.join([
            '{"record_type":"node","node_id":"doc:readme","kind":"document","label":"README","path":"README.md"}',
            '{"record_type":"edge","edge_id":"e1","from":"doc:readme","to":"doc:missing","relation":"references"}',
        ]),
        encoding="utf-8",
    )
    (repo / "archive/knowledge_graph/ORCS_ROUTE_INDEX.seed.jsonl").write_text(
        '{"route_id":"r1","domain":"docs","route_class":"README","source_path":"README.md","target_surface":"README.md","seat":"S1","trust_state":"candidate"}',
        encoding="utf-8",
    )
    (repo / "archive/knowledge_graph/GRAPH_INDEX.md").write_text(
        "SOURCE: scripts/build_lattice_global_index.py\n",
        encoding="utf-8",
    )
    (repo / "README.md").write_text("# temp\n", encoding="utf-8")

    with pytest.raises(ValidationError, match="unknown-edge-target"):
        validate_graph(repo)


def test_kg_query_supports_term_and_seat_filters():
    route_results = run_query("graph index", seat="S7", root=ROOT)
    assert any(item.get("record_family") == "route" for item in route_results)

    node_results = run_query("repository readme", root=ROOT)
    assert any(item.get("node_id") == "doc:readme" for item in node_results)
