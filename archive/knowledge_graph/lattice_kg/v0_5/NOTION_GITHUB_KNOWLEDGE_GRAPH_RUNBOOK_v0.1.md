# Notion GitHub Knowledge Graph Runbook v0.1

status: candidate
canon_status: not_canon
deployment_status: not_deployable
authority: none

## Pipeline

1. Search → fetch: record query, URL, timestamp, and access scope before fetching.
2. Fetch → raw receipt: preserve raw export or receipt under `archive/notion_mirror/raw_exports/`.
3. Raw receipt → mirror packet: mark mirror status and keep canon/deployment false.
4. Mirror packet → graph node: create `raw_source` node with source pointer.
5. Graph node → graph edge: add `derived_from`, `supports`, `contradicts`, or `supersedes` only with evidence.
6. Graph edge → ORCS state: route through crosswalk without promotion.
7. ORCS state → review packet: record reviewer, scope, outcome, blockers, and next safest action.

## One-page manual workflow

Inventory the root, fetch raw content if permitted, write a raw receipt, extract only cited facts, create graph objects, route to ORCS state, and stop at review if ratification is absent.

## Ten-page batch workflow

Create a batch docket, process each page independently, preserve per-page raw receipts, detect duplicates, route conflicts to contradiction records, and summarize only blockers and next actions at batch level.

## Stop conditions

- Raw source is missing.
- Access scope is unknown.
- Privacy review is unresolved.
- Content claims completeness from summary-only material.
- A packet attempts to self-ratify.
- A duplicate cannot be safely linked.

## Operator checklist

- [ ] Inventory record has title, URL, timestamp, query, status, canon status, deployment status, raw status, and access scope.
- [ ] Raw receipt exists or blocker says why it does not.
- [ ] Parsed facts cite raw/source material.
- [ ] Claims have `derived_from` paths.
- [ ] Contamination flags are routed.
- [ ] GitHub issue/PR mapping is present or marked `needs_triage`.
- [ ] Review packet does not ratify without event.
- [ ] Next safest action is explicit.
