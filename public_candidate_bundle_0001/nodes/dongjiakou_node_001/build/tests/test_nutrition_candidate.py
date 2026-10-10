import json
from copy import deepcopy
from pathlib import Path
import pytest
from nutrition.model import run
from simulator_nutrition import compose
from models.current_state import run as baseline
from jsonschema import validate
ROOT = Path(__file__).parents[1]
def scenario(name="central"):
    return json.loads((ROOT / "nutrition" / "examples" / (name + ".json")).read_text())

def test_all_example_schemas_and_models_agree():
    schema = json.loads((ROOT / "nutrition" / "scenario.schema.json").read_text())
    for path in (ROOT / "nutrition" / "examples").glob("*.json"):
        config = json.loads(path.read_text())
        validate(config, schema)
        run(config)

def test_unknown_local_never_becomes_zero():
    result = run(scenario("local_unknown"))
    assert result["conditional_population_task_output_change_percent"] == "UNKNOWN"
    assert result["protein_ingredient_as_is_g"] == "UNKNOWN"
    assert result["realized_credit"] == 0
    assert result["emergency_complete_ration_service_days"] == "UNKNOWN"

def test_central_arithmetic_is_explicitly_hypothetical():
    r = run(scenario())
    assert r["adherent_equivalent_people"] == 4000
    assert r["hypothetical_correction_responders"] == 360
    assert r["conditional_population_task_output_change_percent"] == pytest.approx(.108)
    assert r["gross_convenience_hours_year"] == pytest.approx(121666.6666667)
    assert r["protein_ingredient_dry_g"] == 60
    assert r["protein_ingredient_as_is_g"] == "UNKNOWN"
    assert r["theanine_active_mg"] == pytest.approx(80)
    assert r["combined_population_gain"] == "UNKNOWN"

def test_adverse_and_zero_effects_preserved():
    assert run(scenario("adverse"))["conditional_population_task_output_change_percent"] < 0
    assert run(scenario("low"))["conditional_population_task_output_change_percent"] == 0

def test_baseline_preserved_exactly():
    assert compose(scenario())["baseline"] == baseline()
    assert baseline()["realized_credit"] == 0

@pytest.mark.parametrize("key,value", [("adoption",1.1),("adherence",-1),
    ("population",True),("task_output_effect",float("nan")),
    ("protein_fraction_dry",0),("moisture_fraction",1),("hours_per_serving",0)])
def test_invalid_values_fail(key,value):
    x=scenario();x["inputs"][key]["value"]=value
    with pytest.raises(ValueError):run(x)

def test_units_not_ignored():
    x=scenario();x["inputs"]["protein_target_g"]["unit"]="mg/day"
    with pytest.raises(ValueError):run(x)

def test_no_effect_promoted_to_measured():
    x=scenario();x["inputs"]["task_output_effect"]["evidence_class"]="MEASURED_STUDY"
    x["inputs"]["task_output_effect"]["source_ids"]=["CREATINE3"]
    with pytest.raises(ValueError):run(x)

def test_no_local_prevalence_assumed():
    x=scenario("local_unknown");x["inputs"]["adoption"]["value"]=.5
    x["inputs"]["adoption"]["evidence_class"]="SENSITIVITY"
    with pytest.raises(ValueError):run(x)

def test_mass_basis_conversion():
    x=scenario();x["inputs"]["moisture_fraction"].update(value=.08,evidence_class="SENSITIVITY")
    assert run(x)["protein_ingredient_as_is_g"]==pytest.approx(65.2173913043)
    x["inputs"]["protein_fraction_dry"]["value"]=28/38.2
    assert run(x)["protein_ingredient_dry_g"]==pytest.approx(40.9285714286)

def test_household_and_capacity_are_separate():
    x=scenario()
    for key,value in {"daily_price_cny":10,"displaced_spend_cny":3,
        "equipment_servings_day":3000,"staff_hours_day":100,
        "hours_per_serving":.02,"qualified_staff_fraction":.5}.items():
        x["inputs"][key].update(value=value,evidence_class="SENSITIVITY")
    r=run(x)
    assert r["household_incremental_cny_per_adherent_year"]==2555
    assert r["operational_capacity_servings_day"]==2500
    assert r["capacity_limited_adherent_equivalent_people"]==2500
    assert r["realized_credit"]==0

def test_supplement_stock_does_not_qualify_ration():
    x=scenario()
    for key,value in {"stock_servings":20000,"emergency_people":1000,
        "ration_qualified":True,"shelf_life_qualified":True}.items():
        x["inputs"][key].update(value=value,evidence_class="SENSITIVITY")
    r=run(x)
    assert r["emergency_supplement_days_per_person"]==20
    assert r["emergency_complete_ration_service_days"]=="UNKNOWN"

def test_sources_required_and_unknown_is_loud():
    x=scenario();x["inputs"]["creatine_g_day"]["source_ids"]=[]
    with pytest.raises(ValueError):run(x)
    x=scenario();x["inputs"]["population"]["value"]=None
    with pytest.raises(ValueError):run(x)

