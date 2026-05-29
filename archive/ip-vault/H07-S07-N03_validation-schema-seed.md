---
hsn: H07-S07-N03
title: Validation Schema Seed
author: David Sheldon (@atlaslattice)
date: 2026-05-29
review_state: seed
license: MIT
canon: "no"
source_boundary: "Seed schema for validation frameworks. Not a deployed validator."
---

# Validation Schema Seed

STATUS: SEED — NOT CANON

## Existing validation

- GPTDream++ adversarial tests: `tests/adversarial/` (T01–T12, 63 tests passing)
- Lattice KG quality gates: `python scripts/validate_lattice_quality_gates.py`
- GPTBrain reference checks: `archive/boot/gptbrain/reference_impl/run_checks.sh`

## Candidate additions

- Provenance header validator
- H-S-N coordinate linter
- Review-state transition validator
