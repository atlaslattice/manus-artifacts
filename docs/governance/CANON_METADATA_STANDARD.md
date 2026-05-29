# Canon Metadata Standard

## Summary

Defines the required and optional frontmatter fields for all artifacts in AtlasLattice.
Consistent metadata enables the knowledge graph, governance tracking, and automated quality gates.

---

## Required fields (all artifacts)

| Key | Type | Values / notes |
|---|---|---|
| `title` | string | Human-readable artifact title |
| `artifact_id` | string | Unique slug, e.g. `GOVERNANCE-001` |
| `created_utc` | ISO 8601 date | e.g. `2026-05-28` |
| `canon_status` | enum | `DRAFT` \| `CAND` \| `RAT_PEND` \| `CANON` \| `SUPERS` \| `REJECT` \| `ARCH` |
| `trust_state` | enum | `UNVERIFIED` \| `REVIEWED` \| `RATIFIED` |
| `author` | string or list | GitHub username(s), e.g. `@atlaslattice` |
| `domain` | string | Top-level domain, e.g. `governance`, `kg`, `ci` |

## Conditionally required fields

| Key | Required when | Type | Notes |
|---|---|---|---|
| `ratification_event_id` | `canon_status == CANON` | string | Links to ratification event record |
| `adjudication_receipt_id` | `canon_status == CANON` or `REJECT` | string | Links to adjudication receipt |
| `supersedes` | `canon_status == SUPERS` | string | artifact_id of predecessor |
| `superseded_by` | artifact is superseded | string | artifact_id of successor |

## Recommended optional fields

| Key | Type | Notes |
|---|---|---|
| `version` | semver string | e.g. `v1.0.0` |
| `tags` | list of strings | Keyword tags for KG linking |
| `related_artifacts` | list of artifact_ids | Cross-references |
| `source_lineage` | list of paths or URIs | Provenance sources |
| `last_reviewed_utc` | ISO 8601 date | Last human review date |
| `wave` | string | Campaign wave, e.g. `next144-w1` |

---

## Example frontmatter block

```yaml
---
title: "Canon Lifecycle State Machine"
artifact_id: "GOVERNANCE-001"
created_utc: "2026-05-28"
canon_status: CAND
trust_state: UNVERIFIED
author: "@atlaslattice"
domain: governance
version: v0.1.0
tags: [canon, lifecycle, governance]
related_artifacts: [GOVERNANCE-002, GOVERNANCE-003]
wave: next144-w1
---
```

---

## Validation

All artifacts in `docs/`, `schemas/`, `reference_impl/`, and `projects/` SHOULD include at minimum
the required fields. The `scripts/validate_artifact_metadata.py` script checks for presence of these
keys and will warn on missing fields.

---

## Cross-links

- [Canon Lifecycle State Machine](./CANON_LIFECYCLE_STATE_MACHINE.md)
- [Canon Registry](./CANON_REGISTRY.md)
- [Candidate Registry](./CANDIDATE_REGISTRY.md)
- [Trust-State Glossary](./TRUST_STATE_GLOSSARY.md)

## Status

`candidate` — not canon until ratified by full council and adjudicated by @atlaslattice.
