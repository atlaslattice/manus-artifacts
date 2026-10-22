"""Candidate cross-sector funding ledger: projections never become spendable cash."""
import math
UNKNOWN="UNKNOWN"
def evaluate(config):
    seen=set()
    projected=[]
    for row in config["streams"]:
        key=row["stream_id"]
        if key in seen:raise ValueError("Savings stream allocated twice")
        seen.add(key)
        if row["current_realized_funding_credit_cny"] != 0:
            raise ValueError("No independently verified deployment cash receipt is present in this candidate")
        if row["evidence_class"] not in ("UNKNOWN","SENSITIVITY"):
            raise ValueError("Current funding inputs are UNKNOWN or explicit sensitivities")
        if not row["allocation_owner"]:
            raise ValueError("Allocation owner required")
        vals=[]
        for k in ("gross_cash_savings_cny","incremental_operating_cny","maintenance_reserve_cny",
                  "capital_renewal_cny","existing_commitments_cny"):
            v=row[k]
            if v is not None and (type(v) not in (int,float) or not math.isfinite(v) or v<0):
                raise ValueError("Invalid cash-ledger value")
            if v is not None and row["evidence_class"]!="SENSITIVITY":
                raise ValueError("Unreceipted cash must be labeled sensitivity")
            vals.append(v)
        projected.append(UNKNOWN if any(v is None for v in vals) else vals[0]-sum(vals[1:]))
    obligations=config["annual_benefits_cost_cny"]
    if obligations is not None and (type(obligations) not in (int,float) or not math.isfinite(obligations) or obligations<0):
        raise ValueError("Invalid annual benefits budget")
    if obligations is not None and config["cost_evidence_class"]!="SENSITIVITY":
        raise ValueError("No verified local benefits-cost receipt exists")
    net=UNKNOWN if UNKNOWN in projected else sum(projected)
    return {"module":"FUND01","current_realized_available_cash_cny":0,
        "projected_net_cash_after_existing_commitments_cny":net,
        "annual_benefits_cost_cny":UNKNOWN if obligations is None else obligations,
        "projected_budget_margin_cny":UNKNOWN if net==UNKNOWN or obligations is None else net-obligations,
        "benefits_funded_from_verified_deployment_gains":False,
        "deployment":False,"realized_credit":0,
        "promotion_rule":"Independent deployment cashflow/baseline/additionality/cost/rights/allocation audit; no forecast, QOL points or uncertain avoided capex is spendable funding."}

