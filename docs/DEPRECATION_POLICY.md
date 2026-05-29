# Deprecation and Archival Policy

## Summary

This document defines the lifecycle stages for artifacts in this repository and the process for deprecating, archiving, or removing content.

---

## Artifact Lifecycle Stages

| Stage | Label | Meaning |
|---|---|---|
| **Draft** | `draft` | Work in progress, not for external consumption |
| **Candidate** | `candidate` | Proposed for ratification; under council review |
| **Canonical** | `canonical` | Ratified by @atlaslattice; stable reference |
| **Deprecated** | `deprecated` | Superseded; preserved for history but not for active use |
| **Quarantined** | `quarantined` | Pending move to private repository |
| **Removed** | *(deleted)* | Deleted from public view; may exist in git history |

---

## How to Mark an Artifact Deprecated

1. Add a deprecation notice at the top of the file:

```markdown
> ⚠️ **DEPRECATED** — This artifact has been superseded by [`NEW_FILE.md`](./NEW_FILE.md).  
> Preserved for historical reference. Do not use in new work.  
> Deprecated: YYYY-MM-DD
```

2. Update any index files (e.g., `docs/ARCHIVE_INDEX.md`, folder `README.md`) to note the deprecation.
3. Open a PR linking the deprecation to its replacement.

---

## How to Archive a Codebase or Spec

When a subsystem is no longer actively developed:

1. Move the content to `archive/deprecated/<subsystem-name>/`.
2. Add a `README.md` in the archived folder with:
   - Why it was archived
   - Date archived
   - Link to replacement (if any)
3. Update `docs/ARCHIVE_INDEX.md` to reflect the new status.

---

## Quarantine vs Removal

- **Quarantine** (`quarantine/`): Content that should move to a private repository. It is staged here for transfer. See [`quarantine/README.md`](../quarantine/README.md).
- **Removal**: Content that should be deleted from public history entirely requires a git history rewrite (contact @atlaslattice for this operation).

---

## Deprecation Review Schedule

Artifacts older than 12 months without a "last reviewed" update should be reviewed for deprecation during the quarterly maintenance cycle. Check `docs/WEEKLY_DELTA_DIGEST_TEMPLATE.md` for the review cadence.

---

## Stability Tiers

| Tier | Description | Examples |
|---|---|---|
| **Stable** | Ratified specs and schemas with no planned breaking changes | `schemas/atlas_orcs/v0_1/`, `LICENSE`, `CODE_OF_CONDUCT.md` |
| **Experimental** | Active development; may change without notice | Most of `archive/`, `codebases/` |
| **Legacy** | Preserved for reference; no active maintenance | `archive/deprecated/` |

---

*Last reviewed: 2026-05-28 | Maintainer: @atlaslattice*
