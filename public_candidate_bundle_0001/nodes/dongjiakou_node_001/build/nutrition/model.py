"""NUT01: explicitly hypothetical, non-crediting population sensitivities."""
import math
import json
from pathlib import Path
from copy import deepcopy

FRACTIONS = ("adoption", "adherence", "joint_eligible_prevalence", "correction_response",
             "protein_fraction_dry", "theanine_fraction", "qualified_staff_fraction", "moisture_fraction")
NONNEGATIVE = ("population", "days", "protein_target_g", "creatine_g_day",
               "theanine_material_g_day", "minutes_saved_day", "daily_price_cny",
               "displaced_spend_cny", "equipment_servings_day", "staff_hours_day",
               "hours_per_serving", "stock_servings", "emergency_people", "emergency_days",
               "energy_kwh_serving", "substrate_kg_serving", "grid_kgco2_kwh",
               "substrate_kgco2_kg", "other_kgco2_serving", "displaced_kgco2_serving")
KEYS = set(FRACTIONS + NONNEGATIVE + ("task_output_effect", "creatine_test_effect",
    "creatine_eligible_fraction", "ration_qualified", "shelf_life_qualified"))
KEYS.add("creatine_eligible_fraction")
UNKNOWN = "UNKNOWN"

def validate(config):
    if set(config) != {"scenario_id", "scenario_kind", "inputs"}:
        raise ValueError("Expected scenario_id, scenario_kind, inputs")
    if config["scenario_kind"] not in ("LOCAL_UNKNOWN", "HYPOTHETICAL_SENSITIVITY"):
        raise ValueError("Measured finished-product efficacy is not supported")
    if not isinstance(config["scenario_id"], str) or not config["scenario_id"]:
        raise ValueError("scenario_id required")
    inputs = config["inputs"]
    units = json.loads((Path(__file__).parent / "units.json").read_text())
    sources = {r["source_id"] for r in json.loads((Path(__file__).parent / "source_register.json").read_text())["sources"]}
    if set(inputs) != KEYS:
        raise ValueError(f"Input keys differ: {set(inputs) ^ KEYS}")
    for name, record in inputs.items():
        if set(record) != {"value", "unit", "evidence_class", "source_ids", "basis"}:
            raise ValueError(f"{name}: provenance fields required")
        value = record["value"]
        if record["unit"] != units[name]:
            raise ValueError(f"{name}: incorrect unit")
        if not all(s in sources for s in record["source_ids"]):
            raise ValueError(f"{name}: unregistered source")
        if name in ("task_output_effect", "creatine_test_effect", "joint_eligible_prevalence", "correction_response") and value is not None and record["evidence_class"] != "SENSITIVITY":
            raise ValueError("No regional effect or response receipt; use SENSITIVITY")
        if not record["unit"] or not record["basis"] or not isinstance(record["source_ids"], list):
            raise ValueError(f"{name}: incomplete provenance")
        if value is None:
            if record["evidence_class"] != "UNKNOWN":
                raise ValueError(f"{name}: null must be UNKNOWN")
            continue
        if name in ("ration_qualified", "shelf_life_qualified"):
            if type(value) is not bool:
                raise ValueError("Qualification must be boolean or unknown")
            if value and config["scenario_kind"] != "HYPOTHETICAL_SENSITIVITY":
                raise ValueError("No local qualification receipt exists")
        else:
            if type(value) not in (int, float) or not math.isfinite(value):
                raise ValueError(f"{name}: finite number required")
            if name in NONNEGATIVE and value < 0:
                raise ValueError(f"{name}: negative input")
            if name in FRACTIONS + ("creatine_eligible_fraction",) and not 0 <= value <= 1:
                raise ValueError(f"{name}: fraction outside [0,1]")
            if name in ("task_output_effect", "creatine_test_effect") and not -1 <= value <= 1:
                raise ValueError("Effect outside [-1,1]")
            if name == "hours_per_serving" and value == 0:
                raise ValueError("Labor denominator must be positive")
            if name == "protein_fraction_dry" and value == 0:
                raise ValueError("Protein fraction must be positive")
            if name == "moisture_fraction" and value == 1:
                raise ValueError("Moisture fraction must be less than one")
        if record["evidence_class"] not in ("UNKNOWN", "SENSITIVITY", "PROPOSED",
                "OFFICIAL_REGULATORY_SOURCE", "MEASURED_STUDY", "MODELED"):
            raise ValueError("Unsupported evidence class")
        if record["evidence_class"] in ("MEASURED_STUDY", "OFFICIAL_REGULATORY_SOURCE") and not record["source_ids"]:
            raise ValueError("Evidence reference required")
        if config["scenario_kind"] == "LOCAL_UNKNOWN" and name in (
                "population", "adoption", "adherence", "joint_eligible_prevalence",
                "correction_response", "task_output_effect", "creatine_test_effect",
                "creatine_eligible_fraction"):
            raise ValueError(f"{name}: no local measured receipt; keep null")
    return config

def run(config):
    validate(config)
    values = {k: v["value"] for k, v in config["inputs"].items()}
    def calc(names, fn):
        args = [values[n] for n in names]
        return UNKNOWN if any(v is None for v in args) else fn(*args)
    users = calc(("population", "adoption", "adherence"), lambda p,a,h:p*a*h)
    uplift = calc(("adoption", "adherence", "joint_eligible_prevalence",
                   "correction_response", "task_output_effect"), lambda a,h,p,r,e:a*h*p*r*e*100)
    responders = calc(("population","adoption","adherence","joint_eligible_prevalence",
                       "correction_response"), lambda n,a,h,p,r:n*a*h*p*r)
    demand = UNKNOWN if users == UNKNOWN else users
    capacity = calc(("equipment_servings_day","staff_hours_day","hours_per_serving",
                     "qualified_staff_fraction"), lambda e,h,t,q:min(e,h*q/t))
    delivered = UNKNOWN if UNKNOWN in (demand,capacity) else min(demand,capacity)
    costs = calc(("daily_price_cny","displaced_spend_cny","days"), lambda p,d,t:(p-d)*t)
    theanine = calc(("theanine_material_g_day","theanine_fraction"),lambda m,f:m*f*1000)
    return {
        "module":"NUT01", "classification":"CANDIDATE_NON_CANON",
        "scenario_id":config["scenario_id"], "scenario_kind":config["scenario_kind"],
        "inputs":deepcopy(config["inputs"]),
        "projected_metrics_evidence_class":"SENSITIVITY",
        "realized_credit":0, "deployment":False, "finished_product_efficacy":UNKNOWN,
        "strain":"Fusarium compactum MM-135",
        "protein_ingredient_dry_g":calc(("protein_target_g","protein_fraction_dry"),lambda p,f:p/f),
        "protein_ingredient_as_is_g":calc(("protein_target_g","protein_fraction_dry","moisture_fraction"),
            lambda p,f,m:p/(f*(1-m))),
        "theanine_active_mg":theanine,
        "tea_material_limit_check":UNKNOWN if values["theanine_material_g_day"] is None
            else values["theanine_material_g_day"] <= 0.4,
        "adherent_equivalent_people":users,
        "hypothetical_correction_responders":responders,
        "conditional_population_task_output_change_percent":uplift,
        "creatine_test_change_percent_in_eligible_users":calc(("creatine_test_effect",),lambda e:100*e),
        "creatine_eligible_adherent_people":calc(("population","adoption","adherence",
            "creatine_eligible_fraction"),lambda n,a,h,f:n*a*h*f),
        "combined_population_gain":UNKNOWN,
        "aggregation_rule":"One joint inadequacy cohort; no iron/zinc/D/protein sum. Creatine test endpoint is separate. No GDP conversion.",
        "gross_convenience_hours_year":calc(("population","adoption","adherence","minutes_saved_day","days"),
            lambda n,a,h,m,t:n*a*h*m*t/60),
        "household_incremental_cny_per_adherent_year":costs,
        "operational_capacity_servings_day":capacity,
        "capacity_limited_adherent_equivalent_people":delivered,
        "capacity_caveat":"Health scenarios assume supply. Do not apply them operationally unless delivered demand and safety gates close.",
        "supplement_stock_person_days":calc(("stock_servings",),lambda s:s),
        "emergency_complete_ration_service_days":UNKNOWN,
        "emergency_supplement_days_per_person":calc(("stock_servings","emergency_people"),
            lambda s,p:UNKNOWN if p == 0 else s/p),
        "emergency_rule":"Supplement inventory is not complete ration, clinical resilience, or aerospace qualification.",
        "gross_kgco2_per_serving":calc(("energy_kwh_serving","grid_kgco2_kwh",
            "substrate_kg_serving","substrate_kgco2_kg","other_kgco2_serving"),
            lambda e,g,s,f,o:e*g+s*f+o),
        "hypothetical_net_kgco2_per_serving":calc(("energy_kwh_serving","grid_kgco2_kwh",
            "substrate_kg_serving","substrate_kgco2_kg","other_kgco2_serving","displaced_kgco2_serving"),
            lambda e,g,s,f,o,d:e*g+s*f+o-d),
        "net_environmental_credit":UNKNOWN,
        "shelf_life_years":UNKNOWN, "flavor_acceptance":UNKNOWN,
        "gates":["Chinese form/source/category/dose audit", "MM-135 supplier identity and CoA",
                 "mycotoxin/residual nucleic acid and safety tests", "sensory panel",
                 "finished product controlled study", "packaging and stability validation",
                 "food-grade substrate and utility audit", "local prevalence and uptake survey"],
    }

