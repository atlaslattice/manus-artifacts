---
artifact_id: TEST-POLICY-TEST-STRATEGY-001
title: Test Strategy by Domain
status: candidate
created: 2026-05-28
owner: council
tags: [testing, strategy, reliability, quality]
---

# Test Strategy by Domain

> Maps the testing approach for each major domain of the Atlas Lattice repository.

status: candidate

---

## Testing Philosophy

Atlas Lattice is primarily a knowledge archive with associated Python tooling and schemas. Testing therefore spans two surfaces:
1. **Artifact quality testing** — automated checks on the quality and correctness of documentation/governance artifacts
2. **Software testing** — unit, integration, and adversarial tests for schemas, reference implementations, and scripts

---

## Domain 1: Python Reference Implementations

**Location:** `reference_impl/`, `archive/boot/gptbrain/reference_impl/`

| Test type | What it covers | Tool |
|-----------|---------------|------|
| Unit tests | Individual functions in reference impl modules | pytest |
| Compatibility tests | Verify atlas_orcs reference impl against schema spec | pytest |
| Adversarial tests | Edge cases: malformed input, missing fields, injection attempts | pytest (T01–T12) |
| Contract tests | Verify schema parsing produces correct Python objects | pytest |

**Run command:**
```bash
python -m pytest -q tests/ reference_impl/atlas_orcs/tests/ archive/boot/gptbrain/reference_impl/
```

---

## Domain 2: YAML/JSON Schemas

**Location:** `schemas/`

| Test type | What it covers | Tool |
|-----------|---------------|------|
| Schema parsing tests | Schemas are valid JSON Schema draft-07 | pytest (`tests/test_schema_parsing.py`) |
| Example validation | Valid examples pass; invalid examples fail | pytest |
| Packet format tests | OAI and native thread packet examples | pytest (`tests/test_oai_packet_examples.py`, `tests/test_native_thread_packet_examples.py`) |

---

## Domain 3: Documentation/Governance Artifacts

**Location:** `archive/`, `docs/`, `projects/`

| Test type | What it covers | Tool |
|-----------|---------------|------|
| Metadata completeness | Required frontmatter fields present | `scripts/check_docs_layout_structure.py` |
| AI evidence integrity | Evidence artifacts have valid provenance | `scripts/check_ai_evidence_integrity.py` |
| KG quality gates | Orphan nodes, link density, frontmatter coverage | `scripts/validate_lattice_quality_gates.py` |
| Link integrity | Internal links resolve (planned Q3 2026) | `scripts/check_link_integrity.py` |

---

## Domain 4: Knowledge Graph Index

**Location:** `kg/`, `scripts/`

| Test type | What it covers | Tool |
|-----------|---------------|------|
| Index build test | `build_lattice_global_index.py` runs without error | pytest + CI |
| KG hypercube test | Hypercube graph structure integrity | `tests/test_lattice_kg_hypercube_program.py` |
| Quality gate thresholds | Orphan rate, coverage, link density pass | `validate_lattice_quality_gates.py` |

---

## Domain 5: Product Artifacts

**Location:** `archive/product/`

| Test type | What it covers | Tool |
|-----------|---------------|------|
| Receipt habitat tests | Product-level functional tests | `archive/product/receipt_habitat_v0_1/tests/` |

---

## Test Matrix Summary

| Domain | Test count (current) | Coverage target |
|--------|---------------------|----------------|
| Reference implementations | ~30 | > 85% line coverage |
| Schemas | ~20 | All schemas have at least 1 valid + 1 invalid example |
| Adversarial (T01–T12) | 12 | 100% of defined adversarial scenarios |
| Documentation quality | ~10 | 100% of `archive/governance/` files |
| KG index | ~5 | All KG quality gates |
| Product | ~20 | > 80% line coverage |
| **Total** | **~97** | — |

---

*Atlas Lattice Foundation · status: candidate*
