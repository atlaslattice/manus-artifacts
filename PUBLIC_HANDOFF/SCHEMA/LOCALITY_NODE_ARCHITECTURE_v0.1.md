# Doctrine and lattice | Locality Node Architecture

> Notion page ID: `3f20c1de-73d9-81a7-8747-d469f2eea55a`
>
> Live page: https://app.notion.com/p/3f20c1de73d981a78747d469f2eea55a?pvs=204
>
> Last edited: 2026-10-08T02:23:03.153Z
>
> Verification state: unverified

*Source: **`build/lattice/LOCALITY_NODE_ARCHITECTURE.md`* — full artifact, dumped for review.
**Document ID:** ATLAS-LATTICE-LOCALITY-NODE-ARCHITECTURE-v0.1
**Status:** PUBLIC_CANDIDATE_NON_CANON — **NON-DEPLOYABLE**
**Date:** 2026-10-06
**Repo:** `atlaslattice/manus-artifacts`
**Reference head:** `4756036f9c428fa3aa1d4cea552ae03367523fb5`
---
## 1. The shift
Dongjiakou is not a desalination plant with extras bolted on. It is a
**locality-scale parent node**, and the intelligence lives in the metered
transfer edges between its subnodes — not in pretending the locality is one
giant plant.
```javascript
ATLAS LOCALITY NODE — DONGJIAKOU
|
|-- W01    Water / desalination
|-- C01    Compute + ORCS advisory lattice
|-- P01    Port / rail / logistics metabolism
|-- E01    Grid / wind / PV / storage
|-- E02    LNG cold-energy cascade / air separation
|-- R01    Resource extraction from brine
|-- BIO01  Organics / wastewater / nutrients
|-- M01    Additive manufacturing / 3D print
|-- MAT01  Steel slag / tires / construction materials
|-- CHEM01 Chemical-park process streams
|-- AGR01  Grain / food / controlled-environment agriculture
|-- CARB01 CO2 capture / utilization / mineralization
|-- ECO01  Coastal and ecological monitoring
`-- GOV01  Provenance / contracts / vetoes
```
**What this does not do:** it does not fold the whole locality into one positive
Node-001 number. W01 keeps its existing calculus, and Runs 0–3 do not become
obsolete. They become the audited history of one subnode.
> The locality is not a bigger plant. It is a metabolism.
---
## 2. Every arrow is a first-class ledger entry
A stream edge carries fifteen fields. An edge missing one is not a ledger entry.
<table>
<tr>
<td>Field</td>
<td>Question it answers</td>
</tr>
</table>
<table fit-page-width="true" header-row="true">
<tr>
<td>---</td>
<td>---</td>
</tr>
<tr>
<td>`source_subnode`</td>
<td>Where does it come from?</td>
</tr>
<tr>
<td>`sink_subnode`</td>
<td>Where does it go?</td>
</tr>
<tr>
<td>`material_or_energy`</td>
<td>What is it?</td>
</tr>
<tr>
<td>`quantity`</td>
<td>How much, with units and period?</td>
</tr>
<tr>
<td>`quality_composition`</td>
<td>What grade or chemistry?</td>
</tr>
<tr>
<td>`temperature_pressure`</td>
<td>At what conditions?</td>
</tr>
<tr>
<td>`time_profile`</td>
<td>When does it arrive, hour by hour?</td>
</tr>
<tr>
<td>`ownership`</td>
<td>Who owns it?</td>
</tr>
<tr>
<td>`contract_status`</td>
<td>Is there an agreement, and of what kind?</td>
</tr>
<tr>
<td>`evidence_class`</td>
<td>MEASURED / REPORTED / DERIVED / MODELED / PLANNED / … / UNKNOWN</td>
</tr>
<tr>
<td>`conversion_losses`</td>
<td>What is lost in the transfer?</td>
</tr>
<tr>
<td>`residual_fate`</td>
<td>Where does it end up when it is done?</td>
</tr>
<tr>
<td>`vetoes`</td>
<td>Which vetoes does this edge engage?</td>
</tr>
<tr>
<td>`primary_credit_owner`</td>
<td>Who may count it?</td>
</tr>
</table>
`time_profile` and `residual_fate` are the two fields most often missing in
conventional industrial symbiosis work, and they are the two that decide whether
a symbiosis is real. A heat stream that arrives when nothing needs heat is not a
heat stream.
---
## 3. The register, as built
`python3 simulator.py locality` emits the register. Current state:
<table>
<tr>
<td></td>
<td></td>
</tr>
</table>
<table fit-page-width="true" header-row="true">
<tr>
<td>---</td>
<td>---</td>
</tr>
<tr>
<td>Streams registered</td>
<td>22 — 6 physical, 16 opportunity</td>
</tr>
<tr>
<td>Streams realizing credit</td>
<td>0</td>
</tr>
<tr>
<td>Streams with incomplete schema</td>
<td>0</td>
</tr>
<tr>
<td>Locality clearance</td>
<td>`NOT_ESTABLISHED`</td>
</tr>
</table>
**Zero streams realize credit.** Every edge carries an `edge_state`, and only
`MEASURED_PHYSICAL` can realize credit. Nothing at Dongjiakou is measured yet.
### 3.1 Two graphs, not one
A graph that draws an operational steel-slag link and a hypothetical CO2
coupling the same way looks connected when it is not. At 50, 100 or 500
localities that difference decides whether the map is usable.
<table>
<tr>
<td>Graph</td>
<td>Contains</td>
<td>Count</td>
</tr>
</table>
<table fit-page-width="true" header-row="true">
<tr>
<td>---</td>
<td>---</td>
<td>---</td>
</tr>
<tr>
<td>Opportunity Graph</td>
<td>`CONTRACTED`, `UNDER_CONSTRUCTION`, `PLANNED`, `CANDIDATE_COUPLING`, `REFERENCE_ONLY`</td>
<td>16</td>
</tr>
</table>
### 3.2 A stream may not claim a sink it has not got
We know the plant produced 17.93 Mm³ of water in 2025. We do **not** know that
its sink is the port. Likewise, brine is not drawn to resource recovery, because
recovery is a candidate fate, not the current one.
Both therefore route to an external boundary (`EXT01`) as `REPORTED_PHYSICAL`,
with **separate** `CANDIDATE_COUPLING` edges for the sinks that might later
close.
### 3.3 One owner, bounded allocation
Shared credit ownership is where double counting eventually sneaks back in. A
physical quantity now has exactly **one** ledger owner; anyone else receives a
**bounded allocation** under a conservation constraint:
```javascript
sum(allocations) <= measured_generation
```
---
## 4. The veto rule, and why node clearance is not established
```javascript
NODE_PASS = AND(all component vetoes pass)
```
<table>
<tr>
<td>Veto</td>
<td>State</td>
<td>Why</td>
</tr>
</table>
<table fit-page-width="true" header-row="true">
<tr>
<td>---</td>
<td>---</td>
<td>---</td>
</tr>
<tr>
<td>`ECO-01` primary ecological status</td>
<td>UNRESOLVED</td>
<td>Only secondary summaries available</td>
</tr>
<tr>
<td>`CERT-01` pressure/marine component certification</td>
<td>UNRESOLVED</td>
<td>No certification path for printed parts</td>
</tr>
<tr>
<td>`CARB-01` CO2 counted once</td>
<td>UNRESOLVED</td>
<td>No metered CO2 flow, no transfer ledger entry</td>
</tr>
<tr>
<td>`GRID-01` renewable attribute ownership</td>
<td>UNRESOLVED</td>
<td>No green-direct allocation or contract</td>
</tr>
</table>
> **An unresolved veto is not a pass.**
A component that cannot be evaluated cannot be cleared. This is the structural
difference from a dashboard city: a dashboard can show you the desalination
plant failing while the compute centre is profitable. A flywheel cannot pass if
any component fails.
**`UNRESOLVED`**** and ****`FAIL`**** are semantically distinct.** Unresolved is an absence
of evidence; fail is evidence of a problem. Neither is a pass, but they call for
different responses — and conflating them would be its own error.
### 4.1 Validation is not clearance
These are two different questions and must never be read as one:
<table>
<tr>
<td>State</td>
<td>Question</td>
<td>Answer</td>
</tr>
</table>
<table fit-page-width="true" header-row="true">
<tr>
<td>---</td>
<td>---</td>
<td>---</td>
</tr>
<tr>
<td>`LOCALITY_CLEARANCE`</td>
<td>Has the physical locality node passed its vetoes?</td>
<td>NOT_ESTABLISHED</td>
</tr>
</table>
They are perfectly compatible: the simulator passed *because* it correctly
refused to clear the physical node. Never present the gate count as evidence
that Dongjiakou itself has passed certification, ecology or grid gates.
---
## 5. The scale reframe
Two new numbers, and they are worth sitting with.
<table>
<tr>
<td>Flow</td>
<td>Magnitude</td>
<td>Share of W01's 2025 process energy (39.446 GWh)</td>
</tr>
</table>
<table fit-page-width="true" header-row="true">
<tr>
<td>---</td>
<td>---</td>
<td>---</td>
</tr>
<tr>
<td>40 MW compute subnode at PUE 1.25 reference</td>
<td>438 GWh/year</td>
<td>\~1,110%</td>
</tr>
</table>
The locality's energy resources are large. The compute load is larger.
So the question is not:
> *"There are \~295 MW of renewables planned nearby, therefore run 40 MW of compute."*
It is:
> "Can a 40 MW compute subnode be contracted, dispatched and thermally
> integrated into this locality while preserving water, ecological, grid, carbon
> and component vetoes hour by hour?"
That is a better ORCS problem, and it is the one the architecture is built to ask.
**Correction carried into the record:** the LNG cascade figures were described in
one source as *"measured, operational."* They are not. Contemporary reporting
describes the project as having completed bidding and entered detailed design and
construction, with 26 GWh/year and 8 GWh/year as **projected at commissioning**.
The register therefore records
`E02_LNG_COLD_CASCADE = VERIFIED_PROJECT / UNDER_CONSTRUCTION / CURRENT_CREDIT_ZERO`.
This was independently re-checked: China Daily reports the facility "is expected
to generate 26 million kWh of electricity annually."
---
## 6. The portable schema
The next nodes are **not** clones of Dongjiakou. Define a generic node, then
instantiate a desalination-containing subclass:
```javascript
LOCALITY_NODE
  + DESAL_SUBNODE          (optional after the desal cohort proves the ontology)
  + ORCS_COMPUTE_SUBNODE
  + site-specific modules
```
Consequences:
<table>
<tr>
<td>Consequence</td>
<td>Statement</td>
</tr>
</table>
<table fit-page-width="true" header-row="true">
<tr>
<td>---</td>
<td>---</td>
</tr>
<tr>
<td>Dongjiakou becomes the first fully resolved template</td>
<td>Not a special case accidentally hard-coded into the system</td>
</tr>
<tr>
<td>`DESAL_SUBNODE` becomes optional</td>
<td>An inland steel town, agricultural basin, mining district, island, data-centre corridor or municipal region can use the same StreamGraph without pretending to have seawater RO</td>
</tr>
</table>
That is how "beyond 167" scales rigorously rather than rhetorically.
---
## 7. Why this is not smart cities 1.0
> The system is not smarter because it has more sensors. It is smarter because
> **physical flows are metered**, **every component retains an auditable ledger**,
> **optimization is Pareto rather than a fake universal score**, and a local
> failure cannot be washed out by profit somewhere else.
The Pareto rule is load-bearing and is enforced in the register:
> There is no single number that can rank a locality, because a scalar score is
> exactly what allows a local failure to be washed out by a gain somewhere else.
---
## 8. What changed, and what did not
<table>
<tr>
<td>Changed</td>
<td>Did not change</td>
</tr>
</table>
<table fit-page-width="true" header-row="true">
<tr>
<td>---</td>
<td>---</td>
</tr>
<tr>
<td>The unit of analysis: component → metered edge</td>
<td>The evidence vocabulary</td>
</tr>
<tr>
<td>The compute question: "can we power it" → "can we dispatch and integrate it"</td>
<td>C01 is a load, never a source</td>
</tr>
<tr>
<td>The node set: 167 projects → a discovery universe</td>
<td>UNKNOWN stays UNKNOWN</td>
</tr>
<tr>
<td>New subnodes added: E02, M01, MAT01, CHEM01, AGR01, CARB01, ECO01, GOV01</td>
<td>No credit before measurement</td>
</tr>
</table>
---
## 9. Next receipts, in priority order
<table>
<tr>
<td>Priority</td>
<td>Receipt</td>
<td>Unlocks</td>
</tr>
</table>
<table fit-page-width="true" header-row="true">
<tr>
<td>---</td>
<td>---</td>
<td>---</td>
</tr>
<tr>
<td>2</td>
<td>Chemical-park utility map (heat, steam, CO2, wastewater by plant)</td>
<td>AGR01 sizing, CARB01 coupling</td>
</tr>
<tr>
<td>3</td>
<td>LNG cold-energy cascade EIA</td>
<td>E02 thermal specs, CO2 liquefaction potential</td>
</tr>
<tr>
<td>4</td>
<td>Pilot base project list</td>
<td>Which of the 30 concurrent slots are materials / 3D printing</td>
</tr>
<tr>
<td>5</td>
<td>Node-001 green-direct eligibility confirmation</td>
<td>The 40 MW argument</td>
</tr>
<tr>
<td>6</td>
<td>Dongjiakou construction-waste allocation</td>
<td>M01 feedstock</td>
</tr>
</table>
If these land, the downstream layer becomes a **measured industrial symbiosis**. If
they do not, the components stay zero-credit. Same discipline as everything else.
---
## 10. Keeper
> The node is not "smart" because it has sensors. It is smart because every flow
> is metered, every component is auditable, and no aggregate net-positive claim
> can hide a local veto.
> **The architecture is the intelligence.**
## 11. Siting doctrine correction — population/locality first
**Human-root correction, 2026-10-07.** AGR01 is not a siting constraint for the parent locality node.
The node exists where a **locality, population, industrial metabolism or habitat** exists. Agricultural hinterland is an optimization advantage, not a prerequisite. Long-horizon Atlas scaling is therefore not “find farms and build nodes”; it is **extend the locality metabolism architecture wherever people and flows exist**, ultimately everywhere the evidence and governance contract can be instantiated.
AGR01 remains a standard capability lane, but its implementation is polymorphic:
- open-field hinterland;
- peri-urban/regional agriculture;
- greenhouse / controlled-environment agriculture;
- rooftop/built-surface food production;
- neighboring-node exchange.
The preferred hierarchy is:
**local use first → nearby/regional use second → inter-node exchange third → long-haul commodity disposition only for residual surplus.**
A node does not fail because it lacks farmland. It fails only if it claims a closed nutrient loop that it has not actually closed.
> **The locality defines the node. Agriculture adapts to the locality, not the other way around.**
