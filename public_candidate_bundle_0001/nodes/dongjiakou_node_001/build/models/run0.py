"""Run 0 — desalination baseline and the dated 2025 operating calibration.

Reproduces the derived numerics of:
  * RUN_0_BASELINE_v0_1.json
  * RUN_0_OPERATING_2025_v0_2.json

Invariants exercised here:
  * nameplate capacity never silently becomes an operating volume;
  * the 2018-2020 historical tariff never populates a current cost;
  * recovery 0.45/0.50 stays a technology/application range, not a measured value;
  * reject-equivalent (feed - product) never becomes a marine-discharge claim.
"""

from __future__ import annotations

from typing import Any

from .common import UNKNOWN, is_unknown, require_number, guard_fraction

# --- sourced inputs --------------------------------------------------------
PRODUCT_CAPACITY_M3_DAY = 100_000.0
DAYS_PER_YEAR = 365.0
UF_RO_PROCESS_TRAIN_SEC_KWH_M3 = 2.2
CHEMICAL_COST_CNY_M3_UPPER_BOUND = 0.15
RECOVERY_CASES = (0.45, 0.50)

PRODUCT_SUPPLY_2025_M3 = 17_930_000.0
PRODUCT_SUPPLY_2020_M3 = 12_620_000.0

HISTORICAL_TARIFF_CNY_KWH = 0.555
HISTORICAL_TARIFF_PERIOD = "2018-01-01 through 2020-12-31"

REPORTED_SUPPLY_PRICE_CNY_M3 = 4.25

#: Fields that remain UNKNOWN at Node-001 and may not be backfilled.
UNCHANGED_UNKNOWNS = (
    "whole_site_SEC_kWh_m3",
    "delta_aux_kWh_m3",
    "current_measured_recovery_fraction",
    "current_feed_and_reject_stream_map",
    "current_brine_composition",
    "fouling_rate_and_cleaning_frequency",
    "current_CIP_and_additive_chemistry",
    "current_ecological_monitoring_primary_data",
    "hydraulic_unused_head_profile",
    "roof_structural_and_interconnection_limits",
)


def utilization_fraction(annual_product_m3: float) -> float:
    """Derive utilization U from a reported annual product volume."""
    volume = require_number(annual_product_m3, "annual_product_m3")
    if volume < 0:
        raise ValueError("annual_product_m3 must be non-negative")
    return volume / (PRODUCT_CAPACITY_M3_DAY * DAYS_PER_YEAR)


def mass_balance(recovery: float, annual_product_m3: float) -> dict[str, float]:
    """Feed / product / reject-equivalent balance at a stated technology recovery.

    ``reject_equivalent`` is modelled feed minus product. It is NOT measured
    marine discharge, and the model says so in the returned field name.
    """
    r = guard_fraction(recovery, "recovery", low=1e-9, high=1.0)
    product = require_number(annual_product_m3, "annual_product_m3")
    feed = product / r
    return {
        "annual_feed_m3": feed,
        "annual_product_m3": product,
        "annual_reject_equivalent_m3": feed - product,
    }


def baseline(utilization: Any = UNKNOWN) -> dict[str, Any]:
    """Run 0 v0.1 — nameplate baseline, optionally evaluated at a stated U.

    ``utilization=UNKNOWN`` (the default) returns the per-U coefficients only.
    No Monte Carlo is performed and no UNKNOWN is imputed.
    """
    per_u_product = PRODUCT_CAPACITY_M3_DAY * DAYS_PER_YEAR
    per_u_energy_gwh = per_u_product * UF_RO_PROCESS_TRAIN_SEC_KWH_M3 / 1e6
    per_u_chem = per_u_product * CHEMICAL_COST_CNY_M3_UPPER_BOUND

    result: dict[str, Any] = {
        "artifact_id": "DJK-NODE-001-RUN-0-v0.1",
        "status": "EXECUTED_BASELINE_SIMULATION_NON_CANON",
        "execution_mode": "deterministic; no Monte Carlo; no UNKNOWN imputation",
        "inputs": {
            "product_capacity_m3_day": PRODUCT_CAPACITY_M3_DAY,
            "UF_RO_process_train_SEC_kWh_m3": UF_RO_PROCESS_TRAIN_SEC_KWH_M3,
            "chemical_cost_CNY_m3_relation": "<",
            "chemical_cost_CNY_m3_upper_bound": CHEMICAL_COST_CNY_M3_UPPER_BOUND,
            "recovery_cases": list(RECOVERY_CASES),
            "utilization_U": utilization,
            "whole_site_SEC_kWh_m3": UNKNOWN,
            "plant_effective_tariff_CNY_kWh": UNKNOWN,
        },
        "coefficients_per_U": {
            "annual_product_m3": per_u_product,
            "annual_process_train_energy_GWh": per_u_energy_gwh,
            "annual_chemical_cost_CNY_upper_bound": per_u_chem,
        },
        "mass_balance": {
            f"{r:.2f}": {
                "feed_m3_day": PRODUCT_CAPACITY_M3_DAY / r,
                "product_m3_day": PRODUCT_CAPACITY_M3_DAY,
                "reject_equivalent_m3_day": PRODUCT_CAPACITY_M3_DAY / r - PRODUCT_CAPACITY_M3_DAY,
                "annual_feed_m3_per_U": (PRODUCT_CAPACITY_M3_DAY / r) * DAYS_PER_YEAR,
                "annual_reject_equivalent_m3_per_U": (
                    PRODUCT_CAPACITY_M3_DAY / r - PRODUCT_CAPACITY_M3_DAY
                )
                * DAYS_PER_YEAR,
            }
            for r in RECOVERY_CASES
        },
    }

    if is_unknown(utilization):
        result["U1_reference_not_operating_claim"] = {
            "annual_product_m3": per_u_product,
            "annual_process_train_energy_GWh": per_u_energy_gwh,
            "annual_chemical_cost_CNY_upper_bound": per_u_chem,
        }
    else:
        u = guard_fraction(utilization, "utilization_U")
        result["evaluated_at_U"] = {
            "U": u,
            "annual_product_m3": per_u_product * u,
            "annual_process_train_energy_GWh": per_u_energy_gwh * u,
            "annual_chemical_cost_CNY_upper_bound": per_u_chem * u,
        }

    result["retrofit_credit"] = {
        "S01_solar": 0,
        "H01_mini_hydro": 0,
        "C01_compute": 0,
        "F01_adaptive_fouling": 0,
        "F02_sono_CIP": 0,
        "resource_recovery": 0,
        "OAE": 0,
    }
    return result


def operating_2025() -> dict[str, Any]:
    """Run 0 v0.2 — dated 2025 operating-volume calibration.

    Uses the 2025 reported product supply (17.93 Mm3) as the operating anchor.
    Electricity *cost* stays UNKNOWN: no 2026 plant-specific tariff exists.
    """
    u = utilization_fraction(PRODUCT_SUPPLY_2025_M3)
    process_energy_gwh = PRODUCT_SUPPLY_2025_M3 * UF_RO_PROCESS_TRAIN_SEC_KWH_M3 / 1e6

    mass: dict[str, dict[str, float]] = {}
    for r in RECOVERY_CASES:
        mb = mass_balance(r, PRODUCT_SUPPLY_2025_M3)
        mass[f"{r:.2f}"] = {
            "annual_feed_m3": mb["annual_feed_m3"],
            "annual_product_m3": mb["annual_product_m3"],
            "annual_reject_equivalent_m3": mb["annual_reject_equivalent_m3"],
        }

    return {
        "artifact_id": "DJK-NODE-001-RUN-0-OPERATING-2025-v0.2",
        "status": "EXECUTED_DERIVED_OPERATING_BASELINE_NON_CANON",
        "operating_year": 2025,
        "reported_product_supply_m3": PRODUCT_SUPPLY_2025_M3,
        "derived_utilization_U": u,
        "reported_UF_RO_process_train_SEC_kWh_m3": UF_RO_PROCESS_TRAIN_SEC_KWH_M3,
        "derived_process_train_energy_GWh": process_energy_gwh,
        "chemical_cost_CNY_m3_relation": "<",
        "chemical_cost_CNY_m3_upper_bound": CHEMICAL_COST_CNY_M3_UPPER_BOUND,
        "derived_annual_chemical_cost_CNY_upper_bound": (
            PRODUCT_SUPPLY_2025_M3 * CHEMICAL_COST_CNY_M3_UPPER_BOUND
        ),
        "mass_balance_using_reported_technology_recovery_range": mass,
        "economics": {
            "current_effective_electricity_tariff_CNY_kWh": UNKNOWN,
            "current_electricity_cost_CNY": UNKNOWN,
            "historical_2018_2020_tariff_CNY_kWh": HISTORICAL_TARIFF_CNY_KWH,
            "historical_tariff_counterfactual_only_CNY_for_2025_process_energy": (
                process_energy_gwh * 1e6 * HISTORICAL_TARIFF_CNY_KWH
            ),
            "warning": (
                "The historical tariff counterfactual is not a 2025 or 2026 "
                "electricity-cost claim."
            ),
        },
    }


def historical_counterfactual_2025() -> float:
    """Historical-tariff counterfactual for 2025 process energy (CNY).

    Exposed separately so that a validator can prove it is never consumed as a
    current-cost figure.
    """
    process_energy_gwh = PRODUCT_SUPPLY_2025_M3 * UF_RO_PROCESS_TRAIN_SEC_KWH_M3 / 1e6
    return process_energy_gwh * 1e6 * HISTORICAL_TARIFF_CNY_KWH
