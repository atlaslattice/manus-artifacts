---
title: Atlas Lattice KG — OpenAI Gift Lane
status: candidate
canon_status: not_canon
deployment_status: not_deployed
authority_scope: none
official_openai_claim: none
release_class: open_source_candidate
---

# Atlas Lattice KG — OpenAI Gift Lane

This package stages a candidate, open-source-friendly trust spine for making large human-AI archives more inspectable, provenance-aware, reviewable, and useful under model pressure.

It does **not** claim official OpenAI endorsement, integration, deployment, canon, or authority.

## Core loop

```text
retrieve → label → dream → graph → review → extract deltas → human-root ratifies if appropriate
```

## Why this helps

The package is designed to help model systems distinguish:

- raw source from summary;
- claim from evidence;
- contradiction from verdict;
- dreamstate from proof;
- GitHub receipt from canon;
- graph centrality from authority;
- model output from human-root decision.

## Package contents

```text
schemas/
  artifact.schema.yaml
  claim.schema.yaml
  receipt.schema.yaml
  edge.schema.yaml
  missing-receipt.schema.yaml
  contradiction.schema.yaml
  delta.schema.yaml
  dreamstate.schema.yaml
  review-queue-item.schema.yaml
  source-root-registry.schema.yaml

docs/
  bullshit-olympics-lint-suite.md
  gptdreampp-retrieval-game.md

fixtures/
  openai_eval_fixtures.v0.1.jsonl

reports/
  mirror-completion-report.md
```

## Boundaries

```text
CANON: no
DEPLOYMENT: no
AUTHORITY: none
OFFICIAL OPENAI CLAIM: none
```

## Keeper

```text
Best for OpenAI means useful under pressure:
source-aware,
claim-honest,
interop-ready,
graph-readable,
and allergic to false authority.
```
