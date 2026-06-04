# Schemas

> *Status: CANDIDATE — not canon until ratified by @atlaslattice*

## What This Folder Is

The `schemas/` domain is the machine-readable contract layer for Atlas Lattice. It packages the structural definitions that let candidate artifacts, routed packets, and ingestion events be validated consistently instead of relying on prose-only interpretation.

At present there are three schema families: `atlas_orcs`, `native_thread`, and `o_ai`. Together they define the epistemic governance surface, the native thread ingestion packet, and the O_AI interoperability packet/routing conventions described by the GPTDream++ vault manifest.

## Start Here

→ [GPTDream++ Vault Manifest](../archive/spec/gptdream/VAULT_MANIFEST_2026-05-26.md)

## Contents

| Resource | Description |
|---|---|
| [`atlas_orcs/`](./atlas_orcs/) | Atlas/ORCS governance schema family for artifacts, claims, trust, audit, and ratification. |
| [`native_thread/`](./native_thread/) | Native thread ingestion schema family for thread capture and handoff. |
| [`o_ai/`](./o_ai/) | O_AI packet schema, routing table, and interoperability support files. |
| [`atlas_orcs/v0_1/atlas-artifact.schema.yaml`](./atlas_orcs/v0_1/atlas-artifact.schema.yaml) | Representative core schema for candidate artifact records. |

## Related Domains

- [Reference Implementations](../reference_impl/) — the implementations here are the code-side counterparts to these contracts.
- [Archive](../archive/) — the GPTDream++ vault manifest and appendices explain why these families exist.
- [Docs](../docs/) — knowledge-graph and governance docs describe how schemas support validation and provenance.

---
*Atlas Lattice Foundation · Austin, Texas*
