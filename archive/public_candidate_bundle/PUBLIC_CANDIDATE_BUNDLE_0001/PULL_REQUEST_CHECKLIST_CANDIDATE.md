# Pull Request Checklist Candidate

```text
STATUS: PR CHECKLIST CANDIDATE — NOT CANON
DEPLOYMENT: none
AUTHORITY: none
```

## Required PR packet

```yaml
pr_packet:
  summary:
  affected_paths: []
  source_refs: []
  raw_export_status:
  canon_status: not_canon
  deployment_status: not_deployed
  authority_scope: none
  public_safety_check: pass | needs_review | blocked
  missing_receipts: []
  review_lanes: []
```

## Checklist

- [ ] The PR does not claim canon.
- [ ] The PR does not claim deployment.
- [ ] The PR does not grant authority.
- [ ] Source refs are included.
- [ ] Raw export status is declared.
- [ ] Missing receipts are listed.
- [ ] Public-safety status is declared.
- [ ] Claude-origin material, if present, is routed to adversarial review.
- [ ] OpenAI/GPTBrain output, if present, is not framed as official OpenAI endorsement.
- [ ] Graph edges are not described as promotion.

## Keeper

```text
A clean PR is a receipt packet, not a crown.
```
