# Lattice KG Glossary v0.1

This module is an upstream candidate packet, not proof.

CANON: no
DEPLOYMENT: no
AUTHORITY: none

- **artifact_id**: Stable deterministic identifier for a graph artifact.
- **candidate artifact**: Non-canon, non-deployable artifact pending review.
- **claim_class**: Provenance class for record type (e.g., raw, parsed, claim, review, decision, action).
- **lifecycle_state**: Stage in candidate flow (e.g., intake, in_review, blocked, ready_for_adjudication).
- **contradiction_links**: References to artifacts that challenge or conflict with a claim.
- **supersedes_links**: References to older artifacts replaced by the current one.
- **retrieval reliability**: Deterministic success of lookup by `artifact_id`, path, or indexed filters.
- **quest-loop receipt**: Structured execution note containing scope, validation, blockers, and next safest action.
- **quality gate**: Automated validation and test checks that must pass for merge readiness.
- **M0/M1/M2/M3/M4**: Maturity scale from seed to world-class reproducibility.
