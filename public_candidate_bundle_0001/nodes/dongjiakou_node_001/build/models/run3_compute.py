"""Run 3 — C01 compute as a load and advisory service, never an energy source.

Reproduces the derived numerics of RUN_3_COMPUTE_v0_2.json.

Invariants exercised here:
  * C01 is a load. It is not generation and it is not storage.
  * PUE = 1.25 is a sector policy reference, not a Node-001 receipt. The
    thermodynamic floor PUE = 1 is shown alongside it so the reference never
    hides the facility-level load.
  * Low-grade heat quantity is not electric value. The first-law upper bound is
    reported, but useful-heat credit is ZERO until a measured sink exists.
  * Existing S01 PV is not incremental to the node. Routing it to compute
    changes attribution; it does not make C01 electrically neutral.
  * Model service benefit stays zero without before/after KPI evidence.
"""

from __future__ import annotations

from typing import Any

from .common import UNKNOWN, guard_fraction, require_number

HOURS_PER_YEAR = 8760.0
GWH_PER_MW_YEAR = HOURS_PER_YEAR / 1000.0  # 8.76 GWh per MW at load factor 1

PROCESS_ENERGY_2025_GWH = 39.446
S01_A_PV_GWH = 2.70619355
S01_B_PV_GWH = 2.917982611
SHANDONG_2023_GRID_FACTOR_KGCO2_KWH = 0.6191

#: Reference sensitivity only. NOT a Node-001 receipt.
REFERENCE_PUE = 1.25
REFERENCE_PUE_STATUS = "SECTOR_POLICY_REFERENCE_NOT_NODE_RECEIPT"
REFERENCE_PUE_SOURCE_RECORDS = ("DJK-SR-0026", "DJK-SR-0027")

THERMODYNAMIC_FLOOR_PUE = 1.0

#: Commissioning tiers. 100 kW is the first tier; 250 kW is earned; larger gated.
TIERS_KW = (100.0, 250.0, 500.0, 1000.0)
TIER_ROLES = {
    100.0: "recommended first commissioning tier",
    250.0: (
        "earned expansion tier; annual PV energy magnitude is near facility "
        "energy at PUE=1.25, but hourly matching is UNKNOWN"
    ),
    500.0: "gated scale case",
    1000.0: "later gated scale case",
}

UNKNOWN_PARAMETERS = {
    "L_IT_load_factor": "UNKNOWN_0_TO_1",
    "actual_PUE": "UNKNOWN_GE_1",
    "WUE": "UNKNOWN",
    "compute_cooling_water_source": "UNKNOWN",
    "hourly_solar_compute_overlap": "UNKNOWN",
    "PV_curtailment": "NOT_ESTABLISHED",
    "useful_heat_capture_fraction": "UNKNOWN",
    "coolant_supply_return_temperature": "UNKNOWN",
    "CIP_temperature_setpoint": "UNKNOWN",
    "CIP_thermal_demand": "UNKNOWN",
    "heat_pump_COP": "UNKNOWN",
}


def it_energy_gwh(it_capacity_kw: float, load_factor: float = 1.0) -> float:
    """E_IT = P_IT * 8760 * L, in GWh."""
    p_it = require_number(it_capacity_kw, "it_capacity_kw")
    load = guard_fraction(load_factor, "load_factor")
    if p_it < 0:
        raise ValueError("it_capacity_kw must be non-negative")
    return p_it / 1000.0 * GWH_PER_MW_YEAR * load


def facility_energy_gwh(it_capacity_kw: float, load_factor: float, pue: float) -> float:
    """E_facility = E_IT * PUE."""
    pue_val = require_number(pue, "pue")
    if pue_val < 1.0:
        raise ValueError("pue must be >= 1 (thermodynamic floor)")
    return it_energy_gwh(it_capacity_kw, load_factor) * pue_val


def useful_heat_gwhth(
    it_capacity_kw: float,
    load_factor: float,
    *,
    f_capture: Any = UNKNOWN,
    f_temperature_match: Any = UNKNOWN,
    f_temporal_match: Any = UNKNOWN,
) -> Any:
    """Q_useful = E_IT * f_capture * f_temperature_match * f_temporal_match.

    With any factor UNKNOWN the result is UNKNOWN, not zero and not the
    first-law upper bound. Callers must not substitute 1.0 for a missing factor.
    """
    it_gwh = it_energy_gwh(it_capacity_kw, load_factor)
    fc = guard_fraction(f_capture, "f_capture")
    ft = guard_fraction(f_temperature_match, "f_temperature_match")
    fm = guard_fraction(f_temporal_match, "f_temporal_match")
    return it_gwh * fc * ft * fm


def heat_pump_electric_saved_gwh(q_useful_gwhth: float, q_cip_demand_gwhth: float, cop: float) -> float:
    """E_HP_saved = min(Q_useful, Q_CIP_demand) / COP_HP."""
    q_useful = require_number(q_useful_gwhth, "q_useful_gwhth")
    q_cip = require_number(q_cip_demand_gwhth, "q_cip_demand_gwhth")
    cop_val = require_number(cop, "cop")
    if cop_val <= 0:
        raise ValueError("COP must be positive")
    return min(q_useful, q_cip) / cop_val


def node_net_electric_delta_gwh(
    new_incremental_clean_generation_gwh: float,
    verified_process_electric_savings_gwh: float,
    verified_hp_electric_savings_gwh: float,
    compute_facility_energy_gwh: float,
) -> float:
    """Node net electric delta.

    Every term must be measured or verified. Existing S01 PV assigned to C01 is
    NOT new incremental generation and must not be passed as such.
    """
    return (
        require_number(new_incremental_clean_generation_gwh, "new_incremental_clean_generation_gwh")
        + require_number(verified_process_electric_savings_gwh, "verified_process_electric_savings_gwh")
        + require_number(verified_hp_electric_savings_gwh, "verified_hp_electric_savings_gwh")
        - require_number(compute_facility_energy_gwh, "compute_facility_energy_gwh")
    )


def tier(case_id: str, it_capacity_kw: float) -> dict[str, Any]:
    """One commissioning tier at load factor 1, both PUE boundaries."""
    it_gwh = it_energy_gwh(it_capacity_kw, 1.0)
    fac_floor = it_gwh * THERMODYNAMIC_FLOOR_PUE
    fac_ref = it_gwh * REFERENCE_PUE
    return {
        "case_id": case_id,
        "IT_capacity_kW": it_capacity_kw,
        "IT_energy_GWh_at_L1": it_gwh,
        "facility_energy_GWh_at_L1_PUE1": fac_floor,
        "facility_energy_GWh_at_L1_PUE1_25": fac_ref,
        "process_energy_share_at_PUE1": fac_floor / PROCESS_ENERGY_2025_GWH,
        "process_energy_share_at_PUE1_25": fac_ref / PROCESS_ENERGY_2025_GWH,
        "S01_A_annual_energy_ratio_to_facility_at_PUE1_25": S01_A_PV_GWH / fac_ref,
        "S01_B_annual_energy_ratio_to_facility_at_PUE1_25": S01_B_PV_GWH / fac_ref,
        "grid_only_location_CO2_t_at_PUE1_25": (
            fac_ref * 1e6 * SHANDONG_2023_GRID_FACTOR_KGCO2_KWH / 1000.0
        ),
        "IT_heat_first_law_upper_bound_GWhth": it_gwh,
        "deployment_role": TIER_ROLES[it_capacity_kw],
    }


def run() -> dict[str, Any]:
    """Run 3 — full compute sensitivity package."""
    return {
        "artifact_id": "DJK-NODE-001-RUN-3-COMPUTE-v0.2",
        "status": "EXECUTED_PARAMETRIC_TECHNICAL_SENSITIVITY_NON_CANON",
        "supersedes": "RUN_3_COMPUTE_v0_1.json",
        "study_classification": "TECHNICAL_FEASIBILITY_PLUS_CONDITIONAL_ECONOMICS",
        "baseline": {
            "operating_year": 2025,
            "UF_RO_process_energy_GWh": PROCESS_ENERGY_2025_GWH,
            "average_UF_RO_process_power_MW": PROCESS_ENERGY_2025_GWH * 1000.0 / HOURS_PER_YEAR,
            "S01_A_PV_GWh_year": S01_A_PV_GWH,
            "S01_B_PV_GWh_year": S01_B_PV_GWH,
            "Shandong_2023_average_grid_factor_kgCO2_kWh": SHANDONG_2023_GRID_FACTOR_KGCO2_KWH,
            "current_effective_tariff_CNY_kWh": UNKNOWN,
        },
        "compute_equations": {
            "IT_energy_GWh": "P_IT_MW * 8.76 * L",
            "facility_energy_GWh": "IT_energy_GWh * PUE",
            "location_average_grid_CO2_t": "grid_energy_GWh * 1000 * 0.6191",
            "useful_heat_upper_bound_GWhth": "IT_energy_GWh",
            "useful_heat_credit": "IT_energy_GWh * f_capture * f_temperature_match * f_temporal_match",
            "verified_HP_electricity_saved_GWh": "min(Q_useful,Q_CIP_demand)/COP_HP",
            "node_net_electric_delta_GWh": (
                "new_incremental_clean_generation + verified_process_electric_savings "
                "+ verified_HP_electricity_savings - compute_facility_energy"
            ),
        },
        "unknown_parameters": dict(UNKNOWN_PARAMETERS),
        "reference_scenario": {
            "PUE": REFERENCE_PUE,
            "status": REFERENCE_PUE_STATUS,
            "source_record_ids": list(REFERENCE_PUE_SOURCE_RECORDS),
            "load_factor_L": 1,
            "warning": (
                "Used only to expose facility-level load that the PUE=1 "
                "thermodynamic floor hides."
            ),
        },
        "tiers": [
            tier(f"C01-PILOT-{int(kw)}" if kw < 500 else f"C01-{int(kw)}", kw)
            for kw in TIERS_KW
        ],
        "anti_double_counting": {
            "rule": "PV_credit_compute + PV_credit_desalination <= measured_PV_generation",
            "existing_S01_PV_is_incremental_to_node": False,
            "note": (
                "Routing existing S01 generation to compute changes attribution. "
                "It does not make C01 electrically neutral unless verified "
                "curtailment is captured or new generation/savings are added."
            ),
        },
        "heat_credit": {
            "baseline_useful_heat_GWhth": 0,
            "reason": (
                "No public CIP setpoint, thermal duty, heat-pump COP map, coolant "
                "temperature or temporal overlap receipt."
            ),
            "low_grade_heat_rule": (
                "Thermal quantity is not equal to electric value. Only displaced "
                "measured heat-pump electricity or another verified sink earns "
                "electric credit."
            ),
        },
        "ORCS_gates": {
            "PUE": "MEASURE",
            "WUE": "MEASURE",
            "CUE": "MEASURE_WITH_BOUNDARY",
            "INV_19_Water_Cohesion": "VETO",
            "downstream_water_quality": "NO_DEGRADATION_REQUIRED",
            "evidence_classes": "verified/derived/proposed",
            "model_service_benefit": "ZERO_UNTIL_BEFORE_AFTER_MEASURED",
        },
        "result": {
            "C01_is_energy_source": False,
            "C01_net_positive": "NOT_PROVEN",
            "recommended_first_tier": "100 kW IT",
            "recommended_next_tier": "250 kW IT after pilot gates",
            "larger_tiers": "500 kW and 1 MW are gated",
            "surprising_but_bounded_finding": (
                "At the 1.25 PUE reference, a full-load 250 kW IT facility "
                "consumes about 2.738 GWh/year, close in annual-energy magnitude "
                "to S01's 2.706-2.918 GWh/year. This is not hourly "
                "self-powering and cannot double-count PV."
            ),
        },
    }


# ---------------------------------------------------------------------------
# Locality-scale compute scenario
# ---------------------------------------------------------------------------
#: A 40 MW-class compute subnode is now a legitimate FUTURE LOCALITY SCENARIO.
#: It is not a commissioning tier and it does not replace the 100 kW ladder.
#: The point of computing it is to show how large the load becomes relative to
#: the locality's other flows, so that the question gets asked in the right form.
LOCALITY_SCENARIO_KW = 40_000.0


def locality_scenario_40mw() -> dict[str, Any]:
    """Price the 40 MW-class locality scenario as a load, not an opportunity."""
    it_gwh = it_energy_gwh(LOCALITY_SCENARIO_KW, 1.0)
    facility_gwh = facility_energy_gwh(LOCALITY_SCENARIO_KW, 1.0, REFERENCE_PUE)

    return {
        "artifact_id": "DJK-NODE-001-C01-LOCALITY-SCENARIO-40MW-v0.1",
        "status": "SCENARIO_ONLY_NOT_A_COMMISSIONING_TIER",
        "it_capacity_kw": LOCALITY_SCENARIO_KW,
        "it_energy_gwh_year_at_L1": it_gwh,
        "facility_energy_gwh_year_at_pue_1_25": facility_gwh,
        "pue_basis": REFERENCE_PUE_STATUS,
        "comparisons": {
            "vs_w01_2025_process_energy_gwh": PROCESS_ENERGY_2025_GWH,
            "multiple_of_w01_process_energy": facility_gwh / PROCESS_ENERGY_2025_GWH,
            "vs_s01_a_pv_gwh": S01_A_PV_GWH,
            "multiple_of_s01_a_pv": facility_gwh / S01_A_PV_GWH,
        },
        "the_question_is_not": (
            "There are ~295 MW of renewables planned nearby, therefore run 40 MW "
            "of compute."
        ),
        "the_question_is": (
            "Can a 40 MW compute subnode be contracted, dispatched and thermally "
            "integrated into this locality while preserving water, ecological, "
            "grid, carbon and component vetoes hour by hour?"
        ),
        "unlock_condition": (
            "Node-001 green-direct eligibility confirmation, plus a PPA or "
            "settlement meter and an eligible-load determination. Absent those, "
            "the green-direct credit is exactly zero."
        ),
        "not_claimed": [
            "No green-direct credit.",
            "No net-positive claim at any scale.",
            "No replacement of the 100 kW first commissioning tier.",
            "No suggestion that regional planned capacity is available to the node.",
        ],
    }
