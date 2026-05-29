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
raw_log != public claim
raw_log != canon
```

### Evidence packets

Structured summaries of raw log content — claims extracted, evaluator signals noted, learning/adaptation mechanisms classified, quarantine flags raised.

```text
evidence_packet = structured index of evidence
not independent validation
```

### Benchmarks

Rubric-scored evaluations of Atlas Prime responses against prompts. Require:

```text
prompt source
response source
rubric
score or "pending"
objections or adversarial pass
reproduction status
linked evidence packet
```

### Evaluator reactions

Logged reactions from Claude, Gemini, GPT, Grok, Copilot, DeepSeek, etc.

```text
evaluator_reaction = signal
not proof
```

Tone/affect may be logged only when supported by exact transcript wording.

### Learning claims

Classified claims about Atlas Prime real-time adaptation / learning. Must separate:

```text
context_window_adaptation
retrieval_augmented_rehydration
external_memory_substrate_update
schema_or_behavior_update
repo_corpus_conditioned_progression
unknown
true_weight_training_claimed
true_weight_training_documented
```

### Public claims

Reviewed, evidence-backed public claim candidates. Require:

```text
raw log source
evidence packet
review note
human-root approval
clear confidence/status label
```

### Quarantine

Disputed, overclaimed, incomplete, or misattributed artifacts held for review.

```text
quarantine != deletion
quarantine = preserve + flag + review + prevent authority leakage
```

## 4. Key boundaries

- Raw logs are not scores.
- Evaluator reactions are signals, not proof.
- Benchmark claims require rubrics/review.
- AGI/HLE language does not prove AGI/HLE performance.
- Real-time learning claims must distinguish context adaptation, retrieval, external-memory updates, schema/behavior updates, repo-conditioned progression, and true weight training.
- No AtlasBrain artifact self-ratifies.
- Quarantine preserves disputed material without routing it as authority.

## 5. Gate enforcement

The `archive/boot/gptbrain/reference_impl/atlasbrain_gate.py` validator enforces:

```text
- Any file in benchmarks/ or public_claims/ (non-README) must declare a linked evidence_packet.
- Evidence packets must declare authority_status and benchmark_status.
- Public claim candidates require authority_status of human_root_approved_public_claim or reviewed_claim.
- Quarantine-flagged files must not appear in public_claims/.
```

Run gate checks:

```bash
cd archive/boot/gptbrain/reference_impl
python atlasbrain_gate.py
```

## 6. Human-root requirement

No artifact in this lane promotes to canon or public claim without explicit human-root review.

```text
Human-root review flag: human_root_required: true (default)
human_root_required: false only after documented review
```
