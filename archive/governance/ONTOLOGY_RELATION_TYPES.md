---
artifact_id: KG-SPEC-ONTOLOGY-RELATIONS-001
title: Ontology Relation Types
status: candidate
created: 2026-05-28
owner: council
tags: [knowledge-graph, ontology, relations, schema]
---

# Ontology Relation Types

> Defines the typed relationships used in the Atlas Lattice knowledge graph — enabling machine-readable traversal and semantic querying.

status: candidate

---

## Executive Summary

**Purpose:** Establishes a controlled vocabulary of relation types for linking artifacts in the knowledge graph.
**Audience:** Contributors, AI agents, KG query systems.
**Status:** `candidate`
**Key Decisions:** 14 core relation types defined; relations are expressed in YAML frontmatter under `relations:`; bidirectionality is not assumed.
**Action Required:** Use these relation types when adding `relations:` sections to frontmatter.
**Related Artifacts:** [Persistent Artifact ID Standard](./PERSISTENT_ARTIFACT_ID_STANDARD.md), [Metadata Headers Standard](./METADATA_HEADERS_STANDARD.md)

---

## Relation Syntax

Relations are expressed in document frontmatter under the `relations:` key:

```yaml
relations:
  implements: [KG-SCHEMA-FRONTMATTER-001]
  supersedes: [GOV-POLICY-CANON-STATUS-000]
  references: [LEGAL-REPORT-LICENSE-AUDIT-001, SEC-POLICY-VULN-DISCLOSURE-001]
  governed_by: [GOV-POLICY-REVIEW-SLA-001]
```

Each value is a list of `artifact_id` references.

---

## Core Relation Type Registry

### Hierarchical Relations

| Relation | Meaning | Example |
|----------|---------|---------|
| `parent_of` | This document is the parent/index of the target | A campaign board → individual mission docs |
| `child_of` | This document is a sub-component of the target | An appendix → the main spec |
| `part_of` | This document belongs to a collection (non-hierarchical) | A work log → the TIDELOCKBrain archive |

---

### Temporal / Lifecycle Relations

| Relation | Meaning | Example |
|----------|---------|---------|
| `supersedes` | This document replaces the target (target is deprecated) | v0.2 schema → v0.1 schema |
| `superseded_by` | The target replaces this document | v0.1 schema → v0.2 schema |
| `version_of` | This is a version of the same document as the target | Two date-stamped iterations |

---

### Semantic / Dependency Relations

| Relation | Meaning | Example |
|----------|---------|---------|
| `implements` | This document/impl satisfies the requirements in the target spec | Reference impl → Schema spec |
| `references` | This document cites or links to the target for context | A policy cites a compliance standard |
| `extends` | This document adds to or specializes the target | Appendix J extends Appendix A |
| `governed_by` | This document's content is governed by the target policy | Any artifact → the canon status model |
| `evidence_for` | This document provides evidence in support of the target | A test report → a compliance claim |

---

### Authorship / Agent Relations

| Relation | Meaning | Example |
|----------|---------|---------|
| `authored_by` | Identifies the creating agent or person | Work log → TIDELOCKBrain agent |
| `ratified_by` | Identifies the ratifying agent/person and event ID | Ratified doc → ratification event |
| `reviewed_by` | Documents a formal review | Governance doc → council review record |

---

## Inverse Relations

The KG query system automatically infers inverses. Authors need only declare one direction:

| Declared | Auto-inferred inverse |
|----------|----------------------|
| `parent_of` | `child_of` |
| `supersedes` | `superseded_by` |
| `implements` | `implemented_by` |
| `governed_by` | `governs` |
| `evidence_for` | `evidenced_by` |

---

## Query Examples

```python
# Find all documents that implement a given spec
kg.query("implements", target="KG-SCHEMA-FRONTMATTER-001")

# Find all evidence for a compliance claim
kg.query("evidence_for", target="LEGAL-REPORT-LICENSE-AUDIT-001")

# Find all documents governed by the canon status model
kg.query("governed_by", target="GOV-POLICY-CANON-STATUS-001")
```

(See `scripts/kg_query.py` for the query API.)

---

## Extension Process

To propose a new relation type:
1. Open an RFC per the [RFC Proposal Template](../docs/RFC_PROPOSAL_TEMPLATE.md)
2. Describe the relation semantics and inverse
3. Provide 2+ concrete usage examples
4. Council ratification required before the relation type is canonical

---

*Atlas Lattice Foundation · status: candidate*
