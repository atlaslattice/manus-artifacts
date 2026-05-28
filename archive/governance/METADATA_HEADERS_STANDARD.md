# Metadata Headers Standard

*Atlas Lattice Foundation · Aetherforge Mission #37 · 2026-05-28*

status: candidate

> Defines the required and optional metadata header fields for all Atlas Lattice artifacts, ensuring machine-readable provenance and consistent indexing in the knowledge graph.

---

## Overview

Every significant artifact in the Atlas Lattice repository must carry a YAML frontmatter block at the top of the file. This enables:
- Automated KG indexing
- Status and lifecycle tracking
- Provenance and attribution
- Search and discovery

---

## Required Fields

```yaml
---
title: "Human-readable title"
artifact_id: ALF-[DOMAIN]-[YEAR]-[SEQUENCE]
status: candidate | deprecated | archived
created: YYYY-MM-DD
owner: "@github-username or Atlas Lattice Foundation"
tags: [tag1, tag2]
---
```

| Field | Type | Description |
|-------|------|-------------|
| `title` | string | Human-readable artifact title |
| `artifact_id` | string | Persistent unique ID per taxonomy |
| `status` | enum | Current lifecycle state |
| `created` | date | ISO 8601 creation date |
| `owner` | string | GitHub username or org |
| `tags` | list | Domain tags (max 8, kebab-case) |

---

## Optional Fields

```yaml
---
canon_status: candidate | ratified | deprecated
lifecycle_state: draft | review | active | maintenance | deprecated | archived
ratification_event_id: "COUNCIL-2026-Q3-RAT-042"
trust_state: WORK | CANDIDATE | VERIFIED | BLOCKED
last_updated: YYYY-MM-DD
provenance: "Brief statement of how/why this was created"
supersedes: "path/to/previous-version.md"
superseded_by: "path/to/new-version.md"
related:
  - "path/to/related-doc.md"
---
```

---

## Status Enum Values

| Value | Meaning |
|-------|---------|
| `candidate` | Default; not yet ratified |
| `deprecated` | Superseded; no longer updated |
| `archived` | Frozen historical record |
| `canon` | Ratified and adjudicated (rare; set by @atlaslattice only) |

---

## Artifact ID Format

```
ALF-[DOMAIN-ABBREV]-[YEAR]-[SEQUENCE-5DIGIT]
```

Domain abbreviations:
| Domain | Abbrev |
|--------|--------|
| Governance | GOV |
| Specification | SPEC |
| Knowledge Graph | KG |
| Dream / Memory | DREAM |
| Research | RES |
| Operations | OPS |
| Community | COM |

Example: `ALF-GOV-2026-00001`

Persistent ID assignment is Mission #50.

---

## Scope of Application

**Required for:** All markdown files under `archive/`, `docs/`, `projects/`, `schemas/` (metadata docs)

**Optional for:** Root-level standard files (`README.md`, `LICENSE`, `SECURITY.md`), auto-generated files, test files

---

## CI Enforcement

Mission #63 (metadata completeness checks) will add a CI check that flags new files in required-scope directories missing frontmatter fields.

---

## Related Documents

- [Universal Frontmatter Schema](../../docs/UNIVERSAL_FRONTMATTER_SCHEMA.md)
- [Archive Taxonomy Map](./ARCHIVE_TAXONOMY_MAP.md)
- [Change Classification Rules](./CHANGE_CLASSIFICATION_RULES.md)

---

*Maintained by Atlas Lattice Foundation · status: candidate until ratified*
