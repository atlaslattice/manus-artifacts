# Canon Audit Protocol
Status: Candidate
Date: 2026-05-26

This protocol defines the annual full-archive canon audit.
Its purpose is to ensure that canon labels, candidate claims, lineage chains, and trust-critical governance records remain accurate over time.

## Audit scope

The annual audit reviews:

- all canon-labeled artifacts
- artifacts proposed for canon since the prior audit
- decision log entries affecting canon authority
- supersession and archival chains linked to canon material
- public website canon destinations sourced from the repository

## Audit checklist

- confirm each canon artifact still has valid ratification and adjudication support
- confirm lifecycle label accuracy
- confirm linked predecessors and successors exist
- confirm decision log entries remain reachable and legible
- confirm no candidate artifact is being informally treated as canon without authority
- confirm deprecated canon artifacts carry adequate warning language

## Audit roles

| Role | Responsibility |
| --- | --- |
| Audit lead | Coordinates scope, timing, and findings package |
| Domain steward | Reviews canon within their area |
| Governance steward | Verifies decision rights and record completeness |
| @atlaslattice | Final adjudicator for disputed audit findings |

## Outputs

The annual audit should publish:

- an executive summary
- a findings table
- a remediation list with owners
- updated scorecards or maturity notes where appropriate
- a publication-ready report dated for the audit cycle

## Publication format

Publish the audit as a dated markdown report using a path such as:

`governance/canon-audit-report-YYYY-MM-DD.md`

Include:

- scope statement
- methods used
- findings by domain
- exceptions and unresolved issues
- sign-off or adjudication note

## Remediation timing

Critical canon-integrity issues should be addressed immediately.
Non-critical documentation cleanup should be scheduled into the next mission control cycle.

## Audit principle

The audit is not a ceremonial exercise.
It is the mechanism that proves the archive can sustain public trust beyond a single improvement sprint.
