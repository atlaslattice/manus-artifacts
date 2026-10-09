#!/usr/bin/env python3
"""Standalone mass-conserving brine portfolio sensitivity; no plant controls.
All quantities and prices are synthetic assumptions, not Dongjiakou site data.
"""
import json,sys
from pathlib import Path

def simulate(s):
    flow=s["intake_m3_day"]; days=s["days_year"]; recovery=s["water_recovery_fraction"]
    assert flow>0 and 0<recovery<1 and 0<days<=366
    freshwater=flow*recovery*days; brine=flow*(1-recovery)*days
    feed={}
    for element,mg_l in s["intake_mg_l"].items():
        assert mg_l>=0
        feed[element]=flow*1000*mg_l/1e9*days # kg to tonnes: mg/L * m3*1000 L / 1e9 mg/t
    o={}
    for name,v in s["products"].items():
        element=v["feed_element"]; frac=v["capture_fraction"]; factor=v["product_t_per_element_t"]
        assert 0<=frac<=1 and factor>0 and element in feed
        elemental=feed[element]*frac
        o[name]={"element_input_t_y":feed[element], "element_recovered_t_y":elemental,
                 "product_t_y":elemental*factor,
                 "gross_sales_usd_y":elemental*factor*v["price_usd_t"],
                 "variable_cost_usd_y":elemental*factor*v["cost_usd_t"]}
    assert len({v["feed_element"] for v in s["products"].values()})==len(s["products"]), "Duplicate element allocation"
    scenarios={}
    for name,v in s["scenarios"].items():
        active=v["active_products"]; heat_saving=v["heat_saving_usd_m3_brine"]
        assert 0<=heat_saving<=s["baseline_opex_usd_m3_brine"]
        sales=sum(o[p]["gross_sales_usd_y"] for p in active)
        variable=sum(o[p]["variable_cost_usd_y"] for p in active)
        incremental=v["incremental_fixed_opex_usd_y"]+variable
        base=brine*s["baseline_opex_usd_m3_brine"]
        avoided_disposal=brine*v["avoided_disposal_usd_m3_brine"]
        saved_heat=brine*heat_saving
        net_annual=sales+avoided_disposal+saved_heat-incremental-base
        capex=v["incremental_capex_usd"]
        scenarios[name]={"gross_sales_usd_y":round(sales,2),"incremental_opex_usd_y":round(incremental,2),
          "baseline_opex_usd_y":round(base,2),"avoided_disposal_usd_y":round(avoided_disposal,2),
          "heat_savings_usd_y":round(saved_heat,2),"net_cash_before_capex_usd_y":round(net_annual,2),
          "net_incremental_vs_A_usd_y":None,"incremental_capex_usd":capex,
          "simple_payback_years_vs_A":None}
    base=scenarios["A"]["net_cash_before_capex_usd_y"]
    for name,r in scenarios.items():
        improvement=r["net_cash_before_capex_usd_y"]-base
        r["net_incremental_vs_A_usd_y"]=round(improvement,2)
        r["simple_payback_years_vs_A"]=round(r["incremental_capex_usd"]/improvement,2) if improvement>0 and r["incremental_capex_usd"]>0 else None
    return {"state":"SYNTHETIC_NON_CANON_ZERO_REALIZED","annual_freshwater_m3":freshwater,
      "annual_concentrate_m3":brine,"elemental_feed_t_y":feed,"products":o,"scenarios":scenarios,
      "restrictions":["No extrapolation to local actual feed without assays","Carbon/QOL effects NOT monetized",
      "Chemical stoichiometry, processing order, brine residuals, land and agricultural controls still unresolved",
      "Selling a mineral excludes its reuse as process reagent; no dual allocation"]}

def main():
    p=Path(sys.argv[1] if len(sys.argv)>1 else Path(__file__).with_name("scenario_synthetic.json"))
    result=simulate(json.loads(p.read_text()))
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=="__main__":main()
