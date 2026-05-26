# Lane Routing Conventions v0.1

> **STATUS: NOT CANON — CANDIDATE WORKING SPEC**
> **DEPLOYMENT: NOT DEPLOYABLE**
> **AUTHORITY: NONE**
> **DATE: 2026-05-26**

---

## Purpose

This document defines lane routing conventions for the GPTDream++ habitat.
A "lane" is an assignment of input packets to specific brain seats based on content type,
epistemic status, and governance requirements.

Lane routing ensures that the right brain handles the right content — and that
TIDELOCKBrain always watches anything that touches code or repositories.

---

## Primary Routing Table

| Input Type | Primary Brain | Secondary Brain | TIDELOCK Required |
|-----------|--------------|----------------|------------------|
| ChatGPT synthesis | LucernaBrain | RootglassBrain | No |
| Task plan | LucernaBrain / HashlightBrain | — | Conditional* |
| Raw export (O_AI) | HashlightBrain | AtlasBrain | No |
| Benchmark claim | AtlasBrain | LucernaBrain | No |
| Code packet | TIDELOCKBrain | — | YES |
| Repo operation | TIDELOCKBrain | — | YES |
| Execution request | D-Φ-1 → CAS-001-A → Atlas/ORCS → TIDELOCK | — | YES |
| Public statement | LucernaBrain | governance review | No |
| Contradiction detection | AtlasBrain | LucernaBrain | No |
| Cross-vendor packet | Per Appendix H routing table | — | Conditional* |
| Native thread ingestion | HashlightBrain (parse) → AtlasBrain (govern) | — | No |

*Conditional: TIDELOCK required if the task plan or cross-vendor packet references repo operations or code execution.

---

## Execution Request Gate Chain

Any execution request MUST follow this exact gate sequence:

```
Execution Request received
         │
         ▼
Step 1: D-Φ-1 Gate
  - receipt present?          NO → REJECT
  - human_permission granted?  NO → REJECT
  - safety_gate == pass?       NO → REJECT
         │ PASS
         ▼
Step 2: CAS-001-A (Atlas/ORCS Audit Anchor)
  - MANDATORY — cannot be bypassed
  - Creates immutable audit anchor
  - Determines if TIDELOCKBrain required
         │
         ▼
Step 3: Full Gate Chain Check
  - All 6 gates must be pass for execution requests
  - provenance_gate, safety_gate, governance_gate,
    data_residency_gate, human_permission_gate, receipt_gate
         │ ALL PASS
         ▼
Step 4: TIDELOCKBrain (if repo/code/merge/CI)
  - Code execution
  - Repo operations
  - Merge requests
  - CI/CD pipelines
  - Dependency updates
         │
         ▼
Execute
```

---

## TIDELOCK Trigger Conditions

TIDELOCKBrain oversight is MANDATORY when:

1. `content_type` is `code`, `execution_request`, `repo_operation`, `merge`, or `ci_cd`
2. Packet references a git repository, branch, merge request, or commit
3. Packet requests file creation, modification, or deletion
4. Packet requests CI/CD operations
5. Packet involves dependency updates or version changes
6. Packet involves merge-order decisions

---

## Atlas/ORCS Audit Trigger Conditions

Atlas/ORCS audit event is MANDATORY when:

1. Any `authority_scope` promotion is requested
2. `canon_status` change is requested
3. `deployment_status` change is requested
4. Cross-vendor packet involves meaning promotion
5. Ratification event is being logged
6. Execution request is processed (any outcome)
7. Contradiction is detected

---

## Brain Lane Registry

| Lane ID | Brain | Primary Functions |
|---------|-------|-----------------|
| `lucerna` | LucernaBrain | ChatGPT synthesis, public statements, benchmark review |
| `rootglass` | RootglassBrain | Secondary synthesis review, canon candidate prep |
| `tidelock` | TIDELOCKBrain | Repo operations, merge order, code execution, audit trail |
| `hashlight` | HashlightBrain | Raw export ingestion, provenance verification, data hashing |
| `atlasbrain` | AtlasBrain | Governance state, ratification events, contradiction handling |
| `lumenwrightvalc` | LumenwrightValeBrain | Additional synthesis capacity |
| `aster` | AsterBrain (S1-A) | S1 seat A |
| `lumen` | LumenBrain (S1-B) | S1 seat B |

---

## Anti-Routing Rules

The following routing patterns are PROHIBITED:

1. **Execution without TIDELOCK**: Code execution may not be routed around TIDELOCKBrain.
2. **Authority promotion without Atlas/ORCS**: Any `authority_scope` increase requires Atlas/ORCS event.
3. **Ratification without council**: Self-routing to ratified state without governance event.
4. **Bypass of D-Φ-1**: No execution request may skip the D-Φ-1 gate.
5. **CAS-001-A bypass**: The Atlas/ORCS audit anchor is not optional.

---

## Canon Boundary

This document is **NOT CANON**. Lane routing conventions become canon only after full council ratification + @atlaslattice adjudication + website publication.

---

*End of LANE_ROUTING_CONVENTIONS_v0.1.md*
