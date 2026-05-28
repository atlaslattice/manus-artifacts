---
artifact_id: CICD-POLICY-METADATA-COMPLETENESS-001
title: Metadata Completeness Check Policy
status: candidate
created: 2026-05-28
owner: council
tags: [ci-cd, metadata, completeness, quality-gates]
---

# Metadata Completeness Check Policy

> Defines the required frontmatter fields and the automated CI gate that enforces their presence.

status: candidate

---

## Required Frontmatter Fields

All artifacts in `archive/` and `docs/` must include these YAML frontmatter fields:

| Field | Required in | Format | Example |
|-------|------------|--------|---------|
| `artifact_id` | All governance docs | `DOMAIN-TYPE-SLUG-NNN` | `GOV-POLICY-CANON-001` |
| `title` | All docs | Free text string | `"Canon Status Model"` |
| `status` | All docs | `candidate \| ratified \| deprecated` | `candidate` |
| `created` | All docs | ISO 8601 date | `2026-05-28` |
| `owner` | Governance docs | Team or person | `council` |
| `tags` | All docs | YAML list, kebab-case | `[governance, policy]` |

---

## Optional But Encouraged Fields

| Field | When to use | Format |
|-------|------------|--------|
| `updated` | When content is materially revised | ISO 8601 date |
| `relations` | When artifact has typed KG relationships | YAML map per Ontology Relation Types |
| `superseded_by` | Deprecated docs only | Artifact ID |
| `ratification_event_id` | Ratified docs only | Event ID string |

---

## Coverage Target

| Location | Mandatory fields coverage target |
|----------|--------------------------------|
| `archive/governance/` | 100% by Q3 2026 |
| `archive/spec/` | 100% by Q3 2026 |
| `docs/` | 80% by Q3 2026 |
| `archive/boot/` | 60% by Q4 2026 |
| All other `archive/` | 50% by Q4 2026 |

---

## CI Gate (Planned: Q3 2026)

`scripts/check_metadata_completeness.py` will run on every PR and:
1. Enumerate all `.md` files in `archive/governance/`, `archive/spec/`, and `docs/`
2. Parse YAML frontmatter
3. Report missing required fields per file
4. Fail if any `archive/governance/` file is missing `artifact_id`, `title`, `status`, or `created`
5. Warn (not fail) for `docs/` files missing optional fields

---

## Repair Process

To fix a metadata completeness failure:

1. Open the flagged file
2. Add a YAML frontmatter block at the top if missing:
   ```yaml
   ---
   artifact_id: GOV-POLICY-YOUR-DOC-001
   title: Your Document Title
   status: candidate
   created: YYYY-MM-DD
   owner: council
   tags: [tag1, tag2]
   ---
   ```
3. Assign a new `artifact_id` per the [Persistent Artifact ID Standard](./PERSISTENT_ARTIFACT_ID_STANDARD.md)
4. Re-run the check locally: `python scripts/check_metadata_completeness.py`

---

*Atlas Lattice Foundation · status: candidate*
