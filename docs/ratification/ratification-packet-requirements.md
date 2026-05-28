# Ratification Packet Requirements

> **Status:** CANDIDATE  
> **Artifact Type:** requirements doc  
> **Date:** 2026-05-28  
> **Related:** [Trust State Rubric](./trust-state-rubric.md), [Adjudication Template](./adjudication-request-template.md), [Ratification Flow](../RATIFICATION_AND_TRUST_FLOW.md)

## Required Artifacts in the Packet

<!-- METADATA
stable_id: AL-RT-102
lifecycle_state: CANDIDATE
owner: @atlaslattice
date_created: 2026-05-28
canon_status: candidate
-->

A ratification packet must contain:

1. the candidate artifact under review
2. linked evidence entries or evidence gap note
3. linked validation receipt(s)
4. the relevant pre-ratification checklist
5. blocking issues and proposed next step
6. the adjudication request addressed to `@atlaslattice`

## Required Metadata Fields

Every packet should explicitly state:

- artifact title
- stable ID
- lifecycle state
- trust-state recommendation
- owner / steward
- review date
- validation status
- evidence status

## Review Checklist Completion Requirements

The packet is incomplete until the relevant checklist is filled and every unchecked item is either resolved or called out as a blocker.

## Approval Chain

```text
CANDIDATE → UNDER_REVIEW → RATIFIED
```

- `CANDIDATE`: artifact is ready to assemble but not yet formally submitted
- `UNDER_REVIEW`: packet has been handed to human-root review
- `RATIFIED`: explicit approval and trust-state confirmation have been recorded

## Submission Format

Use a single markdown packet or review bundle that links:

- the artifact
- evidence
- validation receipts
- checklist
- adjudication request

The packet should be easy to scan in a pull request, issue, or review thread without requiring hidden context.
