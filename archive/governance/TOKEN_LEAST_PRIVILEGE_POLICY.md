---
artifact_id: SEC-POLICY-TOKEN-LEAST-PRIVILEGE-001
title: Token Least Privilege Policy
status: candidate
created: 2026-05-28
owner: council
tags: [security, tokens, least-privilege, supply-chain]
---

# Token Least Privilege Policy

> Defines the principle of least privilege as applied to all tokens, secrets, and credentials in the repository.

status: candidate

---

## Principle

Every token, secret, or credential used in this repository must have the **minimum permissions necessary** to perform its function. Over-permissioned tokens are a supply chain risk.

---

## Token Categories

### GitHub Actions GITHUB_TOKEN

The `GITHUB_TOKEN` automatically provided to GitHub Actions workflows must be scoped:

```yaml
# In workflow files — set minimum permissions at workflow level
permissions:
  contents: read      # read repo content
  # Only add write permissions if actually needed
  # pull-requests: write  # only if workflow posts PR comments
  # issues: write         # only if workflow opens issues
```

**Default:** Set `permissions: read-all` at the top of all workflow files unless write is explicitly required for a specific job.

---

### Repository Secrets

| Secret | Purpose | Scope | Rotation |
|--------|---------|-------|---------|
| `GITHUB_TOKEN` | Auto-provided by GitHub; do not store manually | Workflow only | Auto (per-run) |
| `PYPI_TOKEN` (if any) | Publish Python packages | Trusted publishing (OIDC preferred) | Quarterly |
| External service tokens | Third-party integrations | Minimum read scope for the service | 90 days |

---

### Personal Access Tokens (PATs)

PATs must not be committed to the repository and must not be stored as repository secrets when fine-grained tokens or OIDC can be used instead.

| Guideline | Rule |
|-----------|------|
| Use fine-grained PATs | Prefer over classic PATs |
| Scope to minimum repos | Never use `all repositories` scope |
| Set expiration | Maximum 90-day expiration |
| Document purpose | Each PAT stored in GitHub's token UI must have a descriptive name |
| Rotate on personnel change | Any PAT associated with a person who leaves must be rotated immediately |

---

## Audit Process

| Check | Frequency |
|-------|-----------|
| Review GitHub Actions workflow permissions | Quarterly |
| Audit stored repository secrets list | Quarterly |
| Rotate all external service tokens | Every 90 days |
| Verify no over-scoped GITHUB_TOKEN usage | Each wave's CI review |

The audit is documented in [COMPLIANCE_EVIDENCE_INDEX.md](./COMPLIANCE_EVIDENCE_INDEX.md).

---

## Workflow Permission Template

All new workflow files must start with:

```yaml
permissions:
  contents: read
```

Add additional permissions only when needed, with an inline comment explaining why:

```yaml
permissions:
  contents: read
  issues: write      # needed: workflow opens drift detection issues
```

---

*Atlas Lattice Foundation · status: candidate*
