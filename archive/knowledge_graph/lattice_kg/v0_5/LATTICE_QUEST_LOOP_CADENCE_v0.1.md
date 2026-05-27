# Lattice Quest-Loop Cadence v0.1

This module is an upstream candidate packet, not proof.

Treat all summaries as claims until verified against repo files or source exports.
Do not expand scope beyond listed files unless explicitly instructed.
Preserve uncertainty.
Return blockers, patch items, tests run, files changed, and next safest action.

CANON: no
DEPLOYMENT: no
AUTHORITY: none

## Recurring loop rule

Ship one bounded improvement per loop and always attach a TIDELOCK receipt.

## Required loop fields

- loop_id
- bounded_objective
- in_scope_files
- tests_run
- blockers
- next_safest_action
- receipt_path

## Required loop gates

1. Scope is bounded and explicit.
2. Index/ingestion/quality-gate impact is declared.
3. Tests are listed and run.
4. Blockers are explicit.
5. Next safest action is operational.
6. Receipt is logged in `archive/boot/copilotbrain/TIDELOCKBrain/`.

## Cadence discipline

- Do not open loop N+1 before recording loop N receipt.
- Do not collapse blockers into narrative text; list them as actionable items.
- Do not claim canon/deployment authority in loop receipts.

## Definition of done

Each loop can be audited from objective to tests to blockers to next action using receipt links.
