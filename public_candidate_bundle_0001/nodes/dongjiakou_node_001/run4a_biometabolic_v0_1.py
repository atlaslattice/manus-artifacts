#!/usr/bin/env python3
"""Dongjiakou Run 4A BIO01 — organics/wastewater transfer functions.

No node credit is awarded without verified feedstock and chemistry.
Food-waste biogas uses a local Qingdao retrospective reference only.
Wastewater methane uses a stoichiometric theoretical ceiling only.
"""
import argparse, json
LOCAL_BIOGAS_M3_PER_T = 5260000.0 / 260000.0
THEORETICAL_CH4_M3_PER_KG_BCOD_STP = 0.35

def food_waste(food_tpd):
    annual_t = food_tpd * 365.0
    return {
        "annual_feed_tonnes": annual_t,
        "reference_biogas_m3_year": annual_t * LOCAL_BIOGAS_M3_PER_T,
        "energy_credit": "UNKNOWN"
    }

def wastewater(q_m3_day, cod_mg_l, biodegradable_fraction, removal_fraction):
    if not (0 <= biodegradable_fraction <= 1 and 0 <= removal_fraction <= 1):
        raise ValueError("fractions must be in [0,1]")
    kg_cod_day = q_m3_day * cod_mg_l / 1000.0
    kg_bcod_removed_day = kg_cod_day * biodegradable_fraction * removal_fraction
    return {
        "COD_load_kg_day": kg_cod_day,
        "biodegradable_COD_removed_kg_day": kg_bcod_removed_day,
        "theoretical_CH4_ceiling_m3_day_STP": kg_bcod_removed_day * THEORETICAL_CH4_M3_PER_KG_BCOD_STP,
        "warning": "Stoichiometric ceiling, not plant yield; dissolved methane, sulfate, biomass synthesis and parasitics are not closed."
    }

if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--food-waste-tpd",type=float,default=None)
    p.add_argument("--wastewater-m3-day",type=float,default=None)
    p.add_argument("--cod-mg-l",type=float,default=None)
    p.add_argument("--biodegradable-fraction",type=float,default=None)
    p.add_argument("--cod-removal-fraction",type=float,default=None)
    a=p.parse_args()
    out={"artifact_id":"DJK-NODE-001-RUN-4A-BIOMETABOLIC-v0.1","baseline_credit":0}
    if a.food_waste_tpd is not None:
        out["food_waste_reference"]=food_waste(a.food_waste_tpd)
    ww=[a.wastewater_m3_day,a.cod_mg_l,a.biodegradable_fraction,a.cod_removal_fraction]
    if any(v is not None for v in ww):
        if any(v is None for v in ww):
            out["wastewater"]="UNKNOWN_INPUT_SET_INCOMPLETE"
        else:
            out["wastewater"]=wastewater(*ww)
    print(json.dumps(out,indent=2))