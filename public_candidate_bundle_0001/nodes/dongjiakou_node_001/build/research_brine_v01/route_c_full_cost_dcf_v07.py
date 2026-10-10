#!/usr/bin/env python3
"""Illustrative Route C full-stack DCF. Not actual quotes/EPC or contract."""
import json
acid_y=28552.792; hcl_solution_y=46512.94/.31; shell_y=96000
def evaluate(x):
    annual_revenue=acid_y*x["acid_value_cny_t"]
    annual_source=hcl_solution_y*x["hcl_source_price_cny_per_solution_t"]
    annual_cost=(hcl_solution_y*x["logistics_cny_per_solution_t"]+
        hcl_solution_y*x["conditioning_cny_per_solution_t"]+
        shell_y*x["shell_processing_cny_per_wet_t"]+
        acid_y*x["incremental_acid_conversion_cny_per_acid_t"]+
        x["residuals_and_co2_cny_y"]+x["fixed_om_cny_y"])
    # Negative source price = payment to receiver; cancels if two parties within network.
    annual_cashflow=annual_revenue-annual_source-annual_cost
    N=x["years"];rate=x["discount_rate"];cap=x["incremental_capex_cny"]
    npv=-cap+sum(annual_cashflow/((1+rate)**year) for year in range(1,N+1))
    return dict(scenario=x["label"],annual_nominal_acid_value_cny=round(annual_revenue),
       annual_source_payment_cny=round(annual_source),
       annual_other_cash_outlay_cny=round(annual_cost),
       annual_cashflow_before_tax_cny=round(annual_cashflow),
       project_npv_before_tax_cny=round(npv),realized_cashflow_cny=0,
       evidence="ALL COST INPUTS ASSUMED; excludes tax, salvage, working capital and variable annual production")
if __name__=="__main__":
    scenarios=[
       dict(label="optimistic",acid_value_cny_t=1500,hcl_source_price_cny_per_solution_t=-20,
            logistics_cny_per_solution_t=40,conditioning_cny_per_solution_t=10,
            shell_processing_cny_per_wet_t=20,incremental_acid_conversion_cny_per_acid_t=250,
            residuals_and_co2_cny_y=1000000,fixed_om_cny_y=1000000,incremental_capex_cny=50000000,years=15,discount_rate=.10),
       dict(label="middle",acid_value_cny_t=1500,hcl_source_price_cny_per_solution_t=-20,
            logistics_cny_per_solution_t=80,conditioning_cny_per_solution_t=40,
            shell_processing_cny_per_wet_t=60,incremental_acid_conversion_cny_per_acid_t=600,
            residuals_and_co2_cny_y=3000000,fixed_om_cny_y=4000000,incremental_capex_cny=200000000,years=15,discount_rate=.10),
       dict(label="adverse",acid_value_cny_t=1200,hcl_source_price_cny_per_solution_t=135,
            logistics_cny_per_solution_t=150,conditioning_cny_per_solution_t=80,
            shell_processing_cny_per_wet_t=120,incremental_acid_conversion_cny_per_acid_t=1100,
            residuals_and_co2_cny_y=7000000,fixed_om_cny_y=9000000,incremental_capex_cny=500000000,years=15,discount_rate=.10)]
    print(json.dumps([evaluate(x) for x in scenarios],indent=2))
