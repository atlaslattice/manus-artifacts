"""Tests for build_lattice_graph.py — graph build pipeline."""
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SCRIPT = REPO_ROOT / "scripts" / "build_lattice_graph.py"
NODES_OUT = REPO_ROOT / "docs" / "lattice_graph_nodes.json"
GRAPH_OUT = REPO_ROOT / "docs" / "lattice_graph.json"


def test_script_exists():
    assert SCRIPT.exists(), f"script not found: {SCRIPT}"


def test_graph_output_exists():
    """docs/lattice_graph_nodes.json must exist after the graph build."""
    assert NODES_OUT.exists(), f"lattice_graph_nodes.json missing — run build_lattice_graph.py"


def test_nodes_json_is_list():
    data = json.loads(NODES_OUT.read_text())
    assert isinstance(data, list), "lattice_graph_nodes.json must be a JSON array"


def test_nodes_have_required_keys():
    data = json.loads(NODES_OUT.read_text())
    assert len(data) > 0, "nodes list should not be empty"
    required = {"id", "label", "type", "h", "s", "n", "hsn"}
    for node in data[:20]:  # spot-check first 20
        missing = required - node.keys()
        assert not missing, f"Node {node.get('id')} missing keys: {missing}"


def test_hsn_format():
    data = json.loads(NODES_OUT.read_text())
    import re
    pattern = re.compile(r"^H\d{2}-S\d{2}-N\d{2}$")
    # Only check nodes that have an HSN coordinate assigned
    with_hsn = [n for n in data if n.get("hsn")]
    assert len(with_hsn) > 0, "Expected at least some nodes with HSN coordinates"
    bad = [n["hsn"] for n in with_hsn if not pattern.match(str(n["hsn"]))]
    assert not bad, f"Invalid HSN coordinates: {bad[:5]}"


def test_house_range():
    data = json.loads(NODES_OUT.read_text())
    # Only validate nodes that have h assigned (h>0)
    with_house = [n for n in data if n.get("h", 0) > 0]
    assert len(with_house) > 0, "Expected at least some nodes with house assigned"
    bad = [n for n in with_house if not (1 <= n.get("h", 0) <= 12)]
    assert not bad, f"Nodes with out-of-range house: {[n['id'] for n in bad[:5]]}"


def test_graph_json_exists():
    assert GRAPH_OUT.exists(), "lattice_graph.json missing"


def test_graph_json_has_nodes_and_edges():
    data = json.loads(GRAPH_OUT.read_text())
    assert "@graph" in data or "nodes" in data or "graph" in data, \
        "lattice_graph.json should contain @graph or nodes key"


def test_minimum_node_count():
    """We expect at least 300 nodes (144 elements + seed data + markdown)."""
    data = json.loads(NODES_OUT.read_text())
    assert len(data) >= 300, f"Expected ≥300 nodes, got {len(data)}"
