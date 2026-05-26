# Contributing to Atlas Lattice / Manus Artifacts

Thank you for your interest in contributing. This repository is the **canonical public archive** of Atlas Lattice Foundation research, governance artifacts, and system specifications. All contributions are welcome and held to a world-class standard.

---

## Canon Boundaries

> **Nothing is canon until ratified by the full council and adjudicated by @atlaslattice.** All artifacts in this repository are candidates until explicitly marked `(Canonical)`.

- Do **not** edit files marked `(Canonical)` without opening an issue first.
- New artifacts should be submitted as candidates with status clearly marked in their header.

---

## How to Contribute

### Reporting Bugs or Issues
Use the [Issue Tracker](../../issues) with the appropriate template:
- 🐛 **Bug Report** — Something is broken or incorrect
- ✨ **Feature Request** — An improvement or new capability
- 📜 **Artifact Proposal** — Proposing a new artifact for archive consideration

### Submitting Changes

1. **Fork** the repository and create a branch: `feat/your-description` or `fix/your-description`
2. Make your changes following the style of existing documents
3. Open a Pull Request using the provided template
4. A maintainer will review within 7 days

### Branch Naming Conventions

| Prefix | Use |
|--------|-----|
| `feat/` | New artifacts, documents, or capabilities |
| `fix/` | Corrections to existing content |
| `chore/` | Maintenance, CI, tooling |
| `archive/` | Moving or reorganizing existing artifacts |

### Commit Conventions

Use present-tense imperative: `Add X`, `Fix Y`, `Update Z`

---

## Local Validation (GPTBrain Checks)

For contributors working with the `archive/boot/gptbrain/` layer:

```bash
# Install dependencies
pip install pytest ruff

# Lint + format check
ruff check archive/boot/gptbrain/reference_impl/
ruff format --check archive/boot/gptbrain/reference_impl/

# Run pytest suite
python -m pytest archive/boot/gptbrain/reference_impl/ -q

# Run full check harness
bash archive/boot/gptbrain/reference_impl/run_checks.sh
```

---

## Style Guidelines

- Use Markdown for all documents
- Follow existing heading and metadata conventions in the file you're editing
- Keep headings clear and scannable for public audiences
- Add a `status:` marker (candidate / canonical / deprecated) in document headers when relevant

---

## Code of Conduct

All contributors are expected to follow the [Code of Conduct](../CODE_OF_CONDUCT.md). Be excellent to each other.
