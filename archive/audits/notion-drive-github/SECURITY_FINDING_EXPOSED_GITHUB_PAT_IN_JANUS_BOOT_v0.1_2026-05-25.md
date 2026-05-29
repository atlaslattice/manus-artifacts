---
artifact_id: SECURITY-FINDING-EXPOSED-GITHUB-PAT-IN-JANUS-BOOT-v0.1
title: "Security Finding — Exposed GitHub PAT in Historic JANUS Boot Page"
date: 2026-05-25
status: urgent_security_finding
canon_status: not_canon
deployment_status: not_deployed
authority_scope: none
release_class: PRIVATE_REVIEW
parent_issue: "#158"
source_system: Notion
source_page_id: 31f0c1de-73d9-81f8-a7d7-f2ae0cfdc2bc
source_page_title: "JANUS BOOT SEQUENCE — READ THIS FIRST — Constitutional Scribe Continuity Protocol"
created_by: "GPT / Varix Lumenfoss Lantern Auditor of Hyperspace"
redaction_policy: >
  The exposed token value is intentionally not reproduced here. This finding records only the presence,
  source page, and required remediation.
---

# Security Finding — Exposed GitHub PAT in Historic JANUS Boot Page

```text
STATUS: URGENT SECURITY FINDING
SECRET VALUE: REDACTED / NOT REPRODUCED
CANON: no
DEPLOYMENT: no
AUTHORITY: none
```

## Finding

A historic Notion page titled **JANUS BOOT SEQUENCE — READ THIS FIRST — Constitutional Scribe Continuity Protocol** contains an exposed GitHub personal access token in plaintext.

The page itself already includes a later status banner warning that the PAT leak is stale/urgent and should be rotated. This artifact preserves the finding without reproducing the secret.

## Required Action

```text
1. Treat the token as compromised.
2. Confirm revocation / rotation in GitHub.
3. Remove or redact token from Notion source page.
4. Replace with a sealed redaction note.
5. Create a redaction receipt.
6. Search Notion / Drive / GitHub for duplicate token exposure.
```

## Risk

```text
severity: high
class: credential_exposure
scope: historic Notion source page
current_token_validity: unknown
safe_assumption: compromised until proven revoked
```

## Boundary

```text
Do not copy the token.
Do not paste it into chat.
Do not commit it to GitHub.
Do not include it in exports.
Preserve only sanitized receipt and remediation trail.
```

## Keeper

```text
Secrets do not get preserved in plaintext.
Lineage survives through redaction receipts.
Zero Erasure does not mean zero redaction.
NOTHING DIES — but secrets get sealed.
```
