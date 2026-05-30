---
artifact_id: DX-POLICY-ONE-CMD-BOOTSTRAP-001
title: One-Command Bootstrap Guide
status: candidate
created: 2026-05-28
owner: council
tags: [developer-experience, onboarding, setup, bootstrap]
---

# One-Command Bootstrap Guide

> Defines the one-command local development setup for Atlas Lattice contributors.

status: candidate

---

## Goal

Any contributor should be able to clone the repository and run tests with a single command sequence. This guide defines what "one-command bootstrap" means and what it sets up.

---

## Prerequisites

- Python 3.10 or higher
- `git`
- (Optional) Node.js 18+ for web tooling

---

## Bootstrap Command

```bash
git clone https://github.com/atlaslattice/manus-artifacts.git
cd manus-artifacts
make setup   # or: bash scripts/bootstrap.sh
```

The bootstrap script performs:
1. Creates a Python virtual environment (`venv/`)
2. Installs all Python dependencies (`pip install -r requirements.txt`)
3. Runs the full test suite to verify the setup is working
4. Prints a success summary

---

## Bootstrap Script Definition

`scripts/bootstrap.sh` (planned implementation):

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "==> Atlas Lattice Bootstrap"

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Verify setup
echo "==> Running test suite..."
python -m pytest -q --tb=short

echo ""
echo "✅ Bootstrap complete. Activate your venv with:"
echo "   source venv/bin/activate"
```

---

## Makefile Targets

`Makefile` (planned) defines common developer commands:

| Target | Command | Description |
|--------|---------|-------------|
| `make setup` | `bash scripts/bootstrap.sh` | Full bootstrap |
| `make test` | `python -m pytest -q` | Run all tests |
| `make lint` | `bash scripts/run_lint.sh` | Run linters |
| `make kg` | `python scripts/build_lattice_global_index.py` | Rebuild KG index |
| `make validate` | `python scripts/validate_lattice_quality_gates.py` | Run quality gates |
| `make clean` | `rm -rf venv/ __pycache__/` | Clean build artifacts |

---

## Verification

After bootstrap, the contributor should see:

```
N passed in X.Xs
✅ Bootstrap complete.
```

If tests fail, the bootstrap script prints the failure and exits with a non-zero code, pointing the contributor to the NEWCOMER_FAQ.md for troubleshooting.

---

*Atlas Lattice Foundation · status: candidate*
