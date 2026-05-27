# Aetherforge Quest Quality Gate v0.1

This module is an upstream candidate packet, not proof.

Treat all summaries as claims until verified against repo files or source exports.
Do not expand scope beyond listed files unless explicitly instructed.
Preserve uncertainty.
Return blockers, patch items, tests run, files changed, and next safest action.

CANON: no
DEPLOYMENT: no
AUTHORITY: none

## Purpose

Keep Aetherforge playable while enforcing strict technical acceptance gates for every quest.

## Required quest acceptance fields

- quest_id
- mission_lane (`lattice_kg` | `aetherforge_archive` | `gptdream_protocol`)
- in_scope_files
- definition_of_done
- tests_required
- blockers
- next_safest_action
- receipt_path

## Required quest acceptance criteria

1. Candidate boundary is explicit.
2. Claims are source-grounded or marked uncertain.
3. Test commands are listed before execution.
4. Test results are recorded after execution.
5. Blockers are explicit and non-empty when present.
6. Next safest action is operational and bounded.

## Example test command lanes

- `python -m pytest -q tests`
- `cd /tmp/workspace/atlaslattice/manus-artifacts/archive/boot/gptbrain/reference_impl && python -m pytest -q && bash run_checks.sh`

## Rule

Fun framing does not replace acceptance criteria, tests, or receipts.
