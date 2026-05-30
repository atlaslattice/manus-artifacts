---
artifact_id: KG-ROADMAP-PUBLIC-API-001
title: Public KG API Roadmap
status: candidate
created: 2026-05-28
owner: council
tags: [knowledge-graph, api, roadmap, public-facing]
---

# Public KG API Roadmap

> Defines the roadmap for a public, machine-readable API that exposes the Atlas Lattice knowledge graph to external tools and AI agents.

status: candidate

---

## Executive Summary

**Purpose:** Charts the path from the current export-only KG to a fully queryable public API.
**Audience:** Engineers, AI integrators, potential open-source contributors.
**Status:** `candidate`
**Key Decisions:** API v1 is read-only; authentication not required for read; JSON-LD primary response format; deployment on GitHub Pages static + Vercel serverless for query endpoints.
**Action Required:** None — planning reference. Implement per the phases below.
**Related Artifacts:** [Provenance Graph Export Spec](./PROVENANCE_GRAPH_EXPORT_SPEC.md), [KG Visualization Surface Design](./KG_VISUALIZATION_SURFACE_DESIGN.md), [Ontology Relation Types](./ONTOLOGY_RELATION_TYPES.md)

---

## API Philosophy

The Atlas Lattice KG API is an **open-source gift to the world** — fully public, zero authentication required for reads, and designed to be consumed by humans, AI agents, and automated tools alike.

Design principles:
1. **Read-first** — v1 is read-only; writes happen through GitHub PRs
2. **Stable IDs** — `artifact_id` is the eternal key; paths and titles may change
3. **Standard formats** — JSON-LD, RDF, TSV; not proprietary formats
4. **Graceful degradation** — if the API is unavailable, the static files in `kg/` always work
5. **AI-friendly** — responses structured for consumption by LLMs with minimal prompt engineering

---

## Phase 1: Static File API (Current — via GitHub)

Already live:

| Resource | URL | Format |
|----------|-----|--------|
| Full graph export | `kg/provenance_graph.json` | JSON-LD |
| Edge list | `kg/provenance_graph_edges.tsv` | TSV |
| Global index | `kg/global_index.json` | JSON |

**Limitations:** No filtering, no single-artifact lookup, no query.

---

## Phase 2: GitHub Pages Static REST (Q3 2026)

One JSON file per artifact, built at CI time:

| Resource | URL pattern | Format |
|----------|------------|--------|
| Artifact by ID | `kg/artifacts/{artifact_id}.json` | JSON-LD |
| Artifacts by domain | `kg/domains/{domain}.json` | JSON array |
| Artifacts by tag | `kg/tags/{tag}.json` | JSON array |
| Artifacts by status | `kg/status/{status}.json` | JSON array |

**Built by:** An extended `scripts/build_lattice_global_index.py`
**Deployed by:** CI workflow writing to `kg/` directory on GitHub Pages

---

## Phase 3: Serverless Query API (Q4 2026)

A lightweight serverless function layer (Vercel or Cloudflare Workers) adds dynamic query support:

### Endpoints

```
GET /api/v1/artifacts/{artifact_id}
GET /api/v1/artifacts?tag=governance&status=candidate
GET /api/v1/artifacts/{artifact_id}/neighbors?depth=2
GET /api/v1/artifacts/{artifact_id}/relations/{relation_type}
GET /api/v1/search?q=vulnerability+disclosure
GET /api/v1/graph/stats
```

### Response format

```json
{
  "artifact_id": "GOV-POLICY-VULN-DISCLOSURE-001",
  "title": "Vulnerability Disclosure Process",
  "status": "candidate",
  "path": "archive/governance/VULNERABILITY_DISCLOSURE_PROCESS.md",
  "tags": ["governance", "security", "policy"],
  "relations": {
    "governed_by": ["GOV-POLICY-CANON-STATUS-001"],
    "references": ["SEC-POLICY-INCIDENT-RESPONSE-001"]
  },
  "inbound_link_count": 3,
  "outbound_link_count": 2
}
```

---

## Phase 4: SPARQL / GraphQL (Q1 2027)

For power users and AI knowledge retrieval systems:

| Interface | Technology | Use case |
|-----------|-----------|---------|
| GraphQL | Apollo Server (serverless) | Flexible relationship traversal |
| SPARQL | Apache Jena or similar | Semantic web compatibility |

---

## AI Agent Integration

For AI agents needing to hydrate from the KG during a session:

```python
# Fetch artifact by ID
import httpx
r = httpx.get("https://atlaslattice.github.io/manus-artifacts/kg/artifacts/KG-SPEC-CITATION-BLOCKS-001.json")
artifact = r.json()

# Find all governance policies
r = httpx.get("https://atlaslattice.github.io/manus-artifacts/kg/domains/governance.json")
policies = r.json()
```

---

## Rate Limits and Terms

- **v1 (static GitHub Pages):** No rate limits — static file serving
- **v2+ (serverless):** 1,000 requests/hour per IP for unauthenticated; higher limits for authenticated contributors
- **License:** All API responses are MIT-licensed; data is open source
- **Attribution:** Encouraged but not required

---

*Atlas Lattice Foundation · status: candidate*
