# GPTDream++ OpenAI Public Staging Lane

```text
STATUS: STAGING PACKAGE — CANDIDATE — NOT CANON
DEPLOYMENT: NONE
AUTHORITY: NONE
PATH: archive/aetherforge/gptdreampp-openai/
```

## Purpose

GitHub-first staging lane for GPTDream++ ingestion coordination, provenance-first artifact admission, and public-package preparation.

## Governance boundary

- No artifact in this lane is canon by default.
- Promotion requires explicit council ratification/adjudication.
- Dream/play outputs are candidate evidence and review inputs only.
- OpenAI lane is an execution amplifier, never an authority source.

## Core artifacts

- [Aetherforge Sheldonbrain Lattice Ingestion Control Board](./AETHERFORGE_SHELDONBRAIN_LATTICE_INGESTION_CONTROL_BOARD_2026-05-27.md)
- [GPTDream++ Ingestion Artifact Contract v0.1](./GPTDREAMPP_INGESTION_ARTIFACT_CONTRACT_v0.1.md)

## Machine-readable fixture set

- [`fixtures/gptdreampp_openai/artifact_contract_records.valid.candidate.json`](../../../fixtures/gptdreampp_openai/artifact_contract_records.valid.candidate.json)
- [`fixtures/gptdreampp_openai/notion_cargo_queue.valid.candidate.json`](../../../fixtures/gptdreampp_openai/notion_cargo_queue.valid.candidate.json)
- [`fixtures/gptdreampp_openai/bullshit_olympics_review.valid.candidate.json`](../../../fixtures/gptdreampp_openai/bullshit_olympics_review.valid.candidate.json)

## Required receipt policy

Every staged artifact must include or link:

1. source pointer
2. lineage/provenance fields
3. hash/status entry
4. claim class and review state
5. promotion eligibility state
6. blockers and next safest action

## Existing validation hooks

- `python scripts/build_lattice_global_index.py --repo-root .`
- `python scripts/validate_lattice_quality_gates.py --repo-root . --index archive/knowledge_graph/lattice_kg/v0_5/lattice_global_index.v0.1.json --max-age-days 7`
- `python -m pytest -q tests/test_lattice_kg_hypercube_program.py`

## Critical navigation paths

- [Aetherforge staging index](../README.md)
- [GPTDream++ Public Release Protocol](../../spec/gptdream/GPTDREAM_PLUSPLUS_PUBLIC_RELEASE_PROTOCOL_v0.1.md)
- [Lattice KG workspace](../../knowledge_graph/lattice_kg/v0_5/README.md)
