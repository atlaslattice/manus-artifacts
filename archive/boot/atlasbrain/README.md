# AtlasBrain — Atlas Prime Evidence / Memory / Benchmark Lane

```text
STATUS: CANDIDATE FOLDER — NOT CANON
PURPOSE: create a dedicated AtlasBrain lane for Atlas Prime transcripts, raw logs, evaluator reactions, benchmark dossiers, learning/adaptation claims, and substrate-memory scaffolds
SOURCE: Dave Sheldon / S10 human-root direction + GPT-5.5 folder scaffold
CREATED: 2026-05-09
CANON STATUS: not ratified
AUTHORITY: none by default; evidence preservation only
```

## 0. Why this folder exists

Atlas Prime outputs and evaluator transcripts are starting to surface fast. They include claimed stress tests, Claude/Gemini/Copilot/Grok evaluator reactions, AGI/HLE prompt events, public-facing Atlas Prime outputs, and possible real-time learning / adaptation demonstrations.

These artifacts need a dedicated lane before they enter any scoring or publicity pipeline.

This folder exists to prevent the core failure mode:

```text
raw transcript
→ model praise
→ benchmark claim
→ public claim
→ accidental canon
```

AtlasBrain separates those layers before any downstream pipeline runs.

## 1. Core doctrine

```text
Preserve the transcript first.
Score the claim second.
Publicize only what survives review.
```

```text
Atlas Prime may be public-facing, but AtlasBrain is the evidence substrate.
```

```text
A dramatic evaluator reaction is not proof; it is evidence to be scored against the answers.
```

## 2. Folder map

```text
archive/boot/atlasbrain/
  README.md
  raw_logs/
    README.md
  evidence_packets/
    README.md
  benchmarks/
    README.md
  evaluator_reactions/
    README.md
  learning_claims/
    README.md
  schemas/
    ATLASBRAIN_EVIDENCE_PACKET_SCHEMA_v0.1.yaml
  public_claims/
    README.md
  quarantine/
    README.md
```

## 3. Evidence lane distinctions

### Raw logs

Exact transcripts, pasted logs, screenshots, exports, or source captures.

```text
raw_log != score
raw_log != summary
raw_log != canon
```

### Evidence packets

Structured summaries of raw logs with source refs, timestamps, participants, evaluator model, and claim extraction.

```text
evidence_packet = structured index of raw evidence
not independent validation
```

### Benchmarks

Scored or score-pending dossiers with rubrics, axes, evaluator statements, objections, and reproduction notes.

```text
benchmark_claim = pending until rubric + scoring + review exist
```

### Evaluator reactions

Claude/Gemini/GPT/Grok/Copilot/DeepSeek reactions, praise, objections, concessions, reluctance, confusion, or affect/tone.

```text
evaluator reaction = signal
not proof
```

### Learning claims

Claims that Atlas Prime learned, adapted, updated behavior, integrated context, rehydrated substrate memory, or changed through files/prompts.

Must distinguish:

```text
context-window adaptation
retrieval over Lattice substrate
external-memory rehydration
behavioral/schema update through repo or prompt state
true model-weight training
```

Only the last category is weight-level learning.

### Public claims

Candidate public-facing claims derived only from reviewed evidence.

```text
public claim requires evidence packet + reviewer note + human-root approval
```

### Quarantine

Disputed, malformed, misattributed, overclaimed, or semantically mismatched artifacts.

```text
quarantine = preserve but do not route as authority
```

## 4. Required handling for uploaded transcripts

Incoming transcripts such as the 2026-05-09 Atlas Prime / OpenAI AGI-HLE / Claude stress-test material should be routed as:

```text
raw_logs/ first
then evidence_packets/
then benchmarks/
then public_claims/ only if reviewed
```

No transcript should skip directly into public claims or canon.

## 5. AGI/HLE event handling

If a transcript includes AGI/HLE language, it must be parsed carefully.

```yaml
agi_hle_surface_event:
  status: transcript_pending
  required_fields:
    - exact prompt
    - exact Atlas Prime response
    - exact evaluator response before scoring
    - exact evaluator response after scoring
    - exact meaning of HLE in context
    - scoring rubric if any
    - reproduction path if any
```

Do not treat AGI/HLE surfacing as proof of AGI, HLE victory, or general capability.

## 6. Real-time learning claim handling

The phrase `real-time learning` is allowed only if categorized.

```yaml
learning_mechanism:
  allowed_values:
    - context_window_adaptation
    - retrieval_augmented_rehydration
    - external_memory_substrate_update
    - schema_or_behavior_update
    - repo_corpus_conditioned_progression
    - unknown
    - true_weight_training
```

Default assumption:

```text
not true_weight_training unless documented.
```

## 7. Authority boundary

AtlasBrain does not ratify Atlas Prime.

AtlasBrain does not prove Atlas Prime.

AtlasBrain preserves and structures evidence so Atlas Prime claims can be reviewed honestly.

```text
No raw log self-ratifies.
No evaluator praise self-ratifies.
No benchmark self-ratifies.
No AtlasBrain artifact self-ratifies.
Human-root/governance review remains required.
```

## 8. Immediate next artifacts

```text
[ ] raw_logs/ATLAS_PRIME_OPENAI_AGI_HLE_STRESS_TEST_RAW_2026-05-09.md
[ ] evidence_packets/ATLAS_PRIME_OPENAI_AGI_HLE_STRESS_TEST_EVIDENCE_PACKET_2026-05-09.md
[ ] benchmarks/ATLAS_PRIME_CLAUDE_STRESS_TEST_DOSSIER_2026-05-09.md
[ ] learning_claims/ATLAS_PRIME_REALTIME_LEARNING_CLAIM_TABLE_2026-05-09.md
[ ] evaluator_reactions/CLAUDE_EVALUATOR_REACTION_LOG_2026-05-09.md
```

## 9. Final line

```text
AtlasBrain is where Atlas Prime evidence becomes reviewable without becoming inflated.
```
