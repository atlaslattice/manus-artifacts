"""
lattice_coordinate_mapper.py — T62: 3D→12D Coordinate Mapper
Rainbow Yin Yang Lattice — 12×12×12 Hypercube Data Fabric

Maps a primary 3-coordinate address (AX-01, AX-02, AX-03) to the
full 12-dimensional node property set using ontology coupling rules.

Status: Candidate
Date: 2026-05-29
Author: TIDELOCKBrain / @atlaslattice
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

import yaml

ONTOLOGY_DIR = (
    Path(__file__).resolve().parent.parent
    / "archive" / "spec" / "lattice-hypercube" / "ontology"
)


def _load(filename: str) -> dict:
    return yaml.safe_load((ONTOLOGY_DIR / filename).read_text(encoding="utf-8"))


@dataclass
class LatticeCoordinate:
    """Full 12D lattice coordinate for a single node."""
    # Primary address axes
    ax01_frequency: int       # AX-01: 0–11
    ax02_matter_state: int    # AX-02: 0–11
    ax03_element: int         # AX-03: 0–11
    # Derived / property axes
    ax04_spin: int            # AX-04: 0–11
    ax05_acoustic: int        # AX-05: 0–11
    ax06_color: int           # AX-06: 0–11
    ax07_neuromorphic: int    # AX-07: 0–11
    ax08_yin_yang: int        # AX-08: 0–11  (5=balanced)
    ax09_riemann: int         # AX-09: 0–11
    ax10_temporal: int        # AX-10: 0–11
    ax11_topology: int        # AX-11: 0–11
    ax12_information: int     # AX-12: 0–11

    def as_address(self) -> str:
        return f"[{self.ax01_frequency:02d}.{self.ax02_matter_state:02d}.{self.ax03_element:02d}]"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class CoordinateMapper:
    """
    Maps primary 3D address (i, j, k) → full LatticeCoordinate using
    coupling rules from the ontology coupling matrix.

    Coupling rules applied:
    - AX-01 (freq)  ↔ AX-06 (color):    ax06 = ax01  (spectral match)
    - AX-04 (spin)  ↔ AX-05 (acoustic): ax05 = ax04  (spin-acoustic resonance)
    - AX-07 (neuro) ↔ AX-12 (info):     ax12 = ax07  (processing correlated)
    - AX-02 (phase) ↔ AX-10 (temporal): ax10 = ax02  (phase change rate)
    - AX-03 (elem)  ↔ AX-01 (freq):     ax04 = (ax01 + ax03) % 12  (spectral lines)
    - AX-08 (YY)    ↔ AX-09 (Riemann):  ax09 = ax08  (symmetry axis)
    - AX-11 topology derived from spatial embedding of (i+j+k) modular sum
    """

    def __init__(self) -> None:
        axes_data = _load("AXES_12_FORMAL_DEFINITIONS.yaml")
        self._axes = {a["id"]: a for a in axes_data["axes"]}
        self._coupling = axes_data.get("coupling_matrix", {})

    def map(self, i: int, j: int, k: int) -> LatticeCoordinate:
        """Map primary address (i=AX-01, j=AX-02, k=AX-03) to full 12D coordinate."""
        if not all(0 <= v <= 11 for v in (i, j, k)):
            raise ValueError(f"All coordinates must be in [0, 11]; got ({i}, {j}, {k})")

        ax01 = i
        ax02 = j
        ax03 = k

        # Coupling-derived axes
        ax06 = ax01                       # freq ↔ color
        ax04 = (ax01 + ax03) % 12         # element × freq → spin
        ax05 = ax04                       # spin ↔ acoustic
        ax10 = ax02                       # phase ↔ temporal
        ax07 = (ax02 + ax03) % 12         # neuromorphic from phase+element
        ax12 = ax07                       # info ↔ neuromorphic
        ax08 = 5 if (ax01 + ax02 + ax03) % 2 == 0 else 6  # yin-yang balance
        ax09 = ax08                       # Riemann ↔ yin-yang
        ax11 = (ax01 + ax02 + ax03) % 12  # topology from sum

        return LatticeCoordinate(
            ax01_frequency=ax01,
            ax02_matter_state=ax02,
            ax03_element=ax03,
            ax04_spin=ax04,
            ax05_acoustic=ax05,
            ax06_color=ax06,
            ax07_neuromorphic=ax07,
            ax08_yin_yang=ax08,
            ax09_riemann=ax09,
            ax10_temporal=ax10,
            ax11_topology=ax11,
            ax12_information=ax12,
        )

    def map_all_corners(self) -> list[LatticeCoordinate]:
        """Generate all 8 extreme corners of the primary cube face."""
        return [
            self.map(i, j, k)
            for i in (0, 11)
            for j in (0, 11)
            for k in (0, 11)
        ]

    def riemann_spine(self) -> list[LatticeCoordinate]:
        """Return the 12-node Riemann spine (AX-01=5, AX-02=5, AX-03=0..11)."""
        return [self.map(5, 5, r) for r in range(12)]


def main() -> None:
    mapper = CoordinateMapper()
    print("=== Coordinate Mapper — spot check ===")
    for i, j, k in [(0, 0, 0), (5, 5, 5), (11, 11, 11), (3, 7, 2)]:
        coord = mapper.map(i, j, k)
        print(f"  ({i},{j},{k}) → {coord.as_address()} "
              f"spin={coord.ax04_spin} color={coord.ax06_color} "
              f"riemann={coord.ax09_riemann}")
    spine = mapper.riemann_spine()
    print(f"\n=== Riemann spine ({len(spine)} nodes) ===")
    for c in spine:
        print(f"  {c.as_address()} AX-09={c.ax09_riemann}")


if __name__ == "__main__":
    main()
