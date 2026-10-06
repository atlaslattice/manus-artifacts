#!/usr/bin/env python3
"""China 167-project hypothetical multi-resource retrofit simulator v0.1.

Public-record host baseline:
- 167 desalination projects
- 3.077 million tonnes/day aggregate desalination capacity at end-2025

Scenario overlay:
- optionally assume these 167 facilities are Atlas Lattice nodes.
- that overlay is UNVERIFIED_SCENARIO_ASSUMPTION and has no effect on physics.

The model separates:
1. water/desalination load,
2. material throughput and hypothetical recovery,
3. salinity-gradient energy sensitivity,
4. scenario-only Atlas/ORCS labels.

No nuclear reactions or nuclear-fuel-cycle operations are modeled.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from typing import Any, Dict

DAYS_PER_YEAR = 365.0
HOURS_PER_DAY = 24.0

DEFAULT_CONCENTRATIONS_KG_M3 = {
    "chloride": 19.0,
    "sodium": 10.5,
    "magnesium": 1.35,
    "calcium": 0.410,
    "potassium": 0.390,
    "deuterium_equivalent": 0.0325,
    "lithium": 0.00017,
}


def network_balance(s: Dict[str, Any]) -> Dict[str, Any]:
    host = s["host"]
    product_m3_day = float(host["aggregate_product_water_m3_day"])
    projects = int(host["project_count"])
    recovery = float(s["ro"]["water_recovery_fraction"])

    if projects <= 0:
        raise ValueError("project_count must be > 0")
    if product_m3_day <= 0:
        raise ValueError("aggregate_product_water_m3_day must be > 0")
    if not 0 < recovery < 1:
        raise ValueError("water_recovery_fraction must be between 0 and 1")

    feed_m3_day = product_m3_day / recovery
    brine_m3_day = feed_m3_day - product_m3_day

    concentrations = dict(DEFAULT_CONCENTRATIONS_KG_M3)
    concentrations.update(s.get("feed_concentrations_kg_m3", {}))

    inventory = {}
    for species, kg_m3 in concentrations.items():
        kg_day = feed_m3_day * float(kg_m3)
        inventory[species] = {
            "feed_kg_day": kg_day,
            "feed_tonnes_day": kg_day / 1000.0,
            "feed_tonnes_year": kg_day * DAYS_PER_YEAR / 1000.0,
        }

    capture_scenarios = {}
    for label, fraction in s["resource_capture_sensitivity"].items():
        f = float(fraction)
        if not 0 <= f <= 1:
            raise ValueError("capture fractions must be in [0,1]")
        capture_scenarios[label] = {
            species: {
                "captured_tonnes_day": values["feed_tonnes_day"] * f,
                "captured_tonnes_year": values["feed_tonnes_year"] * f,
            }
            for species, values in inventory.items()
        }

    desalination_load = {}
    for label, sec_kwh_m3 in s["energy"]["desalination_specific_energy_kWh_m3"].items():
        daily_kwh = product_m3_day * float(sec_kwh_m3)
        desalination_load[label] = {
            "GWh_day": daily_kwh / 1e6,
            "TWh_year": daily_kwh * DAYS_PER_YEAR / 1e9,
            "average_MW": daily_kwh / HOURS_PER_DAY / 1000.0,
        }

    partner_fraction = float(
        s["energy"]["matched_low_salinity_flow_fraction_of_product"]
    )
    if not 0 <= partner_fraction <= 1:
        raise ValueError("matched_low_salinity_flow_fraction_of_product must be in [0,1]")

    matched_m3_day = product_m3_day * partner_fraction
    salinity_gradient = {}
    for label, specific_kwh_m3 in s["energy"][
        "salinity_gradient_specific_energy_kWh_per_m3_partner"
    ].items():
        daily_kwh = matched_m3_day * float(specific_kwh_m3)
        average_mw = daily_kwh / HOURS_PER_DAY / 1000.0
        salinity_gradient[label] = {
            "matched_low_salinity_m3_day": matched_m3_day,
            "GWh_day": daily_kwh / 1e6,
            "TWh_year": daily_kwh * DAYS_PER_YEAR / 1e9,
            "average_MW": average_mw,
            "100MW_compute_load_equivalents": average_mw / 100.0,
        }

    atlas_overlay = s.get("atlas_lattice_scenario_overlay", {})
    orcs = s.get("orcs_reference_overlay", {})

    return {
        "status": "HYPOTHETICAL_167_HOST_NETWORK_SENSITIVITY",
        "evidence_boundary": {
            "verified_public_host_fact": (
                "167 Chinese desalination projects with aggregate 3.077 million "
                "tonnes/day capacity at end-2025."
            ),
            "atlas_overlay_status": atlas_overlay.get("evidence_status", "NOT_INCLUDED"),
            "atlas_overlay_assumption": atlas_overlay.get("assumption"),
            "orcs_overlay_status": orcs.get("status", "NOT_INCLUDED"),
        },
        "host": {
            "project_count": projects,
            "aggregate_product_water_m3_day": product_m3_day,
            "average_product_water_m3_day_per_project": product_m3_day / projects,
        },
        "ro_mass_balance": {
            "water_recovery_fraction": recovery,
            "feed_m3_day": feed_m3_day,
            "product_m3_day": product_m3_day,
            "brine_m3_day": brine_m3_day,
            "feed_km3_year": feed_m3_day * DAYS_PER_YEAR / 1e9,
            "product_km3_year": product_m3_day * DAYS_PER_YEAR / 1e9,
            "brine_km3_year": brine_m3_day * DAYS_PER_YEAR / 1e9,
        },
        "incoming_species_inventory_not_recovery_claim": inventory,
        "hypothetical_capture_scenarios": capture_scenarios,
        "desalination_electric_load_reference": desalination_load,
        "salinity_gradient_reference_lane": salinity_gradient,
        "architecture_notes": [
            "Use existing pressure-energy recovery before claiming new savings.",
            "Recovered minerals/isotopes are co-products, reusable media, or avoided waste; they are not automatically electrical energy.",
            "Resource recovery and salinity-gradient harvesting can compete for the same brine chemistry; route streams explicitly.",
            "Bulk recovery and trace recovery should be optimized separately.",
            "Natural uranium, if screened, remains a high-level resource-recovery item only; no enrichment or fuel-cycle operation is modeled.",
            "Plant-level retrofit requires site-specific feed chemistry, recovery ratio, membrane train, pressure, pretreatment, discharge permit, and ecology.",
            "Microplastic/PFAS capture only counts as ocean regeneration if the concentrated residual is destroyed, recycled, or securely sequestered rather than returned to the sea.",
            "There is no single universally optimal ocean pH; discharge chemistry should be controlled against local background carbonate chemistry, ecology, and regulatory limits.",
        ],
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("scenario")
    args = p.parse_args()
    scenario = json.loads(Path(args.scenario).read_text())
    print(json.dumps(network_balance(scenario), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
