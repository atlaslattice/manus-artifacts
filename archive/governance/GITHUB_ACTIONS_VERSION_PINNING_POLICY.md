---
artifact_id: CICD-POLICY-ACTION-VERSIONS-001
title: GitHub Actions Version Pinning and Audit Policy
status: candidate
created: 2026-05-28
owner: council
tags: [ci-cd, security, supply-chain, github-actions]
---

# GitHub Actions Version Pinning and Audit Policy

> Defines the rules for pinning GitHub Action versions and auditing them for security.

status: candidate

---

## The Risk

Using unpinned action versions (e.g., `uses: actions/checkout@v4`) means that if the action's tag is moved or the repository is compromised, malicious code could run in the CI pipeline with write access to the repository and secrets.

**Best practice:** Pin actions to a full commit SHA, not a floating tag.

---

## Pinning Rules

### Rule 1: All third-party actions must be pinned by SHA

```yaml
# Good ✅
- uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683  # v4.2.2

# Bad ❌
- uses: actions/checkout@v4
- uses: actions/checkout@main
```

### Rule 2: First-party actions (atlaslattice/*) may use tag refs

Since we control these actions, floating tag refs are acceptable. However, note the tag version in a comment.

### Rule 3: SHA must be commented with the version it corresponds to

```yaml
- uses: actions/setup-python@0b93645e9fea7318ecaed2b359559ac225c90a2  # v5.3.0
```

---

## Current Status (2026-05-28)

| Workflow | Pinning status |
|----------|---------------|
| `.github/workflows/boring-machine-validation.yml` | ⚠️ Needs audit |
| `.github/workflows/gptbrain-reference-checks.yml` | ⚠️ Needs audit |
| `.github/workflows/lattice-kg-quality-gates.yml` | ⚠️ Needs audit |

**Action:** Audit all workflow files and pin to SHA as part of Wave 7 security sprint.

---

## Audit Process

Run quarterly:

1. List all `uses:` references in `.github/workflows/*.yml`
2. For each unpinned reference, look up the current SHA for the pinned tag
3. Update the workflow file with the SHA
4. Record the audit date and findings in [COMPLIANCE_EVIDENCE_INDEX.md](./COMPLIANCE_EVIDENCE_INDEX.md)

---

## Adding a New Action

When adding a new GitHub Action to a workflow:

1. Find the action's latest stable release tag
2. Look up the full commit SHA for that tag on GitHub
3. Use the SHA in the `uses:` field with a comment showing the version
4. Add the action to the audit registry below

---

## Action Registry

| Action | Current pinned SHA | Version | Audit date |
|--------|------------------|---------|-----------|
| `actions/checkout` | (pending audit) | v4.x | — |
| `actions/setup-python` | (pending audit) | v5.x | — |
| `actions/cache` | (pending audit) | v4.x | — |

---

*Atlas Lattice Foundation · status: candidate*
