# Contributing

Thanks for your interest in contributing to manus-artifacts.

## Before you start

This repository is the durable canonical substrate for the Atlas Lattice / GPTBrain system.
Read the canonical substrate rule first:

> GitHub is the canonical record. Drive and Notion are relay/working-vault layers only.

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

## Questions

Open an issue.
