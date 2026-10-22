---
artifact_id: OPENAI-ADJACENT-GITHUB-TOOL-AUDIT-2026-05-30
title: "OpenAI Adjacent GitHub Tool Audit"
version: "0.1"
date: 2026-05-30
status: candidate_audit
canon_status: not_canon
deployment_status: not_deployed
authority_scope: none
write_scope: staging_only
source_surface: GitHub search over atlaslattice org
---

# OpenAI Adjacent GitHub Tool Audit

```text
STATUS: candidate_audit
CANON: no
DEPLOYMENT: no
AUTHORITY: none
QUESTION: Are all OpenAI-adjacent useful tools on GitHub forked and integrated?
ANSWER: No. Several are forked/present; full integration is not yet proven.
```

## Confirmed present / forked or repo-visible

```yaml
present_repos:
  - repo: atlaslattice/open-webui
    visibility: public
    archived: true
    integration_status: forked_or_present_not_active_integration
    lane: UI / local model interface / OpenAI-adjacent front end

  - repo: atlaslattice/AutoGPT
    visibility: public
    archived: true
    integration_status: forked_or_present_not_active_integration
    lane: autonomous-agent framework / historical reference

  - repo: atlaslattice/langchain
    visibility: public
    archived: true
    integration_status: forked_or_present_not_active_integration
    lane: agent/retrieval/tooling framework

  - repo: atlaslattice/browser-use
    visibility: public
    archived: true
    integration_status: forked_or_present_not_active_integration
    lane: browser automation / agentic web use

  - repo: atlaslattice/dify
    visibility: public
    archived: true
    integration_status: forked_or_present_not_active_integration
    lane: workflow/app builder / RAG-agent platform

  - repo: atlaslattice/A2A
    visibility: public
    archived: unknown_from_compact_result
    integration_status: forked_or_present_needs_review
    lane: agent-to-agent protocol / interop

  - repo: atlaslattice/ollama
    visibility: public
    archived: true
    integration_status: forked_or_present_not_active_integration
    lane: local model runtime / non-OpenAI interop

  - repo: atlaslattice/sheldonbrain-rag-api
    visibility: public
    archived: false
    integration_status: active_candidate_ingestion_tool
    lane: Sheldonbrain lineage ingestion

  - repo: atlaslattice/uws
    visibility: public
    archived: false
    integration_status: active_candidate_universal_workspace_shell
    lane: connector/adapter substrate

  - repo: atlaslattice/aluminum-os
    visibility: public
    archived: false
    integration_status: active_candidate_os_substrate
    lane: Aluminum OS / integration substrate
```

## Confirmed searched but not found under `atlaslattice`

```yaml
not_found_in_current_search:
  - llamaindex
  - semantic-kernel
  - crewai
  - autogen
```

## Caution

```text
Forked/present does not mean integrated.
Archived fork does not mean active tool lane.
Integration requires adapter path, source passport, build/test status, security boundary, and graph node/edge mapping.
```

## Integration status categories

```yaml
integration_status_enum:
  - not_found
  - found_archived_reference
  - found_active_unintegrated
  - found_active_candidate_adapter
  - integrated_staging
  - integrated_with_tests
  - public_release_ready
```

## Recommended next actions

```text
1. Create OPENAI_ADJACENT_TOOL_MATRIX.yaml.
2. Give every repo a SourcePassport.
3. Separate archived reference forks from active integration lanes.
4. Prioritize active integration around Sheldonbrain, UWS, Aluminum OS, OpenAI Agents/API patterns, GitHub issue/PR workflow, and source-passport ingestion.
5. Add missing candidates to watchlist: LlamaIndex, Semantic Kernel, CrewAI, AutoGen, OpenAI Agents SDK examples, MCP reference servers.
6. Do not integrate everything blindly; classify by OpenAI benefit, security risk, maintenance state, and fit to the provenance graph.
```

## Keeper

```text
Forked is not integrated.
Archived is not active.
Present is not useful until routed.
Useful is not canon.
Integrate with receipts.
Nothing dies.
```
