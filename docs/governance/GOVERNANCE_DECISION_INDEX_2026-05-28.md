---
artifact_id: GOV-GOVERNANCE-DECISION-INDEX-2026-05-28
title: Governance Decision Index
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
---
# Governance Decision Index

> **Purpose:** Single lookup table for all ratification, demotion, and adjudication events across the Atlas Lattice corpus. Entries are added at every stage transition.

## Index Format

| Event ID | Date | Type | Artifact ID | Outcome | Adjudicator | Notes |
|---|---|---|---|---|---|---|
| ADR-0001 | 2026-05-28 | Scope Decision | ADR-0001-PUBLIC-SCOPE-DECISION-2026-05-28 | DRAFT (pending owner ratification) | @atlaslattice | Public boundary decision |

## Event Type Reference

| Code | Meaning |
|---|---|
| `RAT` | Ratification — CANDIDATE → RATIFIED |
| `DEM` | Demotion — RATIFIED → lower status |
| `CON` | Conflict resolution adjudication |
| `EMG` | Emergency security/PII action |
| `ADR` | Architecture / Operational Decision Record |
| `EXP` | Candidate expiration / forced archive |

## Adding an Entry

When any governance event completes, add a row using the format above and reference the full evidence in the [Adjudication Evidence Template](./ADJUDICATION_EVIDENCE_TEMPLATE_v0_1.md).

## Related Artifacts

- [Ratification Lifecycle](./RATIFICATION_LIFECYCLE_v0_1.md)
- [Unresolved Decision Register](./UNRESOLVED_DECISION_REGISTER_2026-05-28.md)
- [ADR Archive](../decisions/README.md)
