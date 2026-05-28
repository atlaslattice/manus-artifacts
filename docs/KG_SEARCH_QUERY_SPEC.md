# KG Hypercube Search Query Spec

Status: Candidate
Date: 2026-05-28

Defines the query language and search patterns for navigating the Lattice Knowledge Graph hypercube. Enables functional archival and retrieval of logs across the 144-domain lattice.

## Purpose

The Lattice KG is a hypercube: every node can be reached from every other node through a defined path. This spec defines how to query that hypercube for:
1. Node lookup by ID, type, or domain.
2. Path traversal (shortest path, all paths, reachability).
3. Subgraph extraction (by type, domain, agent lineage).
4. Staleness and quality filtering.

## Query Language

### Simple Lookup

```
GET /node/<node-id>
GET /nodes?type=<type>
GET /nodes?domain=<domain>
```

### Path Traversal

```
PATH <from-node-id> TO <to-node-id>
PATH N-README TO N-GPTDREAM-SURFACE
# → N-README → N-TOP50 → N-QUEST → N-VALIDATION → N-GPTDREAM-SURFACE
```

### Subgraph Extraction

```
SUBGRAPH type=Agent
# Returns all agent nodes and their direct connections

SUBGRAPH domain=governance
# Returns all governance nodes (Governance type)

SUBGRAPH lineage=tidelock
# Returns all nodes attributed to TIDELOCK lineage
```

### Reachability Check

```
REACH N-SHELDON IN 3 HOPS
# Returns all nodes reachable from N-SHELDON within 3 hops
```

### Quality Filters

```
NODES WHERE exists=true AND links >= 2
NODES WHERE type=Validation AND links > 0
```

## JSON Query Format

For programmatic use, queries are expressed as JSON:

```json
{
  "query_type": "subgraph | path | lookup | reach",
  "params": {
    "from": "<node-id>",
    "to": "<node-id>",
    "type_filter": "<node type or null>",
    "max_hops": 3,
    "quality_filter": {
      "must_exist": true,
      "min_links": 1
    }
  }
}
```

## Implementation

The current implementation uses the global index JSON directly:
- `docs/generated/LATTICE_GLOBAL_INDEX.json` — node and edge data
- `docs/generated/KG_ADJACENCY_MATRIX.json` — adjacency for path queries
- `docs/generated/swarm_exports/` — agent-scoped derived lattice slices

### Python Query API (reference)

```python
from scripts.build_lattice_global_index import parse_nodes

nodes = parse_nodes()
node_map = {n["id"]: n for n in nodes}

# Lookup
node = node_map.get("N-SHELDON")

# Subgraph by type
agents = [n for n in nodes if n["type"] == "Agent"]

# BFS reachability
from collections import deque
def reach(start_id, max_hops=3):
    visited, queue = {start_id}, deque([(start_id, 0)])
    while queue:
        nid, depth = queue.popleft()
        if depth < max_hops:
            for link in node_map.get(nid, {}).get("links", []):
                if link not in visited and link in node_map:
                    visited.add(link)
                    queue.append((link, depth + 1))
    return visited
```

## Use Cases

### Research retrieval
Find all artifacts related to a research topic:
```
SUBGRAPH domain=research → returns N-RESEARCH and linked archive nodes
```

### Evidence gathering
Find all evidence bundles for AI systems:
```
SUBGRAPH type=Archive AND lineage=evidence → returns N-EVIDENCE linked nodes
```

### Governance audit
Find the governance chain from any artifact back to mission:
```
PATH N-RISK TO N-MISSION → N-RISK → N-GOV-INDEX → N-MISSION
```

### Agent lineage trace
Find all contributions from a specific agent:
```
SUBGRAPH lineage=<agent-id> → derived lattice slice for that agent
```

## Future: Vector Search Extension

Phase 2 will add vector embedding lookups:
```
SEMANTIC SEARCH "regenerative computing constitutional principles"
# Returns top-k semantically similar nodes
```

## Related

- [LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md](./LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md)
- [KG_TOPOLOGY_GUIDE.md](./KG_TOPOLOGY_GUIDE.md)
- [KG_DOMAIN_SUBGRAPHS.md](./KG_DOMAIN_SUBGRAPHS.md)
- [scripts/build_lattice_global_index.py](../scripts/build_lattice_global_index.py)
- [docs/generated/KG_ADJACENCY_MATRIX.json](./generated/KG_ADJACENCY_MATRIX.json)
