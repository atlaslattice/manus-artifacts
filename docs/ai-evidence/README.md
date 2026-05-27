# AI Evidence Logging (Axis 10)

Status: candidate implementation set for Aetherforge Axis 10 tasks (109-119).

This folder provides a provenance-first template system for logging AI system
build evidence in public, auditable, non-overclaim form.

## Files

- `AI_EVIDENCE_SCHEMA_v0.1.md` — core field contract
- `templates/AI_BUILD_LOG_TEMPLATE.md`
- `templates/MODEL_EVAL_LOG_TEMPLATE.md`
- `templates/ARCHITECTURE_DECISION_LOG_TEMPLATE.md`
- `templates/TRAINING_DATA_PROVENANCE_LOG_TEMPLATE.md`
- `templates/SAFETY_INCIDENT_LOG_TEMPLATE.md`
- `templates/DRIFT_PERFORMANCE_LOG_TEMPLATE.md`
- `templates/REPRODUCIBILITY_RECEIPT_TEMPLATE.md`
- `templates/AI_CLAIMS_TO_EVIDENCE_MATRIX_TEMPLATE.md`
- `templates/THIRD_PARTY_VALIDATION_LOG_TEMPLATE.md`
- `templates/AI_EVIDENCE_INDEX_TEMPLATE.md`

## Usage

1. Choose the relevant template.
2. Preserve field names and required headers.
3. Attach source lineage for every material claim.
4. Mark unresolved or unverified claims explicitly.
5. Keep canon status as candidate unless ratified.

## Governance Boundary

All artifacts are candidates until full council ratification and adjudication by
@atlaslattice.
