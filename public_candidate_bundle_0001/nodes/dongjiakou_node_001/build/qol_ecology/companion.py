#!/usr/bin/env python3
"""Non-crediting QOL/ECO scenario reader. No connection to plant control."""
from __future__ import annotations
import json
import math
import sys
from pathlib import Path

def _nonnegative_or_none(x, name):
    if x is None: return None
    if isinstance(x, bool) or not isinstance(x,(int,float)) or not math.isfinite(x) or x<0:
        raise ValueError(name+" requires a finite nonnegative number or null")
    return float(x)

def illustrate_outfall(outfall, days=365):
    """Mass load only, NOT modeled removal or realized avoided discharge."""
    if not isinstance(days,int) or days<=0 or days>366: raise ValueError("days")
    if outfall["status"] not in ("MEASURED","REPORTED","SENSITIVITY","UNKNOWN"):
        raise ValueError("unsupported source status")
    q=_nonnegative_or_none(outfall["flow_m3_day"],"flow")
    n=_nonnegative_or_none(outfall["nitrogen_mg_l"],"N")
    p=_nonnegative_or_none(outfall["phosphorus_mg_l"],"P")
    # 1 m3 = 1000 L; mg / 1e9 = t; hence m3 * mg/L * 1e-6 = t
    convert=lambda c: None if q is None or c is None else q*days*c*1e-6
    return {"outfall_id":outfall["id"],"status":"DERIVED_SENSITIVITY" if outfall["status"]=="SENSITIVITY" else outfall["status"],"nitrogen_input_t_year":convert(n),"phosphorus_input_t_year":convert(p),"realized_avoided_t_year":0,"closure_verified":False}

def finance_sensitivity(finance):
    total=_nonnegative_or_none(finance["total_cost"],"cost")
    fraction=finance["recovery_fraction"]
    if fraction is not None and (isinstance(fraction,bool) or not isinstance(fraction,(int,float)) or not math.isfinite(fraction) or not 0<=fraction<=1):
        raise ValueError("recovery_fraction must be 0..1 or null")
    return {"basis":finance["cost_basis"],"status":"SENSITIVITY_NOT_REALIZED",
            "recovered_value":None if total is None or fraction is None else total*fraction,
            "unfunded_remainder":None if total is None or fraction is None else total*(1-fraction),
            "currency":finance["currency"]}

def calculate(data):
    if data.get("schema_version")!="0.1" or data.get("status")!="PROPOSED_NON_CANON":
        raise ValueError("Unsupported schema/status")
    source_ids={s["id"] for s in data["sources"]}
    if len(source_ids)!=len(data["sources"]): raise ValueError("Duplicate source IDs")
    for item in data["programs"]+data["outfalls"]+[data["finance"]]:
        if not item["source_ids"] or not set(item["source_ids"])<=source_ids:
            raise ValueError("Unresolved provenance source IDs")
    if any(p["realized_credit"]!=0 for p in data["programs"]): raise ValueError("No credit")
    if any(o["realized_avoided_load_t_year"]!=0 for o in data["outfalls"]): raise ValueError("No discharge credit")
    return {"locality_id":data["locality_id"],"schema_version":"0.1",
       "program_count":len(data["programs"]),"programs_measured":sum(p["status"]=="MEASURED" for p in data["programs"]),
       "outfalls":[illustrate_outfall(o) for o in data["outfalls"]],
       "finance":finance_sensitivity(data["finance"]),
       "realized_credit":0,"locality_clearance":"NOT_ESTABLISHED"}

if __name__=="__main__":
    if len(sys.argv)!=2: raise SystemExit("Usage: python3 companion.py scenario.json")
    document=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(json.dumps(calculate(document),indent=2))
