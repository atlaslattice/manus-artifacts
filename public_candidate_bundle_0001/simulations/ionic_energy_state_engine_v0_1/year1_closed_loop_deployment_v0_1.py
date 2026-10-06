#!/usr/bin/env python3
"""Year-1 closed-loop deployment simulator v0.1.

Economic/material-burn companion to Ionic Energy State Engine v0.1.

This model does NOT create an energy source. It compares:
1) a closed-loop working-medium inventory with fractional loss/makeup, and
2) an open-loop material-use comparator that refreshes the full inventory every cycle.

The open-loop comparator isolates the economic value of reuse. It is not a universal
baseline for every electrochemical technology.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any, Dict

SECONDS_PER_YEAR = 365.0 * 24.0 * 3600.0
J_PER_KWH = 3.6e6


def _require_nonnegative(name: str, value: float) -> None:
    if value < 0:
        raise ValueError(f"{name} must be >= 0")


def _require_fraction(name: str, value: float) -> None:
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must be within [0, 1]")


def retention_for_inventory_turnovers(cycles: int, turnovers: float) -> float:
    """Retention needed so gross makeup <= turnovers full inventories over N cycles."""
    if cycles <= 0:
        raise ValueError("cycles must be > 0")
    if turnovers < 0:
        raise ValueError("turnovers must be >= 0")
    return max(0.0, 1.0 - turnovers / cycles)


def _checkpoint(
    *,
    n: int,
    annual_cycles_per_node: int,
    nodes: int,
    inventory_mol_per_node: float,
    loss_mol_per_cycle_per_node: float,
    fresh_fill_cost_usd_per_mol: float,
    makeup_cost_usd_per_mol: float,
    capex_usd_per_node: float,
    fixed_opex_usd_per_node_year: float,
    variable_opex_usd_per_cycle_node: float,
    process_energy_cost_usd_per_cycle_node: float,
    replacement_interval_cycles: int | None,
    replacement_cost_usd_per_node: float,
) -> Dict[str, float | int]:
    if n <= 0:
        raise ValueError("checkpoint cycle must be > 0")
    n = min(n, annual_cycles_per_node)

    startup = nodes * (
        capex_usd_per_node
        + inventory_mol_per_node * fresh_fill_cost_usd_per_mol
    )
    fixed_per_cycle_network = (
        nodes * fixed_opex_usd_per_node_year / annual_cycles_per_node
        if annual_cycles_per_node
        else 0.0
    )
    recurring_per_cycle_network = nodes * (
        variable_opex_usd_per_cycle_node
        + loss_mol_per_cycle_per_node * makeup_cost_usd_per_mol
        + process_energy_cost_usd_per_cycle_node
    ) + fixed_per_cycle_network

    replacements = (
        n // replacement_interval_cycles
        if replacement_interval_cycles and replacement_interval_cycles > 0
        else 0
    )
    replacement_total = replacements * replacement_cost_usd_per_node * nodes
    cumulative = startup + n * recurring_per_cycle_network + replacement_total

    marginal = recurring_per_cycle_network
    if n == 1:
        marginal += startup
    if (
        replacement_interval_cycles
        and replacement_interval_cycles > 0
        and n % replacement_interval_cycles == 0
    ):
        marginal += replacement_cost_usd_per_node * nodes

    return {
        "cycle": n,
        "cumulative_cost_usd": cumulative,
        "average_cost_usd_per_cycle_network": cumulative / n,
        "marginal_cost_of_this_cycle_usd_network": marginal,
        "scheduled_replacements_completed": replacements,
    }


def simulate_year(scenario: Dict[str, Any]) -> Dict[str, Any]:
    dep = scenario["deployment"]
    loop = scenario["closed_loop"]
    econ = scenario["economics"]
    energy = scenario["energy"]
    baseline = scenario["baseline"]

    horizon_days = float(dep.get("horizon_days", 365.0))
    nodes = int(dep.get("nodes", 1))
    scheduled_cycles = int(dep["scheduled_cycles_per_year_per_node"])
    uptime = float(dep.get("uptime_fraction", 1.0))
    inventory = float(dep["working_inventory_mol_per_node"])

    if horizon_days <= 0:
        raise ValueError("horizon_days must be > 0")
    if nodes <= 0:
        raise ValueError("nodes must be > 0")
    if scheduled_cycles <= 0:
        raise ValueError("scheduled_cycles_per_year_per_node must be > 0")
    _require_fraction("uptime_fraction", uptime)
    _require_nonnegative("working_inventory_mol_per_node", inventory)

    cycles = int(math.floor(scheduled_cycles * uptime))
    if cycles <= 0:
        raise ValueError("achieved cycles are zero")

    retention = float(loop["retention_fraction_per_cycle"])
    _require_fraction("retention_fraction_per_cycle", retention)

    fresh_fill_cost = float(loop["fresh_fill_cost_usd_per_mol"])
    makeup_cost = float(loop["makeup_cost_usd_per_mol"])
    disposal_lost = float(loop.get("disposal_cost_usd_per_mol_lost", 0.0))
    for name, val in [
        ("fresh_fill_cost_usd_per_mol", fresh_fill_cost),
        ("makeup_cost_usd_per_mol", makeup_cost),
        ("disposal_cost_usd_per_mol_lost", disposal_lost),
    ]:
        _require_nonnegative(name, val)

    loss_fraction = 1.0 - retention
    loss_mol_per_cycle_per_node = inventory * loss_fraction
    total_makeup_mol = loss_mol_per_cycle_per_node * cycles * nodes
    first_fill_mol = inventory * nodes
    inventory_turnovers_per_node_year = (
        loss_mol_per_cycle_per_node * cycles / inventory if inventory > 0 else 0.0
    )

    capex_per_node = float(econ.get("capex_usd_per_node", 0.0))
    fixed_opex_per_node_year = float(econ.get("fixed_opex_usd_per_node_year", 0.0))
    variable_opex_per_cycle_node = float(econ.get("variable_opex_usd_per_cycle_node", 0.0))
    replacement_cost_per_node = float(econ.get("component_replacement_cost_usd_per_node", 0.0))
    replacement_interval_raw = econ.get("component_replacement_interval_cycles")
    replacement_interval = (
        int(replacement_interval_raw)
        if replacement_interval_raw not in (None, 0)
        else None
    )
    for name, val in [
        ("capex_usd_per_node", capex_per_node),
        ("fixed_opex_usd_per_node_year", fixed_opex_per_node_year),
        ("variable_opex_usd_per_cycle_node", variable_opex_per_cycle_node),
        ("component_replacement_cost_usd_per_node", replacement_cost_per_node),
    ]:
        _require_nonnegative(name, val)

    gross_j_per_mol_cycle = float(energy.get("gross_recovered_J_per_mol_cycle", 0.0))
    process_input_j_per_mol_cycle = float(energy.get("process_input_J_per_mol_cycle", 0.0))
    electricity_price = float(energy.get("electricity_cost_usd_per_kWh", 0.0))
    for name, val in [
        ("gross_recovered_J_per_mol_cycle", gross_j_per_mol_cycle),
        ("process_input_J_per_mol_cycle", process_input_j_per_mol_cycle),
        ("electricity_cost_usd_per_kWh", electricity_price),
    ]:
        _require_nonnegative(name, val)

    gross_output_j = gross_j_per_mol_cycle * inventory * cycles * nodes
    process_input_j = process_input_j_per_mol_cycle * inventory * cycles * nodes
    net_energy_j = gross_output_j - process_input_j
    process_energy_cost = process_input_j / J_PER_KWH * electricity_price
    process_energy_cost_per_cycle_node = (
        process_input_j_per_mol_cycle * inventory / J_PER_KWH * electricity_price
    )

    replacement_count_per_node = (
        cycles // replacement_interval
        if replacement_interval and replacement_interval > 0
        else 0
    )
    replacement_cost = replacement_count_per_node * replacement_cost_per_node * nodes

    first_fill_cost = first_fill_mol * fresh_fill_cost
    makeup_cost_total = total_makeup_mol * makeup_cost
    lost_medium_disposal_cost = total_makeup_mol * disposal_lost
    capex = capex_per_node * nodes
    fixed_opex = fixed_opex_per_node_year * nodes * (horizon_days / 365.0)
    variable_opex = variable_opex_per_cycle_node * cycles * nodes

    closed_loop_total_cost = (
        capex
        + first_fill_cost
        + makeup_cost_total
        + lost_medium_disposal_cost
        + fixed_opex
        + variable_opex
        + replacement_cost
        + process_energy_cost
    )

    baseline_fresh_cost = float(baseline["fresh_material_cost_usd_per_mol"])
    baseline_disposal_cost = float(baseline.get("disposal_cost_usd_per_mol", 0.0))
    _require_nonnegative("baseline fresh material cost", baseline_fresh_cost)
    _require_nonnegative("baseline disposal cost", baseline_disposal_cost)

    open_loop_mol = inventory * cycles * nodes
    open_loop_material_cost = open_loop_mol * baseline_fresh_cost
    open_loop_disposal_cost = open_loop_mol * baseline_disposal_cost

    open_loop_total_cost = (
        capex
        + open_loop_material_cost
        + open_loop_disposal_cost
        + fixed_opex
        + variable_opex
        + replacement_cost
        + process_energy_cost
    )

    cost_savings = open_loop_total_cost - closed_loop_total_cost
    cost_savings_fraction = (
        cost_savings / open_loop_total_cost if open_loop_total_cost > 0 else None
    )

    medium = scenario.get("working_medium", {})
    molar_mass_g_per_mol = medium.get("molar_mass_g_per_mol")
    feedstock_g_per_m3 = medium.get("feedstock_concentration_g_per_m3")

    makeup_mass_kg = None
    raw_feed_m3_for_makeup = None
    if molar_mass_g_per_mol is not None:
        mm = float(molar_mass_g_per_mol)
        _require_nonnegative("molar_mass_g_per_mol", mm)
        makeup_mass_kg = total_makeup_mol * mm / 1000.0
        if feedstock_g_per_m3 not in (None, 0):
            c = float(feedstock_g_per_m3)
            if c <= 0:
                raise ValueError("feedstock_concentration_g_per_m3 must be > 0")
            raw_feed_m3_for_makeup = total_makeup_mol * mm / c

    host = scenario.get("host_infrastructure_reference", {})
    host_capacity_m3_day = host.get("capacity_m3_per_day")
    makeup_fraction_of_host_annual_flow = None
    if raw_feed_m3_for_makeup is not None and host_capacity_m3_day not in (None, 0):
        annual_host_flow = float(host_capacity_m3_day) * horizon_days
        if annual_host_flow > 0:
            makeup_fraction_of_host_annual_flow = raw_feed_m3_for_makeup / annual_host_flow

    checkpoint_cycles = scenario.get("checkpoint_cycles", [1, 100, 1000, cycles])
    checkpoints = []
    seen = set()
    for raw_n in checkpoint_cycles:
        n = min(max(1, int(raw_n)), cycles)
        if n in seen:
            continue
        seen.add(n)
        checkpoints.append(_checkpoint(
            n=n,
            annual_cycles_per_node=cycles,
            nodes=nodes,
            inventory_mol_per_node=inventory,
            loss_mol_per_cycle_per_node=loss_mol_per_cycle_per_node,
            fresh_fill_cost_usd_per_mol=fresh_fill_cost,
            makeup_cost_usd_per_mol=makeup_cost,
            capex_usd_per_node=capex_per_node,
            fixed_opex_usd_per_node_year=fixed_opex_per_node_year * (horizon_days / 365.0),
            variable_opex_usd_per_cycle_node=variable_opex_per_cycle_node,
            process_energy_cost_usd_per_cycle_node=process_energy_cost_per_cycle_node,
            replacement_interval_cycles=replacement_interval,
            replacement_cost_usd_per_node=replacement_cost_per_node,
        ))

    gross_kwh = gross_output_j / J_PER_KWH
    input_kwh = process_input_j / J_PER_KWH
    net_kwh = net_energy_j / J_PER_KWH
    lcoe = closed_loop_total_cost / net_kwh if net_kwh > 0 else None

    return {
        "scenario_id": scenario.get("scenario_id"),
        "status": scenario.get("status", "UNSPECIFIED"),
        "horizon": {
            "days": horizon_days,
            "nodes": nodes,
            "scheduled_cycles_per_year_per_node": scheduled_cycles,
            "uptime_fraction": uptime,
            "achieved_cycles_per_node": cycles,
            "network_cycles": cycles * nodes,
            "cycles_per_second_per_node": cycles / SECONDS_PER_YEAR,
        },
        "closed_loop_burn": {
            "retention_fraction_per_cycle": retention,
            "loss_fraction_per_cycle": loss_fraction,
            "loss_ppm_per_cycle": loss_fraction * 1e6,
            "loss_mol_per_cycle_per_node": loss_mol_per_cycle_per_node,
            "makeup_mol_year_network": total_makeup_mol,
            "first_fill_mol_network": first_fill_mol,
            "inventory_turnovers_per_year_per_node": inventory_turnovers_per_node_year,
            "makeup_mass_kg_year_network": makeup_mass_kg,
            "raw_feed_m3_year_for_makeup": raw_feed_m3_for_makeup,
            "makeup_fraction_of_host_annual_flow": makeup_fraction_of_host_annual_flow,
            "retention_for_0_1_inventory_turnover_year": retention_for_inventory_turnovers(cycles, 0.1),
            "retention_for_1_inventory_turnover_year": retention_for_inventory_turnovers(cycles, 1.0),
            "retention_for_10_inventory_turnovers_year": retention_for_inventory_turnovers(cycles, 10.0),
        },
        "energy_ledger": {
            "gross_output_kWh_year": gross_kwh,
            "process_input_kWh_year": input_kwh,
            "net_kWh_year": net_kwh,
            "year1_levelized_cost_usd_per_net_kWh": lcoe,
            "warning": (
                "Net energy is meaningful only when gross output and every material/process input "
                "are sourced for a real candidate."
            ),
        },
        "year1_costs_usd": {
            "capex_upfront": capex,
            "first_fill": first_fill_cost,
            "makeup": makeup_cost_total,
            "lost_medium_disposal": lost_medium_disposal_cost,
            "fixed_opex": fixed_opex,
            "variable_opex": variable_opex,
            "scheduled_component_replacement": replacement_cost,
            "process_energy": process_energy_cost,
            "closed_loop_total": closed_loop_total_cost,
        },
        "open_loop_material_use_comparator": {
            "full_refresh_mol_year_network": open_loop_mol,
            "material_cost_usd": open_loop_material_cost,
            "disposal_cost_usd": open_loop_disposal_cost,
            "total_cost_usd_same_nonmaterial_assumptions": open_loop_total_cost,
            "closed_loop_savings_usd": cost_savings,
            "closed_loop_savings_fraction": cost_savings_fraction,
            "warning": (
                "This is a material-reuse comparator, not a claim that real baseline plants "
                "discard a full working inventory every cycle."
            ),
        },
        "cost_checkpoints": checkpoints,
        "boundary_notes": [
            "Cycle 1 is expensive because this accounting places CAPEX and first fill up front.",
            "Cycle 100 is cheaper on a marginal and cumulative-average basis if retention is high.",
            "Recurring electrochemical regeneration, pumping, fouling, and wear do not automatically get cheaper with cycle count.",
            "At very high cycle counts, tiny per-cycle losses dominate annual material burn.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("scenario", help="Path to a year-1 scenario JSON file")
    args = parser.parse_args()
    data = json.loads(Path(args.scenario).read_text())
    print(json.dumps(simulate_year(data), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
