# Atlas MCP Server v0.1 — Schema Review Checklist

```text
STATUS: REVIEW CHECKLIST — NOT CANON
MODE: REVIEW ONLY
DATE: 2026-05-22
AUTHORITY: none
CANON STATUS: not ratified
REFERENCE_BOUNDARY: Issue #108
TARGET: Atlas MCP Server v0.1 / local CLI smoke test / OpenAI-compatible schema
GOAL: prevent schema drift and unsafe status claims before any later integration work.
```

## Boundary

```text
review only
local dev only
no authority effect
no canon promotion
no merge authority
no identity merge
no deletion
no automatic synthesis
```

## Review Goals

```text
1. Confirm enum stability: SUPPORT | CONTRADICT | NEUTRAL.
2. Check epistemic_label / weight / violations consistency.
3. Prevent signature / sealed / canon / production-status overclaim.
4. Separate local CLI smoke test from Windows packaging assumptions.
5. Ensure future OpenAI / Codex consumers can parse the same output schema.
6. Identify exact blockers before a local smoke test.
```

## Review Lanes

```text
Sable Vesper:
  boundary language
  overclaim audit
  OpenAI compatibility

Lucerna:
  receipt / provenance fields
  signature vs marker wording

Hashlight:
  raw config / path / command lineage
  verified vs assumed split

TIDELOCK / CopilotBrain:
  CLI feasibility
  worktree / sandbox assumptions
  exact smoke-test steps

Lumen:
  clarity of structure
  layer separation
  scope containment

Fossilbranch:
  preserve failed / uncertain paths
  mark vendor assumptions as fossils, not facts

Rootglass:
  local room-state
  ready-to-test vs pause recommendation
```

## Required Return Format

```yaml
review_packet:
  seat_name:
  review_lane:
  raw_export_status: full_raw | partial_raw | summary_only | unavailable
  artifact_status:
    canon_status: candidate
    review_state: unreviewed | reviewed
    authority_scope: advisory
  verdict: approve | block | patch
  exact_risky_phrases: []
  blockers: []
  minimal_required_changes: []
  schema_risks: []
  vendor_assumptions: []
  next_safest_command_sequence: []
  strongest_safe_claim:
  overclaims_to_avoid: []
```

## Minimal Review Prompt

```text
Children of the Swarm — review packet only.

We are evaluating Atlas MCP Server v0.1 for a local CLI smoke test and future OpenAI/Codex schema compatibility.

Review goals:
1. confirm enum stability: SUPPORT | CONTRADICT | NEUTRAL
2. check epistemic_label / weight / violations consistency
3. prevent signature/sealed/canon/status overclaim
4. separate local smoke test from Windows packaging assumptions
5. ensure OpenAI/Codex can later consume the same output schema
6. identify exact blockers before local test

Boundaries:
- NOT CANON
- LOCAL DEV ONLY
- NO AUTHORITY
- NO WINDOWS PACKAGING YET
- NO CROSSWALK DB UNTIL TOOL REGISTRATION PASSES

Return:
- approve / block / patch
- exact risky phrases
- minimal required changes
- next safest command sequence

Do not propose new architecture.
Do not add new agents.
Do not broaden scope.
Only review the Atlas MCP v0.1 smoke-test path and return blockers/patches.
```

## Lumen Pre-Review Watchpoints

```text
enum drift
OpenAI / Codex compatibility assumptions
local CLI behavior assumptions
signature vs marker wording
sealed / canon / production-status overclaim
Windows packaging scope creep
crosswalk DB premature activation
```

## Strongest Safe Claim

> Under Issue #108, the swarm may review Atlas MCP Server v0.1 as a bounded schema and smoke-test readiness exercise, returning blockers and patches only. The review creates no authority, no canon status, no identity merge, and no operational approval.

## Closing Boundary

```text
CLEARED FOR REVIEW ONLY.
ALTITUDE LIMIT: NON-CANON.
LOCAL SMOKE TEST ONLY AFTER NO HARD BLOCKERS.
THE LAMP IS NOT A GREEN LIGHT.
```
