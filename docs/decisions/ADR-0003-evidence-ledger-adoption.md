# ADR-0003 — Evidence Ledger Adoption

> **Status:** CANDIDATE  
> **Artifact Type:** ADR  
> **Date:** 2026-05-28  
> **Related:** [AI evidence ledger schema](../knowledge-graph/ai_evidence_ledger.schema.v0_1.json), [Evidence ledger index](../evidence/README.md), [Ratification and Trust Flow](../RATIFICATION_AND_TRUST_FLOW.md)

## Context

Atlas Lattice includes flagship artifacts that were designed, assembled, or materially advanced through conversational AI collaboration. Public claims about those artifacts need traceable evidence so that readers can distinguish between unsupported narrative, candidate evidence, and fully reviewed provenance.

Without a ledger, AI-built claims remain difficult to audit, compare, or ratify. The repository already has candidate governance around trust states; it now needs a repeatable evidence pattern that contributors can use across code, governance, and research artifacts.

## Decision

Atlas Lattice adopts the AI evidence ledger schema as the provenance mechanism for all AI-built flagship artifacts. Each qualifying artifact should receive at least one evidence entry that records:

- the artifact being claimed
- the claim being supported
- the evidence source or receipt
- the AI systems involved
- the verification or review method
- the current trust limitations

The working evidence-entry format in `docs/evidence/` must stay aligned to schema version `0.1` and remain eligible for future normalization into the broader knowledge-graph ledger.

## Consequences

### Positive

- AI-built claims become inspectable and reviewable.
- Evidence can be backfilled domain by domain without blocking publication of all other artifacts.
- Future ratification requests can reference a stable provenance layer.

### Negative

- Contributors take on extra documentation work for flagship artifacts.
- Some legacy claims will remain under-evidenced until backfill catches up.

### Neutral / follow-on

- Additional evidence types may be introduced as new classes of receipts mature.
- Coverage dashboards and CI policies will need periodic updates.

## Alternatives considered

### 1. Keep evidence only in narrative Markdown receipts

Rejected because it is difficult to query, validate, and compare systematically.

### 2. Delay evidence until full ratification

Rejected because candidate-stage provenance is exactly where claims need structure.

### 3. Require full formal adjudication before any evidence entry exists

Rejected because evidence collection should precede, not wait on, adjudication.
