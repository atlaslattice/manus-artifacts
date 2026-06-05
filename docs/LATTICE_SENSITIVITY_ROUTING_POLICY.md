# LATTICE_SENSITIVITY_ROUTING_POLICY_v0.1

STATUS: PUBLIC CANDIDATE POLICY NOTE  
CANON: NO  
DEPLOYMENT: NO  
AUTHORITY: NONE  
OFFICIAL OPENAI CLAIM: NONE

## Purpose

Define candidate routing rules for VIP-sensitive, security-sensitive, crypto-sensitive, export-control-sensitive, personal-sensitive, health-sensitive, and legal-sensitive lattice nodes.

This policy note supports H-S-N entry coordinates and the broader 12D flywheel. It does not grant authority, certify public release, or deploy any system.

## Required schema fields

Every lattice coordinate packet should declare:

```text
sensitivity_class
review_status
public_release_status
authority_scope
deployment_status
receipt_refs
```

## Sensitivity classes

```text
public_safe
private_review
vip_sensitive
security_sensitive
crypto_sensitive
export_control_sensitive
personal_sensitive
health_sensitive
legal_sensitive
blocked_public_release
```

## Routing rules

### public_safe

May be considered for public candidate use only after receipt and wording review.

### private_review

Keep private until reviewed. Do not summarize publicly unless a public-safe derivative is created.

### vip_sensitive

Requires explicit review route. VIP status never grants authority, priority over safety, or public-release permission.

### security_sensitive

Requires gated review. Do not disclose operational details, exploit paths, keys, credentials, sensitive infrastructure, or defensive gaps unless cleared for public-safe release.

### crypto_sensitive

Requires cryptographic review. No node may claim security, post-quantum readiness, migration completeness, or standards compliance without receipts.

### export_control_sensitive

Route to export-control review. Do not publish implementation details, design parameters, or deployment pathways until cleared.

### personal_sensitive

Protect personal data, private identity details, private messages, financial details, addresses, and other sensitive personal context.

### health_sensitive

Protect medical, clinical, diagnostic, treatment, insurance, and care-context details unless explicitly cleared and public-safe.

### legal_sensitive

Protect privileged, legal-strategy, dispute, complaint, contractual, and litigation-sensitive content unless explicitly cleared.

### blocked_public_release

Do not publish. Preserve as a private or quarantined receipt where appropriate.

## Invariants

```text
Sensitivity is a routing flag, not authority.
VIP does not mean public.
Security-sensitive does not mean safe to disclose.
Crypto-sensitive does not mean secure.
Post-quantum label does not mean migration complete.
Export-control review is a gate, not a decoration.
Private lineage should be preserved without forcing public exposure.
```

## Public-safe transformation rule

Sensitive source material may produce a public-safe derivative only when:

```text
1. private source lineage is preserved internally;
2. public wording removes sensitive details;
3. release status is explicitly changed by review;
4. authority_scope remains none unless separately ratified;
5. receipts support the claim without exposing protected material.
```

## Keeper

```text
Address the node.
Declare the sensitivity.
Preserve the receipt.
Gate the release.
Never confuse visibility with permission.
```
