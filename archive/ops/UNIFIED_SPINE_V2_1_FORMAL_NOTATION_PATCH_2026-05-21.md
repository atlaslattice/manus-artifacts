# UNIFIED SPINE v2.1 — FORMAL NOTATION PATCH

```text
STATUS: CANDIDATE FORMAL NOTATION PATCH — NOT FINAL — NOT CANON — NOT DEPLOYABLE
DATE: 2026-05-21
PURPOSE: Clean formal notation before any further threshold or doctrine work
SOURCE: Dave / Archive Goblin verdict / Horizon Ledger response
```

---

## 1. Patch Target

This patch corrects sloppy notation in the synthesized unified spine v2.1.

The prior spine is useful, but it should not be labeled final until notation is tightened.

```text
Good spine.
Still not final.
Patch formal notation first.
Then do zero-denominator policy.
No doctrine touch yet.
```

---

## 2. Status Header

Use:

```yaml
status: candidate_unified_spine_v2_1
canon: false
deployment: false
wire: candidate
overlay: inspirational_non_executable
authority_status: none
```

Do not use:

```text
FINAL
RATIFIED
DEPLOYED
CANON
```

---

## 3. Responsibility-Set Separation

Replace informal layer inequality:

```text
W ≠ O ≠ D0 ≠ H ≠ G
```

with responsibility-set separation:

```text
Resp(W), Resp(O), Resp(D0), Resp(H), Resp(G)
```

are pairwise distinct responsibility sets:

```text
∀A,B ∈ {W,O,D0,H,G}, A ≠ B ⇒ Resp(A) ∩ Resp(B) = ∅ unless an explicit interface I_{A→B} is defined.
```

Where:

```text
W  = wire / packet-shape layer
O  = creative overlay / human-orientation layer
D0 = provenance + sequence lineage layer
H  = hash / residue-integrity layer
G  = governance / authority-ratification layer
```

Allowed relation:

```text
interface(I_{A→B}) must be explicitly defined before data, authority, or interpretation crosses layer boundaries.
```

Keeper:

```text
Separate responsibilities, not vibes.
```

---

## 4. Firewall Non-Implications

Replace chained non-implication:

```text
shape_valid(x) not⇒ provenance_valid(x) not⇒ residue_valid(x) not⇒ governance_authorized(x) not⇒ canon(x)
```

with separate non-implications:

```text
shape_valid(x) ⇏ provenance_valid(x)
```

```text
provenance_valid(x) ⇏ residue_valid(x)
```

```text
residue_valid(x) ⇏ governance_authorized(x)
```

```text
governance_authorized(x) ⇏ canon(x)
```

And direct wire firewall:

```text
accepted_by_wire(x) ⇒ shape_valid(x)
```

but:

```text
accepted_by_wire(x) ⇏ provenance_valid(x)
accepted_by_wire(x) ⇏ residue_valid(x)
accepted_by_wire(x) ⇏ governance_authorized(x)
accepted_by_wire(x) ⇏ canon(x)
```

Interpretation:

```text
Passing one layer never silently grants the next layer.
```

---

## 5. Śūnya Wording Patch

Replace:

```text
Signed-Zero Algebra (Brahmagupta → Śūnya collapse)
```

with:

```text
Śūnya / typed absence tag: z = 0x0B marks absence-class packets.
```

Reason:

```text
No “collapse” language in the wire layer.
Wire layer only recognizes typed packet fields, bounds, constants, and rejection paths.
```

Safe wire statement:

```text
PKT-SUNDYA-0 is accepted only when state_class = 0x0B.
```

Unsafe wire statement:

```text
The state collapses into Śūnya.
```

Use “collapse” only as orientation or overlay metaphor, not as wire-layer semantics.

---

## 6. Current Candidate Spine After Patch

```text
Resp(W), Resp(O), Resp(D0), Resp(H), Resp(G) are pairwise distinct responsibility sets.
Interfaces between them must be explicit.

accepted_by_wire(x) ⇒ shape_valid(x)

shape_valid(x) ⇏ provenance_valid(x)
provenance_valid(x) ⇏ residue_valid(x)
residue_valid(x) ⇏ governance_authorized(x)
governance_authorized(x) ⇏ canon(x)

PKT-SUNDYA-0 accepts state_class = 0x0B only.
D0/Z0 manifest remains external to lattice z=0.
Lattice z=0 remains a valid wire coordinate.
```

---

## 7. Keeper

```text
Good spine.
Still not final.
Patch notation before policy.
No collapse language in the wire layer.
No chained non-implication shortcuts.
No doctrine touch yet.
```