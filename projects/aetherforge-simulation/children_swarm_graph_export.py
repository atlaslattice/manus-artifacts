"""Export the Children of the Swarm v0.2 derived lattice as a knowledge graph.

This exporter uses the compact manifest and deterministically expands it into
node/surface/task graph objects. It does not read or mutate the raw workbook.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable

MANIFEST_PATH = Path(__file__).with_name("children_swarm_original_deduped_lattice_v0_2.json")
PROJECT_ID = "project:children-of-the-swarm-v0.2"
RAW_ID = "artifact:raw-workbook:cots-12x12-v0.1"
DERIVED_ID = "artifact:derived-lattice:cots-original-deduped-v0.2"
BOUNDARY_ID = "boundary:raw-preserved-non-canon-staging"


def load_manifest(path: Path = MANIFEST_PATH) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_key(value: str) -> str:
    return "".join(ch.lower() if ch.isalnum() else "-" for ch in value).strip("-")


def node(node_id: str, label: str, node_type: str, **properties: Any) -> dict[str, Any]:
    return {"id": node_id, "label": label, "type": node_type, "properties": properties}


def edge(source: str, relation: str, target: str, **properties: Any) -> dict[str, Any]:
    return {"source": source, "relation": relation, "target": target, "properties": properties}


def derived_task_title(node_name: str, surface_name: str) -> str:
    return f"Map {node_name} across {surface_name} as a receipt-preserving lattice slice"


def expand_derived_tasks(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    nodes = manifest["node_order"]
    surfaces = manifest["source_surfaces"]
    tasks: list[dict[str, Any]] = []
    for node_index, node_name in enumerate(nodes, start=1):
        for surface_index, surface_name in enumerate(surfaces, start=1):
            tasks.append(
                {
                    "task_id": f"ORIG-{node_index:02d}-{surface_index:02d}",
                    "node_name": node_name,
                    "surface_name": surface_name,
                    "node_index": node_index,
                    "surface_index": surface_index,
                    "title": derived_task_title(node_name, surface_name),
                    "raw_rows_covered": manifest["dimensions"]["raw_rows_per_derived_task"],
                    "status": "candidate_staging",
                }
            )
    return tasks


def validate_manifest(manifest: dict[str, Any]) -> dict[str, Any]:
    tasks = expand_derived_tasks(manifest)
    titles = [task["title"] for task in tasks]
    task_ids = [task["task_id"] for task in tasks]
    dimensions = manifest["dimensions"]
    boundary = manifest["boundary"]
    covered = sum(task["raw_rows_covered"] for task in tasks)
    report = {
        "node_count": len(manifest["node_order"]),
        "surface_count": len(manifest["source_surfaces"]),
        "derived_task_count": len(tasks),
        "unique_task_ids": len(set(task_ids)),
        "unique_titles": len(set(titles)),
        "duplicate_titles": len(titles) - len(set(titles)),
        "raw_rows_covered": covered,
        "raw_logs_unchanged": boundary.get("raw_logs_unchanged") is True,
        "canon_adjustments": boundary.get("canon_adjustments") is False,
        "deployment_claims": boundary.get("deployment_claims") is False,
        "authority_claims": boundary.get("authority_claims") is False,
    }
    report["ok"] = (
        report["node_count"] == dimensions["nodes"] == 12
        and report["surface_count"] == dimensions["source_surfaces"] == 12
        and report["derived_task_count"] == dimensions["derived_tasks"] == 144
        and report["unique_task_ids"] == 144
        and report["unique_titles"] == 144
        and report["duplicate_titles"] == 0
        and report["raw_rows_covered"] == dimensions["raw_rows_covered"] == 1728
        and report["raw_logs_unchanged"]
        and report["canon_adjustments"]
        and report["deployment_claims"]
        and report["authority_claims"]
    )
    return report


def build_graph(manifest_path: Path = MANIFEST_PATH) -> dict[str, Any]:
    manifest = load_manifest(manifest_path)
    validation = validate_manifest(manifest)
    tasks = expand_derived_tasks(manifest)

    nodes: list[dict[str, Any]] = [
        node(PROJECT_ID, "Children of the Swarm v0.2 derived lattice", "Project"),
        node(RAW_ID, manifest["source_raw_file"], "RawWorkbook", preserved=True),
        node(DERIVED_ID, "Original deduped lattice v0.2", "DerivedLattice", **manifest["dimensions"]),
        node(BOUNDARY_ID, "Raw-preserved non-canon staging boundary", "Boundary", **manifest["boundary"]),
    ]
    edges: list[dict[str, Any]] = [
        edge(PROJECT_ID, "contains", RAW_ID),
        edge(PROJECT_ID, "contains", DERIVED_ID),
        edge(RAW_ID, "source_for", DERIVED_ID),
        edge(BOUNDARY_ID, "constrains", PROJECT_ID),
        edge(BOUNDARY_ID, "constrains", DERIVED_ID),
    ]

    for index, node_name in enumerate(manifest["node_order"], start=1):
        nid = f"swarm-node:{index:02d}:{canonical_key(node_name)}"
        nodes.append(node(nid, node_name, "SwarmNode", index=index))
        edges.append(edge(DERIVED_ID, "contains", nid))

    for index, surface_name in enumerate(manifest["source_surfaces"], start=1):
        sid = f"source-surface:{index:02d}:{canonical_key(surface_name)}"
        nodes.append(node(sid, surface_name, "SourceSurface", index=index))
        edges.append(edge(DERIVED_ID, "maps_surface", sid))

    for task in tasks:
        tid = f"derived-task:{task['task_id']}"
        nid = f"swarm-node:{task['node_index']:02d}:{canonical_key(task['node_name'])}"
        sid = f"source-surface:{task['surface_index']:02d}:{canonical_key(task['surface_name'])}"
        nodes.append(node(tid, task["title"], "DerivedTask", **task))
        edges.extend(
            [
                edge(DERIVED_ID, "contains", tid),
                edge(tid, "belongs_to_node", nid),
                edge(tid, "belongs_to_surface", sid),
                edge(tid, "compresses_raw_rows", RAW_ID, raw_rows=task["raw_rows_covered"]),
                edge(BOUNDARY_ID, "constrains", tid),
            ]
        )

    graph = {
        "schema_version": "children_swarm.knowledge_graph.v0_2",
        "project": PROJECT_ID,
        "source_manifest": str(manifest_path.name),
        "validation": validation,
        "summary": {
            "nodes": len(nodes),
            "edges": len(edges),
            "swarm_nodes": validation["node_count"],
            "source_surfaces": validation["surface_count"],
            "derived_tasks": validation["derived_task_count"],
            "raw_rows_covered": validation["raw_rows_covered"],
        },
        "nodes": sorted(nodes, key=lambda item: item["id"]),
        "edges": sorted(edges, key=lambda item: (item["source"], item["relation"], item["target"])),
    }
    return graph


def render_text(graph: dict[str, Any]) -> str:
    summary = graph["summary"]
    return "\n".join(
        [
            "Children of the Swarm derived lattice graph",
            f"nodes: {summary['nodes']}",
            f"edges: {summary['edges']}",
            f"swarm_nodes: {summary['swarm_nodes']}",
            f"source_surfaces: {summary['source_surfaces']}",
            f"derived_tasks: {summary['derived_tasks']}",
            f"raw_rows_covered: {summary['raw_rows_covered']}",
            f"validation_ok: {graph['validation']['ok']}",
        ]
    )


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Export Children of the Swarm v0.2 as a knowledge graph.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    parser.add_argument("--manifest-path", default=str(MANIFEST_PATH), help="Path to compact manifest JSON.")
    args = parser.parse_args(list(argv) if argv is not None else None)
    graph = build_graph(Path(args.manifest_path))
    print(json.dumps(graph, indent=2, sort_keys=True) if args.json else render_text(graph))
    return 0 if graph["validation"]["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
