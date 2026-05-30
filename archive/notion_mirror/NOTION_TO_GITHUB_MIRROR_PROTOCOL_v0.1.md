# Notion to GitHub Mirror Protocol v0.1

status: candidate
canon_status: not_canon
deployment_status: not_deployable
authority: none

## Boundary Header

This module is an upstream candidate packet, not proof.
Treat all summaries as claims until verified against repo files or source exports.
Do not expand scope beyond listed files unless explicitly instructed.
Preserve uncertainty.
Return blockers, patch items, tests run, files changed, and next safest action.

CANON: no  
DEPLOYMENT: no  
AUTHORITY: none

## Mirror statuses

- `not_mirrored`: discovered lead only; no GitHub raw receipt exists.
- `mirror_candidate`: candidate selected for safe raw capture.
- `mirrored_raw`: raw export or receipt exists in GitHub.
- `parsed`: parsed packet cites the raw export or source URL.
- `quarantined`: preserved with contamination flags and blocked from authority.
- `superseded`: preserved but displaced by a newer cited record.

## Required mirror metadata

Every mirror packet should include title, URL or raw export pointer, retrieved time, retrieved by, source status, raw export status, sha256 if available, access scope, canon status, deployment status, privacy review status, issue/PR references, and next safest action.

## Folder targets

- Raw receipts: `archive/notion_mirror/raw_exports/`
- Parsed packets: `archive/notion_mirror/parsed_packets/`
- Review packets: `archive/notion_mirror/review_packets/`
- Inventory and dockets: `archive/notion_mirror/`

## Rules

1. Mirror does not imply approval.
2. Mirror does not imply canon.
3. Mirror does not imply source completeness.
4. Raw export is preserved before interpretation.
5. Parsed packets must cite the raw/source record they derive from.
6. Review packets must identify reviewer, review scope, outcome, and open claims.
7. Partial exports are labeled partial and cannot be used to claim completeness.

## Workflows

### Raw-first workflow

Discover source lead, record inventory entry, fetch raw export if permitted, write raw receipt, compute checksum if available, and keep status non-canon/non-deployable.

### Parsed-packet workflow

Read raw/source, extract bounded facts, cite exact source pointer, list uncertainty, and block any summary-only completeness claim.

### Review-packet workflow

Reviewer inspects raw and parsed packet, records review outcome, routes to ORCS state, and leaves ratification empty unless there is an explicit ratification event.

## Failure modes for partial exports

- Missing raw body: `missing_raw`
- Only summary available: `summary_only`
- Unclear access scope: `access_scope_unknown`
- Export interrupted: `partial_export`
- Conflicting page versions: `conflicting_version`
- Privacy risk unresolved: `privacy_review_required`

## Example mirror packet

```yaml
packet_id: notion-mirror-example-v0-1
mirror_status: mirror_candidate
title: Example Notion Root
source_url: https://www.notion.so/example
raw_export_pointer: null
retrieved_at_utc: null
retrieved_by: null
sha256_if_available: null
canon_status: not_canon
deployment_status: not_deployable
raw_export_status: missing_raw
access_scope:
  visible_sources: []
  unavailable_sources: [full Notion page content]
  assumed_context: []
claims_requiring_verification:
  - page title and URL only identify a lead
next_safest_action: fetch raw export before parsing
```
