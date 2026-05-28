# Evidence Standards

> **Status:** CANDIDATE  
> **Artifact Type:** policy / guide  
> **Date:** 2026-05-28  
> **Related:** [Evidence ledger index](./evidence/README.md), [AI evidence ledger schema](./knowledge-graph/ai_evidence_ledger.schema.v0_1.json), [Ratification and Trust Flow](./RATIFICATION_AND_TRUST_FLOW.md)

## Why these standards exist

AI-built and AI-assisted claims must be backed by traceable evidence that a reviewer can inspect, reproduce, or adjudicate. A claim is not sufficiently supported unless it points to a concrete artifact path, a concrete evidence source, a declared verification method, and a trust path for human review.

## What constitutes sufficient evidence for AI-built claims

Sufficient evidence must:

1. identify the artifact by stable ID or operational artifact ID
2. state the exact claim being supported
3. point to a durable source path in the repository
4. record the AI systems involved
5. declare how the claim was verified or reviewed
6. include notes that explain current trust limits when full ratification is still pending

## Required fields by evidence type

### Common fields for all evidence entries

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
- `notes` (strongly recommended)

### Code evidence (`build_receipt`)

Required fields:

- all common fields
- `test_command`

Recommended support:

- passing test count
- receipt or manifest path
- explicit implementation directory

### Governance evidence (`governance_record`)

Required fields:

- all common fields

Recommended support:

- ratification status note
- adjudicator or council review path
- linked governing document

### Research evidence (`research_artifact`)

Required fields:

- all common fields

Recommended support:

- manifest or appendix source
- archive scope note
- source package or vault reference

## Validation receipt standard

A validation receipt is the minimum reproducibility record for a technical claim.

Required fields:

- `receipt_id`
- `receipt_type` = `validation_receipt`
- `artifact_id`
- `artifact_path`
- `validation_date`
- `validator`
- `command`
- `result`
- `summary`
- `evidence_ref`

Preferred format: JSON or Markdown table with machine-readable key/value lines.

Example:

```json
{
  "receipt_id": "VAL-2026-05-28-001",
  "receipt_type": "validation_receipt",
  "artifact_id": "AL-SCHEMA-001",
  "artifact_path": "schemas/atlas_orcs/v0_1",
  "validation_date": "2026-05-26",
  "validator": "pytest",
  "command": "python -m pytest -q tests/adversarial/",
  "result": "pass",
  "summary": "63 tests passing",
  "evidence_ref": "docs/evidence/EVID-CODE-001.json"
}
```

## Migration receipt standard

Use a migration receipt when an artifact is moved, renamed, or structurally re-homed.

Required fields:

- `receipt_id`
- `receipt_type` = `migration_receipt`
- `artifact_id`
- `from_path`
- `to_path`
- `migration_date`
- `reason`
- `performed_by`
- `validation_ref`
- `notes`

## Adjudication request receipt

Use an adjudication request receipt when a candidate artifact is asking for trust-state advancement.

Required fields:

- `request_id`
- `receipt_type` = `adjudication_request`
- `artifact_id`
- `artifact_path`
- `requested_trust_state`
- `submitted_by`
- `submitted_at`
- `evidence_refs`
- `review_links`
- `decision_context`

Route these requests through the [Ratification and Trust Flow](./RATIFICATION_AND_TRUST_FLOW.md).

## Schema reference

Canonical schema reference:

- [docs/knowledge-graph/ai_evidence_ledger.schema.v0_1.json](./knowledge-graph/ai_evidence_ledger.schema.v0_1.json)
- [docs/knowledge-graph/ai_evidence_ledger.seed.v0_1.json](./knowledge-graph/ai_evidence_ledger.seed.v0_1.json)
