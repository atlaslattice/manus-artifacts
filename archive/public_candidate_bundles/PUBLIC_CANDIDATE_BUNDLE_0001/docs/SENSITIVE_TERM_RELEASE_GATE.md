# Sensitive Term Release Gate

```text
STATUS: CANDIDATE STAGING MATERIAL
CANON: no
DEPLOYMENT: no
AUTHORITY: none
MODULE: 11 — Public GitHub / Forkability Excellence
BUNDLE: PUBLIC_CANDIDATE_BUNDLE_0001
```

## Purpose

This gate prevents private, unsafe, unsupported, or high-risk language from entering public GitHub as if it were ready for reuse.

Public intent is not publication permission.

## Sensitive term classes

```yaml
sensitive_term_classes:
  private_identity:
    examples: [addresses, phone_numbers, emails, account_ids, family_details]
    default_release_status: private_hold
  secrets_credentials:
    examples: [api_keys, tokens, passwords, env_values, private_urls]
    default_release_status: do_not_publish
  legal_financial_medical:
    examples: [legal_claims, financial_records, medical_records, insurance_details]
    default_release_status: review_required
  third_party_rights:
    examples: [copyrighted_material, proprietary_docs, partner_claims, vendor_material]
    default_release_status: rights_unclear
  deployment_runtime:
    examples: [deployed, production_ready, live, operational, runtime]
    default_release_status: receipt_required
  authority_canon:
    examples: [canon, ratified, official, approved, single_source_of_truth]
    default_release_status: review_required
  model_contamination:
    examples: [claude_says, model_memory, autonomous_agent_claim, ai_child_authority]
    default_release_status: adversarial_review_required
```

## Release statuses

```yaml
public_release_status:
  - unknown
  - public_ready
  - redact_first
  - private_hold
  - rights_unclear
  - third_party_review_required
  - receipt_required
  - adversarial_review_required
  - do_not_publish
```

## Required checks before public-ready

- [ ] No secrets, keys, tokens, credentials, or env values.
- [ ] No unreviewed private identity material.
- [ ] No unreviewed legal, financial, medical, or security-sensitive material.
- [ ] No third-party rights ambiguity.
- [ ] No unsupported deployment/runtime claims.
- [ ] No unsupported vendor/partner/endorsement claims.
- [ ] No Claude-origin governance authority claims.
- [ ] No canon-like language without explicit ratification receipt.
- [ ] No raw transcript published without public-safe review.

## Safe replacement examples

```yaml
safe_replacements:
  single_source_of_truth: source_index_candidate
  deployed: deployment_claim_requiring_current_receipt
  production_ready: readiness_claim_requiring_validation
  official: artifact_authored_label_not_authority
  canon: canon_like_language_until_ratified
  proven: claim_with_receipts_pending_review
```

## Keeper

```text
Public is powerful.
Power needs gates.
The gate protects the gift.
```
