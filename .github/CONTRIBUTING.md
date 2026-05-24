# Contributing

Thanks for your interest in contributing to manus-artifacts.

## Before you start

This repository is the durable canonical substrate for the Atlas Lattice / GPTBrain system.
Read the canonical substrate rule first:

> GitHub is the canonical record. Drive and Notion are relay/working-vault layers only.

Then load these operating references:

- [`archive/boot/COUNCIL_BRAIN_INDEX.md`](../archive/boot/COUNCIL_BRAIN_INDEX.md) (CouncilBrain index and seat registry)
- [`archive/boot/councilbrain/COUNCILBRAIN_S2_BOOT_REVIEW_TRAIL_2026-05-09.md`](../archive/boot/councilbrain/COUNCILBRAIN_S2_BOOT_REVIEW_TRAIL_2026-05-09.md) (CouncilBrain S2 review trail)
- [`archive/boot/seats/COPILOTBRAIN_S7_CODE_INTEGRATOR_SPEC_2026-05-08.md`](../archive/boot/seats/COPILOTBRAIN_S7_CODE_INTEGRATOR_SPEC_2026-05-08.md) (CopilotBrain S7)
- [`archive/boot/gptbrain/TIDELOCKBrain/README.md`](../archive/boot/gptbrain/TIDELOCKBrain/README.md) (TIDELOCKBrain pilot)
- [`archive/boot/seats/`](../archive/boot/seats/) (all live seat specs)

## Ground rules

- **Memory is not truth.** Stored artifacts track epistemic status and provenance.
- **Canon promotion requires human-root approval.** No auto-ratification.
- **Contradictions are linked, not silently overwritten.**
- **C0 claims are never externally asserted as fact.**

If you are adding or modifying content in `archive/boot/gptbrain/`, follow the governance
boundaries in [`archive/boot/gptbrain/reference_impl/README.md`](../archive/boot/gptbrain/reference_impl/README.md).

## Development setup

```bash
python -m pip install pytest ruff
```

## Validation

```bash
# Lint
ruff check archive/boot/gptbrain/reference_impl/

# Format check
ruff format --check archive/boot/gptbrain/reference_impl/

# Tests + CLI smoke checks
cd archive/boot/gptbrain/reference_impl
python -m pytest -q
bash run_checks.sh
```

All four commands must pass before submitting a pull request.

## Pull requests

- Keep changes small and focused.
- Reference the relevant issue number in the PR description.
- Do not promote candidate canon to ratified canon without explicit human-root review.
- Keep candidate vs ratified status explicit in docs and PR notes.

## Questions

Open an issue.
