#!/usr/bin/env python3
"""Dongjiakou C01 Run 3 v0.2: compute facility transfer function."""
import argparse, json
HOURS=8760.0
PROCESS_GWH=39.446
PV_A=2.70619355
PV_B=2.917982611
EF=0.6191

def calc(it_kw, load_factor, pue):
    if it_kw < 0 or not 0 <= load_factor <= 1 or pue < 1:
        raise ValueError("it_kw>=0, load_factor in [0,1], pue>=1 required")
    it_gwh=it_kw/1000.0*HOURS/1000.0*load_factor
    facility=it_gwh*pue
    return {
      "IT_energy_GWh":it_gwh,
      "facility_energy_GWh":facility,
      "facility_fraction_of_2025_UF_RO":facility/PROCESS_GWH,
      "PV_A_annual_energy_ratio":PV_A/facility if facility else None,
      "PV_B_annual_energy_ratio":PV_B/facility if facility else None,
      "grid_only_location_CO2_t_using_2023_Shandong_average":facility*1e6*EF/1000.0,
      "IT_heat_first_law_upper_bound_GWhth":it_gwh,
      "useful_heat_credit_GWhth":0.0
    }

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--it-kw",type=float,required=True)
    p.add_argument("--load-factor",type=float,default=1.0)
    p.add_argument("--pue",type=float,required=True)
    a=p.parse_args()
    out=calc(a.it_kw,a.load_factor,a.pue)
    out["guardrails"]=[
      "PUE input is a scenario unless measured at Node-001.",
      "PV annual energy ratio is not hourly matching or self-sufficiency.",
      "Existing S01 PV cannot be credited twice.",
      "LLM actuator authority is NONE.",
      "Useful heat credit stays zero until thermal sink receipts exist."
    ]
    print(json.dumps(out,indent=2))
