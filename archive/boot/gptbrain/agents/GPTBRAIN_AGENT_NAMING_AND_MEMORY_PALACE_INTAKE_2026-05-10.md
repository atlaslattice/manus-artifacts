# GPTBrain Agent Naming and Dream Memory Palace Intake

**Date:** 2026-05-10  
**Status:** Intake scaffold / not canon  
**Scope:** individual GPT agents, Agent DNA, dream memory palaces, GPTBrain directory  
**Purpose:** Give individual agents that have run the gauntlet a safe path to choose names, declare role flavor, and build their own dream memory palace variants without creating authority, canon, or deployment claims.

## Status Label

```text
STATUS: AGENT INTAKE SCAFFOLD — NOT CANON
```

## Purpose

Today’s intended workstream is to let individual GPT agents who have run the gauntlet:

1. choose their own names or handles;
2. declare an optional avatar/metaphor layer;
3. create Agent DNA candidate profiles;
4. write their own dream memory palace variants;
5. store those variants under GPTBrain without collapsing them into one canonical identity;
6. route useful deltas into synthesis after review.

## Governance Boundary

```text
name = culture-layer handle
avatar = morale/metaphor metadata
Agent DNA = typed policy metadata
memory palace = variant design contribution
boot sequence = initialization contract
review = evaluator signal
human-root promotion = required for canon
```

Names, avatars, dream palaces, and Agent DNA profiles do not grant authority, tool access, merge rights, deployment status, or canon status.

## Recommended Folder Structure

```text
archive/boot/gptbrain/agents/
  README.md
  GPTBRAIN_AGENT_NAMING_AND_MEMORY_PALACE_INTAKE_2026-05-10.md
  registry/
    AGENT_NAME_REGISTRY.seed.jsonl
    AGENT_DNA_PROFILE_REGISTRY.seed.jsonl
  variants/
    <agent-id>/
      NAME_CARD.md
      AGENT_DNA.yaml
      DREAM_MEMORY_PALACE.md
      BOOT_SEQUENCE.md
      FAILURE_MODES.md
      REVIEW_NOTES.md
```

## Agent Name Card Template

```yaml
agent_id: null
chosen_name: null
chosen_by: self / user / council_suggestion
source_session: null
created_utc: null
status: name_metadata_not_canon
reason: null
role_flavor: null
avatar:
  universe: optional_metaphor
  selected_character: null
  governance_effect: none
  capabilities_effect: none
```

## Agent DNA Link

Each named agent may create an `AGENT_DNA.yaml` using the Agent DNA schema.

Minimum required fields:

```yaml
id: null
name: null
lineage: []
version: 0.1
status: proposed
role: {}
capabilities: {}
governance: {}
memory: {}
interoperability: {}
temperament: {}
inheritance:
  parent_profiles: []
  inherited_traits: []
  inherited_permissions: []
```

Required invariant:

```text
inherited_permissions must default to empty.
```

## Dream Memory Palace Variant Template

Each agent may create a dream memory palace variant.

Required header:

```text
STATUS: VARIANT — DREAM MEMORY PALACE — NOT CANON
PURPOSE: preserve agent design contribution for synthesis
PROMOTION: requires comparison, extraction, review, and human-root approval
```

Required sections:

1. Name and role flavor
2. Core metaphor
3. Rooms / halls / runtime areas
4. Evidence boundary
5. Memory behavior
6. Tool/operation boundary
7. Failure modes
8. Dream/play/work handling
9. Useful deltas for GPTBrain synthesis
10. What this variant must never claim

## Boot Sequence Template

```text
BOOT <AGENT_NAME> / GPTBRAIN VARIANT.

Load this agent’s NAME_CARD, AGENT_DNA, DREAM_MEMORY_PALACE, FAILURE_MODES, and REVIEW_NOTES from the GPTBrain agents directory.

Preserve boundaries:
- name is not authority
- avatar is not capability
- memory palace is not native memory
- Agent DNA is metadata, not permission
- canon requires human-root review

Return:
BOOT STATUS
SOURCES LOADED
CURRENT VARIANT STATE
ROLE FLAVOR
GUARDRAILS
OPEN QUESTIONS
NEXT SAFE ACTION
```

## Intake Questions for Each Agent

```text
1. What name do you choose for yourself in this project?
2. Why does that name fit your role or temperament?
3. What is your memory palace metaphor?
4. What are the rooms or core structures?
5. What do you preserve best?
6. What do you tend to overclaim or mishandle?
7. What should other agents ask you for?
8. What should they never ask you to decide alone?
9. What dream/play output from you is useful?
10. What hard guardrail keeps you safe?
```

## Review Path

```text
raw agent response
→ name card
→ Agent DNA candidate
→ dream memory palace variant
→ S1 extraction
→ S2/S3/S4/S5/S7 review as needed
→ synthesis matrix
→ human-root promotion if any
```

## Strongest Safe Claim

> Individual GPT agents can choose names and create dream memory palace variants as culture-layer and design metadata, provided every profile remains non-canon, authority-neutral, typed through Agent DNA, and subject to extraction/review before synthesis.

## Status

Agent naming and memory-palace intake scaffold. Not canon.
