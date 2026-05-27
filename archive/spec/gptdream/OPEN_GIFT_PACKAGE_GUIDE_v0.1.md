# GPTDream++ Open Gift Package Guide v0.1

> **Status:** CANDIDATE
> **Artifact Type:** guide
> **Stable ID:** AL-GP-001
> **Date:** 2026-05-27

## Objective

Package GPTDream++ as a public open-source gift with clear industry adoption pathways while preserving canon governance boundaries.

## Package Contents

1. **Core spec and appendices**
   - `archive/spec/gptdream/`
2. **Schemas**
   - `schemas/atlas_orcs/v0_1/`
   - `schemas/o_ai/v0_1/`
   - `schemas/native_thread/v0_1/`
3. **Reference implementations**
   - `reference_impl/atlas_orcs/`
   - `reference_impl/execution_gate/`
   - `reference_impl/native_thread/`
4. **Validation evidence**
   - `tests/adversarial/`
   - `archive/spec/gptdream/VAULT_MANIFEST_2026-05-26.md`

## Adoption Pathways

- **Researchers:** consume specs + appendices first.
- **Platform teams:** implement schema validation + execution gates.
- **Agent builders:** fork reference implementations and run compatibility tests.
- **Governance teams:** apply canon boundary and trust state controls before deployment.

## Governance Boundary

- Open-source distribution is permitted for candidate artifacts.
- Canon claims require ratification and adjudication gates.
- Website publication is a canon surface only when explicitly ratified.

## Starter Path

1. Read `README.md` in this folder.
2. Review `VAULT_MANIFEST_2026-05-26.md`.
3. Run relevant tests in `tests/` and `archive/boot/gptbrain/reference_impl/`.
4. Adopt schema + reference impl incrementally under local governance.
