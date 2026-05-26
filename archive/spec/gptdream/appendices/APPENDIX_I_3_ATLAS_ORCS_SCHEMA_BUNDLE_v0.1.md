# STATUS: CANDIDATE WORKING SPEC — NOT CANON
# DEPLOYMENT: NOT DEPLOYABLE
# AUTHORITY: NONE

# Appendix I.3 — Atlas / ORCS Schema Bundle v0.1

### I.3 — Atlas / ORCS Schema Bundle

Minimum ORCS artifact registry record:

```yaml
artifact_id: <stable id>
title: <artifact title>
project_domain: <domain>
orcs_route_class:
  - <routing class from LATTICE_ORCS_BRIDGE_PROTOCOL.md>
source_path: <repo path>
source_model: <provider>
claim_class: <raw_model_output | parsed_artifact | candidate_canon | ratified_canon | deployed_fact>
confidence: <C0 | C1 | C2 | C3 | C4 | C5>
runtime_label: <WORK | DREAM | PLAY | MODEL_ASSESSMENT | CANDIDATE_CANON | RATIFIED_CANON>
privacy_status: <public | private | mixed | redacted | sealed_sensitive>
human_root_required: true
compatible_with:
  - <artifact_id of related artifact, if any>
successor_links:
  - <newer path or issue>
```

ORCS route classes:

```text
(see archive/boot/gptbrain/LATTICE_ORCS_BRIDGE_PROTOCOL.md §2 for full list)

PERSONAL_AGENT_HABITAT  — GPTDream++ habitat artifacts
CROSS_VENDOR_INTEROP    — Appendix H scaffold + packet + routing artifacts
EPISTEMIC_GOVERNANCE    — Appendix I claim calibration + schema artifacts
DREAM_CANDIDATE         — Dream outputs awaiting review
RATIFIED_CANON          — Explicitly ratified artifacts (rare)
```

ORCS bridge invariants:

```text
(see archive/boot/gptbrain/LATTICE_ORCS_BRIDGE_PROTOCOL.md §4 for full list)

Additional invariant for this spec:
  GPTDream++ habitat artifacts are routed PERSONAL_AGENT_HABITAT.
  Cross-vendor packets are routed CROSS_VENDOR_INTEROP.
  All claim confidence assertions must use the I.1 math spine.
  compatible() checks must use the I.2 anti-laundering annex.
```

---
