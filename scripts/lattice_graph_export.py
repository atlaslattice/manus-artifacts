"""
lattice_graph_export.py — T68: Lattice JSON-LD / Graph Export
Rainbow Yin Yang Lattice — 12×12×12 Hypercube Data Fabric

Exports seed nodes and Metatron geometry as a JSON-LD graph
compatible with the existing KG adjacency matrix format.

Status: Candidate
Date: 2026-05-29
Author: TIDELOCKBrain / @atlaslattice
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

# Ensure scripts/ is on the path for sibling imports
SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

from lattice_node_seeder import generate_seed_nodes          # noqa: E402
from lattice_coordinate_mapper import CoordinateMapper       # noqa: E402
from lattice_cross_axis_bridge import CrossAxisBridge        # noqa: E402
from lattice_metatron_geometry import MetatronGeometry       # noqa: E402

DATA_DIR = (
    Path(__file__).resolve().parent.parent
    / "archive" / "spec" / "lattice-hypercube" / "data"
)


JSON_LD_CONTEXT = {
    "@vocab": "https://atlaslattice.github.io/manus-artifacts/lattice/",
    "id": "@id",
    "type": "@type",
    "LatticeNode": "LatticeNode",
    "LatticeEdge": "LatticeEdge",
    "address": "hasAddress",
    "properties": "hasProperties",
    "node_type": "hasNodeType",
    "yin_yang": "hasYinYangBalance",
    "seed_class": "hasSeedClass",
    "coupling_weight": "hasCouplingWeight",
}


def build_graph(
    seed_nodes: list[dict[str, Any]],
    coupling_matrix: list[list[float]],
    metatron: dict[str, Any],
) -> dict[str, Any]:
    """Build a JSON-LD graph from seed nodes + coupling matrix + geometry."""
    graph_nodes: list[dict[str, Any]] = []
    graph_edges: list[dict[str, Any]] = []

    # Add seed nodes
    for node in seed_nodes:
        graph_nodes.append({
            "@type": "LatticeNode",
            "@id": f"node:{node['node_id']}",
            "node_id": node["node_id"],
            "address": node["address"],
            "properties": node["properties"],
            "node_type": node["node_type"],
            "yin_yang": node["yin_yang"],
            "seed_class": node["seed_class"],
            "status": "Candidate",
        })

    # Add axis-coupling edges (Metatron edges represent axis couplings)
    for edge in metatron.get("edges", []):
        graph_edges.append({
            "@type": "LatticeEdge",
            "@id": f"edge:{edge['source']}-{edge['target']}",
            "source": f"axis:{edge['source']}",
            "target": f"axis:{edge['target']}",
            "edge_type": edge["type"],
            "coupling_weight": edge["weight"],
        })

    # Add axis-to-axis coupling edges from coupling matrix
    axis_ids = [f"AX-{i:02d}" for i in range(1, 13)]
    for i, ax_a in enumerate(axis_ids):
        for j, ax_b in enumerate(axis_ids):
            if i >= j:
                continue
            weight = coupling_matrix[i][j]
            if weight > 0.3:  # only include significant couplings
                graph_edges.append({
                    "@type": "LatticeEdge",
                    "@id": f"edge:coupling-{ax_a}-{ax_b}",
                    "source": f"axis:{ax_a}",
                    "target": f"axis:{ax_b}",
                    "edge_type": "coupling",
                    "coupling_weight": round(weight, 4),
                })

    return {
        "@context": JSON_LD_CONTEXT,
        "schema_version": "0.1",
        "status": "Candidate",
        "date": "2026-05-29",
        "author": "TIDELOCKBrain / @atlaslattice",
        "graph_type": "RainbowYinYangLattice",
        "dimensions": 12,
        "total_nodes": len(graph_nodes),
        "total_edges": len(graph_edges),
        "@graph": graph_nodes + graph_edges,
    }


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    print("⚙  Generating seed nodes...")
    seed_nodes = generate_seed_nodes()

    print("⚙  Building coupling matrix...")
    bridge = CrossAxisBridge()
    coupling_matrix = bridge.full_coupling_matrix()

    print("⚙  Generating Metatron geometry...")
    geo = MetatronGeometry()
    metatron = geo.export_json()

    print("⚙  Building JSON-LD graph...")
    graph = build_graph(seed_nodes, coupling_matrix, metatron)

    out_path = DATA_DIR / "LATTICE_GRAPH_EXPORT.json"
    out_path.write_text(
        json.dumps(graph, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"✅  Lattice graph export: {graph['total_nodes']} nodes, "
          f"{graph['total_edges']} edges → {out_path.name}")


if __name__ == "__main__":
    main()
