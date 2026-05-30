---
artifact_id: SEC-POLICY-SECURITY-TRAINING-PLAYBOOK-001
title: Security Training Playbook
status: candidate
created: 2026-05-28
owner: council
tags: [security, training, community, governance]
---

# Security Training Playbook

> A practical security training guide for contributors, council members, and AI agents operating in the Atlas Lattice repository.

status: candidate

---

## Who This Is For

Everyone who commits, reviews, or operates in this repository should complete the baseline security training in this playbook. This is especially important for:
- New contributors
- AI agents onboarding to the swarm
- Council members with elevated permissions

---

## Module 1: Secret Hygiene (Required — 5 minutes)

### The Rule
**Never commit secrets.** A secret is any credential, token, key, password, or sensitive configuration value.

### Common Mistakes

| Mistake | Example | Fix |
|---------|---------|-----|
| Committing `.env` file | `API_KEY=sk-...` in a file | Add `.env` to `.gitignore`; revoke the key |
| Hardcoded test token | `token = "ghp_abc123"` in test file | Use environment variable; rotate the real token |
| Screenshot with visible token | Image showing terminal with API key | Revoke the key; use redacted screenshots |

### Verification
- [ ] `.env` is in `.gitignore`
- [ ] All secrets are stored in GitHub Secrets or environment variables
- [ ] No hardcoded credentials in code, tests, or documentation

---

## Module 2: Pull Request Security Review (Required — 10 minutes)

Before approving any PR, check:

- [ ] No new dependencies added without justification
- [ ] No GitHub Actions added without SHA pinning
- [ ] No new permissions added to workflows without comment
- [ ] No `.github/` changes without @atlaslattice review
- [ ] No schema changes without backward compatibility check
- [ ] No PII in committed work logs or documentation

---

## Module 3: Dependency Security (Required — 5 minutes)

- **Always** review Dependabot PRs within the SLA (see [VULNERABILITY_TRIAGE_SLAS.md](./VULNERABILITY_TRIAGE_SLAS.md))
- **Never** approve a dependency update without checking the package's changelog for breaking or security changes
- **Report** any dependency with a known CVE to the Security Champion immediately

---

## Module 4: AI Agent Security (For AI agents — 5 minutes)

AI agents operating in this repository must:

- [ ] Never commit secrets or tokens of any kind
- [ ] Never modify `.github/workflows/` files without explicit @atlaslattice authorization in the PR description
- [ ] Always set `status: candidate` on new artifacts (never `canon`)
- [ ] Never claim ratification authority
- [ ] Log work in TIDELOCKBrain per the work log format
- [ ] Respect CODEOWNERS — if a file is owned by @atlaslattice, note in the PR that ownership review is required

---

## Module 5: Incident Response Basics (Required — 10 minutes)

If you discover:
- **A committed secret:** Immediately open a GitHub issue with `[SECURITY]` prefix; do NOT include the secret value; notify @atlaslattice
- **A vulnerability in a dependency:** Follow [VULNERABILITY_TRIAGE_SLAS.md](./VULNERABILITY_TRIAGE_SLAS.md)
- **A security incident:** Follow [INCIDENT_RESPONSE_RUNBOOK.md](./INCIDENT_RESPONSE_RUNBOOK.md)

---

## Completion Record

New contributors and AI agents should add a completion record to `archive/governance/SECURITY_TRAINING_COMPLETIONS.md` (create if missing):

```
| Contributor/Agent | Date | Modules completed |
|------|------|------|
| @username | YYYY-MM-DD | 1, 2, 3, 4, 5 |
```

---

*Atlas Lattice Foundation · status: candidate*
