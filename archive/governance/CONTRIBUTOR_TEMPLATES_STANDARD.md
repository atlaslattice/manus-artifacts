---
artifact_id: DX-POLICY-TEMPLATES-STANDARD-001
title: Contributor Templates Standard
status: candidate
created: 2026-05-28
owner: council
tags: [developer-experience, templates, github, community]
---

# Contributor Templates Standard

> Defines the standard set of GitHub issue, PR, and discussion templates for Atlas Lattice.

status: candidate

---

## Template Inventory

All templates live in `.github/`:

| Template | Path | Purpose |
|---------|------|---------|
| Bug report | `.github/ISSUE_TEMPLATE/bug_report.md` | Report bugs |
| Feature request | `.github/ISSUE_TEMPLATE/feature_request.md` | Propose new features |
| Documentation issue | `.github/ISSUE_TEMPLATE/docs_issue.md` | Flag doc problems |
| Good first issue | `.github/ISSUE_TEMPLATE/good_first_issue.md` | Fast Lane issue creation |
| RFC proposal | `.github/ISSUE_TEMPLATE/rfc_proposal.md` | Formal proposals |
| Pull request | `.github/PULL_REQUEST_TEMPLATE.md` | Default PR template |
| Discussion: Q&A | `.github/DISCUSSION_TEMPLATE/question.md` | Help questions |

---

## Bug Report Template

```markdown
---
name: Bug report
about: Report something that is broken or incorrect
labels: bug
---

## What is broken?
[Clear description of the bug]

## Where is it? (file, section, or link)

## Expected behavior

## Actual behavior

## Steps to reproduce (if applicable)

## Additional context
```

---

## Feature Request Template

```markdown
---
name: Feature request
about: Suggest an improvement or new capability
labels: enhancement
---

## Summary
[One sentence: what you want]

## Motivation
[Why is this needed? What problem does it solve?]

## Proposed approach (optional)

## Alternatives considered (optional)
```

---

## Pull Request Template

```markdown
## Summary
[One sentence describing the change]

## Related issue(s)
Closes #[issue number]

## Changes
- [Bullet list of what changed]

## Checklist
- [ ] Frontmatter added/updated (artifact_id, status, tags)
- [ ] Taskboard(s) updated if this closes a campaign task
- [ ] CHANGELOG.md updated
- [ ] Tests pass (`python -m pytest -q`)
```

---

## Template Maintenance

Templates are reviewed annually as part of the annual accessibility audit. Updates go through the standard PR process.

---

*Atlas Lattice Foundation · status: candidate*
