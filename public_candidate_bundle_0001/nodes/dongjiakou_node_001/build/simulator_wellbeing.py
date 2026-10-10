"""Additive NUT01 + QOL01/OPS01 launcher; existing launchers remain unchanged."""
import argparse
import json
from pathlib import Path
from simulator_nutrition import compose as nutrition_compose
from wellbeing.model import run
def compose(nutrition_config, qol_config):
    result=nutrition_compose(nutrition_config)
    result["candidate_extensions"]["QOL01"]=run(qol_config)
    supply=result["candidate_extensions"]["QOL01"]["operations"]["services"].get("nutrition_supply")
    result["candidate_extensions"]["shared_operations_boundary"]={
        "nutrition_supply_capacity_participant_sessions_day":supply["capacity_participant_sessions_day"] if supply else "UNKNOWN",
        "nutrition_health_effects":"NUT01 sensitivities assume supply; do not treat as delivered outcomes until OPS01 and product gates close.",
        "realized_credit":0}
    return result
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("nutrition_scenario",type=Path)
    p.add_argument("qol_scenario",type=Path)
    a=p.parse_args()
    print(json.dumps(compose(json.loads(a.nutrition_scenario.read_text()),
        json.loads(a.qol_scenario.read_text())),indent=2,allow_nan=False))

