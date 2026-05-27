"""Export the Aetherforge simulation sandbox as a knowledge graph."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable

import aetherforge_sim

ROOT = Path(__file__).resolve().parent
MATRIX_PATH = ROOT / "task-matrix-12x12.json"

PROJECT_ID = "project:aetherforge-simulation"
BOUNDARY_ID = "boundary:non_canon_simulation"


def node(node_id: str, label: str, node_type: str, **props: Any) -> dict[str, Any]:
    return {"id": node_id, "label": label, "type": node_type, "properties": props}


def edge(source: str, relation: str, target: str, **props: Any) -> dict[str, Any]:
    return {"source": source, "relation": relation, "target": target, "properties": props}


def file_id(path: str) -> str:
    return f"file:{path}"


def command_id(command: str) -> str:
    return f"cmd:{command}"


def build_graph(matrix_path: Path = MATRIX_PATH) -> dict[str, Any]:
    matrix = aetherforge_sim.load_matrix(matrix_path)
    report = aetherforge_sim.validate_matrix(matrix)
    tasks = aetherforge_sim.expand_tasks(matrix)

    nodes: list[dict[str, Any]] = []
    edges: list[dict[str, Any]] = []

    nodes.append(node(PROJECT_ID, "Aetherforge Simulation Sandbox", "Project", status=matrix.get("status")))
    nodes.append(node(BOUNDARY_ID, "Non-canon local simulation boundary", "Boundary", **matrix["boundary"]))
    edges.append(edge(BOUNDARY_ID, "constrains", PROJECT_ID))

    files = [
        "README.md",
        "task-matrix-12x12.json",
        "aetherforge_sim.py",
        "graph_export.py",
        "tests/test_aetherforge_sim.py",
        "pyproject.toml",
        "CONTRIBUTING.md",
        "KNOWLEDGE_GRAPH.md",
        ".github/workflows/aetherforge-simulation.yml",
    ]
    for path in files:
        fid = file_id(path)
        nodes.append(node(fid, path, "File", path=path))
        edges.append(edge(PROJECT_ID, "contains", fid))

    domains_by_name = {domain["name"]: domain for domain in matrix["domains"]}
    for domain in matrix["domains"]:
        did = f"domain:{domain['id']}"
        nodes.append(node(did, domain["name"], "Domain", domain_id=domain["id"], task_count=len(domain["tasks"])))
        edges.append(edge(file_id("task-matrix-12x12.json"), "defines", did))
        edges.append(edge(PROJECT_ID, "contains", did))
        edges.append(edge(BOUNDARY_ID, "constrains", did))

    for task in tasks:
        tid = f"task:{task['id']}"
        did = f"domain:D{task['domain_index']:02d}"
        nodes.append(node(tid, task["title"], "Task", task_id=task["id"], domain=task["domain"], task_index=task["task_index"], simulation_value=task["simulation_value"], status=task["status"]))
        edges.append(edge(did, "contains", tid))
        edges.append(edge(file_id("task-matrix-12x12.json"), "defines", tid))
        edges.append(edge(BOUNDARY_ID, "constrains", tid))

    commands = {
        "validate": "python -m aetherforge_sim validate",
        "matrix": "python -m aetherforge_sim matrix",
        "simulate": "python -m aetherforge_sim --json simulate --steps 12 --seed 144",
        "test": "pytest",
    }
    for name, command in commands.items():
        cid = command_id(name)
        nodes.append(node(cid, command, "Command", command=command))
        edges.append(edge(file_id("README.md"), "documents", cid))
        edges.append(edge(file_id("aetherforge_sim.py"), "implements", cid if name != "test" else command_id("test")))

    edges.extend([
        edge(command_id("validate"), "validates", file_id("task-matrix-12x12.json")),
        edge(command_id("matrix"), "summarizes", file_id("task-matrix-12x12.json")),
        edge(command_id("simulate"), "generates", "receipt:chain"),
        edge(command_id("simulate"), "emits", "metric:matrix_fingerprint"),
        edge(command_id("simulate"), "emits", "metric:receipt_head"),
        edge(command_id("test"), "validates", file_id("task-matrix-12x12.json")),
        edge(command_id("test"), "validates", file_id("aetherforge_sim.py")),
        edge(file_id("tests/test_aetherforge_sim.py"), "validates", file_id("aetherforge_sim.py")),
        edge(file_id("KNOWLEDGE_GRAPH.md"), "documents", PROJECT_ID),
        edge(file_id("graph_export.py"), "exports", "graph:lattice"),
    ])

    nodes.extend([
        node("receipt:chain", "Deterministic receipt chain", "ReceiptClass"),
        node("metric:matrix_fingerprint", "Matrix fingerprint", "Metric"),
        node("metric:receipt_head", "Receipt head", "Metric"),
        node("graph:lattice", "Aetherforge lattice graph", "Graph", node_count_estimate=len(nodes), edge_count_estimate=len(edges)),
    ])

    graph = {
        "schema_version": "aetherforge.lattice_graph.v1",
        "project": PROJECT_ID,
        "validation": report.to_dict(),
        "summary": {
            "nodes": len(nodes),
            "edges": len(edges),
            "domains": report.domain_count,
            "tasks": report.task_count,
        },
        "nodes": sorted(nodes, key=lambda item: item["id"]),
        "edges": sorted(edges, key=lambda item: (item["source"], item["relation"], item["target"])),
    }
    return graph


def render_text(graph: dict[str, Any]) -> str:
    summary = graph["summary"]
    return "\n".join([
        "Aetherforge lattice graph",
        f"nodes: {summary['nodes']}",
        f"edges: {summary['edges']}",
        f"domains: {summary['domains']}",
        f"tasks: {summary['tasks']}",
        f"validation_ok: {graph['validation']['ok']}",
    ])


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Export Aetherforge simulation sandbox knowledge graph.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    parser.add_argument("--matrix-path", default=str(MATRIX_PATH), help="Path to task matrix JSON.")
    args = parser.parse_args(list(argv) if argv is not None else None)
    graph = build_graph(Path(args.matrix_path))
    print(json.dumps(graph, indent=2, sort_keys=True) if args.json else render_text(graph))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
