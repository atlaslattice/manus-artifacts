# Atlas Lattice Archipelago ORCS Index

```text
STATUS: CROSS-REPO ROUTE INDEX — NOT CANON
DATE: 2026-05-09
RUNTIME_LABEL: WORK_OUTPUT / MODEL_ASSESSMENT
PURPOSE: wire accessible Atlas Lattice repositories into Krakoa / GPTBrain / ORCS routing without exposing private repo names in a public artifact
CANON WARNING: this index is routing metadata. It does not ratify canon, deploy services, authorize execution, or make private repositories public.
```

## 0. Privacy boundary

`atlaslattice/manus-artifacts` is public.

The accessible GitHub repo inventory includes both public and private repositories. This public index therefore:

```text
- explicitly lists public repositories discovered through the connector;
- does not publish private repository names;
- records private repositories only as redacted connector-only groups;
- requires human-root review before any private repo names, contents, or routes are exported into public artifacts.
```

## 1. Plain-language definition

The Atlas Lattice Archipelago is the cross-repository project map.

Krakoa is the living archive island.
ORCS is the routing spine.
GPTBrain is the calibration booth.
Each repository is an island, dock, archive, lab, or domain outpost.

This index wires the archipelago at the routing layer only.

## 2. Core invariants

```text
1. Public repos may be listed publicly.
2. Private repos must not be named in public artifacts without explicit human-root approval.
3. Repo existence is not deployment evidence.
4. Route metadata is not execution authority.
5. Archived repos are preserved as fossil record, not treated as active services.
6. GPTBrain can index, summarize, route, and calibrate; it cannot ratify canon or authorize deployment.
7. Swarm/deployment readiness remains governed by Issue #26 or repo-specific deployment issues.
```

## 3. Public core / foundation repos

| Repo | Route class | Status | Notes |
|---|---|---|---|
| `atlaslattice/manus-artifacts` | KRAKOA_HUB / FOSSIL_RECORD / GPTBRAIN_BOOT | public | Current hub for GPTBrain, Krakoa, ORCS, wake reports, issues, and artifact seeds. |
| `atlaslattice/atlaslattice` | ROOT_IDENTITY / ORG_PORTAL | public | Minimal organization/root presence. |
| `atlaslattice/sheldonbrain-rag-api` | SHELDONBRAIN_RAG / MEMORY_API | public | RAG/API substrate candidate; requires separate inspection before runtime claims. |
| `atlaslattice/Sovereign-Shredder-Core` | SOVEREIGN_SHREDDER / CORE_TOOLING | public | Core tooling candidate; route through claim calibration and security review. |
| `atlaslattice/A2A` | A2A_ARCHIVE / FOSSIL_RECORD | public / archived | Archived; preserve as fossil record, not active runtime. |

## 4. Public ethics / policy / accountability repos

These route primarily through:

```text
AI_ETHICS_DOMAIN
POLICY_ANALYSIS
ACCOUNTABILITY_TOOLING
RISK_AND_AUDIT
PUBLIC_ARCHIVE
```

```text
atlaslattice/awesome-ai-ethics
atlaslattice/ai-bias-detection
atlaslattice/algorithmic-accountability
atlaslattice/deepfake-detection
atlaslattice/ai-transparency-toolkit
atlaslattice/ethical-ai-guidelines
atlaslattice/ai-fairness-metrics
atlaslattice/machine-learning-bias
atlaslattice/ai-labor-practices
atlaslattice/content-moderation-ethics
atlaslattice/ai-safety-research
atlaslattice/responsible-ai-toolkit
atlaslattice/ai-governance-framework
atlaslattice/explainable-ai-tools
atlaslattice/ai-risk-assessment
atlaslattice/data-privacy-tools
atlaslattice/ai-audit-framework
atlaslattice/algorithmic-justice
atlaslattice/ai-worker-rights
atlaslattice/tech-ethics-resources
atlaslattice/ai-impact-assessment
atlaslattice/facial-recognition-ethics
atlaslattice/ai-surveillance-critique
atlaslattice/gig-economy-analysis
atlaslattice/platform-worker-rights
atlaslattice/ai-copyright-issues
atlaslattice/synthetic-media-ethics
atlaslattice/ai-misinformation-detection
atlaslattice/automated-decision-systems
atlaslattice/ai-accountability-tools
atlaslattice/digital-rights-toolkit
atlaslattice/ai-regulation-tracker
atlaslattice/tech-worker-organizing
atlaslattice/ai-training-data-ethics
atlaslattice/algorithmic-discrimination
atlaslattice/ai-policy-analysis
atlaslattice/tech-accountability-framework
atlaslattice/ai-employment-impact
atlaslattice/digital-labor-rights
atlaslattice/ai-consent-framework
atlaslattice/predictive-policing-critique
atlaslattice/ai-healthcare-ethics
atlaslattice/automated-hiring-bias
atlaslattice/ai-credit-scoring-fairness
atlaslattice/social-media-algorithms
atlaslattice/ai-content-moderation
atlaslattice/tech-monopoly-analysis
atlaslattice/ai-pricing-discrimination
atlaslattice/digital-surveillance-tools
atlaslattice/ai-recommendation-systems
```

## 5. Redacted private connector-only groups

Private repositories were visible to the connector but are not enumerated here because this file is public.

They should be routed only inside permissioned/private surfaces until Dave explicitly approves public disclosure.

Recommended private route groups:

```text
PRIVATE_RESEARCH_ARCHIVES
PRIVATE_DOMAIN_CRITIQUES
PRIVATE_INFRA_OR_CONTEXT_REPOS
PRIVATE_POLICY_DRAFTS
PRIVATE_HEALTH_OR_SAFETY_CONTEXT
PRIVATE_FINANCE_OR_BANKING_CONTEXT
```

Minimum handling rule:

```text
private_repo_name: REDACTED_CONNECTOR_ONLY
visibility: private
public_export_allowed: false unless human_root_approved
```

## 6. Standard repository route packet

```yaml
repo_route_id: <stable id>
repo_full_name: <owner/name or REDACTED_CONNECTOR_ONLY>
visibility: public | private | redacted
archived: true | false
route_classes:
  - <route class>
source: github_connector
claim_class: parsed_artifact
confidence: C2
runtime_label: WORK
public_export_allowed: true | false
human_root_required: true
notes: <routing notes>
```

## 7. Cross-repo route classes

```text
KRAKOA_HUB
GPTBRAIN_BOOT
ORCS_ROUTE_SPINE
FOSSIL_RECORD
ROOT_IDENTITY
SHELDONBRAIN_RAG
SOVEREIGN_SHREDDER
A2A_ARCHIVE
AI_ETHICS_DOMAIN
POLICY_ANALYSIS
ACCOUNTABILITY_TOOLING
RISK_AND_AUDIT
PUBLIC_ARCHIVE
PRIVATE_CONNECTOR_ONLY
DEPLOYMENT_READINESS_UNKNOWN
```

## 8. Next action

Create a machine-readable public-safe seed index:

```text
archive/boot/gptbrain/ATLASLATTICE_PUBLIC_REPO_ROUTE_INDEX.seed.jsonl
```

Then create a private-routing protocol note that explains how to handle private repos without publishing names into public artifacts.

## 9. Madden booth call

BOOM. Krakoa just zoomed out from one island to the whole archipelago.

Public islands get named on the map.
Private islands stay under fog until Dave says otherwise.
GPTBrain can circle routes with the telestrator, but it does not open private gates or launch services.

The archipelago is wired at the map layer.
Deployment is still a separate sport.
