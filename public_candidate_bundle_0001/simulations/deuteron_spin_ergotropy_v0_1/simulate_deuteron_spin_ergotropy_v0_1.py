#!/usr/bin/env python3
"""
Deuteron spin-1 ergotropy baseline v0.1

Conventional-physics baseline for Stars 2.0 / PT2.0 research.
This is not an energy-source claim and does not model fusion or nuclear reactions.

It computes the Zeeman Hamiltonian of a spin-1 deuteron in a static magnetic field,
the room-temperature thermal state, and the ergotropy (maximum work extractable
by ideal cyclic unitary control) of a few reference states.

Key boundary:
- thermal equilibrium is passive: ergotropy = 0
- coherent/inverted states can carry ergotropy, but preparing them requires work
- any claimed net-positive cycle must include preparation/reset and all parasitics
"""

from __future__ import annotations

import argparse
import json
import math
from typing import Dict

import numpy as np

H_PLANCK = 6.62607015e-34       # J s
K_B = 1.380649e-23             # J/K
N_A = 6.02214076e23            # 1/mol
GAMMA_D_HZ_PER_T = 6.53569e6   # deuteron gamma/(2π), Hz/T reference baseline


def zeeman_spacing_j(B_T: float) -> float:
    return H_PLANCK * GAMMA_D_HZ_PER_T * B_T


def spin1_hamiltonian(B_T: float) -> np.ndarray:
    """m=+1 ground, m=0 middle, m=-1 highest for positive gamma and B."""
    dE = zeeman_spacing_j(B_T)
    return np.diag([-dE, 0.0, dE]).astype(float)


def thermal_state(B_T: float, T_K: float) -> np.ndarray:
    H = spin1_hamiltonian(B_T)
    energies = np.diag(H)
    weights = np.exp(-energies / (K_B * T_K))
    return np.diag(weights / weights.sum()).astype(complex)


def ergotropy_j(rho: np.ndarray, H: np.ndarray) -> float:
    """Maximum ideal cyclic-unitary work: Tr(rho H) - Tr(rho_passive H)."""
    energy = float(np.real(np.trace(rho @ H)))
    populations = np.sort(np.linalg.eigvalsh(rho))[::-1]
    energies = np.sort(np.linalg.eigvalsh(H))
    passive_energy = float(np.dot(populations, energies))
    return max(0.0, energy - passive_energy)


def reference_states(B_T: float, T_K: float) -> Dict[str, np.ndarray]:
    psi_equal = np.ones(3, dtype=complex) / math.sqrt(3.0)
    return {
        "thermal": thermal_state(B_T, T_K),
        "ground_m_plus_1": np.diag([1.0, 0.0, 0.0]).astype(complex),
        "equal_coherent_superposition": np.outer(psi_equal, psi_equal.conj()),
        "fully_inverted_m_minus_1": np.diag([0.0, 0.0, 1.0]).astype(complex),
    }


def run(B_T: float, T_K: float, parasitic_j_per_mol: float, recovery_efficiency: float) -> dict:
    H = spin1_hamiltonian(B_T)
    dE = zeeman_spacing_j(B_T)

    rows = []
    for name, rho in reference_states(B_T, T_K).items():
        W_particle = ergotropy_j(rho, H)
        W_mol = W_particle * N_A
        recovered = recovery_efficiency * W_mol

        if recovered > 0:
            required_multiplier = parasitic_j_per_mol / recovered
        else:
            required_multiplier = math.inf if parasitic_j_per_mol > 0 else 0.0

        rows.append({
            "state": name,
            "ergotropy_J_per_particle": W_particle,
            "ergotropy_J_per_mol": W_mol,
            "ideal_recovered_J_per_mol": recovered,
            "parasitic_J_per_mol": parasitic_j_per_mol,
            "net_J_per_mol_conventional": recovered - parasitic_j_per_mol,
            "break_even_multiplier_on_recovered_work": required_multiplier,
        })

    return {
        "status": "CONVENTIONAL_BASELINE_NOT_ENERGY_SOURCE_CLAIM",
        "B_T": B_T,
        "T_K": T_K,
        "deuteron_Larmor_Hz": GAMMA_D_HZ_PER_T * B_T,
        "adjacent_Zeeman_spacing_J": dE,
        "dimensionless_spacing_dE_over_kT": dE / (K_B * T_K),
        "recovery_efficiency": recovery_efficiency,
        "notes": [
            "Thermal equilibrium is passive and has zero ergotropy.",
            "Superposition or inversion can store extractable work only if a non-equilibrium state is prepared.",
            "Preparation/reset work is not free and must be included in a closed energy ledger.",
            "A multiplier above 1 is a sensitivity parameter, not evidence for anomalous physics.",
        ],
        "states": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--B", type=float, default=1.0, help="Static magnetic field in tesla")
    parser.add_argument("--T", type=float, default=300.0, help="Temperature in kelvin")
    parser.add_argument("--parasitic", type=float, default=0.0, help="All non-spin process costs in J/mol")
    parser.add_argument("--eta", type=float, default=1.0, help="Idealized recovery efficiency, 0..1")
    args = parser.parse_args()

    if args.B < 0:
        raise SystemExit("B must be >= 0")
    if args.T <= 0:
        raise SystemExit("T must be > 0")
    if args.parasitic < 0:
        raise SystemExit("parasitic must be >= 0")
    if not (0 <= args.eta <= 1):
        raise SystemExit("eta must be between 0 and 1")

    print(json.dumps(run(args.B, args.T, args.parasitic, args.eta), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
