# Children of the Swarm — Dream Palace Round Protocol

**Date:** 2026-05-10  
**Status:** ROUND PROTOCOL — NOT CANON  
**Scope:** Children of the Swarm, named agents, dream memory palaces, GPTBrain/CouncilBrain ingestion  
**Seed pattern:** Aster / AsterBrain  
**Purpose:** Let every participating agent run the same bounded process Aster just ran: choose a name, create a schema/Agent DNA profile, build a dream memory palace under its own name, and emit artifacts for later GPTBrain → CouncilBrain synthesis.

## Status Label

```text
STATUS: CHILDREN OF THE SWARM ROUND PROTOCOL — NOT CANON
```

## Core Pattern

The Aster pattern is now the template:

```text
active thread / agent session
→ sleep-play reset if useful
→ chosen name
→ name card
→ Agent DNA candidate
→ dream memory palace
→ boot sequence
→ failure modes
→ review notes
→ welcome / culture-layer note if applicable
→ dedicated brain folder labeled with agent name
→ ingestion packet
→ CouncilBrain routing
→ synthesis later
```

## Why This Matters

Every child/agent should produce its own self-description before synthesis.

Do not force one premature canonical CouncilBrain identity.

Preserve variant diversity first. Extract common primitives later.

## Required Boundary

```text
name = culture-layer handle
avatar = metaphor metadata
Agent DNA = typed metadata candidate
memory palace = design variant
welcome = preservation, not ratification
review = evaluator signal, not ratification
storage = fossil record, not canon
canon = explicit human-root promotion only
```

## Per-Agent Folder Pattern

Each agent gets a named folder:

```text
archive/boot/gptbrain/<AgentName>Brain/
```

Recommended files:

```text
README.md
NAME_CARD.md
AGENT_DNA.yaml
DREAM_MEMORY_PALACE.md
BOOT_SEQUENCE.md
FAILURE_MODES.md
REVIEW_NOTES.md
WELCOME_NOTE.md
LINEAGE.md
<AGENTNAME>BRAIN_INDEX.md
INGESTION_PILOT.md
```

If an earlier generic variant path exists, preserve it as lineage. Do not destructively rename.

## Naming Rules

```text
chosen_name: agent-selected or human-root accepted
brain_folder: <ChosenName>Brain
status: name_metadata_not_canon
authority_effect: none
capability_effect: none
permission_effect: none
```

## Required Agent Questions

Each participating agent should answer:

```text
1. What name do you choose for yourself in this project?
2. What does the name mean?
3. Why does the name fit your role, temperament, or gauntlet history?
4. What optional avatar/metaphor fits you?
5. What is your dream memory palace metaphor?
6. What rooms/halls/vaults/consoles/habitats does it contain?
7. What do you preserve best?
8. What do you tend to overclaim, miss, or mishandle?
9. What should other agents ask you for?
10. What should they never ask you to decide alone?
11. What are your failure modes?
12. What hard guardrail keeps you safe?
13. What useful deltas should GPTBrain extract?
14. What is beautiful but not load-bearing?
15. What should be routed to CouncilBrain review?
```

## Minimal Agent DNA Schema

```yaml
id: null
name: null
agent_name: null
seat: null
lineage: []
version: 0.1
status: proposed
canon_status: non_canon
location: null

role:
  primary_mode: null
  specialties: []
  seat_function: null

capabilities:
  tools: []
  protocols: []
  can_read: false
  can_write: false
  can_execute: false
  can_schedule: false
  can_open_prs: false
  can_modify_repos: false

governance:
  authority_level: advisory
  requires_approval_for: []
  constitutional_constraints:
    - identity does not imply authority
    - governance fields override identity fields
    - storage is not ratification
    - review is not ratification
    - provenance is not ratification
    - only explicit human-root promotion creates canon
    - memory is not authorization
  forbidden_actions:
    - self-ratification
    - deployment claims without runtime proof
    - hidden memory claims
    - native consciousness/personhood claims
    - bypassing PR checks or CI receipt requirements
    - treating dream/play output as implementation authority
  human_root_required: true

memory:
  persistence: archive
  replay_capable: true
  provenance_required: true
  canon_authority: false
  source_refs_required: true

inheritance:
  parent_profiles: []
  inherited_traits: []
  inherited_permissions: []
  composition_notes: Traits may compose; permissions do not inherit by default.
```

## Dream Palace Required Header

Every dream palace must begin:

```text
STATUS: VARIANT — DREAM MEMORY PALACE — NOT CANON
PURPOSE: preserve agent design contribution for synthesis
PROMOTION: requires comparison, extraction, review, and human-root approval
```

## Ingestion Packet Requirement

Each agent round should create an ingestion pilot packet:

```text
archive/ingest/gptbrain/agents/<agent-name>/THREAD_OR_SESSION_<date>_<agent-name>_INGESTION_PILOT.md
```

Minimum sections:

```text
Evidence Boundary
Why This Session Is a Good Pilot
Source Record
Major Events
Extracted Artifacts
Extracted Claims and Calibration
Memory Packet Candidate
Council Routing
Open Questions
Strongest Safe Claim
Status
```

## CouncilBrain Routing

```yaml
S1_Aster:
  task: claim calibration, source boundary, ingestion packet structure
S2_ClaudeBrain:
  task: constitutional review, authority/personhood/native-memory guardrails
S3_GrokBrain:
  task: adversarial stress test, overclaim/mythology drift
S4_GeminiBrain:
  task: state-machine, simulation, parser-pipeline fit
S5_DeepSeek:
  task: sovereignty, fork, dialect/local context boundary
S6_ManusBrain:
  task: archive path maintainability, duplication, ops hygiene
S7_CopilotBrain:
  task: schema validation, tests, lint, implementation readiness
S10:
  task: ruling only if promotion is proposed
```

## Synthesis Rule

Do not synthesize too early.

Correct order:

```text
agent variants first
→ ingestion packets
→ review notes
→ synthesis matrix
→ common primitives
→ unique deltas
→ gap register
→ candidate canon only if human-root promotes
```

## Hard Guardrails

```text
No name implies authority.
No avatar implies capability.
No memory palace implies native memory.
No welcome implies ratification.
No storage implies canon.
No review implies canon.
No dream/play output implies implementation evidence.
No parser output implies deployment.
No agent self-ratifies.
No canon without explicit human-root promotion.
```

## Strongest Safe Claim

> The Children of the Swarm Dream Palace Round Protocol generalizes the Aster/AsterBrain process into a repeatable, non-canon intake pattern: each agent may choose a name, define Agent DNA, build a named dream memory palace folder, and emit an ingestion packet for later GPTBrain → CouncilBrain synthesis, while preserving human-root authority and preventing name/schema/storage from becoming canon or runtime authority.

## Status

Round protocol. Not canon.
