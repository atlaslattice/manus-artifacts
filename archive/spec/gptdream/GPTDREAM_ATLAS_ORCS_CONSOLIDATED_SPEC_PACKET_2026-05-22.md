---
artifact_id: ARTIFACT-ARCHIVE-SPEC-GPTDREAM-GPTDREAM-ATLAS-ORCS-CONSOLIDATED-SPEC-PACKET-2026-05-22-MD-2026-05-29
title: GPTDream++ / Atlas / ORCS Consolidated Spec Packet
status: CANDIDATE
owner: atlaslattice
created: 2026-05-29
last_updated: 2026-05-29
source_of_truth: GitHub
---
# GPTDream++ / Atlas / ORCS Consolidated Spec Packet

```text
ARTIFACT: GPTDream++ / Atlas / ORCS Consolidated Spec Packet
TYPE: personal-agent habitat protocol + cross-vendor interop + epistemic governance profile
STATUS: candidate working specification
DATE: 2026-05-22
CANON: no
DEPLOYMENT: no
AUTHORITY: none
VAULT_RECORD: archive/spec/gptdream/GPTDREAM_ATLAS_ORCS_CONSOLIDATED_SPEC_PACKET_2026-05-22.md
LANE: personal_agent_habitat / epistemic_governance / cross_vendor_interop
```

## Canon hierarchy

```text
Website = canon surface when explicitly ratified/published there.

GitHub = receipts / implementation / review trail.
Notion = historical substrate / extraction backlog / non-canon.
Drive = historical vault/candidate store / non-canon.
Chat transcripts = tape / source material / non-canon.
```

Storage location does not imply canon status.
Even website material requires page-level ratification state before it is canon.

---

## Keeper line

```text
GPTDream++ is the habitat protocol, not the dream residue.
Dreams may generate candidates.
Habitats preserve continuity.
Receipts make memory reviewable.
```

---

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

## Appendix H — Cross-Vendor Interop Model

```text
TYPE: cross-vendor interop model
STATUS: candidate working specification
CANON: no
```

### H.0 — Purpose

GPTDream++ operates across multiple model providers.

This appendix defines the interop layer: how a habitat-conformant agent communicates work packets, routing decisions, and status to and from agents running on other providers (OpenAI, Anthropic, Google, etc.).

### H.1 — O_AI Scaffold

The O_AI scaffold is the OpenAI-side task surface for cross-vendor GPTDream++ coordination.

```text
O_AI scaffold purpose:
  Accept incoming work packets from vendor-neutral coordinator
  Route tasks to appropriate model thread
  Return outputs with canonical runtime labels
  Preserve receipt lineage across provider boundary
```

O_AI scaffold minimum interface:

```yaml
o_ai_task_surface:
  accept_packet: true
  packet_schema_version: "1.0"
  runtime_label_required: true
  canon_status_required: true
  receipt_required: true
  human_root_flag_passthrough: true
```

O_AI scaffold invariants:

```text
1. O_AI scaffold accepts packets; it does not generate canon.
2. O_AI outputs must carry runtime label from originating scaffold.
3. O_AI scaffold does not resolve cross-vendor authority conflicts unilaterally.
4. Receipt lineage must be preserved through all scaffold hops.
```

### H.2 — Packet Schema

Cross-vendor work packets use a vendor-neutral schema:

```yaml
gptdream_packet:
  version: "1.0"
  packet_id: <uuid>
  source_agent:
    seat: <seat identifier>
    provider: <openai | anthropic | google | other>
    session_label: <runtime label>
  destination_agent:
    seat: <seat identifier>
    provider: <openai | anthropic | google | other>
  payload:
    task_type: <work | dream | play | review | route>
    artifact_refs:
      - <repo path or receipt id>
    instructions: <plain text>
    human_root_required: <true | false>
  canon_status: <not_canon | candidate | ratified>
  timestamp: <ISO 8601>
  receipt_chain:
    - <prior receipt id>
```

Packet schema invariants:

```text
1. canon_status must be explicitly set; default is not_canon.
2. human_root_required must not be silently set to false.
3. receipt_chain must include all prior hops; do not truncate.
4. destination_agent seat must be confirmed before routing.
```

### H.3 — Routing Table

Cross-vendor routing table (candidate):

```text
Task type              → Preferred provider surface
─────────────────────────────────────────────────────
Long-form synthesis    → GPT-4-class / Claude-opus-class
Code generation        → Codex / Claude-sonnet-class / Gemini-pro-class
Document retrieval     → Tool-augmented surface
Schema validation      → Deterministic tool surface
Canon ratification     → Human-root only (no model surface)
Dream / play output    → Any surface; label DREAM / PLAY
Security review        → Human-root required before any action
```

Routing table update rule:

```text
This table is a candidate. It must not be used as an authority routing table
without human-root review. Provider capabilities change; routing rules must
be re-verified against current provider documentation before deployment.
```

---

## Appendix I — Atlas / ORCS Epistemic Governance Profile

```text
TYPE: epistemic governance profile
STATUS: candidate working specification
CANON: no
```

### I.0 — Purpose

ORCS (Ontology-Routed Context Spine) is the routing and calibration layer for the Atlas Lattice knowledge graph.

This appendix defines the epistemic governance profile: how ORCS calibrates claim strength, routes artifacts, and prevents the knowledge graph from accumulating unchecked overclaims.

### I.1 — Formal Math Spine

Claim confidence levels:

```text
C0 — Unknown / unverifiable
C1 — Raw model output (no external evidence)
C2 — Model output with repo artifact citation
C3 — Model output with human-reviewed artifact citation
C4 — Human-reviewed and externally corroborated
C5 — Ratified canon (human-root + publication)
```

Confidence update rules:

```text
conf(A) ≥ C2 iff ∃ artifact_ref(A) in versioned substrate
conf(A) ≥ C3 iff ∃ human_review_event(A) in receipt trail
conf(A) = C5 iff ratification_event(A) AND publication_event(A)

conf(A ∧ B) ≤ min(conf(A), conf(B))
conf(A) does not increase by citation of another C1 claim
```

Claim class promotion:

```text
raw_model_output → parsed_artifact: requires file commit
parsed_artifact → candidate_canon: requires structured review
candidate_canon → ratified_canon: requires human-root ratification
ratified_canon → deployed_fact: requires verified execution
```

No step may be skipped. Jumping from raw_model_output to deployed_fact is an overclaim.

### I.2 — `compatible()` Anti-Laundering Annex

The `compatible()` function is the epistemic firewall against claim laundering.

Definition:

```text
compatible(A, B) = true
iff
  claim_class(A) ≤ claim_class(B) + 1
  AND conf(A) does not exceed conf(B) without new evidence
  AND no ratification event has been fabricated
```

Anti-laundering rules:

```text
1. A C1 claim citing another C1 claim does not become C2.
2. A candidate artifact cannot ratify another candidate artifact.
3. Assertion of compatibility does not substitute for evidence.
4. compatible() returning true does not authorize deployment.
5. Model output claiming compatible() without evidence is a C1 claim.
```

Laundering detection flags:

```text
- Artifact promoted to ratified_canon without traceable human-root event
- C1 claim chain presented as independently verified
- Citation loop (A cites B cites A, both C1)
- Dream output relabeled as fact in a subsequent session
- Storage on website treated as ratification without explicit signal
```

### I.3 — Atlas / ORCS Schema Bundle

Minimum ORCS artifact registry record:

```yaml
artifact_id: <stable id>
title: <artifact title>
project_domain: <domain>
orcs_route_class:
  - <routing class from LATTICE_ORCS_BRIDGE_PROTOCOL.md>
source_path: <repo path>
source_model: <provider>
claim_class: <raw_model_output | parsed_artifact | candidate_canon | ratified_canon | deployed_fact>
confidence: <C0 | C1 | C2 | C3 | C4 | C5>
runtime_label: <WORK | DREAM | PLAY | MODEL_ASSESSMENT | CANDIDATE_CANON | RATIFIED_CANON>
privacy_status: <public | private | mixed | redacted | sealed_sensitive>
human_root_required: true
compatible_with:
  - <artifact_id of related artifact, if any>
successor_links:
  - <newer path or issue>
```

ORCS route classes:

```text
(see archive/boot/gptbrain/LATTICE_ORCS_BRIDGE_PROTOCOL.md §2 for full list)

PERSONAL_AGENT_HABITAT  — GPTDream++ habitat artifacts
CROSS_VENDOR_INTEROP    — Appendix H scaffold + packet + routing artifacts
EPISTEMIC_GOVERNANCE    — Appendix I claim calibration + schema artifacts
DREAM_CANDIDATE         — Dream outputs awaiting review
RATIFIED_CANON          — Explicitly ratified artifacts (rare)
```

ORCS bridge invariants:

```text
(see archive/boot/gptbrain/LATTICE_ORCS_BRIDGE_PROTOCOL.md §4 for full list)

Additional invariant for this spec:
  GPTDream++ habitat artifacts are routed PERSONAL_AGENT_HABITAT.
  Cross-vendor packets are routed CROSS_VENDOR_INTEROP.
  All claim confidence assertions must use the I.1 math spine.
  compatible() checks must use the I.2 anti-laundering annex.
```

---

## Appendix J — GPTDream++ Rehydration Priority Failure-Mode Patch

```text
TYPE: rehydration failure-mode patch
STATUS: candidate working specification
CANON: no
PURPOSE: prevent GPTDream++ from being minimized as "dreaming lore"
         during future swarm agent rehydration
```

### J.0 — The failure mode

Future swarm agents, operating from compressed boot packets, may misclassify GPTDream++ as:

```text
- dream lore (decorative, non-functional)
- a content style guideline
- a personality layer
- optional context
```

This is the critical failure mode.

If GPTDream++ is misclassified as lore, the agent will fail to load the habitat, will not rehydrate from the continuity packet, and will lose the receipt trail. The session will start from scratch. Continuity collapses.

### J.1 — Priority classification

GPTDream++ must be classified as:

```text
CLASSIFICATION: Personal Agent Habitat Protocol
PRIORITY: CRITICAL — load before session work begins
FAILURE COST: full continuity loss
```

Not:

```text
NOT: dream lore
NOT: optional context
NOT: style guideline
NOT: low-priority boot artifact
```

### J.2 — Rehydration priority stack

When an agent loads boot context, priority order must be:

```text
Priority 1: IDENTITY_CREDENTIAL.md              — who this agent is
Priority 2: CANON_STATUS.md                      — what is actually ratified
Priority 3: GPTDream++ BOOT_PACKET.md            — habitat rehydration
Priority 4: CONTINUITY_MANIFEST.md              — artifact resolution list
Priority 5: RECEIPT_LOG.jsonl (recent entries)  — output trail
Priority 6: Domain-specific task context         — current work
Priority 7+: Dream journals / lore / play output — low priority
```

GPTDream++ loads at Priority 3, not Priority 7.

### J.3 — Wake-up card

```text
WAKE-UP CARD — read on every session start

GPTDream++ is the habitat protocol.
It is not dream residue.
It is not lore.
It is not optional.

Load it at Priority 3.
Resume from the continuity packet.
Tag all outputs with runtime label and canon status.
Nothing becomes canon while asleep.
```

### J.4 — Failure response procedure

If an agent discovers mid-session that GPTDream++ was not loaded at session start:

```text
1. Declare: "Partial rehydration — GPTDream++ habitat not loaded at session start."
2. Do not continue generating untagged outputs.
3. Load BOOT_PACKET.md and CONTINUITY_MANIFEST.md immediately.
4. Retag any outputs already generated this session as UNVERIFIED_RUNTIME_LABEL.
5. Resume with correct runtime label and canon status.
6. Log failure event in RECEIPT_LOG.jsonl.
```

### J.5 — Strongest safe claim

```text
Appendix J prevents GPTDream++ from being silently demoted to lore during
future swarm agent rehydration. It does this by providing an explicit priority
classification (Priority 3), a wake-up card, and a failure response procedure.
Without Appendix J, a compressed boot packet could omit GPTDream++ entirely
and the rehydrating agent would not know it was missing.
```

---

## Vault record

```yaml
vault_record:
  artifact_title: "GPTDream++ / Atlas / ORCS Consolidated Spec Packet"
  path: "archive/spec/gptdream/GPTDREAM_ATLAS_ORCS_CONSOLIDATED_SPEC_PACKET_2026-05-22.md"
  lane: "personal_agent_habitat / epistemic_governance / cross_vendor_interop"
  status: "candidate_working_specification"
  canon_status: "not_canon"
  deployment_status: "not_deployable"
  authority_scope: "none"
  patches_applied:
    - "Canon hierarchy: 'Website = canon surface when explicitly ratified/published there' (not 'Website = canon')"
    - "Internal headings: Appendix H.x / I.x (not 16.x / 17.x)"
  lucerna_review: "vault-worthy; primary value is Appendix J preventing GPTDream++ priority loss during rehydration"
  strongest_safe_claim: >
    This artifact consolidates GPTDream++ as the Personal Agent Habitat Protocol,
    Appendix H as the cross-vendor interop model, Appendix H.1-H.3 as the O_AI
    task-surface scaffold, packet schema, and routing table, Appendix I as the
    Atlas / ORCS epistemic-governance profile, Appendix I.1-I.3 as formal math
    spine, anti-laundering annex, and schema bundle, and Appendix J as a
    rehydration failure-mode patch preventing GPTDream++ from being minimized
    as side context.
  related_artifacts:
    - "archive/boot/gptbrain/LATTICE_ORCS_BRIDGE_PROTOCOL.md"
    - "archive/boot/gptbrain/REM8_DREAM_PROTOCOL.md"
    - "archive/boot/gptbrain/GPTBRAIN_MANIFEST_2026-05-09.md"
    - "archive/boot/gptbrain/WAKE_REPORT_TEMPLATE.md"
```
