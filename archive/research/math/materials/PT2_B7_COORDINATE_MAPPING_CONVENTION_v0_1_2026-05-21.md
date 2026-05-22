---
artifact_id: PT2-B7-COORDINATE-MAPPING-CONVENTION-v0.1
title: "Periodic Table 2 — B7 Coordinate Mapping Convention"
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
role: coordinate_mapping_scaffold_only
parent_artifact: PERIODIC-TABLE-2-HYPERCUBE-MATERIALS-PROPERTY-SPACE-v0.1
receipt_status: scaffold_initialized_2026-05-21
mutation_rule: >
  No coordinate claim without receipts.
  No axis calibration without review.
  No predictive claim without simulation or lab receipt.
  No canon promotion without human-root ratification.
---

# Periodic Table 2 — B7 Coordinate Mapping Convention
## Candidate Scaffold v0.1

```text
STATUS:             CANDIDATE — NOT CANON
DEPLOYMENT:         no
PREDICTIVE CLAIM:   no
EXECUTION:          no
ROLE:               coordinate mapping scaffold only
PARENT:             PERIODIC-TABLE-2-HYPERCUBE-MATERIALS-PROPERTY-SPACE-v0.1
BLOCKER RESOLVED:   no — this is the first B7 scaffold, not final resolution
NEXT:               B1 axis calibration after mapping convention review
```

---

## 1. Purpose

This artifact begins blocker B7 from the Periodic Table 2 scaffold:

```text
B7 — Coordinate mapping convention
The mapping from the nine property axes to the three lattice dimensions (x, y, z) is not defined.
A dimensionality reduction strategy or expert-assigned convention is required.
```

This file proposes a candidate convention for discussion. It does not assign real materials to cells, does not calculate confidence weights, and does not validate any property claim.

---

## 2. Boundary Rules

```text
This document IS:
  - a coordinate mapping scaffold
  - a proposed convention for organizing property axes
  - a review target for PT2 v0.2 preparation

This document IS NOT:
  - a physics engine
  - a prediction engine
  - a validated dimensionality reduction model
  - a materials dataset
  - an authority or canon artifact
```

Must-not-infer:

```text
Coordinate proximity ≠ physical equivalence.
Coordinate assignment ≠ validated property claim.
Mapping convention ≠ axis calibration.
Semantic placement ≠ confidence weight.
```

---

## 3. Design Constraint

The PT2 scaffold defines nine property axes:

```text
Physical
Quantum
Structural
Thermal
Electronic
Magnetic
Phonon
Defect
Synthesis
```

The lattice has three coordinate dimensions:

```text
x ∈ {0,...,11}
y ∈ {0,...,11}
z ∈ {0,...,11}
```

Therefore B7 requires a compression from:

```text
P_9 → L_3
```

where:

```text
P_9 = nine-dimensional property space
L_3 = three-dimensional 12×12×12 coordinate lattice
```

This compression must remain reversible enough for audit:

```text
cell assignment must carry the property vector, mapping method, version, and receipt references.
```

---

## 4. Candidate Mapping Strategy

Use a **three-bundle property projection** rather than immediately forcing PCA/UMAP or a black-box embedding.

Candidate projection:

```text
x = composition / structure family axis
y = transport / field-response axis
z = stability / processability / defect axis
```

### 4.1 X Axis — Composition / Structure Family

Input property axes:

```text
Physical
Structural
Synthesis
```

Meaning:

```text
x groups materials by bulk/structural/fabrication family.
```

Representative contributors:

```text
mass density
hardness
elastic moduli
space group
coordination number
lattice parameter
synthesis route
stability window
precursor availability
```

### 4.2 Y Axis — Transport / Field Response

Input property axes:

```text
Quantum
Electronic
Magnetic
```

Meaning:

```text
y groups materials by electronic, magnetic, and quantum response profile.
```

Representative contributors:

```text
band gap
effective mass
spin-orbit coupling
Berry phase
electrical conductivity
carrier mobility
Seebeck coefficient
magnetic moment
Curie temperature
exchange coupling
```

### 4.3 Z Axis — Dynamics / Defect / Thermal Stability

Input property axes:

```text
Thermal
Phonon
Defect
```

Meaning:

```text
z groups materials by lattice dynamics, thermal behavior, and defect tolerance.
```

Representative contributors:

```text
thermal conductivity
Debye temperature
thermal expansion coefficient
phonon dispersion
phonon lifetime
Grüneisen parameter
defect formation energy
defect migration barrier
doping response
```

---

## 5. Formal Projection Skeleton

Let a material candidate have property vector:

```text
p(m) = (
  p_Physical,
  p_Quantum,
  p_Structural,
  p_Thermal,
  p_Electronic,
  p_Magnetic,
  p_Phonon,
  p_Defect,
  p_Synthesis
)
```

Define three bundle functions:

```text
X_bundle(m) = B_x(p_Physical, p_Structural, p_Synthesis)
Y_bundle(m) = B_y(p_Quantum, p_Electronic, p_Magnetic)
Z_bundle(m) = B_z(p_Thermal, p_Phonon, p_Defect)
```

Then the candidate coordinate is:

```text
coord(m) = (
  bucket_12(X_bundle(m)),
  bucket_12(Y_bundle(m)),
  bucket_12(Z_bundle(m))
)
```

Where:

```text
bucket_12: normalized score or category → {0,...,11}
```

Important:

```text
B_x, B_y, B_z, normalization rules, and bucket boundaries are not yet defined.
They are B1 axis-calibration work.
```

---

## 6. Mapping Receipt Requirement

Every coordinate assignment must carry:

```yaml
mapping_receipt:
  material_id: required
  material_formula: required_if_available
  source_dataset: required
  source_record_id: required
  property_vector_version: required
  mapping_method: required
  mapping_method_version: required
  axis_bundle_policy: required
  normalization_policy: required
  bucket_policy: required
  assigned_coordinate: required
  confidence_status: provisional
  reviewer: required
  timestamp: required
```

No coordinate assignment may be treated as meaningful without a mapping receipt.

---

## 7. Candidate Alternatives to Evaluate Later

This scaffold does not preclude other mapping methods.

Future alternatives:

```text
A. Expert-assigned taxonomy mapping
B. PCA projection after dataset ingestion
C. UMAP/t-SNE-style exploratory embedding
D. Graph clustering by property similarity
E. Hybrid expert + statistical mapping
```

Current recommendation:

```text
Start with expert-assigned bundle convention for explainability.
Do not use black-box embedding until receipts and calibration data exist.
```

---

## 8. B7 Acceptance Criteria

B7 is not fully resolved until the following are defined:

```text
1. Exact property axes included in each bundle.
2. Normalization policy for each property axis.
3. Weighting policy inside B_x, B_y, B_z.
4. bucket_12 boundary definitions.
5. Coordinate assignment receipt schema finalized.
6. At least one seed material dataset mapped as a dry run.
7. Error / uncertainty handling for missing property values.
```

This v0.1 artifact satisfies only item 1 at a candidate level.

---

## 9. Hand-Off to B1

After this convention is accepted for review, B1 must define:

```text
- units
- ranges
- normalization
- weighting
- missing-data policy
- bucket boundary policy
- uncertainty propagation
```

B1 is blocked unless B7 remains stable enough to calibrate.

---

## 10. Keeper Lines

```text
Map first.
Calibrate second.
Ingest third.
Predict never without receipts.
```

```text
The coordinate is a filing address, not a property claim.
```

```text
A cell assignment without receipt is just a guess in a nice box.
```

---

## 11. Current Status

```text
DOCUMENT:           PT2-B7-COORDINATE-MAPPING-CONVENTION-v0.1
STATUS:             CANDIDATE — NOT CANON
DEPLOYMENT:         no
PREDICTIVE CLAIM:   no
EXECUTION:          no
BLOCKER STATUS:     B7 opened, not fully resolved
NEXT:               review bundle convention → draft B1 axis calibration
```
