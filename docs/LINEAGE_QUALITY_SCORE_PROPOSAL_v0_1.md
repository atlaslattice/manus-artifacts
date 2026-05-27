---
artifact_id: DOC-LINEAGE-QUALITY-SCORE-PROPOSAL-V0-1-2026-05-27
title: Lineage Quality Score Proposal v0.1
status: CANDIDATE
owner: atlaslattice
created: 2026-05-27
last_updated: 2026-05-27
source_of_truth: GitHub
---

# Lineage Quality Score Proposal v0.1

## Purpose

Define a lightweight scoring model for artifact lineage quality so high-value public artifacts can be prioritized for remediation and canon review.

## Proposed score bands

| Score | Meaning | Minimum signal |
|---|---|---|
| 4 | Strong lineage | Required metadata + explicit upstream citations + validation signal |
| 3 | Usable lineage | Required metadata + at least one provenance reference |
| 2 | Partial lineage | Some required metadata present, but provenance or status is incomplete |
| 1 | Weak lineage | Title/path exists but provenance fields are missing |
| 0 | Unusable lineage | Artifact missing enough metadata to trust routing or ownership |

## Recommended inputs

- Metadata completeness (`artifact_id`, owner, dates, status, source of truth)
- Relationship typing
- Validation or evidence linkage
- Canon/candidate clarity

## Operational use

- Prioritize score `0-1` artifacts in the next-100 metadata queue.
- Require score `3+` before promotion to canon review.
- Include score deltas in monthly provenance drift reporting when richer lineage fields are added.
