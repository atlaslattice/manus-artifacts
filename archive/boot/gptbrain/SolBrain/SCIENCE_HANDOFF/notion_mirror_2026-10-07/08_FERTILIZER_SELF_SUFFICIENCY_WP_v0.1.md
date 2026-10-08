# White Paper | Fertilizer-Input Self-Sufficiency — Dongjiakou Node-001 to 120-Node Lattice v0.1 — DeepSeek Review Draft

> Mirrored from Notion for SolBrain continuity.
>
> Notion page ID: `3f30c1de-73d9-811f-80dd-efca81689858`
>
> Live page: https://app.notion.com/p/3f30c1de73d9811f80ddefca81689858?pvs=204
>
> Last edited: 2026-10-08T03:09:44.154Z
>
> Verification state: unverified

**Document ID:** AGR01-FERTILIZER-SELF-SUFFICIENCY-WP-v0.1  
**Status:** **NON-CANON · FOR INDEPENDENT REVIEW · ZERO REALIZED CREDIT**  
**Purpose:** Give DeepSeek a falsifiable Node-001 → 120-node fertilizer-input self-sufficiency model, with conservative floors separated from research-bounded upside.
<callout icon="🌾" color="green_bg">
	**Design objective:** minimize avoidable external dependence in fertilizer and fertilizer feedstocks while preserving or improving food output, soil condition, water quality and farmer economics.
	**Not a policy claim:** this paper does not assert that China has formally adopted a universal “zero fertilizer imports” policy. It treats maximum practical self-sufficiency as a design objective and compares it with current Chinese fertilizer-security policy.
</callout>
<table_of_contents/>
## Executive summary
The first correction is important: **the working claim that roughly 70% of China's fertilizer is imported is not supported as an economy-wide fertilizer statistic.** WITS/UN Comtrade reports that China imported about **US\$4.88 billion** of HS Chapter 31 fertilizers in 2025 while exporting about **US\$13.49 billion**. China is therefore a major net fertilizer exporter by trade value, although it remains materially exposed to specific imported inputs.[\[1\]](https://wits.worldbank.org/trade/comtrade/en/country/CHN/year/2025/tradeflow/Imports/partner/ALL/product/31)[\[2\]](https://wits.worldbank.org/trade/comtrade/en/country/CHN/year/2025/tradeflow/Exports/partner/ALL/product/31)
The self-sufficiency problem is narrower and more actionable:
- **K / potash:** structural import dependence is the clearest fertilizer vulnerability.
- **S / sulfur:** a major imported upstream feedstock for phosphate fertilizer, with chokepoint exposure.
- **P / phosphorus:** China has a strong domestic phosphate industry, but circular P recovery can reduce virgin rock and sulfuric-acid demand.
- **N / nitrogen:** direct urea imports are currently negligible; the strategic objective is lower domestic energy/feedstock burden and higher nitrogen-use efficiency, not import substitution.
The existing Dongjiakou model contains a **26.0–28.9 kt/y KCl-equivalent dissolved-inventory ceiling per node**. At 120 standardized nodes:
- **25% recovery sensitivity:** 0.780–0.867 Mt/y KCl-equivalent → **6.1–6.8%** of China's 2024 KCl imports.
- **50% recovery sensitivity:** 1.560–1.734 Mt/y → **12.2–13.6%**.
- **100% inventory ceiling:** 3.120–3.468 Mt/y → **24.4–27.1%**.
The **25% case is the proposed conservative planning floor**, not because 25% has been measured at Dongjiakou—it has not—but because it deliberately uses only one quarter of the modeled inventory and credits no P, S, N, straw-return, precision-agriculture or yield benefit.
China imported **12.778 Mt of KCl in 2024**, worth US\$3.766 billion.[\[3\]](https://wits.worldbank.org/trade/comtrade/en/country/CHN/year/2024/tradeflow/Imports/partner/ALL/product/310420) At the 2026 Chinese standard MOP contract benchmark of about **US\$348/t CFR**, the 120-node 25% case corresponds to roughly **US\$271–302 million/y of avoided procurement**, if the recovered product meets equivalent specification and genuinely displaces imports rather than adding supply.[\[4\]](https://www.argusmedia.com/en/news-and-insights/latest-market-news/2828100-bpc-ipl-set-new-india-mop-contract-at-383-t-cfr)
The sulfur lane may eventually be comparably strategic, but **it is not yet creditable**. The published-range Dongjiakou model contains about **109 kt/y sulfate per node**, yet sulfate is already oxidized and cannot be treated as elemental sulfur. However, China is actively building phosphogypsum-to-sulfuric-acid systems: one 2026 Guizhou project is configured around **500 kt/y phosphogypsum → 200 kt/y sulfuric acid**, while a 2026 Hubei project is designed for **1 Mt/y phosphogypsum → 400 kt/y sulfuric acid**.[\[5\]](https://www.kaiyang.gov.cn/zwgk/zdlyxxgk/hjbh_5777165/xmhp/202606/t20260616_90530492.html)[\[6\]](https://hbj.yichang.gov.cn/content-42531-996867-1.html)
If—and only if—Dongjiakou's modeled calcium and sulfate can be separated into a compatible gypsum feed, a transferred-reference calculation using the **internal calcium ceiling** produces a bounded research case of approximately:
- **62.7–76.9 kt/y gypsum-equivalent per node**;
- **25.1–30.8 kt/y sulfuric acid per node** using the Chinese 0.4 t acid/t gypsum project ratio;
- **3.01–3.69 Mt/y sulfuric acid at 120 nodes**;
- equivalent to roughly **0.98–1.21 Mt/y elemental sulfur content**, or **9.9–12.1%** of the approximately 9.95 Mt of crude sulfur represented by China's reported 2024 import-partner quantities.
That is **REFERENCE-BOUNDED UPSIDE, not credit**. Brine gypsum chemistry, purity, energy demand, kiln/reductant requirements and acid-product specification are all unresolved.
The agriculture side may ultimately be as important as extraction. A 2026 Chinese analysis estimated **9.25 Mt K** was supplied through returned cereal residues in 2020—reported as **2.1× national cereal K-fertilizer consumption**—showing that K already circulating through crop residues is an enormous domestic resource.[\[7\]](https://www.sciencedirect.com/science/article/pii/S0378429026001462) A separate China-wide analysis estimated seasonally available direct straw-return nutrients could substitute approximately **10% N, 9% P₂O₅ and 58% K₂O** of chemical fertilizer under its modeled maximum-return conditions.[\[8\]](https://www.mdpi.com/2077-0472/13/6/1187) Those figures are not added to the 120-node offset because current residue-return rates, regional mismatches and double counting must first be resolved.
The central thesis is therefore:
> **Fertilizer self-sufficiency should be attacked from both sides of the ledger: recover more strategic atoms domestically while reducing the amount of virgin fertilizer required per tonne of food.**
## 1. Scope and accounting doctrine
This paper extends <mention-page url="https://app.notion.com/p/3f30c1de73d981449ee0c735cd9b37cb"/> and the <mention-page url="https://app.notion.com/p/3f20c1de73d981dc8d2dca642e4c049b"/>.
The governing rules are:
1. **Local UNKNOWN stays UNKNOWN.** External data may bound a scenario; it does not become a Dongjiakou receipt.
2. **Atoms do not substitute for different atoms.** Magnesium cannot become potassium. Gypsum cannot silently become elemental sulfur. Nitrogen-use efficiency cannot be counted as K recovery.
3. **One tonne gets one primary credit.** A tonne of recovered K cannot be both an import offset and a strategic reserve addition.
4. **Avoided import value requires a counterfactual import.** Domestic production added above demand is inventory, not annual savings.
5. **Demand reduction is separate from supply addition.** Only after the baseline fertilizer requirement is measured can the two be combined.
6. **Agronomic performance is a gate.** Fertilizer reduction that sacrifices total food/protein output does not automatically count as a strategic success.
7. **Ecological performance is a gate.** Salinity, nutrient runoff, heavy metals, persistent contaminants and soil degradation can veto a fertilizer pathway.
### 1.1 Node-siting correction — locality first, agriculture second
AGR01 is **not a siting veto** and an agricultural hinterland is **not required** for an Atlas locality node.
The primary node unit remains the **human locality / population and its metabolism**. In the long horizon, the lattice is intended to extend wherever people and material flows exist, ultimately toward universal locality coverage. Agricultural hinterland is advantageous because it provides low-logistics nutrient sinks, biomass cycling and open-field food production, but it is one implementation condition rather than the definition of a node.
AGR01 should therefore be treated as a **universal food/nutrient capability lane whose physical form is site-specific**:
- existing agricultural hinterland where available;
- peri-urban and neighboring farms;
- controlled-environment agriculture / greenhouse systems;
- rooftop or built-surface production where structurally and economically appropriate;
- regional exchange for unavoidable surplus/deficit.
Each node should report a **nutrient self-sufficiency vector** rather than a binary self-sufficient/not-self-sufficient label:
`SSR_K`, `SSR_P`, `SSR_N`, `SSR_S`, plus `LOCAL_USE_FRACTION` and `INTER_NODE_EXCHANGE_FRACTION`.
The design objective is **local-first use with marginal exchange**, not mandatory local consumption of every output. A dense urban node with no open-field hinterland is still a valid node if it closes as many food/nutrient loops as its physical context allows and reports the remaining exchange honestly.
## 2. What China is actually exposed to
<table fit-page-width="true" header-row="true">
<tr>
<td>Lane</td>
<td>External baseline</td>
<td>Strategic interpretation</td>
<td>Current Atlas credit</td>
</tr>
<tr>
<td>**KCl / potash**</td>
<td>12.778 Mt imported in 2024; US\$3.766B import value</td>
<td>Primary structural fertilizer-input exposure</td>
<td>MODELED only</td>
</tr>
<tr>
<td>**Crude sulfur**</td>
<td>\~9.95 Mt in 2024 by summed reported partner quantities; US\$1.157B import value</td>
<td>Major phosphate-fertilizer feedstock and chokepoint exposure</td>
<td>0</td>
</tr>
<tr>
<td>**Natural phosphate rock**</td>
<td>US\$202.7M imports in 2024</td>
<td>Smaller import exposure; circular P still strategically useful</td>
<td>0</td>
</tr>
<tr>
<td>**Urea**</td>
<td>2025 import value only \~US\$2.4M; partner quantities are tiny</td>
<td>Not a material import-elimination target</td>
<td>0 import offset</td>
</tr>
</table>
Sources: WITS/UN Comtrade KCl 2024,[\[3\]](https://wits.worldbank.org/trade/comtrade/en/country/CHN/year/2024/tradeflow/Imports/partner/ALL/product/310420) sulfur 2024,[\[9\]](https://wits.worldbank.org/trade/comtrade/en/country/CHN/year/2024/tradeflow/Imports/partner/ALL/product/250310) phosphate rock 2024,[\[10\]](https://wits.worldbank.org/trade/comtrade/en/country/CHN/year/2024/tradeflow/Imports/partner/ALL/product/2510) and urea 2025.[\[11\]](https://wits.worldbank.org/trade/comtrade/en/country/CHN/year/2025/tradeflow/Imports/partner/ALL/product/310210)
This framing is consistent with China's 2026 fertilizer-security notice, which explicitly calls for stable phosphate-rock supply, faster phosphogypsum-to-acid projects, priority domestic sulfur supply to phosphate-fertilizer producers, secure potash imports and reserves, soil-test/formula fertilization, organic fertilizer and intelligent blending.[\[12\]](https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260205_1403611.html)
## 3. K — the load-bearing import-substitution lane
### 3.1 Node-001 modeled resource — denominator made explicit
The **KCl-equivalent floor used in this paper** comes from one explicit published-range feed-water sensitivity and must not be mixed with older composition sensitivities:
- fixed 2025 product water: **17.93 Mm³/y**;
- modeled RO recovery sensitivity: **50% → 35.86 Mm³/y feed**, **45% → 39.84 Mm³/y feed**;
- external-reference potassium concentration: **380 mg/L K = 0.380 kg/m³**;
- resulting feed-water K inventory: **13.63–15.14 kt K/y**;
- molecular conversion `KCl/K = 74.5513/39.0983 = 1.9068`;
- resulting inventory ceiling used here: **25.98–28.87 kt/y KCl-equivalent**.
This is why the 25% × 120-node sensitivity reproduces **6.10–6.78% of 12.778 Mt/y 2024 KCl imports**.
A separate legacy composition sensitivity in the archive produced roughly **14.2–17.3 kt/y elemental K**. It is a different modeled basis and **must not be used interchangeably** with the 380 mg/L feed-water basis above. Until a Dongjiakou time-series K assay and permeate/concentrate mass balance exist, both remain MODELED and neither is a measured recoverable product.
### 3.2 120-node sensitivity
<table fit-page-width="true" header-row="true">
<tr>
<td>Case</td>
<td>Per-node KCl-eq</td>
<td>120-node KCl-eq</td>
<td>2024 Chinese KCl imports displaced</td>
<td>2024 import-value equivalent</td>
<td>2026 contract-price equivalent</td>
</tr>
<tr>
<td>**Conservative planning sensitivity — 25%**</td>
<td>6.5–7.2 kt/y</td>
<td>0.780–0.867 Mt/y</td>
<td>**6.1–6.8%**</td>
<td>\~US\$230–256M/y</td>
<td>\~US\$271–302M/y</td>
</tr>
<tr>
<td>**Central sensitivity — 50%**</td>
<td>13.0–14.5 kt/y</td>
<td>1.560–1.734 Mt/y</td>
<td>**12.2–13.6%**</td>
<td>\~US\$460–511M/y</td>
<td>\~US\$543–603M/y</td>
</tr>
<tr>
<td>**Inventory ceiling — 100%**</td>
<td>26.0–28.9 kt/y</td>
<td>3.120–3.468 Mt/y</td>
<td>**24.4–27.1%**</td>
<td>\~US\$920M–1.02B/y</td>
<td>\~US\$1.09–1.21B/y</td>
</tr>
</table>
The **25% case is not called “conservative” because 25% recovery has been demonstrated**. It has not. It is conservative relative to the dissolved-inventory ceiling. The first actual K separation pilot must replace this sensitivity.
### 3.3 Demand-side K may be as important as the brine
A 2026 national analysis estimated cereal residues accumulated **10.7 Mt K** in 2020 and that residue return supplied **9.25 Mt K**, 2.1× national cereal K-fertilizer consumption.[\[7\]](https://www.sciencedirect.com/science/article/pii/S0378429026001462)
Field evidence also supports significant chemical-K substitution in suitable rotations. A maize-rice study found straw return could replace roughly half of chemical K fertilizer in that system,[\[13\]](https://www.sciencedirect.com/science/article/pii/S2214514120300696) while long-term maize-wheat work found straw return could substitute conventional K fertilizer without a yield penalty in the studied conditions.[\[14\]](https://www.mdpi.com/2073-4395/14/6/1266)
**Do not add these percentages to the 6.1–6.8% import offset yet.** Some residue return is already occurring. The national opportunity is to measure the **incremental** reduction in chemical K purchases achievable by better residue accounting and precision K recommendations.
## 4. S — convert an imported feedstock problem into a circular sulfate problem
### 4.1 Why sulfur matters
China's 2026 fertilizer-security policy specifically prioritizes domestic sulfur for phosphate fertilizer and supports phosphogypsum-to-acid projects.[\[12\]](https://www.ndrc.gov.cn/xxgk/zcfb/tz/202602/t20260205_1403611.html)
The 2026 Hormuz disruption showed why this matters: sulfur, ammonia and nitrogen-fertilizer feedstocks can become chokepoint-sensitive even when finished fertilizer supply appears secure.
### 4.2 Published-range sulfate/calcium sensitivity — NOT a Dongjiakou assay
The current model carries approximately:
- **109,373 t/y sulfate (SO₄)** in the cited published-range sensitivity;
- **14.6–17.9 kt/y calcium** from generic seawater-ratio modeling.
**Evidence correction:** these are **MODELED / GENERIC_SEAWATER_COMPOSITION**, not site-specific Dongjiakou brine measurements. A Dongjiakou feed/permeate/concentrate assay remains required before either becomes a recoverable-resource estimate.
The whole sulfate inventory contains about 36.5 kt/y sulfur atoms, but it is chemically wrong to count that as 36.5 kt/y elemental-sulfur displacement.
### 4.3 Internal-calcium gypsum bound
Using only the modeled internal Ca inventory, and without assuming imported/external Ca:
- 14.6–17.9 kt/y **generic-seawater-modeled Ca** could stoichiometrically bind approximately **62.7–76.9 kt/y gypsum-equivalent (CaSO₄·2H₂O)** under a **100%-Ca-capture ceiling**. This is not a Dongjiakou production forecast. The corresponding sulfate requirement is only \~35.0–42.9 kt/y, so Ca is the limiting modeled reagent inside this sensitivity.
- China now has real projects using roughly **0.4 t sulfuric acid per tonne phosphogypsum** as the project-scale output ratio:
	- 500 kt/y gypsum → 200 kt/y H₂SO₄ in Guizhou;[\[5\]](https://www.kaiyang.gov.cn/zwgk/zdlyxxgk/hjbh_5777165/xmhp/202606/t20260616_90530492.html)
	- 1 Mt/y gypsum → 400 kt/y H₂SO₄ in Hubei.[\[6\]](https://hbj.yichang.gov.cn/content-42531-996867-1.html)
- Applying that external ratio gives **25.1–30.8 kt/y H₂SO₄ per node**, or **3.01–3.69 Mt/y at 120 nodes**.
- The sulfur content of that acid equals roughly **0.98–1.21 Mt/y elemental S** at 120 nodes.
- Against the \~9.95 Mt of crude sulfur represented in China's 2024 WITS partner data, that is a **9.9–12.1% research-bounded equivalent**.
**Credit: zero.** This is a comparator-bounded research hypothesis. SWRO-derived gypsum is not automatically equivalent to phosphogypsum, and the process must close energy, reductant, impurities, acid quality, solids and emissions.
### 4.4 Direct agricultural sulfate lane
Even if acid regeneration fails, sulfate may have direct value as:
- gypsum for saline/sodic soil amendment where soil tests justify it;
- sulfate-S fertilizer;
- potassium-magnesium sulfate products;
- magnesium sulfate products.
Those uses can reduce sulfur demand in agriculture, but they must be expressed in **plant-available S** and matched to crop/soil demand. Direct soil application and acid regeneration cannot both claim the same sulfur atoms.
## 5. P — close the nutrient loop before buying more phosphate
The phosphate lane is already technically promising but lacks a Dongjiakou mass denominator.
<mention-page url="https://app.notion.com/p/3f20c1de73d98156b6f8e081c4a26f3f"/> records a China pilot at **25 m³/day** that reported about **95% phosphate-P recovery and \~90% struvite purity**.[\[15\]](https://www.sciengine.com/parse/pdf/1673-9108/41873E746B4543A6B66D9909A03DDCFF.pdf)
Independent seawater-Mg experiments reported **80–90% P recovery**, with modeled chemical-cost reduction of 30–50% versus pure Mg salts, demonstrating why the desalination Mg stream is relevant as a reagent source.[\[16\]](https://www.sciencedirect.com/science/article/pii/S0043135420301081)
The correct integration is:
**BIO01 anaerobic/biological treatment → nutrient-rich sidestream → struvite crystallization using qualified seawater/brine Mg → polishing → compliant fertilizer or strategic nutrient use**
not “desalination itself creates phosphorus.”
Dongjiakou currently lacks the time-series soluble P and NH₄ mass required to calculate annual struvite output. Therefore **national P import displacement remains zero in the conservative model**.
Strategically, recovered P has a second benefit: every qualified tonne of recycled phosphate reduces both virgin phosphate demand and some associated sulfuric-acid burden.
## 6. N — not an import problem, but a huge efficiency opportunity
China's direct urea imports are currently negligible relative to its domestic fertilizer system.[\[11\]](https://wits.worldbank.org/trade/comtrade/en/country/CHN/year/2025/tradeflow/Imports/partner/ALL/product/310210)
The nitrogen goal is therefore:
- reduce domestic ammonia/urea energy demand;
- reduce coal/gas exposure;
- increase nitrogen-use efficiency;
- reduce NH₃ volatilization, nitrate losses and N₂O;
- recycle N from BIO01;
- use legumes to fix atmospheric N biologically;
- use continuous sensing/AI to dose only where crop demand warrants it.
Recent Chinese field evidence gives a useful range:
- a 2024 study found **25% lower maize N application** in maize-soybean intercropping maintained yield/resource advantage;[\[17\]](https://www.sciencedirect.com/science/article/pii/S0378377424004621)
- a 2026 North China Plain study found **30% less N** in intercropping produced the highest net return and reduced deep nitrate residues;[\[18\]](https://www.sciencedirect.com/science/article/pii/S1161030126002364)
- a 2025–26 evidence base repeatedly shows that moderate N reduction, not zero N, is the robust direction.
This should first be tested against the Dongjiakou/Louis Dreyfus grain-food system rather than extrapolated nationally.
## 7. AGR01 — the demand-side architecture
The agricultural programme should be mechanized regenerative agronomy, not small-plot permaculture.
### 7.1 Proposed system
- maize/soybean strip systems or diversified rotations where machinery and contracts permit;
- wheat rotations appropriate to the existing grain network;
- crop-residue return with measured K balance;
- gypsum only where sodicity/salinity tests show benefit;
- BIO01-derived organic inputs only after contaminant and regulatory gates;
- struvite / recovered phosphate only after product qualification;
- AI soil/water/nutrient monitoring;
- variable-rate N/K/S/P;
- piezo/perovskite soak as a continuous sensing/feedback layer, with catalytic/yield effects treated separately.
<mention-page url="https://app.notion.com/p/3f30c1de73d9814d8c28fd9b190d0b83"/> preserves the instrumentation-first intent.
### 7.2 What the evidence says about diversified grain
A 2025 North China Plain experiment found maize/soybean-wheat systems increased grain-protein yield **14.3%**, reduced net N surplus **14.9%**, cut cumulative N₂O **42.2%**, and reduced net GHG emissions **26%** relative to maize-wheat.[\[19\]](https://www.sciencedirect.com/science/article/abs/pii/S0378429025001510)
A 2026 North China Plain optimization study found integrated maize-soybean management could improve yield **14–17%**, profit **13–36%**, fertilizer partial productivity **8–18%**, and reduce N footprint up to **26%**, while warning that long-term soil nutrient drawdown still requires management.[\[20\]](https://www.sciencedirect.com/science/article/pii/S0308521X26000739)
That warning is exactly why the Atlas design needs nutrient mass accounting rather than “regenerative” labels.
## 8. Quantified strategic dent
### 8.1 Conservative floor
Only one national import offset is counted:
**120 nodes × 25% K inventory sensitivity → 6.1–6.8% of 2024 KCl imports.**
P offset = 0.  
S offset = 0.  
N import offset = 0.  
Straw-return national savings = 0.  
Yield benefit = 0.
Using 2024 average import values for a comparable basket of KCl + crude sulfur + phosphate rock (\~**US\$5.13B**), the K-only floor is roughly **4.5–5.0% of that basket's value**.
This is not “5% of all fertilizer imports.” It is a value-weighted screen of three strategic imported input categories.
### 8.2 Research-bounded expansion
If the **internal-Ca gypsum → sulfuric-acid comparator** survives real brine chemistry and engineering:
- K floor: \~US\$230–256M/y at 2024 average import value;
- S-equivalent research case: \~US\$114–140M/y at 2024 average crude-sulfur import value;
- combined: \~**US\$344–396M/y**, or approximately **6.7–7.7%** of the 2024 KCl + sulfur + phosphate-rock import-value basket.
Still excluded:
- struvite P offset;
- residue-return K savings;
- N reduction;
- smart-fertilization savings;
- any increase in food output;
- any soil-restoration value.
### 8.3 Why the biggest upside may come from denominator reduction
The extraction programme can add millions of tonnes of domestic K-equivalent supply. But Chinese agronomic evidence suggests the country may also be carrying significant **uncredited recycled K** in straw and applying chemical fertilizer without fully netting that internal nutrient flow.
If DeepSeek confirms how much of the 9.25 Mt K residue flow is already reflected in regional fertilizer recommendations and purchases, the denominator-reduction opportunity could rival the brine programme.
That is the single highest-value national AGR01 research question after the Dongjiakou K assay.
## 9. Node-001 → 120-node programme
### Horizon 1 — prove the material loops
**Node-001 objectives:**
1. Obtain time-series W01 feed/concentrate assay for K, Mg, Ca, sulfate and contaminants.
2. Run a K separation pilot and report **actual recovery, purity, energy, reagents and residual fate**.
3. Sample BIO01 nutrient streams for soluble P/N/K/S.
4. Run seawater/brine-Mg struvite pilot.
5. Produce and characterize candidate gypsum/sulfate products.
6. Send gypsum sample into a phosphogypsum-to-acid compatibility study.
7. Establish AGR01 conventional grain baseline: yield, protein, N/P/K/S inputs, straw fate, irrigation, soil EC/SAR/pH, nutrient balance.
8. Run mechanized diversified-crop and precision-fertilization test plots.
### Horizon 3 — replicate only survivors
Replication gates:
- K recovery distribution measured across different brines;
- fertilizer-grade specification and lawful use route;
- no deterioration of marine residuals;
- measured product energy cost;
- direct buyer/state-reserve displacement logic;
- agronomy shows equal-or-better food output per hectare and lower imported/virgin nutrient input;
- sulfur route demonstrates actual acid or direct-S displacement rather than sulfur-equivalent arithmetic.
### Horizon 5 — lattice-scale strategic offset
Only at this point should the programme estimate a national realized offset.
The 120-node numbers in this paper remain **standardized-node scenario arithmetic** until the real node portfolio is characterized. A future 120-node fleet will not have identical desalination flows, brine chemistry or agricultural sinks.
## 10. Strategic reserve doctrine
Recovered strategic material should be allocated in this order:
1. **verified domestic import displacement;**
2. **required operating inventory;**
3. **strategic reserve accumulation;**
4. **internal transformation into higher-value public-good uses;**
5. **market sale only for genuine residual surplus.**
For agriculture:
- K can be stored as qualified potash product where stable.
- P can be stored/used as qualified phosphate/struvite products.
- sulfuric acid itself has handling/storage constraints, so sulfate/gypsum feedstock or contracted conversion capacity may be a safer strategic buffer.
- Mg should not be forced into a commodity market; it can support struvite, Mg/S/K fertilizer formulations where agronomically required, construction materials and CO₂ mineralization.
## 11. What DeepSeek should try to falsify
**Request for independent review:**
1. **Trade denominator:** replace 2024 KCl/sulfur/phosphate figures with any better 2025/2026 commodity-consistent Chinese customs series.
2. **K recovery:** find the strongest measured continuous Chinese SWRO/bittern K-recovery analogue and give recovery, energy, reagent, purity and cost ranges.
3. **Straw K:** determine how much of the reported 9.25 Mt/y residue K is already embedded in current fertilizer purchasing/application; quantify truly incremental chemical-K displacement.
4. **Crop allocation:** estimate what fraction of Chinese KCl fertilizer demand goes to cereals versus high-value crops and other agricultural uses.
5. **Sulfur route:** determine whether SWRO-derived CaSO₄/gypsum can enter Chinese phosphogypsum-to-acid systems without unacceptable purification or energy penalties.
6. **S mass balance:** validate or reject the 62.7–76.9 kt/y gypsum-equivalent Node-001 bound using the modeled Ca inventory and sulfate inventory.
7. **P mass:** find Dongjiakou/LDC/SUEZ nutrient-load evidence sufficient to bound annual struvite output.
8. **Regulation:** identify the exact Chinese product-registration route for struvite and brine-derived K/Mg/S fertilizers.
9. **AGR01 baseline:** identify the actual crop/feedstock mix tied to the Dongjiakou grain/food operation and suitable mechanized rotations.
10. **120-node realism:** replace “120 identical Node-001s” with a Chinese desalination-node distribution and rerun the national offset.
### Preferred response format from DeepSeek
For each challenge:
**Claim → supporting or contradicting source → evidence class → corrected number/range → implication for Node-001 → implication for 120 nodes → confidence.**
Do not promote agreement merely because multiple models converge.
## 12. Bottom line
The corrected thesis is stronger than the original “70% fertilizer imports” premise because it identifies the actual weak points.
**China does not need a generic fertilizer-import replacement programme. It needs targeted fertilizer-input resilience.**
Today the most defensible quantified Atlas contribution is:
> **A 120-node standardized desalination lattice at a deliberately conservative 25%-of-inventory K recovery sensitivity could displace approximately 6.1–6.8% of China's 2024 KCl imports, before crediting any sulfur recovery, phosphorus recycling, crop-residue K, nitrogen reduction, precision fertilization or yield improvement.**
The next credible layer is sulfate/gypsum. Chinese industrial projects prove that gypsum-to-sulfuric-acid is not merely a laboratory concept, but its transfer to desalination-derived gypsum remains unproven.
The potentially transformative layer is the agricultural denominator itself: recover K from water, recover P/N from wastewater, recycle K in crop residue, use Mg to close struvite chemistry, use gypsum/sulfate intelligently, and apply less virgin fertilizer per tonne of grain through crop diversity and AI-guided nutrient management.
> **Self-sufficiency is not one mine, one crystal or one fertilizer. It is a closed nutrient metabolism in which every imported atom has to justify why the locality cannot source, recover, recycle or avoid it domestically.**
---
## Source and internal-work references
- <mention-page url="https://app.notion.com/p/3f30c1de73d981449ee0c735cd9b37cb"/>
- <mention-page url="https://app.notion.com/p/3f20c1de73d981dc8d2dca642e4c049b"/>
- <mention-page url="https://app.notion.com/p/3f20c1de73d98156b6f8e081c4a26f3f"/>
- <mention-page url="https://app.notion.com/p/3f30c1de73d9814d8c28fd9b190d0b83"/>
- <mention-page url="https://app.notion.com/p/3f20c1de73d9813384b8c19463af99a1"/>
