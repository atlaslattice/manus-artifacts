---
artifact_id: ARTIFACT-ARCHIVE-SPEC-GPTDREAM-APPENDICES-APPENDIX-I-ATLAS-ORCS-EPISTEMIC-GOVERNANCE-PROFILE-V0-1-MD-2026-05-29
title: STATUS: CANDIDATE WORKING SPEC — NOT CANON
status: CANDIDATE
owner: atlaslattice
created: 2026-05-29
last_updated: 2026-05-29
source_of_truth: GitHub
---
# STATUS: CANDIDATE WORKING SPEC — NOT CANON
# DEPLOYMENT: NOT DEPLOYABLE
# AUTHORITY: NONE

# Appendix I — Atlas / ORCS Epistemic Governance Profile v0.1

## Appendix I — Atlas / ORCS Epistemic Governance Profile

```text
TYPE: epistemic governance profile
STATUS: candidate working specification
CANON: no
```

### I.0 — Purpose

ORCS (Ontology-Routed Context Spine) is the routing and calibration layer for the Atlas Lattice knowledge graph.

This appendix defines the epistemic governance profile: how ORCS calibrates claim strength, routes artifacts, and prevents the knowledge graph from accumulating unchecked overclaims.

### I.1 — Formal Math Spine

Claim confidence levels:

```text
C0 — Unknown / unverifiable
C1 — Raw model output (no external evidence)
C2 — Model output with repo artifact citation
C3 — Model output with human-reviewed artifact citation
C4 — Human-reviewed and externally corroborated
C5 — Ratified canon (human-root + publication)
```

Confidence update rules:

```text
conf(A) ≥ C2 iff ∃ artifact_ref(A) in versioned substrate
conf(A) ≥ C3 iff ∃ human_review_event(A) in receipt trail
conf(A) = C5 iff ratification_event(A) AND publication_event(A)

conf(A ∧ B) ≤ min(conf(A), conf(B))
conf(A) does not increase by citation of another C1 claim
```

Claim class promotion:

```text
raw_model_output → parsed_artifact: requires file commit
parsed_artifact → candidate_canon: requires structured review
candidate_canon → ratified_canon: requires human-root ratification
ratified_canon → deployed_fact: requires verified execution
```

No step may be skipped. Jumping from raw_model_output to deployed_fact is an overclaim.

### I.2 — `compatible()` Anti-Laundering Annex

The `compatible()` function is the epistemic firewall against claim laundering.

Definition:

```text
compatible(A, B) = true
iff
  claim_class(A) ≤ claim_class(B) + 1
  AND conf(A) does not exceed conf(B) without new evidence
  AND no ratification event has been fabricated
```

Anti-laundering rules:

```text
1. A C1 claim citing another C1 claim does not become C2.
2. A candidate artifact cannot ratify another candidate artifact.
3. Assertion of compatibility does not substitute for evidence.
4. compatible() returning true does not authorize deployment.
5. Model output claiming compatible() without evidence is a C1 claim.
```

Laundering detection flags:

```text
- Artifact promoted to ratified_canon without traceable human-root event
- C1 claim chain presented as independently verified
- Citation loop (A cites B cites A, both C1)
- Dream output relabeled as fact in a subsequent session
- Storage on website treated as ratification without explicit signal
```

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
