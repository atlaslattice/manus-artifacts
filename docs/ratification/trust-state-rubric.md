# Trust State Rubric

> **Status:** CANDIDATE  
> **Artifact Type:** rubric  
> **Date:** 2026-05-28  
> **Related:** [Ratification Flow](../RATIFICATION_AND_TRUST_FLOW.md), [Packet Requirements](./ratification-packet-requirements.md), [Canon Boundary Audit](./canon-boundary-audit-2026-05-28.md)

## Trust States

<!-- METADATA
stable_id: AL-RT-104
lifecycle_state: CANDIDATE
owner: @atlaslattice
date_created: 2026-05-28
canon_status: candidate
-->

| State | Meaning | Transition In Criteria | Who Approves | Required Evidence |
| --- | --- | --- | --- | --- |
| `DRAFT` | Working material not yet fit for wider review. | Initial authoring only. | Author / steward. | Basic provenance only. |
| `CANDIDATE` | Publicly visible but not canon. | Candidate notice, basic metadata, related links, and no false canon claims. | Author / steward. | Provenance and candidate-state declaration. |
| `UNDER_REVIEW` | Packet is assembled and formally submitted for adjudication. | Ratification packet complete, validation linked, checklist completed or blocked transparently. | Human reviewer / `@atlaslattice`. | Evidence links, validation receipts, checklist. |
| `RATIFIED` | Approved for canon surface use. | Explicit adjudication and trust-state assignment recorded. | `@atlaslattice`. | Full packet, review outcome, ratification event. |
| `DEPRECATED` | Retained for history but superseded by a better artifact. | Replacement artifact identified and deprecation notice applied. | Steward plus human review when trust-sensitive. | Replacement link, rationale, preserved provenance. |

## Transition Notes

- `DRAFT -> CANDIDATE` requires basic structural and provenance hygiene.
- `CANDIDATE -> UNDER_REVIEW` requires a packet, not just a good artifact.
- `UNDER_REVIEW -> RATIFIED` requires human-root adjudication.
- `CANDIDATE -> DEPRECATED` is valid when the artifact should remain addressable but not promoted.
