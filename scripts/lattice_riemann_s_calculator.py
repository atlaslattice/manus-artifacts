"""
lattice_riemann_s_calculator.py — T65: Riemann S-Operator Numerical Model
Rainbow Yin Yang Lattice — 12×12×12 Hypercube Data Fabric

Numerical approximation of the Riemann zeta function ζ(s) evaluated
at the 12 lattice sample points along the critical strip.
Used as the universal cross-domain transform coupling all 12 axes.

Status: Candidate
Date: 2026-05-29
Author: TIDELOCKBrain / @atlaslattice
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

ONTOLOGY_DIR = (
    Path(__file__).resolve().parent.parent
    / "archive" / "spec" / "lattice-hypercube" / "ontology"
)


def _load(filename: str) -> dict:
    return yaml.safe_load((ONTOLOGY_DIR / filename).read_text(encoding="utf-8"))


def riemann_zeta_approx(s: complex, terms: int = 200) -> complex:
    """
    Approximate ζ(s) via the Euler-Maclaurin partial sum for Re(s) > 1,
    and via analytic continuation for 0 < Re(s) < 1.

    This is a finite-precision approximation suitable for lattice use.
    For the critical strip we use the alternating series (η function):
      η(s) = Σ (-1)^(n-1) / n^s   (converges for Re(s) > 0)
      ζ(s) = η(s) / (1 - 2^(1-s))
    """
    sigma = s.real
    if sigma > 1:
        # Direct Dirichlet series
        result = sum(1.0 / (n ** s) for n in range(1, terms + 1))
        return result
    else:
        # Alternating Dirichlet eta function
        eta = sum(
            ((-1) ** (n - 1)) * (1.0 / (n ** s))
            for n in range(1, terms + 1)
        )
        denom = 1.0 - (2.0 ** (1.0 - s))
        if abs(denom) < 1e-15:
            return complex(float("nan"))
        return eta / denom


@dataclass
class RiemannSample:
    """One sample point on the Riemann S-operator axis."""
    index: int           # AX-09 index 0–11
    s_real: float        # Re(s) sample
    s_imag: float        # Im(s) sample (t component)
    zeta_real: float     # Re(ζ(s))
    zeta_imag: float     # Im(ζ(s))
    zeta_abs: float      # |ζ(s)|
    zeta_phase: float    # arg(ζ(s)) in radians
    coupling_weight: float  # normalized coupling weight 0–1
    description: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "index": self.index,
            "s": {"real": self.s_real, "imag": self.s_imag},
            "zeta": {
                "real": round(self.zeta_real, 6),
                "imag": round(self.zeta_imag, 6),
                "abs": round(self.zeta_abs, 6),
                "phase_rad": round(self.zeta_phase, 6),
            },
            "coupling_weight": round(self.coupling_weight, 6),
            "description": self.description,
        }


class RiemannSOperator:
    """
    The Riemann S-operator: 12 sample points along the critical strip.

    Sampling strategy:
    - s = 0.5 + i*t  (on the critical line Re(s) = 0.5)
    - t values chosen to cover first 12 non-trivial zero neighborhoods
    - Known zero locations (Im part): 14.135, 21.022, 25.011, 30.425,
      32.935, 37.586, 40.919, 43.327, 48.005, 49.774, 52.970, 56.446
    """

    KNOWN_ZERO_IMAGINARY_PARTS = [
        14.1347, 21.0220, 25.0109, 30.4249, 32.9351,
        37.5862, 40.9187, 43.3271, 48.0052, 49.7738,
        52.9703, 56.4462,
    ]

    DESCRIPTIONS = [
        "First non-trivial zero neighborhood — primordial resonance",
        "Second zero — harmonic second",
        "Third zero — ternary node",
        "Fourth zero — quaternary stability",
        "Fifth zero — pentatonic bridge",
        "Sixth zero — hexagonal symmetry",
        "Seventh zero — heptagonal resonance",
        "Eighth zero — octave anchor",
        "Ninth zero — ennead field",
        "Tenth zero — decad completion",
        "Eleventh zero — undecimal bridge",
        "Twelfth zero — duodecimal closure / full lattice span",
    ]

    def __init__(self) -> None:
        riemann_data = _load("RIEMANN_S_OPERATOR.yaml")
        self._spec = riemann_data

    def compute_samples(self) -> list[RiemannSample]:
        """Compute all 12 S-operator sample points."""
        samples: list[RiemannSample] = []
        sigma = 0.5  # Critical line

        for idx, t in enumerate(self.KNOWN_ZERO_IMAGINARY_PARTS):
            s = complex(sigma, t)
            zeta = riemann_zeta_approx(s, terms=300)
            z_abs = abs(zeta)
            z_phase = cmath.phase(zeta)

            # Normalize coupling weight by proximity to zero (inverse of |ζ|)
            # Near zeros → higher coupling weight
            epsilon = 1e-6
            coupling_weight = 1.0 / (z_abs + epsilon)
            # Clamp to [0, 1] after normalization across all 12 samples
            samples.append(RiemannSample(
                index=idx,
                s_real=sigma,
                s_imag=t,
                zeta_real=zeta.real,
                zeta_imag=zeta.imag,
                zeta_abs=z_abs,
                zeta_phase=z_phase,
                coupling_weight=coupling_weight,  # normalized below
                description=self.DESCRIPTIONS[idx],
            ))

        # Normalize coupling weights to [0, 1]
        max_w = max(s.coupling_weight for s in samples)
        for s in samples:
            s.coupling_weight = round(s.coupling_weight / max_w, 6)

        return samples

    def apply_to_axis_pair(
        self,
        axis_a_value: int,
        axis_b_value: int,
        riemann_index: int,
    ) -> float:
        """
        Apply the S-operator to transform a coupling strength between
        two axis values, modulated by the Riemann sample at riemann_index.

        Returns a normalized coupling coefficient in [0, 1].
        """
        if not (0 <= riemann_index <= 11):
            raise ValueError(f"riemann_index must be in [0, 11]; got {riemann_index}")
        samples = self.compute_samples()
        sample = samples[riemann_index]
        # Phase modulation: cosine of zeta phase × harmonic of axis values
        phase_mod = math.cos(
            sample.zeta_phase + math.pi * (axis_a_value + axis_b_value) / 12
        )
        coupling = sample.coupling_weight * abs(phase_mod)
        return round(min(1.0, max(0.0, coupling)), 6)


def main() -> None:
    op = RiemannSOperator()
    samples = op.compute_samples()
    print("=== Riemann S-Operator: 12 Critical Line Samples ===")
    print(f"  {'Idx':>3}  {'t':>8}  {'|ζ(s)|':>12}  {'phase(rad)':>12}  {'w':>8}")
    for s in samples:
        print(f"  {s.index:>3}  {s.s_imag:>8.3f}  {s.zeta_abs:>12.6f}  "
              f"{s.zeta_phase:>12.6f}  {s.coupling_weight:>8.6f}")

    print("\n=== S-Operator coupling (AX-01[3], AX-06[3]) across all 12 Riemann indices ===")
    for r in range(12):
        c = op.apply_to_axis_pair(3, 3, r)
        print(f"  Riemann[{r:02d}] coupling={c:.6f}")


if __name__ == "__main__":
    main()
