#!/usr/bin/env python3
"""Ionic Energy State Engine v0.1.

Conventional thermodynamic scaffold + Alexandrian resource/ecology screen.
Not an energy-source claim. No nuclear reactions are modeled.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any, Dict, Iterable, Tuple

R = 8.31446261815324
F = 96485.33212

SCALE = {
    "VERY_LOW": 0.05,
    "LOW": 0.20,
    "MEDIUM": 0.50,
    "HIGH": 0.80,
    "VERY_HIGH": 1.00,
    "UNKNOWN": None,
}

DEFAULT_WEIGHTS = {
    "resource_abundance": 0.15,
    "circularity": 0.15,
    "renewable_gradient_access": 0.20,
    "extraction_burden": 0.15,
    "ecological_burden": 0.20,
    "infrastructure_compatibility": 0.10,
    "technology_maturity": 0.05,
}

LOW_IS_GOOD = {"extraction_burden", "ecological_burden"}


def electrochemical_delta_mu_j_per_mol(
    *,
    z: float,
    activity_initial: float,
    activity_final: float,
    phi_initial_V: float,
    phi_final_V: float,
    T_K: float = 298.15,
) -> float:
    """Final-minus-initial ideal electrochemical potential, J/mol."""
    if T_K <= 0:
        raise ValueError("T_K must be > 0")
    if activity_initial <= 0 or activity_final <= 0:
        raise ValueError("activities must be > 0")
    return (
        R * T_K * math.log(activity_final / activity_initial)
        + z * F * (phi_final_V - phi_initial_V)
    )


def reversible_work_ceiling_j_per_mol(delta_mu_j_per_mol: float) -> float:
    """Maximum ideal work for a downhill transition."""
    return max(0.0, -delta_mu_j_per_mol)


def net_process_energy_j_per_mol(
    reversible_ceiling_j_per_mol: float,
    recovery_efficiency: float,
    process_costs_j_per_mol: Iterable[float],
) -> Dict[str, float]:
    if not 0.0 <= recovery_efficiency <= 1.0:
        raise ValueError("recovery_efficiency must be within [0, 1]")
    costs = [float(x) for x in process_costs_j_per_mol]
    if any(x < 0 for x in costs):
        raise ValueError("process costs must be >= 0")
    gross = reversible_ceiling_j_per_mol * recovery_efficiency
    total_cost = sum(costs)
    return {
        "reversible_ceiling_J_per_mol": reversible_ceiling_j_per_mol,
        "recovery_efficiency": recovery_efficiency,
        "gross_recovered_J_per_mol": gross,
        "process_cost_J_per_mol": total_cost,
        "net_J_per_mol": gross - total_cost,
    }


def _score_value(field: str, label: str) -> float | None:
    value = SCALE[label]
    if value is None:
        return None
    return 1.0 - value if field in LOW_IS_GOOD else value


def sustainability_screen(
    prior: Dict[str, str],
    weights: Dict[str, float] | None = None,
) -> Tuple[float | None, float]:
    """Return heuristic score + coverage. This is not an energy-performance score."""
    weights = dict(DEFAULT_WEIGHTS if weights is None else weights)
    total_weight = sum(weights.values())
    used_weight = 0.0
    weighted_sum = 0.0

    for field, weight in weights.items():
        label = prior.get(field, "UNKNOWN")
        if label not in SCALE:
            raise ValueError(f"Unknown scale label for {field}: {label}")
        value = _score_value(field, label)
        if value is None:
            continue
        weighted_sum += weight * value
        used_weight += weight

    coverage = used_weight / total_weight if total_weight else 0.0
    score = weighted_sum / used_weight if used_weight else None
    return score, coverage


def rank_candidates(data: Dict[str, Any]) -> list[Dict[str, Any]]:
    rows = []
    for candidate in data["candidates"]:
        score, coverage = sustainability_screen(candidate["screening_prior"])
        rows.append({
            "candidate_id": candidate["candidate_id"],
            "conversion_status": candidate["conversion_status"],
            "screening_score": score,
            "score_coverage": coverage,
            "warning": "Research-priority heuristic only; not energy efficiency or net power.",
        })
    rows.sort(
        key=lambda row: (
            row["screening_score"] is not None,
            row["screening_score"] if row["screening_score"] is not None else -1,
        ),
        reverse=True,
    )
    return rows


def feed_volume_m3_per_mol(*, molar_mass_g_per_mol: float, feedstock_g_per_m3: float) -> float:
    """Ideal raw-feed volume containing one mole before recovery/separation losses."""
    if molar_mass_g_per_mol <= 0 or feedstock_g_per_m3 <= 0:
        raise ValueError("molar mass and feedstock concentration must be > 0")
    return molar_mass_g_per_mol / feedstock_g_per_m3


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--registry",
        default=str(Path(__file__).with_name("candidate_pathways_v0_1.json")),
    )
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("rank")

    p_mu = sub.add_parser("delta-mu")
    p_mu.add_argument("--z", type=float, required=True)
    p_mu.add_argument("--a1", type=float, required=True)
    p_mu.add_argument("--a2", type=float, required=True)
    p_mu.add_argument("--phi1", type=float, default=0.0)
    p_mu.add_argument("--phi2", type=float, default=0.0)
    p_mu.add_argument("--T", type=float, default=298.15)
    p_mu.add_argument("--eta", type=float, default=1.0)
    p_mu.add_argument("--cost", type=float, action="append", default=[])

    p_feed = sub.add_parser("feed-volume")
    p_feed.add_argument("--molar-mass", type=float, required=True)
    p_feed.add_argument("--g-per-m3", type=float, required=True)

    args = parser.parse_args()

    if args.command == "rank":
        data = json.loads(Path(args.registry).read_text())
        print(json.dumps(rank_candidates(data), indent=2))
        return 0

    if args.command == "delta-mu":
        delta = electrochemical_delta_mu_j_per_mol(
            z=args.z,
            activity_initial=args.a1,
            activity_final=args.a2,
            phi_initial_V=args.phi1,
            phi_final_V=args.phi2,
            T_K=args.T,
        )
        ceiling = reversible_work_ceiling_j_per_mol(delta)
        result = {
            "delta_mu_final_minus_initial_J_per_mol": delta,
            **net_process_energy_j_per_mol(ceiling, args.eta, args.cost),
            "boundary_note": (
                "Ideal activity model. Real electrolytes require activity coefficients, "
                "coupled-ion electroneutrality, membrane/device losses, and a declared reset path."
            ),
        }
        print(json.dumps(result, indent=2))
        return 0

    if args.command == "feed-volume":
        print(json.dumps({
            "ideal_feed_volume_m3_per_mol": feed_volume_m3_per_mol(
                molar_mass_g_per_mol=args.molar_mass,
                feedstock_g_per_m3=args.g_per_m3,
            ),
            "boundary_note": (
                "Raw-feed inventory only. Does not include recovery fraction, selectivity, "
                "separation energy, pretreatment, or ecological throughput."
            ),
        }, indent=2))
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
