# Doctrine and lattice | Lattice Scaling Plan — From Node-001 to a National Lattice

> Notion page ID: `3f20c1de-73d9-8193-ab03-fb0a588789e8`
>
> Live page: https://app.notion.com/p/3f20c1de73d98193ab03fb0a588789e8?pvs=204
>
> Last edited: 2026-10-08T02:23:05.246Z
>
> Verification state: unverified

*Source: **`build/lattice/LATTICE_SCALING_PLAN.md`* — full artifact, dumped for review.
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
**Resolved 2026-10-06 (human root).** The node unit has been expanded from the
desalination project to the locality the project exists in. A node is a
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
now the locality, the project count and the node count are not the same
number, and the node count is expected to be lower. Both must be reported, and
neither may be substituted for the other.
> Padding a register to reach a target would destroy the only thing that makes
> the lattice worth building.
---
## 3. What scales and what does not
This distinction is the core of the plan.
<table>
<tr>
<td>Element</td>
<td>Scales?</td>
<td>Notes</td>
</tr>
</table>
<table fit-page-width="true" header-row="true">
<tr>
<td>---</td>
<td>---</td>
<td>---</td>
</tr>
<tr>
<td>Evidence-class vocabulary</td>
<td>Yes</td>
<td>Closed vocabulary, identical at every node</td>
</tr>
<tr>
<td>Run set and equations</td>
<td>Yes</td>
<td>Same deterministic structure, node-specific inputs</td>
</tr>
<tr>
<td>Gate set G01–G16</td>
<td>Yes</td>
<td>Inherited unmodified; may be added to, never weakened</td>
</tr>
<tr>
<td>Credit-ledger discipline</td>
<td>Yes</td>
<td>Same single-credit rule, extended lattice-wide</td>
</tr>
<tr>
<td>Reproduction harness</td>
<td>Yes</td>
<td>Same harness, per-node manifest</td>
</tr>
<tr>
<td>Failure ledger</td>
<td>Yes</td>
<td>Per node, append-only</td>
</tr>
<tr>
<td>Node parameters</td>
<td>No</td>
<td>Every node has its own measured inputs</td>
</tr>
<tr>
<td>Node evidence</td>
<td>No</td>
<td>Never transferable between nodes</td>
</tr>
<tr>
<td>Node veto outcomes</td>
<td>No</td>
<td>A node's ecological veto cannot be inherited or offset</td>
</tr>
<tr>
<td>Aggregate claims</td>
<td>No</td>
<td>Never attributable back to a node</td>
</tr>
</table>
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
<table>
<tr>
<td>ID</td>
<td>Invariant</td>
</tr>
</table>
<table fit-page-width="true" header-row="true">
<tr>
<td>---</td>
<td>---</td>
</tr>
<tr>
<td>L02</td>
<td>A shared resource — generation, corridor, watershed, feedstock — must be explicitly partitioned before either node claims it</td>
</tr>
<tr>
<td>L03</td>
<td>An aggregate may never be attributed back to a single node</td>
</tr>
<tr>
<td>L04</td>
<td>An aggregate may never backfill a node-level UNKNOWN</td>
</tr>
<tr>
<td>L05</td>
<td>A node-level veto is never diluted by lattice-level performance</td>
</tr>
<tr>
<td>L06</td>
<td>Nodes are comparable only under a shared boundary definition and a common schema; non-comparability must be declared</td>
</tr>
<tr>
<td>L07</td>
<td>A registered candidate node is not an assigned coordinate</td>
</tr>
<tr>
<td>L08</td>
<td>Model-extracted statistics are PROPOSED class until human-verified against the primary document</td>
</tr>
<tr>
<td>L09</td>
<td>Coverage and exclusions must be stated with every lattice aggregate</td>
</tr>
<tr>
<td>L10</td>
<td>No lattice-level figure may be used to justify a physical action at any node</td>
</tr>
</table>
---
## 6. The DeepSeek statistics lane
The stated goal includes "DeepSeek statistics on current resource and production
rates." The role this package assigns is precise, and narrower than it might first
appear.
<table>
<tr>
<td>DeepSeek may</td>
<td>DeepSeek may not</td>
</tr>
</table>
<table fit-page-width="true" header-row="true">
<tr>
<td>---</td>
<td>---</td>
</tr>
<tr>
<td>Extract candidate statistics with provenance</td>
<td>Publish a statistic without human verification</td>
</tr>
<tr>
<td>Summarise telemetry and maintenance records</td>
<td>Write to any control system</td>
</tr>
<tr>
<td>Synthesise across domains</td>
<td>Override a deterministic validator</td>
</tr>
<tr>
<td>Explain a fault or a recommendation to an operator</td>
<td>Act as sole authority on any claim</td>
</tr>
</table>
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
<table>
<tr>
<td>#</td>
<td>Action</td>
<td>Owner</td>
<td>Depends on</td>
</tr>
</table>
<table fit-page-width="true" header-row="true">
<tr>
<td>---</td>
<td>---</td>
<td>---</td>
<td>---</td>
</tr>
<tr>
<td>2</td>
<td>Lock the node schema after register review</td>
<td>S6 / human root</td>
<td>1</td>
</tr>
<tr>
<td>3</td>
<td>Define the per-node statistics schema</td>
<td>S6 / DeepSeek lane</td>
<td>2</td>
</tr>
<tr>
<td>4</td>
<td>Obtain the six minimum viable Node-001 receipts</td>
<td>Plant / commercial</td>
<td>—</td>
</tr>
<tr>
<td>5</td>
<td>Instantiate Node-002 as a contract stress test</td>
<td>S6</td>
<td>2</td>
</tr>
<tr>
<td>6</td>
<td>Verify the lattice single-credit rule across two nodes</td>
<td>S6</td>
<td>5</td>
</tr>
</table>
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
## Long-horizon coverage correction — beyond the desalination cohort
The desalination-node cohort is a **deployment/research cohort**, not the final ontology of the lattice.
Long-horizon scaling follows population/locality metabolism rather than agricultural or desalination siting alone. Coastal desalination nodes, inland cities, agricultural basins, industrial districts, mining regions, islands and dense urban regions are all valid locality-node classes with different module inheritance.
Agricultural hinterland improves local closure but is not required. Controlled-environment agriculture, peri-urban production and inter-node exchange provide alternative food/nutrient sinks. The eventual target is therefore **broad locality coverage wherever populations and material flows exist**, with node-specific modules and measured exchange fractions.
> **Cohorts prove modules. Localities define the lattice.**
