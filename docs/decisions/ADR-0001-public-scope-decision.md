---
artifact_id: ADR-0001-PUBLIC-SCOPE-DECISION-2026-05-28
title: ADR-0001 Public Scope Decision
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
---
# ADR-0001: Public Scope Decision

- **Status:** Drafted, pending owner ratification
- **Top-50 mapping:** #4
- **Axis mapping:** Axis 2 #15

## Context

Public launch requires an explicit scope boundary defining what is publishable now versus deferred or redacted.

## Decision draft

1. Repository default is public-by-default candidate artifacts.
2. Any sensitive finding from security/PII audits overrides default publication and requires remediation before public release.
3. Scope exceptions must be explicitly listed in blocker and readiness artifacts.

## Consequences

- Enables auditable launch decisions.
- Keeps manual owner ratification as final authority.
- Provides concrete linkage between blocker closeout and launch status.

## Follow-up

Owner ratification required to move this ADR from draft to accepted.
