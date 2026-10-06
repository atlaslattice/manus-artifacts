#!/usr/bin/env python3
"""Dongjiakou C01 compute module: parametric energy/carbon/heat accounting."""
import argparse, json
HOURS=8760.0
PROCESS_GWH=39.446
GRID_KGCO2_KWH=0.6191
PV_A_GWH=2.70619355
PV_B_GWH=2.917982611
def calc(it_mw, load_factor, pue):
    if it_mw < 0 or not 0 <= load_factor <= 1 or pue < 1:
        raise ValueError("Require it_mw>=0, load_factor in [0,1], PUE>=1")
    it_gwh=it_mw*HOURS*load_factor/1000.0
    facility_gwh=it_gwh*pue
    return {
      "IT_energy_GWh":it_gwh,
      "facility_energy_GWh":facility_gwh,
      "facility_energy_fraction_of_2025_UF_RO":facility_gwh/PROCESS_GWH,
      "location_average_CO2_t_using_2023_Shandong_factor":facility_gwh*1e6*GRID_KGCO2_KWH/1000.0,
      "S01_A_annual_PV_energy_equivalence_fraction":min(1.0,PV_A_GWH/facility_gwh) if facility_gwh else 0.0,
      "S01_B_annual_PV_energy_equivalence_fraction":min(1.0,PV_B_GWH/facility_gwh) if facility_gwh else 0.0,
      "useful_IT_heat_upper_bound_GWhth":it_gwh
    }
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--it-mw",type=float,required=True)
    p.add_argument("--load-factor",type=float,required=True)
    p.add_argument("--pue",type=float,required=True)
    a=p.parse_args()
    out=calc(a.it_mw,a.load_factor,a.pue)
    out["guardrails"]=[
      "Existing S01 PV cannot be credited simultaneously to desalination and compute.",
      "Annual PV equivalence is not direct hourly matching.",
      "No AI operational savings are credited without measured before/after receipts.",
      "LLMs have no direct actuator authority."
    ]
    print(json.dumps(out,indent=2))