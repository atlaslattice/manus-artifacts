# Claim Shredder Rubric v0.1

```text
STATUS: PUBLIC-CANDIDATE REVIEW RUBRIC — NOT CANON
CANON: no
DEPLOYMENT: no
AUTHORITY: none
PURPOSE: shred overclaims before public-candidate release
```

## Purpose

The Claim Shredder turns broad statements into reviewable claim packets. It prevents clean prose from hiding uncertainty, missing receipts, source gaps, or authority leakage.

## Core rule

```text
No claim leaves staging without status, source, evidence, risk, and review route.
```

## Claim packet fields

Each public-facing claim should be reduced to:

```yaml
claim_packet:
  claim_id:
  claim_text:
  claim_type:
  source_refs:
  evidence_refs:
  confidence:
  public_safe: yes | no | conditional
  blockers:
  missing_receipts:
  overclaim_risks:
  reviewer:
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
- blocked_claim
- not_public_safe

## Shred questions

For every claim, ask:

1. Who or what is the source?
2. Is the source exported or only referenced?
3. Is there a hash or durable receipt?
4. Is the claim about a fact, interpretation, ambition, design, or authority?
5. Could the claim imply canon, deployment, endorsement, or institutional approval?
6. Could the claim expose sensitive material?
7. Is the claim safe to publish as written?
8. What would falsify or downgrade it?
9. What review lane owns it?
10. What graph node or edge should represent the uncertainty?

## Required downgrades

Use these downgrades whenever needed:

| Risk | Safer wording |
|---|---|
| canon leakage | candidate / proposed / review-stage |
| deployment leakage | not deployed / simulation-only / staging |
| endorsement leakage | no endorsement / no official integration claim |
| truth laundering | receipt exists, claim still requires review |
| model consensus leakage | model agreement is not authority |
| public release leakage | public-candidate, release blocked pending gate |

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
```

## Pass condition

A claim passes only when it has:

- a source reference or explicit missing-receipt node
- a public-safe wording review
- no canon/deployment/authority leakage
- a review state
- a route to human-root if promotion is requested

## Keeper line

Beautiful prose does not launder weak claims. Shred gently, preserve lineage, route review.
