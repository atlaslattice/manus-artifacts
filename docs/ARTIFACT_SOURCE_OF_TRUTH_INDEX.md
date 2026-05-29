---
artifact_id: DOC-ARTIFACT-SOURCE-OF-TRUTH-INDEX-2026-05-29
title: Artifact Source-of-Truth Index
status: CANDIDATE
owner: atlaslattice
created: 2026-05-29
last_updated: 2026-05-29
source_of_truth: GitHub
---
# Artifact Source-of-Truth Index

This page is the single source-of-truth index for canonical-state tracking on flagship artifacts.

## Canon-State Fields

- `source_of_truth`: authoritative substrate for current record state
- `canon_status`: `CANDIDATE` or `RATIFIED`
- `ratification_event_id`: governing event receipt ID (required when `canon_status = RATIFIED`)
- `trust_state`: trust adjudication state (`pending`, `adjudicated`, `revoked`)

## Flagship Artifact Canon Index

| Artifact | Path | source_of_truth | canon_status | ratification_event_id | trust_state |
|---|---|---|---|---|---|
| Repository entrypoint | `README.md` | GitHub | CANDIDATE | `TBD` | pending |
| Next-144 execution board | `projects/aetherforge-next144-taskboard-2026-05-28.md` | GitHub | CANDIDATE | `TBD` | pending |
| Next-12 issue seeding pack | `projects/aetherforge-next12-worldclass-github-issue-seeding-pack-2026-05-29.md` | GitHub | CANDIDATE | `TBD` | pending |
| Archive index | `docs/ARCHIVE_INDEX.md` | GitHub | CANDIDATE | `TBD` | pending |
| Governance spine | `docs/governance/README.md` | GitHub | CANDIDATE | `TBD` | pending |
| AI systems evidence index | `docs/AI_SYSTEMS_EVIDENCE_INDEX.md` | GitHub | CANDIDATE | `TBD` | pending |

## Operational Rule

No artifact is treated as canon until ratification and adjudication are completed and recorded in this index.
