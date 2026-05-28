# Public Risk Register

*Atlas Lattice Foundation · Aetherforge Mission #23 · 2026-05-28*

status: candidate

> Tracks identified risks to the Atlas Lattice repository and mission, with likelihood/impact ratings and mitigation status. Updated quarterly.

---

## Risk Rating Scale

| Rating | Likelihood | Impact |
|--------|-----------|--------|
| 1 | Rare (< 1% / year) | Negligible |
| 2 | Unlikely (1–10% / year) | Minor |
| 3 | Possible (10–30% / year) | Moderate |
| 4 | Likely (30–70% / year) | Major |
| 5 | Almost Certain (> 70% / year) | Severe |

**Risk Score = Likelihood × Impact**

---

## Active Risk Register (2026-Q2)

### Security Risks

| ID | Risk | L | I | Score | Mitigation | Status |
|----|------|---|---|-------|-----------|--------|
| SEC-001 | Accidental secret commit to public repo | 3 | 4 | 12 | GitHub secret scanning enabled; PII rubric defined | Mitigated |
| SEC-002 | Stale/overprivileged GitHub Action tokens | 3 | 3 | 9 | Token audit planned (Mission #79/#80) | Open |
| SEC-003 | Supply chain attack via third-party Actions | 2 | 4 | 8 | Action pinning planned (Mission #69) | Open |
| SEC-004 | Unauthorized push to main branch | 2 | 5 | 10 | Branch protection in place; CODEOWNERS gap (Mission #78) | Partial |

### Privacy Risks

| ID | Risk | L | I | Score | Mitigation | Status |
|----|------|---|---|-------|-----------|--------|
| PRV-001 | PII in imported archive documents | 4 | 3 | 12 | PII Redaction Rubric defined (Mission #16) | Mitigated |
| PRV-002 | AI output containing personal data | 3 | 3 | 9 | Sensitive content review process defined | Mitigated |

### Governance Risks

| ID | Risk | L | I | Score | Mitigation | Status |
|----|------|---|---|-------|-----------|--------|
| GOV-001 | Canon drift (unratified content treated as authoritative) | 4 | 3 | 12 | Canon status model + ratification workflow in place | Mitigated |
| GOV-002 | Single-point-of-failure (@atlaslattice as sole ratifier) | 3 | 4 | 12 | Council expansion planned; delegation policy forthcoming | Open |
| GOV-003 | Contributor confusion about contribution process | 3 | 2 | 6 | Governance onboarding guide created (Mission #12) | Mitigated |

### Operational Risks

| ID | Risk | L | I | Score | Mitigation | Status |
|----|------|---|---|-------|-----------|--------|
| OPS-001 | Knowledge graph orphan nodes accumulate | 4 | 2 | 8 | Orphan detection planned (Mission #56); KG validation live | Partial |
| OPS-002 | CI workflows become stale / non-functional | 3 | 3 | 9 | CI hardening (Mission #61/#69) planned | Open |
| OPS-003 | Repository grows too large for efficient navigation | 3 | 2 | 6 | Taxonomy map + navigation normalization (Missions #25, #29) | Open |

### Mission / Strategy Risks

| ID | Risk | L | I | Score | Mitigation | Status |
|----|------|---|---|-------|-----------|--------|
| STR-001 | 144-task campaign stalls due to context loss | 3 | 3 | 9 | Taskboard + TIDELOCKBrain memory palace in place | Mitigated |
| STR-002 | Open-source release delayed due to compliance gaps | 2 | 4 | 8 | Wave 2 (Legal/Trust) tasks being executed now | In progress |

---

## Closed / Resolved Risks

| ID | Risk | Resolution | Closed |
|----|------|-----------|--------|
| GOV-000 | No canonical status model | Canon model + ratification workflow published | 2026-05-28 |

---

## Quarterly Review

This register is reviewed at each [quarterly council session](./COUNCIL_REVIEW_CADENCE.md). New risks may be submitted via GitHub Discussions.

---

## Related Documents

- [Compliance Evidence Index](./COMPLIANCE_EVIDENCE_INDEX.md)
- [Incident Response Runbook](./INCIDENT_RESPONSE_RUNBOOK.md)
- [Vulnerability Disclosure Process](./VULNERABILITY_DISCLOSURE_PROCESS.md)
- [Quarterly Legal/Trust Audit Template](./QUARTERLY_LEGAL_TRUST_AUDIT_TEMPLATE.md)

---

*Maintained by Atlas Lattice Foundation · status: candidate until ratified*
