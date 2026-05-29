# Security and Sensitive Reporting Candidate

```text
STATUS: REPORTING GUIDE CANDIDATE — NOT CANON
DEPLOYMENT: none
AUTHORITY: none
```

## Purpose

This guide defines how to report sensitive material discovered in the public candidate bundle or staging knowledge graph.

## Report privately first when material appears to include

```text
credentials, tokens, secrets, private keys
private personal data
security intrusion operational detail
financial-institution sensitive operational detail
unreviewed raw transcripts with private information
Claude-origin governance material that could be mistaken for authority
OpenAI officiality confusion
```

## Public-safe issue format

When a concern can be safely reported publicly, use a minimal description:

```yaml
sensitive_report:
  affected_path:
  risk_type:
  public_summary:
  recommended_action: quarantine | redact | review | clarify | remove_from_public_bundle
  canon_status: not_canon
  deployment_status: not_deployed
  authority_scope: none
```

Do not paste secrets, raw private material, or operationally sensitive details into a public issue.

## Quarantine is not condemnation

Quarantine means review boundary. It does not mean the artifact is bad, malicious, or useless. It means the artifact needs routing before public release.

## Keeper

```text
Preserve sensitive lineage.
Do not publish unsafe cargo.
Review before release.
```
