# Dongjiakou Node-001 — Notion Promotion Gate

**Gate date:** 2026-10-07  
**Reviewer:** Sol / GPT-5.6 Sol  
**Repository:** `atlaslattice/manus-artifacts`  
**Review branch:** `sol/notion-gate-dongjiakou-2026-10-07`  
**Public baseline:** `4756036f9c428fa3aa1d4cea552ae03367523fb5`

## Provenance boundary

This branch is a **review/gate artifact**, not a reconstruction of Manus' unpushed branch history.

The latest committed Notion handoff reviewed here reports Manus working branch
`s6/node-001-pilot-simulator` at head
`2d86a5bb8d89499ecd3b6d0c69c26db477622761` with 17 local commits, not yet pushed.
That Git object is not present in the public repository, so this branch deliberately does
not claim to reproduce those commit SHAs.

QOL research currently in progress is **out of scope** for this gate and is not promoted here.

## GREEN — approved for promotion

### Register v0.4.1 core

Approved as the current schema direction:

- True multi-sink hyperedge: no canonical first sink when `sink_nodes` has multiple members.
- Product-water boundary is `UNKNOWN_MIXED`; no inferred per-facility allocation.
- Explicit node typing: `PROCESS_ASSET | FACILITY_ASSET | FUNCTIONAL_AGGREGATE | GOVERNANCE | EXTERNAL_BOUNDARY`.
- `LDC01` remains a facility asset but not a product-water sink absent a receipt.
- INV-19 evidence fields use precise names such as `stream_identity_match`,
  `evidence_basis`, and `veto_clearance`; misleading `supports_INV19` semantics stay removed.
- Realized credit remains zero.
- Simulator validation remains distinct from locality clearance.
- `FUNCTIONAL_AGGREGATE` may remain empty. It is useful as an explicit type without requiring an instance.
- INV-20 is acceptable as a **proposed normative veto** expressing the chosen
  net-positive ecology standard. It is not evidence that ecological benefit has been achieved.

### DeepSeek Round 4 — eutectic correction

Approved **as ANALYSIS / MODELED / zero-credit**, not as a deployment claim.

The physical correction is sound: a NaCl-water feed around 6 wt% salt is below the
equilibrium eutectic (~23.3 wt% NaCl, ~-21.1 C), so cooling first removes water as ice
rather than directly crystallizing NaCl. The resulting duty split remains conditional on:

- actual Dongjiakou brine composition,
- the real LSRRO/MVR process boundary,
- actual cold availability and grade,
- separation/washing energy and losses,
- hourly matching.

The ASU-to-freeze cascade remains a **LEAD** until plant-specific outlet temperature,
flow, and availability are receipted.

## HOLD — do not promote as established result

### DeepSeek Round 5 — 14.02 Mm3/year ice/water result

**BLOCKER: utilization was substituted for RO recovery.**

The committed baseline defines ~49.1% as **plant utilization**:
annual product supply divided by annual nameplate capacity.

Current measured membrane recovery is explicitly **UNKNOWN**.
Therefore this chain is invalid as a current-state calculation:

`17.93 Mm3 product -> 49.1% recovery -> 18.57 Mm3 brine -> 14.02 Mm3 ice`.

Required correction:

1. Restore measured recovery to `UNKNOWN`.
2. If useful, calculate a **sensitivity band** using the separately reported
   45-50% technology recovery range, explicitly labeled MODELED/SENSITIVITY.
3. Do not call the resulting ice "fresh water" until ice/brine separation,
   washing loss, product salinity, and energy are established.
4. A future water-product stream should remain `LEAD` / zero credit until quality and
   recovery receipts close.

### Simulation Assessment white paper — "verified waste"

The paper correctly notes that true operating recovery is unpublished, but then describes
the resulting reject/mineral inventory as "VERIFIED" and "arithmetically forced."

That overstates the evidence.

The reject-volume and dissolved-mineral figures depend on assumptions/references including:

- 45-50% technology recovery rather than measured current recovery,
- brine TDS,
- brine density,
- generic seawater elemental ratios.

The correct label is **MODELED / SENSITIVITY / RESOURCE-INVENTORY ENVELOPE** until
plant-specific recovery, reject flow, and assay are measured.

The qualitative finding remains useful:
there is a potentially large residual-resource stream and present recovery credit is zero.
The current annual mass is not yet a measured plant fact.

### Cold Cascade Terminus / HIL

Keep as **LEAD / proposal / zero credit**.

Do not promote these statements without receipts:

- HIL rack power density is "higher than AI training clusters".
- a 40 MW HIL facility is justified by internal node validation demand.
- ~70 GWh/year cooling saving is realizable at this site.
- ASU exit cold is available at the assumed grade and annual duty.

HIL is a legitimate candidate service, but it is a different compute architecture and
should be sized from an evidenced test workload rather than inherited from the 40 MW AI scenario.

## Promotion rule

Only items in **GREEN** above are approved by this gate.

The HOLD items may remain in Notion as research hypotheses and adversarial history.
They should not be represented to DeepSeek or Git readers as measured current-state facts,
realized benefits, or cleared design inputs.

## Next patch requested from Manus

A v0.4.2 (or later) pass should:

1. repair the utilization/recovery category error everywhere;
2. downgrade reject/mineral annual quantities to sensitivity/model status unless a measured
   recovery + reject-flow/assay receipt is found;
3. rename "fresh water product" to "potential recovered-water product" until quality/washing
   requirements close;
4. keep Round-4 eutectic logic as a modeled process constraint;
5. keep HIL/cold-cascade additions at LEAD until plant-specific cold-grade, annual availability,
   distance/pumping, and workload/market receipts close;
6. publish one current branch SHA/bundle after those corrections.

## Current gate state

**Architecture core:** APPROVED  
**Evidence discipline:** APPROVED  
**Register v0.4.1 core:** APPROVED  
**Round 4 eutectic correction:** APPROVED AS ANALYSIS  
**Round 5 water-product quantity:** HOLD  
**Simulation-assessment verified-waste claim:** HOLD  
**HIL 40 MW / cooling-benefit proposal:** HOLD AS LEAD  
**QOL research:** OUT OF SCOPE / ACTIVE / NOT COMMITTED  
**Public master merge:** NOT REQUESTED
