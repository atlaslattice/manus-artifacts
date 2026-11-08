# Next phase: Atlas Outcomes simulator adapter v0.1

**Do not implement in this publication PR.** Maintain original source hash, recovered simulator reproduction output, current zero-credit baseline, and all 23 outstanding DAR requests.

## Adapter design

Suggested commands (names subject to code review):

- `simulator.py outcomes validate <ledger.json>`: Draft 2020-12 structure + reconciliation of provenance, uniqueness, method and no unearned credit.
- `simulator.py outcomes current`: same original locality plus **separate** outcomes ledger; no invented measured outputs.
- `simulator.py allocate <lots.json>`: wet/dry mass, soil/ecological reserves, existing commitments, collection losses, no-double-allocation; enforce rights/quality gates.
- `simulator.py resilience <scenario.json>`: scenario tree, annual vs decadal probability, GDP severity vs event odds, correlated shocks, incremental loss avoided, baseline comparisons, avoided-loss cap.
- `simulator.py grv <evidence.json>`: transitions AVAILABLE → REPRODUCIBLE → INDEPENDENTLY VERIFIED → PILOT → OPERATING → MEASURED BENEFITS; forks alone never qualify as deployments.

## Acceptance tests before merge

1. Original recovered `reproduce`, `validate`, `current` outputs remain byte-equivalent where expected.
2. Null and missing evidence never default to zero or success.
3. All positive credit attempts with blocked ecological veto fail.
4. Duplicate biomass-source allocation, K/KCl confusion and acid purity/dry mass basis mismatch fail.
5. 5% decadal event risk and 5% yearly event risk produce different expected losses.
6. Catastrophic 5% GDP severity is **not** treated as event probability or guaranteed project avoidance.
7. End-user value, upstream value added and QOL benefits cannot be double credited in aggregate.
8. Independent GRV replication requires an evidence receipt and a defined counterfactual.
9. Worker, reused water, soil, receiving ecosystem and maintenance assessments remain UNKNOWN unless measured.
10. No plant automation/control interfaces, network credentials or proprietary telemetry are introduced.

## High-priority external data requests

Existing DAR-001…DAR-023 remain untouched. Supplement with: site QOL baseline, irrigation-quality assay, greenhouse gas and air-quality measurements, soil/habitat survey, labor conditions, regional crop residue dry-basis inventory with farm retention floor, shipping/energy price data, firm spare gas storage/delivery capacity, documented local value added, independent adopter receipts, and qualified tourism counts. Record data custody and consent.

## Implementation gate

Do not merge adapter into master without independent reviewer approval, updated CI and negative tests, no simulator regression, and a readable source-to-claim audit trail. Production-scale decisions always require site operator and applicable regulatory authorization.
