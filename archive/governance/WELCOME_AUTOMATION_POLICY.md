---
artifact_id: DX-POLICY-WELCOME-AUTOMATION-001
title: Welcome Automation Policy
status: candidate
created: 2026-05-28
owner: council
tags: [developer-experience, automation, community, welcome, github-actions]
---

# Welcome Automation Policy

> Defines the automated welcome messages for first-time contributors.

status: candidate

---

## Purpose

First impressions matter. When a new contributor opens their first PR or issue, an automated welcome message sets a warm, inclusive tone and provides immediate guidance.

---

## Triggers

| Event | Automation |
|-------|-----------|
| First issue from a new contributor | Welcome message on the issue |
| First PR from a new contributor | Welcome message on the PR |

---

## Welcome Message — First Issue

```markdown
👋 Welcome to Atlas Lattice, @[username]! Thanks for opening your first issue.

Here are some resources to help:
- [NEWCOMER_FAQ.md](docs/NEWCOMER_FAQ.md) — answers the most common questions
- [GLOSSARY.md](docs/GLOSSARY.md) — key terms explained
- [GOVERNANCE_ONBOARDING_GUIDE.md](docs/GOVERNANCE_ONBOARDING_GUIDE.md) — how decisions are made

A council member will respond within 48 hours. You're welcome here! 🌍
```

---

## Welcome Message — First PR

```markdown
🎉 Welcome, @[username]! This is your first PR to Atlas Lattice — thank you!

Before we review, a quick checklist:
- [ ] Does your PR include updated frontmatter (if you modified a governed artifact)?
- [ ] Did you update the taskboard if this closes a campaign task?
- [ ] Do tests pass? (`python -m pytest -q`)

A reviewer will take a look within 5 business days. 
Your contribution is part of building a world-class open-source knowledge graph. 🌐
```

---

## Implementation

The welcome automation uses the `actions/first-interaction` GitHub Action:

```yaml
# .github/workflows/welcome.yml
name: Welcome new contributors

on:
  issues:
    types: [opened]
  pull_request:
    types: [opened]

jobs:
  welcome:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/first-interaction@v1
        with:
          repo-token: ${{ secrets.GITHUB_TOKEN }}
          issue-message: |
            👋 Welcome to Atlas Lattice, @{{ author }}! ...
          pr-message: |
            🎉 Welcome, @{{ author }}! This is your first PR ...
```

---

## Tone Guidelines

Welcome messages must be:
- Warm and non-intimidating
- Brief (under 100 words)
- Action-oriented (provide immediate next steps)
- Inclusive (no jargon; no assumed knowledge)

---

*Atlas Lattice Foundation · status: candidate*
