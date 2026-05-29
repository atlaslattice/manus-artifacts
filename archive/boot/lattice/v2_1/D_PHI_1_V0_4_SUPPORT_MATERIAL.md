# D-Φ-1 v0.4 Support Material — v2.1 Wire / Overlay Separation

```text
STATUS: SUPPORT MATERIAL — CANDIDATE — NOT CANON
PURPOSE: prepare doctrine review support without promoting v2.1 wire or overlay artifacts
ISSUE: manus-artifacts#97
DEPLOYMENT: no
AUTHORITY: none
```

## 1. Review focus

D-Φ-1 v0.4 should evaluate how the v2.1 spine interacts with:

```text
artifact_status.schema.yaml
authority_scope checks
PLAN_SHA256 / DIFF_SHA256 split
tri-partite verifier lanes
D0/Z0 external manifest
z = 0 valid coordinate rule
wire/overlay semantic separation
```

## 2. Open questions

```text
1. Does 0-based indexing 0..11 create any collision with older 1..12 house language?
2. Is Śūnya at 0x0B purely a wire value, or also a semantic marker?
3. Is PktSundya0 a 32-byte gate payload only, or does it also require a semantic envelope?
4. How does external D0/Z0 manifest bind to artifact_status without becoming authority?
5. Which verifier lane owns z=0 coordinate misuse: V_L, V_S, or V_C?
6. What exact pre-commit Layer-1 checks can be run locally without architecture expansion?
```

## 3. Feedback template

```yaml
d_phi_1_v0_4_feedback:
  reviewer:
  reviewed_artifact:
  review_type: logic | security | canon | provenance | implementation
  boundary_leak_detected: true | false
  wire_overlay_contamination_detected: true | false
  z_zero_rule_preserved: true | false
  d0_z0_externality_preserved: true | false
  checksum_receipt_available: true | false
  blockers: []
  recommendations: []
  strongest_safe_claim:
  overclaims_to_avoid: []
```

## 4. Cross-reference notes

```text
- artifact_status decides what an artifact is allowed to mean.
- v2.1 wire spec decides packet gating only after validation.
- Rainbow/Yin-Yang overlay helps human interpretation but does not execute.
- D0/Z0 manifest records provenance externally and must not become hidden root authority.
- z = 0 remains a valid wire coordinate and must not be erased by null/absence assumptions.
```

## 5. Recommended v0.4 doctrine patch candidates

```text
Candidate 1: All wire coordinates must declare indexing convention.
Candidate 2: z=0 is a valid coordinate unless explicitly marked null/absent by artifact_status.
Candidate 3: Creative overlays must declare executable=false.
Candidate 4: External manifests provide receipts, not authority.
Candidate 5: D-Φ-1 blocks when wire/overlay semantics are merged without explicit transformation.
```

## 6. Non-goals

```text
No canon promotion.
No deployment claim.
No implementation rewrite.
No new Rainbow doctrine.
No execution from overlay material.
```

## 7. Keeper line

```text
D-Φ-1 v0.4 should enforce the gate, not beautify the map.
```
