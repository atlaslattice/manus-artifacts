---
artifact_id: ARTIFACT-ARCHIVE-SPEC-ATLASBRAIN-ATLASBRAIN-EVIDENCE-VAULT-STATUS-V0-1-MD-2026-05-29
title: ATLASBRAIN EVIDENCE VAULT STATUS v0.1
status: CANDIDATE
owner: atlaslattice
created: 2026-05-29
last_updated: 2026-05-29
source_of_truth: GitHub
---
# ATLASBRAIN EVIDENCE VAULT STATUS v0.1

STATUS: CANDIDATE — NOT CANON  
DEPLOYMENT: NO  
AUTHORITY: NONE

## Source gravity
- PR #137: Atlas Prime raw/parsed ingestion packet lane.
- PR #179: Evidence Vault schema/guardrail lane.

## Verification
- Raw export pointer preserved at:
  - `/tmp/workspace/atlaslattice/manus-artifacts/archive/boot/atlasbrain/raw_exports/ATLAS_PRIME_SELECT_ALL_RAW_2026-05-23.txt`
- Parsed packet preserved and explicitly derivative at:
  - `/tmp/workspace/atlaslattice/manus-artifacts/archive/boot/atlasbrain/parsed_packets/ATLAS_PRIME_NATIVE_THREAD_INGESTION_PACKET_2026-05-23.md`

## Guardrails implemented
- Parsed packet artifacts require `derived_from_raw: true`.
- Benchmark publication requires raw hash + evidence packet IDs + approved review.
- Public claims remain quarantined until source completeness is `complete` with evidence and approved review.

## Artifacts
- Schemas:
  - `schemas/evidence_vault/v0_1/raw_export.schema.yaml`
  - `schemas/evidence_vault/v0_1/parsed_packet.schema.yaml`
  - `schemas/evidence_vault/v0_1/evidence_packet.schema.yaml`
  - `schemas/evidence_vault/v0_1/benchmark_claim.schema.yaml`
  - `schemas/evidence_vault/v0_1/public_claim.schema.yaml`
- Validator:
  - `reference_impl/atlas_orcs/evidence_vault.py`
- Tests:
  - `tests/test_evidence_vault_validator.py`
  - `tests/test_evidence_vault_schema_guards.py`

## Non-claim boundary
This status artifact is implementation status only.
It is not canon ratification.
It is not deployment approval.
