STATUS: ARCHIVE PUBLIC CANDIDATE | CANON: no | DEPLOYMENT: no | AUTHORITY: none | PROOF: no | PUBLIC_RELEASE: candidate

Recovered historical Manus artifact. Current review decisions: [build/review/EVIDENCE_APPENDIX.md](https://github.com/atlaslattice/manus-artifacts/blob/master/public_candidate_bundle_0001/nodes/dongjiakou_node_001/build/review/EVIDENCE_APPENDIX.md).

# China Seawater Desalination Candidate Node Register

| Metadata | Value |
|---|---|
| **Document ID** | `DJK-LATTICE-CHINA-DESAL-NODE-REGISTER-v0.1` |
| **Status** | `PUBLIC_CANDIDATE_NON_CANON` |
| **Date** | 2026-10-06 |
| **Repo** | Atlas Lattice / Dongjiakou Node-001 |
| **Reference head** | `4756036f9c428fa3aa1d4cea552ae03367523fb5` |
| **National desal project discovery count** | 167 |
| **Target locality node count** | UNKNOWN |
| **Sourced locality node count** | 11 |
| **Regional parents** | 1 |

## Method

The register was built from the **2025 National Seawater Utilization Report** and official or authoritative government/utility disclosures, supplemented by Xinhua, People's Daily and sector reporting where the primary project page was not discoverable. A locality is included only when a source names the locality and documents a seawater-desalination project or locality-specific plan. National or provincial totals are not converted into plant capacities; unknowns are kept explicit.

## Count reconciliation

**167 is the national 2025 count of desalination ENGINEERING PROJECTS.** It is a **discovery universe**, not a node count. The register contains **11 independently sourced candidate localities** plus **1 regional parent**, and it is intentionally not padded.

Project count and locality count are different quantities: some localities contain multiple desal projects. `target_locality_node_count` is therefore **UNKNOWN** and neither number may be substituted for the other.

### Ontology

A **locality node** is a non-overlapping geographic locality boundary. A **regional parent** is an aggregate that contains one or more localities and is **not** a peer of its children.

> A locality node may not geographically contain another locality node.

If geography is solved correctly at nodes 1–12, overlapping water, carbon, energy and waste ledgers do not have to be untangled at node 120.

## Candidate nodes

| ID | Locality | Province | Coastal | Status | Design capacity (m³/day) | Capacity class | Notable plant(s) / operator | Water-use sector | Sources / year | Notes |
|---|---|---|---:|---|---:|---|---|---|---|---|
| DJK-LATTICE-NODE-001 | 董家口（青岛市） / Dongjiakou, Qingdao | 山东省 | Yes | OPERATIONAL | 100,000 | REPORTED | 青岛董家口海水淡化厂 / 青岛水务海水淡化有限公司 | municipal; industrial; port | [Shandong Government](http://gb.shandong.gov.cn/art/2022/10/28/art_116200_560581.html) (2022); [Qingdao Daily](https://www.dailyqd.com/guanhai/424150_1.html) (2025) | Shandong Government reports 10万 m³/day. **Node-001 anchor.** |
| DJK-LATTICE-NODE-003 | 天津滨海新区 / Binhai New Area, Tianjin | 天津市 | Yes | OPERATIONAL | 200,000 | REPORTED | 国投北疆海水淡化工程 / 天津国投津能发电有限公司 | municipal; industrial; power | [Xinhua](https://www.news.cn/politics/20240325/052ef4ce79e14bccbe3490c21abfc681/c.html) (2024); [People's Daily](http://paper.people.com.cn/rmrbhwb/html/2021-06/22/content_3054771.htm) (2021) | 20万 is design capacity; People's Daily distinguishes it from observed current production. |
| DJK-LATTICE-NODE-004 | 唐山海港经济开发区 / Tangshan Port EDZ | 河北省 | Yes | OPERATIONAL | 300,000 | REPORTED | 申港海水淡化项目 / 申港海水淡化有限公司 | industrial; steel; chemical; port | [2025 National Report](https://www.hunan.gov.cn/zqt/zcsd/202606/33996572/files/2531a53343bb47f98eb2ce0f86968502.pdf) (2026) | Three-phase design total. Phase I 50,000 commissioned in 2023; phase II 50,000 completed trial operation in 2025; phase III is demand-dependent and not operating. |
| DJK-LATTICE-NODE-005 | 沧州渤海新区 / Cangzhou Bohai New Area | 河北省 | Yes | OPERATIONAL | 50,000 | REPORTED | 阿科凌新水源海水淡化工程 / project operator not otherwise established | industrial; chemical; port | [2025 National Report](https://www.hunan.gov.cn/zqt/zcsd/202606/33996572/files/2531a53343bb47f98eb2ce0f86968502.pdf) (2026) | Report lists this as newly completed, RO, 50,000 m³/day. Exact operator beyond project/company name is not established. |
| DJK-LATTICE-NODE-006 | 无棣县埕口镇鲁北高新技术开发区 / Chengkou, Wudi | 山东省 | Yes | OPERATIONAL | 124,000 | REPORTED | 鲁北碧水源一期、二期 / 鲁北碧水源海水淡化有限公司; 鑫岳化工项目 / 鑫岳化工集团有限公司 | industrial; chemical | [2025 National Report](https://www.hunan.gov.cn/zqt/zcsd/202606/33996572/files/2531a53343bb47f98eb2ce0f86968502.pdf) (2026) | Locality aggregate: 50,000 + 50,000 + 24,000 m³/day, not one plant. |
| DJK-LATTICE-NODE-007 | 龙口市 / Longkou | 山东省 | Yes | OPERATIONAL | 15,800 | REPORTED | 山东华电龙口发电有限公司海水淡化工程 / same | power; industrial | [2025 National Report](https://www.hunan.gov.cn/zqt/zcsd/202606/33996572/files/2531a53343bb47f98eb2ce0f86968502.pdf) (2026) | Newly completed RO project. |
| DJK-LATTICE-NODE-008 | 舟山市普陀区虾峙镇湖泥岛 / Huni Island, Zhoushan | 浙江省 | Yes | OPERATIONAL | 10,000 | REPORTED | 虾峙镇湖泥岛海水淡化工程 / 舟山市自来水有限公司 | municipal; industrial; port | [2025 National Report](https://www.hunan.gov.cn/zqt/zcsd/202606/33996572/files/2531a53343bb47f98eb2ce0f86968502.pdf) (2026); [China Daily](https://ex.chinadaily.com.cn/exchange/partners/82/rss/channel/cn/columns/sz8srm/stories/WS685a6a85a31009d21e5be5ac.html) (2025) | Report lists 10,000 m³/day newly completed; China Daily identifies the municipal water company context. |
| DJK-LATTICE-NODE-009 | 连云港市田湾 / Tianwan, Lianyungang | 江苏省 | Yes | UNDER_CONSTRUCTION | 45,600 | PLANNED | 田湾核电站海水淡化工程 / 江苏核电有限公司 (project context) | power | [Jiangsu report](http://zgjssw.jschina.com.cn/shixianchuanzhen/lianyungang/202208/t20220802_7640760.shtml) (2022) | Source says construction started and design capacity is 4.56万 m³/day; no later operating confirmation found. |
| DJK-LATTICE-NODE-010 | 盐城市大丰港区 / Dafeng Port Area, Yancheng | 江苏省 | Yes | OPERATIONAL | UNKNOWN | UNKNOWN | 江苏丰海新能源淡化海水发展有限公司海水淡化项目 / same | industrial; port | [Xinhua](http://www.news.cn/photo/20250608/625e66b035cf40608959da9f6be32b42/c.html) (2025) | Location and company are reported; capacity was not established and is **UNKNOWN**. |
| DJK-LATTICE-NODE-011 | 营口仙人岛 / Xianrendao, Yingkou | 辽宁省 | Yes | PLANNED | 100,000 | PLANNED | 营口仙人岛海水淡化工程 / UNKNOWN | industrial; petrochemical; port | [Liaoning Government](https://www.ln.gov.cn/web/zwgkx/zfwj/szfbgtwj/2022n/63E1B9695A0846FCA056B1FF9FBF34C0/index.shtml) (2022) | Provincial plan identifies 100,000 m³/day as a planned project; no operator or commissioning evidence established. |
| DJK-LATTICE-NODE-012 | 三沙市永兴岛/西沙洲 / Yongxing Island / Xishazhou, Sansha | 海南省 | Yes | OPERATIONAL | UNKNOWN | UNKNOWN | 西沙洲海水淡化设备/厂 / UNKNOWN | municipal; island | [Hainan Government](http://www.hainan.gov.cn/hainan/sxian/201507/d305214cf6524b87be181872c8fe7778.shtml) (2015); [Harbin Engineering University](https://news.hrbeu.edu.cn/info/1029/67536.htm) (year not stated) | Equipment installation and a mature Yongxing Island plant are reported, but capacity and operator remain **UNKNOWN**. |

## National/provincial aggregates (aggregate only, not per-plant)

The following figures are **provincial aggregates from the 2025 National Seawater Utilization Report**. They must not be interpreted as the capacity of one plant or as a locality count.

| Province / municipality | 2025 aggregate desalination capacity (m³/day) | Interpretation |
|---|---:|---|
| 辽宁省 | 161,984 | Aggregate; not per plant |
| 天津市 | 456,000 | Aggregate; not per plant |
| 河北省 | 490,700 | Aggregate; not per plant |
| 山东省 | 964,239 | Aggregate; not per plant |
| 江苏省 | 41,510 | Aggregate; not per plant |
| 浙江省 | 823,906 | Aggregate; not per plant |
| 福建省 | 29,950 | Aggregate; not per plant |
| 广东省 | 98,016 | Aggregate; not per plant |
| 广西壮族自治区 | 750 | Aggregate; not per plant |
| 海南省 | 9,750 | Aggregate; not per plant |
| **National total** | **3,076,805** | **Aggregate; 167 engineering projects, not one plant** |

**Aggregate source:** [2025 National Seawater Utilization Report](https://www.hunan.gov.cn/zqt/zcsd/202606/33996572/files/2531a53343bb47f98eb2ce0f86968502.pdf) (Natural Resources Ministry, 2026).

## Regional parents (not peer localities)

| ID | Region | Province | Aggregate capacity (m³/day) | Class | Child localities | Notes |
|---|---|---|---:|---|---|---|
| DJK-LATTICE-REGION-001 | 青岛市 / Qingdao municipality | 山东省 | 345,000 | REPORTED | DJK-LATTICE-NODE-001 | Regional parent, **not** a peer locality. It geographically **contains** Node-001 (Dongjiakou). Aggregate for three backbone projects; do not sum with any child. A 2025 Xinhua account gives 300,000 m³/day for two bases, so the disagreement is retained. |

**Aggregation rule.** `REGIONAL_PARENT` totals are reporting-only. They may never be
attributed back to a child node, and may never backfill a child node UNKNOWN.

**Why this matters.** The previous register listed Qingdao municipality as
`DJK-LATTICE-NODE-002`, a *peer* of Node-001. One peer node geographically containing
another breaks the ontology and would force the untangling of overlapping water,
carbon, energy and waste ledgers at node 120. Next step: subdivide the Qingdao regional
parent into specific non-overlapping locality boundaries — for example a sourced Baifa
service boundary — as each boundary is established.

## Unresolved / what would close it

- The 2025 national report gives 167 **projects** and province totals but not a complete public locality-by-locality plant register. Closing the gap requires the underlying Ministry survey/project annex or provincial inventories, and the result will be a **locality** count that need not equal 167.
- Qingdao reporting conflicts between 345,000 m³/day for three backbone projects and 300,000 m³/day for two application bases. A current utility asset register would close the discrepancy.
- Tangshan 申港’s total design capacity includes a demand-dependent third phase. A current operating permit or dispatch record is needed to separate operating from planned capacity.
- Operator identities and capacities remain UNKNOWN for Sansha and Yancheng. Commissioning certificates, utility disclosures or environmental acceptance documents would close them.
- Guangdong and Guangxi province totals are not converted into locality nodes because locality-specific project evidence was not established in this pass.

## Source documents

- [2025年全国海水利用报告](https://www.hunan.gov.cn/zqt/zcsd/202606/33996572/files/2531a53343bb47f98eb2ce0f86968502.pdf), 自然资源部海洋战略规划与经济司, 2026.
- [海水淡化利用发展行动计划答记者问](https://www.ndrc.gov.cn/xxgk/jd/jd/202105/t20210531_1282162.html), 国家发展和改革委员会, 2021.
- [青岛海水淡化：10年供水超2亿吨](http://gb.shandong.gov.cn/art/2022/10/28/art_116200_560581.html), 山东省人民政府, 2022.
- [淡化海水，如何用得起用得好？](https://www.news.cn/politics/20240325/052ef4ce79e14bccbe3490c21abfc681/c.html), 新华网, 2024.
- [江苏最大海水淡化项目在连开工](http://zgjssw.jschina.com.cn/shixianchuanzhen/lianyungang/202208/t20220802_7640760.shtml), 江苏省新闻, 2022.
- [辽宁省“十四五”海洋经济发展规划](https://www.ln.gov.cn/web/zwgkx/zfwj/szfbgtwj/2022n/63E1B9695A0846FCA056B1FF9FBF34C0/index.shtml), 辽宁省人民政府, 2022.
- [大连市积极利用海水替代淡水资源](https://www.ndrc.gov.cn/fggz/hjyzy/sjyybh/200701/t20070119_1133546.html), 国家发展和改革委员会, 2007.
- [三沙西沙洲建设海水淡化厂](http://www.hainan.gov.cn/hainan/sxian/201507/d305214cf6524b87be181872c8fe7778.shtml), 海南省人民政府, 2015.
- [从苦涩海水到清冽饮用水](http://www.news.cn/photo/20250608/625e66b035cf40608959da9f6be32b42/c.html), 新华网, 2025.
