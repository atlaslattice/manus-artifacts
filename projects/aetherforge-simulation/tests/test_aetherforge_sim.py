from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import aetherforge_sim
import graph_export


ROOT = Path(__file__).resolve().parents[1]
MATRIX_PATH = ROOT / "task-matrix-12x12.json"


def test_matrix_is_exactly_12_by_12() -> None:
    matrix = aetherforge_sim.load_matrix(MATRIX_PATH)
    report = aetherforge_sim.validate_matrix(matrix)
    assert report.ok
    assert report.domain_count == 12
    assert report.tasks_per_domain == 12
    assert report.task_count == 144
    assert report.unique_task_ids == 144
    assert report.boundary_ok


def test_task_ids_are_stable_and_unique() -> None:
    matrix = aetherforge_sim.load_matrix(MATRIX_PATH)
    tasks = aetherforge_sim.expand_tasks(matrix)
    task_ids = [task["id"] for task in tasks]
    assert len(task_ids) == len(set(task_ids))
    assert task_ids[0] == "D01-T01"
    assert task_ids[-1] == "D12-T12"


def test_simulation_is_deterministic() -> None:
    matrix = aetherforge_sim.load_matrix(MATRIX_PATH)
    first = aetherforge_sim.simulate(matrix, steps=12, seed=144)
    second = aetherforge_sim.simulate(matrix, steps=12, seed=144)
    assert first == second
    assert first["steps"] == 12
    assert len(first["receipts"]) == 12


def test_receipt_chain_links_every_step() -> None:
    matrix = aetherforge_sim.load_matrix(MATRIX_PATH)
    result = aetherforge_sim.simulate(matrix, steps=20, seed=7)
    receipts = result["receipts"]
    for previous, current in zip(receipts, receipts[1:]):
        assert current["previous_head"] == previous["head"]
    assert result["receipt_head"] == receipts[-1]["head"]


def test_graph_export_maps_matrix_to_lattice() -> None:
    graph = graph_export.build_graph(MATRIX_PATH)
    assert graph["validation"]["ok"] is True
    assert graph["summary"]["tasks"] == 144
    assert graph["summary"]["domains"] == 12
    node_ids = {node["id"] for node in graph["nodes"]}
    edge_pairs = {(edge["source"], edge["relation"], edge["target"]) for edge in graph["edges"]}
    assert "project:aetherforge-simulation" in node_ids
    assert "boundary:non_canon_simulation" in node_ids
    assert "task:D01-T01" in node_ids
    assert "task:D12-T12" in node_ids
    assert ("boundary:non_canon_simulation", "constrains", "project:aetherforge-simulation") in edge_pairs
    assert ("cmd:simulate", "generates", "receipt:chain") in edge_pairs


def test_cli_validate_json() -> None:
    completed = subprocess.run(
        [sys.executable, "aetherforge_sim.py", "--json", "--matrix-path", str(MATRIX_PATH), "validate"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(completed.stdout)
    assert payload["ok"] is True
    assert payload["task_count"] == 144


def test_cli_simulate_json() -> None:
    completed = subprocess.run(
        [sys.executable, "aetherforge_sim.py", "--json", "--matrix-path", str(MATRIX_PATH), "simulate", "--steps", "3", "--seed", "144"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(completed.stdout)
    assert payload["steps"] == 3
    assert len(payload["receipts"]) == 3
    assert payload["boundary"]["canon_adjustments"] is False


def test_cli_graph_export_json() -> None:
    completed = subprocess.run(
        [sys.executable, "graph_export.py", "--json", "--matrix-path", str(MATRIX_PATH)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(completed.stdout)
    assert payload["schema_version"] == "aetherforge.lattice_graph.v1"
    assert payload["validation"]["ok"] is True
    assert payload["summary"]["tasks"] == 144
