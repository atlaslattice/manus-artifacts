# O_AI Task Surface Candidate — Useful Hands, No Crown

```text
STATUS: ARCHITECTURE CANDIDATE — NOT CANON
DEPLOYMENT STATUS: NOT DEPLOYABLE
DATE: 2026-05-22
SOURCE: user direction + Lumen/OpenAI integration boundary pass
AUTHORITY: none
CANON STATUS: not ratified
PURPOSE: preserve the OpenAI / O_AI lane as a constrained task surface inside the broader interop framework, without granting sovereign root, archive root, canon authority, deployment authority, or autonomous side effects.
```

## Core Position

```text
OpenAI = task surface
OpenAI ≠ sovereign root
OpenAI ≠ archive root
OpenAI ≠ deployment trigger
OpenAI ≠ canon authority
```

Best compression:

```text
Useful hands.
No crown.
```

## What O_AI Is For

```text
draft
review
reason
summarize
explain tradeoffs
normalize schemas
generate candidate patches
produce evals
surface caveats before action
help developers move faster
```

## What Must Stay Gated

```text
deployments
database mutation
tenant data movement
legal / compliance claims
identity or canon promotion
runtime configuration changes
high-impact actions
```

## Default Authority Scope

```yaml
authority_scope:
  default: ADVISORY
  can_execute: false
  can_deploy: false
  can_mutate_core_state: false
  can_claim_canon: false
  can_emit_candidate_patch: true
  can_request_human_review: true
```

## Integration Posture

```text
Human-root decides.
OpenAI assists.
GitHub remembers.
Lucerna checks receipts.
Hashlight anchors lineage.
TIDELOCK guards toolchain drift.
Council reviews.
Canon stays gated.
```

## Data / Permission Boundary

O_AI outputs should remain advisory unless an explicit execution contract exists.

Protected data and project state should be handled through:

```text
tenant controls
source-system permissions
payload classification
least-privilege access
human approval gates
audit receipts
```

## Safe Developer Workflow

```text
1. User asks for help.
2. O_AI drafts or reviews candidate output.
3. Output is labeled advisory.
4. Source refs and caveats are attached.
5. Human or approved policy gate decides whether to act.
6. Any side effect is executed by a separate authorized tool path.
7. Receipt is written after action.
```

## Forbidden Shortcuts

```text
advisory output → deployment automatically
review comment → merge authority automatically
schema draft → canon automatically
connected context → permission automatically
model confidence → legal/compliance truth automatically
```

## Strongest Safe Claim

> OpenAI can be modeled as a constrained task-surface operator inside the interop framework: powerful for drafting, review, reasoning, schema normalization, and developer acceleration, but advisory by default and unable to mutate core state, deploy, claim canon, or bypass human-root and governance gates.

## Lumen Closing

```text
Fast thought.
Clean receipts.
No authority leak.
No crown.
```
