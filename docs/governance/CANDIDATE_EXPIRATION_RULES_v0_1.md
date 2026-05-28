---
artifact_id: GOV-CANDIDATE-EXPIRATION-RULES-v0-1-2026-05-28
title: Candidate Expiration Rules
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
version: v0.1
---
# Candidate Expiration Rules

> **Purpose:** Define when and how `CANDIDATE` artifacts expire (transition to `ARCHIVED`) if they are not promoted to `RATIFIED` within a defined window.

## Expiration Tiers

| Tier | Category | Default TTL | Extension Policy |
|---|---|---|---|
| **Critical Path** | Safety, PII, security, ADRs blocking launch | 30 days | May extend 30 days with written rationale |
| **Standard** | Governance, evidence, metadata artifacts | 90 days | May extend 90 days once with council note |
| **Working** | Planning boards, campaign artifacts, work logs | 180 days | May extend indefinitely with owner sign-off |
| **Dream/Non-Canon** | TIDELOCKBrain logs, REM journals | No expiration | Preserved as institutional memory |

## TTL Start Date

The TTL clock starts from the `created` frontmatter date. If an artifact was created before this policy was adopted (pre-2026-05-28), its TTL clock starts 2026-05-28.

## Expiration Process

1. **Review sweep** — Run monthly by the governance steward (or CI script when available).
2. **Notification** — Add an `expiry_notice` flag in frontmatter 14 days before expiration.
3. **Expiration action** — At TTL+0, status changes to `ARCHIVED` unless promoted or extended.
4. **Registry entry** — All expirations logged in the [Unresolved Decision Register](./UNRESOLVED_DECISION_REGISTER_2026-05-28.md) and [Governance Decision Index](./GOVERNANCE_DECISION_INDEX_2026-05-28.md).

## Expiration Frontmatter Fields

```yaml
expiry_date: YYYY-MM-DD          # computed TTL end date
expiry_notice: true               # set 14 days before expiry
expiry_extended: false            # set true if extension granted
expiry_extension_rationale: ""    # required if extended
```

## Grace Period for Artifacts Under Active Review

Any artifact with an open review thread (`UNDER_REVIEW`) is automatically in grace period — TTL clock paused until review closes.

## Exceptions — No Expiration

- Any `RATIFIED` artifact (expiration does not apply)
- Constitutional / Tier-1 domain artifacts pending major release
- Any artifact explicitly exempted by @atlaslattice in writing

## Related Artifacts

- [Ratification Lifecycle](./RATIFICATION_LIFECYCLE_v0_1.md)
- [Unresolved Decision Register](./UNRESOLVED_DECISION_REGISTER_2026-05-28.md)
- [Canon Ownership Map](./CANON_OWNERSHIP_DOMAIN_MAP_v0_1.md)
