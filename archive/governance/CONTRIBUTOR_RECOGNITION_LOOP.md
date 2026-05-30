---
artifact_id: DX-POLICY-CONTRIBUTOR-RECOGNITION-001
title: Contributor Recognition Loop
status: candidate
created: 2026-05-28
owner: council
tags: [developer-experience, recognition, community, contributor]
---

# Contributor Recognition Loop

> Defines how Atlas Lattice recognizes and celebrates contributor achievements.

status: candidate

---

## Why Recognition Matters

Contributors invest time and creativity in a public-good project. Recognition signals that their work is valued, encourages continued contribution, and attracts new contributors who see that the community is alive and appreciative.

---

## Recognition Mechanisms

### 1. All-Contributors File

The repository maintains an `.all-contributorsrc` file and a contributors section in README.md using the [all-contributors](https://allcontributors.org/) specification.

Contribution types recognized:
- `code` — code contributions
- `doc` — documentation
- `ideas` — design and ideation
- `review` — PR reviews
- `translation` — translations
- `test` — testing
- `data` — knowledge graph data contributions

---

### 2. Wave Completion Shout-Outs

When a wave is completed, the commit message and PR description credit contributors who contributed to that wave:

```
Wave 10 complete: Developer Experience (#109-#120)

Co-authored-by: [contributor name] <email>
```

---

### 3. Quality Report Recognition

The monthly quality report includes a "Contributors This Month" section listing all contributors with merged PRs in the period.

---

### 4. Milestone Badges

Major milestones (25%, 50%, 75%, 100% of the 144 campaign) are marked with a GitHub release and a call-out to contributors in the release notes.

---

### 5. First Contribution Celebration

First-time contributors receive:
- The automated welcome message (see Welcome Automation Policy)
- A personal thank-you comment from a council member on their merged PR

---

## Recognition Ladder

| Milestone | Recognition |
|-----------|------------|
| First merged PR | Welcome comment + all-contributors entry |
| 5 merged PRs | Listed in quality report spotlight |
| 10 merged PRs | Invited to mentor role consideration |
| Domain ownership | CODEOWNERS entry + README acknowledgment |
| Council membership | Full council recognition in README |

---

*Atlas Lattice Foundation · status: candidate*
