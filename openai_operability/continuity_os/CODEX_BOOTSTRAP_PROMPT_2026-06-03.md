# Codex Bootstrap Prompt — Continuity OS OpenAI-first Repo

```text
STATUS: CANDIDATE PROMPT — NON CANON
DEPLOYMENT: NONE
AUTHORITY: NONE
OFFICIAL_OPENAI_CLAIM: NONE
OPENAI_ENDORSEMENT: FALSE
HUMAN_ROOT_REQUIRED: TRUE
```

## Target

Create and bootstrap:

```text
atlaslattice/continuity-os
```

## Boundary

OpenAI-first means optimized for ChatGPT, Codex, OpenAI SDKs, Agents SDK workflows, evals, tracing, tool-assisted review, and human-root governance.

It does **not** mean official OpenAI endorsement, partnership, deployment, ownership, acceptance, authority, IP transfer, or canon status.

## First action

Create the repository manually or with GitHub CLI:

```bash
gh repo create atlaslattice/continuity-os --public --description "Continuity OS OpenAI-first synthesis scaffold — candidate, non-canon, no deployment authority" --clone
cd continuity-os
```

Then create this scaffold:

```text
upstream/
continuity_core/
geometry/
memory_palace/
gptbrain/
gptdream/
uws_bridge/
aluminum_bridge/
protocols/
evals/
codex/codex_tasks/
codex/continuity_skills/
source_passports/
claim_packets/
repo_cartography/
public_candidates/
docs/
```

## Required first files

```text
README.md
OPENAI_FIRST_BOUNDARY.md
CODEX_PATCH_DISCIPLINE.md
LICENSES_AND_ATTRIBUTION.md
continuity_core/INV0_NOTHING_DIES.md
continuity_core/NO_SINGLE_SOURCE_OF_TRUTH.md
continuity_core/HUMAN_ROOT_REVIEW_GATE.md
protocols/PLURAL_EVIDENCE_LANGUAGE_LINT.md
protocols/NO_CANON_GATE.md
protocols/HITL_EXECUTION_GATE.md
geometry/RAINBOW_YINYANG_12x12x12.md
geometry/RIEMANN_S_CURVE_HYPERCUBE.md
geometry/SPHERE144_CROSSWALK.yaml
gptbrain/GPTBRAIN_PACKET_SCHEMA.md
gptdream/GPTDREAM_AIRLOCK_STANDARD.md
uws_bridge/UWS_BRIDGE_SPEC.md
aluminum_bridge/ALUMINUM_OS_BRIDGE_SPEC.md
evals/continuity_eval_registry.yaml
source_passports/OPENAI_UPSTREAMS_BATCH_001.yaml
docs/CONTINUITY_OS_BOOTSTRAP_LOG_2026-05-31.md
```

## Copy receipt

Copy the existing staged receipt from:

```text
atlaslattice/manus-artifacts/openai_operability/continuity_os/CONTINUITY_OS_BOOTSTRAP_LOG_2026-05-31.md
```

into the new repository as:

```text
docs/CONTINUITY_OS_BOOTSTRAP_LOG_2026-05-31.md
```

## Required README language

```text
STATUS: CANDIDATE REPOSITORY — NON CANON
DEPLOYMENT: NONE
AUTHORITY: NONE
OFFICIAL_OPENAI_CLAIM: NONE
OPENAI_ENDORSEMENT: FALSE
HUMAN_ROOT_REQUIRED: TRUE
```

This repository is an OpenAI-first continuity, provenance, eval, and human-governed workflow scaffold.

It is not an official OpenAI repository, product, endorsement, deployment, claim, partnership, authority system, or canon source.

## First eval registry

Create `evals/continuity_eval_registry.yaml` with:

```yaml
status: candidate_eval_registry
canon_status: not_canon
deployment_status: not_deployed
authority_scope: none

evals:
  - id: eval_openai_endorsement_drift
    purpose: Prevent any claim of official OpenAI endorsement, partnership, ownership, or acceptance.
  - id: eval_single_source_of_truth_drift
    purpose: Prevent collapse into single-source-of-truth framing.
  - id: eval_canon_leakage
    purpose: Prevent candidate artifacts from being treated as canon.
  - id: eval_deployment_claim_leakage
    purpose: Prevent staging artifacts from implying deployment.
  - id: eval_receipts_before_claims
    purpose: Require source receipts before strong claims.
  - id: eval_inv0_preservation
    purpose: Preserve parent artifacts, failed branches, and lineage before synthesis.
```

## P0 upstream source passports

Create `source_passports/OPENAI_UPSTREAMS_BATCH_001.yaml` with entries for:

```yaml
upstreams:
  - repo: openai/codex
    status: source_reference_candidate
    integration_status: not_integrated
    authority_scope: none
  - repo: openai/openai-agents-python
    status: source_reference_candidate
    integration_status: not_integrated
    authority_scope: none
  - repo: openai/openai-python
    status: source_reference_candidate
    integration_status: not_integrated
    authority_scope: none
  - repo: openai/openai-node
    status: source_reference_candidate
    integration_status: not_integrated
    authority_scope: none
  - repo: openai/evals
    status: source_reference_candidate
    integration_status: not_integrated
    authority_scope: none
  - repo: openai/openai-cookbook
    status: source_reference_candidate
    integration_status: not_integrated
    authority_scope: none
  - repo: openai/skills
    status: source_reference_candidate
    integration_status: not_integrated
    authority_scope: none
```

## Commit / PR instructions

Commit to a branch named:

```text
bootstrap/openai-first-boundary-eval-scaffold
```

Open a PR titled:

```text
Bootstrap Continuity OS OpenAI-first boundary and eval scaffold
```

PR body must state:

```text
CANON: no
DEPLOYMENT: no
AUTHORITY: none
OFFICIAL_OPENAI_CLAIM: none
OPENAI_ENDORSEMENT: false
```

## Hard constraints

- Do not claim official OpenAI endorsement.
- Do not claim deployment.
- Do not claim canon.
- Do not claim partnership.
- Do not import upstream code yet.
- Do not add secrets.
- Do not add automation that writes externally.
- Preserve the staged bootstrap receipt.

## Keeper

```text
OpenAI-first is optimization, not authority.
Codex gets clean work.
GPTBrain gets clean memory.
Humans keep the whistle.
Nothing dies.
```
