---
artifact_id: DOC-SENSITIVE-CONTENT-TRIAGE-MATRIX-2026-05-28
title: Sensitive Content Triage Matrix
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
---
# Sensitive Content Triage Matrix

| Content class | Example | Risk level | Required action before public release | Evidence target |
|---|---|---|---|---|
| Credentials/secrets | API keys, tokens, private keys | Critical | Remove + rotate + evaluate history rewrite | Secret audit receipt + rewrite receipt |
| Direct personal data | Medical details, address, personal identifiers | High | Redact or exclude from public scope | PII audit receipt + redaction log |
| Third-party restricted content | Licensed/proprietary text or media | High | Remove or replace with rights-cleared summary | Rights decision record |
| Safety-sensitive operational details | Exploitable security internals | Medium-High | Gate behind responsible disclosure path | Security policy cross-reference |
| Internal-only but non-sensitive draft notes | Incomplete strategy notes | Medium | Mark candidate and scope intentionally | ADR + blocker tracker mapping |
| Public-safe knowledge artifacts | General research and governance docs | Low | Publish under normal candidate controls | Standard metadata/provenance checks |

## Triage rule

When classification is uncertain, escalate to owner review and treat as higher risk until adjudicated.
