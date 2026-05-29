# Artifact ID Convention Draft (Candidate)

Status: `candidate` (not canon)  
Date: `2026-05-26`  
Scope: repository-wide artifact naming for traceability and cross-linking.

## Format

`<DOMAIN>_<SUBDOMAIN>_<ARTIFACT_KIND>_<VERSION_OR_PHASE>_<YYYY-MM-DD>`

## Segment rules

- `DOMAIN`: broad area (for example: `GPTDREAM`, `TIDELOCK`, `SOURCEGRAPH`, `COUNCIL`).
- `SUBDOMAIN`: narrower lane or seat (for example: `S7`, `REHYDRATION`, `APPENDIXJ`).
- `ARTIFACT_KIND`: document type (for example: `SPEC`, `REPORT`, `INDEX`, `CHECKLIST`, `MAP`).
- `VERSION_OR_PHASE`: semantic version or execution phase (for example: `v0.1`, `WAVE1`, `DRAFT1`).
- `YYYY-MM-DD`: creation date in ISO format.

## File naming guidance

- Keep names uppercase with underscores for primary governed artifacts.
- Keep date suffixes explicit when chronology matters.
- Keep “DRAFT” markers for non-ratified artifacts.
- Preserve existing historical filenames; apply this convention to new artifacts and major refreshes.

## Example IDs

- `TIDELOCK_S7_INDEX_v0.1_2026-05-26`
- `GPTDREAM_APPENDIXJ_SPEC_v0.1_2026-05-22`
- `COUNCIL_REVIEW_REPORT_WAVE1_2026-05-26`
- `SOURCEGRAPH_ENGINE_SPEC_v0.1_2026-05-26`

## Governance note

This convention draft is operational guidance only and does not confer canon status.

