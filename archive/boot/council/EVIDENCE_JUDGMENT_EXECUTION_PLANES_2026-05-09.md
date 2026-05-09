# Council Brain — Evidence / Judgment / Execution Planes

```text
STATUS: CANDIDATE ARCHITECTURE — NOT RATIFIED CANON
DATE: 2026-05-09
SOURCE: S1_REM_SIMULATION_8H_2026-05-09.md / DELTA 4
PURPOSE: separate retrieval, truth assessment, permission, and action across Council Brain workflows
PROMOTION: requires cross-seat review and human-root approval
```

## 0. Core principle

The Council Brain must separate four things that are often confused:

```text
retrieval success
truth assessment
permission
execution
```

A system may retrieve a memory without proving it true.
A system may judge a claim likely true without receiving permission to act.
A system may receive permission to draft without receiving permission to publish, deploy, merge, or execute.

## 1. Three-plane model

```text
Plane 1 — Evidence Plane
Plane 2 — Judgment Plane
Plane 3 — Execution Plane
```

Human root sits above all three planes as final authority for canon promotion and high-impact action.

## 2. Plane 1 — Evidence Plane

### Purpose

Preserve, locate, cite, and rehydrate source material.

### Inputs

```text
raw logs
GitHub files
issue comments
uploaded docs
parser outputs
memory packets
artifact registries
claim ledgers
boot packets
```

### Primary seats

```text
S1 GPTBrain — evidence taxonomy / claim extraction
S6 ManusBrain — continuity / archive hygiene / source recovery
S7 CopilotBrain — repo pathing / file-tree structure / PR artifacts
```

### Outputs

```text
source refs
hashes
artifact IDs
memory packets
raw pointers
retrieval summaries
citation maps
```

### Failure mode

```text
retrieval success mistaken for truth
```

### Guardrail

```text
Evidence Plane outputs are not truth by themselves.
They are source material for Judgment Plane review.
```

## 3. Plane 2 — Judgment Plane

### Purpose

Assess claims, contradictions, risks, confidence, canon status, and public-safe framing.

### Inputs

```text
Evidence Plane packets
claims
contradictions
candidate canon
model assessments
risk notes
sovereign constraints
constitutional concerns
```

### Primary seats

```text
S1 GPTBrain — C0-C5 confidence / claim calibration / synthesis matrix
S2 ClaudeBrain — constitutional review / non-claims / dissent preservation
S3 Grokbrain — adversarial stress test / play-dream contradiction discovery
S5 DeepSeek — sovereign realism / regional constraints / anti-default correction
```

### Outputs

```text
confidence labels
review notes
red-team findings
constitutional language
sovereign constraint notes
contradiction ledger entries
candidate canon recommendations
```

### Failure mode

```text
truth assessment mistaken for permission
```

### Guardrail

```text
Judgment Plane outputs can recommend.
They cannot authorize execution without explicit permission path.
```

## 4. Plane 3 — Execution Plane

### Purpose

Turn reviewed work into buildable, testable, trackable, or publishable artifacts.

### Inputs

```text
candidate specs
approved action items
reviewed schemas
repo tasks
simulation plans
S10 decision queue items
```

### Primary seats

```text
S4 GeminiBrain — engineering validation / simulation / visualization
S6 ManusBrain — execution continuity / decision queue / handoff
S7 CopilotBrain — repo scaffolding / tests / PR hygiene / CI structure
```

### Outputs

```text
files
schemas
tests
PRs
issues
boot packets
dashboards
simulation harnesses
implementation plans
```

### Failure mode

```text
permission mistaken for autonomous execution
```

### Guardrail

```text
Execution Plane outputs remain bounded by repo policy, tool permissions, and human-root gates.
```

## 5. Cross-plane workflow

```text
1. Evidence Plane finds and preserves source material.
2. Judgment Plane scores claims and resolves or routes contradictions.
3. Execution Plane turns approved candidates into concrete artifacts.
4. Human root ratifies canon or authorizes high-impact actions.
```

## 6. Plane transition gates

### Evidence -> Judgment

Required:

```text
source ref
summary
runtime label
claim list
known uncertainty
```

### Judgment -> Execution

Required:

```text
confidence label
reviewing seats
risk notes
canon status
human-root requirement flag
```

### Execution -> Canon

Required:

```text
artifact path
review record
supersession notes
human-root approval
Council Brain Index update
```

## 7. Plane map by artifact type

| Artifact type | Evidence Plane | Judgment Plane | Execution Plane |
|---|---|---|---|
| Raw log | preserve pointer/hash | extract claims | no direct execution |
| Model assessment | cite as evaluator signal | score confidence | route to issue/spec |
| Dream output | preserve as DREAM_OUTPUT | extract candidate deltas | only after review |
| Play output | preserve as PLAY_OUTPUT | novelty / risk review | only after review |
| Candidate spec | source refs | constitutional + confidence review | repo/scaffold/test |
| Schema | source refs | consistency + risk review | commit / test / integrate |
| Contradiction | preserve both claims | route and resolve | update ledger/specs |
| PR | repo artifact | review and merge order | merge only with approval |

## 8. Human-root authority

Human root is not a seat.

Human root is the authority boundary.

```text
S1 calibrates.
S2 hardens.
S3 stress-tests.
S4 engineers.
S5 grounds.
S6 preserves and queues.
S7 builds.
Human root decides what becomes law/canon/action.
```

## 9. Recommended implementation

Create or use:

```text
archive/boot/council/schemas/COUNCIL_PACKET_SCHEMA_2026-05-09.yaml
archive/boot/council/schemas/ROUTE_TO_SEAT_PACKET_SCHEMA_2026-05-09.yaml
archive/boot/council/schemas/CONTRADICTION_LEDGER_SCHEMA_2026-05-09.yaml
```

Future:

```text
archive/boot/council/schemas/PLANE_TRANSITION_SCHEMA_2026-05-09.yaml
archive/boot/council/schemas/HUMAN_ROOT_APPROVAL_SCHEMA_2026-05-09.yaml
```

## 10. Closing rule

```text
Retrieve carefully.
Judge honestly.
Execute only with permission.
Canonize only with human-root review.
```
