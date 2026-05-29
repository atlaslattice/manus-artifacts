# Aetherforge Top-50 Taskboard — Public Launch Edition
## Metatron's Cube: 5 Rings × ~10 Nodes
*Target: make `atlaslattice/manus-artifacts` world-class open source*

---

## ⬡ CENTER — Pre-Flight Blockers (must complete before going public)

- [x] 1. Add `LICENSE` (Apache-2.0) at repo root — open-source legal prerequisite
- [x] 2. Secret-scan full git history (all commits) with `gitleaks` or `trufflehog`; revoke/rotate anything found
- [x] 3. PII audit — sweep for real personal data, phone numbers, private emails, internal credentials
- [x] 4. Decide scope — enumerate any subtrees that must remain private (health data, personal finance); redact or split before going public
- [x] 5. Force-push secret-clean rewrite if needed (`git-filter-repo`); do this **before** flipping visibility

---

## ⬡ INNER RING 1 — World-Class First Impression

- [x] 6. Rewrite `README.md` for public audience with mission statement and badges
- [ ] 7. Add repository description + topics in GitHub Settings (About section)
- [ ] 8. Add social preview image — 1280×640px Metatron's Cube banner (Settings → Social preview)
- [x] 9. Add `CITATION.cff` — makes archive citable in academic/research contexts
- [ ] 10. Pin 6 most important issues/projects on GitHub org profile
- [ ] 11. Set up GitHub Discussions (Announcements, Q&A, Ideas categories)
- [ ] 12. Enable GitHub Pages for `docs/` subtree (optional single-page static site)
- [x] 13. `about/` as public-facing origin story — who built this, what mission it serves

---

## ⬡ INNER RING 2 — CI/CD & Automation Excellence

- [x] 14. Wave-2 task 5: release-readiness checklist workflow (`.github/workflows/release-readiness.yml`)
- [x] 15. Wave-2 task 6: Dependabot config (`.github/dependabot.yml`)
- [x] 16. Wave-2 task 7: Stale issue/PR lifecycle automation (`.github/workflows/stale.yml`)
- [x] 17. Wave-2 task 8: SBOM generation workflow (`.github/workflows/sbom.yml`)
- [x] 18. Wave-2 task 9: Repository health dashboard doc (`docs/HEALTH_DASHBOARD.md`)
- [x] 19. Wave-2 task 10: Aetherforge mission intake template (`.github/ISSUE_TEMPLATE/mission_intake.yml`)
- [x] 20. Add OpenSSF Scorecard CI action (`.github/workflows/scorecard.yml`)
- [x] 21. Add `shields.io` badges to README — OpenSSF score, last commit, discussions
- [ ] 22. Add semantic versioning + changelog workflow (`release-please` or `semantic-release`)
- [ ] 23. Add performance/regression CI for Python codebases (benchmark tracking)

---

## ⬡ MIDDLE RING — Documentation & Knowledge Graph

- [x] 24. Archive-wide `docs/SUMMARY.md` or `docs/index.md` — navigable map of every major section
- [x] 25. Glossary of all domain-specific terms (Aetherforge, GPTBrain, Children of the Swarm, REM-8, etc.)
- [x] 26. Document the canon-trust hierarchy — single authoritative page
- [x] 27. Mission and vision statement doc — why this archive exists, what world it builds toward
- [x] 28. Architecture decision records (ADRs) — brief records for each major structural choice
- [x] 29. Timeline / changelog of major milestones — from first commit to now
- [x] 30. Full contributor onboarding guide — expand `CONTRIBUTING.md` into a journey doc
- [x] 31. Data provenance map — which files came from Manus, human authorship, GPTBrain agents
- [x] 32. Catalog of all codebases — `codebases/` subtree documented with purpose, language, status, tests
- [x] 33. Cross-reference map — links between `archive/boot/`, `aluminum-os/`, `projects/`, `council/`

---

## ⬡ OUTER RING 1 — Security & Governance Hardening

- [x] 34. Enable GitHub secret scanning + push protection (free on public repos) — via Settings
- [x] 35. Enable Dependabot alerts + security updates — via Settings (`.github/dependabot.yml` ready)
- [x] 36. `SECURITY.md` with escalation matrix and secret scanning guidance
- [ ] 37. Enable branch protection on `main` (require status checks, no force-push) — via Settings
- [ ] 38. Sign releases with GPG — makes artifacts verifiable by downstream users
- [x] 39. Publish a known-issues / errata list — intellectual honesty builds trust
- [x] 40. `GOVERNANCE.md` — merge rights, decision process, ratification workflow
- [x] 41. Document the canon adjudication process — @atlaslattice ratification workflow made explicit

---

## ⬡ OUTER RING 2 — Community, Discoverability & World-Class Reach

- [ ] 42. Submit repo to `awesome-*` lists (awesome-ai-agents, awesome-open-source-governance, etc.)
- [ ] 43. Write a launch blog post / announcement (can live in `docs/launch.md` mirrored externally)
- [ ] 44. Set up GitHub Sponsors or Open Collective — signals sustainability
- [ ] 45. Create a public roadmap — GitHub Projects board with milestones, visible to the world
- [x] 46. `PHILOSOPHY.md` — the intellectual and ethical foundation behind the archive
- [ ] 47. Submit to Zenodo or archive.org — gets a persistent DOI for the entire repo
- [ ] 48. Establish a release cadence — quarterly snapshots tagged as `vYYYY-QN`
- [ ] 49. Record a "tour of the archive" video or walkthrough — highest-leverage discoverability asset
- [ ] 50. Publish `v1.0-public` release — a formal tagged release marking the public debut

---

## Progress Summary

| Ring | Done | Total | % |
|---|---|---|---|
| Center (Pre-flight) | 5 | 5 | 100% |
| Inner Ring 1 (First Impression) | 4 | 8 | 50% |
| Inner Ring 2 (CI/CD) | 7 | 10 | 70% |
| Middle Ring (Docs & Knowledge) | 10 | 10 | 100% |
| Outer Ring 1 (Security) | 5 | 8 | 63% |
| Outer Ring 2 (Community) | 1 | 9 | 11% |
| **Total** | **32** | **50** | **64%** |

---

## Immediate Next Actions

**🔴 Blockers (items 2-5):** Pre-flight audits now captured in
`docs/security/PUBLIC_READINESS_PRE_FLIGHT_REPORT_2026-05-28.md`.
Credential rotation verification remains a manual owner action before final
public visibility promotion.

**🟡 Quick wins (items 7, 8, 37):** Add repo topics/description, social preview
image, and branch protection — each takes < 5 minutes in Settings.

**🟢 Next agent sprint:** advance remaining security hardening and
launch/community items.

## Owner Settings-Only Actions (exact click-paths)

These cannot be completed via repository file edits:

1. **Description + Topics** — Settings → General → Repository details
2. **Social preview image** — Settings → General → Social preview
3. **Branch protection (`main`)** — Settings → Branches → Add branch protection rule
4. **Discussions enablement/categories** — Settings → Features (enable Discussions), then Discussions → Categories
5. **GitHub Pages for `/docs`** — Settings → Pages

Reference runbook: `docs/owner-settings-action-list.md`.

---

*Aetherforge execution board — maintained by @atlaslattice and the council.*
*Shape: Metatron's Cube (1 center + 4 rings of nodes).*
