# Notion Contamination Ruleset v0.1

status: candidate
canon_status: not_canon
deployment_status: not_deployable
authority: none

## Purpose

Preserve contaminated material without granting it authority.

## Contamination flags

- `claude_authored`: content appears authored or materially shaped by Claude rather than source evidence.
- `self_attributed`: artifact claims its own authority, ratification, or canon status.
- `stale_canon`: older canon language conflicts with current ratification boundaries.
- `unsupported_authority`: title, location, author, or tone claims authority without ratification evidence.
- `missing_raw`: raw source/export is absent.
- `summary_only`: only a summary is available; raw context is missing.
- `conflicting_version`: multiple versions disagree and no supersession event resolves them.

## Quarantine outcomes

- `preserve_only`: keep as receipt, do not extract claims.
- `extract_delta_only`: extract bounded differences with source caveats.
- `reject_authority`: preserve content while rejecting its authority claim.

## Example quarantine record

```yaml
record_id: quarantine-example-v0-1
source_ref: archive/notion_mirror/raw_exports/example.yaml
flags:
  - summary_only
  - unsupported_authority
outcome: reject_authority
canon_status: not_canon
deployment_status: not_deployable
preserve_source: true
reason: Summary claims source completeness but no raw export is present.
next_safest_action: request raw export or route to review packet with blocked status.
```
