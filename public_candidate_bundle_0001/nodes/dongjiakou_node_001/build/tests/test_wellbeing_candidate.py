import json
from pathlib import Path
import pytest
from wellbeing.model import run
from simulator_wellbeing import compose
from simulator_nutrition import compose as original
from wellbeing.funding import evaluate
ROOT=Path(__file__).parents[1]
def scenario(local=False):
    name="local_unknown" if local else "shift_capacity_sensitivity"
    return json.loads((ROOT/"wellbeing"/"examples"/(name+".json")).read_text())

def test_local_unknown_cohorts_and_capacity():
    r=run(scenario(True))
    assert all(c["population"]=="UNKNOWN" for c in r["cohorts"])
    assert all(s["capacity_participant_sessions_day"]=="UNKNOWN" for s in r["operations"]["services"].values())
    assert all(e["scenario_endpoint_change_percent_within_cohort"]=="UNKNOWN" for e in r["effects_by_cohort"])
    assert r["population_combined_benefit"]=="UNKNOWN"
    assert r["realized_credit"]==0

def test_6_2_6_is_14h_span_60h_week_not_8_8_8():
    c=run(scenario())["cohorts"][1]
    assert c["on_site_span_hours_day"]==14
    assert c["weekly_active_work_hours"]==60
    assert c["weekly_on_site_span_hours"]==70
    assert c["above_40h_standard_reference"] is True
    assert c["personal_hours_including_obligations"]==2
    assert c["discretionary_hours_after_commute_and_care"]==pytest.approx(-1/3)
    assert c["time_budget_feasible"] is False
    assert c["actual_sleep_hours_day"]=="UNKNOWN"

def test_new_launcher_preserves_nutrition_and_baseline():
    n=json.loads((ROOT/"nutrition"/"examples"/"central.json").read_text())
    r=compose(n,scenario(True));o=original(n)
    assert r["baseline"]==o["baseline"]
    assert r["candidate_extensions"]["NUT01"]==o["candidate_extensions"]["NUT01"]
    assert r["candidate_extensions"]["shared_operations_boundary"]["nutrition_supply_capacity_participant_sessions_day"]=="UNKNOWN"

def test_workweek_ceiling():
    x=scenario();x["cohorts"][0]["workdays_week"]=6
    with pytest.raises(ValueError):run(x)

def test_paid_leave_floor_never_reduces_statutory_entitlement():
    r=run(scenario())
    assert r["cohorts"][0]["candidate_paid_leave_working_days"]==10
    assert r["cohorts"][0]["candidate_paid_leave_five_day_weeks"]==2
    assert r["cohorts"][1]["candidate_paid_leave_working_days"]==15
    assert r["cohorts"][1]["candidate_paid_leave_five_day_weeks"]==3
    assert r["cohorts"][1]["nominal_annual_attendance_days_reference"]==233
    assert run(scenario(True))["cohorts"][0]["candidate_paid_leave_working_days"]=="UNKNOWN"

def test_digital_access_not_conditioned_on_collection():
    x=scenario();x["digital_inclusion"]["access_conditioned_on_research_consent"]=True
    with pytest.raises(ValueError):run(x)
    x=scenario();x["digital_inclusion"]["personal_memory_export_to_research"]=True
    with pytest.raises(ValueError):run(x)
    r=run(scenario(True))["digital_inclusion"]
    assert r["actual_resident_access"]=="UNKNOWN"
    assert r["anonymization_verified"]=="UNKNOWN"
    assert r["annual_operating_and_amortized_cost_cny"]=="UNKNOWN"
    assert r["inputs"]["resident_price_cny"]==0

def test_cross_sector_forecast_never_pays_actual_benefits():
    x=scenario()["funding"]
    x["annual_benefits_cost_cny"]=40000;x["cost_evidence_class"]="SENSITIVITY"
    r=x["streams"][0];r["evidence_class"]="SENSITIVITY"
    r.update(gross_cash_savings_cny=100000,incremental_operating_cny=30000,
        maintenance_reserve_cny=10000,capital_renewal_cny=20000,existing_commitments_cny=10000)
    out=evaluate(x)
    assert out["projected_net_cash_after_existing_commitments_cny"]==30000
    assert out["projected_budget_margin_cny"]==-10000
    assert out["current_realized_available_cash_cny"]==0
    assert out["benefits_funded_from_verified_deployment_gains"] is False
    x["streams"].append(dict(r))
    with pytest.raises(ValueError):evaluate(x)

def test_no_realized_funding_credit_without_receipt():
    x=scenario()["funding"];x["streams"][0]["current_realized_funding_credit_cny"]=1
    with pytest.raises(ValueError):evaluate(x)

def test_shared_role_cannot_be_double_booked():
    x=scenario()
    x["operations"]["services"][1]["requirements"][0]["role_id"]="movement_instructor"
    x["operations"]["services"][1]["requirements"][0]["allocated_qualified_hours_day"]=5
    with pytest.raises(ValueError):run(x)

def test_training_attendance_does_not_create_capacity():
    x=scenario(True);x["operations"]["roles"]["movement_instructor"]["training_pipeline"]["candidate_count"]=1000
    assert run(x)["operations"]["services"]["tai_chi"]["capacity_participant_sessions_day"]=="UNKNOWN"

def test_closed_gate_delivers_no_service():
    x=scenario();x["operations"]["services"][0]["safe_operation_gate"]=False
    r=run(x)
    assert r["operations"]["services"]["tai_chi"]["capacity_participant_sessions_day"]==0
    assert r["effects_by_cohort"][0]["capacity_limited_participant_sessions_day"]==0
    assert r["effects_by_cohort"][0]["scenario_endpoint_change_percent_within_cohort"]=="UNKNOWN"

def test_staff_bottleneck_limits_service():
    x=scenario();r=run(x)
    assert r["operations"]["services"]["tai_chi"]["capacity_participant_sessions_day"]==40
    assert r["effects_by_cohort"][0]["capacity_limited_participant_sessions_day"]==40

def test_capacity_shares_cannot_exceed_one():
    x=scenario();x["effects"][1]["capacity_share"]=.8
    with pytest.raises(ValueError):run(x)

def test_wrong_study_endpoint_and_transfer_rejected():
    x=scenario();x["effects"][0]["endpoint"]="workforce_productivity"
    with pytest.raises(ValueError):run(x)
    x=scenario();x["effects"][0]["transfer_status"]="MEASURED"
    with pytest.raises(ValueError):run(x)

def test_study_population_attached_to_each_effect():
    r=run(scenario())
    assert "high-fall-risk" in r["effects_by_cohort"][0]["source_evidence"]["population"].lower()
    assert "risk factor" in r["effects_by_cohort"][1]["source_evidence"]["population"]
    assert r["population_combined_benefit"]=="UNKNOWN"

@pytest.mark.parametrize("field,value", [("population",True),("work_hours_day",float("nan")),("sleep_opportunity_hours_day",-1)])
def test_bad_values(field,value):
    x=scenario();x["cohorts"][0][field]=value
    with pytest.raises(ValueError):run(x)

def test_hypothetical_effect_remains_cohort_specific_and_capacity_limited():
    x=scenario();e=x["effects"][0];e["relative_effect"]=-.1;e["effect_evidence_class"]="SENSITIVITY"
    r=run(x)
    assert r["effects_by_cohort"][0]["scenario_endpoint_change_percent_within_cohort"]==pytest.approx(-.8)
    assert r["population_combined_benefit"]=="UNKNOWN"
    assert r["realized_credit"]==0

