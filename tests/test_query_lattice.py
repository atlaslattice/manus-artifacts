"""Tests for query_lattice.py — CLI graph query interface."""
import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SCRIPT = REPO_ROOT / "scripts" / "query_lattice.py"
NODES_FILE = REPO_ROOT / "docs" / "lattice_graph_nodes.json"


def run_query(*args):
    result = subprocess.run(
        [sys.executable, str(SCRIPT)] + list(args),
        capture_output=True, text=True, cwd=str(REPO_ROOT)
    )
    return result


def test_script_exists():
    assert SCRIPT.exists()


def test_stats():
    r = run_query("--stats")
    assert r.returncode == 0, f"--stats failed: {r.stderr}"
    assert "Total nodes" in r.stdout or "nodes" in r.stdout.lower()


def test_list_houses():
    r = run_query("--list-houses")
    assert r.returncode == 0
    assert "H01" in r.stdout


def test_filter_by_house():
    r = run_query("--house", "1")
    assert r.returncode == 0
    # Should return element nodes
    assert "H01" in r.stdout


def test_filter_by_house_sphere():
    r = run_query("--house", "1", "--sphere", "1")
    assert r.returncode == 0


def test_filter_by_type():
    r = run_query("--type", "element")
    assert r.returncode == 0
    assert "element" in r.stdout


def test_no_args_shows_help_or_stats():
    r = run_query()
    # Either shows help or stats — should not crash
    assert r.returncode == 0


def test_artifact_id_lookup():
    if not NODES_FILE.exists():
        return
    data = json.loads(NODES_FILE.read_text())
    if not data:
        return
    first_id = data[0]["id"]
    r = run_query("--artifact-id", first_id)
    assert r.returncode == 0
    assert first_id in r.stdout
