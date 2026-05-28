# Evidence and Trust Explainer

> **Status:** CANDIDATE  
> **Artifact Type:** public explainer  
> **Date:** 2026-05-28  
> **Related:** [Evidence Standards](../evidence-standards.md), [Ratification Flow](../RATIFICATION_AND_TRUST_FLOW.md), [Trust State Rubric](../ratification/trust-state-rubric.md)

## What Does “Canon” Mean Here?

<!-- METADATA
stable_id: AL-SYS-323
lifecycle_state: CANDIDATE
owner: @atlaslattice
date_created: 2026-05-28
canon_status: candidate
-->

In this repo, “canon” means an artifact has crossed a formal review boundary. Most public-facing material is still **candidate** state, which keeps it visible without pretending it has already been ratified.

## How Trust States Work

The pipeline is:

```text
DRAFT → CANDIDATE → UNDER_REVIEW → RATIFIED → DEPRECATED
```

Each step requires more evidence and more explicit approval.

## What Is Evidence for an AI-Built Artifact?

Evidence is the audit trail that says what was built, by which system or agent, using which sources, and what validation ran. In practice that can mean a structured evidence entry, a validation receipt, or both.

## Why This Matters for Open-Source AI Governance

Open-source AI work can move fast and still become confusing. Evidence and trust states slow down only the part that should be slow: the move from “interesting candidate” to “trusted artifact.”

## How to Read Trust State Badges

- **DRAFT:** early working material
- **CANDIDATE:** public and usable, but not canon
- **UNDER_REVIEW:** packet assembled and in adjudication
- **RATIFIED:** approved by the formal trust path
- **DEPRECATED:** retained for history, but superseded
