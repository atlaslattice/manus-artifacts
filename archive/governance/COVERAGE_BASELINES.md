---
artifact_id: TEST-POLICY-COVERAGE-BASELINES-001
title: Test Coverage Baselines
status: candidate
created: 2026-05-28
owner: council
tags: [testing, coverage, baselines, quality]
---

# Test Coverage Baselines

> Establishes the minimum test coverage targets for each code domain.

status: candidate · baseline_date: 2026-05-28

---

## Coverage Measurement Tool

**Tool:** `pytest-cov`

```bash
python -m pytest --cov=reference_impl --cov=scripts --cov-report=term-missing -q
```

Coverage is measured as **line coverage** (statements executed during test runs).

---

## Coverage Targets by Domain

| Domain | Location | Current (est.) | Target | Enforcement |
|--------|---------|---------------|--------|-------------|
| `reference_impl/atlas_orcs/` | Atlas/ORCS reference impl | ~85% | ≥ 85% | CI gate (planned Q3 2026) |
| `reference_impl/execution_gate/` | Execution gate impl | ~80% | ≥ 80% | CI gate (planned Q3 2026) |
| `reference_impl/native_thread/` | Native thread impl | ~80% | ≥ 80% | CI gate (planned Q3 2026) |
| `archive/boot/gptbrain/reference_impl/` | GPTBrain reference impl | ~75% | ≥ 75% | CI gate (planned) |
| `scripts/` | KG automation scripts | ~60% | ≥ 70% | CI gate (planned Q4 2026) |
| `archive/product/receipt_habitat_v0_1/` | Product tests | ~80% | ≥ 80% | CI gate (planned) |

---

## Excluded from Coverage

The following are excluded from coverage measurement:
- `tests/` directory itself
- Configuration files (`*.yml`, `*.yaml`, `*.json`)
- `__init__.py` files with no logic
- Template and example files

---

## Coverage Baseline Snapshots

### Baseline: 2026-05-28

| Module | Line coverage |
|--------|-------------|
| `reference_impl/atlas_orcs/` | (Run `python -m pytest --cov=reference_impl/atlas_orcs -q` to measure) |
| `scripts/build_lattice_global_index.py` | (Measured via KG quality gate tests) |
| `scripts/validate_lattice_quality_gates.py` | (Measured via KG quality gate tests) |

*Full coverage report will be generated as part of the Q3 2026 coverage sprint.*

---

## Coverage Ratchet Policy

Coverage targets are **ratchets** — they can only increase over time. Once a coverage target is met, it becomes the new floor:
- If a PR causes coverage to drop below the floor, CI warns (soft gate initially)
- Drops of > 5% block the PR (hard gate, Q4 2026)

---

## Golden Test Priority

For domains where 100% coverage is impractical, prioritize coverage of:
1. Happy path through the main entrypoint
2. Error handling branches (invalid input, missing fields)
3. All adversarial test cases (T01–T12)
4. All schema validation paths

---

*Atlas Lattice Foundation · status: candidate*
