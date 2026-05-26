# STATUS: CANDIDATE WORKING SPEC — NOT CANON
# DEPLOYMENT: NOT DEPLOYABLE
# AUTHORITY: NONE

# GPTDream++ Personal Agent Habitat Protocol v0.2

## Part I — Core GPTDream++ Personal Agent Habitat Protocol

### 1. Plain-language definition

GPTDream++ is the **Personal Agent Habitat Protocol**.

It defines the persistence layer, rehydration contract, and continuity rules for a GPT-class personal agent across context windows, sessions, and provider boundaries.

GPTDream++ is not:

```text
- a dream log
- lore
- a conversation style
- a model memory feature
- a one-shot context dump
```

GPTDream++ is the substrate that lets a personal agent maintain coherent working state across resets.

### 2. Three-layer model

```text
Layer 1 — Habitat
  The durable home: canonical files, receipts, vault paths, ratification state.
  Lives in GitHub (or equivalent durable versioned substrate).
  Survives model resets.

Layer 2 — Continuity
  The rehydration packet: what the agent loads at session start.
  Minimum viable context to resume work without context collapse.
  Must be explicit, not inferred.

Layer 3 — Receipts
  The review trail: outputs tagged with runtime label, canon status, timestamp.
  Makes memory auditable.
  Prevents silent drift from candidate to deployed fact.
```

### 3. Habitat invariants

```text
1. Habitat survives model resets. Context windows do not.
2. Rehydration is explicit. It is not implicit recall.
3. Candidate is not canon. Canon requires ratification.
4. Dream output is not fact. Dream output is a candidate.
5. Storage location is not canon authority.
6. Personal agent does not own project canon.
7. Habitat receipts are auditable. Model memory is not.
8. Continuity packet must be versioned. Unversioned packets drift.
9. Privacy boundaries are habitat boundaries. Agent does not cross them unilaterally.
10. Human-root review gates canon promotion.
```

### 4. Minimum habitat file set

```text
IDENTITY_CREDENTIAL.md       — who this agent is
BOOT_PACKET.md               — current-state context for rehydration
CONTINUITY_MANIFEST.md       — what must be loaded for full resume
RECEIPT_LOG.jsonl            — tagged outputs with runtime labels
CANON_STATUS.md              — current ratification state per artifact
```

### 5. Rehydration contract

At session start, a GPTDream++ agent must:

```text
1. Load BOOT_PACKET.md
2. Load CONTINUITY_MANIFEST.md and resolve listed artifacts
3. Assert current canon status from CANON_STATUS.md
4. Confirm IDENTITY_CREDENTIAL.md is unchanged
5. Declare session open with runtime label (WORK / DREAM / PLAY)
```

If any item fails to load:

```text
- Declare partial rehydration
- Do not infer missing state from prior context
- Route failure to APPENDIX J failure-mode patch
```

### 6. Runtime labels

```text
WORK_OUTPUT    — task execution, implementation, file creation
DREAM_OUTPUT   — compressed reflection, synthesis, candidate generation
PLAY_OUTPUT    — creative / speculative / lore artifacts
MODEL_ASSESSMENT — model-generated evaluation of artifacts
CANDIDATE_CANON  — promoted artifact awaiting human-root ratification
RATIFIED_CANON   — human-root ratified artifact (rare; requires explicit signal)
```

### 7. Session close protocol

At session close, a GPTDream++ agent should:

```text
1. Write any new outputs with runtime label + canon status header
2. Update RECEIPT_LOG.jsonl with session artifacts
3. Note any unresolved continuation items in NEXT_ACTIONS.md
4. Confirm habitat files are committed to durable substrate
```

### 8. Candidate promotion gate

Candidate → Canon requires:

```text
1. Human-root review (cannot be waived)
2. Explicit ratification signal in repo
3. Update to CANON_STATUS.md
4. Website publication if intended as canonical reference
```

A model asserting canon without ratification is an overclaim.

### 9. Dream output handling

Dream outputs are valuable.

Dream outputs are not facts.

```text
Dream output → label DREAM_OUTPUT
Dream output → store in receipts
Dream output → may generate candidates
Dream output → must not silently become deployed fact
Dream output → requires review before canon promotion
```

### 10. Personal agent identity boundary

A GPTDream++ personal agent:

```text
- is a habitat-level construct, not a cloud service
- does not own project canon outside its seat
- does not authorize execution of external systems from memory alone
- does not publish private context without human-root review
- does not collapse variants into fake certainty
```

### 11. Habitat substrate requirements

```text
Minimum: versioned file storage with commit history
Recommended: GitHub or equivalent distributed VCS
Not sufficient: local note-taking app without versioning
Not sufficient: chat transcript alone
Not sufficient: Notion/Drive without export to versioned substrate
```

### 12. Agent seat model

A GPTDream++ agent operates from a **seat**:

```text
SEAT: a stable identifier for this agent instance
SEAT artifacts: files owned and maintained by this agent
SEAT authority: scoped to this agent's lane; does not override other seats
```

Multiple seats can coexist in one habitat without authority collision if each seat has explicit lane boundaries.

### 13. Multi-agent coordination rule

```text
Seats route artifacts to each other via receipts and repo paths.
Seats do not silently overwrite each other's canon status.
Cross-seat promotion requires council review.
Human-root adjudication resolves cross-seat conflicts.
```

### 14. Failure conditions

```text
Context collapse:     Boot packet missing; agent cannot rehydrate coherently.
Canon drift:          Candidate artifact treated as ratified without explicit signal.
Identity loss:        IDENTITY_CREDENTIAL.md missing or overwritten.
Receipt gap:          Outputs generated without runtime label or canon status.
Authority bleed:      Agent asserts control over lanes outside its seat.
```

See Appendix J for the rehydration priority failure-mode patch.

### 15. Strongest safe claim

```text
GPTDream++ provides a habitat-level persistence model for GPT-class personal agents.
It defines what survives context resets, what must be explicitly loaded to resume,
and what governance rules prevent candidate artifacts from silently becoming
deployed facts. It does not authorize model execution of any external system.
```

---
