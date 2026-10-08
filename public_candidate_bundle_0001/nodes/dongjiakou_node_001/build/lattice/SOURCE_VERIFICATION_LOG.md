STATUS: ARCHIVE PUBLIC CANDIDATE | CANON: no | DEPLOYMENT: no | AUTHORITY: none | PROOF: no | PUBLIC_RELEASE: candidate

Recovered historical Manus artifact. Current review decisions: [build/review/EVIDENCE_APPENDIX.md](https://github.com/atlaslattice/manus-artifacts/blob/master/public_candidate_bundle_0001/nodes/dongjiakou_node_001/build/review/EVIDENCE_APPENDIX.md).

# Source Verification Log

**Document ID:** DJK-LATTICE-SOURCE-VERIFICATION-LOG-v0.1
**Status:** PUBLIC_CANDIDATE_NON_CANON
**Date:** 2026-10-06
**Repo:** `atlaslattice/manus-artifacts`
**Reference head:** `4756036f9c428fa3aa1d4cea552ae03367523fb5`

---

## 1. Purpose

This log records externally sourced facts used by the Node-001 build package,
together with their source URLs and the verification status of each. It exists so
that a later reader can re-check any claim without re-deriving it, and so that
**unverified** material is never mistaken for verified material.

Verification status values:

| Status | Meaning |
| --- | --- |
| **VERIFIED** | Independently re-fetched and the specific figures matched the source during this build |
| **CITED** | Source located and plausible; not independently re-fetched in this build |
| **UNVERIFIED** | Transcribed from a repository artifact; not checked against a primary source |

---

## 2. Repository-internal definitions

### 2.1 ORCS

| Field | Value |
| --- | --- |
| Expansion | **Ontology-Routed Context Spine** |
| Source | `archive/architecture/APPENDIX_I_ATLAS_ORCS_EPISTEMIC_PROFILE_V0_3_2026-05-21.md` and `archive/boot/gptbrain/LATTICE_ORCS_BRIDGE_PROTOCOL.md` |
| Status | Repository artifact, candidate, not canon |

Formal definition as recorded in Appendix I:

```
A = (S, Δ, Π, Γ, κ)

S   = possible archive states
Δ   = append-only deltas
Π   = Atlas promotion operator
Γ_t = ORCS governance profile at time t
κ   = CAS-001-A cryptographic receipt / anchor function
```

Governance profile and state evolution:

```
Γ_t      = (Θ_t, W_t, Φ_t, R_t)
S_{t+1}  = S_t ⊕ δ_t
σ(e; Γ_t) = w_c C(e) + w_r R(e) + w_p P(e) + w_a A(e)
```

Load-bearing invariant:

```
Π^q_{Γ_t}(S_t) ⊆ E(S_t)
```

> Atlas promotes from retained evidence. Atlas does not create truth. Atlas only
> selects and elevates what already exists under governance.

Boundary stated in the source: *a high score produces promotion eligibility, not
automatic ratification or truth. Ratification requires an explicit authority
event: human-root / S10.*

Must-not-infer block as recorded:

```
Recorded ≠ promoted
Promoted ≠ ratified
Ratified ≠ deployed
Canonicalized ≠ true
Hashed ≠ meaningful
Receipt-bearing ≠ approved
```

Keeper line as recorded: *The ledger records. Atlas promotes. ORCS governs. CAS
anchors. Nobody pretends the scoreboard created the game.*

**Use in this build:** ORCS supplies the promotion discipline applied to any
net-positive claim in `NET_POSITIVE_PATHWAY.md`, and the evidence vocabulary in
`models/common.py`. No ORCS artifact is ratified, and none of this work ratifies
it.

### 2.2 Evidence boundary ladder

| Stage | Meaning |
| --- | --- |
| raw log | evidence |
| parser output | retrieval aid |
| model assessment | evaluator signal |
| hypothesis | unscored claim |
| candidate canon | review-ready artifact |
| ratified canon | published through Council workflow |

Source: `archive/boot/seats/MANUSBRAIN_S6_EXECUTION_AGENT_SPEC_2026-05-08.md`.

---

## 3. Externally verified claims

### 3.1 Reverse electrodialysis (RED) pilot in an SWRO desalination plant

| Field | Value |
| --- | --- |
| Claim used | Pilot RED stack in a seawater desalination plant; 299 cell pairs, 179.4 m² effective membrane area; maximum gross power density 0.96 W/m² with natural RO brine and 1.46 W/m² with model RO brine; SW controls 0.62 and 0.97 W/m² |
| Source | Sugimoto et al., "Power Generation Performance of a Pilot-Scale Reverse Electrodialysis Using Monovalent Selective Ion-Exchange Membranes," *Membranes* 11(1):27, 2021 |
| URL | https://www.mdpi.com/2077-0375/11/1/27 |
| Status | **VERIFIED** — re-fetched during this build; abstract states 299 cell pairs, 179.4 m², and exactly 0.96 / 1.46 W/m² (natural / model RO brine) against 0.62 / 0.97 W/m² for natural / model seawater |
| Caveat | These are I–V peak gross power densities, not continuous net plant output. The paper is a pilot study, not a commercial deployment. |

### 3.2 Lake-source cooling at Cornell University

| Field | Value |
| --- | --- |
| Claim used | Operating deep-water cooling system saves over 29 million kWh/year versus previous cooling methods, about an 85% reduction in campus cooling energy; operating since July 2000 |
| Source | Cornell University, Facilities and Campus Services, "Lake Source Cooling" |
| URL | https://fcs.cornell.edu/departments/energy-sustainability/district-energy-water/district-cooling/cooling-production/lake-source-cooling |
| Status | **VERIFIED** — search results during this build returned the Cornell Facilities page stating "LSC saves over 29 million kWh per year versus previous cooling methods … about an 85% reduction in energy used for campus cooling" |
| Disagreement noted | Some secondary sources state **20 million** kWh/year and others **25 million** kWh/year (for example a DOE-hosted district-energy presentation citing an average of 25 million kWh/year). The figures differ by source and period. Treat the saving as **20–29 million kWh/year, ~85% reduction**, and cite the Cornell Facilities page for the 29 million figure. |
| Caveat | This is a **freshwater lake** system, not seawater air conditioning. It is an analogue for deep-water cooling, not a direct transferable result for a coastal node. |

### 3.3 China national desalination project count

| Field | Value |
| --- | --- |
| Claim used | The figure of 167 refers to the national count of desalination **engineering projects**, not a count of localities |
| Source | Recorded in `lattice/CHINA_DESAL_NODE_REGISTER.json` (`count_reconciliation` field) from the research pass |
| Status | **CITED** — asserted by the research pass against Chinese national plan and seawater-utilisation reporting; the specific source documents are listed in the register's `source_documents` array |
| Consequence | The locality count and the project count are different quantities. The node unit is the locality (human-root decision, 2026-10-06), so the node count is expected to be lower than 167. Both must be reported and neither substituted for the other. |

---

## 4. Research-register claims

The two gap-fill registers contain further sourced claims. Their full source
lists are authoritative and are not duplicated here:

| Register | Sources | Verified in this build |
| --- | --- | --- |
| `GREEN_ENERGY_OPTIONS.md` | 10 sources, each with year and evidence role | 1 of 10 independently re-fetched (RED, §3.1) |
| `CLOSED_LOOP_OPTIONS.md` | 13 sources, each with year and evidence role | 0 independently re-fetched |

**Honest statement of coverage:** only two headline claims were independently
re-fetched during this build (§3.1 and §3.2). The remaining citations were located
by the research pass and are recorded as **CITED**, not **VERIFIED**. A reviewer
should treat them as sourced-but-not-independently-confirmed.

Both registers explicitly mark options for which **no verifiable result was
located** rather than filling the gap with an estimate:

| Register | Options documented | Options with no verifiable result |
| --- | --- | --- |
| `GREEN_ENERGY_OPTIONS.md` | 11 | 2 |
| `CLOSED_LOOP_OPTIONS.md` | 11 | 2 |

---

## 5. Unverified repository-transcribed material

| Item | Location | Status |
| --- | --- | --- |
| Model version references: DeepSeek-V4.1-Flash, DeepSeek-V4-Pro, Qwen3 family, Qwen3.8, GPT-5.6 Sol | `C01_MODEL_ROUTING_POLICY_v0_2.json`, restated in `manifests/DEPLOYMENT_MANIFEST.md` | **UNVERIFIED** — transcribed, not checked against vendor documentation. No benchmark receipt exists at Node-001. Treat every version string as UNKNOWN-until-verified. |
| PUE = 1.25 as a sector reference | `RUN_3_COMPUTE_v0_2.json`, source records DJK-SR-0026 / DJK-SR-0027 | **UNVERIFIED in this build** — the artifact cites its source records; the underlying policy documents were not re-fetched. It is explicitly labelled a reference, not a Node-001 receipt. |
| Shandong 2023 average grid factor 0.6191 kgCO₂/kWh | `RUN_1_SOLAR_v0_1.json` | **UNVERIFIED in this build** — labelled REPORTED_LATEST_OFFICIAL_FACTOR_LOCATED in the artifact. Not a 2026 marginal factor and not a lifecycle PV calculation. |
| Regional plan: ~214 MW wind, ~81 MW PV around Qianwan/Dongjiakou, ~5 MW port-area PV | `INTEGRATED_NODE_PROFILE_v0_2.json` | **UNVERIFIED in this build** — recorded as REPORTED regional plan. Node access remains UNKNOWN and the energy credit is zero. |

---

## 6. Maintenance rule

- New external claims enter this log with a URL, a year and a status.
- A claim is promoted from CITED to VERIFIED only by re-fetching the source and
  matching the specific figures.
- Where sources disagree, both values are recorded with the disagreement noted.
- Nothing in this log is canon, and nothing in it authorises a physical action.
