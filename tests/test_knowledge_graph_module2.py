from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def _load(path: str):
    return yaml.safe_load((ROOT / path).read_text(encoding="utf-8"))


def test_module2_node_edge_schema_contains_required_types():
    schema = _load("archive/knowledge_graph/KG_NODE_EDGE_SCHEMA_v0.1.yaml")

    node_types = set(schema["graph_node_schema"]["node_types"].keys())
    assert {
        "raw_source",
        "parsed_fact",
        "claim",
        "evidence",
        "review",
        "action_candidate",
    }.issubset(node_types)

    edge_types = set(schema["graph_edge_schema"]["edge_types"].keys())
    assert {"derived_from", "supports", "contradicts"}.issubset(edge_types)


def test_module2_schema_guardrails_present():
    schema = _load("archive/knowledge_graph/KG_NODE_EDGE_SCHEMA_v0.1.yaml")
    guardrails = schema["guardrails"]
    assert "Graph is not memory" in guardrails
    assert "Graph is not canon" in guardrails
    assert "Graph is not authority" in guardrails


def test_module2_source_inventory_seeded_from_180_183_182():
    inv = _load("archive/knowledge_graph/KG_SOURCE_INVENTORY_2026-05-26.yaml")
    records = inv["source_inventory"]
    source_ids = {r["source_id"] for r in records}

    assert {"github-issue-180", "github-issue-183", "github-pr-182"}.issubset(source_ids)

    for record in records:
        assert record["related_lane"] == "openai-graph"
        assert record["surface"] == "GitHub"
        assert record["raw_export_status"] in {"full_raw", "partial_raw", "summary_only", "unavailable"}
