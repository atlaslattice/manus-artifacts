#!/usr/bin/env python3
"""Dongjiakou Node-001 Run 2 — unused-head hydro parametric sensitivity."""
import argparse, json
RHO=1000.0
G=9.80665
V_PRODUCT_2025_M3=17_930_000.0
PROCESS_ENERGY_2025_GWH=39.446
def hydro(volume_m3_year, head_m, eta):
    if volume_m3_year < 0 or head_m < 0 or not 0 <= eta <= 1:
        raise ValueError("volume/head must be nonnegative and eta in [0,1]")
    gwh=RHO*G*volume_m3_year*head_m*eta/3.6e12
    return {"annual_energy_GWh":gwh,"average_power_kW":gwh*1e6/8760.0,"fraction_of_2025_UF_RO_process_energy":gwh/PROCESS_ENERGY_2025_GWH}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--head-m",type=float,default=None)
    p.add_argument("--eta",type=float,default=0.8)
    p.add_argument("--volume-m3-year",type=float,default=V_PRODUCT_2025_M3)
    a=p.parse_args()
    out={"artifact_id":"DJK-NODE-001-RUN-2-HYDRO-v0.1","H_available_m":"UNKNOWN" if a.head_m is None else a.head_m,"eta":a.eta,"volume_basis_m3_year":a.volume_m3_year,"baseline_credit_GWh_year":0.0 if a.head_m is None else None}
    if a.head_m is not None: out["result"]=hydro(a.volume_m3_year,a.head_m,a.eta)
    print(json.dumps(out,indent=2))