# AtlasBrain — Index

```text
STATUS: EVIDENCE-LANE INDEX — NOT CANON
DATE: 2026-05-26
FRESHNESS: ACTIVE
UPDATE CADENCE: weekly or on lane/schema changes
PURPOSE: fast routing index for AtlasBrain evidence, benchmark, quarantine, and public-claim gates
```

## Root and doctrine

- `archive/boot/atlasbrain/README.md`

## Lane map

- `archive/boot/atlasbrain/raw_logs/README.md`
- `archive/boot/atlasbrain/evidence_packets/README.md`
- `archive/boot/atlasbrain/benchmarks/README.md`
- `archive/boot/atlasbrain/evaluator_reactions/README.md`
- `archive/boot/atlasbrain/learning_claims/README.md`
- `archive/boot/atlasbrain/public_claims/README.md`
- `archive/boot/atlasbrain/quarantine/README.md`
- `archive/boot/atlasbrain/schemas/ATLASBRAIN_EVIDENCE_PACKET_SCHEMA_v0.1.yaml`

## Gate + test surfaces

- Gate validator: `archive/boot/gptbrain/reference_impl/atlasbrain_gate.py`
- Gate tests: `archive/boot/gptbrain/reference_impl/test_atlasbrain_gate.py`
- Shared checks: `archive/boot/gptbrain/reference_impl/run_checks.sh`

## Safety kit templates

- `archive/boot/atlasbrain/PUBLIC_CLAIM_PROMOTION_CHECKLIST_TEMPLATE_2026-05-26.md`
- `archive/boot/atlasbrain/QUARANTINE_TRIAGE_DECISION_RUBRIC_2026-05-26.md`
- `archive/boot/atlasbrain/BENCHMARK_DOSSIER_MINIMUM_COMPLETENESS_CHECKLIST_2026-05-26.md`
- `archive/boot/atlasbrain/EVALUATOR_REACTION_DISCLAIMER_TEMPLATE_2026-05-26.md`
- `archive/boot/atlasbrain/EVIDENCE_PACKET_AUTHORING_TEMPLATE_2026-05-26.md`
- `archive/boot/atlasbrain/LEARNING_CLAIM_MECHANISM_CLASSIFICATION_QUICKSHEET_2026-05-26.md`
- `archive/boot/atlasbrain/ATLASBRAIN_LANE_HEALTH_DASHBOARD_2026-05-26.md`

## Index integrity policy

- Every path listed here must resolve to an existing repository file.

## Current operating boundary

- Evidence can inform action.
- Evidence cannot self-authorize public claims or canon status.
- Human-root approval remains required for claim promotion.
