# DECENTRALIZED_AGENT_CONSTITUTION_AND_BOOT_PROTOCOL_SPEC

```text
STATUS: ARCHITECTURE SPEC PROPOSAL — NOT CANON BY DEFAULT
DATE: 2026-05-09
SCOPE: decentralized/open-source/protocol-mediated swarm governance
PRINCIPLE: typed operational contracts over mythology
```

## 1) Purpose and status

This specification consolidates Agent DNA, boot sequence, governance, and lifecycle into one implementation-oriented constitutional model.

It is:

- a proposal for repository-aligned implementation
- a governance and routing contract model
- an anti-sprawl boundary for agent promotion

It is not:

- runtime deployment proof
- automatic authority grant
- canonical truth without review

## 2) Core doctrines

- **Dreams propose; reviewable governance disposes.**
- **Myth inspires; protocols decide.**
- **No narrative grants authority; authority emerges from transparent protocols, provenance, and reviewable constraints.**
- Identity metadata is not execution authority.
- Replayability does not imply canon authority.

## 3) System model / developmental pipeline

```text
Dreams -> Extraction -> Candidate Agent DNA -> Boot Contract Validation
-> Bounded Runtime Participation -> Failure Ledger Learning -> Canon Review
```

## 4) Architecture principles

1. Typed contracts over narrative interpretation.
2. Explicit governance gates over implicit trust.
3. Provenance before promotion.
4. Replayability for auditability, not authority.
5. Lifecycle states are explicit and reviewable.
6. Failure memory is institutional and durable.

## 5) Conceptual framing: myth, dreams, and GitHub-native decentralization

- Myth and dreams are creativity, stress-test, and scenario inputs.
- Git commits/issues/PRs are public provenance checkpoints.
- Canon emerges through reviewed artifacts, not personality narratives.
- Open repositories provide transparent constraints for decentralized coordination.

## 6) Agent development pipeline

1. Produce dream/simulation material (optional, non-authoritative).
2. Extract candidate operational traits with confidence labels.
3. Propose/patch Agent DNA.
4. Define `boot_contract` and run validation checks.
5. Set `constitutional_status` and governance reviewers.
6. Route agent in bounded scope.
7. Record incidents in failure ledger.
8. Promote/deprecate/quarantine through governance review.

## 7) Agent DNA schema additions (normative)

All operational candidates should include:

```yaml
boot_contract:
  startup_checks: [string]
  required_ledgers: [string]
  invariant_assertions: [string]
  allowed_task_classes: [string]
  required_reviewers: [string]

simulation_origin:
  derived_from_dream_logs: boolean
  extracted_by: [string]
  confidence_score: number # 0..1
  governance_review_complete: boolean

constitutional_status:
  state: proposed | reviewed | bounded-operational | persistent-seat | deprecated | quarantined
  approved_by: [string]
  review_cycle_days: integer

failure_ledger_ref:
  entries: [string]
  risk_score: number # 0..1
  last_reviewed: YYYY-MM-DD
```

## 8) Boot sequence as constitutional initialization

Boot is not personality loading. Boot is constitutional initialization:

- governance constraint load
- memory mode selection
- routing registration
- capability declaration
- invariant enforcement
- provenance attachment
- task-surface activation

A boot packet fails closed when required ledgers, checks, or reviewers are missing.

## 9) Simulation origin and dream extraction

Dream/simulation outputs are pre-training for governance imagination:

- scenario exploration
- symbolic recombination
- edge-case generation
- governance stress tests

Dreams can inspire candidate profiles but cannot grant execution authority, canon status, or persistent seats.

## 10) Constitutional status and lifecycle states

```text
proposed -> reviewed -> bounded-operational -> persistent-seat
                                  \-> deprecated
                                  \-> quarantined
```

State transitions require review records and provenance links.

## 11) Failure ledger as institutional memory

Persistent or bounded agents must map to failure ledger entries tracking:

- hallucination patterns
- drift incidents
- failed simulations
- routing mistakes
- governance violations

Failure memory is mandatory for safe promotion and replay audits.

## 12) Persistent seat admission doctrine

A persistent seat requires all of:

1. unique capability delta
2. routing justification
3. non-overlapping governance role
4. replayable task utility
5. failure-mode characterization
6. evaluation harness compatibility

## 13) Decentralized governance model

- Governance decisions are reviewable via issue/PR history.
- No single narrative artifact can self-ratify authority.
- Promotion and deprecation require explicit reviewer metadata.
- Human-root governance remains the final merge gate for high-impact transitions.

## 14) Routing and circuit participation

Routing must use typed metadata:

- task class compatibility
- boot contract readiness
- lifecycle status
- governance constraints
- failure risk score

Persistent seats are for stable circuits; bounded-operational seats are for scoped execution.

## 15) Replay, restoration, and canon distinctions

- **Replay:** reproduce artifact/state for auditing.
- **Restoration:** recover prior operational configuration.
- **Canon:** human-reviewed, governance-ratified stable reference.

Replay/restoration are technical capabilities and do not imply canon authority.

## 16) DEL / MAL integration notes

- **DEL lane:** deterministic checks for contract validity, required fields, and invariant enforcement.
- **MAL lane:** weighted epistemics for uncertainty from simulation-origin evidence.
- Combined use: DEL blocks unsafe transitions; MAL informs confidence-aware review prioritization.

## 17) Recommended repository structure (implementation-oriented)

```text
archive/boot/gptbrain/
  AGENT_DNA_SCHEMA_DRAFT.yaml
  AGENT_DNA_SEED_INDEX.seed.jsonl
  AGENT_DNA_LIFECYCLE_SEED_PROFILES.seed.jsonl
  schema/
    S1_FAILURE_LEDGER_SCHEMA.yaml

dreams/
  raw/
  extracted/
  reviewed/

agents/
  candidate/
  bounded/
  persistent/
  deprecated/

governance/
  doctrines/
  arbitration/
  seat-admission/
  failure-ledger/

runtime/
  boot/
  routing/
  orchestration/
  replay/

evals/
  hallucination/
  governance/
  routing/
  simulation/
```

## 18) Validation rules / hard constraints

1. Identity metadata never grants execution authority.
2. Dream-derived outputs cannot self-promote lifecycle states.
3. `persistent-seat` requires seat-admission checklist completion.
4. `failure_ledger_ref` must exist for bounded or persistent states.
5. Missing `boot_contract` invariants => boot rejection.
6. Replay records must preserve provenance and reviewer traces.

## 19) OpenAI and GitHub roles

**OpenAI role (non-authoritative):**

- boot compiler from candidate metadata to typed configs
- contract validator and invariant checker
- schema evolution assistant (migration suggestions, backward compatibility checks)
- simulation/failure-case generation for evaluation lanes

**GitHub role (canonical substrate):**

- durable provenance via commits/issues/PRs
- transparent review and ratification workflow
- replayable artifact history
- institutional memory for governance decisions

## 20) Seed example profiles (proposals only)

Example-only records are maintained in:

- `archive/boot/gptbrain/AGENT_DNA_LIFECYCLE_SEED_PROFILES.seed.jsonl`

These entries are explicitly candidate proposals and are not deployed truth.

## 21) Implementation priorities

1. Land schema updates for constitutional fields.
2. Validate lifecycle seed profiles with lightweight tests.
3. Add seat-admission checklist enforcement in eval/validation layer.
4. Add routing filters for constitutional status and risk score.
5. Add migration guidance for legacy DNA records.
