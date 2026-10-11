# 龙寻 2.0 / 东家口 DJK-001：国家级资源智能看板对标与差距审查
**DragonSeek 2.0 / Dongjiakou — National Resource Intelligence Dashboard: Landscape, Standards & Gap Review**

**Date:** 2026-10-10 (research snapshot)  
**State:** PROPOSED · NON-CANON · ZERO REALIZED CREDIT · NO DEPLOYMENT OR PRC ENDORSEMENT CLAIM  
**Intended recipient:** DeepSeek technical / architecture review (copy/paste discussion prompt); no submission made.  
**Provenance:** independent desk research + Atlas source inspection. Not a standards conformance certification.  

## 一、请 DeepSeek 审核 / Review request

请独立批判以下技术提案：以东家口 DJK-001 为**计量与物理守恒基准**，以 DragonSeek 2.0 为**中国主权治理下的可替换智能协调层**，探索面向中国产业园区、省域及国家汇总的资源看板。请优先确定已经存在的中国产业互联网、循环经济、污染排放、供应链平台与标准，避免重复造轮子。**不要把用户与 AI 的既有对话解释为 CAC/国家发改委/生态环境部的正式批准。**

Please correct engineering errors, identify prior art and missing Chinese standards, distinguish mandated vs voluntary standards, verify licensing and integration rights, and specify what field evidence is needed before national extrapolation.

## 二、调查结果 / Existing systems (evidence type: official provider or standards registry descriptions)

| Platform / precedent | Proven capability / source | Potential interface, NOT assumed permission |
|---|---|---|
| **KAOS COSMOPlat (卡奥斯), owned/associated with Haier** | Official Haier and COSMOPlat pages: industrial Internet platform, manufacturing orchestration, AIoT, smart energy/carbon management, industrial models, industrial parks | Read-only standards-aligned intake of authorized energy/material/production aggregates; no claim of direct integration. Note: the user's unnamed “K company” is **unconfirmed**; KAOS is a plausible candidate. |
| **Kingdee 金蝶** | Official cloud SCM and smart-park platform pages: procurement, warehouse, supplier coordination, park and services management | Business/financial supply-chain baseline or connector candidate. Also plausible “K” company. |
| **MEE national pollution permit disclosure portal** | Public pages document outfall positions, quantities, receiving destinations, pollutants, allowed concentrations, discharges and applicable standards | Candidate **source of reported permit metadata**; permit limit != measured real effluent; verify legal, field and API access. |
| **GB/T 36578-2018** | SAMR national standard, current; *Data interface specification for circular-economy informatization platform of industrial park*, reviewed May 2025 | Obtain normative clauses and compare schema field-by-field; **recommended** standard, not automatically mandatory. |
| **GB/T 39178-2020** | SAMR current recommended standard, *Guideline for optimization of circular industrial chains in industrial parks* | Process and circular-economy optimization alignment; normative mapping pending. |
| **HJ 274-2026** | MEE construction standard for eco-industrial parks, effective 2026-03-01; covers evaluation indicators and data collection/calculation | ECO01 evaluation candidates; full standard mapping still pending. |
| **MIIT 2025 百城千园行 initiative** | Official MIIT guidance on industrial internet for parks, standards, AI, supply chain, digital transformation | Policy context; not an authorization, procurement or platform integration commitment. |
| **SAP / Circulor and academic industrial-symbiosis tools** | Comparator category from prior research; not re-verified in this snapshot | International prior art; recheck product-specific coverage before novelty claims. |

### Verifiable official sources
- Haier platform: https://www.haier.com/haier_cosmoplat/
- KAOS product overview: https://www.cosmoplat.com/product
- KAOS energy and manufacturing examples: https://www.cosmoplat.com/lighthouseFactory/
- KAOS official cases: https://www.cosmoplat.com/case?id=1976524324720967682
- Kingdee smart park: https://www.kingdee.com/solutions/smart_park.html
- Kingdee SCM: https://en.kingdee.com/products/scm_cloud/
- SAMR GB/T 36578-2018: https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=8348626E3B7A3D8288341F1D06759F62
- SAMR GB/T 39178-2020: https://std.samr.gov.cn/gb/search/gbDetailed?id=V9CWD7Frsic%3D&mode=p
- MEE HJ 274-2026: https://www.mee.gov.cn/ywgz/fgbz/bz/bzwb/other/qt/202602/t20260228_1145104.shtml
- MEE pollution permit portal: https://permit.mee.gov.cn/
- MIIT park program: https://www.miit.gov.cn/ztzl/rdzt/gyhlw/gzdt/art/2025/art_c1ab1b7425bb449ca47534ad8b0dd5a0.html
- MIIT supply-chain digital transformation: https://www.miit.gov.cn/jgsj/xxjsfzs/gzdt/art/2025/art_c195b1b6c1f343e392ee83bf960af9f6.html

## 三、非重复建设与实际差距 / Build-vs-bridge decisions

**Already addressed at least in part by real systems:** material traceability, industrial energy monitoring, industrial AI, SCM, smart-park services, legal pollutant-permit metadata. Do **not** represent these as Atlas inventions. Differences among provider claims, real deployments and accessible APIs require validation.

**Potential synthesis gaps (NOT globally unique claims):**
1. A single auditable comparison joining **mass/element/energy balances + by-product quality + contracted sinks + liquid/sludge/brine fate + financial cost basis**.
2. **QOL01** and **ECO01** as first-class objectives/vetoes and contributors to **FUND01** public-benefit proposals, while nonmarket benefits never count as spendable revenue.
3. Across-site rollups with **no double counting**, conservation constraints, denominators, uncertainty distributions, and measured-vs-modeled separation.
4. Long-horizon lifecycle liabilities, reversible actions, human review and documented false-positive/false-negative audits.
5. Mandarin-first national reporting with common units and semantic contracts; site dialects limited to *local physical reality / technical classifications*, not unit ambiguity.

**Novelty uncertain** until broader patent/software/standard review. Access/integration with KAOS, Kingdee, PRC agencies or sites is not established. Central PRC governance should follow **legally assigned competencies** (CAC for relevant cybersecurity/data, MEE for environmental permitting, NDRC/MIIT for corresponding planning/industry areas, plus provincial/local and operator responsibilities), not imply a single agency can approve all actions.

## 四、Dongjiakou baseline / Current implementation honesty

- Existing baseline v1 is untouched. GitHub draft PR #289 adds `simulator_v2.py` with modules `QOL01`, `ECO01`, `FUND01` and imports v1 `models.locality.run()` and `models.run6_resources.run()`.
- **Partial alpha, not full v1 parity**. v1 run families (solar, hydro, compute, biomass, storage), validator/evidence gates, data fixtures, site calibration and robust funding require consolidation.
- Historic CI run on PR #289 reported **FAILURE**; diagnostic logs were unavailable during earlier fetch. No test pass, merge or deployment claim.
- Prototype QOL programs are PROPOSED. Physical outfall quantity and effluent chemistry remain UNKNOWN. No claimed QOL effects or avoided ocean pollution.
- The user-reported *40% immediate resource recovery / 60% remaining need* is a **scenario sensitivity** with unknown comparable cost/NPV basis; it is not receipted Dongjiakou returns or authorized subsidy.

Git references: https://github.com/atlaslattice/manus-artifacts/pull/289 and https://github.com/atlaslattice/manus-artifacts/pull/288  
Notion code backup (15 select files only): https://app.notion.com/p/3f60c1de73d98121aa6af2ceb8868798

## 五、建议架构 / Proposed review design

**Governance:** National policy contracts / accountability and permission rules set at the competent-authority level; regional/sector administration and legal plant operators retain assigned responsibility. **Not an uncontrolled federation, not an LLM plant-control system.**

**Data:** native Mandarin field documentation; canonical measurements with dimensions, units, conversion version, source original, time zone, temporal resolution, quality assay, instrument uncertainty, identifier, license, permissions and immutable provenance pointers. SI where appropriate, with explicit accepted Chinese industry norms; mapping to GB/T 36578-2018 **after reading normative text**. Localized data capture is allowed, but unvalidated conversion is not.

**Reasoning:** Self-hostable, license-verified DeepSeek candidate; optional Qwen/Manus modules; Atlas Intelligence only as optional reference/replaceable interface; AI provides suggestions, exception reviews and audit explanations. Don't assert self-hostable weights for the newest API-only DeepSeek model until verified.

**Validation:** deterministic mass, energy and financial conservation; constraints; unit testing; source evidence and uncertainty boundaries; cross-sector double-count prevention; ECO/QOL hard vetoes where prescribed by competent authority and safety rules.

**Control:** independent PLC/SCADA safety interlocks and local responsible operators; explicitly approved reversible action pathways; immutable audit trail. Optional redacted external GPT arithmetic/method audit **only with independently approved transfer and classification**; this is a design option, not official government acceptance.

**Time horizons:** hourly operational visibility where sourced; daily/seasonal allocation; multi-year investment; 100–1,000y stewardship scenarios with maintenance/replacement/climate uncertainty and no annual multiplication fallacy.

## 六、DeepSeek 请求回答的 12 个问题

1. 用户提到以 K 开头的现有平台：究竟是卡奥斯 KAOS、金蝶 Kingdee、还是别家？请提供正式来源。
2. 是否有更接近**国家级跨行业物质流 + 社会福利 + 生态 veto**的中国现有系统？
3. GB/T 36578-2018 的**原文接口字段**有哪些？我们的字段如何一一映射？不能凭标题宣称合规。
4. 除此以外，应检索哪些 GB/T、HJ、MIIT、国家数据标准、排污许可、数据安全与关键信息基础设施规范？
5. KAOS/Kingdee/排污许可平台的哪些接口有合法公开文档？哪些需要机构授权与商业合同？
6. 哪些生产/物料/能源数据可由企业授权汇总？如何防止暴露商业秘密？
7. QOL 与 ECO 指标如何进入多目标优化、hard veto、FUND01 财政评估且**不能创造账面现金**？
8. 海岸排污闭环应如何监管残渣、盐水、污泥、地下水、必要生态流量，并防双算？
9. 给出可量化的东家口校准缺口：真实流量、化学检测、产能、合同、边界、价格、计量时间基准。
10. 哪种授权机制能保证 AI 建议不自动下发至厂控、保护当地法定操作责任？
11. 如何建立 v1→v2 数学一致性测试、跨节点互认测试、模型不确定性评估和可重放审计？
12. 哪些模块应直接复用国内现有能力，哪些才值得独立构建？请按 *existing / spec-needed / proposed / tested / pilot-ready* 分级。

## 七、行动边界 / No false launch
A review-ready architecture is not plant clearance, procurement consent, cross-border data approval, regulator acceptance or deployed national infrastructure. Preservation is additive; keep v1 and earlier v2 PRs unmerged pending their own verification gates. This document is for DeepSeek critique and Chinese institutional reality checking, not lobbying or assertions of privileged authorization.

**Keepers:** Measure first. Source every number. A node is not a country. QOL is an objective, not cash. Ecological vetoes are not washed out by commercial scores. Central governance does not erase local physical truth.
