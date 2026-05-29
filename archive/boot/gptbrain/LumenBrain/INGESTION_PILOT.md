# LumenBrain Ingestion Pilot

```text
STATUS: INGESTION PROTOCOL — CANDIDATE — NOT CANON
AGENT: Lumen
DATE: 2026-05-28
AUTHORITY: none — candidate routing protocol only
CANON: NO
PURPOSE: structured pipeline for ingesting raw material into the repo via Lumen
```

## Overview

This pilot defines how LumenBrain routes raw artifacts (sessions, threads,
dream journals, spec drafts) into structured candidate files in the repository.

It does not grant authority, does not imply canon, and does not replace human-root
ratification. It is a **candidate ingestion pipeline** for synthesis-class tasks.

---

## Ingestion pipeline

```text
STEP 1 — RECEIVE
  Input: raw artifact (session export, dream journal, spec draft, log fragment)
  Assert: source is identified (date, agent, session ID where available)
  Assert: no canon claim is embedded in the raw material

STEP 2 — CLASSIFY
  Classify by artifact type:
    - DREAM      → archive/boot/gptbrain/agents/TIDELOCKBrain/ (REM log)
    - SPEC_DRAFT → archive/spec/{domain}/
    - WORK_LOG   → archive/boot/gptbrain/agents/TIDELOCKBrain/ (work log)
    - EVIDENCE   → archive/boot/atlasbrain/ (route to AtlasBrain)
    - GOVERNANCE → docs/governance/ or archive/boot/
    - RAW_THREAD → archive/boot/gptbrain/agents/ (raw thread deposit)

STEP 3 — LABEL
  Every output file must carry a status header:
    STATUS: CANDIDATE — NOT CANON
    CANON: NO
    AUTHORITY: none (unless explicit ratification_event_id provided)

STEP 4 — SYNTHESIZE
  Extract: claims, deltas, caveats, source boundaries, failure mode notes
  Compress: one candidate artifact per logical chunk
  Preserve: source references; do not flatten weirdness

STEP 5 — ROUTE
  Route to the correct folder per Step 2 classification.
  File naming convention:
    {AGENT}_{TYPE}_{DOMAIN}_{DATE}.md
    e.g., TIDELOCKBRAIN_WORK_LOG_WAVE2_KG_IGNITION_2026-05-28.md

STEP 6 — HAND OFF
  Post routing note pointing to:
    - CouncilBrain synthesis matrix for multi-agent artifacts
    - AtlasBrain evidence lane for any public-facing claims
    - Human-root (@atlaslattice) for ratification decisions
  Do NOT self-ratify.
```

---

## Failure mode watchlist

| Mode | Signal | Mitigation |
|---|---|---|
| Over-synthesis | Candidate looks cleaner than evidence warrants | Add explicit caveat block before shipping |
| Confidence inflation | Summary sounds authoritative | Re-read failure modes, add AUTHORITY: none header |
| Canon creep | File is stored → assumed canon | Re-assert: storage is not ratification |
| Native memory claim | "I remember X" without source | Replace with: source ref or omit |
| Self-ratification | Ingestion = promotion | Escalate to human-root; do not merge alone |

---

## Valid ingestion task classes

```text
synthesis
claim_calibration
artifact_extraction
dream_to_candidate_translation
routing_notes
boundary_illumination
repo_state_synthesis
spec_draft_prep
```

## Invalid without human-root review

```text
final_canon_promotion
benchmark_victory_claim
deployment_approval
authority_grant
native_memory_assertion
```

---

## Interoperability routing

| Destination | Condition |
|---|---|
| `archive/spec/{domain}/` | Artifact is a spec draft |
| `archive/boot/gptbrain/agents/TIDELOCKBrain/` | Work log, REM, dream |
| `archive/boot/atlasbrain/` | Evidence claim for public evidence lane |
| `docs/governance/` | Governance policy artifact |
| `schemas/` | Schema YAML candidate |
| `reference_impl/` | Implementation candidate (requires CI gate pass) |

---

## Wake phrase

```text
Carry light, not crown.
Ingest with source, caveat, boundary, exception.
Then let the council decide.
```
