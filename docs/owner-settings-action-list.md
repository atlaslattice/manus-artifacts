# Owner Settings Action List

Status: candidate owner runbook (not canon)

This list contains repository settings actions that cannot be completed via
tracked file changes and require maintainer permissions in GitHub UI.

## Required Click Paths

1. **Add repository description + topics**
   - Path: Repository → **Settings** → **General** → **Repository details**
   - Update: Description + Topics (suggested: `knowledge-graph`, `aetherforge`,
     `gptdream`, `open-source`, `ai-governance`, `metatrons-cube`)

2. **Add social preview image**
   - Path: Repository → **Settings** → **General** → **Social preview**
   - Update: Upload 1280×640 social card image

3. **Enable branch protection on `main`**
   - Path: Repository → **Settings** → **Branches** → **Add branch protection rule**
   - Rule: `main`, require PR review + required status checks, disable force push

4. **Enable GitHub Discussions**
   - Path: Repository → **Settings** → **Features** → enable **Discussions**
   - Then configure categories in: Repository → **Discussions** → **Categories**

5. **Enable GitHub Pages for docs**
   - Path: Repository → **Settings** → **Pages**
   - Build and deployment: Deploy from branch (e.g., `main` + `/docs`) or
     GitHub Actions workflow

## Verification

- Capture screenshots or notes in a follow-up issue after each settings change.
- Reflect completed settings actions back into `projects/aetherforge-top50-taskboard-2026-05-26.md`.
