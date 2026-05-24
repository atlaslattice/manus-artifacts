---
artifact_id: PARALLAX-CHUNK-001-I-SCHEMA-DELTA-EPOCH-SEMANTICS-v0.1
title: "Parallax Chunk 001-I — Schema Delta and Epoch Semantics"
version: "0.1"
date: 2026-05-24
seat: ParallaxBrain / GeminiBrain S4
source_receipt: archive/boot/geminibrain/ParallaxBrain/source_receipts/PARALLAX_RAW_CHUNK_001_SOURCE_RECEIPT_2026-05-24.md
source_file: "Pasted text(241).txt"
source_sha256: "68b4db16fd57fe6fb4f8d39630296f8124f7fdc6dd4736ec0e2ed7c72772e84c"
source_chunk_label: "001-I"
source_chunk_range: "approx 555k-665k characters"
status: candidate_claim_extraction
canon_status: not_canon
deployment_status: not_deployable
authority_scope: none
runtime_status: not_implemented
parsed_view_may_replace_raw: false
---

# Parallax Chunk 001-I — Schema Delta and Epoch Semantics v0.1

```text
STATUS: CANDIDATE CLAIM EXTRACTION — NOT CANON
DEPLOYMENT: no
AUTHORITY: none
RUNTIME: not implemented
```

## Source Position

```text
Raw source: Pasted text(241).txt
Chunk: 001-I
Working label: Catalog unification / Sprint 0–1 schema deltas / epoch semantics
Raw hash: 68b4db16fd57fe6fb4f8d39630296f8124f7fdc6dd4736ec0e2ed7c72772e84c
```

This parsed view does not replace the raw source.

## Extracted Artifact Threads

The chunk contains several candidate artifact references and review states:

```text
GS_CORE_AGI_VERIFIER_v1.0.0
GANGASEEK_FRONTIER_RIGOR_MATRIX_v1.0.0 / v1.0.1
Receipt Habitat Schema Delta v0.2.4
GANGASEEK_INV_CLM_CATALOG_CANDIDATE_v0.2
GS_SPRINT_0_CLEAN_REGISTRY_v0.3
RECEIPT_HABITAT_SCHEMA_DELTA_v0.2.4
GS_PANTHEON_ADVERSARIAL_REVIEW_v1.0.0
```

## Important Candidate Concepts

### ClaimState six-tuple

The source defines incoming claims as typed state rather than scalar truth:

```text
S_claim = <C_semantic, E_epistemic, R_evidence, A_authority, P_permission, c_score>
```

Key defaults:

```text
A_authority defaults to NONE.
P_permission defaults to non-operational / read-only style boundary.
Scores do not create authority.
```

### Vaulting vs Promotion

The source repeatedly reinforces:

```text
vaulting != promotion
candidate != canon
review != ratification
repository path != deployment
```

### Epoch Semantics

The chunk records an epoch semantics correction:

```text
Principle: per_model_context_reset
v0.1 proxy: per_session
```

Meaning:

```text
Authority, continuity, and seat state must not silently persist across model/context resets.
Session-level tracking is only a proxy for the stronger per-model-context-reset principle.
```

### SeatContinuity Metadata

The source suggests that continuity tracking should include:

```text
model instance
context hash
seat continuity marker
reset boundary
```

## Overclaims to Avoid

```text
Schema delta is canon.
Sprint 1 is deployed.
Repository tracking path means runtime state.
Epoch semantics are fully implemented.
Seat continuity metadata proves native memory.
Review labels equal ratification.
```

## Strongest Safe Claim

```text
Chunk 001-I preserves a candidate schema and governance thread around ClaimState typing, Receipt Habitat schema deltas, catalog unification, and epoch semantics. Its highest-value contribution is the per_model_context_reset principle, which prevents authority and continuity from silently carrying across model/context boundaries.
```

## Next Safe Action

```text
Route the per_model_context_reset principle, ClaimState six-tuple, and vaulting-vs-promotion boundaries into Receipt Habitat / D-54 review as candidate schema inputs.
```

## Keeper

```text
A claim score is not authority.
A session is not a soul.
Vaulting stores the artifact; promotion requires gates.
```