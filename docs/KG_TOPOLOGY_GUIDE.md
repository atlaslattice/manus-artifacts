# KG Topology Guide
Status: Candidate
Date: 2026-05-28

Guide for the Metatron-oriented lattice topology, ring layout, and traversal rules.

## Ring structure

- Ring 1: Entry surfaces (README, START_HERE, ROADMAP)
- Ring 2: Program execution (taskboards, questboards, weekly digests)
- Ring 3: Governance control (canon, risk, retention, adjudication)
- Ring 4: Validation and trust gates (tests, quality, provenance)
- Ring 5: Protocol + memory surfaces (GPTDream++, schemas, TIDELOCK artifacts)

## Traversal rules

1. Every new node should define at least one outbound typed edge.
2. Every high-value node should receive at least one inbound edge.
3. Sensitive governance claims must include Source/Citations/Evidence markers.
4. Bidirectional audit is required before claiming ring-complete integrity.

## Required quality checks

- `python scripts/check_graph_link_integrity.py`
- `python scripts/validate_lattice_quality_gates.py`
- `python scripts/kg_bidirectional_audit.py`
- `python scripts/kg_dangling_ref_detector.py`

## Related

- [PUBLIC_ARCHIVE_MAP_v2.md](./PUBLIC_ARCHIVE_MAP_v2.md)
- [KG_DOMAIN_SUBGRAPHS.md](./KG_DOMAIN_SUBGRAPHS.md)
