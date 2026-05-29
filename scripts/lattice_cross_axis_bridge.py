"""
lattice_cross_axis_bridge.py — T63: Cross-Axis Coupling Calculator
Rainbow Yin Yang Lattice — 12×12×12 Hypercube Data Fabric

Computes cross-axis coupling strengths between any two axis indices
using the ontology coupling matrix and Riemann S-operator phase model.

Status: Candidate
Date: 2026-05-29
Author: TIDELOCKBrain / @atlaslattice
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import NamedTuple

import yaml

ONTOLOGY_DIR = (
    Path(__file__).resolve().parent.parent
    / "archive" / "spec" / "lattice-hypercube" / "ontology"
)


def _load(filename: str) -> dict:
    return yaml.safe_load((ONTOLOGY_DIR / filename).read_text(encoding="utf-8"))


class CouplingResult(NamedTuple):
    axis_a: str
    axis_b: str
    coupling_type: str   # direct | indirect | spectral | nodal | ...
    strength: float      # 0.0–1.0 normalized coupling coefficient
    is_primary: bool


class CrossAxisBridge:
    """
    Computes coupling strengths between lattice axes.

    Coupling type weights (empirically derived from ontology):
      direct:           1.00
      self:             1.00
      spectral:         0.85
      spectral_phase:   0.80
      nodal:            0.75
      spectral_weight:  0.70
      topological:      0.65
      manifold_zeta:    0.60
      symmetry_axis:    0.90
      spectral_entropy: 0.60
      indirect:         0.40
      prime_gaps:       0.50
      harmonic:         0.80 (universal Riemann coupling to all axes)
    """

    _TYPE_WEIGHTS: dict[str, float] = {
        "direct": 1.00,
        "self": 1.00,
        "symmetry_axis": 0.90,
        "spectral": 0.85,
        "harmonic": 0.80,
        "spectral_phase": 0.80,
        "nodal": 0.75,
        "spectral_weight": 0.70,
        "topological": 0.65,
        "manifold_zeta": 0.60,
        "spectral_entropy": 0.60,
        "prime_gaps": 0.50,
        "indirect": 0.40,
    }

    def __init__(self) -> None:
        axes_data = _load("AXES_12_FORMAL_DEFINITIONS.yaml")
        self._axes = {a["id"]: a for a in axes_data["axes"]}
        coupling = axes_data.get("coupling_matrix", {})
        self._primary_pairs: set[frozenset[str]] = {
            frozenset(pair) for pair in coupling.get("primary_couplings", [])
        }
        self._universal_operator: str = coupling.get("universal_operator", "AX-09")

    def coupling(self, axis_a: str, axis_b: str) -> CouplingResult:
        """Compute coupling between two axes."""
        if axis_a not in self._axes or axis_b not in self._axes:
            raise ValueError(f"Unknown axis id(s): {axis_a}, {axis_b}")

        if axis_a == axis_b:
            return CouplingResult(
                axis_a=axis_a, axis_b=axis_b,
                coupling_type="self", strength=1.0, is_primary=True,
            )

        # Riemann operator couples universally to all axes
        if self._universal_operator in (axis_a, axis_b):
            other = axis_b if axis_a == self._universal_operator else axis_a
            other_ax = self._axes[other]
            coupling_type = other_ax.get("riemann_coupling", "indirect")
            strength = self._TYPE_WEIGHTS.get(coupling_type, 0.5)
            return CouplingResult(
                axis_a=axis_a, axis_b=axis_b,
                coupling_type=coupling_type, strength=strength,
                is_primary=frozenset([axis_a, axis_b]) in self._primary_pairs,
            )

        pair = frozenset([axis_a, axis_b])
        is_primary = pair in self._primary_pairs

        if is_primary:
            # Determine coupling type from axis riemann_coupling annotations
            ax_a = self._axes[axis_a]
            ax_b = self._axes[axis_b]
            coupling_type = ax_a.get("riemann_coupling", "harmonic")
            strength = self._TYPE_WEIGHTS.get(coupling_type, 0.7) * 1.0
        else:
            # Non-primary pairs get indirect coupling via Riemann mediation
            ax_a = self._axes[axis_a]
            coupling_type = "indirect"
            strength = self._TYPE_WEIGHTS["indirect"]

        return CouplingResult(
            axis_a=axis_a, axis_b=axis_b,
            coupling_type=coupling_type, strength=round(strength, 4),
            is_primary=is_primary,
        )

    def full_coupling_matrix(self) -> list[list[float]]:
        """Return 12×12 coupling strength matrix."""
        axis_ids = [f"AX-{i:02d}" for i in range(1, 13)]
        matrix: list[list[float]] = []
        for a in axis_ids:
            row = []
            for b in axis_ids:
                result = self.coupling(a, b)
                row.append(result.strength)
            matrix.append(row)
        return matrix

    def primary_pairs_summary(self) -> list[CouplingResult]:
        """Return all primary coupling pairs."""
        results = []
        for pair in self._primary_pairs:
            axes = sorted(pair)
            results.append(self.coupling(axes[0], axes[1]))
        return sorted(results, key=lambda r: r.strength, reverse=True)

    def spectral_entropy(self, axis_id: str) -> float:
        """
        Compute the spectral entropy of an axis based on its coupling
        strengths to all other axes.  H = -Σ p_i * log2(p_i)
        """
        axis_ids = [f"AX-{i:02d}" for i in range(1, 13)]
        strengths = [
            self.coupling(axis_id, other).strength
            for other in axis_ids
            if other != axis_id
        ]
        total = sum(strengths)
        if total == 0:
            return 0.0
        probs = [s / total for s in strengths]
        return -sum(p * math.log2(p) for p in probs if p > 0)


def main() -> None:
    bridge = CrossAxisBridge()
    print("=== Primary coupling pairs ===")
    for result in bridge.primary_pairs_summary():
        marker = "★" if result.is_primary else "·"
        print(f"  {marker} {result.axis_a}↔{result.axis_b}  "
              f"type={result.coupling_type:<18} strength={result.strength:.4f}")

    print("\n=== Riemann operator (AX-09) coupling to all axes ===")
    for i in range(1, 13):
        other = f"AX-{i:02d}"
        if other == "AX-09":
            continue
        r = bridge.coupling("AX-09", other)
        print(f"  AX-09↔{other}  {r.coupling_type:<20} {r.strength:.4f}")

    print("\n=== Spectral entropy per axis ===")
    for i in range(1, 13):
        ax = f"AX-{i:02d}"
        h = bridge.spectral_entropy(ax)
        print(f"  {ax}  H={h:.4f} bits")


if __name__ == "__main__":
    main()
