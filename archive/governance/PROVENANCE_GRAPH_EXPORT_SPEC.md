---
artifact_id: KG-SPEC-PROVENANCE-EXPORT-001
title: Provenance Graph Export Specification
status: candidate
created: 2026-05-28
owner: council
tags: [knowledge-graph, provenance, export, graph-format]
---

# Provenance Graph Export Specification

> Defines the format and process for exporting the Atlas Lattice knowledge graph as a machine-readable provenance graph.

status: candidate

---

## Executive Summary

**Purpose:** Enables external tools, AI agents, and humans to consume the full artifact provenance graph in standard formats.
**Audience:** Engineers, AI integrators, KG systems.
**Status:** `candidate`
**Key Decisions:** Primary export format is JSON-LD; secondary is TSV edge list; export triggered by `scripts/build_lattice_global_index.py`; output at `kg/provenance_graph.json`.
**Action Required:** None — reference for implementers. Automated export runs in CI.
**Related Artifacts:** [Ontology Relation Types](./ONTOLOGY_RELATION_TYPES.md), [Machine-Readable Citation Blocks Standard](./MACHINE_READABLE_CITATION_BLOCKS.md), [Persistent Artifact ID Standard](./PERSISTENT_ARTIFACT_ID_STANDARD.md)

---

## Overview

The provenance graph captures every artifact as a **node** and every relationship as a **directed edge**. Sources include:

1. **Frontmatter `relations:` sections** — declared relationships
2. **Parsed `cite` blocks** — citation-derived edges
3. **Markdown links** — implicitly extracted link edges (typed as `references`)
4. **Taskboard completion entries** — task → artifact edges

---

## Node Schema

Each artifact becomes a node:

```json
{
  "id": "GOV-POLICY-CANON-STATUS-001",
  "path": "archive/governance/CANON_STATUS_MODEL.md",
  "title": "Canon Status Model",
  "status": "candidate",
  "created": "2026-05-26",
  "owner": "council",
  "tags": ["governance", "canon", "status"],
  "type": "policy"
}
```

---

## Edge Schema

Each relationship becomes a directed edge:

```json
{
  "source": "KG-SPEC-CITATION-BLOCKS-001",
  "target": "GOV-POLICY-CANON-STATUS-001",
  "relation": "references",
  "weight": 1.0,
  "extracted_from": "frontmatter.relations",
  "accessed": "2026-05-28"
}
```

---

## Export Formats

### Primary: JSON-LD

```json
{
  "@context": {
    "@vocab": "https://atlaslattice.org/kg/",
    "artifact_id": "schema:identifier",
    "implements": "schema:implements",
    "supersedes": "schema:supersedes"
  },
  "nodes": [ ... ],
  "edges": [ ... ],
  "exported_at": "2026-05-28T00:00:00Z",
  "total_nodes": 142,
  "total_edges": 537
}
```

**Output path:** `kg/provenance_graph.json`

### Secondary: TSV Edge List

Human-readable tab-separated edge list for quick inspection:

```tsv
source_id	relation	target_id	extracted_from
KG-SPEC-CITATION-001	implements	KG-SCHEMA-FRONTMATTER-001	frontmatter.relations
GOV-POLICY-CANON-001	references	LEGAL-REPORT-LICENSE-001	markdown.link
```

**Output path:** `kg/provenance_graph_edges.tsv`

### Tertiary: DOT Graph

Graphviz DOT format for visualization:

```dot
digraph KG {
  "GOV-POLICY-001" -> "KG-SCHEMA-001" [label="governed_by"];
  ...
}
```

**Output path:** `kg/provenance_graph.dot`

---

## Export Process

The export is produced by `scripts/build_lattice_global_index.py`:

```bash
python scripts/build_lattice_global_index.py
# Outputs:
#   kg/provenance_graph.json
#   kg/provenance_graph_edges.tsv
#   kg/provenance_graph.dot  (planned)
```

The export runs automatically in CI on every push to main via `.github/workflows/lattice-kg-quality-gates.yml`.

---

## Quality Gates on Export

After export, `scripts/validate_lattice_quality_gates.py` checks:

| Check | Threshold |
|-------|-----------|
| Total nodes | ≥ 50 |
| Total edges | ≥ total_nodes × 0.8 (at least 0.8 edges per node on average) |
| Orphan nodes (0 edges) | ≤ 10% of total nodes |
| Frontmatter coverage | ≥ 80% of nodes have `artifact_id` |
| Broken references | 0 (all edge targets must resolve to known nodes) |

---

## Planned Enhancements

| Feature | Target |
|---------|--------|
| GraphQL query layer | Q3 2026 |
| Incremental export (delta only) | Q3 2026 |
| SPARQL endpoint (read-only) | Q4 2026 |
| Graph visualization (D3.js) | Q4 2026 (see #59) |

---

*Atlas Lattice Foundation · status: candidate*
