---
artifact_id: KG-SPEC-CITATION-BLOCKS-001
title: Machine-Readable Citation Blocks Standard
status: candidate
created: 2026-05-28
owner: council
tags: [knowledge-graph, citations, machine-readable, provenance]
---

# Machine-Readable Citation Blocks Standard

> Defines the format for structured citation blocks that enable automated provenance tracking and KG graph construction.

status: candidate

---

## Executive Summary

**Purpose:** Makes citations parseable by machines, not just readable by humans — enabling automated KG construction and provenance auditing.
**Audience:** Contributors, AI agents, KG automation scripts.
**Status:** `candidate`
**Key Decisions:** Citation blocks use fenced code blocks with `cite` language tag; required fields: `artifact_id`, `path`, `accessed`; optional: `section`, `lines`.
**Action Required:** Use citation blocks when making substantive claims that depend on another artifact's content.
**Related Artifacts:** [Persistent Artifact ID Standard](./PERSISTENT_ARTIFACT_ID_STANDARD.md), [Ontology Relation Types](./ONTOLOGY_RELATION_TYPES.md), [Metadata Headers Standard](./METADATA_HEADERS_STANDARD.md)

---

## When to Use Citation Blocks

Use a machine-readable citation block when:
- Referencing a specific section or lines from another artifact as the basis for a claim
- Creating evidence entries (compliance, AI evidence, provenance)
- Memory archives (TIDELOCKBrain wake reports, delta extractions) referencing source artifacts

Use a plain markdown link `[text](path)` when:
- Simply navigating a reader to a related document without making a specific claim
- Adding "See also" or "Related" references

---

## Citation Block Format

````markdown
```cite
artifact_id: GOV-POLICY-CANON-STATUS-001
path: archive/governance/CANON_STATUS_MODEL.md
section: "Canon Status Levels"
lines: 42-67
accessed: 2026-05-28
claim: "The valid status values are: candidate, ratified, deprecated, archived."
```
````

### Required Fields

| Field | Description |
|-------|-------------|
| `artifact_id` | Stable artifact ID per the [Persistent Artifact ID Standard](./PERSISTENT_ARTIFACT_ID_STANDARD.md) |
| `path` | Repository-relative path to the artifact |
| `accessed` | ISO 8601 date the citation was added (YYYY-MM-DD) |

### Optional Fields

| Field | Description |
|-------|-------------|
| `section` | Name of the section being cited (quoted string) |
| `lines` | Line range (e.g., `42-67`) |
| `claim` | The specific assertion supported by this citation |
| `relation` | Relation type from [Ontology Relation Types](./ONTOLOGY_RELATION_TYPES.md) (e.g., `evidence_for`) |

---

## Inline Citation vs Citation Block

**Inline citation** (quick reference, no machine parsing needed):
```markdown
The canon status model requires a `ratification_event_id` ([GOV-POLICY-CANON-STATUS-001](../archive/governance/CANON_STATUS_MODEL.md)).
```

**Citation block** (machine-parseable, provenance claim):
````markdown
```cite
artifact_id: GOV-POLICY-CANON-STATUS-001
path: archive/governance/CANON_STATUS_MODEL.md
section: "Ratification Requirements"
accessed: 2026-05-28
claim: "A ratification_event_id is required before an artifact may transition to ratified status."
relation: evidence_for
```
````

---

## Multiple Citations

When multiple artifacts support a single claim, list them as separate citation blocks one after another.

---

## Parsing

Citation blocks are parsed by `scripts/build_lattice_global_index.py` when building the KG index. Each parsed citation becomes a graph edge:

```
source_artifact --[relation]--> target_artifact
```

If `relation` is omitted, the default edge type is `references`.

---

## Memory Archive Usage

TIDELOCKBrain wake reports and delta extractions use citation blocks extensively to record which source artifacts informed a session's outputs:

````markdown
```cite
artifact_id: projects/aetherforge-next144-taskboard-2026-05-28
path: projects/aetherforge-next144-taskboard-2026-05-28.md
section: "Wave 4 Tasks"
accessed: 2026-05-28
claim: "Wave 4 tasks #37-#48 were completed in this session."
relation: evidence_for
```
````

---

*Atlas Lattice Foundation · status: candidate*
