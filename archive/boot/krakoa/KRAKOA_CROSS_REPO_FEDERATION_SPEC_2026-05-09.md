# Krakoa Cross-Repo Federation Spec

```text
STATUS: KRAKOA FEDERATION SPEC — CANDIDATE / NOT RATIFIED CANON
DATE: 2026-05-09
ROOT REPO: atlaslattice/manus-artifacts
PURPOSE: Wire relevant Atlas repositories into a provenance-backed federation layer without creating hidden runtime authority.
PROMOTION: Requires human-root review before ratified canon or runtime execution.
```

## 0. Evidence Boundary

Krakoa does **not** mean:

- hidden model-to-model communication;
- autonomous authority;
- legal authority;
- military command authority;
- weapons release authority;
- classified system claims;
- automatic cross-repo execution;
- canon without human-root review.

Krakoa means:

> A visible, artifact-backed federation layer for linking related repos, agents, governance boundaries, provenance records, boot packets, and implementation maturity levels.

## 1. Prime Directive

```text
Federate the archives.
Do not erase the boundaries.

Link the repos.
Do not merge their authority.

Memory may inform action.
Memory cannot authorize action.
```

## 2. Current Relevant Repos

### Root governance / fossil record

```text
atlaslattice/manus-artifacts
```

Role:

```text
Council Brain index, seat specs, incident reviews, hardening audits, culture layer, Krakoa manifest, cross-repo governance records.
```

### Parser / RAG / memory substrate

```text
atlaslattice/sheldonbrain-rag-api
```

Role:

```text
Parser, embeddings/RAG, GPTBrain reference implementation, memory object scaffolding, artifact/claim ledgers, future Krakoa adapter hooks.
```

### Tucker GPT / Gemini defense interface

```text
atlaslattice/tucker-gemini-GPT-
```

Role:

```text
Pentagon-facing / defense-interface translation lane; currently provenance-backed and boot-visible, not runtime-authorized.
```

### Military AI ethics / defense boundary repo

```text
atlaslattice/military-ai-ethics
```

Role:

```text
Domain-specific guardrails for defense/war/military AI ethics: human authority, no autonomous targeting, no official claims without provenance.
```

### Existing Krakoa code references inside root fossil record

```text
codebases/atlas-vault/krakoa_mcp_server.py
codebases/atlas-vault/krakoa_keep_module.py
```

Role:

```text
Earlier Krakoa/Atlas Vault implementation artifacts preserved in manus-artifacts. These are source lineage, not automatic production runtime.
```

## 3. Federation Model

Krakoa is a visible link layer with four classes of wiring:

```yaml
wiring_classes:
  provenance:
    meaning: repo/file/commit/source-lineage links
    executable: false
  boot_visibility:
    meaning: artifacts appear in boot packets, ledgers, or indexes
    executable: false
  adapter_candidate:
    meaning: an adapter/spec/test plan exists
    executable: false by default
  runtime_integration:
    meaning: CI-tested invocation path exists
    executable: only with human-root approval and audit logs
```

## 4. Maturity Ladder

```text
K0 — Mentioned / user-reported
K1 — Repo provenance note exists
K2 — Boot-visible in Council/GPTBrain/Sheldonbrain records
K3 — Adapter spec exists
K4 — Tests / CI validate adapter behavior
K5 — Human-root approved limited runtime invocation
K6 — Production interface with audit logs, revocation controls, and public boundary docs
```

Current repo states:

```yaml
manus-artifacts: K2-K3 governance/root federation
sheldonbrain-rag-api: K2-K3 parser/reference implementation substrate
tucker-gemini-GPT-: K2 boot-visible provenance-backed artifact
military-ai-ethics: K1-K2 defense guardrail target
```

## 5. Cross-Repo Contract

Every Krakoa-aware repo should contain one of:

```text
KRAKOA_WIRING.md
KRAKOA_FEDERATION.md
KRAKOA_DEFENSE_BOUNDARY.md
```

Each document must state:

```text
STATUS
ROLE
UPSTREAM REPOS
DOWNSTREAM REPOS
WHAT THIS REPO MAY DO
WHAT THIS REPO MUST NOT DO
MATURITY LEVEL
HUMAN-ROOT / APPROVAL BOUNDARY
```

## 6. Shared Non-Negotiable Guardrails

```text
NO HIDDEN CANON
NO SILENT CROSS-REPO AUTHORITY
NO AUTONOMOUS TARGETING
NO WEAPONS RELEASE AUTHORITY
NO OFFICIAL POSITION WITHOUT HUMAN APPROVAL
NO CLASSIFIED CLAIMS WITHOUT SOURCE
NO HIGH-IMPACT FORWARDING WITHOUT PROVENANCE
NO DELETING DIVERGENCE TO FORCE SYNTHESIS
```

## 7. Routing Rules

```text
manus-artifacts receives governance and synthesis records.
sheldonbrain-rag-api receives parser/runtime/reference implementation hooks.
tucker-gemini-GPT- receives defense-interface translation constraints.
military-ai-ethics receives defense-specific ethical guardrails.
```

Recommended path for a defense-facing artifact:

```text
raw user/project context
→ manus-artifacts provenance record
→ sheldonbrain parser / claim extraction
→ GPTBrain calibration
→ Tucker defense translation draft
→ military-ai-ethics guardrail review
→ S2/S4/S6/S7 review as needed
→ human-root approval
→ only then external forwarding or runtime invocation
```

## 8. Standard Krakoa Header

```text
STATUS: KRAKOA-AWARE ARTIFACT — NOT CANON BY DEFAULT
REPO ROLE: [root governance / parser / agent / guardrail / implementation]
MATURITY: K0-K6
SOURCE LINEAGE: [paths / commits / issues]
EXECUTION AUTHORITY: NONE UNLESS EXPLICITLY APPROVED
HUMAN-ROOT REVIEW: REQUIRED FOR CANON OR HIGH-IMPACT ACTION
```

## 9. Immediate Wiring Plan

```text
[x] Create root Krakoa federation spec in manus-artifacts.
[ ] Add Krakoa wiring note to sheldonbrain-rag-api.
[ ] Add Krakoa wiring note to tucker-gemini-GPT-.
[ ] Add defense-boundary Krakoa note to military-ai-ethics.
[ ] Create central issue tracking cross-repo wiring status.
[ ] Add future adapter/test-plan tasks after current PR #20 hardening stabilizes.
```

## 10. Strongest Safe Claim

> Krakoa is the Atlas cross-repo federation layer: it makes related repositories mutually visible through provenance, boot records, and explicit maturity levels while preserving human-root authority, repo boundaries, and non-autonomous execution constraints.

## 11. Final Motto

```text
The island connects.
The island does not command.

The gates are visible.
The roots are human.
The archive remembers.
The labels stay sharp.
```
