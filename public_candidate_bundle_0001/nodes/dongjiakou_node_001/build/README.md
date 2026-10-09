# Dongjiakou locality simulator / 董家口地方节点模拟器

STATUS: REVIEWED PUBLIC CANDIDATE | CANON: no | DEPLOYMENT: no | AUTHORITY: none | PROOF: no | PUBLIC_RELEASE: reviewed

Runnable, forkable research model recovered from Manus and extended after review of October 1–8 Notion/Git work and the latest DeepSeek handoff. This is an evidence-aware simulation, with no plant-control interface. Every current realized credit is zero; locality clearance is not established.

## Run locally

```bash
git clone https://github.com/atlaslattice/manus-artifacts.git
cd manus-artifacts/public_candidate_bundle_0001/nodes/dongjiakou_node_001/build
python3 simulator.py reproduce
python3 simulator.py validate
python3 simulator.py current
python3 simulator.py gap resource_gap/examples/dongjiakou_unknown.json
python3 simulator.py gap resource_gap/examples/synthetic_gypsum_acid.json
python3 simulator.py gap resource_gap/examples/synthetic_biological_P.json
python3 -m pip install -r requirements-dev.txt
python3 -m pytest tests -q
```

Python 3.10+; simulator uses the standard library. Pytest and jsonschema are development dependencies only. Fork the repository on GitHub, edit a scenario JSON, and retain each input's basis, unit, uncertainty and citation. CI runs the same reproduction, gate and test checks.

## What is current

`current` emits the QOL review overlay: 20 boundary units (19 internal plus EXT01, including QOL01), 23 streams (5 reported physical, 18 opportunity), six unresolved vetoes, zero realized credits. Named water buyers remain a hyperedge with unknown shares and mixed/unknown boundary allocation. LDC is a food facility, not a water buyer. Operational slag and tire outputs are routed to market; their AM allocations remain candidates. The 26 GWh generation and 8 GWh avoided cooling electricity are separate projections from a reported construction project.

`locality`, `resources`, archived reports and `README_MANUS_RECOVERED.md` preserve the recovered historical Manus snapshot. They do not represent the latest unpublished Manus source. The original source hashes verify. The recovered core passes 226 tests; the recovered core plus reviewed extension checks passes 239 tests; later Notion reports of 316 tests are not claimed as executed here. [Recovery provenance](review/recovery_provenance.json) records this limit.

## Beyond sulfur and gypsum

The sulfur/gypsum lane is an example of a general needs-matched resource model. Biological or hybrid routes can be evaluated for nutrients, protein and other resources when a qualified physical feed and conversion pathway exist. Biology transforms, concentrates or recycles constituents; it does not create sulfur, potassium or phosphorus. Atmospheric nitrogen fixation has a different source boundary and must be modeled explicitly.

The extension uses demand, secure supply, reserve-building flow, accepted dry feed, allocated/delivered fractions, conversion yield, constituent ceiling, hub capacity, market ceiling, energy load and the eight module/eight transfer receipts. It propagates UNKNOWN as null and rejects duplicate feed identities and inconsistent product bases. Passing synthetic fixtures demonstrate arithmetic, not feasibility. Even conditional modeled output earns zero realized credit.

Pure gypsum dihydrate has a theoretical H2SO4-equivalent ceiling of approximately 98.079/172.171 = 0.570 t/t. Industrial acid solution tonnage, pure acid equivalent, dry gypsum and wet feed are different bases. No automatic 0.40–0.50 commercial yield is assumed. The numerical examples are explicitly synthetic; the local case remains unknown.

## Review, citations and missing data

- [Evidence appendix and promotion decisions](review/EVIDENCE_APPENDIX.md)
- [Helium, two cold-energy projects and sludge: transcript review](review/HELIUM_COLD_SLUDGE_REVIEW_2026-10-09.md)
- [Machine-readable helium/cold/sludge claims and open receipts](review/helium_cold_sludge_review_2026-10-09.json)
- [Machine-readable evidence updates](review/evidence_updates_2026-10-08.json)
- [23 original data requests, reconciled](review/unknown_reconciliation_2026-10-08.json)
- [Notion retrieval reference index](review/notion_reference_index_2026-10-08.json)
- [Scenario schema](resource_gap/scenario.schema.json)
- [MIT license for this build](LICENSE)

National circular-economy policy and desalination/brine-recovery policy are verified context. They do not award funding, authorize a site, endorse Atlas Lattice or establish technical/economic performance. Project existence is stronger than a hypothetical route, and remains distinct from measured operation. No original plant-specific DAR receipt is closed by these updates.

## 中文说明

本项目为可运行、可分叉的研究模拟器，供开发者、研究人员和政策研究者参考。硫磺／石膏路径是通用资源需求匹配模型的示例，可扩展到具备真实原料和转化路径的生物或混合资源回收。国家政策、在建项目、中试、预测产量和实测运行分别标注。未知数据保持为空；模拟产量不计入实际收益或生态信用。请参阅证据附录与数据需求清单，补充带日期、边界和来源的实测数据。模型不连接工厂控制系统。

## QOL / Eden review addition

QOL is now a first-class human/ecological objective vector, exposed by `python simulator.py qol`, `current` and resource-gap outputs. The review snapshot adds QOL01 as a functional outcome register:20 boundary units (19 internal plus EXT01),23 material streams,5 separate proposed observation/service links. The32 indicators and6 default strata remain UNKNOWN locally. No composite score or realized QOL benefit is produced. Safety, ecological protection, privacy, fair access, water/product safety and maintenance are non-compensable gates.

Read [QOL_EDEN_STANDARD_v0.1](qol/QOL_EDEN_STANDARD_v0_1.md), the [schema](qol/observation.schema.json) and [eight additional data requests](qol/DATA_REQUESTS.json). Historical publications and reports retain their original19-unit baseline; this additive change is on a review branch pending review. Local QOL tests:264 passed; with the offline integration packet extension,268 passed.

## OS integration review seam

`python simulator.py packet` exports a content-hashed offline locality/QOL envelope for future Continuum/Aluminum/UWS/DragonSeek consumers. It makes zero provider/model calls and grants no actuator authority. [Integration contract and component references](integration/OS_INTEGRATION_CONTRACT_v0_1.md). Connected adapters and AtlasSeek/DragonSeek2.0 model training remain proposed.
