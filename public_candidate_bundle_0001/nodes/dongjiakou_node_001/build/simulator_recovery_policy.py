"""Additive v0.11 policy wrapper preserving previous simulator outputs."""
import argparse
import json
from pathlib import Path
from simulator_wellbeing import compose as wellbeing_compose
from wellbeing.recovery_policy_v011 import run

def compose(nutrition_config,qol_config,policy_config):
    result=wellbeing_compose(nutrition_config,qol_config)
    result["candidate_extensions"]["RECOVERY_POLICY_v0.11"]=run(policy_config)
    return result

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("scenarios",nargs=3,type=Path)
    a=p.parse_args()
    print(json.dumps(compose(*(json.loads(x.read_text()) for x in a.scenarios)),indent=2,allow_nan=False))
