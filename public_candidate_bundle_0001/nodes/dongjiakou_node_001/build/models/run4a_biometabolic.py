"""Run 4A — BIO01 organics / wastewater / nutrient recovery transfer functions.

Reproduces the derived numerics of RUN_4A_BIOMETABOLIC_v0_1.json.

Invariants exercised here:
  * zero baseline credit across every BIO01 product stream;
  * the Qingdao food-waste reference is retrospective and belongs to a different
    site — it is a transfer-function coefficient, not a Dongjiakou design yield;
  * the 0.35 m3 CH4 / kg bCOD figure is a stoichiometric ceiling, not a yield;
  * one N/P/Mg mass cannot receive both a nutrient-recovery and a compost credit;
  * reclaimed water is credited only when verified reuse displaces another source.
"""

from __future__ import annotations

from typing import Any

from .common import UNKNOWN, guard_fraction, require_number

DAYS_PER_YEAR = 365.0

#: Qingdao retrospective operating reference (DJK-SR-0043).
QINGDAO_CUMULATIVE_FOOD_WASTE_T = 260_000.0
QINGDAO_CUMULATIVE_BIOGAS_M3 = 5_260_000.0

#: Stoichiometric ceiling for anaerobic methane yield.
THEORETICAL_CH4_M3_PER_KG_BCOD_STP = 0.35

ILLUSTRATIVE_FEED_TPD = (1.0, 5.0, 10.0, 25.0, 50.0)


def reference_biogas_m3_per_tonne() -> float:
    """Derived reference biogas coefficient from the local Qingdao precedent."""
    return QINGDAO_CUMULATIVE_BIOGAS_M3 / QINGDAO_CUMULATIVE_FOOD_WASTE_T


def food_waste_reference(feed_tonnes_day: float) -> dict[str, Any]:
    """Reference biogas for a stated verified food-waste feed.

    Returns a *reference* volume only. Energy credit is UNKNOWN until CH4
    fraction, flare/use split and conversion efficiency are measured.
    """
    feed = require_number(feed_tonnes_day, "feed_tonnes_day")
    if feed < 0:
        raise ValueError("feed_tonnes_day must be non-negative")
    annual_t = feed * DAYS_PER_YEAR
    return {
        "annual_feed_tonnes": annual_t,
        "reference_biogas_m3_year": annual_t * reference_biogas_m3_per_tonne(),
        "energy_credit": UNKNOWN,
    }


def wastewater_methane_ceiling(
    flow_m3_day: float,
    cod_mg_l: float,
    biodegradable_fraction: float,
    cod_removal_fraction: float,
) -> dict[str, Any]:
    """Theoretical methane ceiling for an eligible high-COD sidestream.

    This is a ceiling, not a plant yield. Dissolved methane, sulfate reduction,
    biomass synthesis and parasitics are not closed.
    """
    q = require_number(flow_m3_day, "flow_m3_day")
    cod = require_number(cod_mg_l, "cod_mg_l")
    if q < 0 or cod < 0:
        raise ValueError("flow_m3_day and cod_mg_l must be non-negative")
    f_bio = guard_fraction(biodegradable_fraction, "biodegradable_fraction")
    f_rem = guard_fraction(cod_removal_fraction, "cod_removal_fraction")

    kg_cod_day = q * cod / 1000.0
    kg_bcod_removed_day = kg_cod_day * f_bio * f_rem
    return {
        "COD_load_kg_day": kg_cod_day,
        "biodegradable_COD_removed_kg_day": kg_bcod_removed_day,
        "theoretical_CH4_ceiling_m3_day_STP": (
            kg_bcod_removed_day * THEORETICAL_CH4_M3_PER_KG_BCOD_STP
        ),
        "warning": (
            "Stoichiometric ceiling, not plant yield; dissolved methane, "
            "sulfate, biomass synthesis and parasitics are not closed."
        ),
    }


def run() -> dict[str, Any]:
    """Run 4A — zero-credit baseline plus explicit transfer functions."""
    coefficient = reference_biogas_m3_per_tonne()
    return {
        "artifact_id": "DJK-NODE-001-RUN-4A-BIOMETABOLIC-v0.1",
        "status": "EXECUTED_PARAMETRIC_TRANSFER_FUNCTION_NON_CANON",
        "study_classification": "TECHNICAL_FEASIBILITY_PLUS_CONDITIONAL_ECONOMICS",
        "baseline_credit": {
            "food_waste_feed_tonnes_day": 0,
            "biogas_m3_year": 0,
            "methane_energy_credit": 0,
            "wastewater_bioreactor_credit": 0,
            "reclaimed_water_credit": 0,
            "struvite_credit": 0,
            "ammonium_credit": 0,
            "compost_credit": 0,
            "reason": (
                "No Node-001 feedstock allocation, chemistry, product assay or "
                "off-take receipt."
            ),
        },
        "local_food_waste_reference": {
            "source_record_id": "DJK-SR-0043",
            "cumulative_food_waste_tonnes": QINGDAO_CUMULATIVE_FOOD_WASTE_T,
            "cumulative_biogas_m3": QINGDAO_CUMULATIVE_BIOGAS_M3,
            "derived_reference_biogas_m3_tonne": coefficient,
            "warning": (
                "Retrospective Qingdao operating reference; not a Dongjiakou "
                "design yield."
            ),
        },
        "food_waste_transfer_function": {
            "equation": (
                f"V_biogas_reference = M_verified_food_waste * {coefficient:.10f} m3/t"
            ),
            "illustrative_cases": [
                {"feed_tonnes_day": feed, **food_waste_reference(feed)}
                for feed in ILLUSTRATIVE_FEED_TPD
            ],
            "energy_output": (
                "UNKNOWN until CH4 fraction, flare/use split and conversion "
                "efficiency are measured"
            ),
        },
        "wastewater_transfer_function": {
            "theoretical_methane_ceiling_STP_m3_per_kg_biodegradable_COD_removed": (
                THEORETICAL_CH4_M3_PER_KG_BCOD_STP
            ),
            "use_rule": (
                "theoretical ceiling only; requires measured eligible flow, COD, "
                "biodegradable fraction, COD removal and dissolved methane loss"
            ),
            "Node_001_input_values": UNKNOWN,
        },
        "compost_and_nutrient_outputs": {
            "compost_tonnes_year": UNKNOWN,
            "P_product_yield": UNKNOWN,
            "N_recovery": UNKNOWN,
            "reclaimed_water_m3_year": UNKNOWN,
        },
        "single_credit_rules": {
            "digestate_nutrient_mass": (
                "N/P mass may be routed to recovered fertilizer OR compost; the "
                "same mass cannot receive both credits."
            ),
            "reclaimed_water": (
                "Credited only when verified reuse displaces another water source."
            ),
            "seawater_derived_Mg": (
                "May be commodity OR nutrient-recovery reagent; one Mg mass "
                "cannot receive both credits."
            ),
            "biogas_energy": (
                "Receives energy credit only after measured gas quantity/"
                "composition and actual conversion/use are receipted."
            ),
        },
    }
