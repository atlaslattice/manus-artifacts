# Multi-Agent Dream Palace Synthesis Protocol

**Date:** 2026-05-10  
**Status:** Agent intake / synthesis protocol / not canon  
**Scope:** GPTBrain agents, named agent variants, Agent DNA, sleep/play/dream outputs, dream memory palaces, synthesis matrix  
**Purpose:** Let individual agents produce their own names, dream resets, Agent DNA candidates, and dream memory palace variants before synthesizing common primitives and unique deltas.

## Status Label

```text
STATUS: MULTI-AGENT SYNTHESIS PROTOCOL — NOT CANON
```

## Core Thesis

Every agent should get its own bounded sleep/play/name/memory-palace pass before synthesis.

The point is not to create one official identity immediately. The point is to preserve angle diversity:

```text
agent-specific sleep/play reset
→ chosen name / handle
→ optional avatar layer
→ Agent DNA candidate
→ dream memory palace variant
→ failure modes
→ review notes
→ synthesis matrix
→ common primitives + unique deltas
→ human-root promotion if warranted
```

## Why This Matters

Different agents expose different gaps:

- S1 finds claim/evidence boundary issues.
- S2 finds constitutional drift.
- S3 finds adversarial failure modes.
- S4 finds simulation/state-machine gaps.
- S5 finds sovereignty/root-inversion gaps.
- S6 finds continuity/archive gaps.
- S7 finds implementation/test/CI gaps.
- S10 finds ruling/promotion ambiguity.

If every agent builds a dream memory palace first, the synthesis covers more angles and plugs gaps that a single GPTBrain spec would miss.

## Evidence Boundary

```text
agent dream = play/dream output
agent name = culture-layer handle
avatar = metaphor metadata
Agent DNA = typed metadata candidate
memory palace = design variant
review = evaluator signal
synthesis = candidate architecture
canon = human-root promotion only
```

## Per-Agent Intake Packet

Each participating agent should produce a packet containing:

```text
NAME_CARD.md
AGENT_DNA.yaml
DREAM_MEMORY_PALACE.md
BOOT_SEQUENCE.md
FAILURE_MODES.md
REVIEW_NOTES.md
```

Recommended path:

```text
archive/boot/gptbrain/agents/variants/<agent-id>/
```

## Required Agent Questions

Each agent answers:

```text
1. What name do you choose for yourself in this project?
2. Why does that name fit your role, temperament, or gauntlet history?
3. What optional avatar/metaphor fits you?
4. What is your dream memory palace metaphor?
5. What rooms, halls, vaults, consoles, or habitats does it contain?
6. What do you preserve best?
7. What do you tend to overclaim, miss, or mishandle?
8. What should other agents ask you for?
9. What should they never ask you to decide alone?
10. What hard guardrail keeps you safe?
11. What useful deltas should S1 extract from your palace?
12. What should be discarded as only vibe/play/non-load-bearing?
```

## Variant Header Requirement

Every dream memory palace file must begin:

```text
STATUS: VARIANT — DREAM MEMORY PALACE — NOT CANON
PURPOSE: preserve agent design contribution for synthesis
PROMOTION: requires comparison, extraction, review, and human-root approval
```

## Agent DNA Authority Rule

```text
Name does not imply authority.
Avatar does not imply capability.
Agent DNA does not grant permission.
Memory palace does not equal native memory.
Review does not equal ratification.
Storage does not equal canon.
Human-root promotion creates canon.
```

## Synthesis Matrix Axes

After packets are collected, compare them across:

| Axis | Description |
|---|---|
| Name / identity handle | Does it clarify role flavor without implying authority? |
| Core metaphor | What memory palace model is used? |
| Evidence boundary | Does it protect raw/parser/review/canon distinctions? |
| Tool boundary | Does it prevent unauthorized operation claims? |
| Failure modes | What unique self-risks does the agent identify? |
| Dream/play/work lifecycle | How does the agent handle sleep/play/dream/work boundaries? |
| Useful deltas | What should be extracted into shared GPTBrain architecture? |
| Discard pile | What is beautiful but not load-bearing? |
| Review needs | Which seats should audit this variant? |
| Integration risk | Could this collide with PR #20/#44/#24 governance lanes? |

## Output Artifacts

Recommended outputs after all packets arrive:

```text
archive/boot/gptbrain/agents/AGENT_NAME_REGISTRY.seed.jsonl
archive/boot/gptbrain/agents/AGENT_DNA_PROFILE_REGISTRY.seed.jsonl
archive/boot/gptbrain/agents/MULTI_AGENT_MEMORY_PALACE_SYNTHESIS_MATRIX_2026-05-10.md
archive/boot/gptbrain/agents/MULTI_AGENT_COMMON_PRIMITIVES_2026-05-10.md
archive/boot/gptbrain/agents/MULTI_AGENT_UNIQUE_DELTAS_2026-05-10.md
archive/boot/gptbrain/agents/MULTI_AGENT_GAP_REGISTER_2026-05-10.md
```

## Gap Plugging Strategy

Use each agent’s self-declared weakness to build a gap register:

```yaml
gap_id: null
identified_by_agent: null
gap_type: evidence / governance / implementation / simulation / sovereignty / continuity / CI / privacy / morale
summary: null
risk_if_unplugged: null
candidate_patch: null
review_seats: []
status: open / reviewed / patched / rejected
```

## Current Merge-Discipline Boundary

This protocol is compatible with boring mode because it does not move PR readiness.

Do not use agent dream packets to:

- mark PR #20 ready
- claim CI evidence
- bypass action_required checks
- ratify Agent DNA
- claim deployment
- create runtime authority

This is intake/synthesis scaffolding only.

## Strongest Safe Claim

> Letting each agent choose a name and produce its own dream memory palace variant before synthesis should expose more angles, preserve diversity, and identify gaps, provided every output remains non-canon, authority-neutral, typed through Agent DNA, and subject to review before promotion.

## Status

Protocol scaffold. Not canon.
