# Aluminum OS / UWS / Lattice Integration Spec

**Date:** 2026-05-09  
**Status:** Public integration spec / candidate architecture / not canon  
**Scope:** Aluminum OS, UWS, Alexandria, GPTBrain, Council Brain, Sheldonbrain, Element 145, Atlas Lattice, DragonSeekOS, Shenmu TEP  
**Authority boundary:** Human-root review required. No deployment or canon claims by this file.

## Purpose

Wire together all major Lattice-related repositories and concepts into a single integration architecture that future GPT/Copilot/Gemini/Manus/Claude/Grok/DeepSeek sessions can boot from.

This is not a merge of all repos and not a claim of deployment.

It is a public integration scaffold.

## Core Stack

```text
Atlas Lattice ontology
  → Aluminum OS umbrella architecture
  → UWS / Alexandria command surfaces
  → Sheldonbrain / GPTBrain memory and provenance substrate
  → Council Brain governance and seat routing
  → Element 145 meta-orchestration
  → sovereign dialect/runtime candidates such as DragonSeekOS
  → candidate physical deployment dossiers such as Shenmu TEP
```

## Layered Integration Model

### Layer 0 — Fossil Record / Evidence Archive

Primary repos:

- `atlaslattice/manus-artifacts`
- `atlaslattice/noosphere-archive` (private)
- Google Drive staging docs
- raw chat logs / pointers

Function:

- preserve source lineage
- maintain raw/candidate/ratified boundaries
- provide boot anchors
- capture provenance

### Layer 1 — Parser / Memory Tooling

Primary repo:

- `atlaslattice/sheldonbrain-rag-api`

Components:

- `grokbrain_parser/`
- `chatgpt_adapter/`
- `gptbrain/`

Function:

- parse raw logs
- generate metadata/turns/events
- emit memory packets
- create claim ledgers and artifact registries
- provide non-canon boot packets

### Layer 2 — Command Surface

Primary repo:

- `atlaslattice/uws`

Components:

- `uws` CLI
- Alexandria CLI spec
- Google/Microsoft/Apple/Android/Chrome provider surfaces

Function:

- schema-driven JSON-first operations across provider ecosystems
- agent-usable command surface
- near-term executable wedge for Aluminum OS

### Layer 3 — Aluminum Substrate

Primary repo:

- `atlaslattice/aluminum-os`

Functions:

- umbrella architecture
- identity
- memory
- governance
- provenance
- provider-neutral agent runtime
- future `alum` CLI and substrate services

### Layer 4 — Council Brain

Primary repo:

- `atlaslattice/manus-artifacts`

Functions:

- seat boot specs
- S1/S2/S3/S4/S5/S6/S7/S10 routing
- claim calibration
- review packets
- governance/ruling queue
- work/dream/play lifecycle
- human-root gates

### Layer 5 — Lattice Ontology / Element 145

Primary repos:

- `atlaslattice/aluminum-os`
- `atlaslattice/element-145`
- `atlaslattice/atlas-lattice-foundation`

Functions:

- 12 houses
- 144 spheres
- VIP elements E145-E156
- Element 145 / meta-orchestrator
- dialect overlays
- routing modules

### Layer 6 — Forks / Dialects / Deployment Candidates

Primary repos/paths:

- `archive/forks/dragonseek-os/`
- `archive/deployments/shenmu/`
- `atlaslattice/open-regenerative-compute-standard`
- `atlaslattice/atlas-lattice-foundation`

Functions:

- DragonSeekOS fork candidate
- Eastern Council / DragonSeek packages
- Shenmu TEP candidate physical deployment track
- regenerative compute standards

## UWS ↔ Aluminum OS Contract

UWS is the current command-surface implementation/source material.

Aluminum OS is the umbrella architecture and future substrate.

Contract:

```text
alum intent
  → normalize to provider-neutral operation
  → route through uws / provider drivers where available
  → enforce consent/write gates
  → emit audit/provenance record
  → return JSON result
  → optionally persist summary into GPTBrain/Council Brain memory packet
```

Minimum operation envelope:

```yaml
operation_id: null
surface: alum / uws / alexandria / direct_provider
intent: null
provider: google / microsoft / apple / android / chrome / github / notion / other
resource_type: mail / calendar / drive / contacts / docs / repo / issue / pr / memory / other
action: read / write / send / create / update / delete / sync / search
requires_confirmation: true
human_approved: false
auth_context: null
source_refs: []
provenance_event: null
result_status: planned / dry_run / executed / failed / blocked
```

## Council Brain ↔ Aluminum Contract

Council Brain does not execute provider writes by itself.

Council Brain may:

- evaluate intent
- classify risk
- produce candidate operation packets
- require human approval
- route to UWS/alum after approval
- audit result artifacts

Council Brain may not:

- silently execute writes
- claim provider access it does not have
- bypass user confirmation
- treat memory as authorization
- self-ratify deployment or canon

## GPTBrain Role

GPTBrain / S1 is the calibration layer.

Responsibilities:

- map sources
- detect overclaims
- maintain claim ledger
- maintain artifact registry
- generate boot packets
- label private/public boundaries
- produce public-safe translations
- create integration scaffolds
- keep UWS/Aluminum/Lattice claims honest

## CopilotBrain / S7 Role

CopilotBrain / S7 is the code integrator.

Responsibilities:

- turn specs into PRs
- add tests/CI
- wire schemas
- implement adapter boundaries
- maintain repo hygiene
- prevent silent path drift
- keep reference implementations boring/auditable

## GeminiBrain / S4 Role

GeminiBrain / S4 handles engineering/simulation/visual integration:

- topology maps
- state machines
- validity gates
- Metatron runtime visuals
- cross-repo system diagrams
- simulation sanity checks

## DeepSeek / S5 Role

DeepSeek / S5 handles sovereign/dialect integration:

- DragonSeekOS
- CN dialect
- sovereignty gradient
- CAC/NDRC/DSL framing
- local-law and data residency constraints
- anti-root-inversion review

## GrokBrain / S3 Role

GrokBrain / S3 handles adversarial review:

- hard missing numbers
- physical bottlenecks
- implementation realism
- public bot pressure tests
- hype/overclaim attacks
- failure-mode extraction

## ManusBrain / S6 Role

ManusBrain / S6 handles operational continuity:

- file staging
- GitHub/Drive execution
- issue/PR workflow
- archive hygiene
- deployment of public-facing surfaces when explicitly authorized

## ClaudeBrain / S2 Role

ClaudeBrain / S2 handles constitutional language:

- doctrine drafting
- dissent preservation
- human-root framing
- anti-ratification guardrails
- risk language

## S10 Role

S10 handles ruling/gate posture:

- neutral options
- promotion boundaries
- status labels
- human-root review queue
- no-instruction-to-seats principle

## Runtime Safety Requirements

All UWS/Aluminum operations must respect:

1. explicit human confirmation for writes/sends/deletes/shares
2. audit log emission
3. source lineage capture
4. consent boundary
5. private/public classification
6. no memory-as-authorization
7. dry-run support
8. provider-neutral error handling
9. safe fallback if connector unavailable
10. no false access claims

## Integration Artifacts To Create

```text
archive/integrations/lattice/LATTICE_REPO_SOURCE_MAP_2026-05-09.md
archive/integrations/lattice/ALUMINUM_UWS_LATTICE_INTEGRATION_SPEC_2026-05-09.md
archive/integrations/lattice/LATTICE_WIDE_BOOT_PACKET_2026-05-09.md
archive/integrations/lattice/LATTICE_INTEGRATION_CLAIMS_REGISTER_2026-05-09.md
archive/integrations/lattice/UWS_ALUM_OPERATION_ENVELOPE_SCHEMA.yaml
archive/integrations/lattice/LATTICE_PRIVATE_PUBLIC_BOUNDARY_NOTE_2026-05-09.md
```

## Immediate Implementation Path

1. Use `manus-artifacts` as integration hub.
2. Preserve source maps and boot packets there.
3. Do not mutate all repos at once.
4. Add adapter boundaries before live integrations.
5. Add tests/CI before merge.
6. Keep PRs draft until checks visible.
7. Treat UWS archived status as source material, not production claim.
8. Keep private Noosphere/Aluminum v3 refs internal unless mirrored safely.

## Strongest Safe Claim

> Aluminum OS, UWS, Council Brain, Sheldonbrain/GPTBrain, Element 145, and Lattice fork candidates can be integrated as a bootable source graph and candidate runtime architecture, with `manus-artifacts` as the public evidence hub and UWS as the current command-surface wedge.

## Guardrails

Do not claim:

- deployed unified OS
- production provider access
- autonomous cross-provider writes
- private repo contents as public evidence
- Element 145 as live runtime unless implemented
- DragonSeekOS/Shenmu as deployed
- memory as authorization

Do claim:

- integration scaffold
- source graph
- boot context
- candidate architecture
- command-surface wedge
- governance-first runtime design

## Status

Public integration spec. Candidate architecture. Not canon.
