# ADR-0002 — Validation Hardening Strategy

> **Status:** CANDIDATE  
> **Artifact Type:** ADR  
> **Date:** 2026-05-28  
> **Related:** [Artifact ID and Lifecycle Contract](../knowledge-graph/ARTIFACT_ID_AND_LIFECYCLE_CONTRACT_v0_1.md), [Evidence standards](../evidence-standards.md), [ADR-0003](./ADR-0003-evidence-ledger-adoption.md)

## Context

Atlas Lattice is shifting from loosely linked candidate artifacts toward a machine-checkable public archive. As the artifact count grows, manual review alone is not enough to catch ID drift, provenance gaps, lifecycle-state mistakes, or missing trust metadata.

Validation hardening is needed so that contributor changes fail early when they break stable identifiers, provenance expectations, or lifecycle constraints. This is especially important for governance-critical documents, machine-readable registries, and AI-built evidence claims.

## Decision

We will implement and maintain Python validation scripts for three core classes of checks:

1. **ID checks** for uniqueness, required fields, and registry integrity.
2. **Provenance checks** for evidence records, source-path presence, and receipt completeness.
3. **Lifecycle checks** for candidate, review, deprecation, and ratification state transitions.

These validators should run in GitHub Actions and remain simple enough to inspect directly in-repo.

## Consequences

### Positive

- Metadata regressions are caught before merge.
- Contributors get a clearer contract for adding artifacts, evidence, and trust-state changes.
- Review effort shifts from basic hygiene to actual adjudication.

### Negative

- Contributors must maintain machine-readable fields with more discipline.
- Validation coverage will expand over time, which may temporarily increase CI failures during backfill waves.

### Neutral / follow-on

- Additional receipt types may require validator updates.
- Some legacy artifacts will remain partially compliant until backfill work is complete.

## Alternatives considered

### 1. Human review only

Rejected because it does not scale and makes drift easy to miss.

### 2. External validation service

Rejected for now because local, transparent Python validators are easier to audit and maintain.

### 3. One monolithic validator for everything

Rejected because smaller focused validators are easier to evolve and reason about.
