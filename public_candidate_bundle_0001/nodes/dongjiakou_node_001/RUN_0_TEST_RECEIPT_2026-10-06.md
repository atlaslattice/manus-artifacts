# Dongjiakou Node-001 — Run 0 Test Receipt

```text
DATE: 2026-10-06
STATUS: EXECUTED BASELINE / NON-CANON
MONTE_CARLO: NO
UNKNOWN_IMPUTATION: NO
RETROFIT_CREDIT: ZERO
```

Run 0 is the floor every later module must beat.

```text
annual product       = 36.5M * U m3/year
UF+RO electricity    = 80.3 * U GWh/year
chemical cost        < 5.475M * U CNY/year
```

Mass balance:

```text
45% recovery:
feed                222,222.22 m3/day
product             100,000.00 m3/day
reject-equivalent   122,222.22 m3/day
annual feed         81.111M * U m3/year
annual reject       44.611M * U m3/year

50% recovery:
feed                200,000.00 m3/day
product             100,000.00 m3/day
reject-equivalent   100,000.00 m3/day
annual feed         73.000M * U m3/year
annual reject       36.500M * U m3/year
```

U remains UNKNOWN. The U=1 values are arithmetic references, not claims of actual utilization.

The baseline credits solar, unused-head mini-hydro, regenerative compute, adaptive fouling, sono-CIP, resource recovery and OAE at zero.

Maintenance events remain separate receipts rather than being collapsed into an assumed membrane lifetime.

An UNKNOWN field may not be sampled in Monte Carlo. Only sourced numerical ranges may enter stochastic analysis.

**Keeper:** Verified baseline first -> one module at a time -> measure interaction -> stack only survivors.
