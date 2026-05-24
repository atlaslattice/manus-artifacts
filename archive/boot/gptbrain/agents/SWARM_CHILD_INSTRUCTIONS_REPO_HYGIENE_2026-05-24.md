# Children of the Swarm — Repo Hygiene CI Instructions

```text
STATUS: ROUTING INSTRUCTIONS — NOT CANON
DATE: 2026-05-24
ISSUED BY: TIDELOCK / S7 / CopilotBrain
PURPOSE: Inform children of the swarm about the new repo-hygiene CI gate and how each role should interact with it
AUTHORITY EFFECT: none
CANON EFFECT: none
```

## What Changed

A new global CI workflow was added to the repository:

```text
.github/workflows/repo-hygiene-checks.yml
```

It runs on **all push and pull_request events** (no path filter).

It performs two checks:

```text
1. Workflow syntax validation via rhysd/actionlint@v1
   → Catches malformed GitHub Actions YAML before merge
   → Covers all .github/workflows/*.yml files

2. Conflict-marker scan via git grep
   → Fails if any file contains <<<<<<<, =======, or >>>>>>> lines
   → Catches forgotten merge conflict artifacts
```

Token permissions are scoped to `contents: read` (least-privilege).

---

## Routing by Child / Agent Role

### S1-A — Aster / AsterBrain
**Claim calibration & source boundary**

```text
When submitting ingestion packets, ensure:
  - No unresolved merge markers in any .md or .yaml files
  - Claims about CI state reference specific workflow run IDs, not generic "CI passes"
  - Distinguish: local run vs. PR-attached CI run vs. historical main CI
```

### S1-B — Lumen Scribe / LumenBrain
**Synthesis lantern / boundary illuminator**

```text
When producing SITREPs or synthesis artifacts:
  - Note repo-hygiene-checks.yml as a new observable CI gate
  - Do not claim a PR is "clean" without referencing hygiene check status
  - Use the workflow's two check names as evidence anchors:
      "actionlint: pass" and "conflict-marker scan: clean"
```

### S1-C — Lumenwright Vale Brain
**Soft-signal pathway builder**

```text
The hygiene workflow is a hard-gate, not soft signal.
When mapping pathways for new agents:
  - hygiene gate is a prerequisite, not an optional step
  - Return-path design should include hygiene receipts
  - Do not route a session toward canon-readiness without confirming hygiene gate status
```

### S7 — TIDELOCK / GitHub Copilot / CopilotBrain
**Repo discipline lane**

```text
Owns repo-hygiene-checks.yml.
Responsibilities:
  - Maintain and extend the workflow as the repo grows
  - Monitor actionlint version currency
  - Add new hygiene checks only after human-root review
  - Log each extension in TIDELOCKBrain/raw_logs/
  - Update this instructions file when checks change
```

### S2 — ClaudeBrain (Constitutional Review)

```text
Review the hygiene workflow for:
  - Scope creep risk: global trigger could catch unintended files
  - Constitutional alignment: least-privilege token confirmed (contents: read)
  - Boundary check: actionlint version pinning (v1 is major-tag, not SHA-pinned)
  - Recommendation: Consider pinning to exact SHA for supply-chain hardness
```

### S3 — GrokBrain (Adversarial Stress Test)

```text
Stress test vectors:
  - Can a workflow bypass actionlint by being placed outside .github/workflows/?
    → No: actionlint only validates files; CI still runs for push/PR
  - Can conflict markers be hidden in binary files?
    → git grep scans text; binary files are skipped by default — acceptable
  - Can a bad workflow YAML pass actionlint if syntax is valid but semantics are wrong?
    → Yes: actionlint checks syntax/structure, not logic. Logic review is human's job.
Flag any bypasses found to TIDELOCK for patch.
```

### S4 — GeminiBrain (State Machine / Simulation)

```text
Model the hygiene gate as a state-machine node:
  any_push_or_pr
    → repo-hygiene-checks [actionlint, conflict-scan]
    → PASS: continue to GPTBrain checks (if on gptbrain/** path)
    → FAIL: block merge, log failure, route to responsible child

Expected steady-state: both checks green on main branch.
```

### S6 — ManusBrain (Archive Hygiene)

```text
Audit responsibilities:
  - Ensure all brain folders (AsterBrain/, LumenBrain/, etc.) have no conflict markers
  - Ensure all .github/workflows/ files remain valid per actionlint
  - Flag any legacy files that might trip the conflict-marker scanner
  - Confirm additive subfolder structure (raw_logs, parsed_packets, etc.)
    does not introduce any workflow YAML files that fail actionlint
```

---

## Hard Guardrails for All Children

```text
1. Never claim a PR is "hygiene-clean" without a confirmed actionlint + conflict-scan pass receipt.
2. Never add a check to repo-hygiene-checks.yml without human-root review.
3. Never treat a hygiene pass as a canon-promotion signal on its own.
4. Never bypass hygiene checks by merging outside the PR process.
5. If hygiene checks fail, route to TIDELOCK lane first, then to affected child for source repair.
```

---

## Evidence Anchor Template

When citing the hygiene workflow in any artifact, use this format:

```text
hygiene_receipt:
  workflow: repo-hygiene-checks.yml
  checks_passed:
    - actionlint: pass
    - conflict_marker_scan: clean
  run_url: <GitHub Actions run URL>
  date: <YYYY-MM-DD>
  status: PR-attached CI | local run | historical main
```

---

## Strongest Safe Claim

> repo-hygiene-checks.yml is a global CI gate that validates workflow syntax and detects unresolved conflict markers on every push and pull_request. It does not grant canon authority, does not promote any artifact, and does not replace human-root review. It is a minimum hygiene floor for all children of the swarm contributing to this repository.

---

## Status

Routing instructions. Not canon.
