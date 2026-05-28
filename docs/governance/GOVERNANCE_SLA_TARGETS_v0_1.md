---
artifact_id: GOV-GOVERNANCE-SLA-TARGETS-v0-1-2026-05-28
title: Governance SLA Targets
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
version: v0.1
---
# Governance SLA Targets

> **Purpose:** Set response and resolution time targets for governance operations so work does not stall indefinitely.

## SLA Tiers

| Tier | Category | Response SLA | Resolution SLA | Escalation |
|---|---|---|---|---|
| **P0 — Emergency** | Security / PII breach, critical canon error | 4 hours | 24 hours | Immediate @atlaslattice action required |
| **P1 — Launch Gate** | Blocker closing a release gate | 2 business days | 7 days | Escalate to @atlaslattice if unresolved |
| **P2 — Standard Governance** | Ratification, demotion, policy updates | 5 business days | 30 days | Council reminder after 14 days |
| **P3 — Working Material** | Campaign board updates, log reviews | 14 days | 90 days | Owner discretion |
| **P4 — Exploratory** | Dream artifacts, non-canon working notes | No SLA | No SLA | N/A |

## Definitions

- **Response SLA** — Time from an event being opened (PR, issue, conflict report) to first substantive action (acknowledgement + triage assignment).
- **Resolution SLA** — Time from first substantive action to final decision recorded.
- **Business day** — defined as any day @atlaslattice is active on GitHub.

## SLA Clock Pause Conditions

The clock pauses when:
- Awaiting external information or a third party
- Explicitly deferred by @atlaslattice with a written rationale
- Artifact is under grace period (active review, no expiration countdown)

## Monitoring

SLA breaches are logged in the [Unresolved Decision Register](./UNRESOLVED_DECISION_REGISTER_2026-05-28.md) as `SLA_BREACH` entries and reviewed in the monthly governance FAQ update.

## Review Cadence

These SLA targets are reviewed and updated at minimum once per quarter or whenever the repository load profile changes significantly.

## Related Artifacts

- [Ratification Lifecycle](./RATIFICATION_LIFECYCLE_v0_1.md)
- [Candidate Expiration Rules](./CANDIDATE_EXPIRATION_RULES_v0_1.md)
- [Governance FAQ Addendum](./GOVERNANCE_FAQ_ADDENDUM_v0_1.md)
