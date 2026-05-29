"""
lattice_query_engine.py — T69: Hypercube Traversal Query Engine
Rainbow Yin Yang Lattice — 12×12×12 Hypercube Data Fabric

Provides a structured query interface for navigating the 1728-node
hypercube. Implements the KG_SEARCH_QUERY_SPEC traversal patterns.

Status: Candidate
Date: 2026-05-29
Author: TIDELOCKBrain / @atlaslattice
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

from lattice_coordinate_mapper import CoordinateMapper, LatticeCoordinate  # noqa: E402
from lattice_cross_axis_bridge import CrossAxisBridge                      # noqa: E402


@dataclass
class QueryResult:
    """Single query result entry."""
    node_id: str
    coordinate: LatticeCoordinate
    score: float
    match_reason: str


class LatticeQueryEngine:
    """
    Hypercube traversal and query engine.

    Supported query types:
    - by_address(i, j, k): exact 3D address lookup
    - neighbors(i, j, k, radius): Manhattan-distance neighbors
    - by_axis_value(axis_id, value): all nodes with axis = value
    - by_coupling_strength(axis_a, axis_b, min_strength): high-coupling nodes
    - riemann_spine(): all 12 Riemann operator spine nodes
    - metatron_anchors(): 13 Metatron's Cube anchor nodes
    - path(start, end): shortest path between two addresses
    """

    def __init__(self) -> None:
        self._mapper = CoordinateMapper()
        self._bridge = CrossAxisBridge()

    # -----------------------------------------------------------------------
    # Core query methods
    # -----------------------------------------------------------------------

    def by_address(self, i: int, j: int, k: int) -> Optional[QueryResult]:
        """Exact 3D address lookup."""
        try:
            coord = self._mapper.map(i, j, k)
        except ValueError:
            return None
        return QueryResult(
            node_id=f"N-{i:02d}.{j:02d}.{k:02d}",
            coordinate=coord,
            score=1.0,
            match_reason="exact_address",
        )

    def neighbors(
        self,
        i: int,
        j: int,
        k: int,
        radius: int = 1,
    ) -> list[QueryResult]:
        """Return all nodes within Manhattan distance `radius` of (i, j, k)."""
        results: list[QueryResult] = []
        for di in range(-radius, radius + 1):
            for dj in range(-radius, radius + 1):
                for dk in range(-radius, radius + 1):
                    ni, nj, nk = i + di, j + dj, k + dk
                    if (ni, nj, nk) == (i, j, k):
                        continue
                    if not all(0 <= v <= 11 for v in (ni, nj, nk)):
                        continue
                    dist = abs(di) + abs(dj) + abs(dk)
                    if dist > radius:
                        continue
                    coord = self._mapper.map(ni, nj, nk)
                    results.append(QueryResult(
                        node_id=f"N-{ni:02d}.{nj:02d}.{nk:02d}",
                        coordinate=coord,
                        score=1.0 / dist,
                        match_reason=f"manhattan_dist={dist}",
                    ))
        return sorted(results, key=lambda r: r.score, reverse=True)

    def by_axis_value(self, axis_id: str, value: int) -> list[QueryResult]:
        """
        Return representative nodes where the given axis index equals value.
        Samples the (value, *, *) plane of the primary coordinate space
        for AX-01, AX-02, AX-03; derived axes use property lookup.
        """
        results: list[QueryResult] = []
        axis_to_primary = {"AX-01": 0, "AX-02": 1, "AX-03": 2}

        if axis_id in axis_to_primary:
            pos = axis_to_primary[axis_id]
            # Scan all positions in the other 2 primary axes at step 5
            for a in range(0, 12, 5):
                for b in range(0, 12, 5):
                    coords_list = [a, a, a]
                    coords_list[pos] = value
                    i, j, k = coords_list[0], coords_list[1], coords_list[2]
                    coord = self._mapper.map(i, j, k)
                    results.append(QueryResult(
                        node_id=f"N-{i:02d}.{j:02d}.{k:02d}",
                        coordinate=coord,
                        score=1.0,
                        match_reason=f"{axis_id}={value}",
                    ))
        else:
            # For derived axes, scan Riemann spine + corners
            for i in range(0, 12, 5):
                for j in range(0, 12, 5):
                    for k in range(0, 12, 5):
                        coord = self._mapper.map(i, j, k)
                        coord_dict = coord.to_dict()
                        axis_field = axis_id.lower().replace("-", "") + "_"
                        # Find the field
                        field_map = {
                            "AX-04": "ax04_spin",
                            "AX-05": "ax05_acoustic",
                            "AX-06": "ax06_color",
                            "AX-07": "ax07_neuromorphic",
                            "AX-08": "ax08_yin_yang",
                            "AX-09": "ax09_riemann",
                            "AX-10": "ax10_temporal",
                            "AX-11": "ax11_topology",
                            "AX-12": "ax12_information",
                        }
                        field = field_map.get(axis_id)
                        if field and coord_dict.get(field) == value:
                            results.append(QueryResult(
                                node_id=f"N-{i:02d}.{j:02d}.{k:02d}",
                                coordinate=coord,
                                score=1.0,
                                match_reason=f"{axis_id}={value} (derived)",
                            ))
        return results

    def riemann_spine(self) -> list[QueryResult]:
        """Return the 12 Riemann operator spine nodes."""
        results = []
        for r in range(12):
            coord = self._mapper.map(5, 5, r)
            results.append(QueryResult(
                node_id=f"N-RIEMANN-{r:02d}",
                coordinate=coord,
                score=1.0,
                match_reason=f"riemann_spine AX-09={r}",
            ))
        return results

    def metatron_anchors(self) -> list[QueryResult]:
        """Return the 13 Metatron's Cube anchor nodes."""
        addresses = [
            (5, 5, 5),   # centre
            (0, 5, 5), (11, 5, 5), (5, 0, 5), (5, 11, 5),
            (5, 5, 0), (5, 5, 11), (0, 0, 5), (11, 11, 5),
            (0, 11, 5), (11, 0, 5), (5, 0, 11), (5, 11, 0),
        ]
        labels = ["centre"] + [f"outer_{i+1}" for i in range(12)]
        results = []
        for (i, j, k), label in zip(addresses, labels):
            coord = self._mapper.map(i, j, k)
            results.append(QueryResult(
                node_id=f"N-METATRON-{label}",
                coordinate=coord,
                score=1.0,
                match_reason=f"metatron_anchor={label}",
            ))
        return results

    def path(
        self,
        start: tuple[int, int, int],
        end: tuple[int, int, int],
    ) -> list[QueryResult]:
        """
        Shortest path between two 3D addresses using Manhattan distance.
        Returns intermediate waypoints.
        """
        si, sj, sk = start
        ei, ej, ek = end
        path_nodes: list[QueryResult] = []

        i, j, k = si, sj, sk
        while (i, j, k) != (ei, ej, ek):
            coord = self._mapper.map(i, j, k)
            path_nodes.append(QueryResult(
                node_id=f"N-{i:02d}.{j:02d}.{k:02d}",
                coordinate=coord,
                score=1.0,
                match_reason="path_waypoint",
            ))
            # Greedy step toward target
            if i != ei:
                i += 1 if ei > i else -1
            elif j != ej:
                j += 1 if ej > j else -1
            elif k != ek:
                k += 1 if ek > k else -1

        # Add end node
        coord = self._mapper.map(ei, ej, ek)
        path_nodes.append(QueryResult(
            node_id=f"N-{ei:02d}.{ej:02d}.{ek:02d}",
            coordinate=coord,
            score=1.0,
            match_reason="path_end",
        ))
        return path_nodes

    def by_coupling_strength(
        self,
        axis_a: str,
        axis_b: str,
        min_strength: float = 0.7,
    ) -> list[QueryResult]:
        """
        Return nodes relevant to a high-coupling axis pair.
        Scans the Riemann spine and corners for nodes where the
        coupling pair's combined axis indices are maximized.
        """
        result = self._bridge.coupling(axis_a, axis_b)
        if result.strength < min_strength:
            return []

        # Return spine + corners as relevant nodes for strongly coupled axes
        spine = self.riemann_spine()
        for qr in spine:
            qr.match_reason = (
                f"coupling {axis_a}↔{axis_b}={result.strength:.3f}"
            )
        return spine


def main() -> None:
    engine = LatticeQueryEngine()

    print("=== by_address(3, 7, 2) ===")
    r = engine.by_address(3, 7, 2)
    if r:
        print(f"  {r.node_id}  spin={r.coordinate.ax04_spin}  "
              f"color={r.coordinate.ax06_color}  riemann={r.coordinate.ax09_riemann}")

    print("\n=== neighbors(5, 5, 5, radius=1) ===")
    neighbors = engine.neighbors(5, 5, 5, radius=1)
    print(f"  Found {len(neighbors)} neighbors")
    for n in neighbors[:4]:
        print(f"  {n.node_id}  score={n.score:.3f}  ({n.match_reason})")

    print("\n=== riemann_spine() ===")
    spine = engine.riemann_spine()
    print(f"  {len(spine)} nodes on Riemann spine")

    print("\n=== metatron_anchors() ===")
    anchors = engine.metatron_anchors()
    print(f"  {len(anchors)} Metatron anchor nodes")

    print("\n=== path((0,0,0) → (3,3,3)) ===")
    route = engine.path((0, 0, 0), (3, 3, 3))
    print(f"  Path length: {len(route)} steps")
    for step in route:
        print(f"  → {step.node_id}")


if __name__ == "__main__":
    main()
