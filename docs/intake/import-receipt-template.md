# Import Receipt Template

> **Status:** CANDIDATE  
> **Artifact Type:** template  
> **Date:** 2026-05-28  
> **Related:** [Migration Standards](./migration-standards-v0.1.md), [Intake Checklist](./intake-checklist.md), [Validation Receipt Format](../validation-receipt-format-v0.1.md)

## Template

<!-- METADATA
stable_id: AL-SYS-205
lifecycle_state: CANDIDATE
owner: @atlaslattice
date_created: 2026-05-28
canon_status: candidate
-->

```yaml
receipt_id: AL-IMPORT-YYYY-MM-DD-001
import_date: 2026-05-28
source_system: Notion
source_doc_title: Example Source Title
source_url: https://www.notion.so/example
triage_class: NORMALIZE
assigned_id: AL-EXAMPLE-001
migration_agent: TIDELOCK
validation_status: PASS
notes: Imported to docs/example/example-source-title.md and queued for KG registration.
```

## Filled Example

```yaml
receipt_id: AL-IMPORT-2026-05-28-001
import_date: 2026-05-28
source_system: Drive
source_doc_title: Aluminum OS Investor Notes v0.3
source_url: https://drive.google.com/example/aluminum-os-investor-notes
triage_class: NORMALIZE
assigned_id: AL-AL-021
migration_agent: TIDELOCK
validation_status: PASS
notes: Reformatted into repo markdown conventions, preserved original date, and queued for registry review after metadata validation.
```
