---
artifact_id: PARALLAXBRAIN-HABITAT-INDEX-v1.0
title: "ParallaxBrain Habitat Index"
version: "1.0"
date: 2026-05-24
seat: ParallaxBrain / GeminiBrain S4
status: candidate_index
canon_status: not_canon
deployment_status: not_deployable
authority_scope: none
runtime_status: not_implemented
native_memory_claim: false
purpose: Index file for GeminiBrain S4 structural review anchors.
related_configuration: archive/boot/geminibrain/ParallaxBrain/PARALLAXBRAIN_REVIEW_CONFIGURATION_v1_0.md
mutation_rule: >
  No claim mutation without new receipts. No canon promotion without human-root ratification.
  This index organizes review lanes only; it does not create runtime state or authority.
---

# ParallaxBrain Habitat Index v1.0

```text
STATUS: CANDIDATE INDEX — NOT CANON
DEPLOYMENT: no
AUTHORITY: none
RUNTIME: not implemented
NATIVE MEMORY CLAIM: false
```

## Purpose

ParallaxBrain is a GeminiBrain S4 review lane for structural analysis, engineering simulation review, interface checks, anomaly tracking, and large-source review preparation.

## Core Lanes

```text
GeminiBrain = S4 engineering / simulation lane
ForgeBrain = build / forge sub-lane
ParallaxBrain = structural review / habitat index lane
```

## Current Configuration

```text
Selected habitat name: ParallaxBrain Metatron Cube
Primary role order:
1. structural auditor
2. anomaly ledger cartographer
3. engineering simulation reviewer
4. metatron cube mapper

Work unit: chunked_by_artifact
First source target: massive_parallax_thread_raw
```

Configuration file:

```text
archive/boot/geminibrain/ParallaxBrain/PARALLAXBRAIN_REVIEW_CONFIGURATION_v1_0.md
```

## Habitat Lanes

```text
raw/              = source material or source receipts
parsed/           = derived views and summaries
claims/           = claim tables, design choices, and labels
review/           = review packets and next-safe-action notes
anchors/          = pinned boot and source anchors
anomaly_ledger/   = drift/anomaly tracking references
source_receipts/  = source hashes, timestamps, and receipt notes
blocker_tables/   = blockers, gaps, and overclaim gates
```

## Pinned Anchors

```text
archive/boot/seats/GEMINIBRAIN_S4_ENGINEERING_SIMULATION_SPEC_2026-05-08.md
archive/boot/geminibrain/GEMINIBRAIN0_ATLAS_PRIME_BOOT_LOG_2026-05-15.md
archive/boot/geminibrain/EPHEMERIS_ATLAS_PRIME_RATIFICATION_LOG_2026-05-15.md
archive/boot/GeminiBrain/ForgeBrain/AGENT_DNA.yaml
archive/boot/gptbrain/adapters/tucker_gemini/README.md
archive/boot/gptbrain/adapters/tucker_gemini/TUCKER_GEMINI_RUNTIME_ADAPTER_SPEC_2026-05-09.md
archive/boot/gptbrain/adapters/tucker_gemini/tucker_gemini_adapter.py
archive/boot/gptbrain/adapters/tucker_gemini/TUCKER_GEMINI_DEPLOYMENT_INSPECTION_CHECKLIST_2026-05-09.md
archive/operations/GEMINI_INTERFACE_SWARM_ANOMALY_LEDGER_PROTOCOL_2026-05-22.md
archive/operations/GEMINI_THREAD_REPLAY_MULTI_RESPONSE_ANOMALY_NOTE_2026-05-22.md
codebases/uws/UWS_GEMINI_SYNTHESIS.md
codebases/aluminum-os/Gemini_Aluminum_OS_Intelligence_Analysis.md
codebases/other/geminiService.ts
archive/gangaseek/governance/GS_GOVERNANCE_INTERFACE_MASTER_v1_0_0_GEMINI_CANDIDATE_RECEIPT_2026-05-22.md
archive/gangaseek/governance/GS_GOVERNANCE_INTERFACE_MASTER_v1_1_0_GEMINI_CANDIDATE_RECEIPT_2026-05-22.md
```

## Required Review Fields

```text
raw_export_status
source_thread_label
thread_time_range
source_refs
sha256_if_available
section_summary
claims_extracted
design_choices
creative_overlay
contradictions_or_uncertainties
overclaims_to_avoid
strongest_safe_claim
next_safe_action
schema_alignment_status
review_hold_flag
```

## Epistemic Labels

```text
VERIFIABLE
DESIGN_CHOICE
SIMULATION_ONLY
CREATIVE_OVERLAY
NOT_VERIFIED
NEEDS_SOURCE
BLOCKED
INFORMATIONAL
```

## Overclaim Gates

```text
adapter_code_does_not_equal_deployment
boot_log_does_not_equal_authority
ratification_filename_does_not_equal_canon
memory_palace_does_not_equal_native_memory
synthesis_does_not_equal_validation
candidate_receipt_does_not_equal_approval
simulation_data_does_not_equal_aerospace_contract
citizen_dividend_does_not_equal_fiscal_entitlement
```

## Review Procedure

```text
1. Preserve source material.
2. Record source references.
3. Separate source text from extracted notes.
4. Label facts, inferences, design choices, and unresolved questions.
5. Preserve blockers and next safe action.
6. Keep all status labels visible.
7. Parsed views may not replace raw source material.
```

## Keeper

```text
Parallax maps the structure.
GeminiBrain simulates and hardens.
ForgeBrain shapes the build.
Raw enters first.
Parsed views derive.
Claims get labels.
Review catches drift.
Human-root decides what stands.
```