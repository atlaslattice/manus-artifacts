STATUS: ARCHIVE PUBLIC CANDIDATE | CANON: no | DEPLOYMENT: no | AUTHORITY: none | PROOF: no | PUBLIC_RELEASE: candidate

Recovered historical Manus artifact. Current review decisions: [build/review/EVIDENCE_APPENDIX.md](https://github.com/atlaslattice/manus-artifacts/blob/master/public_candidate_bundle_0001/nodes/dongjiakou_node_001/build/review/EVIDENCE_APPENDIX.md).

# Lattice Scaling Plan — From Node-001 to a National Lattice

**Document ID:** ATLAS-LATTICE-SCALING-PLAN-v0.1
**Status:** PUBLIC_CANDIDATE_NON_CANON
**Date:** 2026-10-06
**Repo:** `atlaslattice/manus-artifacts`
**Reference head:** `4756036f9c428fa3aa1d4cea552ae03367523fb5`

---

## 1. The goal as stated

> Apply the Atlas Lattice work for a complete local build in the Dongjiakou
> locality, with DeepSeek statistics on current resource and production rates, as
> **Node 1 of a possible 167-node lattice** integrating all Chinese localities
> with desalination plants.

This document sets out how Node-001 becomes the reference implementation for that
lattice, what has to be true at each stage, and — importantly — what must **not**
be claimed at any stage.

---

## 2. The honest position on "167"

### 2.1 Decision — the node unit is the locality

**Resolved 2026-10-06 (human root).** The node unit has been **expanded from the
desalination project to the locality the project exists in**. A node is a
locality, not a single plant. Where a locality hosts more than one desalination
plant or project, those assets sit **inside one node** and are partitioned within
its component ledgers — they are not separate nodes.

This matters because it changes the boundary problem. The single-credit rule must
now hold *within* a locality across its several plants, before it can hold
*across* localities. A locality node with two plants may not credit the same
regional generation, watershed or feedstock twice internally.

### 2.2 The honest position on the count

The number 167 is a **working target**, not an established fact. At the time of
writing, no sourced register of Chinese localities hosting seawater desalination
capacity has been assembled inside this repository. Until that register exists
with per-locality provenance, the following are all UNKNOWN:

- the actual number of qualifying localities
- whether the qualifying count is above or below 167
- which localities qualify, and on what criterion
- the operational versus planned split
- the aggregate capacity

**A target is not a count.** The register build (`DAR-L01`) is in progress and
must be sourced, evidence-classed and honest about shortfall or overage. If the
sourced count is 40, the plan scales to 40. If it is 210, the plan scales to 210.
The lattice is defined by its contract, not by a number chosen in advance.

The national figure of 167 reported in the reviewed sources is a count of
desalination **engineering projects**, not localities. Because the node unit is
now the locality, the project count and the node count are **not the same
number**, and the node count is expected to be lower. Both must be reported, and
neither may be substituted for the other.

> Padding a register to reach a target would destroy the only thing that makes
> the lattice worth building.

---

## 3. What scales and what does not

This distinction is the core of the plan.

| Element | Scales? | Notes |
| --- | --- | --- |
| Node template and component set | **Yes** | Copy the contract |
| Evidence-class vocabulary | **Yes** | Closed vocabulary, identical at every node |
| Run set and equations | **Yes** | Same deterministic structure, node-specific inputs |
| Gate set G01–G16 | **Yes** | Inherited unmodified; may be added to, never weakened |
| Credit-ledger discipline | **Yes** | Same single-credit rule, extended lattice-wide |
| Reproduction harness | **Yes** | Same harness, per-node manifest |
| Failure ledger | **Yes** | Per node, append-only |
| Node parameters | **No** | Every node has its own measured inputs |
| Node evidence | **No** | Never transferable between nodes |
| Node veto outcomes | **No** | A node's ecological veto cannot be inherited or offset |
| Aggregate claims | **No** | Never attributable back to a node |

**The architecture is portable. The evidence is not.**

---

## 4. Staged scaling

### Stage 0 — Reference implementation (current)

Node-001 is built out as a reproducible pilot package: pure-function models, 155
reproduced derived values, 16 gates with negative controls, source manifest with
SHA-256 digests, credit ledger, unknown ledger, failure ledger, commissioning
specification and dashboard specification.

**Exit criterion:** every derived number reproduces; every gate has a negative
control; no unexplained divergence.

**Status:** complete for Node-001, pending human review.

### Stage 1 — Register and schema lock

Build the sourced candidate node register (`DAR-L01`), then freeze the node
schema and the instantiation checklist.

**Exit criteria:**
- every register row carries a source URL and an evidence class
- operational, under-construction and planned are distinguished
- the count is reported honestly against the 167 target, with reconciliation
- the node schema is versioned and locked

**Status:** register research in progress.

### Stage 2 — Common data schema for node statistics

Define the per-node resource and production statistic schema (`DAR-L02`) so nodes
are comparable at all. This is where the DeepSeek statistics lane belongs: a
primary local advisory family for Chinese technical-language document
interpretation, maintenance-record synthesis, telemetry summarisation and
cross-domain synthesis.

**Critical constraint.** DeepSeek produces **advisory synthesis and retrieval**.
It does not produce evidence. A statistic extracted by a model is a
**PROPOSED**-class extraction until a human confirms it against the primary
document. Model consensus is not evidence, and the routing policy already
requires that a model recommendation pass a deterministic validator and an
operator before any physical consequence.

**Exit criteria:**
- schema versioned and locked
- extraction provenance recorded per statistic
- a human-verification step defined for every model-extracted value

### Stage 3 — Second and third nodes

Instantiate two or three additional nodes end to end, chosen to stress the
contract rather than to look good: ideally one very large established plant, one
small or newly built plant, and one whose evidence quality is poor.

**Purpose:** find where the template breaks before instantiating dozens.

**Exit criteria:**
- each node reproduces its own derived numbers
- cross-boundary import/export declarations complete
- at least one non-comparability declaration made explicitly
- template defects fed back into the template version

### Stage 4 — Batch instantiation

Instantiate the remaining sourced nodes under the frozen schema, in batches, with
the same harness.

**Exit criteria:**
- every node passes its own gate suite
- lattice single-credit rule verified across node boundaries
- aggregate reporting clearly separated from node reporting

### Stage 5 — Lattice reporting

Publish a lattice-level view that is explicit about coverage, evidence quality and
non-comparability.

**Exit criteria:**
- no aggregate is attributable back to a single node
- every aggregate states its coverage and its exclusions
- veto outcomes are reported per node and never netted off

---

## 5. Lattice-level invariants

These extend the node invariants to the whole lattice. They are additions to
G01–G16, not replacements.

| ID | Invariant |
| --- | --- |
| **L01** | One physical resource receives at most one primary credit across the entire lattice |
| **L02** | A shared resource — generation, corridor, watershed, feedstock — must be explicitly partitioned before either node claims it |
| **L03** | An aggregate may never be attributed back to a single node |
| **L04** | An aggregate may never backfill a node-level UNKNOWN |
| **L05** | A node-level veto is never diluted by lattice-level performance |
| **L06** | Nodes are comparable only under a shared boundary definition and a common schema; non-comparability must be declared |
| **L07** | A registered candidate node is not an assigned coordinate |
| **L08** | Model-extracted statistics are PROPOSED class until human-verified against the primary document |
| **L09** | Coverage and exclusions must be stated with every lattice aggregate |
| **L10** | No lattice-level figure may be used to justify a physical action at any node |

---

## 6. The DeepSeek statistics lane

The stated goal includes "DeepSeek statistics on current resource and production
rates." The role this package assigns is precise, and narrower than it might first
appear.

| DeepSeek may | DeepSeek may not |
| --- | --- |
| Read Chinese technical and regulatory documents | Establish a measured value |
| Extract candidate statistics with provenance | Publish a statistic without human verification |
| Summarise telemetry and maintenance records | Write to any control system |
| Synthesise across domains | Override a deterministic validator |
| Explain a fault or a recommendation to an operator | Act as sole authority on any claim |

Every model-extracted statistic enters as **PROPOSED** and is promoted only when a
human confirms it against the primary source. The evidence class of a value is
determined by the underlying receipt, never by which model read it.

---

## 7. What must not happen at scale

- Reaching 167 by padding the register.
- Promoting a regional or provincial total to a node-level quantity.
- Copying one node's measured values into another node as a starting assumption.
- Netted lattice performance used to offset a failed node veto.
- Model-extracted statistics entering as MEASURED.
- A coordinate assigned before an explicit taxonomy assignment exists.
- Any node, at any stage, authorising construction, procurement or a change to an
  operating plant.

---

## 8. Immediate next actions

| # | Action | Owner | Depends on |
| --- | --- | --- | --- |
| 1 | Complete the sourced candidate node register | S6 research | — |
| 2 | Lock the node schema after register review | S6 / human root | 1 |
| 3 | Define the per-node statistics schema | S6 / DeepSeek lane | 2 |
| 4 | Obtain the six minimum viable Node-001 receipts | Plant / commercial | — |
| 5 | Instantiate Node-002 as a contract stress test | S6 | 2 |
| 6 | Verify the lattice single-credit rule across two nodes | S6 | 5 |

Additionally, the **net-positive data centre pathway** is specified in
`NET_POSITIVE_PATHWAY.md`. It defines the measurement set (M1–M25), the ORCS
promotion discipline that a net-positive claim must pass, and the falsification
conditions. Net-positive is a node-level claim and may never be produced by
netting a surplus node against a deficit node.

---

## 9. Keeper

> The lattice is source code. The gift is open. The gate remains held.

> Node-001 is not the first of 167 because 167 was chosen. It is the first because
> it is the one that is documented.
