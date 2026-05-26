# Notion Mirror Candidate Workspace

This module is an upstream candidate packet, not proof.

Treat all summaries as claims until verified against repo files or source exports.
Do not expand scope beyond listed files unless explicitly instructed.
Preserve uncertainty.
Return blockers, patch items, tests run, files changed, and next safest action.

CANON: no
DEPLOYMENT: no
AUTHORITY: none


## Purpose

This folder is the bounded GitHub landing zone for Notion discovery, raw exports, parsed packets, review packets, and GitHub sync receipts. Notion discovery is not source completeness, and mirroring is not approval, canon, deployment, or authority.

## Source completeness warning

A Notion root listed here only means a candidate source was discovered or proposed. It does not prove that all related pages, subpages, attachments, comments, history, or external references were fetched.

## Operating lanes

- GPT cohort: preprocessing, clustering, draft shaping, boring extraction.
- Copilot/TIDELOCK: repo-grounded execution, patching, validation, containment.

## Duplicate rule

Duplicates are preserved with explicit duplicate/superseded routing. Do not delete candidate records solely because a duplicate is suspected.

## Files

- `NOTION_SOURCE_ROOT_INVENTORY_v0.1.yaml` — discovered root inventory.
- `NOTION_TO_GITHUB_MIRROR_PROTOCOL_v0.1.md` — mirror gate rules.
- `NOTION_GITHUB_SYNC_DOCKET_v0.1.yaml` — issue/PR mapping docket.
- `NOTION_CONTAMINATION_RULESET_v0.1.md` — contamination labels and outcomes.
- `raw_exports/` — raw export receipts only.
- `parsed_packets/` — parsed packets that cite raw/source material.
- `review_packets/` — review packets and explicit review states.
