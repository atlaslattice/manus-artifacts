# Notion to GitHub Mirror Protocol v0.1

This module is an upstream candidate packet, not proof.

Treat all summaries as claims until verified against repo files or source exports.
Do not expand scope beyond listed files unless explicitly instructed.
Preserve uncertainty.
Return blockers, patch items, tests run, files changed, and next safest action.

CANON: no
DEPLOYMENT: no
AUTHORITY: none


## Status vocabulary

- `not_mirrored`: discovered but no GitHub copy exists.
- `mirror_candidate`: ready for bounded raw-first mirroring.
- `mirrored_raw`: raw source export or receipt preserved.
- `parsed`: parsed packet exists and cites raw/source material.
- `quarantined`: preserved but blocked from authority.
- `superseded`: replaced by a newer candidate without deletion.

## Required mirror metadata

Each mirror packet must include: source id, source title, source URL or raw export pointer, retrieved_at_utc, retrieved_by, raw_export_status, access_scope, privacy_review_required, canon_status, deployment_status, authority boundary, checksum if available, issue/PR refs if known, contamination flags, and next safest action.

## Folder targets

- `archive/notion_mirror/raw_exports/` for raw export receipts and raw-source pointers.
- `archive/notion_mirror/parsed_packets/` for normalized extraction packets.
- `archive/notion_mirror/review_packets/` for explicit review packets.

## Non-promotion rules

Mirroring does not imply approval. Mirroring does not imply canon. Mirroring does not imply source completeness. A page cannot promote itself by being copied into GitHub.

## Raw-first workflow

1. Record discovery in the source root inventory.
2. Preserve raw export or raw-export receipt before parsing.
3. Add checksum when available.
4. Mark missing or partial exports explicitly.

## Parsed-packet workflow

1. Create a parsed packet only after a raw/source pointer exists.
2. Cite `derived_from` raw path or URL for each extracted claim group.
3. Preserve uncertainty and contamination flags.

## Review-packet workflow

1. Route parsed packets to review without changing canon status.
2. Record reviewer, review state, findings, blockers, and next safest action.
3. Require a separate ratification event before any `ratified` state.

## Failure modes for partial exports

- Missing subpages.
- Missing attachments.
- Missing comments or page history.
- Summary-only copy.
- Unclear access scope.
- Stale or conflicting version.
- Unsupported claim of completeness.

## Example mirror packet

```yaml
source_id: notion-root-001
mirror_status: mirror_candidate
source_title: UNKNOWN
source_url: UNKNOWN
raw_export_pointer: null
retrieved_at_utc: null
retrieved_by: null
raw_export_status: not_exported
sha256_if_available: null
access_scope: unknown
privacy_review_required: true
canon_status: not_canon
deployment_status: not_deployable
authority: none
contamination_flags: []
claims_requiring_verification:
  - Any summary or title-derived interpretation.
next_safest_action: Fetch raw export or add source URL receipt before parsing.
```

## Definition of done

A future agent can mirror one Notion page into GitHub without pretending it is verified.
