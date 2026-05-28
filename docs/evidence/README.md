# Evidence Ledger Index

> **Status:** CANDIDATE  
> **Artifact Type:** guide / index  
> **Date:** 2026-05-28  
> **Related:** [Evidence standards](../evidence-standards.md), [AI evidence ledger schema](../knowledge-graph/ai_evidence_ledger.schema.v0_1.json), [Ratification and Trust Flow](../RATIFICATION_AND_TRUST_FLOW.md)

## What the evidence ledger is for

The evidence ledger is the provenance layer for AI-built and AI-assisted Atlas Lattice artifacts. It records what claim is being made, which artifact the claim refers to, what source or receipt supports the claim, which AI systems were involved, and how the claim can be reviewed or reproduced.

## How entries are structured

Each entry in `docs/evidence/` is a single JSON document with:

- `schema_version`
- `evidence_id`
- `artifact_id`
- `artifact_title`
- `artifact_path`
- `claim`
- `evidence_type`
- `evidence_date`
- `evidence_source`
- `ai_systems_involved`
- `verification_method`
- optional supporting fields such as `test_command` and `notes`

See the full field requirements in [Evidence standards](../evidence-standards.md).

## Ledger entries

| Evidence ID | Artifact | Type | Link |
|---|---|---|---|
| `EVID-CODE-001` | `AL-SCHEMA-001` — Atlas ORCS Schema Suite v0.1 | `build_receipt` | [EVID-CODE-001.json](./EVID-CODE-001.json) |
| `EVID-GOV-001` | `AL-MISSION-001` — Mission Charter | `governance_record` | [EVID-GOV-001.json](./EVID-GOV-001.json) |
| `EVID-RESEARCH-001` | `AL-GP-002` — GPTDream++ Vault Manifest | `research_artifact` | [EVID-RESEARCH-001.json](./EVID-RESEARCH-001.json) |

## CI validation status

Evidence entries are checked by [`.github/workflows/evidence-schema-validation.yml`](../../.github/workflows/evidence-schema-validation.yml).

- Validation scope: all `docs/evidence/*.json` files
- Validation checks: valid JSON, required fields present, `schema_version == 0.1`
- Current state: candidate workflow added; status becomes authoritative after the next GitHub Actions run on `main` or an open pull request

## Related docs

- [Evidence coverage dashboard](../evidence-coverage-dashboard.md)
- [Contributor decision tree](../contributor-decision-tree.md)
- [Review SLA](../review-sla.md)
