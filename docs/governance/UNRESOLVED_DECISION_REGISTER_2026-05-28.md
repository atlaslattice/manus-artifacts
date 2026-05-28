---
artifact_id: GOV-UNRESOLVED-DECISION-REGISTER-2026-05-28
title: Unresolved Decision Register
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
---
# Unresolved Decision Register

> **Purpose:** Living register of all open governance decisions, conflicts, SLA breaches, and candidate artifacts awaiting ratification or expiration action. Entries are closed when resolved.

## Open Entries

| Register ID | Date Opened | Type | Artifact / Topic | Priority | Assigned | Due | Status | Resolution |
|---|---|---|---|---|---|---|---|---|
| REG-2026-05-28-001 | 2026-05-28 | BLOCKER | Secret-history audit (Wave 1 Task 1) | P1 | @atlaslattice | — | 🔴 OPEN | Pending owner signoff |
| REG-2026-05-28-002 | 2026-05-28 | BLOCKER | PII audit (Wave 1 Task 3) | P1 | @atlaslattice | — | 🔴 OPEN | Pending owner signoff |
| REG-2026-05-28-003 | 2026-05-28 | DECISION | ADR-0001 public scope ratification (Wave 1 Task 5) | P1 | @atlaslattice | — | 🔴 OPEN | Pending owner ratification |
| REG-2026-05-28-004 | 2026-05-28 | DECISION | Rewrite/no-rewrite decision (Wave 1 Task 7) | P1 | @atlaslattice | — | 🔴 OPEN | Conditional on audit outcomes |
| REG-2026-05-28-005 | 2026-05-28 | CANDIDATE | Wave 2 governance spine (13 artifacts) | P2 | @atlaslattice | 2026-08-28 | 🟡 IN REVIEW | Drafted 2026-05-28; pending ratification |

## Closed Entries

| Register ID | Date Closed | Type | Artifact / Topic | Resolution Summary |
|---|---|---|---|---|
| — | — | — | — | — |

## Entry Type Reference

| Type | Meaning |
|---|---|
| `BLOCKER` | Hard launch gate; must be resolved before public release |
| `DECISION` | Owner/council decision required |
| `CONFLICT` | Two or more artifacts in conflict |
| `CANDIDATE` | Artifact in candidate/review status |
| `SLA_BREACH` | Governance SLA missed; escalation required |
| `EXPIRY` | Candidate artifact approaching or at TTL |

## Adding an Entry

Copy the row format above. Assign the next sequential `REG-YYYY-MM-DD-NNN` ID.  
Close the entry by adding a `Resolution` note and moving the row to **Closed Entries**.

## Related Artifacts

- [Governance Decision Index](./GOVERNANCE_DECISION_INDEX_2026-05-28.md)
- [Governance SLA Targets](./GOVERNANCE_SLA_TARGETS_v0_1.md)
- [Launch Blockers Tracker](../LAUNCH_BLOCKERS_TRACKER.md)
