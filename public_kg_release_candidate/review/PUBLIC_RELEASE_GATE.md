# Public Release Gate v0.1

```text
STATUS: PUBLIC-CANDIDATE REVIEW GATE — NOT CANON
CANON: no
DEPLOYMENT: no
AUTHORITY: none
PUBLIC RELEASE: blocked until gate pass and human-root review
```

## Purpose

This gate prevents candidate Atlas Lattice / public knowledge graph materials from being mistaken for canon, deployment, institutional endorsement, or verified truth before review.

## Gate rule

```text
Index first. Validate second. Publish only after gate. Canon only after human-root.
```

## Required pre-release checks

A public-candidate bundle must pass all checks below before any public-release framing is used.

### 1. Source completeness check

- Each source artifact has a source passport or explicit missing-receipt node.
- Each raw export has a preservation state.
- Each partial export is labeled partial.
- Each missing hash is labeled HashGap.
- Each Drive / Notion / GitHub source root has a visibility and export status.

### 2. Sensitive material check

- Health, financial, legal, private, family, identity, security, credentials, and unpublished third-party material are excluded or quarantined.
- Private model outputs are reviewed before inclusion.
- Unclear provenance routes to quarantine.
- Personal data is not released without explicit human-root approval.

### 3. Claim status check

Every claim must be labeled as one of:

- raw_source_statement
- model_summary
- candidate_interpretation
- review_finding
- evidence_supported
- disputed
- blocked_by_missing_receipt
- not_for_public_release

### 4. Overclaim check

The bundle cannot claim:

- canon
- deployment
- OpenAI endorsement
- official OpenAI integration
- proof of repo state without Git receipts
- proof of Notion contents without exports
- proof of Drive raw cargo without export/fidelity checks
- authority from graph centrality
- authority from model consensus
- truth from receipt existence alone

### 5. Public-safe wording check

Allowed wording:

```text
This is a non-canon public knowledge graph staging effort.
This is provenance-first and receipt-first.
GitHub is treated as a receipt shelf, not canon.
Dream/play outputs are candidate deltas, not deployments.
Public release is routed through gates and human-root review.
```

Forbidden wording:

```text
This is canon.
This is deployed.
OpenAI endorses this.
The graph proves this is true.
The repository proves all sources are complete.
The models agreed, so it is authorized.
```

### 6. Human-root decision check

A bundle can move from candidate to public-release only after an explicit human-root decision event records:

- decision_id
- decision_date
- decision_scope
- approved_files
- excluded_files
- unresolved blockers
- promotion_state
- reviewer notes

## Gate result states

```yaml
gate_states:
  blocked: release_not_allowed
  candidate_ready_for_review: review_may_continue
  quarantine_required: sensitive_or_unclear_material_detected
  missing_receipts_required: source_completeness_gap_detected
  public_candidate_approved: public_candidate_may_be_prepared
  public_release_approved: requires_explicit_human_root_decision
```

## Minimum footer for public-candidate files

```text
This artifact is public-candidate review material, not canon, not deployment, and not authority. Human-root review is required before promotion.
```
