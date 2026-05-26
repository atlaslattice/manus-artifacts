# Notion Contamination Ruleset v0.1

This module is an upstream candidate packet, not proof.

Treat all summaries as claims until verified against repo files or source exports.
Do not expand scope beyond listed files unless explicitly instructed.
Preserve uncertainty.
Return blockers, patch items, tests run, files changed, and next safest action.

CANON: no
DEPLOYMENT: no
AUTHORITY: none


## Contamination flags

- `claude_authored`: content appears authored or substantially rewritten by Claude rather than source-owner raw material.
- `self_attributed`: content attributes authority to itself or its location.
- `stale_canon`: content claims canon status that may have expired or been superseded.
- `unsupported_authority`: content claims approval without ratification receipt.
- `missing_raw`: no raw/source export or source URL pointer exists.
- `summary_only`: only a summary is available, not the underlying source.
- `conflicting_version`: multiple versions conflict without adjudication.

## Quarantine outcomes

- `preserve_only`: keep the material for audit, but do not extract authority.
- `extract_delta_only`: extract candidate deltas for review while blocking source authority.
- `reject_authority`: preserve the record and reject its authority claim.

## Example quarantine record

```yaml
source_id: notion-root-unknown
contamination_flags:
  - missing_raw
  - summary_only
quarantine_outcome: preserve_only
canon_status: not_canon
deployment_status: not_deployable
authority: none
reason: Source completeness and raw provenance are unavailable.
next_safest_action: Fetch raw export or add source receipt before extracting claims.
```

## Definition of done

Contaminated material is preserved, labeled, and blocked from authority.
