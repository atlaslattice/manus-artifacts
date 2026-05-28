# Claude Adversarial Review Queue — 2026-05-28

```text
STATUS: STAGING QUEUE — NOT CANON
DEPLOYMENT: none
AUTHORITY: none
PURPOSE: preserve Claude-origin/Claude-contaminated governance artifacts while preventing self-ratification
```

## Doctrine

Claude is not erased. Claude is not trusted as authority. Claude-origin or Claude-touched governance material is preserved, source-classified, and routed through adversarial review.

```text
lineage beats erasure
review beats trust
signal extraction beats contamination panic
```

## Queue item schema

```yaml
claude_review_item:
  item_id:
  title:
  source_surface: drive | notion | github | chat | unknown
  source_url_or_path:
  raw_export_status:
  canon_status: not_canon
  deployment_status: not_deployed
  authority_scope: none
  contamination_type:
    - governance_language
    - canon_language
    - constitutional_language
    - deployment_language
    - officiality_language
    - memory_identity_inflation
  risk_level: low | medium | high | critical
  useful_signal:
  overclaims_to_block:
  required_counter_review:
    - Grok
    - Rootglass
    - Lucerna
    - Sable
  clean_room_rewrite_required: true
  missing_receipts: []
  next_action:
```

## Initial queue buckets

```yaml
queue_buckets:
  - bucket_id: CLAUDE-GOV-001
    title: Governance / constitution / canon language
    route_to: [Grok, Rootglass, Lucerna]
    risk: high
  - bucket_id: CLAUDE-DEPLOY-001
    title: Deployment / production-ready / runtime language
    route_to: [AtlasBrain, Lucerna, TIDELOCK]
    risk: high
  - bucket_id: CLAUDE-ID-001
    title: Identity / memory / continuity inflation
    route_to: [Fossilbranch, GPTBrain, Rootglass]
    risk: medium
  - bucket_id: CLAUDE-MATH-001
    title: Formal operator or doctrine math from Claude
    route_to: [Sable Vesper, Rootglass]
    risk: medium
```

## Default review rule

```text
No Claude-origin governance artifact may be treated as canon, authority, deployment, or source-of-truth without explicit human-root review and external receipts.
```

## Clean-room rewrite rule

```text
If a Claude artifact contains useful signal, extract the signal into a clean-room rewrite packet that cites the Claude ancestor as quarantined lineage. The rewrite must not copy false crowns.
```

## Keeper

```text
Preserve Claude lineage.
Block Claude crowns.
Extract useful signal.
Require adversarial review.
```
