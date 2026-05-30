---
title: Knowledge Graph Coverage Dashboard
artifact_id: KG-COVERAGE-DASHBOARD-2026-05-29
status: candidate
canon_status: candidate
lifecycle_state: active
ratification_event_id: pending
trust_state: WORK
owner: Atlas Lattice Foundation
last_updated: 2026-05-29
provenance: Created from 7-pillar world-class execution plan (2026-05-29). Tracks node/edge coverage, orphan nodes, and missing links across the 12×12×12 lattice KG.
---

# 📊 Knowledge Graph Coverage Dashboard

*Atlas Lattice Foundation · Target: World-class KG completeness across all 1,728 H-S-N nodes*

---

## Current KG Version

- **Version:** v0.6
- **Location:** `archive/knowledge_graph/lattice_kg/v0_6/`
- **Topology:** 12 Houses × 12 Spheres × 12 Nodes = **1,728 cells** (H-S-N coordinate system)
- **Last validated:** 2026-05-29

---

## Coverage Targets

| Dimension | Current | Target | Status |
|-----------|---------|--------|--------|
| Total nodes defined | TBD (run `build_lattice_global_index.py`) | 1,728 | 🟡 Measure |
| Nodes with frontmatter ID | TBD | 100% | 🟡 Measure |
| Nodes with bidirectional links | TBD | ≥80% | 🟡 Measure |
| Orphan nodes (zero edges) | TBD | 0 | 🟡 Measure |
| Cross-stream links (spec↔code↔tests↔logs) | TBD | ≥60% of nodes | 🟡 Measure |
| Citation blocks present | TBD | ≥90% of spec nodes | 🟡 Measure |
| Missing H-S-N IDs | TBD | 0 | 🟡 Measure |
| Stable artifact_id coverage | TBD | 100% of governed artifacts | 🟡 Measure |

*Run validation scripts to populate actual values. See [Validation Commands](#validation-commands) below.*

---

## Node Coverage by House (H01–H12)

| House | Domain | Nodes Defined | % Coverage | Orphans | Notes |
|-------|--------|--------------|-----------|---------|-------|
| H01 | Governance & Canon | TBD | TBD | TBD | Core governance artifacts |
| H02 | Legal, Privacy, Trust | TBD | TBD | TBD | |
| H03 | Repository Architecture | TBD | TBD | TBD | |
| H04 | Documentation Excellence | TBD | TBD | TBD | |
| H05 | Knowledge Graph Layer | TBD | TBD | TBD | Core KG infra |
| H06 | CI/CD & Automation | TBD | TBD | TBD | |
| H07 | Security & Supply Chain | TBD | TBD | TBD | |
| H08 | Testing & Reliability | TBD | TBD | TBD | |
| H09 | Accessibility & Global Reach | TBD | TBD | TBD | |
| H10 | Developer Experience | TBD | TBD | TBD | |
| H11 | Community & Ecosystem | TBD | TBD | TBD | |
| H12 | Launch & World-Class Ops | TBD | TBD | TBD | |

---

## Edge Coverage (Relation Types)

See `archive/knowledge_graph/lattice_kg/v0_6/CROSSLINK_CONTRACT_v1.0.yaml` for defined relation types.

| Relation Type | Edge Count | % of Nodes with This Edge | Target |
|--------------|-----------|--------------------------|--------|
| `implements` (spec → code) | TBD | TBD | ≥50% |
| `tested_by` (artifact → test) | TBD | TBD | ≥60% |
| `supersedes` (new → old) | TBD | TBD | 100% when applicable |
| `references` (cite → source) | TBD | TBD | ≥90% |
| `depends_on` (task → task) | TBD | TBD | ≥80% of tasks |
| `ratified_by` (artifact → event) | TBD | TBD | 100% for canonical |

---

## Known Gaps (Orphan/Missing)

| Gap | Location | Priority | Issue |
|-----|----------|---------|-------|
| Legacy artifacts without `artifact_id` | Multiple `/archive/` subdirs | P1 | Triage needed |
| Legacy frontmatter using `status:` only | Pre-2026-05-28 docs | P2 | Bulk migration |
| Lattice spec nodes without test links | KG v0.5 → v0.6 delta | P1 | Pending |
| Fork synthesis nodes (missing components) | archive/forks/ | P1 | [FORK_POLICY](../archive/forks/FORK_POLICY.md) |

---

## Validation Commands

```bash
# Build global lattice index (populates coverage data)
python scripts/build_lattice_global_index.py

# Validate quality gates (completeness + integrity)
python scripts/validate_lattice_quality_gates.py

# Validate artifact metadata (frontmatter coverage)
python scripts/validate_artifact_metadata.py

# Check orphan nodes / broken cross-links
python scripts/validate_hypercube_integrity.py

# Run full KG test suite
python -m pytest -q tests/test_lattice_kg_hypercube_program.py
```

---

## Progress History

| Date | Event | Coverage Change |
|------|-------|----------------|
| 2026-05-20 | Lattice 12×12×12 spec published | H-S-N coordinate system established |
| 2026-05-26 | GPTDream++ vault + 63 tests | KG v0.5 test coverage added |
| 2026-05-29 | KG v0.6 unified hypercube | Topology doc + query surface + crosslink contract |
| 2026-05-29 | Dashboard created | Baseline measurement pending |

---

## Cross-References

- [Lattice KG v0.6 README](../archive/knowledge_graph/lattice_kg/v0_6/README.md)
- [Hypercube 12D Topology](../archive/knowledge_graph/lattice_kg/v0_6/HYPERCUBE_12D_TOPOLOGY_v1.0.yaml)
- [Crosslink Contract](../archive/knowledge_graph/lattice_kg/v0_6/CROSSLINK_CONTRACT_v1.0.yaml)
- [Universal Frontmatter Schema](./UNIVERSAL_FRONTMATTER_SCHEMA.md)
- [Archive Index](./ARCHIVE_INDEX.md)

---

*Dashboard updated each session · Status: Candidate · License: MIT*
