# Enumeration Registry
## Public KG Floodgate — All 6 Enum Families

```text
STATUS: CANDIDATE — NOT CANON — authority_scope:none
DATE: 2026-06-04
AGENT: TIDELOCK (Copilot) — Beta-144 Campaign, Module 1, Task M1-05
PRCQ: PRCQ-003, PRCQ-006, PRCQ-007, PRCQ-017, PRCQ-018
KEEPER: "Enums are not evidence. Checklists are not exports."
```

> This document is the single source of truth for all closed-world enum families
> in the Public KG Floodgate. Values here are schema definitions only.
> They carry no authority, canon status, or deployment status.

---

## Enum Family 1 — source_id Format (PRCQ-003)

Stable format for identifying named sources by surface and pointer.

| Format Pattern | Example | Surface |
|----------------|---------|---------|
| `github:{owner}/{repo}@{sha}` | `github:atlaslattice/manus-artifacts@abc1234` | GitHub repo at commit |
| `github:{owner}/{repo}@HEAD` | `github:atlaslattice/manus-artifacts@HEAD` | GitHub repo at current HEAD |
| `gdoc:{doc_id}@frozen:{date}` | `gdoc:1aBcD...@frozen:2026-06-04` | Frozen Google Doc |
| `gsheet:{sheet_id}@frozen:{date}` | `gsheet:2xYzW...@frozen:2026-06-04` | Frozen Google Sheet |
| `gdrive:{file_id}@{version}` | `gdrive:3qRsT...@v1` | Google Drive file |
| `local:{relative_path}@{sha}` | `local:docs/foo.md@abc1234` | Local file in repo |

**Rule:** source_id MUST be stable and pointer-specific. `@HEAD` is only permitted
for references that are explicitly re-resolved at query time.

---

## Enum Family 2 — surface (PRCQ-006)

Closed-world enum for the surface/system a source originates from.

| Value | Description |
|-------|-------------|
| `github` | GitHub repository file or tree |
| `google_docs` | Google Docs document |
| `google_sheets` | Google Sheets spreadsheet |
| `google_drive` | Google Drive file (non-Docs/Sheets) |
| `notion` | Notion page or database |
| `local` | Local file not yet pushed to remote |
| `website` | Published website page |
| `unknown` | Surface not yet identified |

**Rule:** `unknown` is permitted during indexing but must be resolved before
any artifact can be promoted beyond `raw_export_status: not_exported`.

---

## Enum Family 3 — raw_export_status (PRCQ-007)

Describes the export state of a source document.

| Value | Description |
|-------|-------------|
| `not_exported` | Source has never been exported; raw content not attached |
| `export_in_progress` | Export started but not yet complete |
| `partial_export_attached` | Partial raw export attached; incomplete |
| `full_raw_export_attached` | Full raw export is attached and verified |
| `policy_only` | No raw content; only policy/schema/enum definition (safe for GREEN) |
| `frozen_snapshot` | Source was frozen before export; snapshot is the export |

**Rule (PRCQ-008):** Live Google Docs remain `not_exported` until explicitly frozen.
**Rule (PRCQ-009):** Uploaded markdown files must reach `full_raw_export_attached`
before any downstream processing.

---

## Enum Family 4 — canon_status (PRCQ-017)

Describes the canonization state of an artifact.

| Value | Description |
|-------|-------------|
| `not_canon` | Artifact is a candidate; not ratified |
| `canon_candidate` | Nominated for ratification; awaiting council review |
| `council_review` | Under active review by Pantheon Council |
| `ratified` | Ratified by full council; pending human adjudication |
| `canon` | Ratified + adjudicated by @atlaslattice; fully canon |
| `deprecated_canon` | Was canon; since superseded or retired |

**Rule:** All artifacts in the Public KG Floodgate are `not_canon`.
No artifact may advance to `canon` without Pantheon Council ratification
and explicit @atlaslattice adjudication.

---

## Enum Family 5 — deployment_status (PRCQ-018)

Describes where/whether an artifact has been deployed.

| Value | Description |
|-------|-------------|
| `not_deployed` | Artifact exists only in repo/workspace; not published anywhere |
| `staging` | Deployed to a staging/preview environment |
| `deployed_website` | Deployed to the canon website surface |
| `deployed_github_pages` | Deployed to GitHub Pages |
| `deployed_external` | Deployed to a third-party platform |
| `deployment_retired` | Was deployed; deployment retired or revoked |

**Rule:** All artifacts in the Public KG Floodgate are `not_deployed`.

---

## Enum Family 6 — authority_scope (implicit across all packets)

Describes the authority claim level of an artifact.

| Value | Description |
|-------|-------------|
| `none` | No authority claimed; candidate/scaffold only |
| `internal` | Internal working authority; not externally binding |
| `council_candidate` | Submitted to council for authority consideration |
| `council_ratified` | Ratified by council as authoritative |
| `canon_authority` | Full canon authority; ratified + adjudicated |

**Rule:** All artifacts in the Public KG Floodgate are `authority_scope: none`.

---

## Cross-Reference Matrix

| Artifact Stage | source_id | surface | raw_export_status | canon_status | deployment_status | authority_scope |
|----------------|-----------|---------|-------------------|--------------|-------------------|-----------------|
| GREEN packet (schema/enum) | stable | known | policy_only | not_canon | not_deployed | none |
| Raw import (live doc) | stable | known | not_exported | not_canon | not_deployed | none |
| Frozen export | stable | known | frozen_snapshot | not_canon | not_deployed | none |
| Full export ready | stable | known | full_raw_export_attached | not_canon | not_deployed | none |
| Canon candidate | stable | known | full_raw_export_attached | canon_candidate | not_deployed | council_candidate |
| Ratified canon | stable | known | full_raw_export_attached | canon | deployed_website | canon_authority |

---

*CANDIDATE — NOT CANON — authority_scope:none*
*"Enums are not evidence. Checklists are not exports."*
