# Repository Health Dashboard

*Snapshot date: 2026-05-26 | Cadence: updated each wave sprint*

## ⬡ At a Glance

| Signal | Status | Notes |
|---|---|---|
| License | ✅ Apache-2.0 | `LICENSE` at repo root |
| CI: Repo Hygiene | ✅ Active | `.github/workflows/repo-hygiene-checks.yml` |
| CI: Docs Link Checks | ✅ Active | `.github/workflows/docs-link-checks.yml` |
| CI: GPTBrain Checks | ✅ Active | `.github/workflows/gptbrain-reference-checks.yml` |
| CI: CodeQL Security | ✅ Active | `.github/workflows/codeql.yml` |
| CI: Artifact Sync Tests | ✅ Active | `.github/workflows/artifact-sync-tests.yml` |
| CI: Release Readiness | ✅ Active | `.github/workflows/release-readiness.yml` |
| CI: SBOM Generation | ✅ Active | `.github/workflows/sbom.yml` |
| Stale Automation | ✅ Active | `.github/workflows/stale.yml` |
| Dependabot | ✅ Configured | `.github/dependabot.yml` |
| CODEOWNERS | ✅ Present | `.github/CODEOWNERS` |
| SECURITY.md | ✅ Present | `.github/SECURITY.md` |
| CONTRIBUTING.md | ✅ Present | `.github/CONTRIBUTING.md` |
| GOVERNANCE.md | ✅ Present | `GOVERNANCE.md` |
| PHILOSOPHY.md | ✅ Present | `PHILOSOPHY.md` |
| CITATION.cff | ✅ Present | `CITATION.cff` |
| PR Template | ✅ Present | `.github/pull_request_template.md` |
| Issue Templates | ✅ 3 templates | bug, feature, task/ops |
| Branch Protection | ⚠️ Guidance only | See `.github/BRANCH_PROTECTION.md` — enable via Settings |
| Secret Scanning | ⚠️ Manual step | Enable in repository Security settings |
| Dependabot Alerts | ⚠️ Manual step | Enable in repository Security settings |

## ⬡ Wave Summary

| Wave | Tasks | Status |
|---|---|---|
| Wave 1 (Governance Core) | 10/10 | ✅ Complete |
| Wave 2 (Reliability & Automation) | 10/10 | ✅ Complete |

## ⬡ Open Action Items (manual, requires repo Settings access)

1. **Enable branch protection on `main`** — require PR reviews, status checks, no force-push.
   Path: Settings → Branches → Add rule → `main`.

2. **Enable GitHub secret scanning + push protection** — free on public repositories.
   Path: Settings → Security → Secret scanning.

3. **Enable Dependabot security alerts** — auto-alerts for known CVEs.
   Path: Settings → Security → Dependabot alerts.

4. **Set repository visibility to Public** — final step for open-source launch.
   Path: Settings → Danger Zone → Change visibility.

5. **Add repository description + topics** — improves discoverability.
   Suggested topics: `ai-governance`, `constitutional-ai`, `agentic-systems`,
   `aluminum-os`, `gptbrain`, `open-source`, `metatrons-cube`.

6. **Add social preview image** — 1280×640px Metatron's Cube banner.
   Path: Settings → Social preview.

## ⬡ Canon Health

- All artifacts are **candidates** until ratified by full council + @atlaslattice.
- GitHub is the canonical substrate; Drive/Notion are relay layers only.
- See `GOVERNANCE.md` for the full ratification process.

---

*Next scheduled update: Wave 3 sprint completion.*
