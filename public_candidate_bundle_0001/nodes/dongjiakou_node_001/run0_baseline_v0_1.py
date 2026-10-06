#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
DAYS=365.0
def run(U=None):
    Qp=100000.0; sec=2.2; chem=0.15
    result={"artifact_id":"DJK-NODE-001-RUN-0-v0.1","status":"EXECUTED_BASELINE_SIMULATION_NON_CANON"}
    result["inputs"]={"product_capacity_m3_day":Qp,"UF_RO_process_train_SEC_kWh_m3":sec,"chemical_cost_CNY_m3_relation":"<","chemical_cost_CNY_m3_upper_bound":chem,"recovery_cases":[0.45,0.50],"utilization_U":U if U is not None else "UNKNOWN","whole_site_SEC":"UNKNOWN","tariff":"UNKNOWN"}
    result["coefficients_per_U"]={"annual_product_m3":Qp*DAYS,"annual_process_train_energy_GWh":Qp*DAYS*sec/1e6,"annual_chemical_cost_CNY_upper_bound":Qp*DAYS*chem}
    mb={}
    for r in [0.45,0.50]:
        qf=Qp/r; qrej=qf-Qp
        mb[f"{r:.2f}"]={"feed_m3_day":qf,"product_m3_day":Qp,"reject_equivalent_m3_day":qrej,"annual_feed_m3_per_U":qf*DAYS,"annual_reject_equivalent_m3_per_U":qrej*DAYS}
    result["mass_balance"]=mb
    result["retrofit_credit"]={"solar":0,"mini_hydro":0,"compute":0,"adaptive_fouling":0,"sono_CIP":0,"resource_recovery":0,"OAE":0}
    if U is not None:
        if U<0 or U>1: raise ValueError("U must be in [0,1]")
        result["evaluated_at_U"]={"U":U,"annual_product_m3":Qp*DAYS*U,"annual_process_train_energy_GWh":Qp*DAYS*sec/1e6*U,"annual_chemical_cost_CNY_upper_bound":Qp*DAYS*chem*U}
    else:
        result["U1_reference_not_operating_claim"]={"annual_product_m3":Qp*DAYS,"annual_process_train_energy_GWh":Qp*DAYS*sec/1e6,"annual_chemical_cost_CNY_upper_bound":Qp*DAYS*chem}
    return result
if __name__=="__main__":
    p=argparse.ArgumentParser(); p.add_argument("--utilization",type=float,default=None); a=p.parse_args()
    print(json.dumps(run(a.utilization),indent=2))
