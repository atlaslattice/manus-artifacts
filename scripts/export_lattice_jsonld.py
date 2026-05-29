from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.build_lattice_global_index import load_graph_data

HOUSE_REGISTRY_PATH = ROOT / "archive/knowledge_graph/HOUSE_SEED_REGISTRY.json"
JSONLD_OUTPUT_PATH = ROOT / "archive/knowledge_graph/LATTICE_KG.jsonld"


@dataclass(frozen=True)
class ExportStats:
    nodes: int
    edges: int
    routes: int
    cells: int


def load_house_registry(path: Path = HOUSE_REGISTRY_PATH) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload.get("houses", [])


def _coordinate_for_index(index: int) -> str:
    h = (index % 12) + 1
    s = ((index // 12) % 12) + 1
    n = ((index // (12 * 12)) % 12) + 1
    return f"H{h:02d}-S{s:02d}-N{n:02d}"


def build_hsn_cells() -> list[dict[str, str]]:
    cells: list[dict[str, str]] = []
    for h in range(1, 13):
        for s in range(1, 13):
            for n in range(1, 13):
                cells.append(
                    {
                        "@id": f"cell:H{h:02d}-S{s:02d}-N{n:02d}",
                        "@type": "LatticeCell",
                        "hsn": f"H{h:02d}-S{s:02d}-N{n:02d}",
                        "house": f"H{h:02d}",
                        "sphere": f"S{s:02d}",
                        "node": f"N{n:02d}",
                    }
                )
    return cells


def _to_jsonld_graph() -> tuple[list[dict[str, Any]], ExportStats]:
    graph = load_graph_data(ROOT)
    houses = load_house_registry()
    cells = build_hsn_cells()
    records: list[dict[str, Any]] = []

    for index, node in enumerate(graph.nodes):
        house = houses[index % len(houses)] if houses else {}
        records.append(
            {
                "@id": f"node:{node['node_id']}",
                "@type": "GraphNode",
                "node_id": node["node_id"],
                "label": node.get("label", ""),
                "kind": node.get("kind", "unknown"),
                "path": node.get("path", ""),
                "hsn": node.get("hsn", _coordinate_for_index(index)),
                "house_seed": house.get("seed_ref"),
            }
        )

    for edge in graph.edges:
        records.append(
            {
                "@id": f"edge:{edge['edge_id']}",
                "@type": "GraphEdge",
                "edge_id": edge["edge_id"],
                "from": edge.get("from"),
                "to": edge.get("to"),
                "relation": edge.get("relation"),
            }
        )

    for route in graph.routes:
        records.append(
            {
                "@id": f"route:{route['route_id']}",
                "@type": "ReviewRoute",
                "route_id": route["route_id"],
                "domain": route.get("domain"),
                "route_class": route.get("route_class"),
                "source_path": route.get("source_path"),
                "target_surface": route.get("target_surface"),
                "seat": route.get("seat"),
                "trust_state": route.get("trust_state", "candidate"),
            }
        )

    records.extend(cells)
    return records, ExportStats(
        nodes=len(graph.nodes),
        edges=len(graph.edges),
        routes=len(graph.routes),
        cells=len(cells),
    )


def export_jsonld(output_path: Path = JSONLD_OUTPUT_PATH) -> ExportStats:
    graph, stats = _to_jsonld_graph()
    payload = {
        "@context": {
            "hsn": "https://atlaslattice.org/ns/hsn",
            "node_id": "https://atlaslattice.org/ns/node_id",
            "edge_id": "https://atlaslattice.org/ns/edge_id",
            "route_id": "https://atlaslattice.org/ns/route_id",
            "from": {"@id": "https://atlaslattice.org/ns/from"},
            "to": {"@id": "https://atlaslattice.org/ns/to"},
            "seat": "https://atlaslattice.org/ns/seat",
            "trust_state": "https://atlaslattice.org/ns/trust_state",
        },
        "@graph": graph,
    }
    output_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    return stats


def main() -> int:
    stats = export_jsonld(JSONLD_OUTPUT_PATH)
    print(
        f"jsonld-exported nodes={stats.nodes} edges={stats.edges} "
        f"routes={stats.routes} cells={stats.cells} path={JSONLD_OUTPUT_PATH}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
