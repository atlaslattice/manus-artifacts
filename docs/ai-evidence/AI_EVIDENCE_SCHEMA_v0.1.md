# AI Evidence Schema v0.1

Status: candidate schema, non-canon until ratified.

## Required envelope

```yaml
artifact_id: <stable unique id>
artifact_type: ai_build_log | model_eval_log | architecture_decision_log | training_data_provenance_log | safety_incident_log | drift_performance_log | reproducibility_receipt | claims_evidence_matrix | third_party_validation_log | ai_evidence_index
canon_status: NOT_CANON
created_utc: <ISO-8601>
updated_utc: <ISO-8601>
owner: <human or team>
system_name: <system under evidence>
version: <release or commit-aligned version>
claim_class: observed_fact | interpretation | hypothesis
confidence: C0 | C1 | C2 | C3
human_review_required: true
```

## Required provenance fields

```yaml
source_lineage:
  - source_type: repo_path | issue | pr | commit | workflow_run | external_reference
    locator: <path/url/id>
    snapshot_or_sha: <hash/tag/sha if available>
review_lane:
  reviewer: <name/role>
  status: pending | approved | needs_revision | rejected
  reviewed_utc: <ISO-8601 or null>
```

## Required safety fields

```yaml
overclaim_risk: low | medium | high
contradiction_flags:
  - <id or short description>
open_questions:
  - <question>
```

## Minimum quality gates

- Every non-trivial claim must include at least one source lineage item.
- Every artifact must include explicit review lane status.
- Confidence must not exceed available evidence quality.
- Unknowns must be preserved as unknowns.
