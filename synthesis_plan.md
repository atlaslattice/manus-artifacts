# Aluminum OS / UWS Synthesis Plan

**Date:** April 27, 2026
**Author:** Manus AI
**Target:** Dave Sheldon (Constitutional Scribe)
**Status:** 🔍 COUNCIL REVIEW REQUESTED

## 1. Executive Summary

This document presents a comprehensive synthesis plan for unifying the `manus-artifacts` repository into a single, coherent codebase that implements the Aluminum OS / Universal Workspace (UWS) architecture. The analysis reviewed 15 distinct codebase directories containing over 200 files, ranging from Python prototypes and Rust policy engines to extensive Markdown specifications.

The current state of the repository reflects a period of rapid, parallel innovation across multiple AI platforms. While this has generated a wealth of valuable components, it has also resulted in significant fragmentation, overlapping functionality, and a mix of working code, prototypes, and specifications. The goal of this synthesis plan is to transition from this fragmented state to the canonical "Unified Field v4.0" architecture, establishing a robust, constitutionally governed pipeline.

## 2. Target Architecture Mapping

The target architecture, as defined in the `unified-field-v4.0.md` specification, is a four-ring system governed by immutable constitutional principles. The existing components have been mapped to this target pipeline to identify their roles and current maturity levels.

| Pipeline Stage | Target Ring | Primary Components | Current State |
| :--- | :--- | :--- | :--- |
| **INGEST** | Ring 3 (Experience) | `data-pipeline/ingestion_pipeline.py`, `atlas-vault/automated_ingestion_pipeline.py`, `sheldonbrain/ingest_grok_chats.py` | Prototype |
| **COMPILER** | Ring 3 (Experience) | `data-pipeline/ontology_classifier.py`, `sheldonbrain/reclassify_conversations.py` | Prototype |
| **TASK GEN** | Ring 2 (Agent Runtime) | `sovereign-oracle/autonomous.py` (TaskDecomposer), `project-symbiote/src_background.js` | Prototype |
| **ROUTER** | Ring 1 (Inference) | `sovereign-oracle/model_router.py`, `sovereign-oracle/multi_model.py` | Working |
| **BUILD** | Ring 2 (Agent Runtime) | `sovereign-oracle/output_layer.py`, `saas-killer/api_server.py`, `snrs/snrs_v1_3_1_rewrite.py` | Mixed |
| **REVIEW** | Ring 0 (Forge Core) | `aluminum-os-core/src/lib.rs` (NPFM Engine) | Working |
| **VAULT** | Ring 2 (Agent Runtime) | `atlas-vault/krakoa_keep_module.py`, `atlas-lattice/artifact_sync.py`, `sovereign-oracle/memory_store.py` | Prototype |
| **GOVERNANCE** | Ring 0 (Forge Core) | `aluminum-os-core/src/lib.rs`, `bazinga/v0.1-launch-decree.md`, `docs/unified-field-v4.0.md` | Working/Spec |

## 3. Overlaps and Redundancies

The parallel development process has led to several areas of overlapping functionality that must be resolved during the synthesis process.

**Ingestion Pipelines:** Multiple ingestion mechanisms exist across `data-pipeline`, `atlas-vault`, `sheldonbrain`, and `saas-killer`. These pipelines perform similar tasks, such as fetching data from external sources, staging content, and detecting novelty. They must be consolidated into a single, robust ingestion service.

**Ontology Classification:** Both `data-pipeline` and `saas-killer` contain nearly identical Gemini-based classifiers for the 144-sphere ontology. `sheldonbrain` also includes a similar classifier using Vertex AI. These should be merged into a unified compiler module.

**Agent Orchestration:** The `sovereign-oracle` directory contains a central operational brain (`sheldon_core.py`), which is largely duplicated in the `email-processing` directory (`bridge.py`). The `aluminum-os` directory also includes a prototype orchestrator (`trinity_council_v3_aluminum.py`). A single orchestration layer, aligned with the BAZINGA middleware, is required.

**Memory and Vaulting:** Persistent memory and artifact synchronization are handled by multiple components, including `sovereign-oracle/memory_store.py` (ChromaDB), `atlas-vault/krakoa_keep_module.py` (Google Keep), and `atlas-lattice/artifact_sync.py` (Notion/Drive/Pinecone). These must be unified into the "Three-Tier Archive" specified in the v4.0 architecture.

## 4. Synthesis Plan and Roadmap

The synthesis process will transition the repository from a collection of independent projects to a unified, multi-language monorepo.

### 4.1 Proposed Repository Structure

The unified repository will adopt a monorepo structure, organizing components by their architectural ring and primary language.

```text
manus-artifacts/
├── ring0-forge-core/          # Rust microkernel and governance
│   ├── aluminum-os-core/      # NPFM policy engine (Keep)
│   └── invariants/            # OPA Rego policies (To be built)
├── ring1-inference/           # Constitutional middleware
│   └── bazinga/               # BAZINGA v0.2 (Keep/Expand)
├── ring2-agent-runtime/       # Agent execution and routing
│   ├── uws-cli/               # Universal Workspace CLI (Merge uws specs)
│   ├── router/                # Unified model router (Merge sovereign-oracle)
│   └── vault/                 # Three-Tier Archive (Merge atlas-vault, memory_store)
├── ring3-experience/          # Ingestion, compilation, and UI
│   ├── ingest/                # Unified ingestion pipeline (Merge data-pipeline, sheldonbrain)
│   ├── compiler/              # 144-sphere ontology classifier (Merge data-pipeline)
│   └── symbiote/              # Chrome extension bridge (Keep project-symbiote)
├── specs/                     # Canonical specifications
│   ├── constitution/          # Governance documents
│   └── architecture/          # System design documents
└── scripts/                   # Deployment and utility scripts
```

### 4.2 Component Disposition

**Keep and Integrate:**
The `aluminum-os-core` Rust engine is a critical, working component that enforces the Net Positive Flourishing Metric (NPFM). It will form the foundation of Ring 0. The `data-pipeline` provides the most complete ingestion and compilation logic and will be the basis for Ring 3. The `sovereign-oracle` router and memory store offer robust Python implementations for Ring 2. The `bazinga` launch decree provides the product boundary for Ring 1.

**Merge and Consolidate:**
The various ingestion scripts (`atlas-vault`, `sheldonbrain`, `saas-killer`) will be merged into the primary `data-pipeline` to create a unified ingestion service. The duplicate ontology classifiers will be consolidated. The `email-processing` directory, which is largely a fork of `sovereign-oracle`, will be deprecated, with its unique email parsing logic merged into the unified ingestion pipeline.

**Deprecate:**
The `colab-notebooks` directory, containing interactive tutorials, will be deprecated as it is not suitable for an automated pipeline. The `free-bank` specification, while visionary, lacks executable code and falls outside the immediate scope of the Aluminum OS pipeline; it will be moved to an archive or separate repository.

### 4.3 Phased Implementation Roadmap

**Phase 1: Foundation and Restructuring (Weeks 1-2)**
The immediate priority is to establish the monorepo structure and migrate the canonical specifications. The `aluminum-os-core` Rust engine will be positioned as the Ring 0 foundation. The `bazinga` middleware will be initialized as the Ring 1 entry point. All redundant or deprecated codebases will be archived.

**Phase 2: Unified Ingestion and Compilation (Weeks 3-4)**
The focus will shift to Ring 3. The disparate ingestion pipelines will be merged into a single, robust Python service capable of handling various data sources (Drive, Notion, web feeds, email). The 144-sphere ontology classifier will be consolidated and integrated with the ingestion service, forming the COMPILER stage.

**Phase 3: Agent Runtime and Routing (Weeks 5-6)**
Ring 2 will be developed by integrating the `sovereign-oracle` model router and memory store. The "Three-Tier Archive" will be established, unifying the ChromaDB, Google Keep, and Pinecone vaulting mechanisms. The `uws` CLI will be developed to provide the command surface for the agent runtime.

**Phase 4: Constitutional Integration and Testing (Weeks 7-8)**
The final phase will focus on integrating the BAZINGA middleware (Ring 1) with the NPFM policy engine (Ring 0) and the agent runtime (Ring 2). The constitutional gates (e.g., the Dave Protocol, Zero Erasure) will be implemented to ensure all operations comply with the 39 invariants. Comprehensive end-to-end testing will validate the unified pipeline.

## 5. Dependency Management

The unified repository will be a polyglot environment, primarily utilizing Rust and Python.

**Rust (Ring 0 and Ring 1):** Dependencies will be managed via `Cargo.toml` at the workspace level, ensuring consistent versions across the `aluminum-os-core` and `bazinga` crates.

**Python (Ring 2 and Ring 3):** A unified `pyproject.toml` or `requirements.txt` will be established for the Python components, utilizing tools like `uv` or `poetry` for efficient dependency resolution. Key dependencies will include `langchain`, `qdrant-client`, `chromadb`, `fastapi`, and the respective AI provider SDKs (`google-genai`, `anthropic`, `openai`).

**TypeScript/JavaScript (Ring 3 UI):** The `project-symbiote` Chrome extension and any future UI components will manage dependencies via `package.json` and `pnpm`.

## 6. Constitutional Governance Integration

The BAZINGA middleware (Ring 1) will serve as the primary integration point for constitutional governance. Every task generated by the pipeline must pass through the BAZINGA gates before execution.

The `aluminum-os-core` Rust engine will evaluate all `WorkflowProposals` against the Net Positive Flourishing Metric (NPFM). If a task is flagged as "busywork" or violates any of the 39 invariants, the BAZINGA middleware will reject the execution and log the violation in the immutable audit trail. The "Dave Protocol" will be implemented as a human-in-the-loop escalation path for ambiguous or high-stakes operations.
