#!/usr/bin/env python3
"""AGR01/CHEM01 constrained gypsum allocation over time; research-only Python 3.10+.
No field, product, national sulfur or Dongjiakou physical realization asserted.
Run: python3 gypsum_allocation.py allocation_synthetic.json
"""
import json, sys
from pathlib import Path

def run(d):
    years=int(d["years"]); assert 1<=years<=100
    annual=float(d["qualified_dry_gypsum_t_y"]); assert annual>=0
    inventory=0.0; output=[]
    classes=d["soil_classes"]
    for z in classes:
        assert z["hectares"]>=0 and z["initial_t_ha"]>=0 and z["maintenance_t_ha_y"]>=0
        assert 0<=z["reclamation_decline_fraction_y"]<=1 and 0<=z["reclamation_years"]<=years
    national=d["national_sulfur"]
    assert national["balance_s_equivalent_t_y"] is None or isinstance(national["balance_s_equivalent_t_y"],(float,int))
    assert 0<=d["acid_t_per_dry_gypsum_t"]<=98.079/172.171
    industrial=d["industrial_quality"]
    # Missing, unverified or failing assay is not a pass.
    qualified_ind=(industrial["assay_measured"] is True and industrial["hub_acceptance_verified"] is True
       and industrial["measured_gypsum_purity"] is not None
       and industrial["measured_gypsum_purity"]>=industrial["minimum_gypsum_purity"]
       and industrial["measured_moisture_fraction"] is not None
       and industrial["measured_moisture_fraction"]<=industrial["maximum_moisture_fraction"])
    deferred_ind=industrial["assay_measured"] is not True or industrial["hub_acceptance_verified"] is not True
    reserved=str(national["balance_s_equivalent_t_y"] is None)
    for y in range(1,years+1):
        available=annual+inventory
        justified=[]
        for z in classes:
            proven=(z["soil_test_measured"] is True and z["ag_product_batch_assay_pass"] is True
              and z["field_trial_verified"] is True and z["approved_drainage_plan"] is True
              and z["farm_consent_verified"] is True)
            # No invented default field need: without receipts, demand is zero.
            if not proven:continue
            reclaim=z["hectares"]*z["initial_t_ha"]*((1-z["reclamation_decline_fraction_y"])**(y-1)) if y<=z["reclamation_years"] else 0.0
            demand=reclaim+z["hectares"]*z["maintenance_t_ha_y"]
            justified.append((z["name"],max(0,demand)))
        total_ag_demand=sum(v for _,v in justified)
        national_gap=national["balance_s_equivalent_t_y"] is not None and national["balance_s_equivalent_t_y"]<0
        # Conservative policy: if a sulfur shortfall exists, field use is limited to evidence-qualified
        # agronomic demand and optional GOV01 fraction; it never expands to match an optimistic valuation.
        cap=d["sulfur_shortfall_ag_cap_fraction"] if national_gap else 1.0
        assert 0<=cap<=1
        alloc_ag=min(available,total_ag_demand,available*cap)
        ag_classes={k:round(alloc_ag*v/total_ag_demand,5) if total_ag_demand else 0.0 for k,v in justified}
        remaining=available-alloc_ag
        alloc_acid=remaining if qualified_ind else 0.0
        inventory=remaining-alloc_acid
        assert abs(annual+(output[-1]["closing_inventory_t"] if output else 0)-alloc_ag-alloc_acid-inventory)<1e-6
        output.append({"year":y,"available_gypsum_t":round(available,3),
           "ag_assayed_soil_demand_t":round(total_ag_demand,3),
           "ag_allocated_t":round(alloc_ag,3),"ag_by_soil_class_t":ag_classes,
           "acid_feed_allocated_t":round(alloc_acid,3),
           "acid_potential_t":round(alloc_acid*d["acid_t_per_dry_gypsum_t"],3),
           "closing_inventory_t":round(inventory,3),
           "ag_quality_and_soil_receipts_required":len(classes)-len(justified),
           "industrial_quality_pass":qualified_ind,
           "industrial_hold_reason":"UNVERIFIED_HUB_OR_ASSAY" if deferred_ind else ("FAIL_QUALITY_SPEC" if not qualified_ind else None),
           "national_sulfur_gate":"SHORTFALL_PRIORITY" if national_gap else ("UNKNOWN" if national["balance_s_equivalent_t_y"] is None else "NONNEGATIVE_NOT_EXPORT_AUTHORIZATION"),
           "external_sale_credit_t":0,"realized_credit_t":0})
    return {"status":"SYNTHETIC_NON_CANON_ZERO_REALIZED","version":"AGR01_CHEM01_TEMPORAL_v0.1",
      "years":output,
      "constraints":{"internal_exchange":"FULLY_LOADED_AT_COST","ag_default_t_ha":0,
        "national_balance_unverified":reserved,"export_authorized":False,
        "product_standards_require_batch_specific_legal_review":True},
      "notes":["The scenario represents sampled qualified dry gypsum input, not raw theoretical ceiling as achieved output",
       "Field uptake and salt flushing can harm receiving waters; safe drainage and monitoring mandatory",
       "No mass credit twice. Industrial allocation requires measured accepted batch and hub",
       "Agricultural benefit is not automatically inferred from comparator yield gains",
       "No external sale permitted by this model; governance and actual import-zero evidence required"]}

if __name__=="__main__":
    f=Path(sys.argv[1] if len(sys.argv)>1 else Path(__file__).with_name("allocation_synthetic.json"))
    print(json.dumps(run(json.loads(f.read_text())),indent=2))
