# Migration Standards v0.1

> **Status:** CANDIDATE  
> **Artifact Type:** standards doc  
> **Date:** 2026-05-28  
> **Related:** [Import Triage Classes](./import-triage-classes.md), [Import Receipt Template](./import-receipt-template.md), [Metadata Validator](../../scripts/validate_metadata_completeness.py)

## Source Format Requirements

<!-- METADATA
stable_id: AL-SYS-202
lifecycle_state: CANDIDATE
owner: @atlaslattice
date_created: 2026-05-28
canon_status: candidate
-->

Before import, the source artifact must have:

- a stable title or clearly recoverable working title
- an original source system (`Notion`, `Drive`, or equivalent)
- a durable source URL or locator
- an original creation date or best-available provenance timestamp
- enough content fidelity to preserve meaning without hallucinated reconstruction

## Naming Conventions on Import

- New imported artifacts should use **kebab-case** filenames.
- The destination path should match the nearest durable repo domain.
- Version numbers stay in the filename when they are part of the source identity.

## Required Metadata Fields on Import

Imported artifacts should add or preserve:

- status / lifecycle state
- artifact type
- owner or steward
- original creation date
- source system
- source URL
- import date
- any assigned stable ID when applicable

## Provenance Preservation Rules

1. Keep the **original creation date** whenever it is known.
2. Keep the **source URL** even after content is normalized.
3. Note the migration agent or editor who performed the import.
4. Do not rewrite source lineage out of the document.

## Import Receipt Format

Every import should emit a receipt containing:

- `receipt_id`
- `import_date`
- `source_system`
- `source_doc_title`
- `source_url`
- `triage_class`
- `assigned_id`
- `migration_agent`
- `validation_status`
- `notes`

## Quality Check Before Registry

Before an imported artifact is treated as registry-ready, it must pass:

```bash
python3 scripts/validate_metadata_completeness.py
```

If the validator fails, the artifact remains candidate-only and should be routed back through intake cleanup before registry inclusion.
