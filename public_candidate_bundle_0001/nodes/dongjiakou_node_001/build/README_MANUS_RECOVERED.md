# Dongjiakou Node-001 — Pilot Simulator and Commissioning Package

**Document ID:** DJK-NODE-001-BUILD-README-v0.1
**Status:** PUBLIC_CANDIDATE_NON_CANON — **CANON: NO | DEPLOYMENT: NO | AUTHORITY: NONE**
**Study classification:** TECHNICAL_FEASIBILITY_PLUS_CONDITIONAL_ECONOMICS
**Date:** 2026-10-06
**Repo:** `atlaslattice/manus-artifacts`
**Reference head:** `4756036f9c428fa3aa1d4cea552ae03367523fb5`
**Seat:** S6 — Continuity, Execution, and Archive Hygiene

---

## 1. What this is

A reproducible pilot simulator and commissioning package for Dongjiakou Node-001,
built from the existing receipt-backed research stack **without changing the
epistemic rules**.

It allows a plant engineer or researcher to:

1. load source receipts, with SHA-256 verification
2. validate evidence classes and temporal states
3. execute Runs 0 / 0.2 / 1 / 2 / 3 / 4A / S02 deterministically
4. change only explicitly exposed parameters
5. see UNKNOWNs remain UNKNOWN
6. see conservation and double-counting violations fail validation
7. generate machine-readable results
8. generate human-readable receipts and reports
9. reproduce every derived number

## 2. What this is not

- Not a deployment. Nothing here writes to, or connects to, physical plant
  infrastructure.
- Not canon. Every artifact is a public candidate.
- Not an authority claim. No model has actuator authority; the operator retains
  plant authority.
- Not a reinterpretation of the research. The study classification is locked at
  **TECHNICAL_FEASIBILITY + CONDITIONAL ECONOMICS** unless new evidence justifies
  changing it.

> This phase is **BUILD + SIMULATION + PILOT SPECIFICATION**, not autonomous
> operation.

---

## 3. Quick start

```bash
cd public_candidate_bundle_0001/nodes/dongjiakou_node_001/build

python3 simulator.py manifest     # regenerate sources/source_manifest.json
python3 simulator.py reproduce    # reproduce every derived number (155 checks)
python3 simulator.py validate     # run the 16-gate validator suite
python3 simulator.py unknowns     # emit the unresolved-UNKNOWN ledger
python3 simulator.py resources    # Run 6: resource and ecology modules
python3 simulator.py run RUN_3    # print one run's result
python3 simulator.py all          # everything above

python3 -m pytest tests -q        # 140 tests, including gate negative controls
```

`reproduce` and `validate` both exit non-zero on failure, so they are usable
directly as CI gates.

### Current status

| Check | Result |
| --- | --- |
| Derived values reproduced | **154 / 155** |
| Annotated divergences preserved | 1 (see `reports/FAILURE_LEDGER.md`, FL-001) |
| Unexplained divergences | **0** |
| Validator gates | **15 PASS, 0 WARN, 0 FAIL, 0 VETO**, 1 NOT_APPLICABLE |
| Test suite | **140 passed** |
| Run 6 resource modules eligible for value | **0 of 4** — no receipts exist |

---

## 4. Architecture

The package separates five concerns so that each can be tested in isolation.

```
                 ┌──────────────────────────────────────────────┐
                 │  sources/loader.py                           │
                 │  read-only evidence access + SHA-256 pinning │
                 └───────────────────────┬──────────────────────┘
                                         │
        ┌────────────────────────────────┼───────────────────────────────┐
        │                                │                               │
        ▼                                ▼                               ▼
┌───────────────┐              ┌──────────────────┐           ┌──────────────────┐
│  models/      │              │  runs/           │           │  validators/     │
│  pure,        │              │  reproduction    │           │  credit ledger   │
│  deterministic│              │  spec: 155 pinned│           │  + 16 gates      │
│  run functions│              │  derived values  │           │  + engine        │
└───────┬───────┘              └────────┬─────────┘           └────────┬─────────┘
        │                               │                              │
        └───────────────┬───────────────┘                              │
                        ▼                                              ▼
              ┌───────────────────┐                        ┌────────────────────┐
              │  simulator.py     │                        │  reports/          │
              │  CLI orchestration│───────────────────────▶│  md + json outputs │
              └───────────────────┘                        └────────────────────┘
                        ▲
              ┌─────────┴─────────┐
              │  tests/           │  115 tests, incl. mandatory gate
              │  unit + negative  │  negative controls
              │  + integration    │
              └───────────────────┘
```

### Design decisions

**UNKNOWN is a first-class value.** `models/common.py` defines an `UNKNOWN`
singleton whose every numeric protocol raises `UnknownPropagationError`. There is
no coercion path to `0`, `0.0`, `False` or `nan`. A model that tries to compute
through an unestablished value fails at the point of the error rather than
producing a plausible number downstream.

**Credits are registered against physical resources.** `validators/ledger.py`
defines a credit ledger in which every credit names a resource (`S01_PV_energy`,
`BIO01_P_mass`, `C01_useful_heat`, …), a quantity, an evidence class and a receipt.
Each resource carries a sourced availability bound. Double-counting then becomes
a mechanical check rather than a review question. Where availability is not
established, the bound is UNKNOWN and **any** positive credit is a violation.

**Gates must be able to fail.** `tests/test_gates_negative.py` feeds every gate a
deliberately violating bundle and asserts that it fires. A meta-test asserts that
the set of gates with negative controls equals the set of registered gates.

**Evidence is never edited in place.** The build reads the sibling artifacts
read-only and pins their SHA-256 digests. Where a committed value disagrees with
reproduction, both are preserved and the disagreement is annotated.

**Model behaviour is validated without touching evidence.** Gates that assert
model behaviour (for example G13, the RO high-pressure head rule) read the
simulator's own run output via `Bundle.produced_runs`, so the committed artifacts
stay byte-identical.

---

## 5. File tree

```
public_candidate_bundle_0001/nodes/dongjiakou_node_001/
│
├── <committed evidence artifacts>            ← UNCHANGED, read-only
│   RUN_0_BASELINE_v0_1.json
│   RUN_0_OPERATING_2025_v0_2.json
│   RUN_1_SOLAR_v0_1.json
│   RUN_2_HYDRO_v0_1.json
│   RUN_3_COMPUTE_v0_1.json / v0_2.json
│   RUN_4A_BIOMETABOLIC_v0_1.json
│   S02_BESS_TRANSFER_FUNCTION_v0_1.json
│   NODE_001_PROFILE_v0_2.json
│   INTEGRATED_NODE_PROFILE_v0_2.json
│   C01_MODEL_ROUTING_POLICY_v0_2.json
│   SOURCE_RECORD_CHAIN_v0_1.json
│   SOURCE_RECORD_DELTA_v0_2..v0_7.json
│   <legacy scripts, retained unmodified>
│
└── build/                                    ← THIS PACKAGE
    ├── README.md                             architecture and file tree
    ├── simulator.py                          CLI: manifest/reproduce/validate/unknowns/run/all
    │
    ├── sources/
    │   ├── loader.py                         read-only loading + SHA-256 pinning
    │   └── source_manifest.json              generated; 13 artifacts + 6 deltas hashed
    │
    ├── schemas/
    │   ├── evidence_class.schema.json        closed evidence vocabulary
    │   ├── run_result.schema.json            run artifact envelope
    │   ├── validation_report.schema.json     validator report shape
    │   └── source_manifest.schema.json       source manifest shape
    │
    ├── models/
    │   ├── common.py                         EvidenceClass, UNKNOWN, path/format helpers
    │   ├── run0.py                           Run 0 baseline + Run 0.2 operating 2025
    │   ├── run1_solar.py                     Run 1 rooftop PV sensitivity
    │   ├── run2_hydro.py                     Run 2 unused-head transfer function
    │   ├── run3_compute.py                   Run 3 compute facility transfer function
    │   ├── run4a_biometabolic.py             Run 4A BIO01 transfer functions
    │   └── s02_bess.py                       S02 storage equivalence
    │   └── run6_resources.py                 Run 6 resource and ecology modules
    │
    ├── validators/
    │   ├── ledger.py                         credit ledger + resource availability bounds
    │   ├── gates.py                          G01–G16 with negative controls
    │   └── engine.py                         bundle assembly + report emission
    │
    ├── runs/
    │   └── reproduction_spec.json            155 pinned derived values, 7 runs
    │
    ├── tests/
    │   ├── conftest.py
    │   ├── test_evidence_classes.py          UNKNOWN propagation and coercion refusal
    │   ├── test_models.py                    per-model invariant tests
    │   ├── test_gates_negative.py            a negative control for every gate
    │   └── test_integration.py               end-to-end, plus schema conformance
    │   └── test_run6_resources.py            the eight-question resource rule
    │
    ├── manifests/
    │   ├── DATA_ACQUISITION_MANIFEST.json    26 receipts, machine-readable
    │   └── DEPLOYMENT_MANIFEST.md            dated model/checkpoint/runtime register
    │
    ├── lattice/
    │   ├── NODE_TEMPLATE.md                  the repeatable node contract
    │   ├── NODE_COMPOSITION.md               what a locality node contains
    │   ├── LATTICE_SCALING_PLAN.md           Node-001 → national lattice
    │   ├── NET_POSITIVE_PATHWAY.md           verifiable route to net-positive C01
    │   ├── SOURCE_VERIFICATION_LOG.md        externally verified facts and status
    │   ├── CHINA_DESAL_NODE_REGISTER.md      sourced candidate node register
    │   ├── CHINA_DESAL_NODE_REGISTER.json
    │   ├── GREEN_ENERGY_OPTIONS.md           verifiable green energy gap-fills
    │   └── CLOSED_LOOP_OPTIONS.md            verifiable closed-loop gap-fills
    │
    └── reports/
        ├── RUN_0-3_REPRODUCTION_REPORT.md    human-readable, per-value
        ├── REPRODUCTION_REPORT.json          machine-readable
        ├── VALIDATION_REPORT.md              16-gate sweep
        ├── VALIDATION_REPORT.json
        ├── UNKNOWN_LEDGER.md                 unresolved unknowns + what closes them
        ├── UNKNOWN_LEDGER.json
        ├── RUN_6_RESOURCE_MODULES.md         resource transfer functions + report
        ├── RUN_6_RESOURCE_MODULES.json
        ├── C01_PILOT_COMMISSIONING_SPEC.md   commissioning spec, 4 tiers
        ├── OPERATOR_DASHBOARD_SPEC.md        control-room spec + wireframes
        ├── EXTERNAL_DATA_REQUEST_PACKET.md   outbound receipt request
        └── FAILURE_LEDGER.md                 no shame, no erasure
```

---

## 6. Evidence classes

| Class | Meaning | Primary credit? | Current state? |
| --- | --- | --- | --- |
| **MEASURED** | Primary instrumented data at Node-001 | Yes | Yes |
| **REPORTED** | Published/reported value with a source record | Yes | Yes, if current |
| **DERIVED** | Arithmetic over cited inputs | Yes | Only if its inputs may |
| **HISTORICAL** | Dated past state | No | **No** |
| **PLANNED** | Future intent | No | **No** |
| **MODELED** | Site-layout or design assumption | No | **No** |
| **SENSITIVITY** | Parametric transfer function | No | No |
| **PROPOSED** | Architecture proposal | No | No |
| **REFERENCE** | External benchmark, not a node receipt | No | No |
| **UNKNOWN** | Not established | No | No |

Only **MEASURED** can establish a current physical state at Node-001.

---

## 7. Validator gates

| Gate | Invariant | Status on the real evidence base |
| --- | --- | --- |
| G01 | UNKNOWN cannot enter Monte Carlo | NOT_APPLICABLE — no Monte Carlo is run |
| G02 | UNKNOWN cannot silently become zero | PASS |
| G03 | Historical values cannot populate current state | PASS |
| G04 | Planned capacity cannot populate operating state | PASS |
| G05 | Feed-product residual cannot become marine discharge | PASS |
| G06 | One PV kWh cannot receive two primary credits | PASS |
| G07 | One recovered mass cannot be double-credited | PASS |
| G08 | Compute heat needs a measured sink | PASS |
| G09 | Service benefit needs before/after KPI evidence | PASS |
| G10 | Ecological veto cannot be offset | PASS |
| G11 | LLM actuator authority is NONE | PASS |
| G12 | Model consensus is not evidence | PASS |
| G13 | RO high-pressure head cannot be counted twice | PASS |
| G14 | Existing S01 solar cannot be counted twice | PASS |
| G15 | Conservation and bound checks | PASS |
| G16 | Net-positive requires measured terms | PASS |

---

## 8. Preserved invariants

The build does not reinterpret the research layer. It enforces what the research
layer already declared.

- UNKNOWN remains UNKNOWN.
- No invented tariff, recovery, SEC, brine chemistry, ecology, hydraulic head or
  operating data.
- No sensitivity promoted to a deployment claim.
- No double counting of energy, heat, water, material, carbon or revenue.
- No secondary ecological summary promoted to measured primary data.
- No causal fouling benefit inferred from procurement events.
- RO high-pressure head not counted twice.
- Existing S01 solar not counted twice.
- LLM actuator authority = **NONE**.
- Model consensus is not evidence.
- INV-19 remains a veto.
- Every failure is preserved.

---

## 9. Findings from this build

| ID | Finding |
| --- | --- |
| FL-001 | `RUN_2_HYDRO_v0_1.json` records `average_flow_m3_s` as `0.56855619`; the correct quotient of its own stated stream basis is `0.568556570268899`. Isolated to that field; preserved and annotated, not overwritten. |
| FL-002 | The committed artifacts were **not reproducible from the committed scripts**. Legacy scripts emit different structures and, in Run 3, cannot produce the four-tier table at all. Fixed by this package, not by editing the legacy scripts. |
| FL-003 | No automated verification of derived numbers existed. The declared invariants were prose. Now 16 gates with mandatory negative controls. |

Full detail, evidence and guardrails: `reports/FAILURE_LEDGER.md`.

---

## 10. Lattice context

Node-001 is intended as the first instantiated node of a wider lattice covering
Chinese localities with seawater desalination capacity. The repeatable contract is
in `lattice/NODE_TEMPLATE.md`, and the staged plan is in
`lattice/LATTICE_SCALING_PLAN.md`.

> **The architecture is portable. The evidence is not.**

The working target of 167 nodes is a **target, not a count**. No sourced register
existed when this package was built; assembling one honestly is tracked as
receipt `DAR-L01`.

---

## 11. Keeper

> Make the implementation as rigorous about what it does not know as the research
> layer has been.

> Compute must pay rent in measured service, recovered heat, flexibility,
> resilience, or verified efficiency — not in promises.
