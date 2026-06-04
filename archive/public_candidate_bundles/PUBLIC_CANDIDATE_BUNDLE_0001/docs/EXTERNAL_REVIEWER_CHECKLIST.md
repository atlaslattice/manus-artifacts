# External Reviewer Checklist — PUBLIC_CANDIDATE_BUNDLE_0001

```yaml
artifact_id: EXTERNAL_REVIEWER_CHECKLIST_PUBLIC_CANDIDATE_BUNDLE_0001_v0_1
status: candidate_reviewer_checklist
canon_status: not_canon
deployment_status: not_deployed
authority_scope: none
proof_status: not_a_proof
goal: best_in_world_for_openai_operability
```

## First 60 seconds

You are looking at a **candidate public inspection bundle**.

It is meant to help careful reviewers inspect sources, claims, receipts, gaps, and next actions.

It is not canon. It is not deployed. It is not proof. It is not an official endorsement. It is not automatically release-ready.

## Start path

1. Read `README.md`.
2. Read `BUNDLE_0001_FILE_MANIFEST.yaml`.
3. Read `mirror_receipts/mirror_index.yaml`.
4. Read `mirror_receipts/sha_crosswalk.yaml`.
5. Read `docs/BUNDLE_0001_VALIDATION_CHECKLIST.md`.
6. Read `module_packets/MODULE_11_FORKABILITY_SCORECARD_RESULT_v0.1.md`.
7. Open issue #254 for the active P0 forkability hardening queue.
8. Open issue #255 for this external reviewer checklist trail.

## What to verify first

```yaml
first_checks:
  - Does the file exist at the path claimed?
  - Does it have a blob SHA or commit SHA in sha_crosswalk.yaml?
  - Does it state canon_status, deployment_status, authority_scope, and proof_status?
  - Does it distinguish public visibility from proof?
  - Does it distinguish candidate staging from release-readiness?
  - Does it avoid institutional endorsement claims unless a receipt exists?
```

## Forbidden automatic promotions

Never infer:

```yaml
forbidden_promotions:
  - public_repo_means_proven
  - open_source_means_rights_cleared
  - graph_centrality_means_authority
  - issue_opened_means_reviewed
  - bundle_exists_means_release_ready
  - model_output_means_truth
  - Riemann_style_language_means_RH_proof
  - OpenAI_tool_use_means_OpenAI_endorsement
```

## Missing receipt report template

Use this when something is useful but under-receipted.

```yaml
missing_receipt_report:
  reviewer:
  date:
  file_path:
  claim_or_artifact:
  missing_receipt_type:
    - blob_sha
    - commit_sha
    - source_export
    - Notion_export_hash
    - Drive_export_hash
    - license_status
    - privacy_review
    - rights_review
    - external_source
  why_it_matters:
  safest_next_action:
```

## Overclaim report template

Use this when language is too strong for the receipts.

```yaml
overclaim_report:
  reviewer:
  date:
  file_path:
  risky_phrase:
  risk_type:
    - canon_drift
    - deployment_drift
    - proof_drift
    - endorsement_drift
    - rights_drift
    - privacy_drift
    - authority_drift
  safer_replacement:
  needs_human_root_review: true_or_false
```

## SHA / path verification

A strong file receipt should have:

```yaml
sha_path_receipt:
  path:
  branch_or_ref:
  blob_sha:
  commit_sha:
  verification_status:
  verified_by:
  verified_at:
```

A blob SHA confirms file contents. A commit SHA confirms a repository write event. Neither confirms truth, rights clearance, canon, deployment, or proof.

## Privacy / rights / license reminder

Before any artifact is treated as public-release-ready, check:

```yaml
release_review:
  privacy_status:
  rights_status:
  license_status:
  sensitive_terms_status:
  third_party_material_status:
  redline_scan:
  reviewer_lane:
```

If these are absent, the artifact may still be useful, but it should remain candidate / hold-for-review.

## Riemann / S-operator reminder

Allowed:

```yaml
allowed:
  - candidate_operator_seed
  - finite_wire_lattice_diagnostic
  - analytic_research_target
  - baseline_comparison_hypothesis
```

Forbidden:

```yaml
forbidden:
  - proves_Riemann
  - proves_unified_field
  - proves_governance_validity
  - Hilbert_Polya_operator_constructed_without_receipt
```

## Reviewer completion form

```yaml
review_completion:
  reviewer:
  date:
  files_reviewed: []
  passes: []
  warnings: []
  blockers: []
  missing_receipts: []
  overclaims_found: []
  recommended_next_actions: []
  strongest_safe_claim:
```

## Strongest safe claim

This checklist gives external reviewers a safer first path through Bundle 0001 by making boundaries, SHA checks, missing-receipt reporting, overclaim reporting, and release-readiness gates explicit. It does not validate claims, clear rights, prove science, establish canon, or authorize deployment.

## Keeper

```text
Make it kind for strangers.
Make it strict for history.
Verify the path.
Check the SHA.
Flag the crown.
No hidden gaps.
```
