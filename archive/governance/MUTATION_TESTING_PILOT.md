---
artifact_id: TEST-POLICY-MUTATION-TESTING-PILOT-001
title: Mutation Testing Pilot
status: candidate
created: 2026-05-28
owner: council
tags: [testing, mutation-testing, quality, pilot]
---

# Mutation Testing Pilot

> Defines the scope and approach for a pilot mutation testing initiative to evaluate test suite effectiveness.

status: candidate

---

## What Is Mutation Testing?

**Mutation testing** measures how effective a test suite is at detecting bugs by introducing small artificial code changes ("mutants") and checking whether the tests catch them.

- Each mutant is a version of the code with one small change (e.g., `+` changed to `-`, `==` changed to `!=`)
- If a test fails when run against the mutant, the mutant is **killed** (test suite detected the bug)
- If no test fails, the mutant **survives** (the test suite missed a real bug type)
- **Mutation score** = killed mutants / total mutants × 100%

---

## Pilot Scope

The pilot targets a **single, bounded module** to prove value before wider rollout.

**Pilot target:** `reference_impl/atlas_orcs/`

Rationale: this module has the most complete existing test coverage and is the most critical reference implementation.

---

## Tool: mutmut

```bash
pip install mutmut
cd /path/to/repo
mutmut run --paths-to-mutate reference_impl/atlas_orcs/
mutmut results
mutmut html  # generates html report in html/ directory
```

---

## Pilot Success Criteria

| Metric | Target |
|--------|--------|
| Mutation score | ≥ 70% killed |
| Pilot run time | ≤ 10 minutes |
| Surviving mutants reviewed | 100% (manual review of survivors) |

---

## Pilot Timeline

| Phase | Target date | Description |
|-------|------------|-------------|
| Setup | Q3 2026 | Install mutmut; verify it runs |
| Pilot run | Q3 2026 | First full mutation test of `reference_impl/atlas_orcs/` |
| Results review | Q3 2026 | Triage surviving mutants; identify test gaps |
| Fix phase | Q3-Q4 2026 | Add tests to kill meaningful surviving mutants |
| Re-run | Q4 2026 | Verify mutation score ≥ 70% |
| Expand decision | Q4 2026 | Decide whether to expand to other modules |

---

## Surviving Mutant Triage

Not all surviving mutants represent test gaps. A mutant should be triaged as:
- **Kill** — write a test to detect this mutation
- **Equivalent mutant** — the mutation doesn't change observable behavior (e.g., changing an internal constant that doesn't affect output); no action needed
- **Out of scope** — the code path isn't testable in the current architecture; file a separate issue

---

## Expansion Criteria

Expand mutation testing beyond the pilot if:
1. Pilot mutation score ≥ 70%
2. Pilot run time ≤ 10 minutes
3. No significant CI false positives

Next modules after pilot: `reference_impl/execution_gate/`, `scripts/`

---

*Atlas Lattice Foundation · status: candidate*
