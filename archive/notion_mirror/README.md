# Notion Mirror

status: candidate
canon_status: not_canon
deployment_status: not_deployable
authority: none

This directory is the GitHub receipt layer for candidate Notion discovery, raw exports, parsed packets, review packets, and sync dockets.

## Boundary

Notion discovery is not source completeness. A discovered page title or URL is only a lead until raw content is fetched, preserved, cited, and reviewed. Location in this directory does not grant approval, canon, authority, or deployment status.

## Layers

- `NOTION_SOURCE_ROOT_INVENTORY_v0.1.yaml` records discovered roots and missing context.
- `raw_exports/` stores raw export receipts and raw-first custody notes.
- `parsed_packets/` stores extracted packets that cite raw/source records.
- `review_packets/` stores human or council review packets.
- `NOTION_GITHUB_SYNC_DOCKET_v0.1.yaml` ties roots to issues and PRs when known.

## Safe operating rule

Preserve uncertainty. If a future agent cannot verify a Notion source against raw export or source URL, the next safest action is to mark the item blocked and request source access rather than synthesize completeness.
