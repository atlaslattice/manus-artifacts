# Import Triage Classes

> **Status:** CANDIDATE  
> **Artifact Type:** decision guide  
> **Date:** 2026-05-28  
> **Related:** [Migration Standards](./migration-standards-v0.1.md), [Intake Checklist](./intake-checklist.md), [Deprecation Policy](../deprecation-policy.md)

## Triage Classes

### `PRESERVE`
<!-- METADATA
stable_id: AL-SYS-203
lifecycle_state: CANDIDATE
owner: @atlaslattice
date_created: 2026-05-28
canon_status: candidate
-->

Migrate the artifact mostly as-is and attach a provenance block.

### `NORMALIZE`
Migrate the artifact, but reformat structure, headers, or navigation to match repo conventions.

### `DEPRECATE`
Migrate the artifact for historical continuity, then immediately mark it deprecated with a replacement link.

### `REJECT`
Do not migrate the artifact.

**Common reasons to reject:** duplicate content, no provenance, unsafe content, or insufficient confidence that the source is authentic.

## ASCII Decision Tree

```text
           ┌──────────────────────────────┐
           │  New source artifact found?  │
           └──────────────┬───────────────┘
                          │ yes
                          ▼
            ┌────────────────────────────┐
            │ Is provenance recoverable? │
            └──────────────┬─────────────┘
                     no    │ yes
                     ▼     ▼
                [REJECT]  ┌──────────────────────────────┐
                          │ Is it already duplicated or  │
                          │ superseded in the repo?      │
                          └──────────────┬───────────────┘
                                   yes   │ no
                                   ▼     ▼
                           ┌────────────┐ ┌──────────────────────────────┐
                           │DEPRECATE   │ │ Does structure already match │
                           │(keep path, │ │ repo conventions closely?    │
                           │add link)   │ └──────────────┬───────────────┘
                           └────────────┘         yes    │ no
                                                      ▼  ▼
                                                [PRESERVE] [NORMALIZE]
```
