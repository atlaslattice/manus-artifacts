# Curation Loops

> **Status:** CANDIDATE  
> **Artifact Type:** operations guide  
> **Date:** 2026-05-28  
> **Related:** [Questboard](./questboard-2026-05-28.md), [Playable Curation Loop](./playable-curation-loop-v0.1.md), [Validation Receipt Format](../validation-receipt-format-v0.1.md)

## Daily Loop (15 minutes)

<!-- METADATA
stable_id: AL-AF-105
lifecycle_state: CANDIDATE
owner: @atlaslattice
date_created: 2026-05-28
canon_status: candidate
-->

1. **Validate health** — check archive health, active blockers, and whether any validator receipt is stale.
2. **Pick one quest** — choose the highest-leverage open quest from the questboard.
3. **Emit receipt** — log what changed, what validation ran, and what remains open.

## Weekly Loop (2 hours)

1. Run the full existing validation stack relevant to curation work.
2. Refresh the questboard based on benchmark, metadata, evidence, and domain-readme gaps.
3. Audit the evidence ledger for missing entries tied to flagship candidate artifacts.
4. Queue ratification packets whose blockers are now cleared.

## Monthly Loop

1. Update the benchmark scorecard and launch-gap narrative.
2. Perform a migration pass against the intake backlog and IP tracker.
3. Review the ratification candidate queue and advance the cleanest packets.
4. Retire or rewrite stale quests so the board stays grounded in real repo needs.
