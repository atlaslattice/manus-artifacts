# Notion GitHub Knowledge Graph Runbook v0.1

This module is an upstream candidate packet, not proof.

Treat all summaries as claims until verified against repo files or source exports.
Do not expand scope beyond listed files unless explicitly instructed.
Preserve uncertainty.
Return blockers, patch items, tests run, files changed, and next safest action.

CANON: no
DEPLOYMENT: no
AUTHORITY: none


## Pipeline

1. Search → fetch: record search query and discovered root before fetching.
2. Fetch → raw receipt: preserve raw export status, retriever, timestamp, access scope, and checksum if available.
3. Raw receipt → mirror packet: create bounded mirror metadata without canon claims.
4. Mirror packet → graph node: create `raw_source`, `parsed_fact`, or `claim` nodes with `derived_from`.
5. Graph node → graph edge: add sourced edges such as `supports`, `contradicts`, or `supersedes`.
6. Graph edge → ORCS state: map to raw, parsed, candidate, under_review, quarantined, superseded, or ratified.
7. ORCS state → review packet: record findings, blockers, and next safest action.

## One-page manual workflow

Process one page only: inventory record, raw receipt, parsed packet if sourced, graph node, review packet if needed, tests, and docket update.

## Ten-page batch workflow

Batch only after each page has a stable inventory record. Stop the batch if any page lacks access scope, raw export status, or source URL/raw pointer.

## Stop conditions

- Privacy review unresolved.
- Raw/source pointer missing.
- Summary-only packet claims completeness.
- Unsupported ratification or authority wording.
- Scope would expand beyond listed files.

## Operator checklist

- [ ] Inventory record exists.
- [ ] Raw export receipt or source URL exists.
- [ ] `canon_status: not_canon` preserved.
- [ ] `deployment_status: not_deployable` preserved.
- [ ] Claims cite `derived_from`.
- [ ] Blockers and next safest action recorded.

## Definition of done

A future agent can process one Notion page from discovery to graph record without inventing context.
