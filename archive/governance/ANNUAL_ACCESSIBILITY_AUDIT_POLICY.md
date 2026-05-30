---
artifact_id: A11Y-POLICY-ANNUAL-AUDIT-001
title: Annual Accessibility Audit Policy
status: candidate
created: 2026-05-28
owner: council
tags: [accessibility, audit, annual, a11y, quality]
---

# Annual Accessibility Audit Policy

> Defines the scope, process, and schedule for the Atlas Lattice annual accessibility audit.

status: candidate

---

## Purpose

The annual accessibility audit is a systematic review that ensures Atlas Lattice documentation meets its own accessibility standards. It is the primary mechanism for measuring and improving accessibility over time.

---

## Scope

The audit covers a **random sample of 10%** of all documents in:
- `archive/governance/`
- `docs/`
- `archive/spec/`
- `README.md` and other root-level documents (always included)

New documents (created within 12 months of the audit) are sampled at 20%.

---

## Audit Dimensions

Each document is evaluated against the [Docs Accessibility Rubric](./DOCS_ACCESSIBILITY_RUBRIC.md):

1. Readability (plain language, sentence length, defined terms)
2. Visual accessibility (heading hierarchy, alt text, color independence)
3. Navigation and structure (title, anchors, cross-references)
4. Format accessibility (code blocks, lists, bold/italic)

---

## Audit Process

| Step | Action | Owner |
|------|--------|-------|
| 1. Sample | Random-select 10% of documents | Automated script (planned) or manual |
| 2. Score | Apply rubric to each sampled document | Security champion / accessibility reviewer |
| 3. Aggregate | Compute average score per dimension and overall | Reviewer |
| 4. Triage | Flag documents scoring < 10/12 for remediation | Reviewer |
| 5. Remediate | Open GitHub issues for flagged documents | Reviewer |
| 6. Report | Publish audit results in quality report | Reviewer |
| 7. Update policies | Update rubric, guides, or policies based on findings | Council |

---

## Audit Output

The audit produces:
1. A score sheet: every sampled document with its rubric scores
2. A list of remediation issues (GitHub issues, labeled `accessibility`)
3. A summary section in the monthly quality report
4. Trend data: average scores over successive audits

---

## Audit Schedule

| Audit | Scheduled date | Owner |
|-------|--------------|-------|
| First audit | 2027-05-28 (one year after Wave 9) | @atlaslattice + security champion |
| Second audit | 2028-05-28 | TBD |

---

## Audit Records

Audit records are stored at `archive/governance/ACCESSIBILITY_AUDIT_YYYY.md`.

---

*Atlas Lattice Foundation · status: candidate*
