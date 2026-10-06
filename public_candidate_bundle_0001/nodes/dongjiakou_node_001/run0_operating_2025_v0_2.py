#!/usr/bin/env python3
"""Dongjiakou Node-001 Run 0.2 — dated 2025 operating-volume baseline."""
import json

CAPACITY_M3_DAY=100000.0
DAYS=365.0
PRODUCT_2025_M3=17_930_000.0
UF_RO_SEC_KWH_M3=2.2
CHEM_UPPER_CNY_M3=0.15
RECOVERY_CASES=(0.45,0.50)

U=PRODUCT_2025_M3/(CAPACITY_M3_DAY*DAYS)

result={
    "artifact_id":"DJK-NODE-001-RUN-0-OPERATING-2025-v0.2",
    "reported_product_supply_m3":PRODUCT_2025_M3,
    "derived_utilization_U":U,
    "derived_process_train_energy_GWh":PRODUCT_2025_M3*UF_RO_SEC_KWH_M3/1e6,
    "derived_annual_chemical_cost_CNY_upper_bound":PRODUCT_2025_M3*CHEM_UPPER_CNY_M3,
    "mass_balance_using_reported_technology_recovery_range":{}
}

for r in RECOVERY_CASES:
    feed=PRODUCT_2025_M3/r
    result["mass_balance_using_reported_technology_recovery_range"][f"{r:.2f}"]={
        "annual_feed_m3":feed,
        "annual_product_m3":PRODUCT_2025_M3,
        "annual_reject_equivalent_m3":feed-PRODUCT_2025_M3
    }

print(json.dumps(result,indent=2))
