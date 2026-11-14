#!/usr/bin/env python3
"""Correct HCl solution-strength cost comparison for synthetic shell-brine routes.
No site assay, supplier contract, process feasibility or realized financial credit.
"""
import json
HCL_PURE_T=46512.94
ACID_T=28552.79
ACID_VALUE_CNY_T=1500
def model(price_cny_per_solution_t, strength_fraction=0.31, transport_cny_per_solution_t=0,
          all_other_incremental_cny_y=0):
    assert 0<strength_fraction<=1 and price_cny_per_solution_t>=0 and transport_cny_per_solution_t>=0
    assert all_other_incremental_cny_y>=0
    solution_t=HCL_PURE_T/strength_fraction
    reagent_cny=solution_t*(price_cny_per_solution_t+transport_cny_per_solution_t)
    total_cost_cny=reagent_cny+all_other_incremental_cny_y
    acid_value_cny=ACID_T*ACID_VALUE_CNY_T
    return {"hcl_pure_t":HCL_PURE_T,"hcl_solution_t":round(solution_t,2),
      "solution_strength":strength_fraction,"solution_price_cny_t":price_cny_per_solution_t,
      "acid_value_cny_y":round(acid_value_cny,2),
      "reagent_and_delivery_cny_y":round(reagent_cny,2),
      "contribution_before_unmodeled_costs_cny_y":round(acid_value_cny-reagent_cny,2),
      "contribution_after_specified_costs_cny_y":round(acid_value_cny-total_cost_cny,2),
      "break_even_solution_price_cny_t_before_other_costs":round(acid_value_cny/solution_t-transport_cny_per_solution_t,2),
      "status":"SYNTHETIC_ONLY_ZERO_REALIZED"}
if __name__=="__main__":
    print(json.dumps([model(p) for p in [110,135,160,195,250,400]],indent=2))
