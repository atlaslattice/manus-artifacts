# LATTICE_12x12x12_WIRE_INDEXING_SPEC_v2.1

**Strict Wire-Level Specification**  
**Status:** CANDIDATE — NOT CANON — NON-DEPLOYABLE  
**Runtime Status:** Not production code  
**Gate Alignment:** Matches current tested gate (`test_sundya_runner.py` + fixtures + pre-commit)  
**Source:** Corrected two-artifact split from user-provided review packet, 2026-05-21

---

## 1. Lattice Geometry (Wire Definition)

The operational structure is a **finite 3D 12×12×12 cubic lattice** with **0-based wire indexing**:

$$
\mathcal{L} = \{0,1,\dots,11\}^3, \qquad |\mathcal{L}| = 1{,}728.
$$

Coordinate triple (wire):

$$
\mathbf{c} = (x, y, z) \in \{0,\dots,11\}^3
$$

- $x$: House index (wire)
- $y$: Sphere / Layer index (wire)
- $z$: Conservation Class index (wire)

**Flat addressing** (0-based, O(1)):

$$
\text{addr}(\mathbf{c}) = x + 12y + 144z.
$$

Maximum address: 1,727.

**Namespace caveat:**

```text
D0 / Z0 manifest index is external to the lattice coordinate space and must not be confused with lattice z = 0, which remains a valid wire coordinate.
```

---

## 2. Z-Axis: Closed Set of 12 Metadata Tags (Wire)

| Z | Hex | Semantic Role | Type |
|---|---|---|---|
| 0–10 | 0x00–0x0A | Active conservation classes | Typed state |
| **11** | **0x0B** | **Śūnya** (Typed Absence / Void) | Absence marker |

**Śūnya definition** (locked):

$$
z_{\text{Śūnya}} := 0x0B.
$$

Any packet with `state_class == 0x0C` or other unmapped values is rejected at Layer-1.

---

## 3. Śūnya Wire Primitive — PktSundya0 (Fixed 32-byte)

```c
typedef struct {
    uint8_t  version;           // Must be 0x04
    uint8_t  coord_x;           // 0..11
    uint8_t  coord_y;           // 0..11
    uint8_t  state_class;       // Must be 0x0B for Śūnya
    uint32_t sequence_id;       // Little-endian
    uint8_t  residue_hash[24];  // Truncated SHA-256
} PktSundya0_t;
```

```c
_Static_assert(sizeof(PktSundya0_t) == 32, "Layout violation");
```

---

## 4. Layer-1 Shape Validation Rules (Pre-Commit Enforced)

- Packet length **exactly** 32 bytes
- `version == 0x04`
- `coord_x ∈ [0,11]` and `coord_y ∈ [0,11]`
- `state_class == 0x0B` when used as Śūnya token
- Immediate rejection on any violation, including old `0x0F` or `0x0C`

Deferred to D0 / lantern_hash layer:

- Sequence monotonicity
- Full cryptographic hash validation
- Z3 / QF_LIA solver integration

---

## 5. Human Display Layer (Optional, Non-Wire)

```text
Display coordinate = wire coordinate + 1
```

This maps:

```text
wire 0..11 → display 1..12
```

This is a view transformation only. All wire protocols and gates use 0-based indexing.

---

## 6. Current Alignment

```text
Wire coordinates: 0..11
Human display coordinates: 1..12
Śūnya wire value: 0x0B
0x0C: rejected unless future version explicitly changes the protocol
```

---

## 7. Keeper Line

```text
Display can be 1-based.
Wire must match the gate.
Śūnya stays 0x0B unless a new version intentionally breaks compatibility.
```
