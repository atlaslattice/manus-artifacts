# Canon UX + Identity Toolkit (Ring I)

Status: Candidate

Purpose: single-source toolkit for canon UX/identity standards, templates, and promotion hygiene.

## 1) Canon Badge Legend Standard

- 🟢 `CANON` — ratified + adjudicated + published to canon destination
- 🟡 `CANDIDATE` — under review, not canon
- 🔵 `DRAFT` — in-progress working artifact
- ⚫ `ARCHIVED` — retained historical artifact
- 🟠 `DEPRECATED` — superseded, maintained for reference

## 2) Canon State Emoji + Badge Mapping

| State | Emoji | Badge Text |
|---|---|---|
| Canon | 🟢 | CANON |
| Candidate | 🟡 | CANDIDATE |
| Draft | 🔵 | DRAFT |
| Archived | ⚫ | ARCHIVED |
| Deprecated | 🟠 | DEPRECATED |

## 3) “Why this is candidate” Rationale Block Template

```md
## Why this is candidate
- Review state: pending council review and human adjudication
- Evidence present: <yes/no + links>
- Blocking questions: <list>
- Promotion owner: <name/seat>
```

## 4) Canon Promotion Evidence Pack Template

```md
## Canon Promotion Evidence Pack
- Source artifact:
- Version:
- Decision ID:
- Review thread links:
- Adjudication receipt:
- Publication receipt:
- Supersession impact:
```

## 5) Canon Decision ID Naming Convention

Format: `CANON-YYYYMMDD-<DOMAIN>-<NNN>`  
Example: `CANON-20260526-GOV-001`

## 6) Canon Checksum / Hash Snapshot Protocol

- Generate SHA256 for promoted artifact at decision time.
- Record hash in promotion evidence pack.
- Record commit SHA and path.
- Recompute hash if artifact changes post-decision.

## 7) Canon Change Announcement Template

```md
## Canon Change Announcement
- Decision ID:
- Artifact:
- Previous state:
- New state:
- Effective date:
- Summary of change:
- Reviewer/adjudicator:
- Links to evidence:
```

## 8) Canon Visual Timeline Page Template

```md
## Canon Timeline
| Date | Decision ID | Artifact | State Change | Notes |
|---|---|---|---|---|
```

## 9) Canon Supersession Notice Template

```md
## Supersession Notice
This artifact has been superseded by:
- New artifact:
- Effective date:
- Decision ID:
- Migration notes:
```

## 10) Canon Readability Quick-Reference

- Keep headings shallow and explicit.
- Put status near top of file.
- Keep one sentence per bullet when possible.
- Use relative links for in-repo references.
- Separate template blocks from policy prose.
