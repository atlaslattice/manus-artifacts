"""Field-research receipt ledger — DeepSeek review round 1.

The review packet asked one question: which of the registered stream edges does
the locality actually have the legal and commercial right to connect? This module
records what came back.

The protocol matters as much as the findings. A **NULL** is a receipt, not a
failure: it says the connection is not yet real, which is more actionable than
assuming it is. A **FOUND-CONTRADICTS** is the most valuable outcome of all,
because it corrects a working assumption before that assumption propagates to
120 localities.

Outcomes:
    FOUND                — the document exists and supports what we assumed
    FOUND-CONTRADICTS    — the document exists and contradicts what we assumed
    NULL                 — searched, not publicly available (a receipt)
    UNKNOWN-BUT-LEAD     — no direct document, but an adjacent lead exists
    UNKNOWN              — searched, indeterminate
"""

from __future__ import annotations

from typing import Any

OUTCOMES = ("FOUND", "FOUND-CONTRADICTS", "NULL", "UNKNOWN-BUT-LEAD", "UNKNOWN")

#: How strongly a receipt may be relied upon in the register.
_EVIDENCE = {
    "FOUND": "REPORTED",
    "FOUND-CONTRADICTS": "REPORTED",
    "NULL": "UNKNOWN",
    "UNKNOWN-BUT-LEAD": "UNKNOWN",
    "UNKNOWN": "UNKNOWN",
}


#: Search terms for receipts whose searches are recorded separately.
#:
#: A NULL without its search terms is not a receipt, because it cannot be
#: reproduced or falsified. These are the queries that returned nothing.
SEARCH_LOG: dict[str, tuple[str, ...]] = {
    "Q-A3": ("董家口 循环经济示范园区 年度报告", "青岛西海岸新区 循环经济 年度报告"),
    "Q-D2": ("董家口 空分 液氮 液氧 供应", "青岛 空分 项目 供气协议"),
    "Q-D3": ("董家口 LNG冷能 二氧化碳 液化", "青岛 冷能 碳捕集"),
    "Q-D4": ("中石化 青岛LNG 冷能 利用", "董家口 LNG 气化 冷能"),
    "Q-E3": ("董家口 增量配电 许可", "青岛 增量配电 试点"),
    "Q-G1": ("路易达孚 董家口 环评", "董家口 食品产业园 废水"),
    "Q-G3": ("董家口 有机废弃物 收运", "青岛 餐厨垃圾 处理 特许经营"),
    "Q-H2": ("董家口 提锂 中试", "董家口 浓盐水 资源化 招标"),
    "Q-H3": ("鲁北 卤水梯级利用", "山东 浓盐水 溴 镁 提取"),
    "Q-H4": ("董家口 海水 水质 报告", "青岛 海水淡化 浓盐水 成分"),
    "Q-I2": ("董家口 绿电直连 数据中心", "青岛港 绿电 算力"),
}


def _r(qid: str, question: str, outcome: str, finding: str, *,
       evidence: str | None = None, source: str = "", date: str = "",
       url: str = "", effect: str = "", tier: int = 1,
       search: tuple[str, ...] = (), round: int = 1) -> dict[str, Any]:
    if outcome not in OUTCOMES:
        raise ValueError(f"undeclared outcome: {outcome}")
    return {
        "qid": qid,
        "round": round,
        "tier": tier,
        "question": question,
        "outcome": outcome,
        "finding": finding,
        "evidence_class": evidence or _EVIDENCE[outcome],
        "source": source,
        "date": date,
        "url": url,
        "effect_on_register": effect,
        "search_terms": list(search or SEARCH_LOG.get(qid, ())),
    }


def receipts() -> list[dict[str, Any]]:
    """Round 1 field research, as returned by the reviewer."""
    return [
        # ================= TIER 1 =================
        _r("Q-A1", "Circular-economy implementation plan", "FOUND",
           "The zone completed compilation of a park circular-transformation implementation plan "
           "and advanced 20 key supporting projects totalling CNY 12.4bn (2024). A 2026 page "
           "confirms 30 circular-transformation projects landed, CNY 69.5bn total, cutting "
           "enterprise tailings treatment cost by over 80%. Targets: industrial water reuse rate "
           ">=94%, general industrial solid waste comprehensive utilisation >=90%. "
           "The publicly available documents do NOT enumerate enterprise-to-enterprise exchanges "
           "with partner names and quantities.",
           source="Dongjiakou Economic Zone government reporting (2024, 2026)",
           effect="Plan EXISTS and sets two hard targets we can measure against. But the "
                  "enterprise-level exchange list is NULL, so the 16 opportunity edges still "
                  "cannot be confirmed or denied from this document alone. The >=94% water reuse "
                  "and >=90% solid waste targets become new measurable commitments.",
           search=("董家口经济区 循环经济 实施方案", "董家口 园区循环化改造")),

        _r("Q-A2", "Park utility map by plant", "NULL",
           "No published steam, hot water, industrial gas or compressed-air utility map by plant "
           "and capacity was located. The zone is described as having achieved 'nine connections "
           "and one levelling' (九通一平) including centralised wastewater treatment, thermal power, "
           "substations and reclaimed-water networks, but the layout and capacities are not public.",
           effect="Heat layer has no physical stream and remains OPPORTUNITY_ONLY. "
                  "The pipes may exist; we cannot see them.",
           search=("董家口经济区 公用工程 管网", "董家口 蒸汽 管网")),

        _r("Q-A3", "Demonstration-zone reporting obligations", "UNKNOWN-BUT-LEAD",
           "The national circular-economy demonstration designation carries reporting obligations, "
           "but the Dongjiakou annual report was not located. The zone is described as a "
           "national-level circular economy demonstration zone.",
           effect="A lead to pursue for the enterprise-level data that Q-A1 did not yield."),

        _r("Q-B1", "Water supply agreement — WHO ACTUALLY BUYS THE WATER", "FOUND",
           "The plant operates under a PPP agreement signed in 2015. Terms: desalinated water "
           "treatment fee CNY 4.25/m3, with a GUARANTEED MINIMUM VOLUME of 70,000 m3/day; below "
           "that, payment is made at the guaranteed volume rate. Named offtakers: Qingdao Special "
           "Steel, Jinneng Chemical, Bangtuo New Materials, and West Coast Water Affairs Company "
           "(which further supplies Haiwan Chemical and Huicheng Environmental Protection). The "
           "Dongjiakou Water Supply Company buys at CNY 4.25/m3 and sells to industrial users at "
           "CNY 4.00/m3 — a policy-driven loss subsidised by the district government.",
           source="PPP agreement terms (2015) via government/utility reporting",
           date="2015",
           effect="DECISIVE. The product water's sink is now CONTRACTED to a named industrial "
                  "cluster, not the port. The port candidacy for product water is not supported. "
                  "Also gives us the first real price anchor in the entire build (CNY 4.25/m3 "
                  "treatment fee, 70,000 m3/day guaranteed minimum) and reveals the tariff is "
                  "subsidy-dependent, which is a financial-risk finding, not just an input.",
           search=("董家口海水淡化 供水协议", "青岛水务海水淡化 供水 合同")),

        _r("Q-B2", "Port and industrial water demand", "UNKNOWN-BUT-LEAD",
           "The plant was designed to supply the zone's industrial water demand; a 2022 report "
           "states maximum daily supply reaches 100,000 t, 'fully able to meet the industrial "
           "water demand within the Dongjiakou Economic Zone'. Per-user demand figures are not published.",
           effect="Supports that the plant is demand-matched, not port-matched. No per-user split.",
           search=("董家口 工业用水 需求",)),

        _r("Q-B3", "2026 effective electricity settlement", "NULL",
           "Historical anchor CONFIRMED: CNY 0.555/kWh including tax for 2018-2020. Shandong policy "
           "confirms the demand/capacity charge waiver for qualifying two-part-tariff desalination "
           "power was in effect through the end of 2025. NO 2026 plant-specific effective tariff, "
           "bill, retail contract or market-settlement receipt was located.",
           evidence="UNKNOWN",
           source="Shandong preferential-tariff policy; no 2026 receipt",
           effect="Progress, not closure. A 2020 anchor now exists but 2026 remains UNKNOWN, so "
                  "every CNY line in Runs 0-3 remains unmeasurable. This stays the highest-value "
                  "missing receipt. NOTE: the demand-charge waiver expiry at end-2025 means the "
                  "2018-2020 figure CANNOT be carried forward — the 2026 shape is genuinely unknown, "
                  "not merely unpublished.",
           search=("董家口海水淡化 电价", "山东 海水淡化 电价 政策 2026")),

        _r("Q-B4", "Whole-site energy audit", "NULL",
           "No published energy audit (能源审计) or cleaner-production audit (清洁生产审核) with a "
           "stated meter boundary. The 2.2 kWh/m3 figure remains process-train only.",
           effect="The true node energy baseline remains unmeasurable. UNKNOWN stays UNKNOWN.",
           search=("董家口海水淡化 能源审计", "青岛水务海水淡化 清洁生产审核")),

        _r("Q-C1", "Discharge permit", "UNKNOWN-BUT-LEAD",
           "Outfall location documented: 'between the west breakwater of Dongjiakou Port and the "
           "eastern section of the trestle pier', at 119°44'33.10\"E, 35°34'47.17\"N. Zone wastewater "
           "is treated at the Zhongfa Water Treatment Plant (total capacity 43,000 m3/day) and "
           "discharged through the outfall after meeting standards. The permit number and permitted "
           "limits were not located in the national permit register.",
           effect="The outfall is now LOCATED with coordinates. INV-19 still lacks the permit "
                  "receipt. A georeferenced discharge point is new and useful.",
           search=("董家口海水淡化 排污许可证", "董家口 排放口")),

        _r("Q-C2", "Concentrate monitoring", "UNKNOWN-BUT-LEAD",
           "A 2024 journal article in Salt Science & Chemical Engineering analysed the environmental "
           "impact of Dongjiakou's desalination concentrate discharge, finding the impact limited to "
           "within 200 m of the outfall and posing no major environmental risk to marine life in "
           "Langya Bay. This is a peer-reviewed SECONDARY analysis, not primary station data.",
           effect="A bounded-impact claim now exists — but the veto rule stands: a secondary "
                  "summary may never be promoted to a primary ecological receipt. INV-19/ECO-01 "
                  "remain UNRESOLVED. The 200 m figure is a hypothesis to test, not a clearance.",
           search=("董家口 海水淡化 浓盐水 监测",)),

        _r("Q-C3", "Primary OUC monitoring data", "NULL",
           "The 2017 and 2022 Ocean University of China monitoring summaries are referenced in "
           "secondary engineering reports, but the underlying primary station-level data was not "
           "located publicly. This remains the critical gap for ECO-01.",
           effect="ECO-01 stays UNRESOLVED. Confirmed that the gap is real and not a search failure.",
           search=("中国海洋大学 董家口 监测",)),

        _r("Q-C4", "Brine diffusion model / outfall EIA", "UNKNOWN-BUT-LEAD",
           "The outfall project received approval from the Shandong Provincial Ocean and Fisheries "
           "Department (鲁海渔函[2015]330号). An EIA for the desalination project exists, but a "
           "specific brine-diffusion model or detailed outfall EIA was not located publicly.",
           source="鲁海渔函[2015]330号", date="2015",
           effect="A named approval instrument now exists — a concrete target for a direct request.",
           search=("董家口 排放口 环评", "鲁海渔函 2015 330")),

        # ================= TIER 2 — D. LNG cold energy =================
        _r("Q-D1", "LNG cascade EIA thermal specifications", "UNKNOWN-BUT-LEAD",
           "The cascade project completed bidding in June 2026 and entered detailed design and "
           "construction, with the projected 26 GWh/year generation and 8 GWh/year avoided cooling "
           "we already carry. The EIA document with thermal output specifications, cold load and "
           "operating hours was not located.",
           tier=2,
           effect="E02 edges stay UNDER_CONSTRUCTION with credit zero. The two projected figures "
                  "remain projections with no stated operating profile.",
           search=("山东 LNG冷能梯级利用 环评", "青岛 董家口 LNG冷能 项目 公示")),

        _r("Q-D2", "Air-separation offtake agreements", "UNKNOWN",
           "The 660 t/day air-separation project (CNY 230M, Sichuan Air Separation Group + Sinopec "
           "Qingdao LNG, signed 2025-09-02) exists, but liquid-gas offtake agreements and buyer "
           "identities were not located.",
           tier=2, effect="E02 to CHEM01 stays UNDER_CONSTRUCTION; the product sink is unknown."),

        _r("Q-D3", "CO2 liquefaction in scope", "UNKNOWN",
           "No public document confirming or denying CO2 liquefaction in the cold-energy project scope.",
           tier=2,
           effect="The E02 to CARB01 potential coupling stays closed. Note: CO2 liquefaction is a "
                  "natural cold-energy use and would be a genuinely elegant link if in scope."),

        _r("Q-D4", "Is the cold energy incremental?", "UNKNOWN-BUT-LEAD",
           "The Sinopec Qingdao LNG receiving station has been operational since 2014. The cascade "
           "project is described as Shandong's first such project, suggesting incremental recovery, "
           "but this was not definitively confirmed.",
           tier=2,
           effect="Supports incrementality but does not prove it. If cold energy were already being "
                  "used for vaporisation duty, the 26 GWh would not be additive."),

        # ================= E. Renewables and green-direct =================
        _r("Q-E1", "Port green transformation plan", "FOUND",
           "The Qingdao Port Green Transformation Three-Year Action Plan (2026-2028) is confirmed. "
           "It proposes exploring green-direct connection and developing wind and solar around "
           "Qianwan and Dongjiakou port areas — approximately 214 MW wind and 81 MW PV — with "
           "dedicated transmission lines. Targets: 20.1 MW wind at Qianwan North by 2027 "
           "(>30 million kWh/year), >=15 MW new distributed PV, and one virtual power plant by 2028.",
           source="Qingdao Port Green Transformation Three-Year Action Plan 2026-2028",
           date="2026-2028",
           effect="E01 to C01 stays PLANNED but is now a NAMED official plan with dated, countable "
                  "targets. The virtual power plant is a new element not previously registered. "
                  "Node-001 access remains UNKNOWN — a plan is not an allocation.",
           search=("青岛港 绿色转型 三年行动方案",)),

        _r("Q-E2", "Green-direct eligibility for this node", "UNKNOWN-BUT-LEAD",
           "National 2026 green-direct rules permit multi-user projects including industrial parks, "
           "with priority support for compute facilities, at thresholds of >=60% self-consumption "
           "and >=30% load share. NO document naming the Dongjiakou desalination plant or any "
           "compute facility as an enrolled user was located.",
           tier=2,
           effect="The POLICY pathway is confirmed; Node-001 participation is UNKNOWN. GRID-01 "
                  "stays UNRESOLVED. Critically: the rules name compute as a priority class, so "
                  "the 40 MW scenario now has a policy route even with no project announced.",
           search=("绿电直连 山东 2026", "董家口 绿电 直连 数据中心")),

        _r("Q-E3", "Incremental distribution licence", "NULL",
           "No incremental distribution licence or energy-storage pilot at Dongjiakou was located.",
           tier=2, effect="Nothing to register. GRID-01 unchanged."),

        # ================= F. Materials, manufacturing, certification =================
        _r("Q-F1", "Pilot base tenant list", "FOUND",
           "The New Materials Technological Innovation Base (200 mu, 8 pilot workshops, capacity for "
           "30 concurrent projects) has 45 material projects in reserve, 9 expressing clear intent to "
           "move in, 12 high-potential projects under weekly tracking, and 4 confirmed for pilot "
           "workshops with equipment installation underway. A military-civilian special carbon fibre "
           "project has been signed. Projects in reserve include low-molecular-weight polyphenylene "
           "ether, carbon black coupling agent, and Shanghai Jiao Tong University high-end materials. "
           "The full tenant list with workshop assignments was NOT published.",
           tier=2,
           effect="M01 is CONFIRMED to have a physical host with real occupancy. But only 4 of 30 "
                  "slots are filled, so M01 capacity is mostly prospective. The carbon fibre and "
                  "polyphenylene ether projects are new named tenants.",
           search=("董家口新材料中试基地 入驻", "董家口 中试基地 项目 名单")),

        _r("Q-F2", "Construction waste allocation", "FOUND-CONTRADICTS",
           "A Qingdao government planning document states explicitly: 'From the perspective of "
           "enterprise layout, the West Coast New Area's key future industrial development zone — "
           "Dongjiakou Economic Zone and its surrounding areas — LACKS construction waste resource "
           "utilisation enterprises.' It recommends arranging one to two reasonably sized processing "
           "facilities in or around the zone.",
           source="Qingdao construction waste resource utilisation planning document",
           effect="THE REGISTER'S ASSUMPTION IS WRONG AND HAS BEEN CORRECTED. We assumed Dongjiakou "
                  "had construction-waste feedstock flowing to M01. It does not — the zone is "
                  "officially identified as a GAP in the city's processing network. The finding "
                  "inverts the edge: this is not a feedstock surplus seeking a sink, it is a "
                  "capability gap that the city plans to fill. Sited correctly, a node facility "
                  "would be the processing enterprise the plan asks for. That is a genuine "
                  "opportunity, but a different one from the one we registered.",
           search=("青岛 建筑废弃物 资源化利用 布局", "董家口 建筑废弃物")),

        _r("Q-F3", "Special steel slag and ZLD", "FOUND",
           "Qingdao Special Steel reports 100% comprehensive utilisation of steel slag through "
           "intelligent closed-loop processing, having invested CNY 76M in a solid slag processing "
           "line producing granular steel, granular iron, iron concentrate and 劈铁 for return to "
           "converter; slag is processed into cement additives and high-value building materials. "
           "For water, SUEZ/Zhongfa operates a 20,000 m3/day industrial wastewater plant with 100% "
           "reclaimed-water reuse for Special Steel production. Contracted volumes and independent "
           "ZLD verification were not located.",
           tier=2,
           effect="MAT01 to M01 slag link strengthened to OPERATIONAL with a named investment. "
                  "The ZLD claim is an OPERATOR CLAIM, not an independent measurement — it must "
                  "not be promoted on the strength of the operator's own reporting.",
           search=("青岛特钢 钢渣 综合利用", "青岛特钢 中水回用")),

        _r("Q-F4", "Tyre pyrolysis carbon black", "FOUND",
           "The Exista Green Ecological Recycling Demonstration Base at Dongjiakou processes 30,000 "
           "tonnes/year of waste tyres, producing primary oil, environmentally friendly carbon "
           "black, steel wire and combustible gas — described as 'zero pollution, zero residue, "
           "zero emissions, full utilisation'. Carbon black grade, offtake volumes and buyer "
           "identities were not located.",
           tier=2,
           effect="MAT01 to M01 tyre-pyrolysis link confirmed OPERATIONAL at 30,000 t/year. Carbon "
                  "black is a candidate 3D-printing composite feedstock, which is a NEW coupling "
                  "not previously registered. The 'zero emissions' claim is unverified marketing "
                  "language and is registered as such.",
           search=("双星 废旧轮胎 裂解 董家口",)),

        _r("Q-F5", "3D-printing certification for marine/pressure parts", "FOUND-CONTRADICTS",
           "China HAS established a concrete 3D-printing standards framework: T/CBMF 378-2026 / "
           "T/CCPA 90-2026 'General Technical Requirements for Concrete 3D Printers' (effective "
           "2026-09-06); T/CCPA 85-2025 / T/CBMF 366-2025 '3D Printing Concrete Premix'; and a "
           "national standard under development, 'Additive Manufacturing in Construction — "
           "Qualification Principles — Structural and Infrastructure Components', based on "
           "ISO/ASTM 52939:2023. HOWEVER, no classification-society (船级社) or pressure-vessel code "
           "pathway for additively manufactured marine or pressure-boundary components was located.",
           tier=2,
           effect="SCOPE REFINEMENT, and a partial contradiction of our framing. CERT-01 is not "
                  "blocking all additive manufacturing — concrete structural printing has a real "
                  "and current standards path. The veto's true scope is NARROWER AND SHARPER: it "
                  "applies to marine and pressure-boundary components only. CERT-01 remains "
                  "UNRESOLVED for that narrower scope.",
           search=("增材制造 船级社 认证", "3D打印混凝土 标准 T/CBMF")),

        # ================= G. Food, organics, nutrients =================
        _r("Q-G1", "LDC wastewater and residues", "UNKNOWN-BUT-LEAD",
           "The Louis Dreyfus Food Technology Park EIA is referenced in procurement notices, but "
           "wastewater volume and composition were not located publicly.",
           tier=2, effect="AGR01 to BIO01 edge stays UNDER_CONSTRUCTION with composition UNKNOWN."),

        _r("Q-G2", "Wastewater treatment and reclaimed water", "FOUND",
           "The Zhongfa Water Treatment Plant (SUEZ) serves Dongjiakou with 20,000 m3/day industrial "
           "wastewater treatment and 5,000 m3/day municipal treatment. 100% of treated water is "
           "reused by Qingdao Special Steel for production. The zone has a reclaimed-water reuse "
           "network as part of its 'nine connections and one levelling' infrastructure. Daily inflow "
           "to the main line is approximately 3,000-4,000 m3/day, and the secondary line "
           "11,300-31,500 m3/day.",
           tier=2,
           effect="BIO01 now has an OPERATIONAL treatment host with stated capacities, and a real "
                  "reuse loop already exists (Special Steel at 100%). Note the loop is ALREADY "
                  "CLAIMED by Special Steel — so a 100% reuse claim cannot also be attributed to "
                  "another subnode. That is exactly the kind of double count the credit rule exists "
                  "to prevent.",
           search=("中法水务 董家口 污水处理", "董家口 中水回用")),

        _r("Q-G3", "Organic waste concession", "UNKNOWN-BUT-LEAD",
           "The Zhongfa plant has a sludge composting project (楼山河污泥堆肥项目) with civil works "
           "complete, and a 2014 QTV report describes a kitchen-waste pretreatment system producing "
           "biogas and fertiliser. No BIO01-contractable organic waste concession at Dongjiakou was "
           "identified.",
           tier=2, effect="A lead only. No concession to contract into yet."),

        # ================= H. Resource extraction =================
        _r("Q-H1", "Baifa lithium — real status", "FOUND",
           "The Baifa seawater lithium extraction project (world's first) completed two pilot rounds "
           "processing 200,000 tonnes of seawater using a high-selectivity ion sieve effective at "
           "0.17 ppm Li. A patent for a 'lithium ion sieve-based double-layer ultrafiltration "
           "membrane' was filed in August 2024 by the Qingdao Institute of Bioenergy and Bioprocess "
           "Technology (CAS) and Qingdao Baifa Seawater Desalination Co., and published February "
           "2026. Commercial operation was expected by end of 2025. Actual 2026 operating status and "
           "product buyers were NOT confirmed.",
           source="CAS Qingdao Institute of Bioenergy and Bioprocess Technology + Qingdao Baifa "
                  "patent, filed 2024-08, published 2026-02",
           date="2024-2026",
           effect="A credible proof-of-path with an identifiable IP holder and a named research "
                  "partner — which is also a direct route to ask for the missing data. But the "
                  "register still cannot promote R01: expectation of commercial operation is not "
                  "operation, and 2026 status is unconfirmed. R01 credit stays zero.",
           search=("百发海水淡化 提锂 离子筛", "青岛 海水 提锂 专利 2026")),

        _r("Q-H2", "Dongjiakou-specific extraction pilot", "NULL",
           "No Dongjiakou-specific lithium, uranium, deuterium or trace-resource pilot, tender or "
           "research agreement was located.",
           tier=2,
           effect="R01 remains a candidate coupling only. There is no site-specific extraction "
                  "activity to register."),

        _r("Q-H3", "Lubei brine cascade reference", "UNKNOWN-BUT-LEAD",
           "Lubei is referenced in a Shandong policy document as operating a 'brine cascade "
           "utilisation' model extracting bromine and magnesium from concentrated brine, forming a "
           "'technology + resource recycling' model. Specific material-flow data was not located.",
           tier=2,
           effect="Remains REFERENCE_ONLY — a design analogue from another site, never credited "
                  "at Dongjiakou."),

        _r("Q-H4", "Dongjiakou brine chemistry assay", "NULL",
           "No published brine chemistry (ion concentrations in feed, product and concentrate) for "
           "Dongjiakou was located. The R01 transfer functions remain parameterised on generic "
           "seawater values.",
           tier=2,
           effect="R01-Li and R01-D stay MODELED on generic values. A site assay remains the "
                  "single cheapest experiment that would convert R01 from model to fact."),

        # ================= I. Compute =================
        _r("Q-I1", "Data centre projects at Dongjiakou", "UNKNOWN-BUT-LEAD",
           "A public procurement notice lists a 'Dongjiakou Economic Zone 2026 Smart Park O&M Service "
           "Project'; a separate tender for a 'Public Pipe Gallery Smart Operation Platform' includes "
           "one data centre with hardware and platform software, a 45 m2 server room and a command "
           "centre. A 2026 news article mentions a municipal state-owned enterprise responsible for "
           "green data centre O&M and computing platform expansion receiving financing in the "
           "Dongjiakou context. No 40 MW-scale data centre or 智算中心 project was confirmed.",
           tier=2,
           effect="Small-scale compute EXISTS but at 45 m2 it is two orders of magnitude below the "
                  "40 MW scenario. Registering this honestly: the locality has an operations-grade "
                  "server room, not a compute campus. The 40 MW scenario remains a scenario.",
           search=("董家口 数据中心 招标", "董家口 智算中心")),

        _r("Q-I2", "Direct-green for compute", "UNKNOWN-BUT-LEAD",
           "National policy gives priority support to compute facilities under green-direct rules, "
           "and the Qingdao Port plan proposes green power for the port area. No document connects a "
           "Dongjiakou compute load to a direct-green supply arrangement.",
           tier=2, effect="No change. C01 remains a load with no supply contract."),

        # ================= ROUND 2 — five targeted follow-ups =================
        _r("Q-B1-2", "PPP contract terms and the take-or-pay clause", "FOUND-CONTRADICTS",
           "Terms confirmed via a Qingdao Water Beiyuan bond prospectus — a SECONDARY disclosure "
           "of the PPP, not the contract text, which is referenced "
           "(《青岛董家口经济区海水淡化政府和社会资本合作项目合作合同》) but not published. "
           "Signed 2015-11-20 between the Dongjiakou EDZ Management Committee and Qingdao Water "
           "Beiyuan Technology Development Co. Concession 30 years. Construction 10 months. "
           "Commercial operation 2017-01-01. Water price CNY 4.25/m3. Take-or-pay minimum "
           "70,000 m3/day with the government paying the shortfall. 2019 actual throughput "
           "31,500 m3/day; 2019 revenue CNY 106M and net profit CNY 22M. 2019 offtakers were "
           "Qingdao Special Steel and Huaneng Group; the 2025 list has since evolved. "
           "CONTRADICTION: total investment is CNY 450M in the bond prospectus but CNY 900M in a "
           "2015 tender notice — possibly different scopes (plant only vs plant plus membrane "
           "R&D base). Both are retained with dates.",
           source="Qingdao Water Beiyuan bond prospectus, chinamoney.com.cn",
           date="2015-2020",
           round=2,
           effect="The take-or-pay clause is now CONFIRMED BINDING across every year we can see "
                  "(31,500 m3/day in 2019, 49,123 in 2025, against a 70,000 guarantee). A 30-year "
                  "concession means the contract outlives most planning horizons. Still NOT "
                  "obtained: the contract text, escalation clauses, and subsidy-withdrawal "
                  "provisions — which is precisely where the risk sits.",
           search=("董家口 海水淡化 PPP 合同", "青岛水务北苑 债券 募集说明书")),

        _r("Q-B3-2", "2026 electricity settlement — reconfirmation", "NULL",
           "Confirmed as a document that does NOT EXIST in the public record. Confirmed context: "
           "CNY 0.555/kWh incl. tax granted by the Shandong Price Bureau for 2018-2020 "
           "specifically for the Baifa and Dongjiakou projects; a 2022 policy document confirms "
           "Qingdao 'secured preferential electricity price policies' for both, with a maximum "
           "CNY 10M award under the desalination construction incentive scheme; a 2023 industry "
           "article states CNY 0.55/kWh and per-tonne water treatment electricity cost below CNY 2.",
           evidence="UNKNOWN",
           round=2,
           effect="The critical path has moved from search to INSTITUTIONAL REQUEST. This is now "
                  "the single most valuable missing receipt in the build, and it cannot be "
                  "obtained by searching. Note the 2023 claim of sub-CNY-2/tonne electricity "
                  "cost is CONSISTENT with the 2.2 kWh/m3 process figure at CNY 0.55-0.90/kWh, "
                  "so it does not by itself resolve the whole-site boundary question.",
           search=("董家口海水淡化 电费 结算 2026", "山东 海水淡化 电价 政策 2026")),

        _r("Q-A1-2", "Circular-transformation plan project annex", "FOUND-CONTRADICTS",
           "The plan exists and targets are confirmed (industrial water reuse >=94%, general "
           "industrial solid waste comprehensive utilisation >=90%), with cooperation with CAS "
           "teams on smart park design. The PROJECT ANNEX listing the specific projects with "
           "partner names and quantities is NOT published. CONTRADICTION: a 2024 source reports "
           "20 projects / CNY 12.4bn, while a 2026 government page reports 30 projects / "
           "CNY 69.5bn. Additional phases, a broader scope, or a different counting basis are all "
           "possible. Both retained with dates, unreconciled.",
           source="Dazhong Daily 2024-03-06; Baidu Baijiahao 2024-02-28; government page 2026",
           date="2024-2026",
           round=2,
           effect="The annex remains the document that would open the 16 opportunity edges. It is "
                  "likely internal. Route: direct request to the Dongjiakou EDZ Management "
                  "Committee (经济发展部). The two hard targets are now measurable commitments we "
                  "can hold the zone to.",
           search=("董家口 园区循环化改造 项目 名单", "青岛 循环化改造 重点项目 清单")),

        _r("Q-H4-2", "CAS Qingdao Institute — patent and contact pathway", "FOUND",
           "Patent CONFIRMED: CN121446313A, '一种锂离子筛基双层超滤膜及其制备方法和应用'. Applicants: "
           "中国科学院青岛生物能源与过程研究所 and 青岛百发海水淡化有限公司. Filed 2024-08-02, "
           "published 2026-02-03. Abstract describes a lithium ion sieve-based double-layer "
           "ultrafiltration membrane made by dry-wet spinning phase inversion, integrable into "
           "lithium-rich natural water treatment systems for simultaneous water separation and "
           "lithium adsorption. Research group led by Gao Jun (高军) at the Bionic Energy Interface "
           "Technology Research Center, with collaborators Sui Xin and Liu Xueli at Qingdao "
           "University, publishing on bioinspired ion sieving for Li/Mg separation.",
           source="CN121446313A; CAS Qingdao Institute of Bioenergy and Bioprocess Technology",
           date="2024-2026",
           round=2,
           effect="The brine-chemistry question now has a NAMED INSTITUTION, a NAMED RESEARCH "
                  "GROUP and a CONTACT PATHWAY. This converts R01 from an unattended gap into a "
                  "specific approach. The patent and group are REPORTED; the brine chemistry "
                  "itself remains UNKNOWN pending response.",
           search=("CN121446313A", "中科院青岛生物能源与过程研究所 锂离子筛")),

        _r("Q-C4-2", "鲁海渔函[2015]330号 — the outfall instrument, and a critical distinction",
           "FOUND",
           "Instrument FOUND and named: 《关于董家口港区尾水排海管道工程路面的批复》, Shandong "
           "Provincial Department of Ocean and Fisheries, 2015. Outfall between the west breakwater "
           "of Dongjiakou Port and the eastern trestle section, 119°44'33.10\"E, 35°34'47.17\"N "
           "(CGCS2000). The citing EIA also confirms the outfall serves the Zhongfa Water "
           "Treatment Plant, total capacity 43,000 m3/day (main line 11,000 + side line 32,000). "
           "CRITICAL DISTINCTION: this is the WASTEWATER (尾水) outfall, NOT necessarily the "
           "DESALINATION CONCENTRATE outfall. The brine discharge may use a separate pipeline or "
           "share this one. Which is not established. Full text and permitted limits not obtained.",
           source="Jinneng Chemical EIA report 2023-08-22, citing 鲁海渔函[2015]330号",
           date="2015, cited 2023",
           round=2,
           effect="RAISES A QUESTION ABOUT OUR OWN EVIDENCE. If the brine discharge uses a "
                  "separate outfall, then the 2024 secondary study reporting impact 'within 200 m "
                  "of the outfall' may describe the WRONG outfall, and INV-19 would rest on a "
                  "document that does not cover the stream it was cited for. This does not change "
                  "the veto state — it changes how weak the evidence beneath it is. Escalated for "
                  "adversarial review rather than resolved unilaterally.",
           search=("鲁海渔函 2015 330", "董家口 尾水排海 管道 批复")),
    ]


# ---------------------------------------------------------------------------
# Derived views
# ---------------------------------------------------------------------------
def outcome_counts() -> dict[str, int]:
    counts = {o: 0 for o in OUTCOMES}
    for r in receipts():
        counts[r["outcome"]] += 1
    return counts


def by_outcome(outcome: str) -> list[dict[str, Any]]:
    return [r for r in receipts() if r["outcome"] == outcome]


def contradictions() -> list[dict[str, Any]]:
    """Assumptions the research actively overturned. The most valuable outcome."""
    return by_outcome("FOUND-CONTRADICTS")


def nulls() -> list[dict[str, Any]]:
    """Receipts of absence — the connection is not yet real."""
    return by_outcome("NULL")


def register_relevant() -> list[dict[str, Any]]:
    """Receipts that actually change an edge, a veto or a number."""
    return [r for r in receipts() if r["effect_on_register"]]


def round_summary() -> dict[str, Any]:
    rs = receipts()
    r1 = [r for r in rs if r["round"] == 1]
    r2 = [r for r in rs if r["round"] == 2]

    def _counts(items: list[dict[str, Any]]) -> dict[str, int]:
        c = {o: 0 for o in OUTCOMES}
        for r in items:
            c[r["outcome"]] += 1
        return c

    return {
        "rounds": 2,
        "reviewer": "DeepSeek",
        "questions_asked": 35,
        "questions_answered": len(rs),
        "round_1": {"asked": 30, "answered": len(r1), "outcomes": _counts(r1)},
        "round_2": {"asked": 5, "answered": len(r2), "outcomes": _counts(r2)},
        "outcomes": outcome_counts(),
        "found": [r["qid"] for r in by_outcome("FOUND")],
        "contradictions": [r["qid"] for r in by_outcome("FOUND-CONTRADICTS")],
        "nulls": [r["qid"] for r in by_outcome("NULL")],
        "leads": [r["qid"] for r in by_outcome("UNKNOWN-BUT-LEAD")],
        "interpretation": (
            "The review CONFIRMED several real links (contracted water offtake, operational slag "
            "and tyre-pyrolysis reuse, the official 214 MW wind + 81 MW PV plan, the pilot base and "
            "its partial occupancy), EXFOUND one contradiction that corrected a working assumption "
            "(construction waste), NARROWED one veto's scope (CERT-01 applies to marine and "
            "pressure-boundary components, not to concrete structural printing, which has a "
            "current standards path), and left the single highest-value economic figure genuinely "
            "NULL (the 2026 electricity settlement). Nine NULLs are receipts of absence: those "
            "connections are not yet real."
        ),
        "discipline_note": (
            "No finding was promoted on the strength of a model agreeing with another model. "
            "Findings are credited when a document is produced. A plan is not an allocation, an "
            "operator claim is not an independent measurement, and an expectation of commercial "
            "operation is not operation."
        ),
    }
