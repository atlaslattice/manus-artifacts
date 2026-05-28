# Contributor Onboarding Journey

```
STATUS: CANDIDATE — NOT CANON
PURPOSE: step-by-step onboarding for new contributors to atlaslattice/manus-artifacts
LAST_UPDATED: 2026-05-28
```

Welcome to **atlaslattice/manus-artifacts** — a living constitutional substrate
for human-AI co-creation, structured as a knowledge-graph hypercube under the
Aetherforge initiative.

> Everything is a candidate until ratified. Everything connects to everything.
> The shape is Metatron's Cube.

---

## Quick-Start (5 minutes)

| Want to… | Go here |
|---|---|
| Understand the vision | [PHILOSOPHY.md](../PHILOSOPHY.md) |
| Understand governance | [GOVERNANCE.md](../GOVERNANCE.md) |
| See what tasks are open | [Wave-3 sprint board](../projects/aetherforge-top10-taskboard-2026-05-28.md) |
| Find a first task | Open an issue → pick from Wave-3 board |
| Report a bug or issue | [GitHub Issues](https://github.com/atlaslattice/manus-artifacts/issues/new/choose) |
| Log AI evidence | [docs/ai-evidence/README.md](./ai-evidence/README.md) |

---

## Step 1 — Orient Yourself

1. Read [README.md](../README.md) — start at "What Is This?"
2. Read [PHILOSOPHY.md](../PHILOSOPHY.md) — understand the mission.
3. Read [GOVERNANCE.md](../GOVERNANCE.md) — understand canon boundaries.
4. Read [.github/CONTRIBUTING.md](../.github/CONTRIBUTING.md) — understand the PR workflow.
5. Read [docs/canon-trust-hierarchy.md](./canon-trust-hierarchy.md) — understand CANDIDATE vs RATIFIED.

---

## Step 2 — Find Your First Task

The board hierarchy runs from program to sprint:

| Level | Board |
|---|---|
| Program (144 tasks) | [aetherforge-144-task-campaign-2026-05-27.md](../projects/aetherforge-144-task-campaign-2026-05-27.md) |
| Portfolio (50 tasks) | [aetherforge-top50-taskboard-2026-05-26.md](../projects/aetherforge-top50-taskboard-2026-05-26.md) |
| Sprint Wave 3 (active) | [aetherforge-top10-taskboard-2026-05-28.md](../projects/aetherforge-top10-taskboard-2026-05-28.md) |

**Recommended first task types for new contributors:**
- Documentation improvements (any `docs/` file)
- Metadata additions (adding STATUS/title fields to existing artifacts)
- Cross-link additions (adding links between related documents)

---

## Step 3 — Open an Issue

Before coding, open an issue using one of these forms:

| Form | Use when |
|---|---|
| [Artifact Proposal](https://github.com/atlaslattice/manus-artifacts/issues/new?template=artifact-proposal.yml) | Adding a new artifact to the archive |
| [Governance Review Request](https://github.com/atlaslattice/manus-artifacts/issues/new?template=governance-review-request.yml) | Requesting canon review of a candidate |
| [Community Onboarding](https://github.com/atlaslattice/manus-artifacts/issues/new?template=community-onboarding.yml) | Introducing yourself |
| [GPTDream Task](https://github.com/atlaslattice/manus-artifacts/issues/new?template=task_ops.yml) | Operational task tracking |

---

## Step 4 — Prepare Your Change

1. Fork or create a branch from `main`.
2. Make your change — keep it **additive**: never delete canon documents.
3. Run local validation relevant to changed paths:

   ```bash
   # If you touched docs/ or archive/ markdown:
   python scripts/check_markdown_links.py
   python scripts/validate_artifact_metadata.py

   # If you touched archive/boot/gptbrain/**:
   cd archive/boot/gptbrain/reference_impl
   python -m pytest -q
   bash run_checks.sh
   ```

4. Verify no secrets or credentials are present in your diff.

---

## Step 5 — Submit Your PR

1. Reference the originating issue or task board item in the PR description.
2. Ensure all required CI checks are green.
3. Request a CODEOWNERS review.
4. Use the [PR template](../.github/pull_request_template.md) checklist.

---

## Step 6 — Post-Merge: Canon Tracking

After merge, your artifact is a **CANDIDATE** — not canon. To nominate it
for canon promotion:

1. Add a row to [docs/canon-candidate-register.md](./canon-candidate-register.md).
2. Open a [Governance Review Request](https://github.com/atlaslattice/manus-artifacts/issues/new?template=governance-review-request.yml).
3. Ensure the artifact carries all [minimum canon fields](./canon-trust-hierarchy.md).

---

## Aetherforge Game Framing

Contributions are scored in the Aetherforge game. See the
[Arc-3 gameplay design](../projects/aetherforge-arc3-wave3-gameplay.md)
for scoring mechanics and the current arc story.

> *Every edge you forge in the KG earns an Edge Token.*
> *Every orphan you connect brings the lattice closer to coherence.*

---

*Related: [.github/CONTRIBUTING.md](../.github/CONTRIBUTING.md)*
*Related: [docs/canon-candidate-register.md](./canon-candidate-register.md)*
*Related: [projects/README.md](../projects/README.md)*
