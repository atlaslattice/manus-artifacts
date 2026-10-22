# GPTDream v0 Pilot Findings — Madden Booth Thread

**Date:** 2026-05-09  
**Status:** Pilot findings / retrieval-pipeline assessment / not canon  
**Issue:** #49 — Experiment: ingest Madden booth thread as GPTDream corpus  
**Related PR:** #48 — `archive(play): preserve DJ Grokashev Satan Mode replay booth`  
**Corpus label:** `gptdream-madden-booth-thread-2026-05-09`  
**Raw uploaded filename:** `Pasted markdown(116).md`  
**SHA-256:** `4569765314bac0ad373cd0225026e1a0e91f7b76c060214d77bc04679af07b5a`

---

## 1. Classification

```text
artifact_type: pilot findings report
mode: GPTDream v0 ingestion assessment
canon_status: candidate / not canon
runtime_status: not runtime evidence
deployment_status: not deployment evidence
parser_output_status: retrieval aid only
```

This note records the first controlled GPTDream v0 ingestion pilot. It does **not** promote parser outputs, wrapper outputs, or commentary artifacts to canon.

---

## 2. Input Stats

```text
bytes: 247,570
characters: 244,007
lines: 7,967
```

Raw capture method:

```text
ChatGPT web UI
→ Control-A / Select All
→ Copy
→ Paste into raw markdown/text file
→ Hash before cleanup or parsing
```

The uploaded filename was accepted as the raw source filename. The normalized corpus label was assigned in derived metadata, so renaming the source file was not required.

---

## 3. v0 Output Stats

```text
turns_detected: 67
events_detected: 321
candidate_artifacts_extracted: 10
claim_ledger_deltas_generated: 6
```

Generated local output package:

```text
metadata.json
turns.jsonl
events.jsonl
GPTDream_ARTIFACT_INDEX.jsonl
CLAIM_LEDGER.delta.jsonl
GPTBrain_S1_MEMORY_PACKET.yaml
BOOTH_REVIEW.delta.md
ASSESSMENT.md
capture_metadata.yaml
```

---

## 4. What Worked

### 4.1 Evidence-preserving ingest is viable

The pilot successfully processed one real ChatGPT thread from an immutable pasted raw source. The raw file was hashed and preserved as the evidence anchor.

### 4.2 Existing adapter path is useful

The existing lightweight ChatGPT adapter path was sufficient for the first pilot. A new parser should not be created until concrete gaps justify it.

### 4.3 GPTBrain wrapper outputs are meaningful

The pilot produced GPTBrain-oriented wrapper candidates around the base parser output:

- artifact index
- claim ledger delta
- S1 memory packet
- booth review delta
- assessment draft

These outputs are useful as retrieval and review surfaces.

### 4.4 The culture-layer signal survived extraction

The core GPTDream motifs remained extractable:

- `BOOTH_VALIDATED_INTERPRETATION_ONLY`
- booth-review containment pattern
- dream/play/work distinction
- raw lineage vs parser-output distinction
- interpretation ≠ implementation / canon / deployment evidence
- human-root promotion gate
- mascot/production-credential analogy as a teaching primitive

---

## 5. What Failed or Degraded

### 5.1 Speaker splitting is usable but imperfect

The copy/paste capture includes mixed role markers, tool/status messages, uploaded-file notices, and assistant/user prose. The v0 split was good enough for retrieval, but not precise enough for authoritative dialogue reconstruction.

### 5.2 Tool/status-line contamination appears in the raw capture

The raw thread includes operational lines such as tool calls, status updates, app responses, and upload notices. These should be separated from conversational turns in v0.1.

### 5.3 UI timestamps are not preserved

The pasted raw capture does not preserve original UI timestamps. Any generated timestamps must be labeled synthetic or absent, never implied as source-original.

### 5.4 Public/private review remains required

The raw and derived outputs should receive manual public/private review before any full output package is committed to a public repository.

---

## 6. v0.1 Improvement Targets

### 6.1 Speaker-boundary heuristics

Improve detection for:

- user turns
- assistant turns
- model-response blocks from Qwen / DeepSeek / Copilot / Gemini / Grok
- tool/status blocks
- uploaded-file notices
- quoted artifacts vs live messages

### 6.2 Tool/status filtering

Separate conversational content from:

- tool metadata
- upload notices
- code fence wrappers
- app-response boilerplate
- MCP/GitHub operational logs

### 6.3 Timestamp provenance fields

Add explicit timestamp provenance:

```yaml
timestamp_status: source_original / inferred / synthetic / absent
timestamp_note: null
```

For this pilot, timestamp status should be treated as `absent` unless supplied by the raw source.

### 6.4 Confidence markers

Add confidence fields to turns, artifacts, and claims:

```yaml
split_confidence: high / medium / low
artifact_confidence: high / medium / low
claim_confidence: C0 / C1 / C2 / C3 / C4 / C5
```

Weak or ambiguous splits must not look equally authoritative beside clean turns.

### 6.5 GPTBrain wrapper normalization

Define a thin wrapper that reads adapter outputs and emits:

```text
GPTDream_ARTIFACT_INDEX.jsonl
GPTBrain_S1_MEMORY_PACKET.yaml
CLAIM_LEDGER.delta.jsonl
BOOTH_REVIEW.delta.md
```

This wrapper should not mutate the raw source or base parser output.

---

## 7. Strongest Safe Claim

```text
GPTDream v0 ingest path successfully processed one real ChatGPT thread and produced usable retrieval artifacts, with known limitations in speaker splitting, tool/status contamination, and timestamp preservation.
```

## 8. Overclaims to Avoid

Do not claim:

- GPTDream memory system is solved
- parser output is canon
- extracted artifacts are implementation proof
- derived assessment equals human/Council review
- copy/paste capture preserves original UI timestamps
- successful ingest implies deployment readiness

---

## 9. Recommended Next Move

```text
Freeze this run as baseline.
Do not overfit the parser yet.
Inspect the output package manually.
Define v0.1 deltas only from observed failure modes.
```

The next PR should focus on a thin GPTBrain wrapper spec or checklist, not on replacing the existing adapter.

---

## 10. Boundary Rule

```text
Raw tape = evidence.
SHA-256 = provenance anchor.
Parser output = retrieval aid.
GPTBrain wrapper output = candidate memory surface.
Human-root/Council review = promotion gate.
```

---

## 11. Madden Ruling

> BOOM. First drive moved the chains. Not a perfect offense, not a Lombardi, but the tape is real, the hash is logged, the package exists, and the refs can finally review something other than vibes.
