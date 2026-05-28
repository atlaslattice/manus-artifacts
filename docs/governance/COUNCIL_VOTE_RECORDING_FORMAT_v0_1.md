---
artifact_id: GOV-COUNCIL-VOTE-RECORDING-FORMAT-v0-1-2026-05-28
title: Council Vote Recording Format
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
version: v0.1
---
# Council Vote Recording Format

> **Purpose:** Standardize how council votes are recorded so they are auditable, discoverable, and linked to adjudication evidence.

## Vote Record Format

Each vote is recorded as a YAML block inside a markdown section or in a dedicated vote file.

```yaml
vote_id: VOTE-YYYY-MM-DD-NNN
date: YYYY-MM-DD
artifact_id: ARTIFACT-ID-BEING-VOTED-ON
motion: "Ratify / Demote / Reject / Defer <artifact_id>"
voters:
  - name: "@member1"
    vote: APPROVE          # APPROVE | REJECT | ABSTAIN
    notes: "optional note"
  - name: "@member2"
    vote: APPROVE
    notes: ""
result: PASS               # PASS | FAIL | DEFERRED | NO_QUORUM
quorum_met: true
notes: "Any broader context for the vote record"
adjudication_event_id: ADJ-YYYY-MM-DD-NNN   # populated after @atlaslattice adjudicates
```

## Vote Outcome Rules

| Condition | Result |
|---|---|
| Majority APPROVE, @atlaslattice adjudicates APPROVE | PASS |
| Any REJECT without satisfactory resolution | FAIL or DEFERRED |
| Insufficient voters to meet quorum | NO_QUORUM (reschedule) |
| Motion needs more evidence before deciding | DEFERRED |

## Quorum Policy

- Minimum quorum: **2 council members** (including @atlaslattice or their designated proxy).
- Quorum is required for all ratifications.
- Demotions and emergency actions may proceed without quorum when @atlaslattice acts unilaterally, but must be logged.

## Where to Record Votes

1. Inline in the relevant [Adjudication Evidence](./ADJUDICATION_EVIDENCE_TEMPLATE_v0_1.md) file for the artifact.
2. Referenced from the [Governance Decision Index](./GOVERNANCE_DECISION_INDEX_2026-05-28.md).

## Immutability

Vote records are **append-only**. Corrections are recorded as amended entries, not overwrites. The original vote record is preserved.
