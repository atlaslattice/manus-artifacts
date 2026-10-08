STATUS: ARCHIVE PUBLIC CANDIDATE | CANON: no | DEPLOYMENT: no | AUTHORITY: none | PROOF: no | PUBLIC_RELEASE: candidate

Recovered historical Manus artifact. Current review decisions: [build/review/EVIDENCE_APPENDIX.md](https://github.com/atlaslattice/manus-artifacts/blob/master/public_candidate_bundle_0001/nodes/dongjiakou_node_001/build/review/EVIDENCE_APPENDIX.md).

# White Paper — Dongjiakou Locality Node: Contractual Reality Review Packet

**Document ID:** DJK-LATTICE-DEEPSEEK-CONTRACTUAL-REALITY-REVIEW-v0.1
**Prepared by:** Manus (S6 — Continuity, Execution, and Archive Hygiene)
**For:** DeepSeek, as the primary field-research reviewer
**Status:** REQUEST FOR REVIEW — **NON-CANON, NON-DEPLOYABLE**
**Date:** 2026-10-06
**Repo:** `atlaslattice/manus-artifacts`
**Public Git baseline:** `4756036f9c428fa3aa1d4cea552ae03367523fb5`
**Working head:** `s6/node-001-pilot-simulator` (not yet pushed; GitHub connector blocked on 2FA)

---

## 1. The ask, stated plainly

We have mapped the **physics** of the Dongjiakou locality node. We now need the
**contractual reality**.

Specifically: **which of the 22 registered stream edges does the locality actually
have the legal and commercial right to connect?**

The register currently contains **22 edges: 6 physical** (what flows today) and
**16 opportunity** (what could flow). **Zero of them realize credit.** Every one
of the 16 opportunity edges is blocked on one of two things: a physical receipt,
or a **document that tells us whether the connection is permitted and contracted
at all**.

That second category is where you are the best available resource, and that is
what this packet asks for.

> The node is not limited by physics. It is limited by five unresolved vetoes and
> the absence of contractual evidence. Physics is mapped. Contractual reality is
> next.

---

## 2. Where the build stands

### 2.1 The locality node

Dongjiakou is modelled as a **locality-scale parent node**, not a desalination
plant. Fifteen subnodes are declared:

```
W01 water · C01 compute · P01 port · E01 grid · E02 LNG cold cascade
R01 resource extraction · BIO01 organics · M01 additive manufacturing
MAT01 materials · CHEM01 chemicals · AGR01 food/ag · CARB01 carbon
ECO01 ecology · GOV01 provenance · EXT01 external boundary
```

### 2.2 The credit rule that governs every answer

```
realized_credit  requires
    edge_state    == MEASURED_PHYSICAL
AND evidence_class == MEASURED
AND primary_credit_owner is valid
```

**Nothing is credited on the strength of a plan, a projection, a signature or a
reference from another site.** A stream may be counted once, by one owner;
everyone else receives a bounded allocation under `sum(allocations) ≤ measured
quantity`.

### 2.3 The five unresolved vetoes

| Veto | What it requires |
| --- | --- |
| `INV-19` | Downstream water quality must not deteriorate |
| `ECO-01` | Coastal/ecological status measured at primary level, not secondary summaries |
| `CERT-01` | Pressure-boundary and marine components must be certified |
| `CARB-01` | Transferred CO₂ counted once, never double-claimed |
| `GRID-01` | Renewable attributes not claimed by node, generator and PPA buyer simultaneously |

```
NODE_PASS = AND(all vetoes pass)  →  NOT_ESTABLISHED
```

An **unresolved** veto is not a **pass**, and it is not a **fail** either. It is an
absence of evidence. Closing them is the critical path.

---

## 3. How to answer — the review protocol

For **each** question below, please return one of four outcomes:

| Outcome | Meaning |
| --- | --- |
| **FOUND** | The document exists. Give title, publisher, date, URL, and the specific figures or clauses that answer the question, quoted. |
| **FOUND-CONTRADICTS** | A document exists and it **contradicts** what our register assumes. Say so directly — this is the most valuable outcome. |
| **NULL** | You searched and no such document is publicly available. **This is a receipt, not a failure.** A search that returns UNKNOWN is still an experiment with a result. State the searches you ran so the null is reproducible. |
| **UNKNOWN-BUT-LEAD** | No direct document, but you found an adjacent lead (a tender notice, an EIA notice board entry, a company filing, a news item with a number). Give the lead and label it clearly as a lead, not a finding. |

**Rules for your response:**

1. **Distinguish document classes explicitly.** An EIA notice, a signed contract,
   a tender award, a government plan, a company press release and a news report
   are five different evidence strengths. Label each.
2. **Give the year.** A 2021 figure and a 2026 figure are different facts.
3. **Distinguish plan from contract from operation.** "Planned", "signed",
   "under construction" and "operating" are four different states and we track
   them separately.
4. **Do not fill gaps by inference.** If a document says 345,000 m³/day for a
   locality and 100,000 m³/day for one plant, do not compute the remainder and
   present it as a plant capacity.
5. **Report disagreement rather than resolving it.** If two sources conflict,
   give both with dates. We retain disagreements in the register.
6. **Prioritise Chinese-language primary sources** — government portals, EIA
   notice boards, procurement platforms (公共资源交易平台), utility disclosures,
   company annual reports — over English secondary reporting.

---

## 4. The questions

### TIER 1 — these unblock the most

#### A. The circular-economy plan (governance; unlocks the whole opportunity graph)

**Q-A1.** Does the Dongjiakou Economic Zone have a published circular-economy
implementation plan — 董家口经济区循环经济实施方案, 园区循环化改造方案, or the
国家循环经济示范园区 designation dossier? **Does it enumerate specific
enterprise-to-enterprise material, energy, water or waste exchanges, with partner
names and quantities?**

- *Why it matters:* This single document decides which of the 16 opportunity
  edges are real. It is the highest-value item on this list.
- *Search:* `董家口经济区 循环经济 实施方案`, `董家口 园区循环化改造`,
  `青岛西海岸新区 循环经济示范园区 方案`, `董家口 产业链 循环 名单`

**Q-A2.** Is there a published **park utility map** — steam, hot water, industrial
gas, compressed air, wastewater, reclaimed water — by plant and by capacity?
(蒸汽管网 / 工业气体管网 / 污水处理 / 中水回用)

- *Why it matters:* Three layers (Heat, Carbon, Pollution) currently have no
  physical stream because we cannot see the utility network.
- *Search:* `董家口经济区 公用工程 管网`, `董家口 蒸汽 管网 规划`,
  `青岛董家口 集中供热 供气`

**Q-A3.** What are the reporting obligations attached to the national
circular-economy demonstration designation, and is there a published annual
report?

#### B. Water offtake and the plant's own boundary (W01)

**Q-B1.** Is there a public **water supply agreement** between the Dongjiakou
desalination plant and any specific offtaker — the port, an industrial user, or
the municipal network? **Volumes, duration, price?**

- *Why it matters:* We know the plant produced 17.93 Mm³ in 2025. We do **not**
  know that the port is its sink. This closes `S-W01-P01-C1` one way or the other.
- *Search:* `董家口海水淡化 供水协议`, `青岛水务海水淡化 供水 合同`,
  `董家口 淡化水 用户`, `青岛 海水淡化 管网 供水`

**Q-B2.** What is Dongjiakou's **port and industrial water demand** in m³/day, from
published sources? And municipal demand served by desalination?

**Q-B3.** *(Standing ask.)* What is the **2026 effective electricity settlement
for this plant** — the actual tariff, including any Shandong preferential or
demand-charge treatment?

- *Why it matters:* This single figure converts every current CNY line in Runs 0–3
  from UNKNOWN to measurable. It is the highest-value number in the entire build.
- *Search:* `董家口海水淡化 电价`, `青岛 海水淡化 用电 优惠`,
  `山东 海水淡化 电价 政策 2026`, `青岛水务 海水淡化 电费`

**Q-B4.** Is there a published **energy audit** (能源审计), **cleaner production
audit** (清洁生产审核) or **energy management report** for the plant giving
whole-site annual kWh with a stated meter boundary?

- *Why it matters:* 2.2 kWh/m³ is the UF+RO **process train**, not the whole site.
  The true node baseline is currently unmeasurable.
- *Search:* `董家口海水淡化 能源审计`, `青岛水务海水淡化 清洁生产审核`,
  `海水淡化 综合能耗 报告`

#### C. Discharge, permit and ecology — the `INV-19` and `ECO-01` vetoes

**Q-C1.** What is the plant's **discharge permit** (排污许可证)? Permit number,
issuing authority, permitted limits, monitoring requirements. Is it published in
the national permit register? (全国排污许可证管理信息平台)

- *Why it matters:* This is the entry point to `INV-19`. A permit is not proof of
  compliance, but it establishes what is permitted and what is monitored.

**Q-C2.** Are **concentrate/brine monitoring reports** (浓盐水监测报告,
海水淡化 排放监测) published, on any cadence?

**Q-C3.** The Ocean University of China (中国海洋大学) produced 2017 and 2022
follow-up monitoring summaries. **Is the underlying primary station-level data
available anywhere**, or only the summaries?

- *Why it matters:* `ECO-01` is `UNRESOLVED` precisely because we only hold
  secondary summaries. Veto rule: a secondary summary may never be promoted to a
  primary ecological receipt.

**Q-C4.** Is there a published **brine diffusion model** or outfall EIA
(环境影响评价) for the discharge?

- *Search:* `董家口海水淡化 排污许可证`, `青岛 海水淡化 浓盐水 监测`,
  `董家口 排放口 环评`, `青岛 海水淡化 环境影响评价`

---

### TIER 2 — these unlock specific layers

#### D. LNG cold energy (E02) — the largest single opportunity edge

Our register carries the cascade as
`VERIFIED_PROJECT / UNDER_CONSTRUCTION / CURRENT_CREDIT_ZERO`, with **26 GWh/year
projected generation** and **8 GWh/year projected avoided cooling**. Reporting
says bidding completed June 2026 with the project entering detailed design and
construction.

**Q-D1.** Is the **EIA** (环境影响评价) for the cold-energy cascade project
published? What are the **thermal output specifications, the cold load, and the
assumed annual operating hours**?

- *Why it matters:* It converts two projected numbers into a defensible profile.
- *Search:* `山东 LNG冷能梯级利用 环评`, `青岛 董家口 LNG冷能 项目 公示`,
  `山东首个 LNG冷能梯级利用 环评`

**Q-D2.** The air-separation project (≈660 t/day, liquid nitrogen/oxygen/argon,
¥230M, Sichuan Air Separation Group + Sinopec Qingdao LNG, signed 2025-09-02):
**are there liquid-gas offtake agreements, and who are the buyers?**

**Q-D3.** Is **CO₂ liquefaction** in the project scope? (It is a natural
cold-energy use and would connect E02 to CARB01.)

**Q-D4.** Is Sinopec Qingdao LNG's cold energy otherwise already used — for
example for vaporisation duty — such that the 26 GWh is genuinely incremental?

#### E. Renewables and green-direct (E01) — the `GRID-01` veto

**Q-E1.** The **Qingdao Port Green Transformation Three-Year Action Plan
(2026–2028)** proposes ~214 MW wind and ~81 MW PV around Qianwan and Dongjiakou,
with green-direct implementation targeted by 2028. **What are the site,
timeline, ownership and connection arrangements?**

**Q-E2.** Under the 2026 national green-direct (绿电直连) rules — multi-user
projects, ≥60% self-consumption, ≥30% load share rising to 35% by 2030 —
**is a desalination plant or a compute facility at Dongjiakou an eligible load?**

- *Why it matters:* This is the explicit unlock condition for the 40 MW compute
  scenario, and for `GRID-01`.
- *Search:* `绿电直连 山东 2026`, `青岛港 绿色转型 三年行动方案`,
  `董家口 绿电 直连 数据中心`

**Q-E3.** Is there an **incremental distribution licence** (增量配电业务许可证)
or energy-storage pilot at Dongjiakou?

#### F. Materials and additive manufacturing (MAT01, M01) — the `CERT-01` veto

**Q-F1.** The **Dongjiakou New Materials pilot base** (新材料中试基地, ~¥700M,
~200 mu, 8 pilot workshops, capacity for 30 concurrent projects): **what is the
tenant list, and which workshops or slots are materials, recycling or additive
manufacturing?**

- *Why it matters:* This is the physical host for M01 and the material-validation
  path.
- *Search:* `董家口新材料中试基地 入驻`, `董家口 中试基地 项目 名单`,
  `青岛西海岸新区 新材料 中试 企业`

**Q-F2.** Is Dongjiakou allocated a **specific quota of construction waste**
(建筑废弃物) under Qingdao's 61-processor, 109.4 Mt/yr processing system? Which
processors serve the zone?

**Q-F3.** **Qingdao Special Steel (青岛特钢):** the slag-to-Runyi-Fengtai link and
the SUEZ/Zhongfa water reuse (zero liquid discharge) — **what are the contracted
volumes, and is the ZLD claim independently verified anywhere?**

**Q-F4.** **Doublestar (双星) tyre pyrolysis:** carbon black grade, offtake
volumes and buyers? (Carbon black would be a raw feedstock for 3D-printing
composites.)

**Q-F5.** *(CERT-01 specific.)* Is there any Chinese certification pathway —
GB standard, 船级社 (classification society) approval, or 压力容器 code — under
which an **additively manufactured marine or pressure-boundary component** could
be accepted? **If no such pathway exists, that is the finding we need.**

#### G. Food, organics and nutrients (AGR01, BIO01)

**Q-G1.** The **Louis Dreyfus Food Technology Park** (153,000 m², 1.5 Mt/yr feed
protein, 370 kt/yr refined oil, 15 kt/yr lecithin, completion 2027): does its
**EIA** state **wastewater volume and composition**, residue streams and solid
waste handling?

**Q-G2.** What wastewater treatment capacity serves Dongjiakou, who operates it,
and is there a published **reclaimed water reuse network** with volumes?

**Q-G3.** Is there an **organic waste collection or composting concession** at
Dongjiakou that a BIO01 loop could contract into?

#### H. Resource extraction (R01) — the lithium and deuterium lanes

**Q-H1.** The **Baifa (百发) seawater lithium project** is reported as the world's
first seawater lithium extraction: two pilot rounds processing 200,000 t of
seawater, a high-selectivity ion sieve working at 0.17 ppm Li, battery-grade
lithium carbonate, with commercial cooperation scheme completed. **Is it
operating as of 2026? Who supplies the ion sieve? Who buys the product?**

- *Why it matters:* It is the closest proof-of-path. But Baifa yield must **not**
  be transferred blindly to Dongjiakou chemistry.

**Q-H2.** Is there any **Dongjiakou-specific** lithium, uranium, deuterium or
trace-resource pilot, tender or research agreement?

**Q-H3.** **Lubei (鲁北)** operates a mature cascading-brine scheme. Is there a
published **卤水梯级利用** scheme with material flows we can learn from as a
design reference? (Reference only — never credited at Dongjiakou.)

**Q-H4.** Is there any published **brine chemistry** for Dongjiakou — actual ion
concentrations in feed, product and concentrate?

- *Why it matters:* R01-Li and R01-D currently return transfer functions
  parameterised on generic seawater values. A site assay converts them to facts.
- *Search:* `董家口 海水 水质 报告`, `青岛 海水淡化 浓盐水 成分`,
  `百发海水淡化 提锂 离子筛`

#### I. Compute and the 40 MW question (C01)

**Q-I1.** Are there announced **data centre or 算力 projects at Dongjiakou** —
智算中心, 数据中心, 边缘计算 — at any stage?

**Q-I2.** Is any **direct-green or dedicated supply arrangement** proposed for a
compute load at Dongjiakou?

- *Why it matters:* A 40 MW subnode would draw **438 GWh/year** at the PUE 1.25
  reference — about **11× the plant's entire 2025 process energy**. That is a
  legitimate future locality scenario, but it is gated on green-direct
  eligibility, not on the existence of nearby renewables.

---

## 5. What each answer unlocks

| Answer | Effect on the register |
| --- | --- |
| Tier 1-A (circular-economy plan) | Reclassifies opportunity edges to `CONTRACTED` or `PLANNED`, or deletes them entirely |
| Tier 1-B3 (2026 tariff) | Converts the **entire current CNY column** from UNKNOWN to measurable |
| Tier 1-B4 (whole-site SEC) | Establishes the true node energy baseline |
| Tier 1-C1/C3 (permit, primary data) | Moves `INV-19` and `ECO-01` from UNRESOLVED toward PASS or FAIL |
| Tier 2-D1 (cascade EIA) | Converts two projected GWh figures into a stated operating profile |
| Tier 2-E2 (green-direct) | Unlocks the 40 MW scenario and `GRID-01` |
| Tier 2-F5 (certification pathway) | Resolves or fails `CERT-01` — a veto either way |
| Tier 2-H4 (brine assay) | Turns R01 transfer functions into measured values |

**Note the asymmetry.** A **FOUND** answer may allow a stream to be credited. A
**NULL** answer does not fail the project — it tells us the connection is not yet
real, which is equally actionable and considerably more honest than assuming it.

---

## 6. What we are **not** asking

To keep scope clean, we are **not** asking you to:

- estimate any quantity that no document states;
- convert a locality aggregate into plant capacities;
- rank the locality's potential or produce a single score — **the optimizer is a
  Pareto front, not a scalar score**, and a scalar is exactly what lets a local
  failure be washed out by a gain elsewhere;
- endorse the programme, the architecture, or any deployment;
- reconcile conflicting sources by choosing a winner — report both, dated.

We are **not** treating multi-model agreement as evidence. Your finding does not
become verified because you and another model agree; it becomes verified when a
document is produced and a human checks it against the primary source.

---

## 7. The standard we are holding

> **Dream freely. Promote nothing without receipts.**

> The ledger records. Atlas promotes. ORCS governs. CAS anchors. Nobody pretends
> the scoreboard created the game.

> Products are not power. Gradients are power.

> UNKNOWN stays UNKNOWN.

---

## 8. Response format

Please return, for each question: **ID → outcome → source → figures → URL →
evidence class → any contradiction to what we assumed.**

A one-line-per-question table is ideal, with quotes and links underneath for
anything marked FOUND or FOUND-CONTRADICTS. Nulls matter as much as findings — we
will record them in the register's unresolved ledger with your search terms so
they are reproducible.

---

**End of packet.** Current state: `SIMULATOR_VALIDATION = PASS`,
`LOCALITY_CLEARANCE = NOT_ESTABLISHED`, 22 streams, 0 realizing credit, 5 of 5
vetoes UNRESOLVED.