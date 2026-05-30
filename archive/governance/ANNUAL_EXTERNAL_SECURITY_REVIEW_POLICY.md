---
artifact_id: SEC-POLICY-EXTERNAL-SECURITY-REVIEW-001
title: Annual External Security Review Policy
status: candidate
created: 2026-05-28
owner: council
tags: [security, audit, governance, compliance]
---

# Annual External Security Review Policy

> Defines the process for conducting an annual external security review of the Atlas Lattice repository.

status: candidate

---

## Purpose

An annual external security review provides an independent, objective assessment of the repository's security posture. It complements the internal Security Champion role and automated gates by bringing outside expertise.

---

## Scope

The annual external review covers:

| Area | What is reviewed |
|------|----------------|
| GitHub repository configuration | Branch protection, CODEOWNERS, secret scanning settings |
| CI/CD pipeline security | Action pinning, workflow permissions, secret handling |
| Dependency supply chain | SBOM completeness, high-severity CVE backlog |
| Governance artifacts | Canon status model integrity, ratification process |
| Access controls | Contributor roles, token audit, PAT inventory |
| Incident response readiness | Runbook quality, past incident post-mortems |
| KG data integrity | Provenance claims, AI evidence audit trail |

---

## Review Format

| Format | Description |
|--------|------------|
| **Lightweight (default)** | Async review by a trusted community security contributor; 1-2 week timeline |
| **Full external audit** | Formal engagement with a security firm; when repository reaches >100 contributors or handles sensitive data at scale |

The default lightweight review is sufficient for the current repository scale.

---

## Review Cadence

| Review | Date | Reviewer | Status |
|--------|------|---------|--------|
| First review | 2027-05-28 | TBD | Scheduled |

---

## Process

1. **Prepare review package:** Compile current security policies, CI workflow files, SBOM, and last 90 days of security alerts into a review package
2. **Engage reviewer:** Identify a qualified reviewer (security community member, Open Source Security Foundation contact, or security contractor)
3. **Provide access:** Grant read-only access to the repository; no write access required for external review
4. **Receive findings:** Reviewer provides a written findings report
5. **Triage findings:** Security Champion triages per [VULNERABILITY_TRIAGE_SLAS.md](./VULNERABILITY_TRIAGE_SLAS.md)
6. **Publish summary:** A public summary of the review and remediation actions is published in `archive/governance/` (sensitive findings may be redacted)
7. **Update risk register:** Update [PUBLIC_RISK_REGISTER.md](./PUBLIC_RISK_REGISTER.md) with any accepted residual risks

---

## Review Report Template

```markdown
# External Security Review Report — [Year]

**Review date:** YYYY-MM-DD
**Reviewer:** [Name/Organization]
**Scope:** [As defined in policy]

## Summary

[One paragraph summary of overall findings]

## Findings

### Critical
- (none / list findings)

### High
- (none / list findings)

### Medium/Low
- (none / list findings)

## Remediation Status

| Finding | Severity | Status | Target date |
|---------|---------|--------|-------------|

## Conclusion

[Reviewer conclusion and recommended next steps]
```

---

*Atlas Lattice Foundation · status: candidate*
