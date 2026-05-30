# Public Release Gate v0.1

```text
STATUS: PUBLIC-CANDIDATE REVIEW GATE — NOT CANON
CANON: no
DEPLOYMENT: no
AUTHORITY: none
PUBLIC RELEASE: blocked until gate pass and human-root review
PANTHEON ADVERSARIAL REVIEW REQUIRED: yes
WEBSITE PLACEMENT REQUIRED FOR CANON: yes
SINGLE SOURCE OF TRUTH: rejected
```

## Purpose

This gate prevents candidate Atlas Lattice / public knowledge graph materials from being mistaken for canon, deployment, institutional endorsement, verified truth, hierarchy, or a single source of truth before review.

## Gate rule

```text
Many versions before synthesis. Fossils preserved. No hierarchy. Publish only after gates. Canon only after Pantheon adversarial review, human-root adjudication, and website placement.
```

## Required pre-release checks

A public-candidate bundle must pass all checks below before any public-release framing is used.

### 1. Source completeness check

- Each source artifact has a source passport or explicit missing-receipt node.
- Each raw export has a preservation state.
- Each partial export is labeled partial.
- Each missing hash is labeled HashGap.
- Each Drive / Notion / GitHub source root has a visibility and export status.
- Each fossil or failed branch has a preservation state when relevant.

### 2. Multi-version preservation check

- Raw logs are preserved.
- Derived artifacts are separate from raw logs.
- Competing versions are preserved before synthesis.
- Failed branches are preserved as fossils instead of silently deleted.
- Contradictions and supersessions are explicit graph objects.
- No review packet claims to be the only valid source.

### 3. Sensitive material check

- Health, financial, legal, private, family, identity, security, credentials, and unpublished third-party material are excluded or quarantined.
- Private model outputs are reviewed before inclusion.
- Unclear provenance routes to quarantine.
- Personal data is not released without explicit human-root approval.

### 4. Claim status check

Every claim must be labeled as one of:

- raw_source_statement
- model_summary
- candidate_interpretation
- review_finding
- evidence_supported
- disputed
- contradicted
- superseded
- fossil_preserved
- blocked_by_missing_receipt
- not_for_public_release

### 5. Overclaim check

The bundle cannot claim:

- canon
- deployment
- OpenAI endorsement
- official OpenAI integration
- single source of truth
- hierarchy by default
- proof of repo state without Git receipts
- proof of Notion contents without exports
- proof of Drive raw cargo without export/fidelity checks
- authority from graph centrality
- authority from model consensus
- truth from receipt existence alone

### 6. Public-safe wording check

Allowed wording:

```text
This is a non-canon public knowledge graph staging effort.
This is provenance-first and receipt-first.
Many versions are preserved before synthesis.
Fossils and failed branches are preserved.
GitHub is treated as a receipt shelf, not canon.
Dream/play outputs are candidate deltas, not deployments.
Public release is routed through gates, adversarial Pantheon review, and human-root adjudication.
Canon requires placement on the canonical website surface.
```

Forbidden wording:

```text
This is canon.
This is deployed.
OpenAI endorses this.
The graph proves this is true.
This repository is the single source of truth.
The repository proves all sources are complete.
The models agreed, so it is authorized.
A GitHub merge creates canon.
```

### 7. Pantheon adversarial review check

Doctrine-level and public-canon claims require adversarial review before human-root adjudication.

The review packet should record:

- reviewers / council seats
- objections
- contradictions
- missing receipts
- unsupported claims
- quarantine requirements
- recommended public-safe wording
- dissenting versions preserved
- fossils preserved

### 8. Human-root adjudication and website placement check

A bundle can move from candidate to canon only after explicit human-root adjudication and placement on the canonical website surface.

The decision event records:

- decision_id
- decision_date
- decision_scope
- approved_files
- excluded_files
- unresolved blockers
- dissenting versions preserved
- fossilized branches
- promotion_state
- website canonical URL if promoted
- reviewer notes

## Gate result states

```yaml
gate_states:
  blocked: release_not_allowed
  candidate_ready_for_review: review_may_continue
  quarantine_required: sensitive_or_unclear_material_detected
  missing_receipts_required: source_completeness_gap_detected
  pantheon_review_required: adversarial_review_required_before_adjudication
  human_root_adjudication_required: human_root_decision_needed
  website_placement_required: canon_not_possible_until_placed_on_site
  public_candidate_approved: public_candidate_may_be_prepared
  public_release_approved: requires_explicit_human_root_decision
  canon_promoted: requires_website_placement_after_adjudication
```

## Minimum footer for public-candidate files

```text
This artifact is public-candidate review material, not canon, not deployment, and not authority. Many versions are preserved before synthesis. Pantheon adversarial review, human-root adjudication, and website placement are required before canon.
```
