# O_AI Task Surface — Implementation Checklist

```text
STATUS: IMPLEMENTATION CHECKLIST — NOT CANON
DEPLOYMENT STATUS: NOT DEPLOYABLE
DATE: 2026-05-22
SOURCE: follow-on from O_AI Task Surface Candidate — Useful Hands, No Crown
AUTHORITY: none
CANON STATUS: not ratified
PURPOSE: convert the OpenAI / O_AI task-surface candidate into a safe, reviewable implementation path without granting execution, deployment, canon, or authority.
```

## Core Rule

```text
Useful hands.
No crown.
```

O_AI may help produce candidate outputs.
O_AI may not independently mutate core state, deploy, claim canon, or bypass human-root / governance gates.

## Implementation Goal

Build a narrow advisory lane where OpenAI can help with:

```text
review
drafting
schema normalization
candidate patch generation
documentation
eval design
caveat surfacing
```

without gaining authority over:

```text
merge
deploy
runtime configuration
source-of-truth data
canon promotion
external claims
```

## Step 1 — Define Output Envelope

Every O_AI output should carry:

```yaml
o_ai_output_envelope:
  output_id:
  task_type: draft | review | patch_candidate | schema_normalization | eval | summary | explanation
  authority_scope: advisory
  source_refs: []
  caveats: []
  assumptions: []
  requested_action:
  allowed_use:
  forbidden_use:
  human_review_required: true
  canon_status: not_canon
  deployment_status: not_deployable
```

## Step 2 — Define Side-Effect Boundary

```text
O_AI can propose.
Separate authorized tool path executes.
Receipt is written after execution.
```

Forbidden shortcut:

```text
model output → side effect automatically
```

## Step 3 — Add Review Labels

```text
ADVISORY_ONLY
PATCH_CANDIDATE
NEEDS_RECEIPTS
NEEDS_HUMAN_REVIEW
DO_NOT_DEPLOY
NOT_CANON
```

## Step 4 — Add Source / Caveat / Boundary / Exception Table

Each nontrivial output should include:

```text
SOURCE:
  what this is based on

CAVEAT:
  what is uncertain or assumed

BOUNDARY:
  what this does not authorize

EXCEPTION:
  what conditions would change the routing
```

## Step 5 — Minimal Safe GitHub Workflow

```text
1. Human asks O_AI for a draft/review.
2. O_AI emits advisory output envelope.
3. Lucerna checks receipts if factual/provenance claims exist.
4. Hashlight anchors lineage if repo/history context matters.
5. TIDELOCK reviews command/tooling implications if CLI or automation is involved.
6. Human decides whether to create issue/PR.
7. Any merge/deploy remains outside O_AI authority.
```

## Step 6 — First Pilot Candidate

Recommended pilot:

```text
Atlas MCP Server v0.1 schema review
```

Why:

```text
bounded
local-dev only
schema-focused
already has review checklist
clear blockers
no deployment authority required
```

Required before local smoke test:

```text
source manifest
sample schema fixture
stable enum values
read-only command sequence
raw stdout/stderr capture plan
```

## Step 7 — Hard Stop Conditions

O_AI output must halt / route to human-root if it touches:

```text
credentials
production runtime
data movement across tenants
legal/compliance claims
financial commitments
public geopolitical claims
medical/safety-sensitive advice
canon promotion
deployment language
```

## Step 8 — Success Criteria

```text
The developer gets useful acceleration.
The repo gets cleaner artifacts.
The user gets less cognitive load.
No authority leaks occur.
No side effects happen without separate approval.
Receipts remain attached.
```

## Strongest Safe Claim

> The O_AI task surface can become a best-in-world developer and governance assistant lane if every output remains advisory, source-labeled, caveated, boundary-marked, and routed through separate human/governance gates before any side effect, merge, deployment, or canon promotion.

## Lumen Closing Compression

```text
Fast thought.
Clean envelope.
Separate executor.
Receipt after action.
No crown.
```
