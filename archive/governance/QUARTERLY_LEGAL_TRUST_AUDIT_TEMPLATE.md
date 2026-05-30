# Quarterly Legal/Trust Audit Template

*Atlas Lattice Foundation · Aetherforge Mission #24 · 2026-05-28*

status: candidate

> Template for conducting quarterly legal and trust audits of the Atlas Lattice repository. Complete this template at the end of each quarter and file as `QUARTERLY_AUDIT_YYYY-Qn.md`.

---

## Audit Metadata

```yaml
audit_period: YYYY-Qn   # e.g., 2026-Q3
audit_date: YYYY-MM-DD
conducted_by: "@atlaslattice (and/or designated auditor)"
status: draft / complete
```

---

## Section 1 — License Compliance

- [ ] Root LICENSE file is present and correct
- [ ] Third-party attribution inventory is current (all new deps added this quarter?)
- [ ] No third-party content with incompatible licenses was introduced
- [ ] SPDX header progress: ___% of target files have headers

**Notes:**

---

## Section 2 — Privacy & PII

- [ ] No unredacted Tier A PII was discovered or remains in the repository
- [ ] Any PII removal requests were processed within 30 days
- [ ] AI-generated artifacts were reviewed for personal data before commit
- [ ] Data retention schedule was followed (stale artifacts quarantined if applicable)

**Notes:**

---

## Section 3 — Security

- [ ] GitHub secret scanning found no active exposed credentials
- [ ] All P0/P1 incidents from the quarter have been resolved and logged
- [ ] Vulnerability disclosure SLAs were met for all reported issues
- [ ] GitHub Action versions were reviewed for known CVEs
- [ ] CODEOWNERS file is accurate and complete

**Security incident summary this quarter:** *(none / list incidents)*

**Notes:**

---

## Section 4 — Governance

- [ ] Review SLA compliance: ___% of PRs closed within their SLA tier
- [ ] Council review cadence was followed (weekly triage / monthly wave review)
- [ ] Change classification was applied to all PRs
- [ ] No unauthorized canon promotions occurred (all canon changes had @atlaslattice approval)
- [ ] Deprecation policy was followed for all deprecated artifacts

**SLA breach log:** *(none / list breaches with reason)*

**Notes:**

---

## Section 5 — Export Control

- [ ] No EAR/ITAR-controlled technical data was identified in new contributions
- [ ] Export control checklist was followed for any uncertain submissions

**Notes:**

---

## Section 6 — Risk Register Update

- [ ] All active risks were reviewed
- [ ] New risks identified this quarter were added to the register
- [ ] At least one risk was mitigated or closed (if applicable)

**New risks added:** *(none / list IDs)*

**Notes:**

---

## Section 7 — Open Items Carried Forward

| Item | Owner | Due Date |
|------|-------|----------|
| | | |

---

## Audit Sign-Off

| Role | Name | Date |
|------|------|------|
| Auditor | | |
| Ratification Authority | @atlaslattice | |

---

## Filing Instructions

1. Complete all sections.
2. Save as `archive/governance/QUARTERLY_AUDIT_YYYY-Qn.md`.
3. Link from the [Compliance Evidence Index](./COMPLIANCE_EVIDENCE_INDEX.md).
4. Reference in the [Council Review Cadence](./COUNCIL_REVIEW_CADENCE.md) quarterly session notes.

---

## Related Documents

- [Compliance Evidence Index](./COMPLIANCE_EVIDENCE_INDEX.md)
- [Public Risk Register](./PUBLIC_RISK_REGISTER.md)
- [Review SLA Policy](./REVIEW_SLA_POLICY.md)
- [Council Review Cadence](./COUNCIL_REVIEW_CADENCE.md)

---

*Maintained by Atlas Lattice Foundation · status: candidate until ratified*
