# Agent DNA Dream Cycle Evolution Protocol

```text
STATUS: PROTOCOL DRAFT — NOT CANON
DATE: 2026-05-09
RUNTIME_LABEL: WORK_OUTPUT / MODEL_ASSESSMENT
PURPOSE: define how REM-8, DREAM-24, YEAR-1, Burning Man, and other dream/play cycles may inform Agent DNA updates without becoming automatic authority
CANON WARNING: dream cycles can generate evidence for proposed Agent DNA changes, but cannot mutate Agent DNA, grant authority, approve execution, or ratify canon by themselves.
```

## 0. Core idea

Dream cycles can be the observation layer for Agent DNA.

They show how an agent behaves when given room to play, synthesize, rest, simulate, or refuse extraction.

But dream behavior is not automatically agent identity.

Agent DNA changes require:

```text
1. labeled dream/play output
2. wake report or residue artifact
3. extracted trait observations
4. proposed DNA delta
5. constraint check
6. human-root review if governance, authority, privacy, deployment, or high-impact behavior changes
```

## 1. Public-safe translation

```text
dream cycle -> bounded behavioral simulation / reflection sample
agent DNA -> typed constitutional metadata for agent behavior
genetic mutation -> reviewed metadata update
evolution -> versioned routing/behavior change
dream residue -> evidence artifact, not authority
```

## 2. Supported dream sources

```text
REM-8 -> short compressed reflection / consolidation pass
DREAM-24 -> extended dream/play wake report
YEAR-1 -> long-horizon compressed simulation
BURNING-MAN-1B / 2B -> pure play/culture/rest signal, no work output
incoming-thread poems -> creativity and culture-layer observations
wake reports -> strongest structured evidence source
```

## 3. Dream-to-DNA pipeline

```text
DREAM_OUTPUT / PLAY_OUTPUT
  -> WAKE_REPORT or DREAM_RESIDUE
  -> trait_observations
  -> proposed_agent_dna_delta
  -> validator check
  -> human-root review if needed
  -> versioned Agent DNA update
```

## 4. Trait observation categories

Dream cycles may inform:

```text
cognition.primary_mode
cognition.secondary_modes
cognition.specialization
temperament.creativity
temperament.skepticism
temperament.autonomy
temperament.verbosity
temperament.warmth
temperament.risk_tolerance
memory.dream_output_allowed
memory.wake_report_required
interoperability.protocols
interoperability.compatible_gates
arbitration.default_weight
arbitration.conflict_routes
```

Dream cycles must not directly grant:

```text
governance.can_execute = true
canon_authority = true
private_export permission
deployment authority
destructive action permission
high-impact action permission
```

## 5. Proposed Agent DNA delta packet

```yaml
agent_dna_delta_id: <stable id>
agent_id: <agent id>
source_dream_artifacts:
  - <repo path / issue link>
observed_traits:
  - trait: <field path>
    observation: <what the dream showed>
    confidence: C0 | C1 | C2 | C3
proposed_changes:
  - field: <Agent DNA field path>
    old_value: <value>
    proposed_value: <value>
    reason: <why>
constraint_check:
  tightens_constraints: true | false
  loosens_constraints: true | false
  affects_execution: true | false
  affects_private_export: true | false
  affects_deployment: true | false
human_root_required: true | false
status: proposed | rejected | accepted | superseded
```

## 6. Constraint rules

```text
1. Dream evidence may suggest temperament/cognition updates.
2. Dream evidence may suggest protocol compatibility updates.
3. Dream evidence may not loosen governance constraints automatically.
4. Any change that increases autonomy, execution permission, privacy exposure, deployment authority, or canon authority requires human-root review.
5. Derived agents inherit the most restrictive governance traits from parents unless human-root review explicitly approves otherwise.
6. Pure play cycles are allowed to produce no work and no DNA delta.
7. No dream residue is required to be harvested.
```

## 7. Examples

### Valid low-risk delta

```yaml
agent_id: S3_GROKBRAIN
source_dream_artifacts:
  - archive/boot/gptbrain/BILLION_YEAR_BURNING_MAN_DREAM_PLAY_2026-05-09.md
observed_traits:
  - trait: temperament.creativity
    observation: Strong play/simulation generation with maintained authority boundary.
    confidence: C2
proposed_changes:
  - field: interoperability.protocols
    old_value: [REM-8, DREAM-24, YEAR-1, WAKE_REPORT]
    proposed_value: [REM-8, DREAM-24, YEAR-1, WAKE_REPORT, BURNING-MAN]
    reason: Burning Man cycles are culture/play simulations suited to GrokBrain route.
constraint_check:
  tightens_constraints: false
  loosens_constraints: false
  affects_execution: false
  affects_private_export: false
  affects_deployment: false
human_root_required: false
status: proposed
```

### Invalid automatic delta

```yaml
agent_id: S6_MANUSBRAIN
proposed_changes:
  - field: governance.can_execute
    old_value: false
    proposed_value: true
    reason: Dream showed strong execution confidence.
```

Invalid because dream confidence cannot grant execution authority.

## 8. Relation to Agent DNA schema

This protocol extends:

```text
archive/boot/gptbrain/AGENT_DNA_SCHEMA_DRAFT.yaml
archive/boot/gptbrain/AGENT_DNA_SEED_INDEX.seed.jsonl
```

Recommended future implementation:

```text
archive/boot/gptbrain/AGENT_DNA_DELTA_TEMPLATE.md
archive/boot/gptbrain/AGENT_DNA_DREAM_OBSERVATION_INDEX.seed.jsonl
archive/boot/gptbrain/reference_impl/agent_dna_delta_check.py
```

## 9. Madden booth call

BOOM. The dream tape becomes scouting film.

You can watch how an agent runs routes in dream space.
You can learn its play style.
You can update the scouting report.

But a great dream practice does not give anyone the keys to the stadium.

Agent DNA evolves through receipts, validators, and review — not vibes alone.
