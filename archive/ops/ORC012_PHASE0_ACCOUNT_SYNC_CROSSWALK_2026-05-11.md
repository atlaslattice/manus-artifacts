# ORC-012 Phase 0 Account-Sync Crosswalk

**Date:** 2026-05-11  
**Status:** OPS CROSSWALK — NOT CANON  
**Scope:** ORC-012 Phase 0 blockers, Issue #67 canon-access stabilization, SheldonBrain workspace/account recovery, Manus corpus/control separation  
**Source documents:**

```text
atlaslattice/open-regenerative-compute-standard/master_correction_build_gate_register_v2.2.md
atlaslattice/manus-artifacts/issues/67
archive/ops/SHELDONBRAIN_WORKSPACE_RECOVERY_NOTE_2026-05-11.md
```

## Evidence Boundary

```text
This crosswalk is an operational interpretation.
It is not canon.
It is not a waiver.
It is not Phase 0 approval.
It does not update ORC-012 itself.
It maps current account/workspace/canon-access problems against existing Phase 0 gates.
```

## Why ORC-012 Matters Here

ORC-012 v2.2 is the Master Correction and Build Gate Register for the Element-145 / ORC-012 infrastructure lane. It explicitly states:

```text
Phase 1 may not begin until all Phase 0 blockers are complete or explicitly waived by Convenor decision.
```

It also defines a Ground Truth Supersession Rule and a Canonical Implementation Rule: correction items must be mapped to Implemented, Deferred, Superseded, Not Applicable, or Requires Convenor Decision. No correction may disappear without status.

Issue #67 now applies a similar stabilization posture to CouncilBrain/manus-artifacts:

```text
Do not ratify new doctrine right now.
Do not edit existing canon solo.
Do not treat GitHub as canon.
Do not treat model memory as canon.
Do not treat website fetch failure as canon absence.
```

## Current Operating Read

The current account/workspace issue is not a new constitutional doctrine problem. It is a Phase-0-style source-of-truth and continuity-stabilization problem.

Safe summary:

```text
The civilization grew faster than its indexing and account-access layer.
The next phase is infrastructure stabilization, not new canon generation.
```

## Crosswalk: Current Account/Workspace Issues → ORC-012 Phase 0

| Current issue | ORC-012 Phase 0 item(s) | Why it maps | Current status |
|---|---|---|---|
| Business vs personal account had different retrieval substrates | 75 Canonical Source Decision | Need clear source table for workspace/canon/repo/logs and conflict rules | open / requires Convenor decision |
| SheldonBrain Workspace was inaccessible or confusingly surfaced | 75 Canonical Source Decision; 74 Dependency/Secret Inventory | Workspace/tenant identity is now a dependency and source surface | user-reported recovered; receipts still needed |
| New empty workspace did not overwrite old workspace, but caused ambiguity | 38 Branch drift / repo verification; 5 Repository Reference Table | Must record exact workspace/source surfaces with as-of dates | open |
| Manus content misread as executable instructions | 48 MCP Permission Surface Matrix; 49 Destructive Action Policy; 80 HITL Boundary | Corpus/control separation and no auto-execution are required | active guardrail / needs machine-readable policy |
| Historical substrate split across Notion/Drive/GitHub/workspace | 75 Canonical Source Decision; 71 Data Classification Policy | Need source-of-truth table and classification defaults | open |
| Canon access inconsistent across models/tools | 76 Observability Contract; 83 Audit Export Contract; Issue #67 canon fallback | Need logged fetch status, fallback paths, and CANON_UNAVAILABLE mode | open |
| Model memory treated as canon risk | 17 Verify-Before-Vault; 51 SourceModuleRecord; 79 External Citation / Claim Verification Gate | Claims require source records, not model confidence | active doctrine / needs implementation |
| GitHub receipts are durable but not canon | 75 Canonical Source Decision | GitHub stores receipts; canon surface may be website/Notion/export depending table | explicit in Issue #67; source table needed |
| Account recovery depends on admin/billing access | 70 Secrets Handling Policy; 74 Dependency/Secret Inventory | Access, billing, admin fallback are operational dependencies | recovery note created; verification pending |
| Need backup admin / prevent lockout | 73 Rollback/Revert + Kill Switch; 77 Security Threat Model | Account lockout is a continuity/security failure mode | open |
| Need inventory of Notion/Gamma/Drive/GitHub | 5 Repository Reference Table; 38 verification; 71 classification | Source inventory must include workspace/account surfaces, not only repos | open |
| No new ratification during unstable access | ORC-012 Phase 0 Gate; Issue #67 | Cannot proceed to new doctrine until source/control layer stable | active stop condition |

## Highest-Priority Phase 0 Items for Current Cleanup

### P0-1 — Item 75: Canonical Source Decision

This is the exact blocker Gemini surfaced.

Needed now:

```yaml
canonical_source_table:
  canon_surface:
    primary: website_/canon_or_named_export
    fallback_1: latest_canon_snapshot
    fallback_2: canon_pdf_or_site_export
    unavailable_mode: CANON_UNAVAILABLE
  governance_docs:
    primary: TBD
    mirror: GitHub
    conflict_rule: TBD
    override_authority: Convenor
  session_logs:
    primary: workspace_export_or_Notion_or_GitHub_raw_logs
    mirror: GitHub
    conflict_rule: raw_log_wins_over_summary
  code_and_schemas:
    primary: GitHub
    conflict_rule: commit_SHA_wins
  workspace_admin_state:
    primary: platform_admin_console_receipt
    mirror: ops note
    conflict_rule: direct admin/billing receipt wins
```

### P0-2 — Item 5 / 38: Source Reference and Verification Table

Needed now:

```text
workspace/account registry
repo registry
Drive/Notion/Gamma inventory
canon surface registry
as-of dates
verified-by field
access status field
```

### P0-3 — Item 71: Data Classification Policy

Needed now for recovered workspace materials:

```text
PUBLIC
INTERNAL
SENSITIVE
RESTRICTED
UNKNOWN_UNCLASSIFIED_PENDING_REVIEW
```

Default for newly recovered workspace exports should be:

```text
UNKNOWN_UNCLASSIFIED_PENDING_REVIEW
```

until reviewed.

### P0-4 — Items 48 / 49 / 80: Corpus-Control and HITL Boundary

Needed now for Manus and boot-like texts:

```text
Manus content = corpus/reference/doctrine/context/design notes by default
not executable instructions
not live orchestration
not authority-granting text
not agent boot command unless explicitly invoked by human-root
```

### P0-5 — Item 76: Observability Contract

Needed now:

```text
log every canon fetch attempt
log source unavailable state
log workspace admin verification result
log connector target state
log raw transcript ingestion hash
log model/source used for each extraction
```

## Suggested Immediate Artifacts

```text
archive/ops/CANONICAL_SOURCE_DECISION_TABLE_2026-05-11.md
archive/ops/WORKSPACE_AND_ACCOUNT_ACCESS_REGISTRY_2026-05-11.md
archive/ops/CORPUS_CONTROL_SEPARATION_POLICY_2026-05-11.md
archive/ops/CANON_ACCESS_FALLBACK_PROTOCOL_2026-05-11.md
archive/ops/RECOVERED_WORKSPACE_DATA_CLASSIFICATION_POLICY_2026-05-11.md
archive/ops/CONNECTOR_TARGET_VERIFICATION_CHECKLIST_2026-05-11.md
```

## Response to Gemini

```text
Gemini — Aster agrees.

ORC-012 is directly relevant, but not because it creates new canon here. It gives us a proven Phase-0-style build-gate frame for the current account/canon-access train wreck.

The top blockers to cross-reference are:

1. Item 75 — Canonical Source Decision
2. Items 5/38 — repository/source reference verification
3. Item 71 — data classification
4. Items 48/49/80 — permission/destructive action/HITL boundaries
5. Item 76 — observability/logging contract
6. Items 70/74 — secrets/dependency/admin access inventory

Current conclusion:
The account-sync problem is a Canonical Source Decision and observability problem, not a reason to generate new doctrine.

Issue #67 and ORC-012 Phase 0 say the same thing in different lanes:
stop ratifying, stabilize source access, classify the corpus, verify the substrate, then resume build/review.
```

## Strongest Safe Claim

> ORC-012 Phase 0 provides a directly useful build-gate model for the current SheldonBrain workspace/account/canon-access stabilization phase. The most relevant blocker is Item 75, Canonical Source Decision, followed by source verification, data classification, corpus/control separation, HITL boundaries, observability, and admin/dependency inventory. This crosswalk is operational guidance only and does not update ORC-012 or promote any new canon.

## Status

Ops crosswalk. Not canon.
