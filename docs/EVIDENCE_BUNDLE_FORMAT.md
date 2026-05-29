# Evidence Bundle Format

Status: Candidate
Date: 2026-05-28

Defines the canonical structure for evidence bundles that document AI systems built by @atlaslattice. This format enables traceable, verifiable, world-class public evidence of AI work.

## Purpose

Evidence bundles capture:
1. **System-built evidence**: proof that a specific AI system, model, or integration was designed and implemented by @atlaslattice.
2. **Capability evidence**: functional outputs demonstrating real-world capability.
3. **Lineage evidence**: traceability chain from concept → spec → implementation → test.

## Bundle Structure

An evidence bundle is a directory or JSON manifest:

```
evidence/<system-name>/
  manifest.json          # required: bundle metadata
  spec/                  # optional: design docs, specs
  implementation/        # optional: code pointers or snippets
  tests/                 # optional: passing test receipts
  outputs/               # optional: screenshots, logs, demo outputs
  provenance.md          # required: human-readable narrative
```

### manifest.json schema

```json
{
  "bundle_id": "<unique ID, e.g. EV-001>",
  "system_name": "<display name>",
  "author": "@atlaslattice",
  "date": "<ISO 8601>",
  "status": "Candidate | Ratified",
  "canon": false,
  "system_type": "agent | model | integration | protocol | infrastructure",
  "description": "<one-paragraph description>",
  "capability_claims": [
    { "claim": "<text>", "evidence_file": "<path to evidence>" }
  ],
  "lineage": {
    "concept_artifact": "<path>",
    "spec_artifact": "<path>",
    "implementation_artifact": "<path>",
    "test_artifact": "<path>"
  },
  "related_nodes": ["<N-XXXX>", "..."]
}
```

### provenance.md required sections

Every `provenance.md` must include:
1. **System summary** — what it is and what it does.
2. **Author attestation** — explicit statement of authorship by @atlaslattice.
3. **Key artifacts** — list of linked files with creation dates.
4. **Capability claims** — cross-referenced with evidence files.
5. **Governance status** — candidate/ratified, ratification event ID if applicable.

## Examples

- `archive/boot/gptbrain/` — GPTBrain AI system evidence
- `archive/spec/gptdream/` — GPTDream++ protocol evidence
- `reference_impl/` — Reference implementation evidence

## Validation

Evidence bundles are validated by:
1. `manifest.json` schema check (future CI gate).
2. Existence of all referenced `evidence_file` paths.
3. `provenance.md` section completeness check.

## Related

- [ARTIFACT_LINEAGE.md](./ARTIFACT_LINEAGE.md)
- [CANON_LIFECYCLE.md](./CANON_LIFECYCLE.md)
- [CHILDREN_SWARM_LATTICE.md](./CHILDREN_SWARM_LATTICE.md)
- [LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md](./LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md)
