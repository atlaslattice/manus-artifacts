# Scripts

*Atlas Lattice Foundation · Automation & Validation Tools*

This directory contains automation scripts for repository maintenance, validation, and knowledge graph operations.

---

## Scripts

| Script | Purpose |
|--------|---------|
| `build_lattice_global_index.py` | Builds the Lattice global knowledge graph index from seed data |
| `validate_lattice_quality_gates.py` | Validates lattice route and positron review integrity |
| `validate_artifact_metadata.py` | Validates artifact metadata headers across the repository |
| `check_markdown_links.py` | Validates relative markdown links in repository files |
| `check_docs_layout_structure.py` | Checks docs directory layout structure |
| `check_ai_evidence_integrity.py` | Validates AI evidence artifact integrity |
| `kg_query.py` | Knowledge graph query tool |

---

## Running Scripts

All scripts require Python 3.9+. Run from the repository root:

```bash
python scripts/<script-name>.py
```

---

## CI Integration

These scripts are invoked by CI workflows in `.github/workflows/`:
- `lattice-kg-quality-gates.yml` — runs KG validation suite
- `boring-machine-validation.yml` — runs full validation suite

See [Lattice KG Quality Gates workflow](../.github/workflows/lattice-kg-quality-gates.yml) for CI integration details.

---

*Maintained by Atlas Lattice Foundation · MIT License*
