---
artifact_id: SEC-POLICY-SECRET-SCANNING-001
title: Secret Scanning Patterns Policy
status: candidate
created: 2026-05-28
owner: council
tags: [security, secret-scanning, supply-chain, ci-cd]
---

# Secret Scanning Patterns Policy

> Defines how secret scanning is configured and what additional patterns are monitored beyond GitHub's defaults.

status: candidate

---

## Baseline: GitHub Default Secret Scanning

GitHub Advanced Security secret scanning is enabled for this repository. It automatically detects:
- GitHub personal access tokens (PATs)
- OAuth tokens
- AWS, GCP, Azure credentials
- Stripe, Twilio, and other service tokens
- 200+ secret patterns by default

**Requirement:** GitHub secret scanning alerts must be reviewed within 48 hours of opening.

---

## Custom Patterns

The following custom patterns supplement GitHub's defaults:

| Pattern name | Description | Regex (illustrative) |
|-------------|-------------|---------------------|
| Atlas API Key | Internal Atlas Lattice API keys | `atlaslattice_[a-zA-Z0-9]{32}` |
| GPTBrain session token | Session token format | `gptbrain_sess_[a-zA-Z0-9]{40}` |
| Council signing key hint | Hints of key material in docs | `-----BEGIN.*PRIVATE KEY-----` |

Custom patterns are configured in `.github/secret_scanning.yml`.

---

## Developer Pre-Commit Checklist

Before every commit, verify:
- [ ] No API keys, tokens, or passwords in any committed file
- [ ] No `.env` files staged for commit (should be in `.gitignore`)
- [ ] No hardcoded credentials in test fixtures
- [ ] No internal system URLs that reveal internal infrastructure

---

## Alert Response

| Alert type | Response | Owner | SLA |
|-----------|---------|-------|-----|
| GitHub PAT exposed | Revoke immediately; rotate | @atlaslattice | 1 hour |
| Third-party service token | Revoke + rotate + audit usage | Section owner | 4 hours |
| Internal pattern match | Investigate; redact if confirmed | Security champion | 24 hours |
| False positive | Dismiss with justification | Alert reviewer | 48 hours |

---

## Scanning Scope

Secret scanning applies to:
- All commits pushed to any branch
- All pull request commits
- Historical commits on the default branch

---

## Audit

Secret scanning configuration and alert history are reviewed quarterly as part of the [Compliance Evidence Index](./COMPLIANCE_EVIDENCE_INDEX.md) update.

---

*Atlas Lattice Foundation · status: candidate*
