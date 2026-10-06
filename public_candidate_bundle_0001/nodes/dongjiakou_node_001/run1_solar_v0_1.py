#!/usr/bin/env python3
"""Dongjiakou Node-001 Run 1 — rooftop solar technical sensitivity."""
import json

ROOF_M2=17474.32
ACTIVE_COVERAGE=0.60
LOCAL_REFERENCE_MWP=12.4956
LOCAL_REFERENCE_MWH_YEAR=14022.86
PROCESS_ENERGY_2025_GWH=39.446
SHANDONG_GRID_FACTOR_KGCO2_KWH=0.6191
HISTORICAL_TARIFF_CNY_KWH=0.555

active_area=ROOF_M2*ACTIVE_COVERAGE
yield_kwh_kwp=LOCAL_REFERENCE_MWH_YEAR/LOCAL_REFERENCE_MWP

cases={}
for name,eff in [("S01_A",0.23),("S01_B_SEA_SHIELD",0.248)]:
    mwp=active_area*eff/1000.0
    gwh=mwp*yield_kwh_kwp/1000.0
    cases[name]={
        "module_efficiency_fraction":eff,
        "DC_capacity_MWp":mwp,
        "annual_generation_GWh":gwh,
        "fraction_of_2025_UF_RO_process_energy":gwh/PROCESS_ENERGY_2025_GWH,
        "historical_0_555_tariff_counterfactual_CNY":gwh*1e6*HISTORICAL_TARIFF_CNY_KWH,
        "location_based_CO2_avoided_tonnes_using_2023_Shandong_factor":gwh*1e6*SHANDONG_GRID_FACTOR_KGCO2_KWH/1000.0,
        "current_cost_saving_CNY":"UNKNOWN"
    }

print(json.dumps({
    "artifact_id":"DJK-NODE-001-RUN-1-SOLAR-v0.1",
    "active_module_area_m2":active_area,
    "local_yield_kWh_per_kWp_year":yield_kwh_kwp,
    "cases":cases
},indent=2))
