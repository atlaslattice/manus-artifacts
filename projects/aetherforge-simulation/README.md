# Aetherforge Simulation Sandbox

This subtree is a **non-canon, open-source simulation sandbox** for making the repository easier to test, validate, and extend without changing canon documents or making deployment/authority claims.

## Scope

- Functional simulation infrastructure only.
- No canon adjustments.
- No deployment claims.
- No authority claims.
- Deterministic local execution by default.
- Zero runtime dependencies beyond Python 3.10+.

## Quickstart

```bash
cd projects/aetherforge-simulation
python -m aetherforge_sim validate
python -m aetherforge_sim matrix
python -m aetherforge_sim --json simulate --steps 12 --seed 144
```

## What is included

- `task-matrix-12x12.json` — balanced 144-task matrix.
- `aetherforge_sim.py` — deterministic simulator, validator, and CLI.
- `tests/test_aetherforge_sim.py` — pytest coverage for matrix shape, determinism, receipts, and CLI behavior.
- `LICENSE.md` — permissive license notice for this simulation subtree.

## Quality bar

A change is considered useful here only when it improves at least one of these: reproducibility, validation, documentation, simulation behavior, safety boundaries, test coverage, or contributor usability.
