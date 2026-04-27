# Aluminum OS / UWS Codebase Synthesis Plan

**Version:** 1.0
**Date:** April 27, 2026
**Author:** Manus AI (Codebase Audit Agent)
**Commissioned By:** Dave Sheldon (Constitutional Scribe)
**Status:** 🔍 COUNCIL REVIEW REQUESTED
**GitHub:** [atlaslattice/manus-artifacts](https://github.com/atlaslattice/manus-artifacts)

---

> *This document presents the results of a comprehensive audit of the `manus-artifacts` repository and proposes an actionable plan to synthesize its 15 codebase directories into a single, constitutionally governed pipeline aligned with the Unified Field v4.0 architecture.*

---

## 1. Executive Summary

The `manus-artifacts` repository contains over 200 files across 15 distinct codebase directories, plus supporting top-level directories for governance, documentation, and research. These components were built across multiple AI platforms over several months of rapid, parallel innovation. The result is a rich but fragmented collection of Python prototypes, Rust policy engines, JavaScript extensions, and extensive Markdown specifications.

This synthesis plan maps every component to the target Aluminum OS / UWS pipeline, identifies seven major areas of overlap and redundancy, and proposes a four-phase implementation roadmap to unify everything into a monorepo organized by the canonical Four-Ring Architecture. The plan preserves all working code, consolidates duplicates, archives deprecated components, and identifies the new glue code required to connect the rings into a functioning end-to-end pipeline.

The target pipeline flow is:

```
SESSION / INPUT
   ↓
INGEST (data-pipeline)
   ↓
COMPILER (artifact structuring via 144-sphere ontology)
   ↓
TASK GENERATION (typed JSON)
   ↓
ROUTER (assign collaborator / model selection)
   ↓
MANUS (build)
   ↓
GITHUB (source of truth) → Claude and GPT review
   ↓
VAULT (living archive)
```

---

## 2. Full Codebase Inventory

The following table summarizes every codebase directory reviewed, its primary language, file count, overall maturity, and the pipeline stages it addresses.

| Codebase | Files | Language | State | Pipeline Stages |
| :--- | :---: | :--- | :--- | :--- |
| `codebases/sheldonbrain/` | 46 | Python, Markdown | Mixed | INGEST, COMPILER, REVIEW, VAULT |
| `codebases/sovereign-oracle/` | 23 | Python | Prototype | ROUTER, BUILD, REVIEW, GOVERNANCE |
| `codebases/email-processing/` | 23 | Python | Mixed | INGEST, COMPILER, ROUTER, BUILD, VAULT |
| `codebases/snrs/` | 13 | Python, Markdown | Mixed | INGEST, COMPILER, BUILD, VAULT |
| `codebases/uws/` | 11 | Markdown, Rust (spec) | Spec | BUILD, INFRASTRUCTURE, ROUTER |
| `codebases/atlas-lattice/` | 11 | Python, Markdown | Mixed | GOVERNANCE, BUILD, VAULT, INGEST |
| `codebases/aluminum-os/` | 8 | Markdown, Python | Spec | GOVERNANCE, INFRASTRUCTURE, BUILD |
| `codebases/data-pipeline/` | 7 | Python | Prototype | INGEST, COMPILER, INFRASTRUCTURE |
| `codebases/saas-killer/` | 6 | Python | Prototype | INGEST, COMPILER, BUILD |
| `codebases/colab-notebooks/` | 4 | Python (Jupyter) | Prototype | INGEST |
| `codebases/atlas-vault/` | 3 | Python | Mixed | INGEST, COMPILER, VAULT, INFRASTRUCTURE |
| `codebases/project-symbiote/` | 1 | JavaScript | Prototype | BUILD, ROUTER, TASK_GEN |
| `codebases/free-bank/` | 1 | Markdown | Spec | OTHER |
| `codebases/other/` | 48 | Python, JS, Markdown | Mixed | INGEST, BUILD, REVIEW, VAULT |
| `aluminum-os-core/` | 12 | Rust | **Working** | GOVERNANCE, REVIEW, VAULT |

---

## 3. Detailed Component Analysis

### 3.1 sheldonbrain (46 files)

The sheldonbrain codebase is the knowledge substrate for the entire ecosystem. It implements a multi-component system for ingesting, classifying, and retrieving knowledge from AI agent conversations using a custom 144-sphere ontology and a RAG pipeline backed by Qdrant and Pinecone vector databases. The key working components are `ingest_grok_chats.py` (ingestion of Grok chat exports into Qdrant using LangChain and HuggingFace embeddings) and `reclassify_conversations.py` (AI-powered reclassification using Vertex AI). The `sheldonbrain-omega-v1/` subdirectory contains the GrokBrain v4 engine, the Janus Protocol for session continuity, and a simulation engine, all at prototype or spec stage. Three ZIP archives contain earlier iterations of the codebase. The primary gap is fragmentation: multiple RAG implementations exist without a unified deployment path, and the Pantheon Council consensus process remains manual.

### 3.2 sovereign-oracle (23 files)

The sovereign-oracle is a Python toolkit for building the autonomous operational core of the system. It contains the most mature implementations of several critical pipeline components. The `model_router.py` provides intelligent model selection based on task complexity and cost, while `multi_model.py` implements fallback chains and parallel consensus mechanisms across multiple LLMs. The `memory_store.py` provides persistent semantic memory via ChromaDB, and `autonomous.py` implements a `TaskDecomposer` for breaking goals into subtasks and a `SelfHealingExecutor` for error recovery. The `server.py` exposes these capabilities as a FastAPI REST API. The `output_layer.py` handles multi-format export (PDF, HTML, dashboards) and social publishing. The primary gap is the lack of a unified orchestration framework connecting these well-designed but loosely coupled components.

### 3.3 email-processing (23 files)

This directory is largely a fork of `sovereign-oracle` with the addition of `email_processing.py`, a rule-based email classifier that structures raw email data into JSON. The duplicate files (`autonomous.py`, `bridge.py`, `memory_store.py`, `multi_model.py`, `output_layer.py`, `server.py`) are near-identical to their sovereign-oracle counterparts. The unique value is the email parsing logic, which should be extracted and merged into the unified ingestion pipeline. The rest of this directory should be deprecated in favor of sovereign-oracle.

### 3.4 snrs (13 files)

The Sovereign Node Radius Stack (SNRS) codebase contains a Monte Carlo simulation (`snrs_v1_3_1_rewrite.py`) that models the economic feasibility of converting underutilized building stock into self-sustaining "dignity nodes." The simulation is working and produces 100-year financial projections using NumPy, Pandas, and SciPy. The `144_sphere_ingestion_protocol_Version2.py` is a prototype for cross-domain ontology synthesis. The remaining files are detailed specification documents (master spec, SHUGS whitepapers, ontology stress tests) that serve as the intellectual foundation for the SNRS project. The simulation is standalone and not yet integrated with the broader pipeline.

### 3.5 uws (11 files)

The Universal Workspace (UWS) directory is entirely specification-based, containing architectural reviews and integration guides from multiple AI collaborators (Claude, Grok, Gemini, Copilot). The `UWS_ALUMINUM_OS_V1_ARCHITECTURE.md` is the canonical architecture specification for the UWS CLI, defining the command grammar, provider abstraction layer, and kernel substrates. The `UWS_COPILOT_CLI_SPEC.md` specifies "Alexandria," the Microsoft-native counterpart. These specifications define the target for the Ring 2 Agent Runtime but contain no executable code. The primary gap is the translation of these detailed specs into a working Rust CLI.

### 3.6 atlas-lattice (11 files)

This codebase defines the constitutional and organizational foundation for the ecosystem. The `GOVERNANCE_CONSTITUTION_Pantheon_Council_v1.md` establishes the governance structure for multi-AI collaboration. The `LATTICE_DESKTOP_AGENT_Architecture_Spec.md` specifies a ChromeOS-based desktop agent. The `artifact_sync.py` is a Python prototype for synchronizing artifacts across Notion, Google Drive, and Pinecone using `rclone` and `manus-mcp-cli`. The Pinecone integration is a placeholder. This codebase provides critical governance documents and a key synchronization tool that should be completed and integrated into the VAULT pipeline stage.

### 3.7 aluminum-os (8 files)

This directory contains the visionary specifications for Aluminum OS, including the constitutional corpus, the Universal OS v2.0 spec (Sovereign Clipboard, Intent Routing Engine), cultural adapter specifications, and the hardware specification for the "Aluminum Link" connector. The `aluminum_os_unified_field.md` declares v3.0 "production ready" and integrates all constitutional, software, and hardware concepts. The `trinity_council_v3_aluminum.py` is a Python prototype that orchestrates data transfer between Google Drive, GCS, and Notion. The primary gap is the enormous distance between these detailed specifications and executable implementations.

### 3.8 data-pipeline (7 files)

This is the most complete implementation of the INGEST and COMPILER stages. The `gdrive_connector.py` handles Google Drive OAuth2 authentication and file fetching. The `ingestion_pipeline.py` implements staging, novelty detection via vector embeddings, and significance filtering using heuristics and a Gemini LLM. The `ontology_classifier.py` uses Gemini to classify content into the 144-sphere ontology. The `scheduler.py` provides periodic job execution via APScheduler, and `run_ingestion.py` is the CLI entry point. Dependencies include `google-api-python-client`, `langchain-huggingface`, `google-generativeai`, `qdrant-client`, and `structlog`. The primary gaps are robust error handling, monitoring, and integration with downstream pipeline stages.

### 3.9 saas-killer (6 files)

The saas-killer codebase is a Python-based RAG system with a FastAPI server (`api_server.py`), an ingestion pipeline with novelty detection, an ontology classifier, and Zapier webhook integration. The `api_server.py` provides endpoints for querying the knowledge base, ingesting documents, and health checks, with basic authentication and rate limiting. The `ingestion_pipeline.py` and `ontology_classifier.py` are nearly identical to their counterparts in `data-pipeline`. The unique value is the `zapier_webhooks.py` router and the `api_server.py` structure. The duplicate components should be consolidated with `data-pipeline`.

### 3.10 atlas-vault (3 files)

This small but valuable codebase contains three distinct components. The `automated_ingestion_pipeline.py` is a working ingestion system that fetches content from news feeds and web pages, uses TF-IDF for novelty filtering, and scores items for significance. The `krakoa_mcp_server.py` is a FastMCP-based server that exposes local filesystem, device controls (via ADB), and GCP resources to AI agents. The `krakoa_keep_module.py` vaults artifacts into Google Keep with organizational labels. These components are disconnected from each other and need to be integrated into a cohesive ingestion-to-vault workflow.

### 3.11 project-symbiote (1 file)

Project Symbiote is a Chrome extension prototype (`src_background.js`) that functions as an in-browser AI assistant. It uses the Anthropic Claude API to interpret user commands and the Google Drive API for file operations. It includes a constitutional safety layer for action approval. The extension is missing its UI (side panel, options page) and content script. It represents the Ring 3 Experience Layer's browser-based interface and should be developed further as the primary user-facing surface.

### 3.12 free-bank (1 file)

A single Markdown blueprint for an open-source, AI-powered banking application. It outlines a vision for decentralized finance using blockchain, DeFi, and AI, but contains no executable code. This falls outside the immediate scope of the Aluminum OS pipeline and should be archived.

### 3.13 codebases/other (48 files)

A mixed collection including another copy of `artifact_sync.py`, a Claude RAG specification (`claude_rag.py`), Chrome extension files (Vite + TypeScript + Gemini integration), Markdown knowledge base articles, and video files. The Chrome extension files represent an earlier or parallel iteration of Project Symbiote using Gemini instead of Claude. The `artifact_sync.py` duplicate confirms the need for consolidation.

### 3.14 aluminum-os-core (12 files, Rust)

This is the most mature and critical codebase in the entire repository. It is a working Rust policy engine that evaluates AI and automation workflows against the Net Positive Flourishing Metric (NPFM). The `AluminumEngine` in `src/lib.rs` composes five submodules: `classification` (5-dimensional agency scoring), `telemetry` (NPFM calculation), `routing` (displaced worker transition planning), `embodiment` (robotics safety gate), and `governance` (immutable audit trail). The engine accepts a `WorkflowProposal` and produces an `EngineVerdict` (Approved, Conditional, or Rejected). The integration test suite validates realistic scenarios including "Good Automation," "Busywork Generator," and "Untested Robotics." All 20 tests pass. This is the constitutional heart of Ring 0 and should be treated as foundational infrastructure.

---

## 4. Overlaps and Redundancies

The parallel development process has produced seven major areas of overlapping functionality that must be resolved.

| Overlap Area | Affected Codebases | Resolution |
| :--- | :--- | :--- |
| Ingestion pipelines | `data-pipeline`, `atlas-vault`, `sheldonbrain`, `saas-killer`, `email-processing` | Merge into unified `ring3-experience/ingest/` |
| Ontology classifiers | `data-pipeline`, `saas-killer`, `sheldonbrain` | Consolidate into `ring3-experience/compiler/` |
| Model routing | `sovereign-oracle`, `email-processing` | Keep `sovereign-oracle` version in `ring2-agent-runtime/router/` |
| Memory/vaulting | `sovereign-oracle`, `atlas-vault`, `atlas-lattice`, `codebases/other` | Unify into `ring2-agent-runtime/vault/` (Three-Tier Archive) |
| Agent orchestration | `sovereign-oracle`, `email-processing`, `aluminum-os` | Consolidate under BAZINGA middleware in `ring1-inference/` |
| API servers | `sovereign-oracle`, `saas-killer` | Merge into single FastAPI service |
| Artifact sync | `atlas-lattice`, `codebases/other` | Deduplicate; keep one canonical version |

The most significant redundancy is between `email-processing` and `sovereign-oracle`, which share approximately 80% of their code. The `email-processing` directory appears to be a fork that added email parsing logic without removing the parent files.

---

## 5. Gap Analysis

Beyond overlaps, several critical capabilities are missing from the current codebase and must be built as new glue code.

**Task Generation (TASK_GEN):** No component currently produces typed JSON task specifications from compiled artifacts. The `sovereign-oracle/autonomous.py` TaskDecomposer is the closest analog, but it operates on natural language goals rather than structured ontology output. A new module is needed that accepts compiled 144-sphere artifacts and emits typed task JSON conforming to a schema that the ROUTER can consume.

**Pipeline Orchestration:** No end-to-end orchestrator connects INGEST through VAULT. Each stage operates independently. A pipeline controller is needed, likely implemented as a Python service that sequences the stages and handles error recovery, retry logic, and state persistence.

**BAZINGA-to-NPFM Bridge:** The BAZINGA middleware (Ring 1, Rust) and the NPFM engine (Ring 0, Rust) are both specified but not yet connected. A Rust-level integration is needed where BAZINGA calls the `AluminumEngine.evaluate()` method before dispatching any task to the ROUTER.

**Python-to-Rust FFI:** The pipeline's Python components (Ring 2 and Ring 3) need to invoke the Rust governance engine (Ring 0). This requires either a Foreign Function Interface (FFI) bridge using PyO3 or a gRPC/REST service wrapper around the Rust engine.

**GitHub Integration:** The pipeline specifies GitHub as the source of truth, but no component currently automates commit, PR creation, or review assignment. A GitHub integration module using the `gh` CLI or GitHub API is needed.

**Monitoring and Observability:** No component provides health checks, metrics, or alerting for the pipeline. Structured logging via `structlog` is present in `data-pipeline` but not in other codebases.

---

## 6. Proposed Unified Repository Structure

The unified repository adopts a monorepo structure organized by the Four-Ring Architecture from Unified Field v4.0. Each ring is a top-level directory containing its language-specific build configuration.

```
manus-artifacts/
├── ring0-forge-core/                    # Rust — Constitutional kernel
│   ├── Cargo.toml                       # Workspace-level Cargo config
│   ├── aluminum-engine/                 # NPFM policy engine (from aluminum-os-core)
│   │   ├── src/
│   │   │   ├── lib.rs                   # AluminumEngine orchestrator
│   │   │   ├── classification/          # Task agency scoring
│   │   │   ├── telemetry/               # NPFM calculation
│   │   │   ├── routing/                 # Displaced worker tier routing
│   │   │   ├── embodiment/              # Robotics safety gate
│   │   │   └── governance/              # Immutable audit trail
│   │   └── tests/
│   └── invariants/                      # OPA Rego policies (NEW — to be built)
│       └── policies/
│
├── ring1-inference/                     # Rust — Constitutional middleware
│   └── bazinga/                         # BAZINGA v0.2 binary
│       ├── Cargo.toml
│       ├── CONSTITUTION.md
│       └── src/
│           ├── main.rs                  # CLI entry point (5 commands)
│           ├── engines/                 # Constitutional engine, TrustGuard
│           ├── adapters/                # Google, Microsoft, Apple providers
│           └── commands/                # sync-notion, sync-drive, sync-github, index, bench
│
├── ring2-agent-runtime/                 # Python — Agent execution
│   ├── pyproject.toml                   # Unified Python dependencies
│   ├── router/                          # Model selection and multi-model consensus
│   │   ├── model_router.py              # (from sovereign-oracle)
│   │   ├── multi_model.py               # (from sovereign-oracle)
│   │   └── cost_tracker.py
│   ├── vault/                           # Three-Tier Archive
│   │   ├── memory_store.py              # ChromaDB hot layer (from sovereign-oracle)
│   │   ├── artifact_sync.py             # Notion/Drive/Pinecone sync (from atlas-lattice)
│   │   └── krakoa_keep.py               # Google Keep staging (from atlas-vault)
│   ├── task_gen/                        # Task generation (NEW — to be built)
│   │   └── task_generator.py            # Compiled artifacts → typed JSON tasks
│   ├── orchestrator/                    # Pipeline controller (NEW — to be built)
│   │   └── pipeline.py                  # End-to-end stage sequencing
│   └── server/                          # FastAPI service (merged from sovereign-oracle + saas-killer)
│       └── api_server.py
│
├── ring3-experience/                    # Python + JS — User-facing surfaces
│   ├── ingest/                          # Unified ingestion pipeline
│   │   ├── gdrive_connector.py          # (from data-pipeline)
│   │   ├── email_processor.py           # (from email-processing)
│   │   ├── web_feed_ingester.py         # (from atlas-vault)
│   │   ├── chat_ingester.py             # (from sheldonbrain)
│   │   ├── ingestion_pipeline.py        # Core staging + novelty detection (from data-pipeline)
│   │   ├── scheduler.py                 # APScheduler job runner (from data-pipeline)
│   │   └── run_ingestion.py             # CLI entry point
│   ├── compiler/                        # 144-sphere ontology classification
│   │   ├── ontology_classifier.py       # Gemini-based classifier (consolidated)
│   │   └── reclassifier.py              # Re-classification logic (from sheldonbrain)
│   └── symbiote/                        # Chrome extension (from project-symbiote)
│       └── src/
│
├── specs/                               # Canonical specifications (read-only archive)
│   ├── constitution/                    # Governance documents
│   │   ├── unified-field-v4.0.md
│   │   ├── bazinga-launch-decree.md
│   │   └── governance-constitution.md
│   ├── architecture/                    # System design documents
│   │   ├── uws-v1-architecture.md
│   │   ├── aluminum-os-v2-spec.md
│   │   └── lattice-desktop-agent.md
│   └── research/                        # SNRS, SHUGS, and other research
│       ├── snrs/
│       └── shugs/
│
├── simulations/                         # Standalone simulation tools
│   └── snrs/                            # SNRS Monte Carlo simulation (from snrs/)
│       ├── snrs_simulation.py
│       └── requirements.txt
│
├── archive/                             # Deprecated codebases (preserved, not active)
│   ├── colab-notebooks/
│   ├── free-bank/
│   └── legacy-email-processing/
│
├── scripts/                             # Deployment and utility scripts
│   ├── setup.sh                         # Environment setup
│   └── migrate.sh                       # Migration script for restructuring
│
└── README.md
```

---

## 7. Component Disposition Table

The following table specifies the disposition of every current codebase directory.

| Current Location | Disposition | Destination | Rationale |
| :--- | :---: | :--- | :--- |
| `aluminum-os-core/` | **KEEP** | `ring0-forge-core/aluminum-engine/` | Working Rust engine, 20 tests passing, constitutional foundation |
| `codebases/data-pipeline/` | **KEEP** | `ring3-experience/ingest/` + `compiler/` | Most complete INGEST/COMPILER implementation |
| `codebases/sovereign-oracle/` | **KEEP** | `ring2-agent-runtime/router/` + `vault/` + `server/` | Best model router, memory store, and API server |
| `codebases/sheldonbrain/` | **MERGE** | `ring3-experience/ingest/chat_ingester.py` + `compiler/reclassifier.py` | Extract working ingestion and classification scripts |
| `codebases/atlas-vault/` | **MERGE** | `ring3-experience/ingest/web_feed_ingester.py` + `ring2-agent-runtime/vault/krakoa_keep.py` | Extract ingestion pipeline and Keep vaulting module |
| `codebases/atlas-lattice/` | **MERGE** | `ring2-agent-runtime/vault/artifact_sync.py` + `specs/constitution/` | Extract sync script and governance docs |
| `codebases/saas-killer/` | **MERGE** | `ring2-agent-runtime/server/api_server.py` | Extract API server structure and Zapier webhooks |
| `codebases/email-processing/` | **MERGE** | `ring3-experience/ingest/email_processor.py` | Extract email parsing logic only; rest is duplicate of sovereign-oracle |
| `codebases/snrs/` | **KEEP** | `simulations/snrs/` + `specs/research/snrs/` | Working simulation preserved; specs archived |
| `codebases/uws/` | **ARCHIVE** | `specs/architecture/` | Spec-only; informs Ring 2 development |
| `codebases/aluminum-os/` | **ARCHIVE** | `specs/constitution/` + `specs/architecture/` | Spec-only; canonical vision documents |
| `codebases/project-symbiote/` | **KEEP** | `ring3-experience/symbiote/` | Prototype Chrome extension for Ring 3 |
| `codebases/colab-notebooks/` | **DEPRECATE** | `archive/colab-notebooks/` | Interactive tutorial, not pipeline-compatible |
| `codebases/free-bank/` | **DEPRECATE** | `archive/free-bank/` | Out of scope; no executable code |
| `codebases/other/` | **MERGE** | Various | Extract Chrome extension to symbiote; archive rest |

---

## 8. New Glue Code Required

The following new modules must be written to connect the existing components into a functioning pipeline.

| Module | Location | Language | Purpose | Estimated Effort |
| :--- | :--- | :---: | :--- | :---: |
| Task Generator | `ring2-agent-runtime/task_gen/` | Python | Convert compiled 144-sphere artifacts into typed JSON task specs | 2-3 days |
| Pipeline Orchestrator | `ring2-agent-runtime/orchestrator/` | Python | Sequence INGEST → COMPILER → TASK_GEN → ROUTER → BUILD → VAULT | 3-5 days |
| BAZINGA-NPFM Bridge | `ring1-inference/bazinga/src/engines/` | Rust | Connect BAZINGA middleware to AluminumEngine for governance gates | 2-3 days |
| Python-Rust FFI | `ring0-forge-core/` | Rust + Python | PyO3 bindings or gRPC wrapper for Python to call NPFM engine | 3-5 days |
| GitHub Integration | `ring2-agent-runtime/` | Python | Automate commits, PR creation, and review assignment via `gh` CLI | 1-2 days |
| Monitoring Service | `ring2-agent-runtime/` | Python | Health checks, structured logging, and alerting for all stages | 2-3 days |

---

## 9. Dependency Management Strategy

The polyglot nature of the repository requires a coordinated dependency management approach.

**Rust (Ring 0 and Ring 1)** will use a Cargo workspace defined at `ring0-forge-core/Cargo.toml` and `ring1-inference/bazinga/Cargo.toml`. Current Rust dependencies are minimal and well-chosen: `serde`, `serde_json`, `chrono`, `uuid`, `thiserror`, `log`, `clap`, `tokio`, and `reqwest`. If PyO3 is adopted for the FFI bridge, it will be added as a workspace dependency.

**Python (Ring 2 and Ring 3)** will use a single `pyproject.toml` at the `ring2-agent-runtime/` level, managed by `uv` for fast, reproducible installs. The consolidated dependency set includes:

| Category | Packages |
| :--- | :--- |
| AI/ML SDKs | `google-genai`, `anthropic`, `openai`, `langchain`, `langchain-huggingface` |
| Vector DBs | `qdrant-client`, `chromadb`, `pinecone-client` |
| Web Framework | `fastapi`, `uvicorn`, `pydantic` |
| Data Sources | `google-api-python-client`, `google-auth-oauthlib`, `gkeepapi`, `gnews`, `feedparser`, `beautifulsoup4` |
| Scheduling | `apscheduler`, `schedule` |
| Utilities | `structlog`, `python-dotenv`, `tqdm`, `numpy`, `pandas`, `scipy`, `scikit-learn` |

**TypeScript/JavaScript (Ring 3 UI)** will use `pnpm` with a `package.json` in the `ring3-experience/symbiote/` directory. The Chrome extension dependencies include the Vite build system, the Anthropic SDK (or Gemini SDK), and Chrome Extension APIs.

---

## 10. Constitutional Governance Integration Points

The BAZINGA middleware serves as the constitutional checkpoint for the entire pipeline. The following table identifies where governance gates must be inserted.

| Pipeline Stage | Gate Type | Enforcement Mechanism | Invariants Checked |
| :--- | :--- | :--- | :--- |
| INGEST | **Zero Erasure Gate** | All ingested data is immutably logged before processing | INV-4 (Zero Erasure) |
| COMPILER | **Ontology Integrity Gate** | Classification must map to valid 144-sphere ontology entries | INV-29 (Spheres OS Lattice) |
| TASK_GEN | **NPFM Gate** | Every generated task is evaluated by AluminumEngine for net-positive flourishing | INV-15 (Sacred Species + Joy Metric) |
| ROUTER | **TrustGuard Gate** | Model selection must pass bitmask firewall; no untrusted models | INV-9 (TrustGuard Defense) |
| BUILD | **Dave Protocol Gate** | High-stakes operations require human-in-the-loop approval | INV-5 (Dave Protocol) |
| REVIEW | **Pantheon Consensus Gate** | Multi-AI review with adversarial challenge before vault commitment | INV-6 (Pantheon Harmony) |
| VAULT | **Audit Trail Gate** | Every vaulted artifact is cryptographically signed and logged | INV-1 (Agentic Sovereignty), INV-2 (Zero Erasure) |

---

## 11. Phased Implementation Roadmap

### Phase 1: Foundation and Restructuring (Weeks 1-2)

The immediate priority is to establish the monorepo structure without breaking any existing functionality. This phase involves creating the directory structure, moving files to their new locations, updating import paths, and verifying that the `aluminum-os-core` Rust tests still pass. All deprecated codebases will be moved to `archive/`. The canonical specifications will be organized under `specs/`. A root `README.md` will document the new structure and provide onboarding instructions.

**Deliverables:** New directory structure committed to GitHub. All Rust tests passing. Migration script (`scripts/migrate.sh`) that automates the restructuring.

### Phase 2: Unified Ingestion and Compilation (Weeks 3-4)

The focus shifts to Ring 3. The five disparate ingestion pipelines will be merged into a single service with pluggable connectors for Google Drive, email (via Gmail MCP), web feeds, and chat exports. The `data-pipeline` codebase provides the foundation; the unique logic from `atlas-vault`, `sheldonbrain`, `saas-killer`, and `email-processing` will be extracted and integrated as connector modules. The 144-sphere ontology classifier will be consolidated into a single implementation using the Gemini API, with Vertex AI as a fallback. The `run_ingestion.py` CLI will be updated to support all connector types.

**Deliverables:** Unified ingestion service with 4+ connectors. Consolidated ontology classifier. End-to-end test: ingest a document from Drive, classify it, and output structured JSON.

### Phase 3: Agent Runtime and Routing (Weeks 5-6)

Ring 2 development begins. The `sovereign-oracle` model router and memory store will be positioned as the core of the agent runtime. The "Three-Tier Archive" will be established by integrating ChromaDB (hot layer), Google Keep (staging), and Pinecone (cold/sovereign layer) behind a unified vault interface. The Task Generator module will be built to convert compiled artifacts into typed JSON task specifications. The Pipeline Orchestrator will be implemented to sequence all stages from INGEST through VAULT. The FastAPI server will be consolidated from the `sovereign-oracle` and `saas-killer` implementations.

**Deliverables:** Working model router with cost tracking. Three-Tier Archive with unified API. Task Generator producing typed JSON. Pipeline Orchestrator running end-to-end.

### Phase 4: Constitutional Integration and Testing (Weeks 7-8)

The final phase connects the governance layer. The BAZINGA-NPFM bridge will be built in Rust, allowing the BAZINGA middleware to call `AluminumEngine.evaluate()` before dispatching tasks. The Python-Rust FFI (via PyO3 or gRPC) will enable the Python pipeline orchestrator to invoke governance checks. All seven governance gates (identified in Section 10) will be implemented and tested. Comprehensive end-to-end integration tests will validate the complete pipeline from SESSION/INPUT through VAULT, including constitutional enforcement.

**Deliverables:** BAZINGA-NPFM bridge operational. Python-Rust FFI working. All governance gates enforced. End-to-end integration test suite passing. GitHub automation for PR creation and review assignment.

---

## 12. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
| :--- | :---: | :---: | :--- |
| Rust-Python FFI complexity delays Phase 4 | Medium | High | Start with gRPC wrapper (simpler); migrate to PyO3 later |
| Ingestion connector merge introduces regressions | Medium | Medium | Write integration tests for each connector before merging |
| Specification drift between docs and code | High | Medium | Treat `specs/` as read-only archive; code is source of truth |
| API key management across multiple providers | Medium | High | Centralize in `.env` with `python-dotenv`; rotate credentials |
| Scope creep from ambitious spec documents | High | Medium | Strict phase gates; only build what the roadmap specifies |

---

## 13. Success Criteria

The synthesis is complete when the following conditions are met:

1. The monorepo structure matches the proposed layout in Section 6.
2. The `aluminum-os-core` Rust engine passes all 20 existing tests plus new integration tests.
3. A document can be ingested from Google Drive, classified by the 144-sphere ontology, converted to a typed JSON task, routed to an appropriate AI model, built, reviewed by the NPFM engine, and vaulted, all in a single automated pipeline run.
4. Every pipeline stage has a corresponding BAZINGA governance gate that enforces the relevant constitutional invariants.
5. The pipeline state is persisted to GitHub as the source of truth after each successful run.
6. The Three-Tier Archive provides hot (ChromaDB), staging (Keep), and cold (Pinecone/IPFS) storage with a unified query interface.

---

*Compiled by Manus AI -- April 27, 2026*
*For Council Review: Claude, Grok, Gemini, Copilot, and Dave Sheldon (Constitutional Scribe)*
*GitHub: [atlaslattice/manus-artifacts/synthesis_plan.md](https://github.com/atlaslattice/manus-artifacts/blob/master/synthesis_plan.md)*
