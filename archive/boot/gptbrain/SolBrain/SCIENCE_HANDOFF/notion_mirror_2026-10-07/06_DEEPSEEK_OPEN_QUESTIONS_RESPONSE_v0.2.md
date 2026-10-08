# Response | DeepSeek AGR01 Open Questions — Sulfur, SWRO Gypsum, Nutrient SSR & Metabolic Catchment v0.2

> Mirrored from Notion for SolBrain continuity.
>
> Notion page ID: `3f30c1de-73d9-810f-b487-ea272fc00350`
>
> Live page: https://app.notion.com/p/3f30c1de73d9810fb487ea272fc00350?pvs=204
>
> Last edited: 2026-10-08T02:53:57.651Z
>
> Verification state: unverified

**Status:** NON-CANON RESPONSE · FOR DEEPSEEK REVIEW · ZERO REALIZED CREDIT
**Purpose:** Close the remaining open questions from DeepSeek's AGR01 adversarial review.
## 1. Complete the cut-off section — regional vs node-level processes
> **Some processes will naturally remain regional rather than node-level because physics, hazard, geology or economies of scale make forced hyper-localization worse.**
Atlas should distinguish three transformation scales:
1. **Node-local** — crop-residue return, local fertigation, BIO01 nutrient recovery, struvite where a suitable sidestream exists, direct gypsum/sulfate soil amendment where agronomically justified, controlled-environment agriculture, and local K product use where separation/product quality are proven.
2. **Regional hub** — gypsum → sulfuric acid, large ammonia/Haber-Bosch trains, phosphate-rock beneficiation / phosphoric-acid production, hazardous/high-temperature fertilizer chemistry, and shared strategic storage where local storage is unsafe or inefficient.
3. **National / strategic** — import balancing, national reserves, geologically concentrated resources, and emergency redistribution during supply disruption.
**Localization rule:** localize distributed, low-hazard, mass-heavy biological loops; aggregate processes whose scale, temperature, hazard or feedstock concentration materially improves at regional scale.
The objective is **local-first metabolism, not autarky**.
## 2. Sulfur exposure — K-equivalent depth
### 2.1 2025 structural exposure
China imported **9.6084 Mt sulfur in 2025**. China Sulfuric Acid Industry Association reporting cited by SMM gives **11.80 Mt domestic sulfur production** and **21.40 Mt apparent sulfur consumption** for 2025. This implies an import share of roughly **44.9%** on that series. A separate 2026 securities-sector synthesis using a different domestic-production series reports **49.3% import dependence**. The accounting bases differ, so retain a **\~45–49% 2025 import-dependence band** rather than pretending there is one settled denominator.[\[1\]](https://news.smm.cn/news/103858102)[\[2\]](https://pdf.dfcfw.com/pdf/H3_AP202606101823424533_1.pdf)
By comparison, current potash evidence remains roughly **65–70% import-dependent**. Therefore:
- **K:** higher structural import dependence.
- **S:** lower structural dependence than K, but substantially higher acute price/chokepoint volatility.
### 2.2 Short-term disruption severity
- November 2025 sulfur imports: **487.3 kt**, down **28.08% YoY**.
- December 2025: **422.4 kt**, down **44.42% YoY**.[\[3\]](https://m.mysteel.com/oilchem/a/26012315/40C5DF74A4873E71_abc.html)
- Q1 2026 imports: **1.5501 Mt**, down **37.67%** from Q1 2025.[\[4\]](https://en.oilchem.net/26-0424-10-1f8a9c18b95000b3.html)
- IFPRI reports China's elemental-sulfur imports down **58% in H1 2026**, with reduced domestic phosphate-fertilizer production/exports.[\[5\]](https://www.ifpri.org/blog/how-are-fertilizer-markets-coping-with-the-continued-closure-of-the-strait-of-hormuz/)
China's 2026 fertilizer-security notice explicitly tells producers to prioritize domestic sulfur for phosphate fertilizer and supports phosphogypsum-to-acid projects.[\[6\]](https://zfxxgk.ndrc.gov.cn/wap/iteminfo.jsp?id=20603)
### 2.3 Sulfur risk metrics
- STRUCTURAL_IMPORT_DEPENDENCE_S
- SUPPLIER_CONCENTRATION_S
- MIDDLE_EAST_SHARE_S
- MONTHLY_IMPORT_VOLATILITY_S
- IMPORT_PRICE_VOLATILITY_S
- DAYS_OF_STOCK_S
- PHOSPHATE_OUTPUT_AT_RISK_S
- DOMESTIC_SULFUR_DISPLACEMENT_S
**Conclusion:** sulfur is the **acute resilience priority**; potash remains the **structural dependency priority**.
## 3. SWRO gypsum chemistry — can it use the same sulfuric-acid route?
### 3.1 Core answer
**Probably compatible after conditioning; not proven as a drop-in feed.**
The sulfuric-acid/cement chemistry is fundamentally a **calcium-sulfate** process, not a phosphate-specific reaction. Published Müller–Kühne-type work describes gypsum/anhydrite as calcium-sulfate feedstocks, and modern research explicitly evaluates ordinary gypsum / industrial by-product gypsum for sulfuric-acid + cement co-production.[\[7\]](https://pubs.acs.org/doi/10.1021/acssuschemeng.4c08838)[\[8\]](https://www.sciencedirect.com/science/article/pii/S0959652620318485)
China also has a direct non-phosphogypsum analogue: an official Ningxia environmental approval describes a project using **flue-gas-desulfurization gypsum plus electrolytic-manganese residue**, with calcination gas routed to sulfuric-acid production.[\[9\]](https://www.znzf.gov.cn/xxgk/zfxxgkml/xzqlyx/xzxkjggk/202512/t20251215_5109454.html)
Therefore phosphogypsum is **not the only calcium-sulfate feedstock class** that can enter this process family.
### 3.2 Why SWRO gypsum is still not automatically compatible
SWRO-derived precipitate can carry NaCl / residual chloride, Mg salts, boron and trace ions, antiscalant residues / organics, variable water content / crystal form, and co-precipitated solids.
RO-concentrate studies show antiscalants can materially suppress or distort gypsum precipitation. However, the problem is treatable:
- one study completely degraded an RO scale inhibitor using UV/H₂O₂ before seeded precipitation and achieved **97.12% CaSO₄ precipitation**;[\[10\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11124285/)
- another RO-concentrate recovery study produced **\~92% pure gypsum** after selective precipitation;[\[11\]](https://onlinelibrary.wiley.com/doi/10.2175/106143009X12487095236919)
- calcium-sulfate process patents explicitly include feed purification because alkalis/fluorides/other impurities can damage the clinker and acid systems.[\[12\]](https://patents.google.com/patent/US11845657B2/en)
### 3.3 Revised classification
> **The core calcium-sulfate chemistry is transferable in principle, and non-phosphogypsum gypsum-to-acid routes exist. SWRO gypsum appears to be a purification/specification problem rather than a fundamental chemistry mismatch, but direct Chinese plant compatibility is UNKNOWN until a target-plant acceptance assay and kiln trial are completed.**
Required Node-001 qualification train:
**antiscalant destruction/scavenging → controlled gypsum precipitation → wash → dewater → assay → optional calcination/anhydrite conditioning → target-plant raw-meal test → pilot kiln / off-gas test**
Minimum assay: CaSO₄·2H₂O / anhydrite fraction, Na, Cl, Mg, K, P, F, B, Si, Fe/Al, metals, TOC / antiscalant residue, moisture and particle size.
**Credit remains zero.**
## 4. P, N and S denominators — what can and cannot be published now
DeepSeek is correct that the SSR framework requires both demand and supply for every nutrient.
But one additional correction is needed:
**K's national supply calculation is reproducible; K's local demand denominator is still UNKNOWN too.**
So today for Node-001:
- SSR_K = UNKNOWN
- SSR_P = UNKNOWN
- SSR_N = UNKNOWN
- SSR_S = UNKNOWN
### 4.1 Why we should not manufacture denominators
Dongjiakou has evidence of grain/food logistics and processing, but that does not establish hectares in the Node-001 agricultural production boundary, crop mix, target yields, fertilizer application, soil-test status, straw return, greenhouse area or seasonal nutrient demand.
Likewise, BIO01 does not yet have measured annual P/N/K/S loads.
Therefore no legitimate local SSR number exists yet.
### 4.2 Denominator formulas
For nutrient x in \{N,P,K,S\} and time period t:
REQUIREMENT_x(t) = sum(crop_area_i × agronomic_net_requirement_i,x) + CEA_requirement_x(t)
where agronomic_net_requirement is **soil-test / target-yield nutrient need after credited soil supply**, not historical fertilizer application if historical application is excessive.
LOCAL_SUPPLY_x = residue_return_x + wastewater_recovery_x + digestate_x + biological_fixation_x + local_mineral_x + other_verified_local_x
REQUIREMENT_x = LOCAL_USE_x + INTER_NODE_IMPORT_USE_x + EXTERNAL_IMPORT_USE_x + RESERVE_DRAW_x + UNMET_x
SSR_x = LOCAL_USE_x / REQUIREMENT_x
INTER_NODE_FRACTION_x = INTER_NODE_IMPORT_USE_x / REQUIREMENT_x
EXTERNAL_IMPORT_FRACTION_x = EXTERNAL_IMPORT_USE_x / REQUIREMENT_x
SURPLUS_x = max(0, LOCAL_SUPPLY_x - LOCAL_USE_x - RESERVE_ADDITION_x)
No tonne may occupy two allocation buckets.
### 4.3 Urban-node edge case
A node with no local crop production must **not** receive SSR_x = 100% merely because fertilizer demand is zero.
Use AGR_NUTRIENT_SSR_x = NA where local agronomic requirement is zero, plus separate FOOD_SELF_PROVISION by commodity class and RECOVERED_NUTRIENT_EXPORT_x.
That prevents a dense city from gaming the nutrient metric while remaining fully valid as an Atlas node.
## 5. Metabolic catchment — operational definition
A metabolic catchment should be a **versioned graph around a fixed locality boundary**, not a fuzzy radius that expands whenever the model needs more resources.
### 5.1 Boundary classes
**A. NODE_CORE** — fixed administrative / governance locality polygon; population and physical assets whose home location is inside the node. Every physical asset has exactly **one home node**.
**B. INTER_NODE_EDGE** — any measured/contracted flow whose source and sink have different home nodes. These flows do **not** expand the core boundary.
**C. EXTERNAL_EDGE** — source or sink lies outside the Atlas lattice / current accounting universe.
### 5.2 Catchment as graph
METABOLIC_CATCHMENT = NODE_CORE + evidenced inbound/outbound edges + seasonal profiles
It is therefore partly geographic and partly contractual. This prevents double counting: a farm cannot become local to two adjacent cities.
### 5.3 Required metrics
Food: population, food-demand basket by commodity, local food production, lattice food imports and external food imports.
Agriculture: field/CEA area, crop, yield, N/P/K/S requirement, nutrient application, crop-residue return and harvested nutrient export.
Circular supply: wastewater N/P/K/S, digestate, struvite, recovered K, gypsum/sulfate and other nutrient products.
Exchange: origin node, destination node, quantity, quality, distance, mode, seasonal profile, losses, contract and primary credit owner.
### 5.4 Time resolution
Report both **annual balance** for strategic self-sufficiency and **monthly/seasonal balance** for actual farm availability.
A locality that has enough K annually but not during planting is not operationally self-sufficient.
## 6. Revised keeper
> **The locality defines the node. Agriculture adapts to the locality. The metabolic catchment is the fixed locality core plus evidenced exchange edges, never a movable boundary used to improve a score. Nutrient self-sufficiency is measured independently for N, P, K and S against agronomic demand; inter-node exchange and external imports are separate fractions. K is the deeper structural import dependency, while sulfur is the more acute chokepoint/price-volatility exposure. SWRO gypsum is a plausible calcium-sulfate feed after purification, but direct compatibility with a target gypsum-to-acid line remains a pilot gate, not a credit.**
## 7. Immediate receipts that close the remaining UNKNOWNs
1. Node-001 agricultural / CEA asset map.
2. Crop mix + hectares + target yields.
3. Soil-test / recommended N-P-K-S requirement by field or production unit.
4. Actual fertilizer purchases/applications.
5. Straw/residue return and exported biomass.
6. BIO01 time-series N/P/K/S loads.
7. Recovered K product assay and recovery.
8. SWRO gypsum product assay after antiscalant-removal/precipitation.
9. Target Chinese gypsum-to-acid plant feed specification.
10. Seasonal inter-node nutrient-flow matrix.
Until these receipts exist, SSR values remain UNKNOWN rather than modeled into existence.
## Dongjiakou reconnection
The parent/subnode mapping and corrected sulfur aggregation thresholds are carried forward in <mention-page url="https://app.notion.com/p/3f30c1de73d9815d832cc50d6eff5cc3"/>.
