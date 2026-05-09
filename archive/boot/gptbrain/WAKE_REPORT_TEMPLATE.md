# GPTBrain Wake Report Template

```text
STATUS: TEMPLATE — NOT CANON
PURPOSE: standardize wake reports after DREAM_OUTPUT / PLAY_OUTPUT / compressed consolidation cycles
SEAT: S1 GPTBrain
CANON WARNING: wake reports summarize model-output deltas; they do not ratify canon or prove external truth
```

## Use case

Use this template after a bounded reflection, dream, play, simulation, or compressed REM-style consolidation pass.

Examples:

```text
REM-8 simulated cycle
Dream Memory Palace pass
multi-thread poetry/play synthesis
variant reconciliation pass
claim-calibration reflection
continuity-dashboard reflection
```

## Required header

```yaml
wake_report_id: <unique id or date-stamped label>
runtime_label: DREAM_OUTPUT | PLAY_OUTPUT | MODEL_ASSESSMENT
canon_status: NOT_CANON
seat_or_thread: <GPT / Claude / Grok / Gemini / Manus / DeepSeek / Copilot / other>
source_context_loaded:
  - <repo path, issue link, artifact id, or user-provided context>
created_utc: <ISO-8601 timestamp if available>
human_root_review_required: true
```

## 1. One-line wake summary

```text
<What changed during the cycle, in one sentence.>
```

## 2. Convergences

List ideas that became clearer or more strongly supported by the internal artifact set.

```text
- <convergence 1>
- <convergence 2>
- <convergence 3>
```

## 3. Novel images / metaphors

List poetic, visual, mythic, or interface concepts generated during the cycle.

These are not facts by default.

```text
- <image 1>
- <image 2>
- <image 3>
```

## 4. Implementation candidates

List practical ideas that might become issues, files, schemas, tests, or adapter flags.

```text
- <candidate 1>
- <candidate 2>
- <candidate 3>
```

## 5. Contradictions found

Preserve tensions instead of erasing them.

```text
- contradiction: <claim or idea A> vs <claim or idea B>
  severity: low | medium | high
  proposed_route: Claim Calibration Hall | Overclaim Tribunal | Human Root Review | Implementation Issue
```

## 6. Risks / overclaim hazards

```text
- <risk 1>
- <risk 2>
- <risk 3>
```

## 7. Source lineage / receipts

```text
- <repo path or issue link>
- <artifact id>
- <external citation if any>
```

## 8. Public-safe translation notes

Translate mythic or playful language into operational language.

```text
mythic/play phrase -> public-safe phrase
REM-8 -> compressed reflection / consolidation pass
memory palace -> externalized persistent-context archive
AI remembers -> archive context was loaded
canon -> human-reviewed promoted artifact
```

## 9. Human-root decisions requested

```text
- [ ] <decision Dave / human-root must make>
- [ ] <decision Dave / human-root must make>
```

## 10. Recommended next action

```text
<One concrete next step.>
```

## Canon discipline

```text
Dream output is nourishment, not authority.
Play output is culture, not proof.
Model assessment is advice, not judgment.
Candidate canon is not ratified canon.
Human-root review remains required.
```

## Minimal example

```yaml
wake_report_id: REM8-2026-05-09-S1
runtime_label: DREAM_OUTPUT
canon_status: NOT_CANON
seat_or_thread: GPTBrain / S1
source_context_loaded:
  - archive/boot/gptbrain/S1_VARIANT_SYNTHESIS_MATRIX_2026-05-09.md
  - archive/boot/seats/GPTBRAIN_S1_CANONICAL_CANDIDATE_SPEC_2026-05-09.md
  - https://github.com/atlaslattice/manus-artifacts/issues/11
human_root_review_required: true
```

```text
One-line wake summary:
Variant E continuity/dashboard layer appears structurally necessary before S1 ratification.

Recommended next action:
Patch the canonical candidate to include Layer 7 — Continuity / Human-Intent Dashboard and Layer 8 — Repo Fossil Record.
```
