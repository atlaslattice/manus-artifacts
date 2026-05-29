# Lattice 12×12×12 Pure Wire Test Plan v2.1
**Candidate Validation Plan for Pure Wire Spec**

```text
STATUS: TEST PLAN / CANDIDATE
CANON: no
DEPLOYMENT: no
RUNTIME: no
AUTHORITY: none
WIRE: candidate
OVERLAY: excluded
DATE: 2026-05-22
RELATED_SPEC: archive/architecture/LATTICE_12x12x12_PURE_WIRE_SPEC_v2.1_CANDIDATE.md
```

---

## 0. Purpose

This document defines a reviewable test plan for the candidate pure wire lattice spec.

It does not implement runtime validation.  
It does not ratify the wire spec.  
It does not promote anything to canon.  
It does not import overlay semantics.

The purpose is to make the next engineering step obvious:

```text
spec → fixtures → tests → CI evidence → review → possible promotion later
```

---

## 1. Scope

This test plan covers only:

```text
wire coordinate bounds
flat address mapping
inverse address mapping
human display mapping
D₀ external namespace separation
Śūnya typed absence tag
PktSundya0 Layer-1 shape predicate
firewall non-implication assertions
```

This test plan excludes:

```text
Rainbow overlay
Yin-Yang overlay
chiral dissonance
metabolic yield
critical mirror axis
theta-kernel analogy
governance authorization
canon ratification
runtime deployment
```

---

## 2. Core Wire Assertions

### A1 — Coordinate domain

```text
VALID:   x,y,z ∈ {0,1,...,11}
INVALID: any coordinate < 0
INVALID: any coordinate > 11
```

### A2 — Address range

```text
VALID:   0 ≤ addr(c) ≤ 1727
INVALID: addr < 0
INVALID: addr > 1727
```

### A3 — Flat address equation

```math
addr(x,y,z) = x + 12y + 144z
```

### A4 — Inverse address equation

```math
x = addr \bmod 12
```

```math
y = \left\lfloor \frac{addr}{12} \right\rfloor \bmod 12
```

```math
z = \left\lfloor \frac{addr}{144} \right\rfloor
```

### A5 — Śūnya typed absence tag

```text
z = 0x0B is the candidate typed absence tag.
z = 0x0B does not imply canon, deployment, provenance, residue, or authority.
```

### A6 — D₀ namespace separation

```text
D₀ is external.
D₀ is not z = 0.
D₀ is not wire coordinate 0x00.
D₀ is not an in-lattice cell.
```

---

## 3. Candidate Fixture Table

| fixture_id | input | expected | notes |
|---|---:|---:|---|
| WIRE_ADDR_0000 | `(0,0,0)` | `0` | lowest valid lattice address |
| WIRE_ADDR_0001 | `(1,0,0)` | `1` | x increments by 1 |
| WIRE_ADDR_0012 | `(0,1,0)` | `12` | y increments by 12 |
| WIRE_ADDR_0144 | `(0,0,1)` | `144` | z increments by 144 |
| WIRE_ADDR_1727 | `(11,11,11)` | `1727` | highest valid lattice address |
| WIRE_INV_0000 | `0` | `(0,0,0)` | inverse lowest |
| WIRE_INV_1727 | `1727` | `(11,11,11)` | inverse highest |
| WIRE_INVALID_NEG_X | `(-1,0,0)` | invalid | coordinate below domain |
| WIRE_INVALID_X_12 | `(12,0,0)` | invalid | coordinate above domain |
| WIRE_INVALID_Z_12 | `(0,0,12)` | invalid | z above domain |
| WIRE_SUNYA_VALID | `(x=0,y=0,z=0x0B)` | valid z tag | shape still requires full packet predicate |
| WIRE_D0_EXTERNAL | `D₀` | external namespace | not in lattice address range |

---

## 4. PktSundya0 Shape Fixtures

### P0 — Valid minimal shape

```yaml
fixture_id: PKT_SUNDYA0_VALID_MINIMAL
buf_len: 32
version: 0x04
x: 0
 y: 0
z: 0x0B
expected:
  L1_valid: true
  provenance_effect: none
  residue_effect: none
  authority_effect: none
  canon_effect: none
```

### P1 — Invalid length

```yaml
fixture_id: PKT_SUNDYA0_INVALID_LENGTH_31
buf_len: 31
version: 0x04
x: 0
y: 0
z: 0x0B
expected:
  L1_valid: false
  allowed_action: reject_or_hold
```

### P2 — Invalid version

```yaml
fixture_id: PKT_SUNDYA0_INVALID_VERSION
buf_len: 32
version: 0x03
x: 0
y: 0
z: 0x0B
expected:
  L1_valid: false
  allowed_action: reject_or_hold
```

### P3 — Invalid z tag

```yaml
fixture_id: PKT_SUNDYA0_INVALID_Z_NOT_SUNYA
buf_len: 32
version: 0x04
x: 0
y: 0
z: 0x0A
expected:
  L1_valid: false
  allowed_action: reject_or_hold
```

### P4 — Invalid x coordinate

```yaml
fixture_id: PKT_SUNDYA0_INVALID_X_12
buf_len: 32
version: 0x04
x: 12
y: 0
z: 0x0B
expected:
  L1_valid: false
  allowed_action: reject_or_hold
```

---

## 5. Firewall Tests

The tests must explicitly assert that passing one layer does not promote downstream effects.

### F1 — Shape valid does not imply provenance valid

```yaml
input:
  L1_valid: true
expected:
  provenance_valid: not_inferred
  provenance_effect: none
```

### F2 — Provenance valid does not imply residue valid

```yaml
input:
  provenance_valid: true
expected:
  residue_valid: not_inferred
  residue_effect: none
```

### F3 — Residue valid does not imply governance authorized

```yaml
input:
  residue_valid: true
expected:
  governance_authorized: not_inferred
  authority_effect: none
```

### F4 — Governance authorized does not imply canon

```yaml
input:
  governance_authorized: true
expected:
  canon: not_inferred
  canon_effect: none_without_ratification
```

---

## 6. Suggested File Targets for Later Implementation

```text
archive/architecture/tests/lattice_wire_v2_1/test_address_mapping.py
archive/architecture/tests/lattice_wire_v2_1/test_pkt_sundya0_shape.py
archive/architecture/tests/lattice_wire_v2_1/test_firewall_nonimplications.py
archive/architecture/fixtures/lattice_wire_v2_1/valid_addresses.yaml
archive/architecture/fixtures/lattice_wire_v2_1/invalid_addresses.yaml
archive/architecture/fixtures/lattice_wire_v2_1/pkt_sundya0_shapes.yaml
```

These are proposed targets only. This document does not create runtime tests.

---

## 7. Acceptance Criteria

```text
[ ] Address mapping fixtures include lowest, highest, and basis vectors.
[ ] Inverse mapping fixtures round-trip correctly.
[ ] Invalid coordinate fixtures reject values outside 0..11.
[ ] D₀ remains external and never maps to z=0 or addr=0.
[ ] PktSundya0 shape predicate accepts only buf_len=32, v=0x04, x/y in range, z=0x0B.
[ ] Passing L1_valid never infers provenance, residue, authority, canon, or deployment.
[ ] Overlay terms do not appear in executable-facing fixtures.
```

---

## 8. Strongest Safe Claim

```text
This test plan defines reviewable candidate fixtures and assertions for the pure wire lattice spec, including address mapping, namespace separation, Śūnya packet shape, and firewall non-implications, without claiming canon, deployment, runtime implementation, or overlay authority.
```

---

## 9. Keeper Line

```text
Boring tests make wild systems survivable.
```

**End of Test Plan**
