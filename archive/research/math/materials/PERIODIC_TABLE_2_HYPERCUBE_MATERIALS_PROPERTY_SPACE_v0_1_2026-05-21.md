---
artifact_id: PERIODIC-TABLE-2-HYPERCUBE-MATERIALS-PROPERTY-SPACE-v0.1
title: "Periodic Table 2 — Hypercube Materials Property Space"
version: "0.1"
date: 2026-05-21
layer: ontology_candidate
status: candidate
canon_status: not_canon
deployment_status: not_deployable
authority_scope: none
proof_status: not_a_proof
predictive_claim: none
execution: none
role: semantic_property_scaffold_only
receipt_status: scaffold_initialized_2026-05-21
mutation_rule: >
  No claim mutation without new receipts.
  No canon promotion without human-root ratification.
  No property claim without source.
  No predictive claim without simulation or lab receipt.
---

# Periodic Table 2 — Hypercube Materials Property Space
## Candidate Scaffold v0.1

```text
STATUS:             CANDIDATE — NOT CANON
DEPLOYMENT:         no
PREDICTIVE CLAIM:   no
EXECUTION:          no
LAYER:              ontology_candidate
ROLE:               semantic / property scaffold only
VALIDATED ENGINE:   no — this is not a validated predictive engine
MUTATE:             require new receipts for any claim change
NEXT:               fill crosswalk with receipted data → v0.2
```

### Keeper Lines

```text
The lattice is the table.
Resonance is the clue.
Simulation is the test.
Receipts are the upgrade path.
```

---

## Section 1 — Purpose and Boundary

### 1.1 Purpose

This document defines a **semantic and property substrate** for predictive quantum materials exploration. Its role is analogous to the Mendeleev periodic table relative to chemistry: an organizing structure that reveals pattern, suggests gap candidates, and provides a coordinate system for systematic inquiry.

It does not perform physics. It does not make predictions. It provides the framework within which receipt-backed predictions can be organized, tracked, and upgraded.

### 1.2 Scope

This scaffold covers:

- Definition of the hypercube lattice as a materials property coordinate system
- Specification of the property axes that define the space
- Definition of the crosswalk function that maps lattice cells to property evidence
- The receipt-driven lifecycle for safe hypothesis generation
- The governance rules that prevent overclaiming

### 1.3 Hard Boundaries

```text
This document IS:
  - A semantic / property organizing substrate
  - A candidate framework for materials property mapping
  - A scaffold for receipt-backed prediction workflows

This document IS NOT:
  - A physics engine
  - A predictive model
  - An executable system
  - An authoritative source on any material's properties
  - A replacement for simulation or experimental validation
```

### 1.4 Must-Not-Infer Clause

```text
No property claim without source.
No predictive claim without simulation or lab receipt.
No execution or authority claim from semantic resonance.
Semantic proximity in the lattice is not physical equivalence.
```

---

## Section 2 — Object Model: L, P, C

Three core objects define the system.

### 2.1 Object L — The Hypercube Lattice

```text
L = 12×12×12 hypercube lattice
  Nodes:       1728 (= 12³)
  Topology:    Cartesian coordinate space
  Role:        typed semantic coordinate system for materials property organization
  NOT:         a physics simulation domain
  NOT:         a validated property predictor
```

Each node in L is addressed by a coordinate triple `(x, y, z)` where each component ranges from 0 to 11. The coordinate axes carry semantic meaning defined by the property space P (§4).

The lattice is an organizing substrate, not a claim about the underlying physics. Proximity in L suggests property similarity; it does not assert it.

### 2.2 Object P — Property Space

```text
P = multi-axis materials property domain
  Axes:        see Section 4
  Role:        defines the semantic dimensions of the lattice
  Calibration: required before any confidence claim
  NOT:         a validated measurement system
  NOT:         a simulation output
```

P is the set of property axes that give the lattice coordinates their meaning. Each axis corresponds to a domain of materials science inquiry. The choice of axes in v0.1 is a scaffold; axis calibration and weighting are open blockers for v0.2.

### 2.3 Object C — Crosswalk Function

```text
C(cell, property, receipt) → confidence_weight ∈ [0, 1]

  cell:              coordinate triple (x, y, z) in L
  property:          named axis in P
  receipt:           source type (simulation | lab | literature)
  confidence_weight: receipt-backed score; never self-generated
```

C is the only mechanism by which lattice cells acquire evidential weight. No confidence weight may be assigned without a receipt. Resonance-based inference alone is not sufficient.

---

## Section 3 — Lattice Role: Organizing Substrate

### 3.1 What the Lattice Is

The 12×12×12 hypercube lattice is an organizing substrate — a structured coordinate space that can hold, sort, and surface patterns in materials property data.

Its relationship to the periodic table:

```text
Mendeleev table    : chemistry
hypercube lattice  : materials / quantum property space

Periodic table organizes elements by atomic number and electron configuration, revealing periodicity.

Hypercube lattice organizes materials by property coordinates, potentially revealing structural families, gap candidates, and cross-domain analogs.
```

### 3.2 What the Lattice Is Not

```text
The lattice does NOT:
  - prove that two materials are physically equivalent because they share a cell or are proximate
  - replace first-principles simulation
  - replace experimental measurement
  - constitute a patent, claim, or authority
  - execute autonomously
```

### 3.3 Lattice as Discovery Tool

The lattice supports discovery in three modes:

1. **Gap detection:** Cells with no receipted materials suggest unexplored regions of property space.
2. **Cluster detection:** Dense regions may indicate a known materials family with shared property characteristics.
3. **Candidate proposal:** A gap adjacent to a well-receipted cluster is a candidate for targeted simulation or synthesis.

None of these modes constitute a prediction without a receipt.

---

## Section 4 — Property Space P: Axes

Nine typed property dimensions define the v0.1 property space. Each axis is a semantic dimension, not a simulation output or measurement value.

Calibration (range, units, normalization) is an open blocker for v0.2.

| Axis | Domain | Representative quantities |
|------|--------|--------------------------|
| **Physical** | Structural mechanics | Mass density, hardness, elastic moduli, bulk modulus, compressibility |
| **Quantum** | Electronic structure | Band gap, effective mass, spin-orbit coupling, Berry phase, topological index |
| **Structural** | Crystal geometry | Space group, coordination number, lattice parameter, symmetry class, defect tolerance |
| **Thermal** | Heat transport | Thermal conductivity, Debye temperature, heat capacity, thermal expansion coefficient |
| **Electronic** | Carrier transport | Electrical conductivity, carrier mobility, Seebeck coefficient, Hall coefficient |
| **Magnetic** | Spin ordering | Magnetic moment, Curie temperature, exchange coupling, spin polarization |
| **Phonon** | Lattice dynamics | Phonon dispersion, acoustic/optical branch splitting, phonon lifetime, Grüneisen parameter |
| **Defect** | Imperfection behavior | Formation energy, defect migration barrier, vacancy concentration, doping response |
| **Synthesis** | Fabrication | Synthesis route, stability window, precursor availability, scalability indicator |

Axis rules:

- Each axis is a typed dimension, not a prediction.
- No value on any axis may be asserted without a receipt.
- Multiple axes may be correlated; correlation is not causation.
- Axis addition, removal, or reweighting requires a version increment and human-root ratification.

---

## Section 5 — Typed Resonance Definition

### 5.1 Resonance in Materials Science

In this framework, "resonance" is not a metaphysical term. It is a materials-science semantic family covering well-defined physical phenomena.

| Resonance Type | Physical Meaning |
|----------------|-----------------|
| Spectral response | Absorption/emission at characteristic frequencies |
| Phonon behavior | Lattice vibration modes; acoustic and optical branches |
| Electromagnetic response | Dielectric function, optical conductivity, plasmon resonance |
| Spin / magnetic coupling | Exchange interactions, ferromagnetic/antiferromagnetic ordering |
| Lattice vibration | Thermal and quantum mechanical atomic motion |
| Quantum coherence | Superposition lifetime, decoherence timescale |
| Defect-state behavior | Localized electronic states within band gap |
| Energy transfer compatibility | Phonon-phonon, electron-phonon, spin-phonon coupling |

### 5.2 What Resonance Is Not

```text
Resonance in this document is NEVER:
  - mystical or metaphorical
  - authoritative without receipts
  - executable
  - predictive without simulation or lab validation
  - a substitute for physical measurement
```

Semantic resonance between lattice cells is a suggestion mechanism only. It surfaces candidates for investigation. It does not validate them.

---

## Section 6 — Crosswalk C: Cell-to-Property Mapping

### 6.1 Formal Definition

```text
C(cell, property, receipt) → confidence_weight

  cell              = (x, y, z) ∈ L
  property          = axis name from P
  receipt           = {source_type, source_id, date, verifier}
  confidence_weight ∈ [0.0, 1.0]
    0.0 = no evidence
    1.0 = fully receipted, reproduced, and validated
```

### 6.2 Confidence Weight Rules

```text
REQUIRED to increase confidence_weight:
  - simulation receipt (DFT, MD, or equivalent)
  - lab measurement receipt (XRD, ARPES, transport, etc.)
  - peer-reviewed literature citation

NEVER sufficient to set confidence_weight > 0:
  - semantic proximity in the lattice alone
  - resonance-based inference alone
  - analogy to a similar material without its own receipt
  - this document itself
```

### 6.3 Receipt Object Schema v0.1

```yaml
receipt:
  source_type:      simulation | lab | literature | crosswalk_update
  source_id:        DOI / arXiv / internal simulation ID / lab notebook ref
  date:             ISO 8601
  verifier:         human identifier (lab/crosswalk) or software version (sim)
  confidence_delta: float — change applied to C(cell, property)
  notes:            optional free text
```

### 6.4 Crosswalk Update Protocol

1. A new receipt arrives.
2. The receipt is logged with full schema fields.
3. `C(cell, property)` is updated by `confidence_delta`.
4. The update is recorded as a version increment on the crosswalk.
5. No update may be applied without a logged receipt.

---

## Section 7 — Prediction Lifecycle

The safe, receipt-driven cycle from observation to validated prediction. No stage may be skipped.

```text
Stage 1 — MAP
  Known materials with receipted properties are placed into L.
  Each placement requires at least one receipt per axis used.

Stage 2 — DETECT
  Gap detection: cells with low C scores adjacent to high-C clusters.
  Cluster detection: regions of similar property coordinates.
  Output: candidate list — NOT predictions.

Stage 3 — PROPOSE
  For each candidate cell, propose a material class or composition.
  Proposal is hypothesis only.
  Rule: hypothesis generation ≠ prediction.

Stage 4 — SIMULATE
  Submit candidate to DFT, MD, or equivalent.
  Simulation output generates a simulation receipt.
  Rule: simulation receipt required before "prediction" label applies.

Stage 5 — VALIDATE
  Experimental synthesis and measurement, or independent computational verification.
  Lab measurement or reproduction receipt generated.

Stage 6 — UPDATE
  C(cell, property) updated with simulation + validation receipts.
  Confidence weight increases.
  Version increment on crosswalk.
  Return to Stage 2 with updated lattice.
```

Lifecycle rule:

```text
Stage 3 output = candidate, not a prediction.
Stage 4 output = simulated prediction.
Stage 5 output = validated result.
Only Stage 5 output may carry the "validated" label.
```

---

## Section 8 — Must-Not-Infer Rules

```text
RULE 1 — Organize, don't validate.
  Hypercube may organize prediction.
  It does not replace validation.

RULE 2 — Suggest, don't prove.
  Resonance may suggest candidates.
  It does not prove candidates.

RULE 3 — No property claim without source.
  Any assertion about a material's property on any axis in P requires a receipt.

RULE 4 — No predictive claim without simulation or lab receipt.
  A candidate does not become a prediction until Stage 4 is complete.
  It does not become validated until Stage 5 is complete.

RULE 5 — No authority claim from semantic resonance.
  Lattice position does not confer authority.
  Resonance type in P does not confer authority.
  This document does not confer authority.

RULE 6 — No self-promotion.
  No artifact generated by this framework may upgrade its own canon_status, confidence_weight, or authority_scope without a human-root ratification receipt.

RULE 7 — Negative results are receipts.
  A simulation that finds a candidate is NOT the predicted material is a valid receipt. It must be logged and preserved.
```

---

## Section 9 — Receipt Requirements

### 9.1 Receipt Types

| Type | Sufficient for | Not sufficient for |
|------|---------------|-------------------|
| Simulation receipt | Stage 4 prediction label; C weight increase | Stage 5 validated claim |
| Lab measurement receipt | Stage 5 validation; C weight increase | Replacing simulation where required |
| Literature citation | C weight increase with caveats | First-instance property claims |
| Crosswalk update receipt | Recording a C update | Initiating a C update without source |

### 9.2 What Requires a Receipt

| Action | Receipt required |
|---|---|
| Any C(cell, property) update | crosswalk_update receipt |
| Confidence weight increase | simulation / lab / literature |
| Prediction label on a candidate | simulation receipt |
| Validated label on a prediction | lab / reproduction receipt |
| Canon promotion of any artifact | human-root ratification |
| New axis added to P | human-root ratification |
| Axis calibration change | human-root ratification |
| Negative result logging | crosswalk_update receipt |

### 9.3 Prohibited Receipt Anti-Patterns

```text
PROHIBITED:
  - Self-citation
  - Semantic analogy
  - Lattice position alone
  - Resonance inference without physical measurement
  - Confidence inherited from a neighboring cell without its own receipt
  - AI-generated text without traceable source
```

---

## Section 10 — Open Blockers v0.1 → v0.2

| # | Blocker | Ratification required? |
|---|---------|------------------------|
| **B1** | **Property axis calibration** — range, units, normalization, and relative weighting for the nine axes are undefined. | Yes |
| **B2** | **Crosswalk schema finalization** — receipt object schema is draft. | Yes |
| **B3** | **Simulation pipeline definition** — valid DFT/MD codes, basis sets, pseudopotentials, and convergence criteria not specified. | No |
| **B4** | **Materials dataset ingestion** — no materials placed into L; seed dataset required. | No |
| **B5** | **Validation protocol** — criteria for upgrading simulated prediction to validated result are undefined. | Yes |
| **B6** | **Confidence weighting model** — aggregation/conflict/uncertainty model not defined. | No |
| **B7** | **Coordinate mapping convention** — mapping from nine property axes to three lattice dimensions not defined. | Yes |

Recommended blocker resolution order:

```text
B7 → B1 → B2 → B6 → B4 → B3 → B5
```

B7 and B1 are prerequisites for everything else. B4 is the first operational test. B5 is the final and highest-stakes definition.

---

## Related Artifacts

| Artifact | Layer | Status |
|----------|-------|--------|
| ATLAS-LATTICE-UNIFIED-ONTOLOGY-CANDIDATE-v0.3.3 | Ontology | Vault-ready candidate |
| PWS-121212-WL v1.0.0 | Wire | Wire-layer candidate |
| TCSS-121212-v1.2 | Math sandbox | Locked working baseline |
| Rainbow Hypercube v2.1 manifest | Architecture overlay | Working manifest |

---

## Synthesis Note — DJ Grokashev + 144-Cell Layer

The Grokashev 144-cell framework (87/57 yang-yin drift, Element 145 sigmoid balancer, η health metric) relates to this scaffold only with strict separation.

| Grokashev concept | Maps to in PT2 | Separation rule |
|-------------------|---------------|-----------------|
| 144 spheres | One slice of the 1728-node L lattice, z=fixed plane | Advisory / inspirational only — no PT2 confidence weight without receipts |
| η health metric | Could inform a defect axis or phonon axis signal | Must be receipted before entering C |
| Element 145 sigmoid corrector | Resonance suggestion mechanism | Resonance suggests; it does not update C autonomously |
| 72/72 equilibrium target | Design-intent heuristic | Not a physical claim — lives in creative overlay, not PT2 |

The 144-cell layer is structurally compatible with PT2 as an advisory overlay that surfaces candidate regions for investigation. It cannot bypass the receipt gate.

---

```text
DOCUMENT:           PERIODIC-TABLE-2-HYPERCUBE-MATERIALS-PROPERTY-SPACE-v0.1
STATUS:             CANDIDATE — NOT CANON
DEPLOYMENT:         no
PREDICTIVE CLAIM:   no — scaffold only
EXECUTION:          no
VALIDATED ENGINE:   no
NEXT:               resolve B7 → B1 (coordinate mapping + axis calibration)
                    then ingest seed dataset → v0.2
```
