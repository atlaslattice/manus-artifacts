---
artifact_id: CICD-POLICY-DOCS-PREVIEW-BUILDS-001
title: Docs Preview Builds Policy
status: candidate
created: 2026-05-28
owner: council
tags: [ci-cd, documentation, preview, deployment]
---

# Docs Preview Builds Policy

> Defines how pull request documentation changes are previewed before merging, enabling reviewers to see rendered output.

status: candidate

---

## Purpose

Markdown renders differently in different contexts. A preview build gives reviewers and authors a rendered view of documentation changes before they merge to main, reducing formatting surprises and improving review quality.

---

## Preview Build Approach

### Phase 1 (Now): GitHub Native Rendering

GitHub renders markdown natively in the PR diff view. For most documentation changes, this is sufficient. Reviewers can:
- View rendered markdown in the "Rich diff" view
- Check that headings, tables, and code blocks render correctly
- Follow links to verify they resolve

**Limitation:** No cross-document rendering; complex navigation not visible.

---

### Phase 2 (Q3 2026): GitHub Pages Preview per PR

A CI workflow will deploy a static preview site for each PR:

1. On every PR push, build a static markdown site (using MkDocs or similar)
2. Deploy to a PR-specific GitHub Pages URL: `https://atlaslattice.github.io/manus-artifacts/pr/{pr_number}/`
3. Post a comment on the PR with the preview URL
4. Teardown the preview when the PR is merged or closed

**Workflow:** `.github/workflows/docs-preview.yml` (planned Q3 2026)

---

### Phase 3 (Q4 2026): Full KG Preview

The preview includes:
- Rendered documentation site
- Interactive KG graph visualization with the PR's changes applied
- Link integrity report for the PR's changes

---

## Review Checklist for Docs PRs

Before approving a documentation PR, reviewers should verify:

- [ ] All headings render correctly (no `#` symbols showing)
- [ ] Tables render and are readable
- [ ] Code blocks have correct syntax highlighting
- [ ] All links in changed files resolve (no 404s)
- [ ] No placeholder text (TODO, FIXME, TBD) in production paths
- [ ] Frontmatter is valid YAML

---

## Tooling Reference

| Tool | Use |
|------|-----|
| GitHub PR "Rich diff" view | Phase 1 preview (available now) |
| MkDocs | Phase 2 site builder (planned) |
| GitHub Pages | Phase 2/3 preview hosting |

---

*Atlas Lattice Foundation · status: candidate*
