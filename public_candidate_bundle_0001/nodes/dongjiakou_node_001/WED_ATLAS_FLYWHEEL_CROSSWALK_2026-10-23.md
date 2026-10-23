# Water–Energy–Data Crosswalk: Dongjiakou and the Atlas Lattice Flywheel

STATUS: CANDIDATE  
CANON: no  
DEPLOYMENT: no  
AUTHORITY: none  
PROOF: no  
PUBLIC_RELEASE: candidate

Date: October 23, 2026. Additive methodology update. No numerical model, historical output, test result or realized integration credit is changed.

## Receipt fields

- artifact_id: DONGJIAKOU_WED_CROSSWALK_2026_10_23_v0_1
- title: WED crosswalk: Dongjiakou, Corpus Christi, Maui and Oʻahu
- source_surface: github + external + chat
- source_uri: https://arxiv.org/abs/2610.23614
- source_path: public_candidate_bundle_0001/nodes/dongjiakou_node_001/WED_ATLAS_FLYWHEEL_CROSSWALK_2026-10-23.md
- raw_export_status: cited repository files fetched in full; external paper abstract/metadata only
- receipt_status: partial_content (paper); full_export_present (repository documents)
- canon_status: non-canon
- deployment_status: not established
- authority_scope: research documentation only
- public_release_status: candidate; publication requested by user
- missing_receipts: [paper full text and supplements, current site-specific commissioning records, metered transfers, assays, contracts]
- linked_claims: [methodological alignment, not design validation or causal influence]
- review_lane: scope, provenance, thermodynamics, lifecycle burdens and financial accounting

## 1. Paper and evidence boundary

Huang, Jincheng; Xiao, Guoan; Lan, Xin; Yin, Caichun; Jiang, Zhimeng; Cui, Yue; Liu, Jianguo. *Water-Energy-Data nexus reveals sustainability gaps and priorities for AI infrastructure*. arXiv:2610.23614v1 [cs.CY], submitted October 16, 2026. [Abstract](https://arxiv.org/abs/2610.23614) · [PDF](https://arxiv.org/pdf/2610.23614) · [DOI](https://doi.org/10.48550/arXiv.2610.23614).

The authors report an LLM-assisted evidence synthesis covering 12,825 studies across mineral extraction, semiconductor manufacturing, data-center operations and e-waste processing. Their framework addresses spatial and lifecycle dependencies that operational-energy-focused assessments can overlook, including burdens transferred between places.

This update uses the abstract, not a completed full-text review. Detailed screening quality, operational indicators, relation to water–energy–food literature and transferability to municipal waste remain review questions. A synthesis is research in its own right; it is not a new operating-plant trial. The paper does not validate Atlas designs, ROI, savings or deployment. Similarity does not establish awareness of, influence from, or endorsement of Atlas Lattice.

## 2. Existing Dongjiakou alignment

The [integrated node architecture](INTEGRATED_NODE_ARCHITECTURE_v0_1.md) already preserves standalone component, transfer and aggregate-node ledgers. Compute remains a load. No aggregate positive score can erase a component-level ecological, safety or regulatory failure. LLMs have no PLC/SCADA actuator authority.

| WED issue interpreted from abstract | Existing/proposed Atlas implementation | Evidence required |
|---|---|---|
| Narrow operating-energy boundary | Separate process, utility-service and compute-facility ledgers | Metered auxiliaries, water, discharge and compute PUE |
| Spatial burden transfer | Record receiving location and residual fate | Transport, acceptance, treatment and final destination |
| Lifecycle dependence | Include construction, replacements and end-of-life | Equipment/material inventories and lifetime assumptions |
| Benefits hide burdens elsewhere | Same-service counterfactual and transfer ledger | No duplicated cash, material, carbon or avoided-cost credits |
| Data benefits versus resource costs | Disaggregated physical service benefit per compute kWh | Incremental measured improvement versus credible baseline |

This mapping is our proposed interpretation, not a statement that the paper specifies these fields.

### Prior findings retained

- [Cold-cascade evidence v0.5](https://github.com/atlaslattice/open-regenerative-compute-standard/blob/main/docs/notion-mirrors/2026-10-12-dongjiakou-lng-cascade-v05.md) records a separate ¥108 million cold-use project and LNG-assisted air-separation initiative. The cold-use project's **26 GWh/year generation + 8 GWh/year avoided cooling electricity** are projected quantities, not delivered output. The combined 34 GWh/year is neither 34 GW nor a thermal-cold budget. Current commissioning was not re-audited here, and no integrated Atlas data-center/freeze-desalination connection is credited.
- [Engineering and cost v0.4](https://github.com/atlaslattice/open-regenerative-compute-standard/blob/main/docs/notion-mirrors/2026-10-12-dongjiakou-corpus-desal-cost-v04.md) preserves the reported original 100,000 m³/day desalination nameplate (about 26.4 MGD). Historical design energy, narrower UF/RO energy and actual annual production are different boundaries. Historical Chinese CAPEX is not a contemporary all-in U.S. construction quote.
- [Compute transfer function](run3_compute_v0_2.py) holds useful heat credit at zero pending sink receipts. A hypothetical continuous 40 MW IT load at PUE 1.25 uses **438 GWh/year facility electricity**; ideal IT heat is at most 350.4 GWh thermal/year, with less transferable. Those quantities are illustrative, not actual Node-001 operation.
- [BIO01 response](DEEPSEEK_RESPONSE_BIO01_v0_1.md) records earlier reported Qingdao digestion and local biological wastewater-treatment precedents. These are archived claims, not newly verified operations. Proposed node biogas, compost, nutrient and water-reuse increments retain zero credit without assigned feed, measurements and acceptance. Saline brine, CIP chemicals, toxic industrial wastewater and hazardous streams are not generic digester feed.

## 3. Full flywheel: proposed integration, not automatic net positivity

A useful flywheel connects qualified outputs to accepted inputs while accounting for energy, logistics, treatment and final residues. Resources can circulate; energy degrades and requires replenishment. These are parallel conditional branches, not a mandatory serial chain:

1. **Water:** desalination, separately collected wastewater, treatment/polishing, qualified reuse, storage and emergency supply.
2. **Energy:** contracted power, storage and measured heat/cold duties; temperature and hourly matching, including backup.
3. **Compute:** justified inference and optimization workloads; flexible dispatch and operator advice; measured gains compared with compute's own resource footprint.
4. **Organics:** allocated suitable feed → biological conversion → biogas and digestate → qualified nutrient/compost products.
5. **Brine/minerals:** assayed chemistry → selective separation → accepted products; distinct contaminated residual routes.
6. **Materials:** reuse-first inspection, metals, suitable polymers and aggregates, specialist processors/refineries where needed.
7. **Community/ecology:** resident water reliability and affordability, instream flows/coastal quality, actual land preservation, local employment and maintenance capability.

Cold-intensive freezing/air-separation duties need compatible low-temperature supply before warmer sinks. Server heat may serve melting or suitable heating duties; it is not free refrigeration. Do not allocate the same cold, heat, electricity or material twice.

### Proposed minimum transfer record

Record source/destination; evidence status; mass/volume and wet/dry basis; composition/contaminants; temperature/pressure; hourly/seasonal availability; distance; treatment/transport parasitics; ownership/contract; receiving specifications; price/transfer charge; rejected fraction/final fate; baseline and displaced demand.

Compare matched services under standalone facilities, physical sharing, physical sharing plus justified compute advice, and optional biological/mineral recovery. Keep operator cash, internal transfers, societal benefits and avoided public spending distinct. Import substitution requires accepted grade and actual demand displacement, net of imported inputs. A positive financial balance cannot override ecological or safety vetoes.

## 4. Corpus Christi: same framework, different physics

The [Corpus white paper v1.2](https://github.com/atlaslattice/open-regenerative-compute-standard/blob/main/docs/whitepapers/ORCS_CORPUS_THERMAL_WATER_MINERAL_WP_v1_2_2026-10-14.md) proposes refinery heat recovery, wastewater reuse, desalination, qualified minerals and dry-cooled optimization/inference compute. It considers a **5 MW pilot expandable to 20 MW**, conditional on power, workload and site evidence; these are not operating Atlas assets.

Dongjiakou receives/regasifies LNG. Corpus LNG exports through liquefaction, consuming refrigeration. **Do not transplant a regasification cold credit to an export terminal.** Transfer the stream ledger, exergy matching and lifecycle method.

Harbor Island and Inner Harbor are separate scopes. Prior 20/30/50/100-MGD historical and hypothetical cases must not be combined into one current approved design. Current procurement/permit status is not refreshed here. Heat must be surplus after existing recovery; reuse needs contracts/quality; gross mineral inventory is not saleable yield.

## 5. Maui and Oʻahu: distinguish islands and scenario versions

The [October 16 Maui handoff](https://github.com/atlaslattice/open-regenerative-compute-standard/blob/main/research/solgpt-maui-orcs-comprehensive-handoff-2026-10-16.md) proposes **Central 25 + West 6 + North 5 = 36 MGD nameplate**, with water/reuse, recovery, inference, microgrids and residents-first service. Proposed, not installed. Its financial stress tests show unresolved funding gaps; the architecture is not automatically self-financing.

The earlier [geothermal/biosolar/ZLD study](https://github.com/atlaslattice/open-regenerative-compute-standard/blob/main/research/geothermal-biosolar-zld-maui-corpus-christi-siting-v1.0-2026-10-15.md) uses a distinct **15-MGD** scenario and expensive full-ZLD energy sensitivity. Do not apply those totals to 36 MGD. No commercial Maui geothermal supply or full integrated ZLD/data-center coupling is established. Staged concentrate management must be compared on actual chemistry, energy and residuals.

The [Hawaiʻi commercial recovery package](https://github.com/atlaslattice/open-regenerative-compute-standard/blob/main/research/shreddernaut/hawaii-commercial-recovery-2026-10-23/README.md) moves Shreddernaut toward commercial supplier-configured machinery. Screening, ferrous/nonferrous recovery, combustible preparation, fines treatment and residual handling need separately identified scope. Soil-washing filter cake is not equivalent to organic sewage sludge or automatically fuel. A supplier inquiry and Mandarin summary were sent; no supplier offer or partnership is established here, and private email is not reproduced.

**Oʻahu is a separate reference, not a Maui deployment.** [EPA's October 16 announcement](https://www.epa.gov/newsreleases/epa-announces-109-million-wifia-loan-increase-water-supply-reliability-honolulu-hawaii) reports a $109 million WIFIA loan for Kalaeloa's 1.7-MGD desalination project, including byproduct-disposal works, recycled-water pipeline and transmission. Financing evidence does not establish operation or total project CAPEX, let alone an Atlas compute connection.

[Honolulu's October 1 G.R.O.W. expansion](https://www.honolulu.gov/mayor/city-expands-food-waste-composting-program-islandwide-beginning-october-1st/) routes food/green waste from eligible three-cart households to composting. [Hawaiʻi Gas](https://www.hawaiigas.com/sustainability/renewable-natural-gas) separately describes wastewater-biogas upgrading at Honouliuli, while [Cambi](https://www.cambi.com/customer-stories/honolulu-honouliuli) lists thermal-hydrolysis delivery in 2026 and operation in 2027 as scheduled. No co-location, food-waste co-digestion, shared data center or accepted Shreddernaut RDF contract is established. The opportunity is interface assessment among real/proposed facilities, not relabeling them as one installed loop.

## 6. Next gates and change report

- Read full paper/supplements: methods, LLM validation, operational indicators, e-waste burden transfer and WEF relationship.
- Retrieve site-resolved assays, hourly flows, temperature profiles, commissioning evidence and contracts.
- Normalize electrical/thermal/exergy, whole-line/component, calendar/operating-hour and lifecycle/cashflow boundaries.
- Run matched-service scenarios only after explicit inputs; no new simulation was executed for this document.
- Retain component vetoes, operator approval and zero unearned integration credits.
- Preserve source claims and corrections additively.

files_changed: new crosswalk, companion DeepSeek briefing, additive navigation link in existing architecture.  
commands_run: repository file fetch/read/create/update; external abstract and EPA source retrieval.  
test_results: documentation checks only; no code tests or historic test recertification.  
receipts_added: fetched repository context; paper metadata/abstract; EPA project text.  
missing_receipts_created: full text, assays, meters, current commissioning and commercial terms.  
blockers: no new physical/contractual connections or complete cross-site simulation.  
forbidden_claims_avoided: canon, deployed full loop, proven net positivity, vendor endorsement and causal influence.
