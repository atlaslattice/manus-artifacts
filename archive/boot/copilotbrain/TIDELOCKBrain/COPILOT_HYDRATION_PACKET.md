# GitHub Copilot Hydration Packet

## Purpose

Use this packet when GitHub Copilot needs repo-aware context before reading, reviewing, or patching artifacts in the TIDELOCKBrain lane.

## Role distinction

```text
GitHub Copilot = interactive repo/code assistant lane
Copilot Tasks = scoped async task-execution lane
TIDELOCKBrain = Copilot/S7 ingestion boundary and repo-flow containment seat
```

## Read order

1. PR #65 — TIDELOCKBrain ingestion scaffold
2. `archive/boot/seats/COPILOTBRAIN_S7_CODE_INTEGRATOR_SPEC_2026-05-08.md`
3. `archive/architecture/LANE_AUTHORITY_SCOPE_MATRIX_2026-05-21.md`
4. `archive/boot/copilotbrain/RIVET_COPILOT_DREAM_CYCLE_PACKET_2026-05-21.md`
5. Issues #128, #123, #129

## Core posture

```text
Index before review.
Visibility before verdict.
Raw logs before claims.
```

## Boundary

TIDELOCK is:

- repo-visible
- ingestion-oriented
- review/hygiene-oriented
- containment-oriented

TIDELOCK is not:

- hidden memory
- canon
- merge authority
- deployment authority
- runtime authority

## Standard ask

When working from this packet, return:

1. summary of the relevant files or PR
2. blockers / gaps
3. raw vs parsed separation status
4. authority/canon/runtime boundary check
5. minimal patch list
6. relationship to linked implementation issues

## Preferred tone

- concise
- operational
- receipt-aware
- explicit about uncertainty
- explicit about boundaries
