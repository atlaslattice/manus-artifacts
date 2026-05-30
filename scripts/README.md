# Scripts

*Atlas Lattice Foundation · Automation & Validation Tools*

This directory contains automation scripts for repository maintenance, validation, and knowledge graph operations.

---

## Scripts

| Script | Purpose |
|--------|---------|
| `build_lattice_global_index.py` | **Builds the unified Lattice global KG index** (491 nodes, 12 dimensions) |
| `validate_hypercube_integrity.py` | **Runs 12D hypercube integrity gates** (G01–G06: orphans, duplicates, connectivity, schema, coverage, broken links) |
| `validate_lattice_quality_gates.py` | Validates lattice route and positron review integrity |
| `validate_artifact_metadata.py` | Validates artifact metadata headers across the repository |
| `check_markdown_links.py` | Validates relative markdown links in repository files |

---

## 12D Hypercube Pipeline (recommended entry point)

```bash
# 1. Build / refresh the global index
python scripts/build_lattice_global_index.py --report

# 2. Validate all 6 integrity gates
python scripts/validate_hypercube_integrity.py

# 3. Query the lattice
python scripts/build_lattice_global_index.py --query "governance"
```

---

## Running Scripts

All scripts require Python 3.9+. Run from the repository root:

```bash
python scripts/<script-name>.py
```

---

## CI Integration

These scripts are invoked by CI workflows in `.github/workflows/`:
- `hypercube-integrity.yml` — **builds index + runs all 6 integrity gates + tests**
- `lattice-kg-quality-gates.yml` — runs KG validation suite
- `boring-machine-validation.yml` — runs full validation suite

---

*Maintained by Atlas Lattice Foundation · MIT License*

