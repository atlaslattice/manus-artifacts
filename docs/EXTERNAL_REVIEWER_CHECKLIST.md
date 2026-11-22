# External reviewer checklist — Atlas Public Candidate Bundle 0001

**Status: PUBLIC REVIEW CANDIDATE · CANON: NO · DEPLOYMENT: NO · AUTHORITY: NONE · RELEASE: NOT APPROVED**

This is the **current cold-reviewer entry point** for [Manus issue #255](https://github.com/atlaslattice/manus-artifacts/issues/255), not a claim that the bundle is verified. It reconciles rather than overwrites the earlier [archived full reviewer checklist](../archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/docs/EXTERNAL_REVIEWER_CHECKLIST.md).

## First 60 seconds: a safe route

1. Open the current [public candidate START HERE](../public_candidate_bundle_0001/START_HERE.md) and read its release boundary.
2. Open [Public Release Gate](../public_candidate_bundle_0001/docs/PUBLIC_RELEASE_GATE.md), which defaults uncertain source rights, private content and unsupported proof claims to HOLD.
3. Open the separate [archived Bundle 0001 README](../archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/README.md). This is a **distinct historical bundle surface**, not proof of byte-for-byte mirror parity.
4. In that archived surface, inspect [file manifest](../archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/BUNDLE_0001_FILE_MANIFEST.yaml), [mirror index](../archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/mirror_receipts/mirror_index.yaml), [SHA crosswalk](../archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/mirror_receipts/sha_crosswalk.yaml), and [validation checklist](../archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/docs/BUNDLE_0001_VALIDATION_CHECKLIST.md).
5. Write down every missing receipt, contradictory claim and license/privacy issue. Do **not** treat public visibility, reported local tests, a graph edge, or a merge as release or canon approval.

## Mandatory per-artifact status check

| Check | Required reviewer evidence |
| --- | --- |
| Exact source | Repository owner/name, branch or immutable commit SHA, path, observed content, raw_export_status |
| Status | Candidate/contradicted/quarantined/superseded where applicable; canon_status, deployment_status, authority_scope and proof_status |
| Provenance | Original source owner and source-rights scope; blob SHA for contents and separately a commit SHA for history |
| Reproducibility | Commands, execution environment, real test outputs or an explicit NOT RUN / NOT TESTABLE reason |
| Release | privacy_status, rights_status, license_status, redline_scan, third_party_material_status, reviewer and release audience |
| Human action | Explicit human decision receipt and scope before publication, deployment, governance or private-source transfer |
| Preservation | Non-destructive predecessor and dissent/contradiction records; lawful privacy deletion remains a separate constraint |

A SHA-1 Git **blob** verifies the retrieved object content under Git object encoding; a **commit** identifies a repository revision. Neither authenticates scientific truth, copyright permission, or identity. The earlier crosswalk may contain unresolved or stale values—verify every link instead of copying it forward.

## Forbidden inference

- Public GitHub ≠ rights-cleared source.
- Open source ≠ approval to republish proprietary or private archives.
- Test passing ≠ deployed integration or scientific validity.
- Official-sounding text, structured math, Riemann/S-operator vocabulary, model consensus and graph centrality ≠ proof, canon, endorsement or jurisdiction.
- An AI, Play resident or automation thread ≠ an independently authenticated human approver.
- Private Play/Social/Quiet/Dream/Imagine records ≠ Work inputs without separate rights, explicit consent and scope.

### Missing-receipt report (copy into issue #254 or the scoped source issue)

```yaml
kind: missing_receipt
artifact_id: 
repository: atlaslattice/manus-artifacts
branch_or_commit:
path:
raw_export_status: unknown
claimed_evidence:
missing_receipt_type: # source-root | SHA | test log | rights | privacy | license | external citation
observed_result: # verified | reported_only | stub | 404_at_claimed_ref | blocked
why_it_matters:
next_safe_action:
reviewer:
review_date:
```

### Overclaim report

```yaml
kind: overclaim
artifact_id:
source_path_and_ref:
risky_phrase:
category: # canon | deployment | mathematical_proof | endorsement | rights | identity | privacy
strongest_safe_replacement:
contradicting_source:
dissent_retention_ref:
needs_human_root_review: true
```

## Completion gate for this reviewer entry point

A careful stranger must be able to locate the candidate START HERE, current release gate, archived bundle source and SHA crosswalk, identify which claims were *reported* instead of tested, and file a missing receipt or overclaim report. **This checklist's presence meets only that navigation/documentation requirement**, not the wider [forkability hardening issue #254](https://github.com/atlaslattice/manus-artifacts/issues/254).

## Explicit science boundary

Finite coordinate or spectral diagnostics are candidate engineering/research. No supplied receipt proves the Riemann Hypothesis, a unified field, a complete 1,728-node scientific ontology, a hosted agent federation or validated governance. The burden of independent proof is not satisfied by notation.

**Keeper:** Make it easy to find the source, hard to mistake a claim for a result, and impossible to mistake review documentation for authorization.
