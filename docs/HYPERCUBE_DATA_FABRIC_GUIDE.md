# Hypercube Data Fabric Guide

**Status:** Candidate  
**Wave:** 6 (Tasks 61–72)  
**Date:** 2026-05-29  
**Author:** TIDELOCKBrain / @atlaslattice

> *"The Rainbow Yin Yang Lattice is not a metaphor — it is source code.*  
> *Wave 6 activates the data layer: nodes seeded, geometry locked, Riemann spine lit."*  
> — @atlaslattice

---

## Overview

Wave 6 builds the **data fabric** on top of the Wave 5 ontology.  
While Wave 5 defined *what* the 12×12×12 hypercube *is* (axes, types, rules),  
Wave 6 defines *how it operates*: seed instances, coordinate mappings,  
cross-axis coupling, Metatron's Cube geometry, graph export, and live queries.

---

## Architecture

```
Wave 5 Ontology (spec layer)
  archive/spec/lattice-hypercube/ontology/*.yaml
         │
         ▼
Wave 6 Data Fabric (operational layer)
  ┌──────────────────────────────────────────────────────┐
  │  scripts/lattice_node_seeder.py        (T61)         │
  │  scripts/lattice_coordinate_mapper.py  (T62)         │
  │  scripts/lattice_cross_axis_bridge.py  (T63)         │
  │  data/LATTICE_NODE_SEED_REGISTRY.yaml  (T64)         │
  │  scripts/lattice_riemann_s_calculator.py (T65)       │
  │  scripts/lattice_metatron_geometry.py  (T66)         │
  │  scripts/lattice_graph_export.py       (T68)         │
  │  scripts/lattice_query_engine.py       (T69)         │
  └──────────────────────────────────────────────────────┘
         │
         ▼
  archive/spec/lattice-hypercube/data/
    LATTICE_NODE_SEED_REGISTRY.yaml / .json
    METATRON_CUBE_GEOMETRY.json
    LATTICE_GRAPH_EXPORT.json
```

---

## Components

### T61 — Node Seeder (`lattice_node_seeder.py`)

Generates **53 representative seed nodes** across the 1728-node hypercube:

| Seed class | Count | Description |
|---|---|---|
| `primary_corner` | 27 | Corners of the AX-01/02/03 primary cube face |
| `riemann_spine` | 12 | Riemann operator spine (AX-09 = 0..11) |
| `metatron_outer` | 12 | Metatron's Cube outer ring |
| `metatron_center` | 1 | Metatron's Cube centre |
| `apex` | 1 | Unified Field Apex — requires Pantheon Council ratification |

Run: `python scripts/lattice_node_seeder.py`

---

### T62 — Coordinate Mapper (`lattice_coordinate_mapper.py`)

Maps a primary 3D address `(AX-01, AX-02, AX-03)` to the full **12D coordinate**
using ontology coupling rules from `AXES_12_FORMAL_DEFINITIONS.yaml`.

Key coupling rules:
- **AX-01 ↔ AX-06** (Frequency ↔ Color): `ax06 = ax01`
- **AX-02 ↔ AX-10** (MatterState ↔ Temporal): `ax10 = ax02`
- **AX-04 ↔ AX-05** (Spin ↔ Acoustic): `ax05 = ax04`
- **AX-07 ↔ AX-12** (Neuromorphic ↔ Information): `ax12 = ax07`

```python
from scripts.lattice_coordinate_mapper import CoordinateMapper
mapper = CoordinateMapper()
coord = mapper.map(3, 7, 2)  # → full LatticeCoordinate(ax01=3, ax02=7, ax03=2, ...)
```

---

### T63 — Cross-Axis Bridge (`lattice_cross_axis_bridge.py`)

Computes **coupling strengths** between any pair of axes.

The Riemann operator (AX-09) is the universal coupling hub — it connects to
all 11 other axes with a coupling type and normalized strength in [0, 1].

```python
from scripts.lattice_cross_axis_bridge import CrossAxisBridge
bridge = CrossAxisBridge()
result = bridge.coupling("AX-01", "AX-06")
# CouplingResult(axis_a='AX-01', axis_b='AX-06', coupling_type='direct', strength=1.0, is_primary=True)
```

Full 12×12 coupling matrix: `bridge.full_coupling_matrix()`

---

### T64 — Seed Registry (`LATTICE_NODE_SEED_REGISTRY.yaml`)

YAML + JSON registry of all 53 seed nodes, written by the seeder script.  
Located at: `archive/spec/lattice-hypercube/data/LATTICE_NODE_SEED_REGISTRY.yaml`

---

### T65 — Riemann S-Calculator (`lattice_riemann_s_calculator.py`)

Numerical approximation of **ζ(s)** at the 12 critical line sample points
`s = 0.5 + i·t` where `t` corresponds to the 12 known non-trivial zeros.

These are the "spine" values of the universal Riemann S-operator —
the transform that couples all 12 axes of the Rainbow Yin Yang Lattice.

```python
from scripts.lattice_riemann_s_calculator import RiemannSOperator
op = RiemannSOperator()
samples = op.compute_samples()  # list of 12 RiemannSample objects
coupling = op.apply_to_axis_pair(3, 3, riemann_index=5)
```

---

### T66 — Metatron's Cube Geometry (`lattice_metatron_geometry.py`)

Generates the sacred geometry of Metatron's Cube for the 12-axis lattice:

- **13 nodes**: 1 APEX (centre) + 6 inner ring (AX-01..06) + 6 outer ring (AX-07..12)
- **78 edges**: complete graph connecting all 13 nodes
- Inner ring radius: 1.0 (hexagonal, 60° spacing)
- Outer ring radius: 2.0 (hexagonal, 30° offset)
- Written to: `archive/spec/lattice-hypercube/data/METATRON_CUBE_GEOMETRY.json`

```python
from scripts.lattice_metatron_geometry import MetatronGeometry
geo = MetatronGeometry()
data = geo.export_json()  # JSON-serializable dict
```

---

### T68 — Graph Export (`lattice_graph_export.py`)

Exports the full lattice data as **JSON-LD** compatible with the
existing KG adjacency matrix format (`docs/generated/KG_ADJACENCY_MATRIX.json`).

Output: `archive/spec/lattice-hypercube/data/LATTICE_GRAPH_EXPORT.json`

```
53 nodes + 144 edges (coupling + Metatron geometry)
```

Run: `python scripts/lattice_graph_export.py`

---

### T69 — Query Engine (`lattice_query_engine.py`)

Hypercube traversal and query interface implementing patterns from
[`docs/KG_SEARCH_QUERY_SPEC.md`](./KG_SEARCH_QUERY_SPEC.md):

| Method | Description |
|---|---|
| `by_address(i, j, k)` | Exact 3D address lookup |
| `neighbors(i, j, k, radius)` | Manhattan-distance neighborhood |
| `by_axis_value(axis_id, value)` | All nodes where axis = value |
| `riemann_spine()` | 12 Riemann operator spine nodes |
| `metatron_anchors()` | 13 Metatron's Cube anchor nodes |
| `path(start, end)` | Shortest path between two addresses |
| `by_coupling_strength(a, b, min)` | High-coupling axis pair nodes |

```python
from scripts.lattice_query_engine import LatticeQueryEngine
engine = LatticeQueryEngine()
result = engine.by_address(5, 5, 5)       # Metatron centre
spine = engine.riemann_spine()            # 12 Riemann nodes
path = engine.path((0,0,0), (11,11,11))  # path to Apex corner
```

---

## Data Files

All generated data lives in `archive/spec/lattice-hypercube/data/`:

| File | Description |
|---|---|
| `LATTICE_NODE_SEED_REGISTRY.yaml` | 53 seed node instances (YAML) |
| `LATTICE_NODE_SEED_REGISTRY.json` | Same, JSON format |
| `METATRON_CUBE_GEOMETRY.json` | 13-node / 78-edge Metatron's Cube |
| `LATTICE_GRAPH_EXPORT.json` | Full JSON-LD graph (53 nodes, 144 edges) |

---

## Testing

Wave 6 test suite: `tests/test_hypercube_data_fabric.py`

```bash
python -m pytest tests/test_hypercube_data_fabric.py -v
```

All 78 tests should pass. Combined with Wave 5 (116 tests), total test suite
covers all ontology + data fabric artifacts.

---

## Governance

All Wave 6 artifacts are **non-canonical candidates**.  
Pantheon Council ratification required before promotion.  
The Unified Field Apex node (`N-APEX`) additionally requires explicit
@atlaslattice human adjudication.

---

## Links

- Ontology layer: [`archive/spec/lattice-hypercube/ontology/`](../archive/spec/lattice-hypercube/ontology/)
- Data layer: [`archive/spec/lattice-hypercube/data/`](../archive/spec/lattice-hypercube/data/)
- Wave 5 taskboard: [`projects/aetherforge-wave5-hypercube-ontology-2026-05-29.md`](../projects/aetherforge-wave5-hypercube-ontology-2026-05-29.md)
- Wave 6 taskboard: [`projects/aetherforge-wave6-data-fabric-2026-05-29.md`](../projects/aetherforge-wave6-data-fabric-2026-05-29.md)
- KG Node Index: [`docs/LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md`](./LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md)
- Search Query Spec: [`docs/KG_SEARCH_QUERY_SPEC.md`](./KG_SEARCH_QUERY_SPEC.md)

---
*Generated by TIDELOCKBrain — Wave 6 Data Fabric — Candidate artifact*
