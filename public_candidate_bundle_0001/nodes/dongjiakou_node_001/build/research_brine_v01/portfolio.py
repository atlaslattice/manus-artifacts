#!/usr/bin/env python3
"""DJK brine portfolio sensitivity. SYNTHETIC ONLY. No plant control or site forecast.
Network internal exchanges are at audited full cost, never market rates.
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
        feed[element]=flow*mg_l*days/1e6 # mg/L * m3 *1000 L /1e9 mg/t
    products={}
    assert len({v["feed_element"] for v in s["products"].values()})==len(s["products"]), "Duplicate constituent allocation"
    for name,v in s["products"].items():
        e=v["feed_element"]; cap=v["capture_fraction"]; factor=v["product_t_per_element_t"]
        internal=v["network_use_fraction"];assert 0<=cap<=1 and factor>0 and e in feed and 0<=internal<=1
        product=feed[e]*cap*factor
        cost=product*v["production_and_delivery_cost_usd_t"]
        products[name]={"elemental_feed_t_y":feed[e],"elemental_recovered_t_y":feed[e]*cap,
          "product_t_y":product,"network_transfer_t_y":product*internal,
          "external_sale_t_y":product*(1-internal),
          "network_transfer_at_cost_usd_y":cost*internal,
          "external_sales_usd_y":product*(1-internal)*v["external_price_usd_t"],
          "production_and_delivery_cost_usd_y":cost,
          "external_premium_over_at_cost_usd_y":product*(1-internal)*(v["external_price_usd_t"]-v["production_and_delivery_cost_usd_t"])}
    scenarios={}
    for name,v in s["scenarios"].items():
        active=v["active_products"]; heat=v["heat_saving_usd_m3_brine"]
        assert 0<=heat<=s["baseline_opex_usd_m3_brine"]
        assert 0<=v["avoided_disposal_usd_m3_brine"]<=s["baseline_disposal_cost_usd_m3_brine"]
        assert len(active)==len(set(active))
        external=sum(products[p]["external_sales_usd_y"] for p in active)
        internal_at_cost=sum(products[p]["network_transfer_at_cost_usd_y"] for p in active)
        prod_cost=sum(products[p]["production_and_delivery_cost_usd_y"] for p in active)
        fixed=v["incremental_fixed_opex_usd_y"]
        baseline=(s["baseline_opex_usd_m3_brine"]+s["baseline_disposal_cost_usd_m3_brine"])*brine
        avoided=brine*v["avoided_disposal_usd_m3_brine"]
        saved=brine*heat
        node_net=external+internal_at_cost+avoided+saved-prod_cost-fixed-baseline
        # Network consolidation: cancel at-cost internal transfer income with matching recipient expense.
        # Product production is a real network expense; internal consumption value is NOT invented revenue.
        consolidated_net=external+avoided+saved-prod_cost-fixed-baseline
        scenarios[name]={"external_sales_usd_y":round(external,2),"internal_transfer_at_cost_usd_y":round(internal_at_cost,2),
          "production_delivery_cost_usd_y":round(prod_cost,2),"fixed_incremental_opex_usd_y":fixed,
          "baseline_brine_management_usd_y":round(baseline,2),"avoided_disposal_usd_y":round(avoided,2),
          "saved_energy_usd_y":round(saved,2),"node_cash_after_internal_cost_recovery_usd_y":round(node_net,2),
          "network_consolidated_cash_usd_y":round(consolidated_net,2),
          "incremental_capex_usd":v["incremental_capex_usd"]}
    base=scenarios["A"]["network_consolidated_cash_usd_y"]
    for val in scenarios.values():
        increment=val["network_consolidated_cash_usd_y"]-base
        val["incremental_consolidated_vs_A_usd_y"]=round(increment,2)
        val["payback_if_positive_years"]=round(val["incremental_capex_usd"]/increment,2) if increment>0 and val["incremental_capex_usd"]>0 else None
    return {"status":"SYNTHETIC_NON_CANON_ZERO_REALIZED",
      "freshwater_m3_year":freshwater,"concentrate_m3_year":brine,"elemental_feed_t_year":feed,
      "products":products,"scenario_results":scenarios,
      "network_trade_rule":"Every internal transfer at verified production + delivery cost; eliminated in consolidated ledger",
      "limitations":["No physical plant measurements; input seawater profile is illustrative",
       "No full thermodynamic/process feasibility, reagents stoichiometry or acid/base costs beyond assumed unit costs",
       "No agronomic end-use assumed: grain agriculture demands irrigation crop/salinity and local food safety approvals",
       "No QOL carbon or avoided purchases monetized; report outside cash until receipts exist",
       "No plant or node clearance; no verified mineral or zero-discharge credit"]}

if __name__=="__main__":
    path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name("scenario_synthetic.json")
    print(json.dumps(simulate(json.loads(path.read_text())),indent=2,sort_keys=True))
