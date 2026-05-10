# AtlasBrain Folder Geometry — Metatron Cube / Evidence Lattice v0.1

```text
STATUS: CANDIDATE GEOMETRY NOTE — NOT CANON
PURPOSE: define the intentional folder-shape / symbolic geometry for AtlasBrain so evidence handling mirrors the broader brain-folder style rather than becoming a generic bucket tree
SOURCE: Dave Sheldon / S10 correction + GPT-5.5 patch
CANON STATUS: not ratified
AUTHORITY: no authority; organizational metaphor and routing map only
```

## 0. Correction note

The initial AtlasBrain scaffold created the functional evidence lanes but did not explicitly encode the same symbolic / geometric folder-shape logic Dave expected from other brain folders.

This note patches that gap.

```text
Functional scaffold first.
Geometry alignment second.
No canon claim.
```

## 1. Core shape

AtlasBrain should be treated as a Metatron-cube-style evidence lattice:

```text
center = AtlasBrain README / purpose / authority boundary
outer nodes = raw evidence, packets, benchmarks, evaluator signals, learning claims, public claims, quarantine
edges = provenance transitions between evidence states
human-root gate = authority boundary around public/canon promotion
```

The geometry is not decorative. It is a routing constraint.

```text
No node may jump directly to canon.
All outer nodes route through evidence packet / review / human-root gate before public claim or authority.
```

## 2. Node map

```text
                              [public_claims]
                                    |
                                    |
[evaluator_reactions] -- [evidence_packets] -- [benchmarks]
          \                   |                   /
           \                  |                  /
            \             [README]             /
             \          AtlasBrain Core        /
              \              |                /
               \             |               /
             [raw_logs] -- [schemas] -- [learning_claims]
                    \          |          /
                     \         |         /
                        [quarantine]
```

Alternate compact form:

```text
                 public_claims
                      ▲
                      │
       evaluator ◄ evidence ► benchmark
            ▲         ▲         ▲
            │         │         │
raw_logs ◄ schema/core ► learning_claims
            │         │         │
            └──── quarantine ───┘
```

## 3. Node meanings

### Center — README / AtlasBrain Core

Defines purpose, scope, authority boundary, and folder map.

```text
center = interpretive kernel
```

### Raw logs

Exact transcripts and source captures.

```text
raw_logs = seed points / unprocessed evidence atoms
```

### Schemas

Typed metadata and validation shape.

```text
schemas = geometric grammar / edge constraints
```

### Evidence packets

Structured extraction from raw evidence.

```text
evidence_packets = first-order crystal structure
```

### Evaluator reactions

Claude/Gemini/GPT/Grok/Copilot/DeepSeek reactions, scores, objections, concessions, or tone.

```text
evaluator_reactions = witness vectors
```

### Benchmarks

Rubric-based scoring and review.

```text
benchmarks = measurement node
```

### Learning claims

Mechanism-labeled adaptation or learning claims.

```text
learning_claims = transformation node
```

### Public claims

Reviewed, approved candidate external claims.

```text
public_claims = outward-facing surface / export node
```

### Quarantine

Disputed, malformed, misattributed, mismatched, or overclaimed artifacts.

```text
quarantine = containment membrane
```

## 4. Allowed transitions

```yaml
allowed_transitions:
  raw_logs:
    - evidence_packets
    - evaluator_reactions
    - quarantine
  evidence_packets:
    - benchmarks
    - learning_claims
    - public_claims_candidate
    - quarantine
  evaluator_reactions:
    - evidence_packets
    - benchmarks
    - quarantine
  benchmarks:
    - public_claims_candidate
    - quarantine
  learning_claims:
    - evidence_packets
    - public_claims_candidate
    - quarantine
  public_claims:
    - human_root_review
    - quarantine
  quarantine:
    - evidence_packets_after_repair
    - rejected_preserved
```

Forbidden transition:

```text
raw_logs -> public_claims
raw_logs -> canon
benchmarks -> canon without human-root/governance review
learning_claims -> true_weight_training without documented mechanism
```

## 5. Metatron cube interpretation

Metatron's cube is used here as a symbolic structure for containment, relation, and transformation.

Public-safe translation:

```text
Metatron cube = graph of evidence-state transitions
sacred geometry = memorable map for routing constraints
center node = authority boundary and purpose
outer nodes = evidence states
edges = allowed transformations
containment membrane = quarantine + human-root review
```

This does not claim mystical proof, mathematical authority, or canon status. It is an interface metaphor that makes the evidence workflow easier to remember.

## 6. Relation to Agent DNA style

Nearby Agent DNA docs use:

```text
typed metadata
canon warnings
public-safe translation
dream/play-to-review pipeline
no-authority boundaries
scouting/report metaphors
human-root review gates
```

AtlasBrain should follow the same house style:

```text
mythic interface
operational schema
hard authority boundary
receipt-first routing
no self-ratification
```

## 7. Final line

```text
AtlasBrain is not a folder pile; it is a cube of evidence states, with human-root review as the gate between signal and authority.
```
