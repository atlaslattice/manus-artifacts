"""Run 1 — rooftop PV technical sensitivity on the desalination workshop roof.

Reproduces the derived numerics of RUN_1_SOLAR_v0_1.json.

Invariants exercised here:
  * the roof layout is MODELED, not surveyed — roof structure is UNKNOWN;
  * the local yield reference is a DIFFERENT project, used only as a yield basis;
  * current CNY savings stay UNKNOWN without a plant-specific current tariff;
  * the 2023 Shandong average grid factor is a location-based average, not a
    marginal factor, and not a lifecycle PV carbon calculation.
"""

from __future__ import annotations

from typing import Any

from .common import UNKNOWN, require_number

# --- sourced inputs --------------------------------------------------------
ROOF_FOOTPRINT_M2 = 17_474.32
ACTIVE_MODULE_COVERAGE_FRACTION = 0.60

LOCAL_REFERENCE_CAPACITY_MWP = 12.4956
LOCAL_REFERENCE_GENERATION_MWH_YEAR = 14_022.86

PROCESS_ENERGY_2025_GWH = 39.446
SHANDONG_2023_GRID_FACTOR_KGCO2_KWH = 0.6191
HISTORICAL_TARIFF_CNY_KWH = 0.555

#: Module-efficiency cases. S01_B names a commercial component inside a
#: modelled site layout; it is not a procurement commitment.
MODULE_CASES: dict[str, float] = {
    "S01_A": 0.23,
    "S01_B_SEA_SHIELD": 0.248,
}


def active_module_area_m2() -> float:
    """Modelled active module area on the workshop roof."""
    return ROOF_FOOTPRINT_M2 * ACTIVE_MODULE_COVERAGE_FRACTION


def local_yield_kwh_per_kwp_year() -> float:
    """Specific yield derived from the local reported reference project."""
    return LOCAL_REFERENCE_GENERATION_MWH_YEAR / LOCAL_REFERENCE_CAPACITY_MWP


def case(name: str, module_efficiency: float) -> dict[str, Any]:
    """One rooftop PV case at a stated module efficiency."""
    eff = require_number(module_efficiency, "module_efficiency_fraction")
    if not 0 < eff <= 1:
        raise ValueError("module_efficiency_fraction must lie in (0, 1]")

    area = active_module_area_m2()
    capacity_mwp = area * eff / 1000.0
    yield_kwh_kwp = LOCAL_REFERENCE_GENERATION_MWH_YEAR / LOCAL_REFERENCE_CAPACITY_MWP
    generation_gwh = capacity_mwp * yield_kwh_kwp / 1000.0

    return {
        "module_efficiency_fraction": eff,
        "DC_capacity_MWp": capacity_mwp,
        "annual_generation_GWh": generation_gwh,
        "fraction_of_2025_UF_RO_process_energy": generation_gwh / PROCESS_ENERGY_2025_GWH,
        "current_cost_saving_CNY": UNKNOWN,
        "historical_0_555_tariff_counterfactual_CNY": (
            generation_gwh * 1e6 * HISTORICAL_TARIFF_CNY_KWH
        ),
        "location_based_CO2_avoided_tonnes_using_2023_Shandong_factor": (
            generation_gwh * 1e6 * SHANDONG_2023_GRID_FACTOR_KGCO2_KWH / 1000.0
        ),
    }


def run() -> dict[str, Any]:
    """Run 1 — full sensitivity package."""
    return {
        "artifact_id": "DJK-NODE-001-RUN-1-SOLAR-v0.1",
        "status": "EXECUTED_TECHNICAL_SENSITIVITY_NON_CANON",
        "baseline": "DJK-NODE-001-RUN-0-OPERATING-2025-v0.2",
        "site_inputs": {
            "desalination_workshop_footprint_m2": ROOF_FOOTPRINT_M2,
            "effective_active_module_coverage_fraction": ACTIVE_MODULE_COVERAGE_FRACTION,
            "active_module_area_m2": active_module_area_m2(),
            "coverage_status": "MODELED_CONSERVATIVE",
            "roof_structural_suitability": UNKNOWN,
            "interconnection_limit": UNKNOWN,
        },
        "local_generation_reference": {
            "reference_capacity_MWp": LOCAL_REFERENCE_CAPACITY_MWP,
            "reference_generation_MWh_year": LOCAL_REFERENCE_GENERATION_MWH_YEAR,
            "derived_yield_kWh_per_kWp_year": (
                LOCAL_REFERENCE_GENERATION_MWH_YEAR / LOCAL_REFERENCE_CAPACITY_MWP
            ),
            "evidence": "DERIVED_FROM_LOCAL_REPORTED_PROJECT",
        },
        "cases": {name: case(name, eff) for name, eff in MODULE_CASES.items()},
        "carbon_boundary": {
            "Shandong_2023_average_grid_factor_kgCO2_kWh": SHANDONG_2023_GRID_FACTOR_KGCO2_KWH,
            "status": "REPORTED_LATEST_OFFICIAL_FACTOR_LOCATED",
            "warning": (
                "Not a 2026 marginal emissions factor and not a lifecycle PV "
                "carbon calculation."
            ),
        },
    }
