"""Unit tests for the deterministic Node-001 models.

Each test asserts a modelling *invariant*, not merely an arithmetic result.
"""

from __future__ import annotations

import pytest

from models import run0, run1_solar, run2_hydro, run3_compute, run4a_biometabolic, s02_bess
from models.common import UNKNOWN, UnknownPropagationError, is_unknown


# ---------------------------------------------------------------------------
# Run 0
# ---------------------------------------------------------------------------
def test_run0_baseline_per_u_coefficients():
    result = run0.baseline()
    coeff = result["coefficients_per_U"]
    assert coeff["annual_product_m3"] == 36_500_000.0
    assert coeff["annual_process_train_energy_GWh"] == pytest.approx(80.3)
    assert coeff["annual_chemical_cost_CNY_upper_bound"] == pytest.approx(5_475_000.0)


def test_run0_baseline_leaves_unknowns_unknown():
    result = run0.baseline()
    assert is_unknown(result["inputs"]["utilization_U"])
    assert is_unknown(result["inputs"]["whole_site_SEC_kWh_m3"])
    assert is_unknown(result["inputs"]["plant_effective_tariff_CNY_kWh"])
    assert "U1_reference_not_operating_claim" in result
    assert "evaluated_at_U" not in result


def test_run0_baseline_at_stated_utilization():
    result = run0.baseline(utilization=0.4912328767)
    evaluated = result["evaluated_at_U"]
    assert evaluated["annual_product_m3"] == pytest.approx(17_930_000.0, rel=1e-9)
    assert evaluated["annual_process_train_energy_GWh"] == pytest.approx(39.446, rel=1e-9)
    assert "U1_reference_not_operating_claim" not in result


def test_run0_baseline_rejects_out_of_range_utilization():
    with pytest.raises(ValueError):
        run0.baseline(utilization=1.4)


def test_run0_retrofit_credits_are_all_zero():
    credits = run0.baseline()["retrofit_credit"]
    assert set(credits.values()) == {0}


def test_run0_reject_equivalent_is_not_named_discharge():
    """The modelled residual must never be labelled a discharge quantity."""
    result = run0.operating_2025()
    for case in result["mass_balance_using_reported_technology_recovery_range"].values():
        assert "annual_reject_equivalent_m3" in case
        assert not any("discharge" in key for key in case)
        assert not any("marine" in key for key in case)


def test_run0_operating_2025_derived_values():
    result = run0.operating_2025()
    assert result["derived_utilization_U"] == pytest.approx(0.4912328767, rel=1e-8)
    assert result["derived_process_train_energy_GWh"] == pytest.approx(39.446)
    assert result["derived_annual_chemical_cost_CNY_upper_bound"] == pytest.approx(2_689_500.0)


def test_run0_current_electricity_cost_stays_unknown():
    economics = run0.operating_2025()["economics"]
    assert is_unknown(economics["current_effective_electricity_tariff_CNY_kWh"])
    assert is_unknown(economics["current_electricity_cost_CNY"])
    assert economics["historical_2018_2020_tariff_CNY_kWh"] == pytest.approx(0.555)


def test_utilization_fraction_rejects_negative_volume():
    with pytest.raises(ValueError):
        run0.utilization_fraction(-1.0)


# ---------------------------------------------------------------------------
# Run 1
# ---------------------------------------------------------------------------
def test_run1_active_area_and_yield():
    assert run1_solar.active_module_area_m2() == pytest.approx(10_484.592, rel=1e-12)
    assert run1_solar.local_yield_kwh_per_kwp_year() == pytest.approx(1122.223823, rel=1e-8)


def test_run1_current_savings_stay_unknown():
    cases = run1_solar.run()["cases"]
    for case in cases.values():
        assert is_unknown(case["current_cost_saving_CNY"])


def test_run1_roof_structure_and_interconnection_stay_unknown():
    site = run1_solar.run()["site_inputs"]
    assert is_unknown(site["roof_structural_suitability"])
    assert is_unknown(site["interconnection_limit"])


def test_run1_sea_shield_case_exceeds_base_case():
    cases = run1_solar.run()["cases"]
    assert (
        cases["S01_B_SEA_SHIELD"]["annual_generation_GWh"]
        > cases["S01_A"]["annual_generation_GWh"]
    )


def test_run1_rejects_impossible_efficiency():
    with pytest.raises(ValueError):
        run1_solar.case("BAD", 1.5)


# ---------------------------------------------------------------------------
# Run 2
# ---------------------------------------------------------------------------
def test_run2_credit_is_zero_without_a_head_receipt():
    baseline = run2_hydro.run()["baseline"]
    assert baseline["hydro_credit_GWh_year"] == 0
    assert is_unknown(baseline["H_available_m"])


def test_run2_energy_scales_linearly_with_head():
    one = run2_hydro.hydro_energy_gwh(run2_hydro.STREAM_VOLUME_M3_YEAR, 10.0, 0.8)
    five = run2_hydro.hydro_energy_gwh(run2_hydro.STREAM_VOLUME_M3_YEAR, 50.0, 0.8)
    assert five == pytest.approx(one * 5.0)


def test_run2_ideal_case_at_unit_efficiency():
    ideal = run2_hydro.hydro_energy_gwh(run2_hydro.STREAM_VOLUME_M3_YEAR, 1.0, 1.0)
    assert ideal == pytest.approx(0.0488425651, rel=1e-8)


def test_run2_pump_head_is_explicitly_excluded():
    excluded = run2_hydro.run()["excluded_head"]
    assert excluded["status"] == "MOTOR_SUPPLIED_NOT_RECOVERABLE"
    assert "400-630" == excluded["SWRO_pump_head_m"]


def test_run2_rejects_negative_head():
    with pytest.raises(ValueError):
        run2_hydro.hydro_energy_gwh(1_000_000.0, -1.0, 0.8)


# ---------------------------------------------------------------------------
# Run 3
# ---------------------------------------------------------------------------
def test_run3_it_energy_uses_the_8760_convention():
    assert run3_compute.it_energy_gwh(100.0, 1.0) == pytest.approx(0.876)
    assert run3_compute.it_energy_gwh(250.0, 1.0) == pytest.approx(2.19)
    assert run3_compute.it_energy_gwh(1000.0, 1.0) == pytest.approx(8.76)


def test_run3_facility_energy_enforces_the_pue_floor():
    assert run3_compute.facility_energy_gwh(250.0, 1.0, 1.25) == pytest.approx(2.7375)
    with pytest.raises(ValueError):
        run3_compute.facility_energy_gwh(250.0, 1.0, 0.95)


def test_run3_four_tiers_with_expected_roles():
    tiers = run3_compute.run()["tiers"]
    assert [t["IT_capacity_kW"] for t in tiers] == [100.0, 250.0, 500.0, 1000.0]
    assert tiers[0]["deployment_role"] == "recommended first commissioning tier"
    assert "earned expansion tier" in tiers[1]["deployment_role"]
    assert "gated" in tiers[2]["deployment_role"]


def test_run3_compute_is_not_an_energy_source():
    result = run3_compute.run()["result"]
    assert result["C01_is_energy_source"] is False
    assert result["C01_net_positive"] == "NOT_PROVEN"


def test_run3_useful_heat_credit_is_zero():
    assert run3_compute.run()["heat_credit"]["baseline_useful_heat_GWhth"] == 0


def test_run3_useful_heat_refuses_to_assume_missing_factors():
    """A missing capture/temperature/temporal factor must not default to 1.0."""
    with pytest.raises(UnknownPropagationError):
        run3_compute.useful_heat_gwhth(250.0, 1.0)


def test_run3_useful_heat_with_all_factors_present():
    q = run3_compute.useful_heat_gwhth(
        250.0, 1.0, f_capture=0.5, f_temperature_match=0.8, f_temporal_match=0.5
    )
    assert q == pytest.approx(2.19 * 0.5 * 0.8 * 0.5)


def test_run3_heat_pump_savings_are_capped_by_cip_demand():
    saved = run3_compute.heat_pump_electric_saved_gwh(10.0, 4.0, 3.0)
    assert saved == pytest.approx(4.0 / 3.0)


def test_run3_s01_pv_is_not_incremental():
    assert run3_compute.run()["anti_double_counting"]["existing_S01_PV_is_incremental_to_node"] is False


def test_run3_net_delta_requires_numbers():
    with pytest.raises(UnknownPropagationError):
        run3_compute.node_net_electric_delta_gwh(UNKNOWN, 0.0, 0.0, 1.0)


def test_run3_reference_pue_is_labelled_a_reference():
    ref = run3_compute.run()["reference_scenario"]
    assert ref["PUE"] == 1.25
    assert ref["status"] == "SECTOR_POLICY_REFERENCE_NOT_NODE_RECEIPT"


# ---------------------------------------------------------------------------
# Run 4A
# ---------------------------------------------------------------------------
def test_run4a_every_baseline_credit_is_zero():
    credits = run4a_biometabolic.run()["baseline_credit"]
    numeric = {k: v for k, v in credits.items() if k != "reason"}
    assert set(numeric.values()) == {0}


def test_run4a_reference_coefficient():
    assert run4a_biometabolic.reference_biogas_m3_per_tonne() == pytest.approx(
        20.2307692308, rel=1e-9
    )


def test_run4a_energy_output_stays_unknown():
    case = run4a_biometabolic.food_waste_reference(10.0)
    assert is_unknown(case["energy_credit"])
    assert case["reference_biogas_m3_year"] == pytest.approx(73_842.3076923, rel=1e-8)


def test_run4a_wastewater_ceiling_is_a_ceiling_not_a_yield():
    result = run4a_biometabolic.wastewater_methane_ceiling(1000.0, 5000.0, 0.6, 0.9)
    assert result["theoretical_CH4_ceiling_m3_day_STP"] == pytest.approx(
        result["biodegradable_COD_removed_kg_day"] * 0.35
    )
    assert "not plant yield" in result["warning"]


def test_run4a_single_credit_rules_are_declared():
    rules = run4a_biometabolic.run()["single_credit_rules"]
    assert "cannot receive both credits" in rules["digestate_nutrient_mass"]
    assert "cannot receive both credits" in rules["seawater_derived_Mg"]
    assert "displaces another water source" in rules["reclaimed_water"]


def test_run4a_rejects_out_of_range_fractions():
    with pytest.raises(ValueError):
        run4a_biometabolic.wastewater_methane_ceiling(1000.0, 5000.0, 1.5, 0.9)


# ---------------------------------------------------------------------------
# S02
# ---------------------------------------------------------------------------
def test_s02_baseline_credit_is_zero():
    assert s02_bess.run()["baseline_credit"] == 0


def test_s02_average_solar_energy_per_day():
    result = s02_bess.run()["average_solar_energy_MWh_day"]
    assert result["A"] == pytest.approx(7.414228904, rel=1e-8)
    assert result["B"] == pytest.approx(7.994472907, rel=1e-8)


def test_s02_equivalence_is_labelled_as_equivalence():
    guardrails = " ".join(s02_bess.run()["guardrails"])
    assert "not an optimum" in guardrails
    assert "No BESS benefit is credited" in guardrails


def test_s02_requires_time_series_data():
    required = s02_bess.run()["required_first_data"]
    assert "hourly PV AC output" in required
    assert "hourly plant load" in required
