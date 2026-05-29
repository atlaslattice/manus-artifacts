---
title: Contribution Playbooks
artifact_id: DOCS-CONTRIBUTION-PLAYBOOKS-2026-05-29
status: candidate
canon_status: candidate
lifecycle_state: active
ratification_event_id: pending
trust_state: WORK
owner: Atlas Lattice Foundation
last_updated: 2026-05-29
provenance: Created from 7-pillar world-class execution plan (2026-05-29). Repeatable step-by-step playbooks for every common contribution type.
---

# 📚 Contribution Playbooks

*Repeatable, step-by-step guides for every common contribution type in Atlas Lattice.*

> Start here if you know what you want to contribute but aren't sure how to do it correctly.
> See [START_HERE.md](./START_HERE.md) if you're new to this archive.

---

## Playbook Index

| # | Playbook | Use When |
|---|----------|---------|
| PB-01 | [Add a New Artifact](#pb-01-add-a-new-artifact) | Creating new research, spec, or governance doc |
| PB-02 | [Migrate Legacy Artifact](#pb-02-migrate-legacy-artifact) | Adding frontmatter to an existing file |
| PB-03 | [Fix a Broken Link](#pb-03-fix-a-broken-link) | A relative link is 404 |
| PB-04 | [Propose a Fork Synthesis](#pb-04-propose-a-fork-synthesis) | Incorporating an external GitHub repo |
| PB-05 | [Submit a Swarm Task](#pb-05-submit-a-swarm-task) | Proposing work via intake process |
| PB-06 | [Upgrade an Artifact's Status](#pb-06-upgrade-an-artifacts-status) | Moving candidate → ratified |
| PB-07 | [Open a Governance RFC](#pb-07-open-a-governance-rfc) | Proposing process or architecture changes |
| PB-08 | [Add Tests for an Artifact](#pb-08-add-tests-for-an-artifact) | Improving KG quality gates or coverage |

---

## PB-01: Add a New Artifact

**Use when:** Creating any new research doc, spec, governance artifact, or data file.

**Steps:**

1. **Choose the right path.** See [NAMING_CONVENTIONS.md](./NAMING_CONVENTIONS.md) and [ARCHIVE_INDEX.md](./ARCHIVE_INDEX.md) for where things belong.

2. **Create the file with universal frontmatter:**
   ```yaml
   ---
   title: <Your Title>
   artifact_id: <DOMAIN>-<SLUG>-<YYYY-MM-DD>
   status: candidate
   canon_status: candidate
   lifecycle_state: draft
   ratification_event_id: pending
   trust_state: WORK
   owner: Atlas Lattice Foundation
   last_updated: <YYYY-MM-DD>
   provenance: <one sentence: created by whom, when, why>
   ---
   ```

3. **Write content.** Follow existing style in that section of the archive.

4. **Add cross-links.** Link back to at least one parent doc (e.g., archive index, project board).

5. **Run quality gates locally:**
   ```bash
   python scripts/validate_artifact_metadata.py
   python scripts/check_markdown_links.py
   ```

6. **Open a PR** using branch `feat/your-artifact-name`. Reference the artifact proposal issue if one exists.

7. **Update ARCHIVE_INDEX.md** to include the new artifact.

---

## PB-02: Migrate Legacy Artifact

**Use when:** An existing file lacks the universal frontmatter schema.

**Steps:**

1. **Check current state.** Does the file have `status:` in a header? That's legacy format.

2. **Add full frontmatter** at the top of the file (before any `#` heading):
   ```yaml
   ---
   title: <derive from H1 heading>
   artifact_id: <DOMAIN>-<SLUG>-<original-date-or-2026-05-29>
   status: candidate
   canon_status: candidate
   lifecycle_state: active
   ratification_event_id: pending
   trust_state: WORK
   owner: Atlas Lattice Foundation
   last_updated: <YYYY-MM-DD>
   provenance: Migrated to universal frontmatter schema 2026-05-29.
   ---
   ```

3. **Remove the old inline `status:` line** if it was a standalone line (e.g., `status: candidate`).

4. **Run metadata validation:**
   ```bash
   python scripts/validate_artifact_metadata.py
   ```

5. **Open a PR** using branch `chore/migrate-frontmatter-<filename>`.

---

## PB-03: Fix a Broken Link

**Use when:** A relative Markdown link returns 404.

**Steps:**

1. **Identify the broken link** — CI will flag it, or run:
   ```bash
   python scripts/check_markdown_links.py
   ```

2. **Find the correct target.** Use the [Archive Index](./ARCHIVE_INDEX.md) or `find` in the repo.

3. **Update the link.** Use repo-relative paths from the file's location (e.g., `../docs/GLOSSARY.md`).

4. **Re-run link checks:**
   ```bash
   python scripts/check_markdown_links.py
   ```

5. **Open a PR** using branch `fix/broken-link-<short-description>`.

---

## PB-04: Propose a Fork Synthesis

**Use when:** You want to incorporate an external GitHub repository to fill a gap in the lattice.

**Steps:**

1. **Read the Fork Policy:** [FORK_POLICY.md](../archive/forks/FORK_POLICY.md) — all steps are mandatory.

2. **Open an issue** using the RFC Proposal template with:
   - Upstream repo URL
   - License compatibility check result
   - Gap being filled (which KG node/H-S-N coordinate)
   - Adaptation plan

3. **Get approval** from @atlaslattice before forking.

4. **Fork the repo** on GitHub under `atlaslattice/`.

5. **Add provenance doc** in `archive/forks/<repo-name>/PROVENANCE.md`.

6. **Link to the fork** from the relevant KG node and from `ARCHIVE_INDEX.md`.

7. **Update KG_COVERAGE_DASHBOARD.md** to mark the gap as addressed.

---

## PB-05: Submit a Swarm Task

**Use when:** You have work to propose for the swarm intake queue.

**Steps:**

1. **Use the intake issue template.** Go to: [New Issue → Swarm Intake](https://github.com/atlaslattice/manus-artifacts/issues/new?template=swarm_intake.md)

2. **Fill out all fields** including:
   - Module name
   - 12 tasks
   - Difficulty per task (Low/Med/High)
   - Dependencies
   - Preferred owner

3. **Post the issue.** It enters INTAKE on the [Living Execution Board](../projects/LIVING_EXECUTION_BOARD.md).

4. **An orchestrator** (or @atlaslattice) will triage and assign.

---

## PB-06: Upgrade an Artifact's Status

**Use when:** An artifact has completed council review and is ready for ratification.

**Steps:**

1. **Confirm prerequisites per [Ratification Workflow](./RATIFICATION_WORKFLOW.md):**
   - Source provenance and creation context documented
   - Council review notes recorded
   - No open blockers or `BLOCKED` trust_state

2. **Open an RFC issue** proposing the status upgrade, linking the artifact.

3. **Council review window** — minimum 24 hours open for comments.

4. **If approved** — @atlaslattice adjudicates and assigns `ratification_event_id`.

5. **Update artifact frontmatter:**
   ```yaml
   canon_status: ratified
   ratification_event_id: RAT-<YYYY-MM-DD>-<NNN>
   trust_state: VERIFIED
   ```

6. **Append to [Canon Decision Ledger](./CANON_DECISION_LEDGER.md)**.

7. **Append to [Adjudication Trail](./ADJUDICATION_TRAIL.md)**.

---

## PB-07: Open a Governance RFC

**Use when:** Proposing process, architecture, or policy changes that affect how the whole repo operates.

**Steps:**

1. **Use the RFC Proposal issue template.** Include problem statement, proposed solution, and alternatives considered.

2. **Allow minimum 7-day open comment window.**

3. **Respond to all comments.** Revise proposal if needed.

4. **If approved by @atlaslattice** — implement changes and reference the RFC issue in all changed artifacts.

---

## PB-08: Add Tests for an Artifact

**Use when:** Improving coverage for a spec, schema, or governance artifact.

**Steps:**

1. **Identify the target artifact** and find its KG node (H-S-N coordinate).

2. **Find the right test location:**
   - Schema tests → `tests/adversarial/` or `tests/test_schema_parsing.py`
   - Metadata/link tests → add to `scripts/validate_artifact_metadata.py`
   - KG integrity → `tests/test_lattice_kg_hypercube_program.py`

3. **Write the test** following existing test patterns in the same file.

4. **Run locally:**
   ```bash
   python -m pytest -q <test-file>
   ```

5. **Update [KG_COVERAGE_DASHBOARD.md](./KG_COVERAGE_DASHBOARD.md)** to reflect improved coverage.

6. **Open a PR** using branch `feat/tests-<artifact-slug>`.

---

## Need a Playbook That Doesn't Exist?

Open an issue with label `docs-request` and describe the contribution type. We'll write the playbook.

---

*Playbooks maintained by Atlas Lattice Foundation · Status: Candidate · License: MIT*
