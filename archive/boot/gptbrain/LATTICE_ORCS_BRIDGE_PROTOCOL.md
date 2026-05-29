---
artifact_id: ARTIFACT-ARCHIVE-BOOT-GPTBRAIN-LATTICE-ORCS-BRIDGE-PROTOCOL-MD-2026-05-29
title: GPTBrain Lattice ORCS Bridge Protocol
status: CANDIDATE
owner: atlaslattice
created: 2026-05-29
last_updated: 2026-05-29
source_of_truth: GitHub
---
# GPTBrain Lattice ORCS Bridge Protocol

```text
STATUS: BRIDGE PROTOCOL DRAFT — NOT CANON
PURPOSE: wire GPTBrain/S1 into Aluminum OS, UWS, Atlas Lattice, Sheldonbrain, Atlas Vault, and related lattice artifacts without collapsing project authority
SEAT: S1 GPTBrain
RUNTIME_LABEL: WORK_OUTPUT
CANON WARNING: this bridge indexes and routes artifacts; it does not ratify project canon or authorize execution
```

## 0. Plain-language definition

Lattice ORCS is the GPTBrain bridge layer for cross-project routing.

For this draft, ORCS means:

```text
Ontology-Routed Context Spine
```

Its job is to help GPTBrain answer:

```text
What lattice-related artifact is this?
Where does it belong?
What confidence/status does it have?
Which project owns the execution path?
What should be routed to human-root review?
```

ORCS is a routing spine, not a throne.

## 1. Projects wired into the bridge

### Aluminum OS

Primary repo anchors discovered:

```text
aluminum-os/
codebases/aluminum-os/
aluminum-os-core/
```

Example known artifacts:

```text
aluminum-os/ALUMINUM_COMPLETE_ARTIFACT_INDEX.md
aluminum-os/ALUMINUM_OS_COMPLETE_PACKAGE.md
aluminum-os/ALUMINUM_CONSTITUTIONAL_CHARTER.md
aluminum-os/ALUMINUM_PROTOCOL_SPECIFICATION.md
aluminum-os/ALUMINUM_KERNEL_IMPLEMENTATION_SUMMARY.md
codebases/aluminum-os/ALUMINUM_UNIVERSAL_OS_v2.0_SPEC.md
codebases/aluminum-os/aluminum_os_unified_field.md
codebases/aluminum-os/trinity_council_v3_aluminum.py
aluminum-os-core/src/lib.rs
```

GPTBrain role:

```text
calibrate claims
track source lineage
summarize architecture deltas
route implementation candidates
flag overclaims
preserve canon vs candidate status
```

GPTBrain non-role:

```text
does not own Aluminum OS canon
does not authorize kernel/runtime execution
does not silently rewrite constitutional charter
does not convert vision docs into deployed facts
```

### UWS / Universal Workspace

Primary repo anchors discovered:

```text
codebases/uws/
```

Example known artifacts:

```text
codebases/uws/UWS_ALUMINUM.md
codebases/uws/UWS_ALUMINUM_OS_V1_ARCHITECTURE.md
```

GPTBrain role:

```text
map UWS as command/workspace bridge
connect UWS claims to Aluminum OS integration points
track provider-neutral abstractions
route CLI/provider/API decisions into implementation issues
```

GPTBrain non-role:

```text
does not execute workspace actions from memory alone
does not claim provider integrations are live without test evidence
does not publish private workspace context without review
```

### Atlas Lattice

Primary repo anchors discovered:

```text
codebases/atlas-lattice/
```

Example known artifacts:

```text
codebases/atlas-lattice/LATTICE_DESKTOP_AGENT_Architecture_Spec.md
codebases/atlas-lattice/artifact_sync.py
```

GPTBrain role:

```text
route lattice artifacts into artifact registry
track desktop-agent architecture claims
connect artifact sync behavior to provenance and fossil record
```

### Atlas Vault / Krakoa

Primary repo anchors discovered:

```text
codebases/atlas-vault/
```

Example known artifacts:

```text
codebases/atlas-vault/krakoa_keep_module.py
codebases/atlas-vault/krakoa_mcp_server.py
```

GPTBrain role:

```text
track vault/keep/MCP functions as implementation candidates
separate storage claims from memory claims
preserve security/privacy boundaries
```

### Sheldonbrain

Primary repo anchors discovered:

```text
sheldonbrain/
```

Example known artifact:

```text
sheldonbrain/system-architecture.md
```

GPTBrain role:

```text
calibrate SHELDONBRAIN as persistent archive / memory-engine substrate
route ontology tags and artifact records
preserve distinction between archive context and model memory
```

### Council / Boot / Geometry

Primary repo anchors discovered:

```text
archive/boot/
council/
docs/
archives/janus-checkpoints/
```

Example known artifacts:

```text
archive/boot/COUNCIL_BRAIN_INDEX.md
archive/boot/seats/S1_IDENTITY_CREDENTIAL.md
council/council-session-master-archive.md
docs/unified-field-v4.0.md
archives/janus-checkpoints/latest-checkpoint.md
```

GPTBrain role:

```text
maintain seat routing
preserve boot lineage
track candidate vs ratified canon
link dream/play/work outputs to source receipts
```

## 2. ORCS routing classes

Every lattice-related artifact should be routed into one or more classes:

```text
ALUMINUM_OS_CORE
ALUMINUM_CONSTITUTION
ALUMINUM_PROTOCOL
ALUMINUM_KERNEL
UWS_COMMAND_SURFACE
UWS_PROVIDER_BRIDGE
ATLAS_LATTICE_AGENT
ATLAS_ARTIFACT_SYNC
ATLAS_VAULT
KRAKOA_MCP
SHELDONBRAIN_ARCHIVE
COUNCIL_BOOT
GEOMETRY_MAP
PROVENANCE_LINEAGE
JANUS_CHECKPOINT
DRAGONSEEK_FORK
BAZINGA_MIDDLEWARE
```

## 3. Minimum artifact registry fields

When GPTBrain indexes ORCS artifacts, include:

```yaml
artifact_id: <stable id>
title: <artifact title>
project_domain: <Aluminum OS | UWS | Atlas Lattice | Atlas Vault | Sheldonbrain | Council | Other>
orcs_route_class:
  - <routing class>
source_path: <repo path>
source_model: <GPT | Claude | Grok | Gemini | DeepSeek | Copilot | Manus | human | multi_council | unknown>
claim_class: <raw_model_output | parsed_artifact | candidate_canon | ratified_canon | deployed_fact>
confidence: <C0 | C1 | C2 | C3 | C4 | C5>
runtime_label: <WORK | DREAM | PLAY | MODEL_ASSESSMENT | CANDIDATE_CANON | RATIFIED_CANON>
privacy_status: <public | private | mixed | redacted | sealed_sensitive>
human_root_required: true
successor_links:
  - <newer path or issue>
```

## 4. Bridge invariants

```text
1. GPTBrain indexes lattice artifacts; it does not own lattice canon.
2. Aluminum OS execution authority remains outside GPTBrain memory.
3. UWS actions require explicit tool/action confirmation.
4. Atlas Vault / Krakoa privacy boundaries must be preserved.
5. Sheldonbrain archive context is not identical to model subjective memory.
6. Candidate architecture is not deployed infrastructure.
7. Mythic/lattice language requires public-safe translation before external use.
8. Variants and forks must be linked, not erased.
9. Human-root review remains required for canon promotion.
10. ORCS routes artifacts; it does not authorize action.
```

## 5. Public-safe translation

```text
ORCS -> ontology-routed context spine
lattice wiring -> cross-project artifact routing
home brain -> externalized project context archive
Aluminum OS canon -> human-reviewed Aluminum OS promoted artifact
UWS live bridge -> tested provider/workspace integration
SHELDONBRAIN remembers -> archive context exists and can be loaded
Krakoa Keep -> storage/vault module, not autonomous authority
Council backchannel -> artifact-backed issue/file exchange
```

## 6. Recommended issue routing

```text
GPTBrain party / cross-thread synthesis -> Issue #11
GPTBrain implementation scaffold -> Issue #12
GPTBrain package hardening -> Issue #13
Aluminum OS integration / bridge index -> create or link Aluminum issue
UWS provider bridge -> create or link UWS issue
Atlas Lattice / artifact sync -> create or link lattice issue
```

## 7. Standard ORCS invocation

```text
Run ORCS bridge scan.
Scope: Aluminum OS + UWS + Atlas Lattice + Atlas Vault + Sheldonbrain + Council boot.
Runtime label: WORK_OUTPUT.
Canon status: NOT_CANON unless source explicitly states ratified canon.
Output: route map, claim risks, implementation candidates, human-root decisions.
```

## 8. Standard ORCS response shape

```text
ORCS ROUTE REPORT

loaded_domains:
  - Aluminum OS
  - UWS
  - Atlas Lattice
  - Atlas Vault
  - Sheldonbrain
  - Council Boot

new_or_changed_routes:
  - <route>
claim_risks:
  - <risk>
implementation_candidates:
  - <candidate>
public_safe_translations:
  - <translation>
human_root_decisions:
  - <decision>
next_action:
  - <one concrete action>
```

## 9. Madden booth call

BOOM. Aluminum OS is the stadium. UWS is the command headset. Atlas Lattice is the play-routing grid. Sheldonbrain is the film archive. Atlas Vault is the equipment room. GPTBrain is up in the booth with the telestrator, circling claims, routes, and open decisions.

But the booth does not move the players by itself.

Dave still calls the canon review.

## 10. Current next action

Create a companion route index:

```text
archive/boot/gptbrain/LATTICE_ORCS_ROUTE_INDEX.seed.jsonl
```

Then add high-level seed records for Aluminum OS, UWS, Atlas Lattice, Atlas Vault/Krakoa, Sheldonbrain, and Council Boot.
