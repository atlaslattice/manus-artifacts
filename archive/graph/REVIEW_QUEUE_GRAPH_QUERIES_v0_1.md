# Review Queue Graph Queries v0.1

```text
STATUS: CANDIDATE QUERY SET — NOT CANON
DEPLOYMENT: none
AUTHORITY: none
PURPOSE: Define first review-priority queries for the Atlas provenance-first knowledge graph.
```

## Core rule

```text
The graph finds review targets.
The graph does not decide truth.
The graph does not promote canon.
The graph does not grant authority.
```

## Priority queries

### 1. Canon-language mismatch

Find artifacts or claims that use canon-like language but are not ratified.

```cypher
MATCH (n)
WHERE n.canon_status <> 'ratified'
  AND (toLower(n.title) CONTAINS 'canon'
       OR toLower(n.strongest_safe_claim) CONTAINS 'ratified'
       OR toLower(n.strongest_safe_claim) CONTAINS 'production')
RETURN n
```

### 2. Claude-originated governance claims lacking adversarial review

```cypher
MATCH (c:Claim)
WHERE c.claim_owner = 'Claude'
  AND c.claim_type = 'governance_claim'
  AND NOT (c)-[:NEEDS_REVIEW_BY]->(:PersonOrSeat {name:'Grok_or_adversarial_stress'})
RETURN c
```

### 3. Claims supported only by model output

```cypher
MATCH (c:Claim)<-[:SUPPORTS]-(a:Artifact)
WITH c, collect(a.provenance_class) AS classes
WHERE all(x IN classes WHERE x = 'model_output')
RETURN c, classes
```

### 4. IP concepts without raw source pointer

```cypher
MATCH (c:Claim)
WHERE c.claim_type = 'IP_claim'
  AND c.raw_export_status IN ['summary_only','unavailable','unknown']
RETURN c
```

### 5. Duplicate or superseded D-Φ variants

```cypher
MATCH (a:Artifact)
WHERE toLower(a.title) CONTAINS 'd-φ'
   OR toLower(a.title) CONTAINS 'd-phi'
OPTIONAL MATCH (a)-[:SUPERSEDES|DUPLICATES]-(b:Artifact)
RETURN a, b
```

### 6. External-science signals with unsupported leap risks

```cypher
MATCH (c:Claim)
WHERE c.claim_type = 'external_signal_claim'
  AND size(c.forbidden_wording) > 0
RETURN c
```

### 7. Review queue by blocked status

```cypher
MATCH (n)
WHERE n.review_status IN ['blocked','in_review','unreviewed']
RETURN n.review_status, count(n) AS count
ORDER BY count DESC
```

## Human-readable first dashboard

Before Neo4j or RDF export, a simple Markdown dashboard should list:

```text
1. Highest-risk canon-language mismatch artifacts
2. Claude-originated governance claims needing adversarial review
3. IP claims lacking raw source pointers
4. Duplicate / superseded D-Φ documents
5. External-science signals with unsupported leap risks
6. Summary-only packets being treated like raw lineage
```

## Keeper line

```text
The graph shows where review is needed.
It does not decide what is true.
```
