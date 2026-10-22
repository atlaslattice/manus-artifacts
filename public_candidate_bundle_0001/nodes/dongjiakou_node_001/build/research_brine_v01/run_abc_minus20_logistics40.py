#!/usr/bin/env python3
"""Standalone DJK S01 synthetic A/B/C; user-selected byproduct -20 and logistics 40.
No direct process control or realized credit. Standard Python 3 only.
"""
import csv
from pathlib import Path

brine_gypsum_t=95961.77
shell_gypsum_t=71381.98
pure_hcl_t=46512.94
strength=0.31
hcl_solution_t=pure_hcl_t/strength
acid_conversion=0.40
acid_value_cny_t=1500
logistics_cny_t_solution=40
cases=[("A brine only",0,0),("B purchased HCl",shell_gypsum_t,195),("C byproduct HCl",shell_gypsum_t,-20)]
rows=[]
for name,extra_gypsum,source_price in cases:
    extra_acid=extra_gypsum*acid_conversion
    qty=hcl_solution_t if extra_gypsum else 0
    source_payment=source_price*qty
    logistics=qty*logistics_cny_t_solution
    incremental_contribution=extra_acid*acid_value_cny_t-source_payment-logistics
    rows.append(dict(route=name,brine_gypsum_t_y=round(brine_gypsum_t,2),extra_gypsum_t_y=round(extra_gypsum,2),
        total_gypsum_t_y=round(brine_gypsum_t+extra_gypsum,2),
        total_acid_potential_t_y=round((brine_gypsum_t+extra_gypsum)*acid_conversion,2),
        extra_acid_potential_t_y=round(extra_acid,2),hcl_solution_31pct_t_y=round(qty,2),
        source_price_cny_t_solution=source_price,source_payment_cny_y=round(source_payment,2),
        logistics_cny_y=round(logistics,2),
        incremental_acid_value_cny_y=round(extra_acid*acid_value_cny_t,2),
        incremental_contribution_pre_other_costs_cny_y=round(incremental_contribution,2),
        realized_credit_cny_y=0))
assert abs(rows[2]["incremental_contribution_pre_other_costs_cny_y"]-39828353.16)<1
assert abs(rows[1]["incremental_contribution_pre_other_costs_cny_y"]-7569378.65)<1
out=Path(__file__).with_name("abc_minus20_logistics40.csv")
with out.open("w",newline="") as handle:
    writer=csv.DictWriter(handle,fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
print("Synthetic A/B/C completed. Outputs:",rows,"\nCSV:",out)
