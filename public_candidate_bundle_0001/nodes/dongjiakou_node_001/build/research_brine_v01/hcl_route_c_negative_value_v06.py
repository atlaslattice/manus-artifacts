#!/usr/bin/env python3
"""Route C negative-value byproduct HCl transfer-cost and consolidated-balance screen.
All numbers synthetically assumed; no contractual receipt, plant assay or profit asserted.
"""
import json
PURE_HCL_T_Y=46512.94
POTENTIAL_ACID_T_Y=28552.79
def evaluate(price_per_solution_t, concentration=.31, delivered_logistics_per_solution_t=0,
             conditioning_per_solution_t=0, other_incremental_cost_cny_y=0,
             acid_value_per_t=1500, supplier_avoided_cost_per_solution_t=0):
    assert 0<concentration<=1 and min(delivered_logistics_per_solution_t,conditioning_per_solution_t,other_incremental_cost_cny_y,supplier_avoided_cost_per_solution_t)>=0
    solution=PURE_HCL_T_Y/concentration
    transfer=price_per_solution_t*solution
    logistics=solution*delivered_logistics_per_solution_t
    conditioning=solution*conditioning_per_solution_t
    value=POTENTIAL_ACID_T_Y*acid_value_per_t
    receiver=value-transfer-logistics-conditioning-other_incremental_cost_cny_y
    # If supplier is INSIDE network, cancel financial transfer. Avoided disposal may be a
    # real benefit only if documented in a preexisting outside-cost counterfactual;
    # do not add an invented supplier credit on top of a guaranteed negative transfer.
    consolidated_before_supplier_avoidance=value-logistics-conditioning-other_incremental_cost_cny_y
    return dict(hcl_solution_t_y=round(solution,2),supplier_price_cny_t=price_per_solution_t,
      supplier_to_receiver_transfer_cny_y=round(transfer,2),
      buyer_contribution_before_other_omitted_costs_cny_y=round(receiver,2),
      network_consolidated_before_avoided_disposal_cny_y=round(consolidated_before_supplier_avoidance,2),
      documented_avoided_disposal_sensitivity_cny_y=round(solution*supplier_avoided_cost_per_solution_t,2),
      realized_credit_cny_y=0,status="SCENARIO_ONLY",
      warning="Transfer cancels inside one network; avoided disposal is a separate evidenced baseline, not an invented subsidy")
if __name__=="__main__":
    print(json.dumps([evaluate(p,delivered_logistics_per_solution_t=70,conditioning_per_solution_t=25)
       for p in [195,0,-20,-50,-100]],indent=2))
