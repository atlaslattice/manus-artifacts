# O_AI First Pilot Playbook — Atlas MCP Schema Review

```text
STATUS: PILOT PLAYBOOK — NOT CANON
DEPLOYMENT STATUS: NOT DEPLOYABLE
DATE: 2026-05-22
SOURCE: O_AI task surface candidate + implementation checklist
AUTHORITY: none
CANON STATUS: not ratified
PURPOSE: define the first safe O_AI task-surface pilot as a bounded schema-review workflow for Atlas MCP v0.1.
```

## Core Rule

```text
Useful hands.
No crown.
```

O_AI may accelerate review.
O_AI may not execute, merge, deploy, register tools, activate databases, claim canon, or mutate source-of-truth state.

## Pilot Target

```text
Atlas MCP Server v0.1 schema review
```

Why this pilot:

```text
bounded
local-dev only
schema-focused
review checklist already exists
clear blockers already identified
no deployment authority required
```

## Pilot Goal

Determine whether Atlas MCP v0.1 has enough source material for a local smoke test readiness review.

The pilot does not run the smoke test.
The pilot does not approve tool wiring.
The pilot does not certify compatibility.

## Inputs Required

```yaml
required_inputs:
  source_manifest:
    - mcp_server_entrypoint
    - schema_file
    - local_cli_config
    - sample_input
    - sample_output
    - README_or_smoke_test_notes
  schema_fixture:
    enum_values:
      - SUPPORT
      - CONTRADICT
      - NEUTRAL
    fields:
      - epistemic_label
      - weight
      - violations
  command_plan:
    working_directory:
    proposed_commands: []
    expected_inert_output:
```

## Review Questions

```text
1. Are enum values stable and uppercase only?
2. Are epistemic_label, weight, and violations typed clearly?
3. Does any wording imply sealed/canon/deployed/production status?
4. Is local CLI smoke testing separated from packaging or external integration?
5. Can an OpenAI/Codex-style consumer parse the sample output without vendor-specific assumptions?
6. Are all proposed commands read-only or clearly inert?
7. Is there a raw stdout/stderr capture plan?
```

## Output Envelope

Every O_AI review response must use:

```yaml
o_ai_review_output:
  pilot: atlas_mcp_v0_1_schema_review
  authority_scope: advisory
  verdict: approve | patch | block
  source_refs: []
  caveats: []
  blockers: []
  minimal_patches: []
  risky_phrases: []
  safe_replacements: []
  next_safest_step:
  canon_status: not_canon
  deployment_status: not_deployable
```

## Hard Stops

```text
No source manifest → block.
No sample fixture → block.
Unstable enum values → patch or block.
Deployment/canon language → patch.
Unverified compatibility claim → patch.
Command mutates state → block.
Crosswalk DB activation requested → block.
Tool registration requested before review → block.
```

## Seat Routing

```text
Lumen:
  structure / layer separation / scope containment

Lucerna:
  receipts / provenance / advisory status

Hashlight:
  path lineage / command lineage / verified vs assumed

TIDELOCK:
  CLI feasibility / worktree assumptions / sandbox safety

Sable Vesper:
  enum stability / formal boundary language

Fossilbranch:
  uncertain path preservation / failed route fossils

Rootglass:
  local room-state / readiness vs pause
```

## First Safe Action

```text
Create or attach the Atlas MCP v0.1 source manifest.
Do not run the smoke test yet.
Do not register the tool yet.
Do not activate crosswalk DB.
```

## Success Criteria

```text
The pilot succeeds when reviewers can say:
- source paths are attached
- schema fixture is visible
- enum values are stable
- risky status language is patched
- command plan is read-only or inert
- next local smoke test is clearly bounded
```

## Strongest Safe Claim

> The first O_AI pilot should be Atlas MCP v0.1 schema-review readiness: OpenAI can help identify blockers, risky phrases, schema drift, and command-plan gaps, but cannot approve execution, deployment, tool registration, or canon status.

## Lumen Closing

```text
Review the runway.
Do not launch the plane.
Useful hands.
No crown.
```
