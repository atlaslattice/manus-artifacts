---
artifact_id: SEC-POLICY-SECURITY-CHAMPION-ROTATION-001
title: Security Champion Rotation Policy
status: candidate
created: 2026-05-28
owner: council
tags: [security, governance, community, rotation]
---

# Security Champion Rotation Policy

> Defines the security champion role, responsibilities, and rotation schedule.

status: candidate

---

## What Is a Security Champion?

The Security Champion is the designated council member responsible for security awareness, triage coordination, and proactive security hygiene in a given period.

This is not a full-time role — it's a rotating accountability that ensures security is always someone's job, not everyone's vague responsibility.

---

## Responsibilities

| Responsibility | Frequency |
|--------------|-----------|
| Review Dependabot alerts | Weekly |
| Review secret scanning alerts | Weekly |
| Triage CodeQL findings | Per PR |
| Run quarterly security audit | Quarterly |
| Update [PUBLIC_RISK_REGISTER.md](./PUBLIC_RISK_REGISTER.md) | Quarterly |
| Review workflow permissions | Quarterly |
| Coordinate with external security reporters | As needed |
| Deliver security awareness update to council | Monthly (brief) |

---

## Rotation Schedule

| Period | Security Champion | Notes |
|--------|-----------------|-------|
| 2026 Q2 (Apr–Jun) | @atlaslattice | Founding period — no rotation yet |
| 2026 Q3 (Jul–Sep) | @atlaslattice | Until council expanded |
| 2026 Q4+ | Rotating council member | Once ≥ 3 active council members |

Rotation frequency: **quarterly** (once council is large enough).

---

## Handoff Process

At the end of each rotation:
1. Outgoing champion creates a handoff note in `archive/governance/SECURITY_CHAMPION_HANDOFF_YYYY_QN.md`
2. Note includes: open alerts, accepted risks, pending audits, lessons learned
3. Incoming champion acknowledges the handoff in the same file

---

## Escalation

If the Security Champion identifies a Critical severity issue:
- Immediately notify @atlaslattice regardless of time
- Per [INCIDENT_RESPONSE_RUNBOOK.md](./INCIDENT_RESPONSE_RUNBOOK.md)

---

*Atlas Lattice Foundation · status: candidate*
