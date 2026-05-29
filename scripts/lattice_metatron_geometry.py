"""
lattice_metatron_geometry.py — T66: Metatron's Cube Geometry Export
Rainbow Yin Yang Lattice — 12×12×12 Hypercube Data Fabric

Generates the Metatron's Cube geometry for the 1728-node lattice:
- 13-node Fruit of Life geometry (1 centre + 12 outer circles)
- Full Metatron's Cube edge set (78 lines connecting all 13 nodes)
- 3D hypercube projection coordinates
- SVG-ready coordinate table

The geometry maps to the 12 primary axes + 1 apex of the lattice.

Status: Candidate
Date: 2026-05-29
Author: TIDELOCKBrain / @atlaslattice
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

DATA_DIR = (
    Path(__file__).resolve().parent.parent
    / "archive" / "spec" / "lattice-hypercube" / "data"
)


@dataclass
class GeometryNode:
    """A node in the Metatron's Cube geometry."""
    id: str
    label: str
    x: float          # 2D projected x (SVG)
    y: float          # 2D projected y (SVG)
    z: float          # 3D z coordinate (depth)
    radius: float     # Circle radius for Fruit of Life
    axis_id: str      # Corresponding lattice axis (AX-01 to AX-12 or APEX)
    color: str        # Hex color
    symbol: str       # Unicode symbol


@dataclass
class GeometryEdge:
    """An edge in Metatron's Cube."""
    source: str
    target: str
    type: str         # "spine" | "outer" | "cross"
    weight: float     # coupling weight


class MetatronGeometry:
    """
    Metatron's Cube geometry generator.

    Structure:
    - 1 central node (APEX / centre of the cube)
    - 12 outer nodes arranged in 2 rings of 6 (hexagonal layers)
    - All 13×12/2 = 78 edges connecting every pair

    The 12 outer nodes map to the 12 lattice axes.
    Radii follow the sacred geometry ratio 1 : √3 : 2.
    """

    # Sacred geometry radii (normalized, centre = 1.0)
    INNER_RING_RADIUS = 1.0
    OUTER_RING_RADIUS = 2.0
    NODE_CIRCLE_RADIUS = 0.4  # Circle radius for Fruit of Life

    # Color palette — Rainbow Yin Yang Lattice
    AXIS_COLORS = {
        "AX-01": "#FF3333",   # Frequency — red
        "AX-02": "#FF8C00",   # MatterState — orange
        "AX-03": "#FFD700",   # Element — gold
        "AX-04": "#7FFF00",   # Spin — chartreuse
        "AX-05": "#00CED1",   # Acoustic — dark turquoise
        "AX-06": "#1E90FF",   # ColorHarmonic — dodger blue
        "AX-07": "#9400D3",   # Neuromorphic — violet
        "AX-08": "#FF69B4",   # YinYangBalance — hot pink
        "AX-09": "#C0C0C0",   # Riemann — silver
        "AX-10": "#8B4513",   # Temporal — saddle brown
        "AX-11": "#2E8B57",   # SpatialTopology — sea green
        "AX-12": "#191970",   # Information — midnight blue
        "APEX": "#FFFFFF",     # Unified Field Apex — white
    }

    AXIS_SYMBOLS = {
        "AX-01": "ν", "AX-02": "Φ", "AX-03": "Ε", "AX-04": "σ",
        "AX-05": "Ω", "AX-06": "λ", "AX-07": "Ψ", "AX-08": "☯",
        "AX-09": "ζ", "AX-10": "τ", "AX-11": "Τ", "AX-12": "ℐ",
        "APEX": "✦",
    }

    AXIS_LABELS = {
        "AX-01": "Frequency", "AX-02": "MatterState", "AX-03": "Element",
        "AX-04": "Spin", "AX-05": "Acoustic", "AX-06": "ColorHarmonic",
        "AX-07": "Neuromorphic", "AX-08": "YinYangBalance",
        "AX-09": "RiemannOperator", "AX-10": "Temporal",
        "AX-11": "SpatialTopology", "AX-12": "Information",
        "APEX": "UnifiedFieldApex",
    }

    def generate_nodes(self) -> list[GeometryNode]:
        """Generate the 13 Metatron geometry nodes."""
        nodes: list[GeometryNode] = []

        # Centre node (APEX)
        nodes.append(GeometryNode(
            id="APEX", label="Unified Field Apex",
            x=0.0, y=0.0, z=0.0,
            radius=self.NODE_CIRCLE_RADIUS * 1.5,
            axis_id="APEX",
            color=self.AXIS_COLORS["APEX"],
            symbol=self.AXIS_SYMBOLS["APEX"],
        ))

        # Inner ring: AX-01 to AX-06 (6 nodes, radius=1.0, in hexagonal arrangement)
        for i, ax in enumerate(["AX-01", "AX-02", "AX-03", "AX-04", "AX-05", "AX-06"]):
            angle = math.radians(i * 60)  # 60° spacing
            x = self.INNER_RING_RADIUS * math.cos(angle)
            y = self.INNER_RING_RADIUS * math.sin(angle)
            z = 0.5  # slight depth offset for inner ring
            nodes.append(GeometryNode(
                id=ax, label=self.AXIS_LABELS[ax],
                x=round(x, 6), y=round(y, 6), z=round(z, 6),
                radius=self.NODE_CIRCLE_RADIUS,
                axis_id=ax,
                color=self.AXIS_COLORS[ax],
                symbol=self.AXIS_SYMBOLS[ax],
            ))

        # Outer ring: AX-07 to AX-12 (6 nodes, radius=2.0, offset 30° from inner)
        for i, ax in enumerate(["AX-07", "AX-08", "AX-09", "AX-10", "AX-11", "AX-12"]):
            angle = math.radians(i * 60 + 30)  # 30° offset from inner ring
            x = self.OUTER_RING_RADIUS * math.cos(angle)
            y = self.OUTER_RING_RADIUS * math.sin(angle)
            z = 1.0  # outer ring deeper
            nodes.append(GeometryNode(
                id=ax, label=self.AXIS_LABELS[ax],
                x=round(x, 6), y=round(y, 6), z=round(z, 6),
                radius=self.NODE_CIRCLE_RADIUS,
                axis_id=ax,
                color=self.AXIS_COLORS[ax],
                symbol=self.AXIS_SYMBOLS[ax],
            ))

        return nodes

    def generate_edges(
        self, nodes: list[GeometryNode]
    ) -> list[GeometryEdge]:
        """Generate all 78 Metatron edges (complete graph on 13 nodes)."""
        edges: list[GeometryEdge] = []
        node_map = {n.id: n for n in nodes}

        node_ids = [n.id for n in nodes]
        for i, src_id in enumerate(node_ids):
            for tgt_id in node_ids[i + 1:]:
                src = node_map[src_id]
                tgt = node_map[tgt_id]
                dist = math.sqrt((src.x - tgt.x) ** 2 + (src.y - tgt.y) ** 2)

                if src_id == "APEX" or tgt_id == "APEX":
                    edge_type = "spine"
                elif dist <= self.INNER_RING_RADIUS * 1.1:
                    edge_type = "outer"  # adjacent in same ring
                else:
                    edge_type = "cross"

                # Weight inversely proportional to distance
                weight = round(1.0 / (dist + 0.01), 4)

                edges.append(GeometryEdge(
                    source=src_id, target=tgt_id,
                    type=edge_type, weight=weight,
                ))

        return edges

    def export_json(self) -> dict[str, Any]:
        """Export full geometry as a JSON-serializable dict."""
        nodes = self.generate_nodes()
        edges = self.generate_edges(nodes)
        return {
            "schema_version": "0.1",
            "status": "Candidate",
            "date": "2026-05-29",
            "geometry": "Metatron's Cube — 12-Axis Lattice",
            "total_nodes": len(nodes),
            "total_edges": len(edges),
            "inner_ring_radius": self.INNER_RING_RADIUS,
            "outer_ring_radius": self.OUTER_RING_RADIUS,
            "nodes": [asdict(n) for n in nodes],
            "edges": [asdict(e) for e in edges],
        }

    def write(self, output_dir: Path) -> None:
        output_dir.mkdir(parents=True, exist_ok=True)
        data = self.export_json()
        path = output_dir / "METATRON_CUBE_GEOMETRY.json"
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"✅  Metatron geometry written: {len(data['nodes'])} nodes, "
              f"{len(data['edges'])} edges → {path.name}")


def main() -> None:
    geo = MetatronGeometry()
    nodes = geo.generate_nodes()
    edges = geo.generate_edges(nodes)
    print(f"=== Metatron's Cube Geometry ===")
    print(f"  Nodes: {len(nodes)}")
    print(f"  Edges: {len(edges)}")
    for n in nodes:
        print(f"  {n.id:<10} ({n.x:>7.4f}, {n.y:>7.4f}, {n.z:>5.2f})  {n.symbol}  {n.label}")
    geo.write(DATA_DIR)


if __name__ == "__main__":
    main()
