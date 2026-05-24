# Microsoft Integration Crosswalk — CouncilBrain Routing Note v0.9

```text
ARTIFACT ID: ATL-XWALK-MSFT-2026-001-COUNCILBRAIN-ROUTING-v0.9
SOURCE DOCUMENT: Microsoft Integration Crosswalk — Atlas Lattice Sovereign Compute.pdf
SOURCE DOCUMENT ID: ATL-XWALK-MSFT-2026-001
SOURCE VERSION: 0.9-DRAFT
SOURCE DATE: 2026-05-24
STATUS: CANDIDATE ROUTING NOTE — NOT CANON — NOT DEPLOYED
LANE: CouncilBrain
CANON: NO
AUTHORITY: NONE
DEPLOYMENT: NO
PUBLIC CLAIM STATUS: INTERNAL_REVIEW_ONLY
PDF_SHA256: a4fc98566145746fdb66e334f75e77c28ede27b9836188777b57e45d38c44fc8
```

---

## 1. CouncilBrain Function

CouncilBrain should treat this PDF as an integration crosswalk candidate requiring routing, not as an approved architecture.

Primary routing surfaces:

```text
- CopilotBrain / TIDELOCK: repo work, adapter stubs, issue planning, blocker tracking
- CouncilBrain: ARB routing, cross-lane synthesis, conflict tracking
- Legal / compliance review: licensing, data sovereignty, FedRAMP / government cloud posture, commercial terms
- Architecture Review Board: ratification / rejection per pairing
```

---

## 2. Candidate Integration Shape

The document evaluates:

```text
6 Microsoft capability clusters × 8 Atlas Lattice elements = 48 possible pairings
23 candidate touchpoints identified
7 high-affinity
11 moderate-affinity
5 low-affinity / monitor-only
```

CouncilBrain should route this into a phased review queue, not implementation.

---

## 3. ARB Gate Required

No pairing advances to implementation without explicit ARB review and ratification.

Hard rule:

```text
candidate mapping ≠ ARB approval
R3 readiness ≠ implementation permission
Microsoft commercial capability ≠ Atlas integration authority
```

---

## 4. Four Critical Blockers

CouncilBrain should register these as blockers:

```text
B-MSFT-001 / RSK-08 — GangaSeek / DragonSeek internal API documentation missing.
B-MSFT-002 / RSK-13 — legal and compliance review of all six Microsoft capability clusters incomplete.
B-MSFT-003 / RSK-14 — ARB assessment and ratification not initiated / incomplete.
B-MSFT-004 / RSK-01 — ACC Confidential Clean Rooms GA required for ACC-dependent integrations.
```

---

## 5. Recommended CouncilBrain Queue

```yaml
councilbrain_queue:
  phase_0_preconditions:
    - resolve_RSK_08_api_docs
    - resolve_RSK_13_legal_compliance_review
    - resolve_RSK_14_ARB_review
    - monitor_RSK_01_ACC_clean_rooms_GA

  phase_1_sandbox_POC_candidates:
    - GoldenTrace ↔ Entra Verified ID
    - INV-L10 ↔ Azure Arc
    - INV-L10 ↔ Planetary Computer Pro
    - INV-L10 ↔ Fabric / Synapse
    - INV-L19 ↔ Azure Arc

  phase_2_limited_pilot:
    gate: successful_phase_1_plus_ARB_submission

  phase_3_ratification_decision:
    gate: explicit_ARB_ratification_or_rejection_per_pairing
```

---

## 6. CouncilBrain Risk Register Additions

```yaml
risk_register:
  - id: RSK-08
    severity: critical_blocking
    status: open
    action: produce_internal_API_docs
  - id: RSK-13
    severity: critical_blocking
    status: open
    action: legal_compliance_review_all_capabilities
  - id: RSK-14
    severity: critical_blocking
    status: open
    action: initiate_ARB_review
  - id: RSK-01
    severity: high_open
    status: monitor_until_ACC_clean_rooms_GA
    action: monitor_product_GA_and_API_stability
```

---

## 7. Keeper

```text
CouncilBrain routes the question.
ARB answers the architecture.
CopilotBrain prepares the work orders.
TIDELOCK blocks premature implementation.
```