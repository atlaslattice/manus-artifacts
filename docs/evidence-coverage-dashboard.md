# Evidence Coverage Dashboard

> **Status:** CANDIDATE  
> **Artifact Type:** dashboard  
> **Date:** 2026-05-28  
> **Generated:** 2026-05-28  
> **Related:** [Evidence ledger index](./evidence/README.md), [Evidence standards](./evidence-standards.md), [Artifact registry](./knowledge-graph/artifact_registry.v0_1.json)

## Coverage basis

This dashboard tracks coverage for current flagship candidate artifacts using entries present in `docs/evidence/`. Legacy seed-ledger entries in `docs/knowledge-graph/ai_evidence_ledger.seed.v0_1.json` are excluded from the percentage below until they are backfilled into the evidence folder.

## Coverage table

| Domain | Artifacts | Has evidence | Coverage % |
|---|---:|---:|---:|
| Governance | 3 | 1 | 33.3% |
| Schema + reference code | 1 | 1 | 100.0% |
| GPTDream++ research | 2 | 1 | 50.0% |
| Knowledge-graph + evidence infrastructure | 5 | 0 | 0.0% |
| Execution + CI operations | 5 | 0 | 0.0% |
| **Total** | **16** | **3** | **18.8%** |

## Overall coverage score

**18.8%** of currently tracked flagship artifacts have a dedicated evidence entry in `docs/evidence/`.

## Top gaps

1. Knowledge-graph and evidence-infrastructure artifacts have no backfilled evidence entries yet.
2. Execution campaign, workflow, and validator artifacts still rely on implicit provenance rather than dedicated evidence records.
3. GPTDream++ package-guide artifacts need a direct evidence entry separate from the vault manifest.

## Linked evidence entries

- [EVID-CODE-001](./evidence/EVID-CODE-001.json)
- [EVID-GOV-001](./evidence/EVID-GOV-001.json)
- [EVID-RESEARCH-001](./evidence/EVID-RESEARCH-001.json)
