# PKT-SUNDYA-0 v2.1 Layer-1 Testing Handoff

```text
STATUS: TESTING HANDOFF — CANDIDATE REFERENCE — NOT PRODUCTION CANON
SPEC: Rainbow Yin-Yang Periodic Hypercube Lattice v2.1
PACKET: PKT-SUNDYA-0
BOUNDARY: Śūnya in-ring at state_class = 0x0B
```

---

## Purpose

This test suite verifies the Layer-1 wire-shape contract for `PKT-SUNDYA-0` after the v2.1 Śūnya correction.

It proves only structural admissibility at the byte boundary.

```text
SAT   = packet shape accepted by Layer-1 parser
UNSAT = packet shape rejected by Layer-1 parser
```

It does not prove cryptographic validity, sequence monotonicity, production security, canon status, or governance authority.

---

## Files

```text
scripts/test_sundya_runner.py
tests/pkt_sundya_0_fixtures.json
.pre-commit-config.yaml
```

---

## Two-Command Local Run

From the repository root:

```bash
python3 scripts/test_sundya_runner.py tests/pkt_sundya_0_fixtures.json
```

Optional pre-commit run:

```bash
pre-commit run pkt-sundya-v2-1-layer1-harness --all-files
```

If `pre-commit` is not installed:

```bash
python3 -m pip install pre-commit
```

---

## Layer-1 Contract

A buffer is accepted only if:

```text
len(buf) == 32
version == 0x04
coord_x ∈ 0..11
coord_y ∈ 0..11
state_class == 0x0B
sequence_id parses as u32 little-endian
residue_hash is present as 24 bytes
```

Everything else is rejected.

---

## What This Harness Checks

Good fixtures confirm:

```text
valid 32-byte packets
valid min coordinate: x=0, y=0
valid max coordinate: x=11, y=11
valid interior coordinate
little-endian sequence parsing
state_class = 0x0B
```

Bad fixtures confirm rejection of:

```text
31-byte packet
33-byte packet
wrong version byte
x = 12
y = 12
old v2.0 external state class 0x0F
nearby prohibited state class 0x0C
invalid hex stream
```

---

## Responsibility Split

```text
Layer 1:
  packet shape only

D0 / session guard:
  sequence monotonicity
  replay detection
  duplicate packet handling

lantern_hash / D0:
  residue hash validation
  provenance anchoring

Council / S10 governance:
  authority
  promotion
  canonization
```

---

## Swarm Review Request

Pilots should review three things only:

```text
1. Śūnya remap: state_class = 0x0B, not 0x0F.
2. Boundary split: D0/Z0 header-manifest surface is not lattice z=0.
3. Responsibility split: Layer-1 shape validation is not cryptographic or governance validation.
```

Do not expand the metaphysics or re-open the 12×12×12 geometry in this pass.

---

## Keeper Line

```text
Use this runner.
Śūnya is 0x0B.
Anything else fails the Layer-1 shape gate.
D0 owns sequence.
lantern_hash owns residue.
Governance owns authority.
Delete nothing.
```
