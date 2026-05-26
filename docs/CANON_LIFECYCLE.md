# Canon Lifecycle
Status: Candidate
Date: 2026-05-26

This document defines the archive-wide lifecycle for artifacts in the Manus repository.
It is governance-first by design: state labels are not cosmetic, and no artifact becomes canon by accident.
Within the Aetherforge Metatron's Cube program, lifecycle discipline is the mechanism that keeps all five rings aligned.

## Purpose

The lifecycle exists to answer five questions consistently:

1. What is the current authority level of an artifact?
2. What evidence is required to change that authority level?
3. Who has approval rights at each transition point?
4. How should older artifacts remain visible after supersession?
5. How do public readers distinguish living doctrine from historical record?

## State machine

`Draft -> Candidate -> Canon -> Archived -> Deprecated`

The normal forward path is Draft to Candidate to Canon.
Archived and Deprecated are downstream preservation states rather than publishing states.
Direct jumps are allowed only when explicitly listed in the transition table below.

## State definitions

### 1. Draft

A Draft is a working artifact under active development.
It may be incomplete, exploratory, or unstable.
Drafts can exist in GitHub for transparency, but they should not be cited as authoritative doctrine.

Typical characteristics:

- Unfinalized structure or unresolved assumptions
- Limited review coverage
- No promotion package or decision record yet attached
- Suitable for internal coordination and scoped external review

### 2. Candidate

A Candidate is reviewable and intentionally published for scrutiny.
This is the default public status for the repository on 2026-05-26.
Candidate means the artifact is coherent enough to examine, link, discuss, and compare, but not yet canon.

Typical characteristics:

- Clear title, scope, status, and date
- Named steward and domain ownership
- Metadata complete enough for indexing and lineage tracking
- Reviewable by council and public readers

### 3. Canon

Canon is the highest active authority state.
A Canon artifact is the current governing reference for its subject area until superseded, archived, or deprecated.
Canon does not mean permanent perfection; it means currently ratified authority.

Typical characteristics:

- Full council ratification recorded
- Adjudication by @atlaslattice recorded
- Promotion checklist completed
- Decision log entry published and linkable
- Stable citation target for downstream doctrine and website publication

### 4. Archived

Archived artifacts are retained for continuity, provenance, and historical comparison.
An Archived artifact may once have been canon, or it may be a candidate preserved for context.
Archived material remains accessible and cited as history, not current authority.

Typical characteristics:

- Preserved without routine content mutation
- Linked to successor artifacts where relevant
- Retained for audit and lineage inspection
- Clearly labeled as non-current

### 5. Deprecated

Deprecated artifacts remain visible but are actively discouraged for operational use.
Deprecation is used when an artifact is misleading, unsafe, superseded in a materially incompatible way, or no longer acceptable as a reference.
Deprecation is stronger than archival because it carries a warning signal.

Typical characteristics:

- Explicit rationale for why use should stop
- Link to replacement or remediation path
- Visible warning in front matter or header note
- Retained only for traceability and audit completeness

## Transition criteria and approvals

| Transition | Minimum criteria | Primary approver | Required record |
| --- | --- | --- | --- |
| Draft -> Candidate | Scope defined, structure stabilized, status/date present, steward assigned, ready for review | Domain steward | Pull request or steward note |
| Candidate -> Canon | Promotion checklist complete, evidence attached, metadata complete, no unresolved blocking objections, council vote complete | Full council ratification + adjudication by @atlaslattice | Canon decision log entry |
| Canon -> Archived | A newer canon supersedes it, or the subject becomes historical rather than active | Domain steward with council notice | Lineage update + archival note |
| Candidate -> Archived | Candidate preserved for history but not promoted | Domain steward | Archival rationale note |
| Canon -> Deprecated | Active harm, invalidity, broken provenance, or formal replacement requiring warning label | Full council + adjudication by @atlaslattice | Deprecation decision record |
| Candidate -> Deprecated | Material defect or trust breach discovered during review | Domain steward with council escalation for high-impact cases | Deprecation note |
| Archived -> Deprecated | Historical artifact now needs warning context | Domain steward or council, depending on impact | Decision note |
| Deprecated -> Archived | Warning no longer needed, but preservation still required | Council review recommended | Updated archival note |

## Approval roles

### Domain steward

Domain stewards may advance artifacts from Draft to Candidate and may recommend archival actions.
They are responsible for making sure documentation quality, metadata completeness, and linkage standards are met.

### Full council

The full council is the ratification body for canon changes and major deprecations.
Council review establishes collective legitimacy and should be reflected in the decision record.

### @atlaslattice adjudication

Adjudication by @atlaslattice is the final canon authority gate for this repository.
No artifact should be presented as canon without that explicit adjudication.

## Examples

- A new Aetherforge operating doctrine begins as Draft while terminology and scope are still moving.
- Once review-ready, it becomes Candidate so collaborators can inspect structure and evidence.
- If ratified and adjudicated, it becomes Canon and may be published to the public website canon destination.
- When a later doctrine supersedes it, the earlier canon version becomes Archived with lineage links.
- If an old systems note contains outdated guidance that could mislead builders, it becomes Deprecated rather than merely Archived.

## Operating rules

- When in doubt, use Candidate rather than Canon.
- Never infer canon from file age, popularity, or reuse alone.
- Archived and Deprecated artifacts must remain traceable unless retention policy explicitly says otherwise.
- Lifecycle state should appear in the artifact header and metadata when metadata is present.
- Every state change that affects authority should be linkable from the decision log.

## Related documents

- [CANON_BOUNDARY.md](./CANON_BOUNDARY.md)
- [CANON_PROMOTION_CHECKLIST.md](./CANON_PROMOTION_CHECKLIST.md)
- [CANON_DECISION_LOG_FORMAT.md](./CANON_DECISION_LOG_FORMAT.md)
- [../governance/CANON_CONFLICT_RESOLUTION.md](../governance/CANON_CONFLICT_RESOLUTION.md)
- [../governance/CANON_AUDIT_PROTOCOL.md](../governance/CANON_AUDIT_PROTOCOL.md)
