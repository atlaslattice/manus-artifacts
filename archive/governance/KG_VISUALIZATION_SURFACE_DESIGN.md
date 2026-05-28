---
artifact_id: KG-ROADMAP-VISUALIZATION-SURFACE-001
title: Knowledge Graph Visualization Surface Design
status: candidate
created: 2026-05-28
owner: council
tags: [knowledge-graph, visualization, roadmap, public-facing]
---

# Knowledge Graph Visualization Surface Design

> Design document for the public knowledge graph visualization — making the Atlas Lattice KG browsable and explorable by anyone.

status: candidate

---

## Executive Summary

**Purpose:** Defines what the KG visualization will look like, how it will be deployed, and the roadmap to make it live.
**Audience:** Engineers, council, public contributors.
**Status:** `candidate`
**Key Decisions:** Primary surface is a GitHub Pages static site; uses D3.js force-directed graph; data from `kg/provenance_graph.json`; MVP by Q4 2026.
**Action Required:** None — design reference for future implementation.
**Related Artifacts:** [Provenance Graph Export Spec](./PROVENANCE_GRAPH_EXPORT_SPEC.md), [Public KG API Roadmap](./KG_PUBLIC_API_ROADMAP.md)

---

## Vision

Anyone visiting the Atlas Lattice repository should be able to:
1. See the full artifact network as an interactive graph
2. Click any node to navigate to that artifact
3. Filter by domain, tag, or status
4. Search for artifacts and highlight them in the graph
5. Follow relationship edges to explore the knowledge graph

---

## Visualization Approach

### Primary: Force-Directed Node Graph

**Library:** D3.js v7
**Layout:** Force-directed graph — nodes repel; edges attract connected nodes
**Node appearance:**
- Color = domain (governance = blue, legal = red, KG = green, spec = purple, docs = orange)
- Size = inbound link count (hub nodes appear larger)
- Shape = document type (circle = policy, diamond = spec, square = index)

**Edge appearance:**
- Color = relation type (references = grey, implements = green, supersedes = orange)
- Arrow = direction of relation
- Thickness = citation frequency

---

### Filters and Controls

| Control | Function |
|---------|---------|
| Domain filter | Show only governance / legal / KG / spec / docs |
| Status filter | Show only candidate / ratified / deprecated |
| Tag filter | Multi-select from tag vocabulary |
| Depth slider | Show N-hop neighborhood around selected node |
| Search box | Highlight matching nodes |

---

### Click Behavior

- Single click: highlight node and its direct neighbors; show artifact card in sidebar
- Double click: navigate to the artifact on GitHub
- Right click: copy artifact_id to clipboard

---

## Artifact Card (Sidebar)

When a node is selected, a sidebar shows:

```
┌─────────────────────────────────┐
│ [Title]                         │
│ artifact_id: GOV-POLICY-001     │
│ status: candidate               │
│ created: 2026-05-28             │
│ owner: council                  │
│ tags: governance, policy        │
│                                 │
│ Outbound links: 4               │
│ Inbound links: 7                │
│                                 │
│ [View on GitHub ↗]             │
└─────────────────────────────────┘
```

---

## Deployment

**Host:** GitHub Pages (`https://atlaslattice.github.io/manus-artifacts/kg/`)
**Build:** Static HTML + D3.js; data from `kg/provenance_graph.json` (built in CI)
**Update frequency:** Rebuilds on every push to main
**Fallback:** If JS is disabled, the TSV edge list (`kg/provenance_graph_edges.tsv`) is linked as a plain-text alternative

---

## Implementation Roadmap

| Phase | Deliverable | Target |
|-------|-------------|--------|
| P0 | Data pipeline complete (`provenance_graph.json`) | ✅ 2026-05-28 (in CI) |
| P1 | Static HTML prototype with D3.js force graph | Q3 2026 |
| P2 | Filters, search, sidebar artifact card | Q3 2026 |
| P3 | GitHub Pages deployment + CI rebuild | Q4 2026 |
| P4 | SPARQL/GraphQL query overlay | Q1 2027 |

---

## Accessibility Requirements

- All nodes must have accessible labels (aria-label) with artifact title
- Color coding must not be the sole distinguishing factor (shapes required)
- Keyboard navigation: Tab to select nodes, Enter to open artifact
- Screen reader: reads artifact title and relation count when node is focused
- High-contrast mode toggle

---

*Atlas Lattice Foundation · status: candidate*
