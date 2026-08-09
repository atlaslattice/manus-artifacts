---
artifact_id: RECEIPT-HABITAT-SCHEMA-CANDIDATE-v0.3.1-REVIEW-PACKET-2026-05-23
title: "Receipt Habitat Schema v0.3.1 — Candidate Review Packet"
version: "0.1"
date: 2026-05-23
source_artifact: RECEIPT-HABITAT-SCHEMA-CANDIDATE-v0.3.1
source_file: RECEIPT_HABITAT_SCHEMA_CANDIDATE_v0.3.1.txt
source_sha256: a5fe042c1692ac2b0cf1567ce8eca98868586eb2d990a59cbb7e13fc3ca7193a
source_char_count: 33357
source_line_count: 884
layer: review_candidate
status: candidate_review_packet
canon_status: not_canon
deployment_status: not_deployable
authority_scope: none
execution: none
proof_status: not_a_proof
release_class: PRIVATE_REVIEW
mutation_rule: >
  Preserve as candidate review and ingest index. Do not treat as canon,
  deployment, constitutional ratification, or implementation proof. Full source
  body remains in uploaded file context unless separately committed.
---

# Receipt Habitat Schema v0.3.1 — Candidate Review Packet

```text
STATUS: candidate review packet
CANON: no
DEPLOYMENT: no
AUTHORITY: none
EXECUTION: none
PROOF: not_a_proof
SOURCE SHA256: a5fe042c1692ac2b0cf1567ce8eca98868586eb2d990a59cbb7e13fc3ca7193a
```

## 1. Source summary

The uploaded `RECEIPT_HABITAT_SCHEMA_CANDIDATE_v0.3.1.txt` consolidates the Receipt Habitat schema stack through v0.3.1. It claims to consolidate v0.1, v0.2, v0.2.1, v0.2.2, v0.2.3, v0.2.4, epoch ruling 2026-05-23T15:06 CDT, and S5 Parallax booth patches.

The artifact is internally marked:

```text
status: candidate
canon_status: not_canon
deployment_status: not_deployable
authority_scope: none
proof_status: not_a_proof
release_class: PRIVATE_REVIEW
```

## 2. Key Copilot patch compliance observed

The v0.3.1 source appears to address the S4/Copilot PATCH review in several important ways:

```text
- It avoids presenting itself as canon or deployed.
- It frames convenor-approved values as pending D-54 rather than constitutional ratification.
- It changes the mission/product framing toward evidence layer before action.
- It includes Object 14 `record_locked` plus `lock_reason`.
- It surfaces Sprint 2 blocker state directly at Objects 13-15.
- It preserves B-01 FRONTIER-RIGOR-MATRIX as orphan/labeled and Sprint 2 blocked.
- It includes a Sprint 2 integration task for build_state / ExecutionRiskTier enum alignment.
```

## 3. Remaining concerns before ratification workflow

```yaml
remaining_concerns:
  d54_workflow_visibility:
    issue: >
      The header describes D-54 as council ingestion, discussion, vote, and Convenor sign-off.
      If S1 certification, S2 verification, and S3 adversarial review are mandatory pre-vote steps,
      those should be explicit in the D-54 workflow block.
    severity: patch

  source_citation_receipt:
    issue: >
      The source says canonical site was fully ingested in the same session, but the visible
      source packet should include a source_citation receipt with URL and hash/bundle metadata
      where possible.
    severity: patch

  v03_footer_mismatch:
    issue: >
      The document footer still says DOCUMENT: RECEIPT-HABITAT-SCHEMA-CANDIDATE-v0.3,
      while the artifact header is v0.3.1. This should be normalized to v0.3.1.
    severity: patch

  duplicate_epoch_enum:
    issue: >
      The epoch_type enum lists per_model_context_reset twice.
    severity: patch

  safe_to_act_subset_field:
    issue: >
      The file preserves the safe-to-act invariant in Linkage prose but does not obviously
      define a dedicated `safe_to_act_subset` field in ClaimState or SynthesisResult.
      If Copilot's prior required patch is still binding, add this field explicitly.
    severity: patch

  context_hash_field:
    issue: >
      SeatContinuity includes current_instance_id and epoch fields, but the visible source
      does not show an explicit `context_hash` / `context_hash_basis` field. If Grok's
      epoch ratification required this, add it.
    severity: patch

  d54_status_field:
    issue: >
      Consider adding a machine-readable D-54 status enum such as not_submitted,
      s1_certified, s2_verified, s3_adversarial_reviewed, discussion_open, vote_open,
      convenor_signed, rejected.
    severity: suggested_patch
```

## 4. Ratification posture

```yaml
ratification_posture:
  candidate_ready_for_review: true
  block_tier_overclaims_detected: false
  patch_required_before_d54_submission: true
  sprint_0_execution_ready_signal: plausible
  sprint_1_status: implementation_ready_where_not_dependent_on_remaining patches
  sprint_2_status: blocked_on_FRONTIER_RIGOR_MATRIX_or_reanchor
```

## 5. Safe interpretation

```text
v0.3.1 is a high-quality consolidated candidate schema.
It is not canon.
It is not deployed.
It is not constitutional ratification.
It is suitable for review, patching, and D-54 preparation.
```

## 6. Keeper

```text
Consolidation landed as candidate.
Patch before ratification.
Sprint 0 can move.
D-54 needs clean machine-visible status.
Preserve the tape.
```
