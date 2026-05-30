---
artifact_id: SEC-POLICY-CODEOWNERS-001
title: CODEOWNERS Coverage Policy
status: candidate
created: 2026-05-28
owner: council
tags: [security, governance, codeowners, review]
---

# CODEOWNERS Coverage Policy

> Defines how CODEOWNERS is structured and enforced to ensure every significant file path has a designated owner.

status: candidate

---

## Purpose

A `CODEOWNERS` file ensures that changes to sensitive or critical files require review from designated owners. Without it, anyone can approve changes to any file — including governance documents, schemas, and security policies.

---

## CODEOWNERS File

Location: `.github/CODEOWNERS`

### Current Coverage Map

```
# Default owner — catches everything not matched below
* @atlaslattice

# Governance policies
/archive/governance/ @atlaslattice

# Legal and compliance
/archive/governance/LICENSE_AUDIT_REPORT.md @atlaslattice
/archive/governance/PII_REDACTION_RUBRIC.md @atlaslattice
/archive/governance/DATA_RETENTION_POLICY.md @atlaslattice
/archive/governance/COMPLIANCE_EVIDENCE_INDEX.md @atlaslattice

# Schemas (technical review required)
/schemas/ @atlaslattice

# Reference implementations
/reference_impl/ @atlaslattice

# CI/CD workflows
/.github/workflows/ @atlaslattice

# Security policies
/archive/governance/VULNERABILITY_DISCLOSURE_PROCESS.md @atlaslattice
/archive/governance/INCIDENT_RESPONSE_RUNBOOK.md @atlaslattice
/archive/governance/SECRET_SCANNING_PATTERNS_POLICY.md @atlaslattice

# Project boards
/projects/ @atlaslattice

# README
/README.md @atlaslattice
```

---

## Coverage Requirements

| File category | Owner required | Min reviewers |
|--------------|--------------|--------------|
| Governance policies (`archive/governance/`) | @atlaslattice | 1 |
| Schemas (`schemas/`) | @atlaslattice | 1 |
| Reference implementations (`reference_impl/`) | @atlaslattice | 1 |
| CI/CD workflows (`.github/workflows/`) | @atlaslattice | 1 |
| User-facing docs (`docs/`) | Any council member | 1 |
| Work logs and dream journals | No requirement | 0 (optional review) |

---

## Adding New Owners

As the council grows, additional CODEOWNERS may be added:

1. Propose the change in a PR with an explanation of scope
2. @atlaslattice must approve all CODEOWNERS changes
3. New owners must have signed the Contributor Agreement (once established)

---

## Coverage Audit

CODEOWNERS coverage is audited quarterly to ensure no new file categories have been added without an owner. The audit verifies that every file in `archive/governance/`, `schemas/`, and `.github/` is matched by a CODEOWNERS rule.

---

*Atlas Lattice Foundation · status: candidate*
