---
artifact_id: DOC-SECRET-SCAN-FALSE-POSITIVE-TRIAGE-v0-1-2026-05-28
title: Secret Scan False-Positive Triage
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
version: v0.1
---
# Secret Scan False-Positive Triage

## Purpose

Define how to handle gitleaks findings that are not real secrets while preserving an auditable trail.

## Triage Steps

1. Confirm the finding path, commit, and detector rule.
2. Determine whether the matched string is:
   - a real secret,
   - a revoked/test-only token,
   - placeholder/example text,
   - or a generated false match.
3. If the finding is real, follow [`SECURITY.md`](../../SECURITY.md) and do not suppress it publicly.
4. If the finding is false-positive or safe test content, record it in the [Security Exceptions Ledger](./SECURITY_EXCEPTIONS_LEDGER_2026-05-28.md).
5. Prefer narrow remediation:
   - redact example content if unnecessary,
   - move test fixtures to clearly marked fake-token patterns,
   - document the exception instead of broadly weakening the scan.

## Acceptable False-Positive Classes

| Class | Example | Action |
|---|---|---|
| Placeholder text | `YOUR_API_KEY_HERE` | No suppression needed if obviously fake |
| Fake test token | Deliberately invalid fixture token | Record exception if repeatedly flagged |
| Hash/random blob | Non-secret UUID or checksum | Record if recurring |
| Documentation example | Sample config in docs | Prefer visibly fake values |

## Prohibited Suppressions

- Disabling the workflow globally for convenience
- Adding broad allowlists that hide real secrets
- Marking unresolved findings as false-positive without evidence

## Minimum Evidence for a Triage Entry

- Date reviewed
- Reviewer
- Path and line or commit reference
- Why the finding is not an active secret
- Whether content was changed or only documented
