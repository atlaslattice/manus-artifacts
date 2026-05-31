# Bundle 0001 Validation Checklist

```yaml
artifact_id: BUNDLE_0001_VALIDATION_CHECKLIST_v0_1
bundle_id: PUBLIC_CANDIDATE_BUNDLE_0001
status: candidate_validation_checklist
canon_status: not_canon
deployment_status: not_deployed
authority_scope: none
proof_status: not_a_proof
goal: best_git_on_earth
```

## Purpose

Give an external reviewer or swarm child a safe, concrete way to inspect PUBLIC_CANDIDATE_BUNDLE_0001 without mistaking visibility for truth, graph structure for authority, or candidate staging for release-readiness.

This checklist is intentionally boring. Boring checks make the beautiful work safer.

## Quick validation path

1. Confirm the file path exists.
2. Confirm the file has a blob SHA or commit SHA in `mirror_receipts/sha_crosswalk.yaml`.
3. Confirm the file declares status, canon status, deployment status, and authority scope.
4. Confirm any strong claim has a receipt, blocker, or review lane.
5. Confirm no private raw cargo is exposed.
6. Confirm rights/license status is either resolved or explicitly pending.
7. Confirm scientific/math claims are marked candidate unless independently reviewed.
8. Confirm Riemann/S-operator language does not claim proof.
9. Confirm OpenAI/GitHub/Microsoft/Google/xAI are not described as endorsers unless a receipt exists.
10. Confirm next safest action is written.

## Required fields per candidate file

```yaml
required_fields:
  - artifact_id_or_title
  - path
  - status
  - canon_status
  - deployment_status
  - authority_scope
  - source_scope_or_source_inputs
  - receipts_or_missing_receipts
  - blockers_or_review_required
  - strongest_safe_claim
  - overclaims_to_avoid
  - next_safest_action
```

## Status values

```yaml
allowed_status_values:
  canon_status:
    - not_canon
    - canon_candidate
    - canon
    - rejected
    - unknown
  deployment_status:
    - not_deployed
    - inert
    - staging
    - deployed
    - unknown
  authority_scope:
    - none
    - advisory_only
    - human_root_required
    - authorized_by_human_root
    - unknown
  proof_status:
    - not_a_proof
    - proof_target
    - externally_reviewed
    - unknown
```

## File-level checks

```yaml
file_checks:
  existence:
    pass: file exists at stated path
    fail: path missing or ambiguous
  sha_receipt:
    pass: blob_sha or commit_sha is recorded
    warn: blob_sha pending but file exists
    fail: no SHA and no reason
  boundary_header:
    pass: non-canon / not deployed / no authority visible near top
    fail: status absent or buried
  source_scope:
    pass: source inputs are named
    warn: source class named but not path-specific
    fail: no source scope
  release_status:
    pass: public/private/sensitive/license status visible or explicitly pending
    warn: pending but routed
    fail: public reuse implied with no rights status
  overclaim_lint:
    pass: no forbidden claims or risky phrases are bounded
    fail: proof/deployment/endorsement/canon claims without receipt
```

## Bundle-level checks

```yaml
bundle_checks:
  front_door:
    target: START_HERE or README equivalent
    current_note: START_HERE exists under public_candidate_bundle_0001; archive bundle path needs reconciliation
  manifest:
    target: BUNDLE_0001_FILE_MANIFEST.yaml
    current_note: manifest exists but planned-vs-present statuses need reconciliation
  mirror_index:
    target: mirror_receipts/mirror_index.yaml
    current_note: exists as candidate machine-readable mirror map
  sha_crosswalk:
    target: mirror_receipts/sha_crosswalk.yaml
    current_note: exists but many commit SHAs/export hashes remain pending
  forkability_scorecard:
    target: module_packets/MODULE_11_FORKABILITY_SCORECARD_RESULT_v0.1.md
    current_note: exists; score is candidate baseline, not trophy
  external_reviewer_path:
    target: FIRST_12_PUBLIC_INSPECTION_ISSUES or issue templates
    current_note: needs direct inspection and label/issue route confirmation
```

## Forbidden automatic promotions

```yaml
never_infer:
  - public_repo_means_proven
  - open_source_means_rights_cleared
  - issue_opened_means_reviewed
  - bundle_exists_means_release_ready
  - graph_centrality_means_authority
  - model_consensus_means_truth
  - Riemann_style_language_means_RH_proof
  - OpenAI_tool_use_means_OpenAI_endorsement
```

## Validation commands / manual equivalents

Use these as manual checks until scripts exist.

```text
# 1. Search for status headers
Search each candidate file for:
canon_status
CANON:
Deployment:
authority_scope
proof_status

# 2. Search for risky terms
Search each candidate file for:
official
endorsed
proven
deployed
canonical
production-ready
single source of truth
Riemann proof
unified field proven

# 3. Check SHA crosswalk
For each public candidate file, ensure one row exists in:
archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/mirror_receipts/sha_crosswalk.yaml

# 4. Check release gate
For every file intended for public reuse, ensure privacy/rights/license status is present or explicitly pending.

# 5. Check contribution path
A stranger should be able to answer:
Where do I start?
What can I safely inspect?
What should I not assume?
How do I report a missing receipt?
```

## Reviewer result template

```yaml
review_result:
  reviewer:
  date:
  file_or_surface:
  pass:
  warnings: []
  blockers: []
  missing_receipts: []
  overclaims_found: []
  safest_next_action:
  strongest_safe_claim:
```

## Strongest safe claim

This checklist makes PUBLIC_CANDIDATE_BUNDLE_0001 easier to inspect safely by naming required fields, forbidden promotions, SHA/release checks, and reviewer result format. It does not validate the bundle, resolve rights, establish canon, prove claims, or authorize release.

## Keeper

```text
Validate the path.
Verify the SHA.
Read the boundary.
Flag the crown.
Preserve the gap.
```
