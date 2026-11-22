# Atlas Intelligence ↔ DragonSeek v1.6.2 — implementation crosswalk
Date: 2026-10-11. Status: AUDITED SOURCE · PROPOSED CROSS-REPO INTEGRATION · NO DEPLOYED INTEROPERABILITY

## Source now recovered
[Atlas Intelligence](https://github.com/atlaslattice/Atlas-Intelligence) was successfully uploaded to GitHub main, providing server.ts, src/App.tsx, firestore.rules, src/lib/lcp.ts, src/lib/verifier.ts, src/lib/agent-utils.ts, and docs/UNIFIED_ARCHITECTURE.md. Original files remain owned by that repository.

## Existing interfaces
- Element 145/ATLAS is currently **Gemini-primary**, according to README.md. Multi-provider routing is only scaffolded; do not claim GPT routing is operational.
- `src/lib/verifier.ts` performs lexical checks for claim labels, flagged empirical overclaims and inline URL citations. This is useful scaffolding, not robust factual/constitutional verification.
- `src/lib/lcp.ts` describes INGEST/ACTIVATE/ROUTE/SYNTHESIZE, but INGEST matches literal house names and assigns constant confidence 0.85; it does **not** yet implement embedding similarity or real cross-domain understanding.
- `src/lib/agent-utils.ts` creates up to twelve user-scoped Gemini house agent records in Firestore; this is not evidence autonomous analysis tasks ran.
- `firestore.rules` represents source-level policies; deployments and real authorization tests remain unverified.
- `src/App.tsx` uses a dedicated epistemic system prompt and verification-panel UI. Model outputs are not proofs of correctness.

## Shared DragonSeek constitutional integration target
1. Embed complete source files with integrity receipts; current candidate uses a Git blob SHA-1 manifest, not yet a signed SHA-256 release manifest.
2. Implement `constitution.lookup(id,version)` and `constitution.search(text)` with citations to original documents. Preserve conflict sets and select applicable jurisdiction explicitly.
3. Add pre-execution policy gating in the OS for tool permissions, privacy, physical hazards and human consent, with defaults fail-closed for undefined capabilities. Text prompts and regex validators alone are insufficient.
4. Add post-execution verification, structured TransparencyPackets, per-source uncertainty and traceable receipts. Partition measured/estimated/simulated/proposed claims.
5. Integrate with an AI adapter after permission and credentials configuration; no weights modified. For future US Atlas ARI, GPT may be selected as primary provider via a new branch; DragonSeek CN can remain separate.
6. Local audit and read-only dashboard must work offline without live provider credentials.

## Corpus reconciliation outstanding
April 29 registry and Aluminum OS website have conflicting INV-0 definitions. DeepSeek ratification is user-reported in this conversation, no independently verified signed resolution or exact document-version scope has been provided. Preserve both candidates with linked provenance.
Current PR #304 contains 41 invariant entries and 102 doctrine entries, which are all explicitly defined objects in the Aluminum OS website source. That source calls the invariant total 43, leaving a documented two-item counting discrepancy rather than grounds to invent two entries. The April registry was archived and verified by exact reconstruction. The user set active INV-0 = Nothing Dies, preserving the historical System Integrity variant. PR remains DRAFT pending executable Python test evidence; initial workflow jobs failed before returning steps.

## Verification checklist for graduation
- 100% local corpus coverage and hashes validated
- Registry contradiction tests (e.g., INV-0) pass and never overwrite
- All privilege escalation, external write, and high-risk action tests fail closed unless authorized
- Offline dashboard + registry API smoke tests
- AI adapter citation and refusal to invent nonexistent doctrines
- Explicit Mandarin-first locale and Arabic RTL smoke tests
- Browser-live feed receipt testing remains separate from constitutional tests

No government, vendor, or council operational approval is implied by published code.
