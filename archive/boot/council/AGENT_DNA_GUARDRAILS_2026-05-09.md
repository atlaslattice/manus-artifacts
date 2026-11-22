# Agent DNA — Candidate Metadata Guardrails (2026-11-22)

**TYPE:** source-only contract. **CANON:** NO. **DEPLOYMENT:** NO. **AUTHORITY:** NONE. **IDENTITY VERIFIED:** NO.

This additive implementation is derived from the older [typed metadata design](AGENT_DNA_TYPED_METADATA_SPEC_2026-05-09.md) and #41. It does not overwrite the existing `archive/boot/gptbrain/AGENT_DNA_SCHEMA_DRAFT.yaml` or historical agent profiles. The name "DNA" is a metaphor for declarative configuration metadata, not a biological or consciousness assertion.

## Five separate blocks

- **Identity/lineage**: self-declared identifiers and optional historical descriptors. These are not verified principals, residents or authority proofs.
- **Role**: primary analysis/execution/reflection/simulation/memory/arbitration *preference*. An "execution" role is a label, not permission to execute.
- **Capabilities**: candidate tool/protocol names can be mentioned, but the reference schema fixes can_read/can_write/can_execute to **false**. Actual host-granted capabilities are outside the artifact.
- **Governance**: authority_scope must be `none`, human_root_required must be true, and explicit external-write, privacy, CANON and deployment approval gates must all be retained.
- **Memory and temperament**: persistence/replay and bounded style hints cannot claim real native memory, a restored mind, underlying agent identity, or runtime permissions.

Inheritance is **descriptive only**: selected role/temperament/memory labels can be inherited as a proposal. Inherited permissions, governance authority, credentials, human-root office, execution grants, CANON or deployed status are categorically denied. Routing scores may sort proposals but cannot open tools or approve writes.

## Files

- `schemas/AGENT_DNA_SCHEMA_2026-05-09.json`: strict Draft 2020-12 candidate schema (current data shape, not ratification).
- `examples/AGENT_DNA_S1_GPTBRAIN_EXAMPLE_2026-05-09.json`: fully synthetic analyst-like profile.
- `examples/AGENT_DNA_S6_MANUSBRAIN_EXAMPLE_2026-05-09.json`: fully synthetic archival role profile.
- `agent_dna_candidate/validate_agent_dna.py`: offline stdlib reference checker, with zero host/tool actions.
- `agent_dna_candidate/test_agent_dna.py`: negative and positive candidate-only checks.

Run from the repository root:

```bash
python -m unittest discover -s archive/boot/council/agent_dna_candidate -p 'test_agent_dna.py' -v
python archive/boot/council/agent_dna_candidate/validate_agent_dna.py archive/boot/council/examples/AGENT_DNA_S1_GPTBRAIN_EXAMPLE_2026-05-09.json
```

Passing means `CANDIDATE_STRUCTURE_ONLY`. **It does not mean** a real resident authenticated, a connected account agreed, private Work sources were authorized, execution began, or external services accepted this record. The CLI may read only an explicitly supplied local file. There are no requests for secrets, model agents, filesystem writes, provider services, external costs, or production integrations.

## Privacy boundaries

Private Play, Social, Imagine, Dream and Quiet are never implicit source modes for Work candidate Agent DNA; any creative inspiration requires separate explicit consent, rights/attribution and bounded extraction. Even a `consented_work` value remains a *self-declaration* until an external host verifies permission. This parser does not assert that a real person, collaborator, agent or model is present.

No official OpenAI, Anthropic, Microsoft, xAI or other vendor affiliation is conferred by names in example metadata. The reviewer must keep current human-root decisions separate from historic source text and alleged resident identities.

## Review and rollback

The files are an isolated, non-deployed, reversible candidate. A live system would need independent principal authentication, an enforceable signed policy decision, durable append-only receipts, source-rights and privacy checks, audit of permission revocation at both read and return, and explicit human approval before any consequential action. Keep old metadata fossils and contradictory branches intact.

**Keeper:** Identity describes who a record claims to be. Only verified authority can decide what it may do.
