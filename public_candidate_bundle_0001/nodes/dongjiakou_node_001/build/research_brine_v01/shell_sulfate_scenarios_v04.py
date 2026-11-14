#!/usr/bin/env python3
"""Screen shell calcium + brine sulfate options, synthetic and zero realized credit.
Outputs physical upper bounds, NOT qualified gypsum, industrial feasibility or acid profit.
"""
import json,sys
from pathlib import Path
CA=40.078;SO4=96.06;CACO3=100.087;GYPS=172.171;HCL=36.461;H2SO4=98.079;CO2=44.01
def run(d):
    q=d["brine_m3_day"];days=d["days_y"]
    ca=q*d["calcium_mg_l"]*days/1e6
    sulfate=q*d["sulfate_mg_l"]*days/1e6
    assert ca>=0 and sulfate>=0 and days>0
    old_moles=min(ca/CA,sulfate/SO4) # kiloton-scale mole ratios in t / g mol^-1
    direct=old_moles*GYPS*d["direct_capture"]
    sulfate_remaining=sulfate-direct*SO4/GYPS
    shell=d["shell_wet_t_y"]*d["shell_dry_fraction"]*d["shell_caco3_mass_fraction"]
    assert min(shell,sulfate_remaining)>=0 and 0<=d["direct_capture"]<=1
    routes=[]
    for name,details in d["routes"].items():
        cap=details["calcium_activation_fraction"]; sep=details["gypsum_capture_fraction"]
        assert 0<=cap<=1 and 0<=sep<=1
        moles=min(shell*cap/CACO3,sulfate_remaining/SO4)
        # Recovery feed can originate from brine sulfate or sulfuric acid. Separate explicitly.
        if details["sulfate_source"]=="brine":
            new_gyp=moles*GYPS*sep
            acid_imported_s=0.0
        elif details["sulfate_source"]=="sulfuric_acid":
            new_gyp=(shell*cap/CACO3)*GYPS*sep
            acid_imported_s=new_gyp*H2SO4/GYPS
        else:raise ValueError("Unsupported sulfate origin")
        hcl_req=(moles*2*HCL) if details["activation"]=="hcl" else 0
        sulfuric_req=acid_imported_s if details["activation"]=="sulfuric_acid" else 0
        co2_generated=(shell*cap/CACO3)*CO2
        # Mandatory upper bound only: actual process pH, solubility and salts may forbid this yield.
        routes.append({"route":name,"additional_gypsum_t_y":round(new_gyp,2),
           "total_gypsum_t_y":round(direct+new_gyp,2),
           "brine_origin_additional_sulfate_t_y":round(new_gyp*SO4/GYPS if details["sulfate_source"]=="brine" else 0,2),
           "hcl_stoichiometric_t_y":round(hcl_req,2),
           "h2so4_input_t_y":round(sulfuric_req,2),
           "co2_released_upper_t_y":round(co2_generated,2),
           "new_sulfur_from_h2so4_recycling_t_y":0,
           "process_capex_and_cost_unknown":True,
           "qualification_verified":False})
    return {"status":"SYNTHETIC_NON_CANON_REALIZED_ZERO","input_brine_sulfate_t_y":round(sulfate,2),
        "input_brine_calcium_t_y":round(ca,2),"direct_gypsum_t_y":round(direct,2),
        "sulfate_remaining_after_direct_t_y":round(sulfate_remaining,2),
        "shell_caco3_t_y":round(shell,2),"routes":routes,
        "warnings":["Stoichiometric ceilings only, not chemical equilibrium predictions.",
         "Sulfuric acid route counts acid-origin sulfate, not recovered brine sulfate.",
         "Acid dosing and CO2 evolved need independent health/safety/air permits.",
         "No internal market margins, physical receipts or customs displacement claimed."]}
if __name__=="__main__":
    p=Path(sys.argv[1] if len(sys.argv)>1 else Path(__file__).with_name("shell_sulfate_synthetic_v04.json"))
    print(json.dumps(run(json.loads(p.read_text())),indent=2))
