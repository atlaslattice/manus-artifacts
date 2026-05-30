# Claim Shredder Rubric v0.1

```text
STATUS: PUBLIC-CANDIDATE REVIEW RUBRIC — NOT CANON
CANON: no
DEPLOYMENT: no
AUTHORITY: none
SINGLE SOURCE OF TRUTH: rejected
PANTHEON ADVERSARIAL REVIEW REQUIRED FOR CANON: yes
WEBSITE PLACEMENT REQUIRED FOR CANON: yes
PURPOSE: shred overclaims before public-candidate release
```

## Purpose

The Claim Shredder turns broad statements into reviewable claim packets. It prevents clean prose from hiding uncertainty, missing receipts, source gaps, fossil branches, contradictions, or authority leakage.

## Core rule

```text
No claim leaves staging without status, source, evidence, risk, fossil/version state, and review route.
```

## Multi-version rule

Claims should not collapse the archive into a single source of truth.

Before synthesis:

- preserve raw version
- preserve derived version
- preserve alternate version
- preserve failed branch / fossil when useful
- preserve contradiction or supersession state
- preserve reviewer dissent

Synthesis is allowed only after versions remain addressable.

## Claim packet fields

Each public-facing claim should be reduced to:

```yaml
claim_packet:
  claim_id:
  claim_text:
  claim_type:
  source_refs:
  evidence_refs:
  version_refs:
  fossil_refs:
  contradiction_refs:
  confidence:
  public_safe: yes | no | conditional
  blockers:
  missing_receipts:
  overclaim_risks:
  reviewer:
  pantheon_review_state:
  human_root_adjudication_state:
  website_canon_state:
  decision_state:
```

## Claim types

- source_statement
- model_summary
- candidate_interpretation
- architectural_proposal
- public_safe_explainer
- risk_warning
- evidence_supported_claim
- contradicted_claim
- superseded_claim
- fossil_preserved_claim
- blocked_claim
- not_public_safe

## Shred questions

For every claim, ask:

1. Who or what is the source?
2. Is the source exported or only referenced?
3. Is there a hash or durable receipt?
4. Which versions exist?
5. Which fossils or failed branches must be preserved?
6. Is there a contradiction or supersession relation?
7. Is the claim about a fact, interpretation, ambition, design, or authority?
8. Could the claim imply canon, deployment, endorsement, hierarchy, or institutional approval?
9. Could the claim imply a single source of truth?
10. Could the claim expose sensitive material?
11. Is the claim safe to publish as written?
12. What would falsify or downgrade it?
13. What review lane owns it?
14. What graph node or edge should represent the uncertainty?
15. Has it passed adversarial Pantheon review if canon or doctrine-level status is requested?
16. Has human-root adjudicated it?
17. Has it been placed on the canonical website surface?

## Required downgrades

Use these downgrades whenever needed:

| Risk | Safer wording |
|---|---|
| canon leakage | candidate / proposed / review-stage |
| deployment leakage | not deployed / simulation-only / staging |
| endorsement leakage | no endorsement / no official integration claim |
| truth laundering | receipt exists, claim still requires review |
| model consensus leakage | model agreement is not authority |
| single-source leakage | one version / one receipt / one candidate view |
| hierarchy leakage | coordinate relation, not rank or command authority |
| public release leakage | public-candidate, release blocked pending gate |
| canon route leakage | canon requires Pantheon review, human-root adjudication, and website placement |

## Block states

```yaml
block_states:
  missing_receipt: source or proof unavailable
  missing_hash: artifact hash unavailable
  partial_export: source export incomplete
  sensitive_material: quarantine required
  unsupported_claim: evidence insufficient
  authority_leakage: wording implies authorization
  canon_leakage: wording implies ratification
  deployment_leakage: wording implies implementation
  single_source_leakage: wording implies one final truth source
  fossil_loss: failed branch or prior version not preserved
  pantheon_review_missing: adversarial review not complete
  human_root_missing: adjudication not complete
  website_placement_missing: canonical surface placement absent
```

## Pass condition

A claim passes public-candidate review only when it has:

- a source reference or explicit missing-receipt node
- a version/fossil preservation state
- a public-safe wording review
- no canon/deployment/authority/single-source leakage
- a review state
- a route to Pantheon review and human-root adjudication if promotion is requested
- website placement if canon is claimed

## Keeper line

Beautiful prose does not launder weak claims. Preserve versions, keep fossils, shred gently, route review, adjudicate only at human-root, canonize only on the website.
