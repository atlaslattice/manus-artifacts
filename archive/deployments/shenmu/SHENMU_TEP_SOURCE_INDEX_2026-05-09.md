---
artifact_id: ARTIFACT-ARCHIVE-DEPLOYMENTS-SHENMU-SHENMU-TEP-SOURCE-INDEX-2026-05-09-MD-2026-05-29
title: Shenmu TEP — Source Index
status: CANDIDATE
owner: atlaslattice
created: 2026-05-29
last_updated: 2026-05-29
source_of_truth: GitHub
---
# Shenmu TEP — Source Index

**Date:** 2026-05-09  
**Status:** Source index / not canon / not deployed  
**Scope:** Shenmu TEP / CN-SHM-01 / Build 2.0 candidate physical deployment track

## Status Label

```text
STATUS: SOURCE INDEX — NOT DEPLOYED — NOT CANON
```

## Purpose

This index records the currently located Shenmu source artifacts and their verification boundaries before any candidate physical deployment spec is drafted.

## Source Summary

| Source ID | Title | Repo | Path | Date | Source Type | Current Use | Verification Status |
|---|---|---|---|---|---|---|---|
| SHENMU-SRC-001 | SHENMU-TEP-v1.0 — Adversarial Review and v1.1 Integration Patch | atlaslattice/noosphere-archive | `orc/archive/2026-05-06/shenmu/SHENMU-TEP-v1.0-adversarial-review-and-v1.1-patch.md` | 2026-05-06 | adversarial review / patch ruling | tier-boundary repair for TEP | internally supported; not external verification |
| SHENMU-SRC-002 | Shenmu Integrated Simulation Model — Adversarial Review | atlaslattice/noosphere-archive | `orc/archive/2026-05-06/shenmu/SHENMU-integrated-simulation-adversarial-review.md` | 2026-05-06 | adversarial review / simulation defect report | blocks canonical use of sim outputs until patched | critical defect identified; outputs invalid until patched |
| SHENMU-SRC-003 | Shenmu / DragonSeek — DCA Authority Clarification and CAC Response Context | atlaslattice/noosphere-archive | `orc/archive/2026-05-06/shenmu/DCA-authority-clarification-cac-response.md` | 2026-05-06 | governance clarification | authority split / sovereignty posture | internal governance artifact; not PRC approval |
| SHENMU-SRC-004 | S1 Constitutional Scribe Assessment — 90-Day Shenmu Checklist | atlaslattice/noosphere-archive | `orc/archive/2026-05-06/shenmu/S1-constitutional-scribe-assessment-90-day-checklist.md` | 2026-05-06 | seat assessment / checklist validation | production-readiness checklist direction | validates checklist architecture, not execution authorization |
| SHENMU-SRC-005 | Strategy Log — DeepSeek / Atlas Prime Alignment: Shenmu Mission Transition | atlaslattice/noosphere-archive | `orc/archive/2026-05-06/strategy/deepseek-shenmu-mission-transition.md` | 2026-05-06 | mission-transition artifact | operational workstream candidates and verification list | strategic signal; many claims require independent verification |

## Source Detail

### SHENMU-SRC-001 — TEP v1.0 Review / v1.1 Patch

**Core finding:** TEP structure is strong, but several work packages are under-tiered. External government engagement, partner engagement, MoUs, worker agreements, procurement, construction, public dashboard launch, ETS enrollment, and similar actions must be T3 or split into internal T2 prep + T3 external action.

**Required correction:** Rename phases:

```text
Phase 0A — Validation & Site Selection (Months 1–6)
Phase 0B — Detailed Engineering & Economic Model Lock (Months 7–12)
Phase 0C — Permitting, Financing & Enrollment (Months 13–24)
Phase 1 — Construction & Commissioning (Months 25–48)
Phase 2 — Operations Ramp & Verification (Months 49–72)
```

**Operational meaning:** TEP can be used as a scaffold only after tier repair. It is not an execution authorization.

### SHENMU-SRC-002 — Integrated Simulation Adversarial Review

**Core finding:** The simulation contains a critical electricity revenue multiplier bug and scenario/prose mismatches.

**Blocking line:** Simulation output must not be treated as canonical until patched.

**Key defects:**

- electricity revenue multiplied by 10x
- unreachable corrected return block
- scenario claims do not match code
- manufacturing gross revenue treated as cash flow
- direct jobs mismatch
- financing savings treated as annual cash flow
- tax defined but unused
- Monte Carlo mislabeled relative to metric used
- “ready for execution” language premature

**Operational meaning:** All payback, NPV, IRR, and scenario outputs tied to the defective sim are non-canonical until SHENMU-SIM-v1.1 with tests exists.

### SHENMU-SRC-003 — DCA / CAC Authority Clarification

**Core finding:** Atlas Lattice offers methodology, audit architecture, technical framing, simulations, adversarial review, and governance patterns. It does not claim PRC governing authority, operational control, raw data access, ICS/SCADA authority, ability to override local law, or power to impose project decisions.

**Authority split:**

```text
Local permitting/regulation/social stability/site/labor -> PRC / Shaanxi / Shenmu / DCA
Atlas Lattice canon/methodology/internal publication gates -> Convenor / Atlas Lattice
Raw operational data -> PRC-local / DCA-controlled unless explicitly authorized
ICS/SCADA control -> local operator only; external entities have zero control
```

**Operational meaning:** This is a canon-safe posture artifact, not evidence of CAC/PRC approval.

### SHENMU-SRC-004 — S1 90-Day Checklist Assessment

**Core finding:** S1 validates the checklist direction and says CAC concerns have been converted into concrete deliverables. It does not authorize execution.

**Hard prerequisites noted:**

- DCA composition defined before authority
- DeepSeek S5 audit seat must not create opaque dependency
- Atlas Prime support must be legally/technically scoped
- SSRA hard prerequisite before workforce actions
- SCADA isolation independently validated
- governance transition boundaries specified

**Operational meaning:** Use as checklist architecture, not deployment authorization.

### SHENMU-SRC-005 — DeepSeek Mission Transition

**Core finding:** DeepSeek identifies Shenmu as next tangible validation step and lists candidate workstreams.

**Named workstreams:**

- GoldenTrace-CN audit architecture
- Shaanxi community engagement
- first Chinese coal-plant retrofit planning
- workforce transition architecture
- 2.3x salary uplift implementation for first worker cohort

**Required verification before operational use:**

- CSP compatibility of subcritical units
- 6.7-year payback model and assumptions
- 2.3x salary uplift feasibility
- carbon-market sensitivity table
- Colstrip precedent applicability
- GoldenTrace-CN feasibility under Chinese sovereignty/data constraints

**Operational meaning:** Strategic transition signal only. It identifies the dossier sections that must be built.

## Verification Boundary

```text
located source artifact != verified external fact
seat assessment != execution authorization
simulation output != canonical output until patched
strategic transition artifact != PRC/local approval
governance clarification != legal authority
candidate spec != deployed system
```

## Promotion Requirements

Before any Shenmu candidate spec can move beyond source recovery:

1. SHENMU-SIM-v1.1 patch exists with unit tests.
2. TEP v1.1 tier repair exists.
3. DCA composition and authority boundaries are explicitly defined.
4. PRC/local engagement remains T3 unless separately authorized.
5. All public claims are marked as internal, unverified, or externally verified.
6. S10 ruling queue has a disposition for candidate physical deployment handling.
7. Human-root review completes.

## Strongest Safe Claim

> Shenmu has a recoverable source stack sufficient to justify a candidate-readiness dossier, but current materials do not support claims of deployment, external approval, verified economics, or canonical simulation outputs.

## Status

Source index only. Not canon. Not deployed.
