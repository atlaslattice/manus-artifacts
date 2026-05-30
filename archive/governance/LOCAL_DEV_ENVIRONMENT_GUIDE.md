---
artifact_id: DX-POLICY-LOCAL-DEV-ENV-001
title: Local Development Environment Guide
status: candidate
created: 2026-05-28
owner: council
tags: [developer-experience, local-dev, setup, documentation]
---

# Local Development Environment Guide

> Comprehensive guide to setting up a local development environment for Atlas Lattice contributors.

status: candidate

---

## Quick Start (see also: One-Command Bootstrap Guide)

```bash
git clone https://github.com/atlaslattice/manus-artifacts.git
cd manus-artifacts
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m pytest -q
```

---

## Detailed Setup

### 1. Python Environment

**Recommended version:** Python 3.11 (tested; 3.10+ required)

```bash
# Check your version
python --version

# Create isolated environment
python -m venv venv

# Activate
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate.bat       # Windows CMD
venv\Scripts\Activate.ps1       # Windows PowerShell
```

---

### 2. Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Key dependencies:
- `pytest` — test runner
- `jsonschema` — schema validation
- `pyyaml` — frontmatter parsing
- `requests` — HTTP utilities (planned scripts)

---

### 3. Running Tests

```bash
# All tests
python -m pytest -q

# Specific test file
python -m pytest tests/test_schema_parsing.py -v

# Specific test
python -m pytest tests/test_schema_parsing.py::test_oai_packet -v

# KG quality gates
python scripts/build_lattice_global_index.py
python scripts/validate_lattice_quality_gates.py
```

---

### 4. Running Linters

```bash
# Docs structure check
python scripts/check_docs_layout_structure.py

# AI evidence integrity check
python scripts/check_ai_evidence_integrity.py
```

---

### 5. Rebuilding the KG Index

```bash
python scripts/build_lattice_global_index.py
```

Output: `kg/global_index.json`

---

## Windows Notes

The repository is developed primarily on Linux/macOS CI, but is supported on Windows with the following notes:
- Use PowerShell or Windows Terminal with Git Bash
- File paths in scripts use `/` — these work in Git Bash and PowerShell 7+
- Line endings: the repository uses LF; Git for Windows auto-converts on checkout (`git config --global core.autocrlf input` recommended)

---

## Editor Setup

**Recommended:** VS Code with the following extensions:
- Python (Microsoft)
- Pylance (type checking)
- YAML (Red Hat)
- Markdown All in One

---

## Troubleshooting

| Problem | Solution |
|---------|---------|
| `ModuleNotFoundError` | Activate venv; run `pip install -r requirements.txt` |
| Tests fail on import | Ensure `python -m pytest` not `pytest` (module path matters) |
| `python` not found | Use `python3` on some Linux distributions |
| Permission error on Windows | Run Terminal as Administrator or use `--user` flag for pip |

---

*Atlas Lattice Foundation · status: candidate*
