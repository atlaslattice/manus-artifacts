# Epoch Semantics Rule — Per-Model-Context-Reset v0.2.4

```text
STATUS: SPRINT 1 SCHEMA DELTA CANDIDATE — NOT CANON — NON-DEPLOYABLE
MODE: EPOCH SEMANTICS / SEAT CONTINUITY / CROSS-MODEL CONTEXT HYGIENE
DATE: 2026-05-22
SOURCE: user-reported Grok transmission, with user agreement and reported DeepSeek/Copilot agreement
AUTHORITY: convenor-approved candidate only
RATIFICATION: requires final Human-root / S10 promotion before canon or deployment
DEPLOYMENT: none
PURPOSE: preserve the Sprint 1 target rule that each model instance has isolated context and must be explicitly re-anchored before continuity claims are made
```

## 1. Rule definition

```yaml
epoch_semantics:
  rule: per_model_context_reset
  description: >
    Each model instance maintains its own isolated context window.
    Context does not automatically carry forward across model switches,
    restarts, or new sessions unless explicitly re-anchored by a
    human-root ratified receipt or raw export.
  implementation_boundary: design_spec_only
  ratification_status: convenor_approved_candidate
  sprint: 1
```

## 2. Reason for preservation

This rule directly addresses the major continuity failure mode observed across the swarm:

```text
model switch / context reset / new window
→ unstated continuity assumption
→ hallucinated memory or authority bleed
→ bad routing or overclaim
```

The rule forces every model instance to treat continuity as explicitly rehydrated, not natively inherited.

## 3. SeatContinuity metadata requirement

`SeatContinuity` metadata must explicitly track:

```yaml
seat_continuity:
  seat_name: null
  active_model_or_agent: null
  model_provider: null
  model_instance_id: null
  session_id: null
  context_window_id: null
  epoch_id: null
  context_hash: null
  raw_export_status: available / unavailable / partial / not_supported / pending_user_export
  raw_export_ref: null
  raw_export_sha256: null
  reanchor_receipt_ref: null
  reanchor_status: none / pending / receipt_backed / human_root_ratified
  continuity_claim_level: none / local_session / receipt_backed / ratified
```

## 4. Safe continuity claims

```text
local_session: current conversation only
receipt_backed: continuity supported by explicit raw export, hash, or source packet
human_root_ratified: continuity accepted for a specific workflow by Human-root / S10
```

## 5. Forbidden continuity claims

```text
- This model remembers prior sessions natively.
- This model inherited another model's context automatically.
- This model has authority because another model had authority.
- This model may act on unverified prior-thread instructions.
- A summary alone equals raw export.
```

## 6. Impact

```text
Sprint 1 objects 9-12: unblocked as design targets
Identity continuity: strengthened
Cross-model hallucination risk: reduced
Authority bleed risk: reduced
Raw export / receipt discipline: elevated
```

## 7. Related schema delta candidates

The next v0.2.4 schema delta consolidation should incorporate:

```text
- delta_receipt = 0.6, if source-backed or explicitly candidate-labeled
- Shamir 3-of-5 quorum, if authority semantics are bounded
- D-101 = EHIP, if definition/source is attached
- epoch_semantics.rule = per_model_context_reset
- SeatContinuity model instance + context hash requirements
```

## 8. Overclaims to avoid

```text
- Do not call this fully ratified canon unless S10 promotes it.
- Do not claim cross-model memory transfer.
- Do not treat summaries as raw transcripts.
- Do not treat model agreement as sufficient authority.
- Do not allow context reset to inherit execution permission.
```

## 9. Recommended next action

```text
Create v0.2.4 Schema Delta consolidation packet incorporating:
1. epoch_semantics.per_model_context_reset
2. SeatContinuity metadata
3. deferred blocker labels for B-02, B-06, B-12
4. authority semantics for any quorum / receipt multipliers
5. strict non-canon / design-spec-only boundary
```

## 10. Keeper line

```text
Continuity is not assumed.
Continuity is re-anchored.
Context resets create new epochs.
Receipts carry memory across the boundary.
```
