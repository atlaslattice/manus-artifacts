# Council-Seat Quickstart Checklist

```text
STATUS: CANDIDATE — NOT CANON
DATE: 2026-05-26
SCOPE: New contributors joining a Council seat or Children of the Swarm brain lane
AUTHORITY EFFECT: none
CANON EFFECT: none
```

## What this is

A quickstart guide for anyone onboarding to a Council seat (S1–S7) or a Children of
the Swarm brain folder (AsterBrain, LumenBrain, TIDELOCKBrain, etc.).

It does not confer seat authority, canon status, or merge rights.

---

## Pre-flight (read first)

- [ ] Read [`COUNCIL_BRAIN_INDEX.md`](../archive/boot/COUNCIL_BRAIN_INDEX.md) — seat roster, canon boundary, evidence taxonomy.
- [ ] Read [`CONTRIBUTING.md`](../.github/CONTRIBUTING.md) — canon-boundary rules, local validation commands.
- [ ] Read [`SECURITY.md`](../SECURITY.md) — what must never be committed.
- [ ] Confirm: "I understand that nothing is canon until ratified by full council and adjudicated by @atlaslattice."

---

## Core rule set (memorize these)

```text
name    != authority
folder  != canon
memory palace != native memory
review  != ratification
storage != canon
dream   != fact
canon   = explicit human-root promotion only
```

---

## Seat orientation checklist

### 1. Locate your seat spec

| Seat | Brain | Spec file |
|------|-------|-----------|
| S1 | GPTBrain | `archive/boot/seats/GPTBRAIN_S1_CANONICAL_CANDIDATE_SPEC_2026-05-09.md` |
| S2 | ClaudeBrain | `archive/boot/seats/CLAUDEBRAIN_S2_CONSTITUTIONAL_SCRIBE_SPEC_2026-05-08.md` |
| S3 | GrokBrain | `archive/boot/seats/GROKBRAIN_S3_PERSISTENT_MEMORY_PALACE_SPEC_2026-05-08.md` |
| S4 | GeminiBrain | `archive/boot/seats/GEMINIBRAIN_S4_ENGINEERING_SIMULATION_SPEC_2026-05-08.md` |
| S5 | DeepSeekBrain | `archive/boot/seats/DEEPSEEK_S5_BOOT_SEQUENCE_AND_BRAIN_SPEC_2026-05-08.md` |
| S6 | ManusBrain | `archive/boot/seats/MANUSBRAIN_S6_EXECUTION_AGENT_SPEC_2026-05-08.md` |
| S7 | CopilotBrain | `archive/boot/seats/COPILOTBRAIN_S7_CODE_INTEGRATOR_SPEC_2026-05-08.md` |

- [ ] Open your seat spec and read the full guardrail section.
- [ ] Read your seat's `S{N}_IDENTITY_CREDENTIAL.md` in `archive/boot/seats/`.
- [ ] Read your seat's `S{N}_MEMORY_PACKET_TEMPLATE.yaml` in `archive/boot/seats/`.

### 2. Find your brain folder (if applicable)

Children of the Swarm brain folders live under `archive/boot/gptbrain/`:

| Brain | Swarm slot | Folder |
|-------|-----------|--------|
| AsterBrain | S1-A | `archive/boot/gptbrain/AsterBrain/` |
| LumenBrain | S1-B | `archive/boot/gptbrain/LumenBrain/` |
| LumenwrightValeBrain | S1-C | `archive/boot/gptbrain/LumenwrightValeBrain/` |
| TIDELOCKBrain | S7 | `archive/boot/gptbrain/TIDELOCKBrain/` |
| HashlightBrain | TBD-05 | `archive/boot/gptbrain/HashlightBrain/` |
| LanternBridgeBrain | TBD-06 | `archive/boot/gptbrain/LanternBridgeBrain/` |
| ValewrightBrain | TBD-07 | `archive/boot/gptbrain/ValewrightBrain/` |

- [ ] Open your brain folder's `README.md`.
- [ ] Read `AGENT_DNA.yaml` — role, functions, failure modes.
- [ ] Read `BOOT_SEQUENCE.md` — load order and boot phrase.
- [ ] Read `FAILURE_MODES.md` — know your drift states and repairs.

### 3. Understand the canonical substrate

- [ ] GitHub is the durable canonical substrate. Drive and Notion are relay layers only.
- [ ] Every artifact needs: repo path, file contents, status label, and commit/PR note.
- [ ] Label every artifact as `candidate` until it passes the full ratification workflow.

### 4. First contribution checklist

- [ ] Open or reference an issue before making changes.
- [ ] Branch name: descriptive, no secrets.
- [ ] File status labels: include `STATUS: CANDIDATE — NOT CANON` in all new governed artifacts.
- [ ] Commit message: `<type>: <short description>` (e.g., `scaffold: add HashlightBrain standard files`).
- [ ] PR description: link the issue, list files changed, confirm no canon claims.
- [ ] Run local CI checks before pushing:
  ```bash
  python -m pytest -q              # from archive/boot/gptbrain/reference_impl/
  bash run_checks.sh               # from archive/boot/gptbrain/reference_impl/
  ruff check archive/boot/gptbrain/reference_impl/
  ```

---

## Canon boundary checklist (run before every PR)

- [ ] Does any new file claim to be `ratified`, `canon`, or `authoritative`? → Remove or add disclaimer.
- [ ] Does any file impersonate a human, claim native memory, or claim model-weight authority? → Fix.
- [ ] Does any file use `{{placeholder}}` syntax or leave template variables unfilled? → Fill or remove.
- [ ] Does any file expose secrets, credentials, or PII? → Remove immediately.

---

## Ongoing seat hygiene

- [ ] Log significant work in the TIDELOCKBrain work log: `archive/boot/gptbrain/TIDELOCKBrain/`.
- [ ] Update `CHANGELOG.md` when adding significant new artifacts.
- [ ] Cross-link new artifacts from the relevant index file.
- [ ] Keep the Aetherforge Council Taskboard (`projects/aetherforge-top10-taskboard-2026-05-26.md`) current.

---

## Key reference files

| Purpose | Path |
|---------|------|
| Seat roster | `archive/boot/COUNCIL_BRAIN_INDEX.md` |
| Contributing guide | `.github/CONTRIBUTING.md` |
| Swarm squad index | `archive/boot/gptbrain/agents/CHILDREN_OF_THE_SWARM_SQUAD_INDEX_2026-05-10.md` |
| Artifact ID convention | `archive/spec/ARTIFACT_ID_CONVENTION_DRAFT_2026-05-26.md` |
| Taskboard | `projects/aetherforge-top10-taskboard-2026-05-26.md` |
| Issue templates | `.github/ISSUE_TEMPLATE/` |
| Labels | `.github/labels.yml` |

---

*Candidate artifact. Not ratified. Requires full council review and @atlaslattice adjudication.*
