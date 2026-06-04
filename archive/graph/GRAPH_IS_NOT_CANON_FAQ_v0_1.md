# Graph Is Not Canon FAQ v0.1

```text
STATUS: CANDIDATE FAQ — NOT CANON
DEPLOYMENT: none
AUTHORITY: none
PURPOSE: prevent graph centrality, clustering, and connectivity from being mistaken for truth, canon, or authority
```

## Core rule

```text
A graph edge is not a promotion.
A cluster is not canon.
A central node is not authority.
```

## What the graph does

The provenance graph helps the swarm and human reviewers:

- find related artifacts
- locate missing receipts
- trace source lineage
- detect contradictions
- identify duplicate or superseded materials
- prioritize review queues
- route artifacts to the correct reviewer lanes
- preserve how claims evolved over time

## What the graph does not do

The graph does not:

- decide truth
- ratify canon
- deploy systems
- grant authority
- prove ownership
- prove implementation
- replace raw sources
- replace human-root review
- turn model output into evidence

## Common failure modes

### 1. Centrality drift

```text
Failure: This node is highly connected, so it must be important/true/authoritative.
Correction: Centrality only means many edges point to or from the node. It increases review priority, not authority.
```

### 2. Cluster drift

```text
Failure: These artifacts cluster together, so they form a canon body.
Correction: A cluster is a review group. Canon requires explicit ratification.
```

### 3. Citation drift

```text
Failure: This artifact cites another artifact, so the cited claim is validated.
Correction: Citation is lineage or reference. It is not ratification.
```

### 4. Retrieval drift

```text
Failure: The graph retrieved this artifact, so it must be the current truth.
Correction: Retrieval surfaces candidates. Review establishes status.
```

### 5. Summary drift

```text
Failure: The summary node captures the raw source.
Correction: A summary is derived. It must point back to raw or explicitly mark raw_export_status != full_raw.
```

## Required graph metadata

Every high-value node should declare:

```yaml
canon_status: not_canon | candidate | ratified
deployment_status: not_deployable | experimental | deployed
authority_scope: none | advisory | review | ratification | execution
provenance_class: website_canon | github_receipt | notion_working | drive_file | chat_transcript | external_signal | unknown
raw_export_status: full_raw | partial_raw | summary_only | unavailable | unknown
review_status: unreviewed | in_review | reviewed | blocked | approved
```

## Review priority, not authority

The graph may increase review priority when it finds:

- contradictions
- unsupported claims
- public-facing risk
- canon-like language
- missing receipts
- private/public boundary risk
- duplicated or superseded artifacts
- model-output-only support

It may not increase authority.

## Keeper lines

```text
The graph maps.
The registry remembers.
The predicates constrain.
The receipts decide what can be reviewed.
The human-root decides what can be canon.
```

```text
Build the atlas OpenAI can reason over.
Do not crown the map.
```
