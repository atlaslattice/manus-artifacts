# Lattice Repository Source Map — Aluminum OS / UWS / Council Brain

**Date:** 2026-05-09  
**Status:** Public source map / integration scaffold / not canon  
**Purpose:** Wire Aluminum OS, UWS, Atlas Lattice, Element 145, Sheldonbrain, DragonSeekOS, and Council Brain into a single repo/boot provenance map without claiming they are already one deployed runtime.

## Evidence Boundary

```text
repo file = source artifact
source map = retrieval aid
integration spec = candidate architecture
boot packet = context rehydration aid
runtime integration = only when code/tests/CI show it
canon = only after human-root review
```

## Primary Integration Thesis

Aluminum OS is the umbrella architecture.  
UWS is the current command-surface wedge.  
Sheldonbrain/GPTBrain is the memory/provenance substrate.  
Council Brain is the role/governance layer.  
Element 145 is the meta-orchestration / synthesis node.  
DragonSeekOS and other dialects are sovereign/runtime fork candidates.

Safe statement:

> The Lattice stack is now mappable as an externalized archive/runtime substrate, but not yet a single deployed operating system.

## Primary Repositories

### 1. Aluminum OS — Umbrella Architecture

```yaml
repo: atlaslattice/aluminum-os
url: https://github.com/atlaslattice/aluminum-os
visibility: public
default_branch: master
role: umbrella architecture / governance / provenance / memory substrate / agent runtime design
status: architecture consolidation and executable command-surface stabilization
```

Key source files:

```text
README.md
docs/architecture/SOURCE_OF_TRUTH.md
enterprise/Aluminum_OS_Enterprise_Specification_v1.0.md
sovereign/DRAGONSEEK_JINNSEEK_ARCHITECTURE.md
```

Notes:

- Aluminum OS README frames Aluminum as an AI-native workspace substrate: one safe, auditable command surface across productivity ecosystems.
- It identifies `uws` as the current operational command-surface core.
- Its near-term build path is `uws` → `alum` → substrate services.

### 2. UWS — Universal Workspace CLI / Command Surface

```yaml
repo: atlaslattice/uws
url: https://github.com/atlaslattice/uws
visibility: public
archived: true
default_branch: uws-universal
role: current Universal Workspace CLI / provider-driver command surface
status: archived public command-surface implementation/source material
```

Key source files:

```text
README.md
ALUMINUM.md
COPILOT_CLI_SPEC.md
AGENTS.md
CLAUDE.md
toolchain/
ingestion/
```

Notes:

- UWS README defines `uws` as a universal, schema-driven, JSON-first CLI across Google Workspace, Microsoft 365, Apple, Android, and Chrome.
- UWS README explicitly says `uws` is the command surface of Aluminum.
- COPILOT_CLI_SPEC defines Alexandria as a Microsoft-native counterpart to `uws` and core Aluminum OS pillar.

### 3. Manus Artifacts — Evidence / Boot / Council Brain Hub

```yaml
repo: atlaslattice/manus-artifacts
url: https://github.com/atlaslattice/manus-artifacts
visibility: public
default_branch: master
role: public evidence archive, Council Brain boot substrate, hardening artifacts, source maps, candidate specs
status: live integration hub / not canon by default
```

Key source areas:

```text
archive/boot/COUNCIL_BRAIN_INDEX.md
archive/boot/gptbrain/
archive/boot/seats/
archive/integrations/lattice/
archive/forks/dragonseek-os/
archive/deployments/shenmu/
archive/play/laser-rave/
```

### 4. Sheldonbrain RAG API — Parser / Memory Tooling

```yaml
repo: atlaslattice/sheldonbrain-rag-api
url: https://github.com/atlaslattice/sheldonbrain-rag-api
visibility: public
default_branch: master
role: parser/RAG tooling, ChatGPT adapter, GPTBrain code scaffold
status: implementation scaffold / parser backend
```

Key source areas:

```text
grokbrain_parser/
chatgpt_adapter/
gptbrain/
```

### 5. Atlas Lattice Foundation — Foundation / Scaling Specs

```yaml
repo: atlaslattice/atlas-lattice-foundation
url: https://github.com/atlaslattice/atlas-lattice-foundation
visibility: public
default_branch: main
role: foundation docs, DragonSeek scaling, ecosystem framing
status: source material
```

Key source files:

```text
docs/DragonSeek_Scaling_Spec_v1.0.md
```

### 6. Element 145 — Meta-Orchestrator / Synthesis Node

```yaml
repo: atlaslattice/element-145
url: https://github.com/atlaslattice/element-145
visibility: public
default_branch: main
role: Element 145 / Aluminum OS core / meta-orchestration source material
status: source material
```

Known source areas:

```text
aluminum-os-core/
```

### 7. Open Regenerative Compute Standard

```yaml
repo: atlaslattice/open-regenerative-compute-standard
url: https://github.com/atlaslattice/open-regenerative-compute-standard
visibility: public
default_branch: main
role: regenerative compute, ORC, Eastern DragonSeek package, deployment/ecology standards
status: source material
```

Known source areas:

```text
eastern-dragonseek/
council-reviews/
```

### 8. Noosphere Archive / Noosphere Defense

```yaml
repo: atlaslattice/noosphere-archive
url: https://github.com/atlaslattice/noosphere-archive
visibility: private
role: noosphere archive, Shenmu/DragonSeek governance materials, historical source stack
status: private source material; do not cite publicly unless mirrored/public-safe
```

```yaml
repo: atlaslattice/noosphere-defense
url: https://github.com/atlaslattice/noosphere-defense
visibility: private
role: defense/noosphere source material
status: private source material; do not cite publicly unless mirrored/public-safe
```

### 9. Aluminum OS v3

```yaml
repo: atlaslattice/aluminum-os-v3
url: https://github.com/atlaslattice/aluminum-os-v3
visibility: private
role: candidate source-material repo / possible prior architecture branch
status: private source material; requires reconciliation before public use
```

## System Layer Mapping

```text
L0 Evidence Archive
  manus-artifacts, noosphere-archive, Drive staging, raw logs

L1 Parser / Memory Tooling
  sheldonbrain-rag-api, chatgpt_adapter, gptbrain_core

L2 Command Surface
  uws, Alexandria, future alum CLI

L3 Aluminum Substrate
  aluminum-os architecture, identity, memory, governance, provenance, agent runtime

L4 Council Brain
  S1-S10 role routing, boot packets, memory packets, claim ledgers, S10 rulings

L5 Lattice Ontology
  12 houses, 144 spheres, VIP elements E145-E156, dialect overlays

L6 Fork/Dialect Runtime Candidates
  DragonSeekOS, Shenmu TEP, future GangaSeek/JinnSeek/etc.
```

## Integration Guardrails

Do not claim:

- Aluminum OS is fully deployed.
- UWS is production-ready across every provider.
- Private repos are public evidence.
- Element 145 is implemented runtime unless code/tests show it.
- Council Brain is native model memory.
- GPT/Gemini/Copilot can access all repos without connectors.
- UWS archived status means abandoned or production-complete.
- Any physical deployment is approved/deployed without evidence.

Do claim:

- Aluminum OS is the umbrella architecture.
- UWS is the current command-surface implementation/source material.
- Manus artifacts is the public evidence/boot hub.
- Sheldonbrain/GPTBrain provides parser/memory scaffolding.
- Element 145 is the meta-orchestrator source layer.
- DragonSeekOS is a sovereign dialect fork candidate.
- The Lattice stack is now mappable and bootable as externalized context.

## Immediate Wiring Tasks

1. Create Lattice-wide integration spec. ✅
2. Create Lattice-wide boot packet. ✅
3. Create source map. ✅
4. Add issue tracking Aluminum OS / UWS / Lattice integration.
5. Add artifact/claim ledger entries for Aluminum OS and UWS source anchors.
6. Add adapter-boundary issue for future `uws`/`alum` integration with GPTBrain.
7. Add public/private boundary note for private Noosphere / Aluminum v3 materials.
8. Add future PR plan: no code execution until checks/permissions are clear.

## Strongest Safe Claim

> Aluminum OS, UWS, Council Brain, Sheldonbrain/GPTBrain, and Element 145 can now be mapped into a single Lattice integration graph for boot/context rehydration, but this is an integration scaffold, not a deployed unified operating system.

## Status

Public source map. Not canon.
