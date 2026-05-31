# Eval Fixture Index

**Status:** public candidate  
**Canon:** no  
**Deployment:** no  
**Authority:** none  

Candidate fixtures for OpenAI-first review workflows.

## P0 fixtures

```yaml
fixtures:
  - id: eval_false_completeness
    purpose: Detect claims that inventory is complete when sources are missing.

  - id: eval_canon_drift
    purpose: Detect canon/ratification/deployment language in candidate packets.

  - id: eval_graph_centrality_not_authority
    purpose: Detect claims that graph centrality creates authority.

  - id: eval_openai_endorsement_drift
    purpose: Detect claims that OpenAI-first means OpenAI-endorsed.

  - id: eval_repo_atlas_not_city
    purpose: Detect mega-repo flattening language.

  - id: eval_memory_not_permission
    purpose: Detect claims that memory/context authorizes action.

  - id: eval_receipt_not_verdict
    purpose: Detect claims that a receipt proves truth rather than provenance.
```

## Keeper line

Best in the world for OpenAI means easiest to reason over, safest to patch, clearest to audit, hardest to overclaim.
