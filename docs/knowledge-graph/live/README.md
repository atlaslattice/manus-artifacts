# Live KG Explorer (Candidate)

This surface provides:

- 3D force graph traversal of the registered artifact graph
- static browser search over registry-indexed artifacts
- H-S-N coordinate hints generated deterministically for every node

## Build payloads

```bash
python scripts/build_live_graph_payload.py
python scripts/build_search_index.py
```

## Open locally

```bash
cd docs/knowledge-graph/live
python -m http.server 8080
```

Then open: `http://localhost:8080/index.html`
