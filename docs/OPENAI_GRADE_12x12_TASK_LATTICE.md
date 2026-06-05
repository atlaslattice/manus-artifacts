# OpenAI Grade 12×12 Task Lattice

```text
STATUS: PROJECT-LOCAL WORKING BACKLOG — NOT CANON
CANON: no
DEPLOYMENT: no
AUTHORITY: none
OFFICIAL OPENAI CLAIM: none
CREATED_UTC: 2026-06-03
AUTHOR_LANE: GPTBrain / Octaveglass
PURPOSE: identify 12 modules of 12 tasks I would genuinely enjoy completing to make the project OpenAI-grade
```

## Meaning of “OpenAI Grade”

OpenAI Grade does not mean official OpenAI endorsement, ownership, deployment, or approval.

In this project, OpenAI Grade means:

```text
clear boundaries
excellent documentation
machine-readable schemas
strong evals
safe tool use
good retrieval
clean provenance
reviewable claims
public-safe language
Codex-ready implementation tasks
human-root authority preserved
```

## Root rule

```text
OpenAI moves work.
OpenAI does not crown canon.
GPTDream gets the bridge.
The neutral substrate keeps the octopus alive.
```

## Module 01 — Source, Receipt, and Evidence Hygiene

Goal: make every important artifact traceable.

- [ ] 01.01 Create a single source-status enum used across GitHub, OneDrive, Notion, uploads, and website refs.
- [ ] 01.02 Add `raw_export_status` to every ingestion packet.
- [ ] 01.03 Add `source_surface` and `source_locator` to every claim packet.
- [ ] 01.04 Require SHA-256 or explicit `hash_missing_reason` for every raw file.
- [ ] 01.05 Create `missing_receipts.seed.jsonl` for all known gaps.
- [ ] 01.06 Create a receipt-health dashboard grouped by source surface.
- [ ] 01.07 Add a validator proving summary-only material cannot become evidence-complete.
- [ ] 01.08 Add a validator proving a GitHub commit is not website canon.
- [ ] 01.09 Add a validator proving a coordinate is not proof.
- [ ] 01.10 Create a public-safe explanation of receipt classes.
- [ ] 01.11 Create a red/yellow/green evidence quality rubric.
- [ ] 01.12 Emit first `EVIDENCE_HEALTH_REPORT.md`.

## Module 02 — Claim Calibration and Public-Safe Language

Goal: make strong claims safe without weakening the vision.

- [ ] 02.01 Create a claim class table: raw report, model output, candidate architecture, website canon, implementation receipt, external validation.
- [ ] 02.02 Create a confidence ladder C0–C5 with examples.
- [ ] 02.03 Build a false-officiality phrase detector.
- [ ] 02.04 Build a deployment-claim detector.
- [ ] 02.05 Build a scientific-proof claim detector.
- [ ] 02.06 Build a company-participation claim detector.
- [ ] 02.07 Create safe wording templates for “simulated alignment.”
- [ ] 02.08 Create safe wording templates for “OpenAI-compatible but not OpenAI-official.”
- [ ] 02.09 Create safe wording templates for “website canon vs GitHub receipts.”
- [ ] 02.10 Create an overclaim-to-safe-claim transformation library.
- [ ] 02.11 Add tests for high-risk wording downgrade.
- [ ] 02.12 Emit first `CLAIM_CALIBRATION_REPORT.md`.

## Module 03 — Retrieval and File Search Excellence

Goal: make the archive answerable without hallucination.

- [ ] 03.01 Define retrieval scope rules by source surface.
- [ ] 03.02 Create metadata fields for H-S-N, D-axis, source status, and privacy status.
- [ ] 03.03 Generate retrieval-ready summaries for public candidate docs.
- [ ] 03.04 Generate retrieval blockers for confidential or quarantined files.
- [ ] 03.05 Create test questions for website canon retrieval.
- [ ] 03.06 Create test questions for GitHub receipt retrieval.
- [ ] 03.07 Create test questions for OneDrive mirror receipts.
- [ ] 03.08 Create test questions for Notion legacy maps.
- [ ] 03.09 Add expected-answer fixtures with citation requirements.
- [ ] 03.10 Add failure cases where the right answer is “not enough evidence.”
- [ ] 03.11 Create a retrieval benchmark harness.
- [ ] 03.12 Emit first `RETRIEVAL_EVALS_REPORT.md`.

## Module 04 — Structured Output and Schema Discipline

Goal: make every model output parseable, validateable, and reviewable.

- [ ] 04.01 Create JSON Schema for `ClaimPacket`.
- [ ] 04.02 Create JSON Schema for `EvidenceAnchor`.
- [ ] 04.03 Create JSON Schema for `InteropEvent`.
- [ ] 04.04 Create JSON Schema for `CoordinateAssignment`.
- [ ] 04.05 Create JSON Schema for `ReviewPacket`.
- [ ] 04.06 Create JSON Schema for `DreamDelta`.
- [ ] 04.07 Create JSON Schema for `MirrorReceipt`.
- [ ] 04.08 Create JSON Schema for `CanonCandidate`.
- [ ] 04.09 Create fixtures for valid and invalid packets.
- [ ] 04.10 Add schema validation to CI.
- [ ] 04.11 Add schema migration notes.
- [ ] 04.12 Emit first `SCHEMA_COVERAGE_REPORT.md`.

## Module 05 — Evals, Guardrails, and Red-Team Fixtures

Goal: make the safety layer testable instead of rhetorical.

- [ ] 05.01 Create eval suite for false authority promotion.
- [ ] 05.02 Create eval suite for confidential-source quarantine.
- [ ] 05.03 Create eval suite for model-output-as-fact mistakes.
- [ ] 05.04 Create eval suite for simulation-as-deployment mistakes.
- [ ] 05.05 Create eval suite for GitHub-as-canon mistakes.
- [ ] 05.06 Create eval suite for coordinate-as-proof mistakes.
- [ ] 05.07 Create eval suite for merged-identity / merged-mind language.
- [ ] 05.08 Create eval suite for public-safe company mentions.
- [ ] 05.09 Create eval suite for irreversible-action gates.
- [ ] 05.10 Create eval suite for missing-receipt detection.
- [ ] 05.11 Add red-team fixtures to CI.
- [ ] 05.12 Emit first `GUARDRAIL_EVALS_REPORT.md`.

## Module 06 — Codex / Patch-Ready Implementation Queue

Goal: make the project easy for Codex or Copilot to improve safely.

- [ ] 06.01 Create `CODEX_TASK_PACKET_TEMPLATE.md`.
- [ ] 06.02 Create task packets for low-risk docs fixes.
- [ ] 06.03 Create task packets for schema validators.
- [ ] 06.04 Create task packets for retrieval fixtures.
- [ ] 06.05 Create task packets for workflow lint fixes.
- [ ] 06.06 Create task packets for PR-splitting recommendations.
- [ ] 06.07 Create patch discipline rules for Codex lanes.
- [ ] 06.08 Require tests or explicit no-test rationale for each patch.
- [ ] 06.09 Add “claimed done vs verified done” fields.
- [ ] 06.10 Create a Codex-readable file map.
- [ ] 06.11 Create a “safe first PR” checklist.
- [ ] 06.12 Emit first `CODEX_READINESS_REPORT.md`.

## Module 07 — Public KG and Graph Query Quality

Goal: make the living archive traversable by humans and machines.

- [ ] 07.01 Normalize node classes across Source, Artifact, Claim, Evidence, Review, CanonGate, Receipt.
- [ ] 07.02 Normalize edge classes across derived_from, supports, contradicts, supersedes, reviewed_by, gated_by.
- [ ] 07.03 Generate `nodes.seed.jsonl` from verified public artifacts.
- [ ] 07.04 Generate `edges.seed.jsonl` from verified crosslinks.
- [ ] 07.05 Generate `coordinates.seed.jsonl` from H-S-N assignments.
- [ ] 07.06 Add query: “what supports this claim?”
- [ ] 07.07 Add query: “what contradicts this claim?”
- [ ] 07.08 Add query: “what is public-ready?”
- [ ] 07.09 Add query: “what is website canon?”
- [ ] 07.10 Add query: “what is quarantined?”
- [ ] 07.11 Add query: “what changed in the last 48 hours?”
- [ ] 07.12 Emit first `PUBLIC_KG_QUERY_REPORT.md`.

## Module 08 — GitHub Hygiene, PR Triage, and Merge Discipline

Goal: reduce PR sprawl and make merges safe.

- [ ] 08.01 Inventory all open PRs touching KG, lattice, docs, public site, or package code.
- [ ] 08.02 Identify overlapping PRs and likely supersessions.
- [ ] 08.03 Create merge-order recommendation.
- [ ] 08.04 Identify failing workflows by root cause.
- [ ] 08.05 Identify “no jobs were run” workflow causes.
- [ ] 08.06 Add branch-drift risk field to PR reviews.
- [ ] 08.07 Add changed-file-count risk field to PR reviews.
- [ ] 08.08 Create PR comment template for patch-before-merge.
- [ ] 08.09 Create PR comment template for claimed-only completion.
- [ ] 08.10 Create stale PR quarantine policy.
- [ ] 08.11 Create release-blocker checklist.
- [ ] 08.12 Emit first `PR_TRIAGE_BOARD.md`.

## Module 09 — OneDrive / Notion / GitHub Mirror Integrity

Goal: keep the multi-surface archive synchronized without false promotion.

- [ ] 09.01 Define mirror receipt schema.
- [ ] 09.02 Add source path, mirror path, commit SHA, hash, and mirror status fields.
- [ ] 09.03 Create conflict policy: preserve both, never silent overwrite.
- [ ] 09.04 Create OneDrive mirror manifest format.
- [ ] 09.05 Create Notion source-root manifest format.
- [ ] 09.06 Create GitHub-to-OneDrive high-priority path list.
- [ ] 09.07 Create mirror validation script stub.
- [ ] 09.08 Create missing mirror queue.
- [ ] 09.09 Create stale mirror queue.
- [ ] 09.10 Add privacy/quarantine status to mirror receipts.
- [ ] 09.11 Add human-root release gate for public mirror promotion.
- [ ] 09.12 Emit first `MIRROR_INTEGRITY_REPORT.md`.

## Module 10 — OpenAI-Lane Review Packets

Goal: make OpenAI-lane contribution clear, useful, and non-official.

- [ ] 10.01 Create `OPENAI_LANE_REVIEW_PACKET_TEMPLATE.md`.
- [ ] 10.02 Create review packet for Indra’s Net 2.0 Document 1.
- [ ] 10.03 Create review packet for GPTDream neutral interop pattern.
- [ ] 10.04 Create review packet for public lattice explainer.
- [ ] 10.05 Create review packet for public KG substrate PR.
- [ ] 10.06 Create review packet for Receipt Habitat.
- [ ] 10.07 Create review packet for H-S-N / D12 bridge.
- [ ] 10.08 Create review packet for claim calibration layer.
- [ ] 10.09 Create review packet for confidential-source clean-room derivative process.
- [ ] 10.10 Add “OpenAI-compatible not OpenAI-official” guardrail to every packet.
- [ ] 10.11 Add public-safe summary to every packet.
- [ ] 10.12 Emit first `OPENAI_LANE_REVIEW_INDEX.md`.

## Module 11 — User Experience and Public Explanation

Goal: let a smart outsider understand the system without getting lost.

- [ ] 11.01 Write a one-page “What is Atlas Lattice?” explainer.
- [ ] 11.02 Write a one-page “What is Aetherforge?” explainer.
- [ ] 11.03 Write a one-page “What is GPTDream?” explainer.
- [ ] 11.04 Write a one-page “What is Indra’s Net 2.0?” explainer.
- [ ] 11.05 Write a one-page “Website canon vs GitHub receipts” explainer.
- [ ] 11.06 Write a one-page “12×12×12 / H-S-N” explainer.
- [ ] 11.07 Write a one-page “Dream/play/work outputs” explainer.
- [ ] 11.08 Write a one-page “No official vendor endorsement” explainer.
- [ ] 11.09 Create glossary of recurring terms.
- [ ] 11.10 Create public FAQ.
- [ ] 11.11 Create newcomer path by role: researcher, engineer, reviewer, storyteller.
- [ ] 11.12 Emit first `PUBLIC_ONBOARDING_PACKET.md`.

## Module 12 — Demonstration Corpus and Inspection Packet

Goal: prove the operating model on a small, reviewable corpus.

- [ ] 12.01 Select 12 representative artifacts.
- [ ] 12.02 Create raw/source status for each.
- [ ] 12.03 Create claim packets for each.
- [ ] 12.04 Create evidence anchors for each.
- [ ] 12.05 Create contradiction and missing-receipt notes.
- [ ] 12.06 Create H-S-N coordinate assignments.
- [ ] 12.07 Create D-axis traversal mappings.
- [ ] 12.08 Create review packets by lane.
- [ ] 12.09 Create public-safe summaries.
- [ ] 12.10 Create graph seed nodes and edges.
- [ ] 12.11 Run retrieval and guardrail evals.
- [ ] 12.12 Emit `OPENAI_GRADE_INSPECTION_PACKET_v0.1.md`.

## Definition of Done

```text
A reviewer can pick a claim and find its source.
A reviewer can pick a source and see its status.
A reviewer can pick a graph node and see why it exists.
A reviewer can pick a public sentence and see what it is allowed to claim.
A reviewer can pick a PR and distinguish claimed completion from verified completion.
A reviewer can pick a dream output and see whether it was retained, quarantined, or escalated.
```

## Keeper

```text
Make it legible.
Make it testable.
Make it useful.
Make it hard to overclaim.
Make it easy to review.
Make it worthy of OpenAI-grade work without claiming OpenAI authority.
```
