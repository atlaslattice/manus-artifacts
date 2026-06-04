# ⚡ Aetherforge Top-50 Taskboard
### Public Archive World-Class Elevation Sprint

> **Issued by:** TIDELOCKBRAIN (Copilot) · 2026-05-26
> **Mission:** Elevate the full `atlaslattice/manus-artifacts` git archive to public, world-class standard.
> **Shape:** Metatron's Cube — 5 rings × 10 tasks each.
> **Canon status:** Candidate. Requires @atlaslattice adjudication before ratification.

---

## Ring I — Canon & Structure (Foundation Node)
*Build the immovable skeleton beneath the entire archive.*

| # | Task | Status | Notes |
|---|---|---|---|
| 1 | Define a single global canon policy for what constitutes authoritative content in-repo | 🟡 Candidate | See [CONTRIBUTING.md](../.github/CONTRIBUTING.md) draft |
| 2 | Create a repository-wide taxonomy for all artifact types (doctrine, spec, log, dream, seed, schema) | ✅ Done | `docs/knowledge-graph/artifact_taxonomy.v0_1.json` |
| 3 | Add stable semantic IDs for every major document (`ALM-v4`, `BAZZINGA-v0.1`, etc.) | ⬜ Open | Enables canonical cross-links |
| 4 | Standardize folder naming conventions across all domains | ⬜ Open | Audit needed |
| 5 | Add lifecycle states to all artifacts: `draft` → `candidate` → `ratified` → `archived` | ⬜ Open | Frontmatter standard |
| 6 | Add ownership metadata to each major domain/folder (`CODEOWNERS`) | ⬜ Open | |
| 7 | Create a global index of all top-level systems and projects with one-line value props | ✅ Done | See [ARCHIVE_INDEX.md](../docs/ARCHIVE_INDEX.md) |
| 8 | Add canonical cross-links between related artifacts (e.g., Aluminum OS ↔ Ring 0 Rust core) | ⬜ Open | |
| 9 | Define versioning expectations for strategy/doctrine docs | ⬜ Open | |
| 10 | Publish a "how to read this archive" newcomer map | ✅ Done | See [START_HERE.md](../docs/START_HERE.md) |

---

## Ring II — Quality Gates & Reliability (Forge Node)
*Make every CI run a proof of archive integrity.*

| # | Task | Status | Notes |
|---|---|---|---|
| 11 | Enforce markdown linting and heading structure checks in CI | ✅ Done | `repo-hygiene-checks.yml` |
| 12 | Enforce broken-link detection for all internal markdown links | ✅ Done | `docs-link-checks.yml` |
| 13 | Add YAML frontmatter/schema validation for key document classes | ✅ Done | `artifact-graph-checks.yml` + `validate_artifact_graph.py` |
| 14 | Add duplicate-title and duplicate stable-ID detection | ⬜ Open | Python script |
| 15 | Add orphan-file detection for unlinked important artifacts | ⬜ Open | |
| 16 | Add merge-conflict marker detection across all text files | ✅ Done | `repo-hygiene-checks.yml` |
| 17 | Add required review checklist for high-impact documentation PRs | ✅ Done | PR template |
| 18 | Add CI reporting that summarizes doc health by domain | ⬜ Open | |
| 19 | Add a "public-ready" label gate before artifact promotion | ⬜ Open | GitHub Labels |
| 20 | Automate weekly archive hygiene report via GitHub Issue | ⬜ Open | GH Actions schedule |

---

## Ring III — Discoverability & Knowledge Graph (Lattice Node)
*Make the archive navigable by anyone on Earth.*

| # | Task | Status | Notes |
|---|---|---|---|
| 21 | Build a searchable master catalog of all artifact domains | ✅ Done | See [ARCHIVE_INDEX.md](../docs/ARCHIVE_INDEX.md) |
| 22 | Add tags for themes, systems, and maturity levels to major artifacts | ⬜ Open | Frontmatter tags |
| 23 | Generate auto-updated topic pages from tags | ⬜ Open | Python script |
| 24 | Build timeline views for key initiatives and decisions | ⬜ Open | Markdown table |
| 25 | Add "related artifacts" sections to major docs | ⬜ Open | |
| 26 | Add "start here" reading paths by persona | ✅ Done | See [START_HERE.md](../docs/START_HERE.md) |
| 27 | Add glossary pages for domain-specific terms | ✅ Done | See [GLOSSARY.md](../docs/GLOSSARY.md) |
| 28 | Add changelog streams per major project/domain | ⬜ Open | CHANGELOG.md per domain |
| 29 | Publish architecture map of all repository domains (ASCII + visual) | ✅ Done | In README.md |
| 30 | Add dependency graph for conceptual and project relationships | ✅ Done | Mermaid graph added to `README.md` |

---

## Ring IV — Governance, Trust & Contributor UX (Council Node)
*Make contributing safe, clear, and canon-respecting.*

| # | Task | Status | Notes |
|---|---|---|---|
| 31 | Expand CONTRIBUTING into a world-class onboarding flow | ✅ Done | [CONTRIBUTING.md](../.github/CONTRIBUTING.md) |
| 32 | Add issue templates for archive curation, ideas, and reports | ✅ Done | `.github/ISSUE_TEMPLATE/` |
| 33 | Add PR template tuned for canon-change documentation | ✅ Done | `.github/pull_request_template.md` |
| 34 | Add CODEOWNERS coverage for critical directories | ⬜ Open | `.github/CODEOWNERS` |
| 35 | Add governance rules for deprecation and supersession | ⬜ Open | Extend CONTRIBUTING |
| 36 | Add provenance fields to all major artifacts: author, source, last review date | ⬜ Open | Frontmatter audit |
| 37 | Define and publish review SLAs for public-facing artifacts | ⬜ Open | |
| 38 | Add "decision record" standard for major architectural changes | ⬜ Open | ADR format |
| 39 | Publish a public quality rubric for "world-class artifact" status | ⬜ Open | |
| 40 | Add SECURITY.md with responsible disclosure policy | ✅ Done | [SECURITY.md](../SECURITY.md) |

---

## Ring V — Public Showcase & Brand-Grade Presentation (Sovereign Node)
*Make the world want to read this.*

| # | Task | Status | Notes |
|---|---|---|---|
| 41 | Redesign README as a premium public landing page | ✅ Done | [README.md](../README.md) |
| 42 | Add flagship artifact spotlight with value statements | ✅ Done | In README.md |
| 43 | Add polished project overview pages for each major initiative | ✅ Done | Added project overview READMEs and refreshed Chinook v1.0 |
| 44 | Add visual identity consistency across major docs | ⬜ Open | Emoji + heading conventions |
| 45 | Add a "state of the archive" quarterly report | ⬜ Open | [State_of_the_Union_Briefing.md](../State_of_the_Union_Briefing.md) extends this |
| 46 | Add curated "best-of" reading lists by theme | ⬜ Open | |
| 47 | Write a publish-ready mission narrative: who, what, why, how | ✅ Done | In README.md intro |
| 48 | Add a public roadmap board for archive elevation milestones | ✅ Done | This file |
| 49 | Generate a world-readiness scorecard comparing vs. top public knowledge repos | ⬜ Open | |
| 50 | Launch Aetherforge "public debut" — announce archive is world-class ready | ⬜ Open | Final gate |

---

## Progress Summary

```
Ring I   (Canon & Structure):       3/10 done
Ring II  (Quality Gates):           5/10 done
Ring III (Discoverability):         6/10 done
Ring IV  (Governance & Trust):      5/10 done
Ring V   (Public Showcase):         6/10 done
─────────────────────────────────────────────
Total:  25/50 tasks complete  ▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░  50%
```

---

## Next Sprint Candidates (Highest-Impact Open Tasks)

1. **#34** — CODEOWNERS (unlocks #37 SLAs)
2. **#14** — Duplicate-title and duplicate stable-ID detection
3. **#18** — CI reporting for doc health by domain
4. **#39** — Public quality rubric for world-class artifact status
5. **#49** — World-readiness scorecard against top repos

---

*Taskboard maintained by TIDELOCKBRAIN · All status changes require human-root review · Metatron's Cube geometry: 5 rings × 10 nodes = 50 sovereign tasks*
