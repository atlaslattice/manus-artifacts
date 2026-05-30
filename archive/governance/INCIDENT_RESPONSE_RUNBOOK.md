# Incident Response Runbook

*Atlas Lattice Foundation · Aetherforge Mission #21 · 2026-05-28*

status: candidate

> Step-by-step playbook for responding to security incidents, data exposures, and critical failures in the Atlas Lattice repository and its infrastructure.

---

## Incident Classification

| Class | Description | Examples |
|-------|-------------|---------|
| **P0 — Critical** | Active breach or exfiltration risk | Leaked API key, exposed credentials, RCE in CI |
| **P1 — High** | Significant data exposure or integrity risk | PII committed to public repo, broken secret scanning |
| **P2 — Medium** | Contained risk requiring prompt attention | Stale token with broad scope, misconfigured CODEOWNERS |
| **P3 — Low** | Informational / housekeeping | Outdated dependency, minor misconfiguration |

---

## Response Team

| Role | Responsibility |
|------|---------------|
| **Incident Commander** | @atlaslattice (primary); Governance Lead (backup) |
| **Technical Lead** | Engineering Lead or DevOps Lead |
| **Comms Lead** | Council Chair or designated spokesperson |
| **Scribe** | Documents all actions with timestamps |

---

## P0 — Critical Incident Playbook

### T+0 — Detection

1. Any contributor detecting a P0 incident **immediately** contacts @atlaslattice via the fastest available channel.
2. Do not discuss publicly until the incident is contained.

### T+0 to T+1h — Contain

1. Revoke any exposed credentials immediately (GitHub PAT, API keys, tokens).
2. If code with active exploit is in main: assess emergency branch protection lock.
3. If secrets are in git history: **do not** push any new commits until history purge is planned.

### T+1h to T+4h — Remediate

1. Create a private branch for the fix.
2. Purge secrets from git history using `git filter-repo` if needed.
3. Force-push the cleaned history **after coordinating with all active contributors**.
4. Rotate all potentially exposed credentials.

### T+4h to T+24h — Verify & Document

1. Confirm no residual exposure via GitHub secret scanning sweep.
2. File a private GitHub Security Advisory.
3. Document timeline in this runbook's Incident Log section.
4. Notify affected parties per [Vulnerability Disclosure Process](./VULNERABILITY_DISCLOSURE_PROCESS.md).

### T+24h to T+72h — Disclose

1. Publish GitHub Security Advisory (coordinated with reporter if external).
2. Update [Compliance Evidence Index](./COMPLIANCE_EVIDENCE_INDEX.md).
3. Add entry to [Public Risk Register](./PUBLIC_RISK_REGISTER.md).

---

## P1 — High Incident Playbook

1. Acknowledge within 48 hours.
2. Assess scope: what data was exposed? Who may have seen it?
3. Apply [PII Redaction Rubric](./PII_REDACTION_RUBRIC.md) if personal data involved.
4. Remediate within 7 days.
5. File post-mortem in `archive/governance/INCIDENT_LOG_YYYY.md`.

---

## P2/P3 — Standard Remediation

- Remediate within SLA per [Vulnerability Disclosure Process](./VULNERABILITY_DISCLOSURE_PROCESS.md).
- No emergency escalation required.
- Log in quarterly council session.

---

## Incident Log Index

Incidents are logged in annual files:

- `archive/governance/INCIDENT_LOG_2026.md` *(to be created on first incident)*

Each entry includes: date, class, summary, actions taken, resolution, and lessons learned.

---

## Post-Mortem Template

```
## Incident: [Short Title]
- Date: YYYY-MM-DD
- Class: P0 / P1 / P2 / P3
- Summary: [1-2 sentences]
- Timeline:
  - T+0: [detection]
  - T+Xh: [containment]
  - T+Xh: [remediation]
  - T+Xh: [disclosure]
- Root Cause: [technical and process factors]
- Lessons Learned: [what changes prevent recurrence]
- Action Items: [with owners and due dates]
```

---

## Related Documents

- [Vulnerability Disclosure Process](./VULNERABILITY_DISCLOSURE_PROCESS.md)
- [PII Redaction Rubric](./PII_REDACTION_RUBRIC.md)
- [Compliance Evidence Index](./COMPLIANCE_EVIDENCE_INDEX.md)
- [Public Risk Register](./PUBLIC_RISK_REGISTER.md)
- [SECURITY.md](../../SECURITY.md)

---

*Maintained by Atlas Lattice Foundation · status: candidate until ratified*
