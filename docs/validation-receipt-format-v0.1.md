# Validation Receipt Format v0.1

> **Status:** CANDIDATE
> **Artifact Type:** spec
> **Date:** 2026-05-28

<!-- METADATA
stable_id: AL-CI-003
lifecycle_state: CANDIDATE
owner: @atlaslattice
date_created: 2026-05-28
canon_status: candidate
-->

## Candidate Status Note

This receipt format is a candidate-state contract for recording validation evidence across CI and manual review runs.

## Required Fields

Validation receipts must include the following fields:

- `receipt_id`
- `run_date`
- `workflow_run_id`
- `checks_run` (list)
- `checks_passed` (list)
- `checks_failed` (list)
- `overall_status`
- `generated_by`

## Format Guidance

- `receipt_id` should be globally unique within the evidence log namespace.
- `run_date` should use ISO 8601 UTC timestamps.
- `workflow_run_id` should align with the originating GitHub Actions run when automation produced the receipt.
- `checks_run`, `checks_passed`, and `checks_failed` should preserve deterministic ordering for audit diffs.
- `overall_status` should be one of `PASS`, `FAIL`, or `WARN`.
- `generated_by` should identify the workflow, agent, or operator that assembled the receipt.

## Example JSON

```json
{
  "receipt_id": "AL-LOG-VAL-2026-05-28-001",
  "run_date": "2026-05-28T09:00:00Z",
  "workflow_run_id": "1234567890",
  "checks_run": [
    "validate_metadata_completeness",
    "validate_provenance_fields",
    "validate_lifecycle_consistency"
  ],
  "checks_passed": [
    "validate_provenance_fields"
  ],
  "checks_failed": [
    "validate_metadata_completeness",
    "validate_lifecycle_consistency"
  ],
  "overall_status": "FAIL",
  "generated_by": "github-actions/validation-hardening"
}
```

## Schema Reference

This format is intended to pair with the candidate evidence and logging surfaces defined in the Atlas Lattice knowledge-graph and CI validation stack. A future schema publication can codify this document as a machine-readable JSON Schema once the field set is ratified.
