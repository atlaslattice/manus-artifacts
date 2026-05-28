# GPTDream++ Public Release Protocol v0.1

```text
STATUS: CANDIDATE PUBLIC RELEASE PROTOCOL — NOT CANON
DEPLOYMENT: NOT DEPLOYABLE
AUTHORITY: NONE
```

## Purpose

Provide a clear, reproducible, open-source release posture for GPTDream++ artifacts while preserving canon boundaries.

## Public-facing clarity rules

- Use operational language for external audiences.
- Keep mythic language as optional framing, never as authority.
- Mark every candidate artifact as non-canon unless explicitly ratified.
- Preserve uncertainty and claims requiring verification.

## Reproducibility rules

Before release updates, run and report:

```text
python -m pytest -q tests
cd /tmp/workspace/atlaslattice/manus-artifacts/archive/boot/gptbrain/reference_impl
python -m pytest -q
bash run_checks.sh
```

## Schema and reference-implementation parity checks

Before candidate release packets are advanced:

- confirm schema lane exists (`schemas/atlas_orcs/v0_1/`, `schemas/o_ai/v0_1/`, `schemas/native_thread/v0_1/`)
- confirm matching reference implementations exist (`reference_impl/atlas_orcs/`, `reference_impl/native_thread/`, `reference_impl/execution_gate/`)
- run lattice quality gates to keep cross-lane retrieval and governance checks intact

## Critical navigation paths

- [Repository root README](../../../README.md)
- [Lattice KG workspace](../../knowledge_graph/lattice_kg/v0_5/README.md)
- [Lattice World-Class Contributor Start Here v0.1](../../knowledge_graph/lattice_kg/v0_5/LATTICE_WORLD_CLASS_CONTRIBUTOR_START_HERE_v0.1.md)
- [Lattice KG Query Cookbook v0.1](../../knowledge_graph/lattice_kg/v0_5/LATTICE_KG_QUERY_COOKBOOK_v0.1.md)
- [GPTDream++ OpenAI Public Staging Lane](../../aetherforge/gptdreampp-openai/README.md)

## Boundary rules

- A protocol draft is not a ratification event.
- A test pass is not canon promotion.
- A publication candidate is not deployment authority.
- Human/root review remains required for authority transitions.

## Open-source gift posture

GPTDream++ should be legible, reproducible, source-grounded, and safe for public learning without false completeness.

## Release checklist

- [ ] Scope declared
- [ ] Boundaries declared
- [ ] Tests run and reported
- [ ] Blockers documented
- [ ] Next safest action documented
- [ ] Handoff packet completed
