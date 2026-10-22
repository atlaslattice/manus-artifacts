# Atlas Lattice v0.6 — Outcomes and Replication Publication Index

STATUS: PUBLIC REVIEW CANDIDATE | CANON: NO | DEPLOYMENT: NO | REALIZED CREDIT: ZERO

This release adds **documentation and schemas only**. It does not change the recovered Dongjiakou simulator or its 23 outstanding data requests, historical 239 reported local tests or six ecological vetoes.

- [Full v0.6 White Paper](ATLAS_LATTICE_REGENERATIVE_RESILIENCE_QOL_GRV_v0.6.md): entire October 9 dialogue delta, national economic/strategic context, QOL/Eden design, GRV, resource allocation and validation gates.
- [Outcome ledger](../schemas/atlas_outcome_ledger_v0.1.schema.json): evidence-aware metric records with null baselines, counterfactuals and zero credits.
- [Physical allocation ledger](../schemas/atlas_resource_allocation_v0.1.schema.json): reserved soil biomass, route allocation, dry-mass bases and unique lots.
- [Resilience scenario ledger](../schemas/atlas_resilience_scenario_v0.1.schema.json): probabilities with explicit horizon, severity, avoided loss and essential service coverage.
- [107-metric catalog](../fixtures/outcomes_metric_registry_v0.1.json): candidate metric names, units and direction, not plant measurements.
- [Dongjiakou unknown-first fixture](../fixtures/dongjiakou_outcomes_unknown_v0.1.json).
- [Synthetic biomass allocation fixture](../fixtures/atlas_resource_allocation_synthetic_v0.1.json).
- [Synthetic catastrophic resilience fixture](../fixtures/atlas_resilience_synthetic_v0.1.json).
- [Schema contract tests](../tests/test_outcome_contracts.py).
- [Simulator implementation roadmap](OUTCOME_SIMULATOR_NEXT_PHASE.md).

## How to run schema-only contract tests

```bash
python -m pip install pytest jsonschema
python -m pytest public_candidate_bundle_0001/tests/test_outcome_contracts.py -q
```

Do **not** interpret passing tests as plant validation; they test structural and a handful of invariant assertions only.

Original October 8 audited simulator: [README](../nodes/dongjiakou_node_001/build/README.md) and [evidence appendix](../nodes/dongjiakou_node_001/build/review/EVIDENCE_APPENDIX.md).

No credentials, site access data, private device data, personal health files or deployment approvals are requested or reproduced.
