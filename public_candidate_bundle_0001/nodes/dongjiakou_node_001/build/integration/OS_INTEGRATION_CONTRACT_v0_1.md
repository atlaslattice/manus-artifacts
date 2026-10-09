# Continuum / Aluminum / UWS / DragonSeek integration contract v0.1

STATUS: SCHEMA PUBLIC REVIEW CANDIDATE | CANON: no | DEPLOYMENT: no | AUTHORITY: none | PROOF: no | PUBLIC_RELEASE: candidate

Prepared2026-10-08 America/Chicago (2026-10-09 UTC). Scope: component discovery, pinned references, a proposed interface map and a working offline export packet. No external OS service, CLI driver or model endpoint is connected by this change.

## Why integrate now

The locality simulator now exposes physical scenarios, evidence boundaries, unresolved vetoes and a first-class QOL vector. These are useful shared contracts for a broader operating substrate: every service can refer to the same dated source, uncertainty, affected cohort and authority boundary. Start with one offline node packet and verify its interpretation in each component before expanding scope.

## Component roles and maturity

| Component | Source examined | Proposed interface | Review finding |
|---|---|---|---|
|Continuum OS / Alexandria2.0 |[README at26e166a](https://github.com/atlaslattice/continuum-os/blob/26e166a169036b03e4731ad5d5e283fc441ad586/README.md) |Index immutable artifacts, evidence classes, source lineage and compatibility metadata. |The README describes an integration/index surface with independent repositories. It does not prove a deployed national OS or every registry runtime. |
|Aluminum OS |[README at562f80e](https://github.com/atlaslattice/aluminum-os/blob/562f80e05472005516f7532306a516f2fa30dfdb/README.md) |Identity/consent, memory, governance and agent workspace orchestration. |Current README points to UWS as the executable command-surface path. The May2026 source-of-truth document contains older topology/authority vocabulary; preserve its date and reconcile rather than treating all descriptions as the same implementation. |
|UWS |[README atdbc89bd](https://github.com/atlaslattice/uws/blob/dbc89bd1a3d7727a04cf7cf30e1401ee9b118a0f/README.md) |Future JSON command adapter: read evidence, run approved offline scenario, export review packet. |Public universal branch exists. No UWS installation or provider-driver compatibility test was performed here. Preserve its Apache2.0/upstream licensing and provenance. |
|DragonSeekOS |[Existing fork spec](https://github.com/atlaslattice/manus-artifacts/blob/85f06406c724067ef917c55761ba5ff4354409ef/archive/forks/dragonseek-os/repo-seed/DRAGONSEEK_OS_FORK_SPEC_v0.1.md) |China-localized advisory workflow, vocabulary, infrastructure and reviewed local regulatory mapping. |An archived, explicitly candidate dialect/runtime design exists. A target repository name is not evidence that the repository or a deployed service exists. The June local-boot receipt preserves a user report and explicitly lacks verified runtime logs. |
|Atlas Intelligence / Atlas Prime |Named retrieval/evidence role in existing architecture and archives |Return source-linked review claims, uncertainty and contradiction records. |No exact standalone implementation repository was located by the focused search. This interface role is proposed; do not claim a tested service. |
|Aluminum OS v3 |[README atdeb6dfc](https://github.com/atlaslattice/aluminum-os-v3/blob/deb6dfc225e05082c5015cb32ba918e7a465c9ea/README.md) |Candidate reusable modules after build/API/security review. |README states bare-metal and cross-device limitations. Its headline “shipped OS”must not override its own honest-limit section. No boot/build validation was performed here. |

Each component retains its own history, license, authority and permissions. The repository pins and review scope are in [component_refs.json](component_refs.json). Do not copy entire code trees or apply this build's MIT license to another repository's code or documentation.

## First executable seam

```bash
python simulator.py packet
```

This exports a schema-validated, content-hashed offline locality/QOL packet. It performs zero provider/model calls and has no actuator authority. A consumer can parse it and preserve UNKNOWN, evidence status, QOL strata and six unresolved ecology/accounting vetoes. [Packet schema](packet.schema.json).

Optional `--revision FULL_SHA`records a supplied source revision; it never authenticates that assertion. The default is null for an unverified working tree. A release consumer must separately verify the repository commit, source manifest and packet bytes. Content addressing proves byte identity, not truth, authorship, receipt validity or physical performance.

The packet's outer classification is SIMULATED. Embedded reports or references retain their own classes and boundaries. Model-produced claims enter as review claims. Retrieval must preserve contradictory/null results and avoid promoting repeated model text into corroborated evidence.

## Authority and namespace boundaries

Physical PLC/SCADA/safety control remains an independent deterministic/operator-controlled layer. OS scheduling, model advice, evidence retrieval and QOL observation confer no actuator authority. A service outage must not become a plant safety dependency. Public research APIs expose aggregate/synthetic data only; no credentials, raw operational telemetry or individual health/location records are introduced.

Invariant IDs require a source namespace. For example, the older Aluminum source-of-truth's INV-20 concerns a neural/other substrate, while the Dongjiakou register's INV-20 concerns marine net-positive discharge. These are different definitions. Preserve original IDs and source documents, and refer to `djk-locality-001:INV-20`or an explicitly mapped OS ID. Never join rules solely because their short identifiers match.

QOL and ecology have non-compensable safeguards. Resource output, model confidence, votes, profit, cultural narrative or a composite score cannot override a failed local safety/privacy/ecological gate. The absence of a harm finding does not establish net-positive benefit. Community benefit is assessed through locally valid, voluntary and disaggregated measurement, not automated social ranking or individual enforcement.

## AtlasSeek / DragonSeek2.0 model path

These are proposed names for an Atlas application/profile or a future documented derivative. A retrieval profile, an API adapter, an open-weight deployment, a fine-tune and an upstream model fork are different artifacts; record which one exists at each release.

DeepSeek's current official materials list V4.1-Flash, with API alias `deepseek-flash`. The official [model card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) and [LICENSE](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/LICENSE) show MIT licensing. That supports a derivative path while retaining required attribution/notices. It does not grant trademark rights, partnership status, government authorization or readiness of a training dataset.

The September release announcement and current API pricing/update pages contain differing V4-Pro routing statements; retain date/version and verify actual served model at runtime instead of assuming an alias pins weights. See [official update log](https://api-docs.deepseek.com/updates/) and [current model table](https://api-docs.deepseek.com/quick_start/pricing/). A deployable profile needs exact artifact revision, license file hash, inference runtime/quantization, observed hardware/memory/latency, evaluations, data permissions and budget. These remain unknown.

Recommended progression:

1. Offline evidence/QOL packet and source-linked retrieval/profile; zero paid calls required for this contract.
2. One isolated UWS/Aluminum adapter with permission checks, receipt logging, timeout/failure behavior and cross-component conformance tests.
3. Versioned AtlasSeek/DragonSeek advisory profile against approved public research; evaluate citation fidelity, UNKNOWN preservation, quantity/unit errors, regional language and hostile-source handling.
4. Consider local weights or fine-tuning only after an exact base revision/license, dataset rights, privacy separation, hardware budget and useful measured advantage are established. Model training is not started by this PR.

A broad national or municipal infrastructure OS is a research/adaptation horizon. Adoption, legal authority and public-sector deployment require independent stakeholder processes and documented decisions. This publication makes no claim of PRC/CAC/NDRC approval or any vendor's institutional endorsement.

## First acceptance test

A consumer receives the Dongjiakou packet, identifies it as simulated/review candidate, retains32 QOL dimensions and unknown cohorts, preserves all six local vetoes and their namespace, rejects any actuation request, and emits a source-linked review record. No source is promoted because a model repeats it. Only after that round trip is tested should additional services or nodes be connected.
