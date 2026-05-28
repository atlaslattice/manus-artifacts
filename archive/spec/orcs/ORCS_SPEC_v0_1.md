# ORCS Spec v0.1

```text
STATUS: SPEC CANDIDATE — NOT CANON
VERSION: v0.1
DATE: 2026-05-28
DOMAIN: atlas_orcs / knowledge_graph
AUTHORITY: none — candidate spec only
CANON: NO
PURPOSE: define the Ordered Route Classification System for the Atlas Lattice KG
```

## 1. What is ORCS?

**ORCS** (Ordered Route Classification System) is the edge-routing substrate of
the Atlas Lattice knowledge graph. It defines:

1. How artifacts (nodes) connect to each other through typed edges (routes).
2. The classification of every route by `route_class`, `domain`, `seat`, and `trust_state`.
3. The seed ledger format (JSONL) used to persist routes in the repository.
4. The governance rules that govern promotion, deprecation, and conflict resolution of routes.

ORCS does not claim authority. ORCS does not canonize artifacts.
ORCS provides routing structure so that humans and agents can navigate the lattice.

---

## 2. Core concepts

### Route

A **route** is a directed edge in the knowledge graph from a `source_path` to a
`target_surface`. Every route carries:

| Field | Type | Description |
|---|---|---|
| `route_id` | string | Unique identifier, format: `KG-ORCS-{YYYY}-{MMDD}-{NNNN}` |
| `domain` | string | Domain affinity (governance, gptbrain, schemas, tests, etc.) |
| `route_class` | string | Class from the Route Class Taxonomy |
| `source_path` | string | Relative path of the source node |
| `target_surface` | string | Relative path or surface label of the target node |
| `seat` | string | Responsible governance seat (S1–S11) |
| `trust_state` | string | One of: `candidate`, `canon`, `quarantine`, `deprecated` |

### Node

A **node** is any repository artifact that participates in the graph:
a file, a directory, a schema, a workflow, a JSONL seed, a markdown doc.

### Trust state

Trust states govern the reliability and authority of a route:

| Trust state | Meaning |
|---|---|
| `candidate` | Route proposed but not ratified |
| `canon` | Route ratified by human-root after council review |
| `quarantine` | Route flagged for review; source may contain sensitive content |
| `deprecated` | Route superseded; kept for historical record |

---

## 3. Seed ledger format

Routes are stored in JSONL files (one JSON object per line).

### File naming convention

```text
archive/knowledge_graph/{SCOPE}_ROUTE_INDEX.seed.jsonl
```

Current seed files:
- `archive/knowledge_graph/ORCS_ROUTE_INDEX.seed.jsonl` — primary ORCS seed ledger
- `archive/knowledge_graph/GRAPH_SEED.jsonl` — broader KG node seed

### Record format

```json
{
  "route_id": "KG-ORCS-2026-0528-0001",
  "domain": "governance",
  "route_class": "COUNCIL_BOOT",
  "source_path": "archive/boot/COUNCIL_BRAIN_INDEX.md",
  "target_surface": "archive/boot/gptbrain/GPTBRAIN_INDEX_OF_INDEXES_2026-05-26.md",
  "seat": "S1",
  "trust_state": "candidate"
}
```

All fields are required. Additional optional fields:

| Optional field | Type | Description |
|---|---|---|
| `ratification_event_id` | string | ID of ratification event if trust_state is canon |
| `deprecated_by` | string | route_id of successor if deprecated |
| `quarantine_reason` | string | Reason string if quarantined |
| `notes` | string | Free-text annotation |

---

## 4. Route ID convention

```text
KG-ORCS-{YYYY}-{MMDD}-{NNNN}

YYYY = 4-digit year
MMDD = 2-digit month + 2-digit day  
NNNN = 4-digit zero-padded sequence number (per-day scope)

Examples:
  KG-ORCS-2026-0528-0001
  KG-ORCS-2026-0528-0042
  KG-ORCS-2026-0601-0001
```

---

## 5. Governance rules

### 5.1 Adding a route

1. Assign a unique `route_id` following the convention above.
2. Set `trust_state: candidate`.
3. Append the record to the appropriate seed JSONL.
4. Reference the route in the artifact it sources from (where practical).
5. Route candidate for council review if it touches governance or evidence lanes.

### 5.2 Promoting a route to canon

1. A human-root ratification event (`ratification_event_id`) must exist.
2. Set `trust_state: canon`.
3. Add `ratification_event_id` field to the record.
4. Log in `CHANGELOG.md` and `archive/knowledge_graph/GRAPH_INDEX.md`.

### 5.3 Deprecating a route

1. Set `trust_state: deprecated`.
2. Add `deprecated_by` pointing to the successor route_id.
3. Do not delete the record (fossil preservation).

### 5.4 Quarantining a route

1. Set `trust_state: quarantine`.
2. Add `quarantine_reason`.
3. Move source artifact to `quarantine/` if required by quarantine policy.
4. Escalate to human-root for resolution.

---

## 6. Seat assignment

Each route is assigned to a governance seat responsible for stewardship:

| Seat | Domain affinity |
|---|---|
| S1 | Governance, canon, council |
| S2 | GPTBrain routing, dream memory |
| S3 | AtlasBrain, evidence lane |
| S4 | Gate control, Krakoa gates |
| S5 | ORCS route substrate |
| S6 | Schemas |
| S7 | Reference implementation, CI/CD |
| S8–S11 | Extended swarm seats (TBD) |

---

## 7. Validation

Routes in the seed ledger are validated by:

- `scripts/build_lattice_global_index.py` — builds full route index
- `scripts/validate_lattice_quality_gates.py` — validates quality gates
- `tests/test_lattice_kg_hypercube_program.py` — hypercube completeness tests

CI gate: `.github/workflows/lattice-kg-quality-gates.yml`

---

## 8. Topology alignment

ORCS routes map to the 13-sphere Metatron's Cube topology:

```text
S00 (Center / README) ←→ all Ring-1 and Ring-2 spheres
Ring 1: S01 Governance · S02 GPTBrain · S03 AtlasBrain · S04 Gates · S05 ORCS
Ring 2: S06 Schemas · S07 Ref Impl · S08 gptdream Tests · S09 Adversarial
         S10 Aetherforge World · S11 Project Lanes · S12 Workflows
```

Every ORCS route is an edge in this graph, connecting spheres per the
Metatron topology in `archive/knowledge_graph/METATRON_CUBE_TOPOLOGY.md`.

---

## 9. Versioning

This is v0.1. Breaking changes require a new version number (`v0_2`, `v1_0`, etc.)
and a deprecation notice for changed fields.

See also:
- `ORCS_ROUTE_CLASS_TAXONOMY_v0_1.md` — complete route class enumeration
- `archive/knowledge_graph/ORCS_ROUTE_INDEX.seed.jsonl` — live route seed
- `schemas/atlas_orcs/v0_1/` — YAML schema contracts
