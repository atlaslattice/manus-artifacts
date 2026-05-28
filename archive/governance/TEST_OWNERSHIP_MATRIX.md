---
artifact_id: TEST-POLICY-TEST-OWNERSHIP-MATRIX-001
title: Test Ownership Matrix
status: candidate
created: 2026-05-28
owner: council
tags: [testing, ownership, governance, accountability]
---

# Test Ownership Matrix

> Defines who is responsible for each test domain in the Atlas Lattice repository.

status: candidate

---

## Purpose

Unowned tests decay. This matrix ensures every test suite has a named owner who is responsible for:
- Keeping tests passing
- Adding new tests when new code ships
- Triaging flaky tests
- Reviewing test-related PRs in their domain

---

## Ownership Matrix

| Test domain | Test location | Current owner | Backup owner |
|-------------|--------------|---------------|-------------|
| Schema parsing | `tests/test_schema_parsing.py` | @atlaslattice | TIDELOCK (AI agent) |
| OAI packet tests | `tests/test_oai_packet_examples.py` | @atlaslattice | TIDELOCK |
| Native thread tests | `tests/test_native_thread_packet_examples.py` | @atlaslattice | TIDELOCK |
| Adversarial suite (T01–T12) | `tests/adversarial/` | @atlaslattice | TIDELOCK |
| Atlas/ORCS compatible | `reference_impl/atlas_orcs/tests/test_compatible.py` | @atlaslattice | TIDELOCK |
| GPTBrain schema presence | `archive/boot/gptbrain/reference_impl/test_schema_presence.py` | @atlaslattice | TIDELOCK |
| Receipt habitat | `archive/product/receipt_habitat_v0_1/tests/` | @atlaslattice | — |
| KG hypercube program | `tests/test_lattice_kg_hypercube_program.py` | @atlaslattice | TIDELOCK |
| Docs layout structure | `scripts/check_docs_layout_structure.py` (script test) | @atlaslattice | TIDELOCK |
| AI evidence integrity | `scripts/check_ai_evidence_integrity.py` (script test) | @atlaslattice | TIDELOCK |
| KG quality gates | `scripts/validate_lattice_quality_gates.py` | @atlaslattice | TIDELOCK |

---

## Owner Responsibilities

| Responsibility | Frequency |
|--------------|-----------|
| Review PRs that touch the owned test domain | Per PR |
| Ensure tests pass on main after each wave | Per wave |
| Triage flaky tests in owned domain | Within 2 weeks of detection |
| Add tests for new code in owned domain | Same PR as new code |
| Report coverage for owned domain in quality report | Monthly |

---

## Expanding Ownership

As the council and contributor community grows, test ownership should be distributed:

1. New contributors who own a feature area should be assigned test ownership for that area
2. Ownership transfers are documented in this file via a PR
3. @atlaslattice must approve all ownership changes

---

## AI Agent Test Ownership

AI agents (TIDELOCK and swarm members) serve as backup owners and execute test runs during wave sprints. They:
- Run the full test suite during each wave
- Report test results in TIDELOCKBrain work logs
- Flag failures to @atlaslattice immediately
- Do not make unilateral changes to test coverage thresholds

---

*Atlas Lattice Foundation · status: candidate*
