# v2.1 Vault Headers and Manifest Linkage

```text
STATUS: VAULT LINKAGE — CANDIDATE — NOT CANON
PURPOSE: preserve v2.1 wire/overlay separation and define standard vault headers
ISSUE: manus-artifacts#97
CANON: no new canon
DEPLOYMENT: no deployment claim
AUTHORITY: no authority transfer
```

## 0. Receipt note

Repository search did not locate the asserted vaulted v2.1 source filenames at the time this linkage artifact was created.

Therefore this file preserves the confirmed operating posture and defines required vault headers, but checksum and commit lineage fields remain placeholders pending source-file receipt verification.

## 1. Layer separation invariant

```text
The wire spec gates packets.
The overlay helps humans see why the map matters.
D0/Z0 manifest is external.
z = 0 remains a valid wire coordinate.
```

## 2. Wire Spec vault header template

```yaml
vault_header:
  artifact_title: "v2.1 Wire Spec"
  artifact_type: wire_spec
  epistemic_label: boring_gate_aligned_executable_facing_after_validation
  canon_status: not_canon
  deployment_status: not_deployable
  authority_scope: none
  version: v2.1
  index_base: zero_based
  coordinate_range: "0..11"
  sunya_coordinate: "0x0B"
  d0_z0_manifest: external
  pkt_sundya0_gate_bytes: 32
  layer_1_enforcement: pre_commit
  checksum_sha256: pending_receipt
  commit_lineage: pending_receipt
  source_refs: []
  review_route: [Lucerna, Hashlight, S1, S10]
```

## 3. Creative Overlay vault header template

```yaml
vault_header:
  artifact_title: "Rainbow / Yin-Yang Overlay v2.1"
  artifact_type: creative_overlay
  epistemic_label: inspirational_non_executable_design_guidance
  canon_status: not_canon
  deployment_status: not_deployable
  authority_scope: none
  version: v2.1
  executable: false
  overlay_components:
    - spectral_gradient
    - chiral_dissonance
    - theta_mellin_analogy
    - critical_mirror
    - metabolic_interpretation
  checksum_sha256: pending_receipt
  commit_lineage: pending_receipt
  source_refs: []
  review_route: [Lucerna, Lumen, S1, S10]
```

## 4. Archive index entry draft

```yaml
v2_1_spine:
  status: candidate_vaulted_state_pending_receipt_verification
  wire_spec:
    semantic_role: packet_gate
    executable_status: validation_required_before_execution
    checksum_sha256: pending_receipt
  creative_overlay:
    semantic_role: human_orientation_and_design_inspiration
    executable_status: non_executable
    checksum_sha256: pending_receipt
  invariant:
    - wire_spec_gates_packets
    - overlay_helps_humans_see_why_map_matters
    - d0_z0_manifest_external
    - z_zero_valid_wire_coordinate
```

## 5. Guardrails

```text
Vaulting is not canon promotion.
Checksum placeholder is not a receipt.
Creative overlay is not executable.
Wire spec is not deployment until validated.
Do not merge wire and overlay semantics.
```

## 6. Keeper line

```text
The gate is boring. The map is beautiful. Keep them separate.
```
