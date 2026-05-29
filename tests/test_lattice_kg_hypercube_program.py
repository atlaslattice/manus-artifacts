import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX_JSON = ROOT / "docs" / "generated" / "LATTICE_GLOBAL_INDEX.json"
ADJ_JSON = ROOT / "docs" / "generated" / "KG_ADJACENCY_MATRIX.json"


def run(cmd):
    result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0, f"{' '.join(cmd)} failed\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}"


def load_index():
    return json.loads(INDEX_JSON.read_text(encoding="utf-8"))


def test_lattice_topology_pipeline_builds():
    run(["python", "scripts/check_graph_link_integrity.py"])
    run(["python", "scripts/build_lattice_global_index.py"])
    run(["python", "scripts/validate_lattice_quality_gates.py"])
    run(["python", "scripts/kg_mermaid_autogen.py"])
    run(["python", "scripts/kg_node_quality_scorer.py"])
    run(["python", "scripts/kg_dangling_ref_detector.py"])


def test_lattice_topology_invariants():
    run(["python", "scripts/build_lattice_global_index.py"])
    data = load_index()
    metrics = data["metrics"]
    node_ids = {node["id"] for node in data["nodes"]}

    assert metrics["node_count"] >= 20
    assert metrics["edge_density"] >= 1.0
    assert metrics["unknown_link_count"] == 0

    for node in data["nodes"]:
        assert node["exists"], f"missing file for node {node['id']}"
        for link in node["links"]:
            assert link in node_ids, f"unknown link {link} from {node['id']}"


def test_adjacency_matrix_output_exists_and_matches_nodes():
    run(["python", "scripts/build_lattice_global_index.py"])
    payload = json.loads(ADJ_JSON.read_text(encoding="utf-8"))
    index = load_index()
    assert payload["status"] == "Candidate"
    assert len(payload["adjacency"]) == index["metrics"]["node_count"]
