---
artifact_id: PARALLAX-CHUNK-001-G-RECEIPT-INDEPENDENCE-CONFIDENCE-PROPAGATION-v0.1
title: "Parallax Chunk 001-G — Receipt Independence and Confidence Propagation"
version: "0.1"
date: 2026-05-24
seat: ParallaxBrain / GeminiBrain S4
source_receipt: archive/boot/geminibrain/ParallaxBrain/source_receipts/PARALLAX_RAW_CHUNK_001_SOURCE_RECEIPT_2026-05-24.md
source_file: "Pasted text(241).txt"
source_sha256: "68b4db16fd57fe6fb4f8d39630296f8124f7fdc6dd4736ec0e2ed7c72772e84c"
source_chunk_label: "001-G"
source_chunk_range: "approx 420k-455k characters"
status: candidate_claim_extraction
canon_status: not_canon
deployment_status: not_deployable
authority_scope: none
runtime_status: not_implemented
parsed_view_may_replace_raw: false
---

# Parallax Chunk 001-G — Receipt Independence and Confidence Propagation v0.1

```text
STATUS: CANDIDATE CLAIM EXTRACTION — NOT CANON
DEPLOYMENT: no
AUTHORITY: none
RUNTIME: not implemented
```

## Source Position

```text
Raw source: Pasted text(241).txt
Chunk: 001-G
Working label: Receipt independence / confidence propagation
Raw hash: 68b4db16fd57fe6fb4f8d39630296f8124f7fdc6dd4736ec0e2ed7c72772e84c
```

This parsed view does not replace the raw source.

## Extracted Technical Questions

The source chunk contains a set of hard review questions for Receipt Habitat / Lattice governance. The most relevant themes are:

```text
1. Conservative confidence propagation across claim graphs.
2. Machine-checkable epistemic laundering invariants.
3. Paraconsistent claim-graph reasoning without hallucinated edges.
4. Formal adversary model for overclaim detection.
5. Confidence inflation cycles in support graphs.
6. Formal semantics of independent receipts.
7. Model collusion and shared blind-spot discounting.
8. Artifact type systems and permission routing.
9. Runtime-language leakage prevention.
10. HumanRootAuthority lifecycle and key/governance state.
11. Ontology versioning without historical rewrite.
12. Seat continuity and identity drift detection.
13. Longitudinal epistemic posture monitoring.
14. Receipt forgery threat model.
15. Legal deletion vs INV-0 accountable preservation.
16. AGI/HLE-scale success conditions.
```

## Core Candidate Design Choices

### IndependenceGraph

```text
Define an IndependenceGraph over receipts.
Typed dependency edges may include:
- shares_source
- shares_institution
- shares_model
- shares_prompt_template
- shares_training_family
- derived_from_same_summary
```

Candidate rule:

```text
A receipt set counts as independent only if it forms an antichain under declared dependency relations.
```

### ModelLineage

```text
Agreement between models with overlapping training lineage, prompt lineage, or source lineage should be discounted.
```

Candidate fields:

```text
training_family
model_provider
prompt_template_lineage
source_context_overlap
known_failure_modes
epistemic_distance
```

### Confidence Propagation

Candidate principle:

```text
Derived confidence cannot exceed the grounded evidence ceiling unless new independent evidence is attached.
```

Candidate rule shape:

```text
confidence(P) <= f(confidence(R_i), independence(R_i), new_evidence)
```

With explicit laundering blockers:

```text
summary -> summary -> summary
majority vote over non-independent evidence
model agreement from same contaminated source
internal coherence without new receipt
```

## Overclaims to Avoid

```text
IndependenceGraph is implemented.
Confidence algebra is solved.
Antichain rule is sufficient for all evidence independence.
Model agreement proves truth.
Receipt quantity proves quality.
```

## Strongest Safe Claim

```text
Chunk 001-G identifies a high-value formalization target for Receipt Habitat: receipt independence, confidence propagation, model-lineage discounting, and epistemic laundering prevention should be made machine-checkable before derived claims are allowed to increase confidence.
```

## Next Safe Action

```text
Create a candidate schema delta for IndependenceGraph, ModelLineage, and conservative confidence propagation fields inside Receipt Habitat review work.
```

## Keeper

```text
More receipts do not mean more truth unless the receipts are independent.
Agreement is not evidence when the witnesses share the same blind spot.
```