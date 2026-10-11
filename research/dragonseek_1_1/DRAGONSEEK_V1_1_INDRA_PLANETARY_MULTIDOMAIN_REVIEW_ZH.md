# DragonSeek 1.1 — 殷陀罗网·全球地球—空天多圈层韧性观测协议
**Tidal Lantern / Indra's Net · 2026-10-11 · PROPOSED / NON-CANON / ZERO REALIZED CREDIT · 开源研究、只读、非政府平台**

> 一颗地球，多个主权主体。统一的是可审计数据语义；分开的，是治理权限、数据控制权、地域法律和真实操作授权。

## 一、技术推进：DeepSeek评审问题逐条处理（不可覆盖v1.0原版）

| DeepSeek问题 | v1.1完成内容 / 状态 |
|---|---|
| **CRITICAL 手机地理标记漂移** | 强制底图及覆盖层的视觉宽高均为 **14:10**；旧版手机特殊 `1/1.05` 拉伸删除。来源图片2240×1600，地理范围72–151°E、0–56°N；研究使用 EPSG:4326 经纬度柱状等距。**代码/几何修正完成，浏览器移动端视觉验收尚未完成（本地无Chromium）。** |
| **HIGH 初始微电网默认隐性失败** | 用户此前测试已实际重算：20kW负荷，35kWp PV，380kWh电池，云/日照因子0.65：**仅24/168小时完全服务**，第25小时开始部分短缺。明确标“故意失败压力测试”；同容量/同负荷存储独立版仅**17小时**。没有把失败悄悄改成成功。 |
| **HIGH 电池充/放电功率缺失** | 引入独立 `battery_max_charge_kw`、`battery_max_discharge_kw`，默认95kW；每小时应用PV入电、电池SOC、双向效率与kW功率上限。仍非电网潮流/继电保护模型。 |
| 太阳能简化 | 显示 `CRUDE_12H_SINE_NO_WEATHER`，模拟12小时日照正弦，0.85定值损失，非青岛十月真实天气。下一步用本地气象记录、辐射、纬度/季节、温度、组件朝向建真实发电曲线。 |
| 危险授权布尔值 | 移除“用户自己填True便通过重要数据”模式；新增 `AuthorizationRecord`：发行方、数据所有者、用户身份、目的、范围、司法管辖、过期、文档SHA、聚合复核编号；**还需可信发行方与可信文档哈希在独立注册表配置。** 研究测试中的模拟“可信”不是司法认证、数字签名、撤销服务或生产IAM。 |
| 时间、时效 | 数据需 `retrieved_at`/`ttl_seconds`，全部源时间显式UTC偏移；手动公开气象查询以UTC请求，前端把有效时戳显示+00:00。界面含STALE/UNKNOWN/NOT CONNECTED状态；关闭伪实时。 |
| 来源类型和安全可视化 | `event_provenance`、`classification`、`data_flow_authorization`、`data_owner`、`jurisdiction`、`crs`、`cii_operator_designation_status`均出现在点击标记的检查面板。 |
| 重要数据目录申报 | 事件为五项相关字段预留 `filing_rule_id`、`applicable_filing_schedule`、`reporting_entity`、`change_trigger`、`filed_receipt_id`，均默认NULL；不暗示每个实体受同样申报日期或由研究系统自动报送。 |
| 单位tce源头歧义 | 保留原始GB/T2589与DeepSeek报告的NBS统计换算候选为**独立有日期和适用域的转换配方**；29,307.6 与29,271.2 kJ/kgce的差异还需取得精确NBS官方条文后才升级SOURCE_VERIFIED。绝不平均或跨域自动选择。 |
| 交付验证 | 45/45全新本地Python单元测试PASS；JavaScript `node --check` PASS。移动端浏览器可视化、实际现场和GitHub CI均**未验证**。 |

## 二、核心研究：IN-DRA-01 多圈层星球链路

**分层架构：**

```
地球系统/天气/海洋  ─┐
地表服务/韧性       ─┤
地下地质/地震/磁场 ─┤
地面空气交通/气象 ─┼─> 源头来源与时间校验 ─> 数据分类授权门 ─> 公众聚合视图 / 有权限的本地研究视图
近地轨道/太空碎片 ─┤                         └─> UNKNOWN/STALE/未授权：明确降级/拒绝
陨石火流星/NEO   ─┤
全球农业/蝗虫/疫情 ─┘
```

每个适配器必须保存 `provider_legal_name`、`reference_url`、`license_and_tos`、`data_owner`、`source_evidence_class`、`event_provenance`、`source_issued_at`、`valid_at`、`retrieved_at`、`ttl_seconds`、`temporal_model_type`、`crs`或天体坐标系、`datum`、`uncertainty`、`allowed_jurisdictions`、`authorization_record_id`、`quality_flags`、`operator_warning_status`。

**不能把全部数据叫“实时”：**轨道根数是特定历元的估计，NEO轨道需要星历和误差范围，地震目录含后续修订，卫星火点受过境/云影响，病原体废水报告有采样、检测与发表延迟，公众气象服务不等于气象局正式预警。

### A. AVIATION01 航空与大气交通

- 可由中国民航局CAAC官方公开通告、ICAO公共资料、经过许可的OpenSky等**研究许可**来源构建区域级天气/航班异常、航空气象和空域受阻聚合层。
- 分清民用空管**法定空域分离**与本研究航班公开态势展示；ADS-B接收可能覆盖不全，飞行计划/军航/安全敏感航迹和未公开航空管制信息不能采集显示。
- 它**不能**用于为航班改航、处理ATC飞行间隔、控制机场、发布NOTAM或引导机场安保行动。
- 未来与台风/雷暴、高空风场、结冰/颠簸和低能见度图层联动，仅用于公众防灾、交通连锁延误与韧性研究。

### B. ORBIT01 + SSA01 近地轨道与卫星避碰研究

- 全球民用公共研究适配器：CelesTrak GP、公开ESA Space Safety、经确认公开的中国国家航天局信息；**公开轨道目录非完整卫星清单**。
- 保存轨道/坐标体系（ECI如TEME/GCRS、epoch UTC、时间标度、轨道模型SGP4、协方差是否存在、追踪标识与发布机构）。地面WGS84地图**不得直接把轨道坐标画成经纬度**；需经过受验证的时标和地球自转变换。
- 卫星交会只能在取得合法数据、有精度和协方差、经过专业验证后作**风险研究**。没有协方差或高精度状态时，不得生成可用于运营的碰撞概率、规避机动指令、具名高敏目标聚焦或机动优化。
- CelesTrak 2026公开使用政策：GP数据通常两小时更新，不应疯狂轮询；须缓存、遵守失败退避和新版CSV格式要求。
- 最初地图只显示**轨道科研信息卡片**，绝不显示虚构碰撞警报。

### C. NEO01 + METEOR01 行星防御、火流星、星历

- NASA/JPL CNEOS **Sentry**（潜在冲击风险）、**Scout**（新发现候选）、**SBDB/CAD**（小天体轨道及预测接近）、MPC（原始天体观测）为全球可公开研发候选。实际危险性**仅由有专业资格的天文机构评估和公告**。
- 对**潜在接近**区分：绝对距离、月球距离LD、轨道不确定度区间、接近时刻TDB/UTC转换、推测质量、速度和后续观测，**接近不等于撞击**。
- 大气火流星/天然陨石与航天器再入要分开，未识别目标归UNKNOWN；不通过传感器异常认定“外星入侵”。
- JPL APIs明言**不要直接嵌入网页**（CORS）；后续服务端缓存或独立公开数据镜像必须符合法律和使用条款，未接入。
- **(16) Psyche小行星**：NASA任务科学目标与金属/硅酸盐的测量不确定性可以入天体目录；没有采矿权、可提取储量、利润或向地球运回技术证明。NASA在2026称金属可能占体积**30%–60%**，并非纯金属宝藏。

### D. SEIS01 + DEEP-EARTH01 + MAG01 地震与深地观测

- 中国地震台网公开震讯与全球USGS地震GeoJSON/QuakeML作为已知权威参考；世界台网/地球磁场可选择INTERMAGNET、EarthScope/FDSN，根据来源许可和观测延迟评估。
- 分成至少四个不同物理模块：**①地震波P/S/面波频谱、震源深度、规模与仪器台阵；②重力、地球潮汐、应力/形变与地壳构造；③地磁场、地电与磁测/大地电磁MT；④地—电离层共振/Schumann、空间天气和电离层。** 不能把全部深地测量都叫Schumann，也不能把监测到某频率视为地震可预测依据。
- 时间跨度从毫秒波形到多年慢滑移，不同单位（Hz、nT、m/s、m/s²、Gal、Pa、km深度）不可混用；仪器校准、噪声谱、假信号、三维波速模型及误差边界必填。
- **不声称可以可靠预测具体地震时间/地点/震级**；台网已签发的预警与研究异常必须视觉分离。
- INTERMAGNET通常受署名-非商业(CC BY-NC)等许可及站点差异约束，不得认为所有信号可商业镜像。

### E. GLOBAL01 中国参与的世界各地公共项目长期计划

- **长期视图只预留插件，不在这一版地图展示具体项目坐标。** 将中方相关公开国外港口、能源、农业、水利、铁路、地震防灾、医疗研究等计划录入经合法公开验证的
  `project_id / host_country / china_participation_type / consent_and_legal_owner / phase / geographic_resolution / as_of / source / financial_scope / data_sensitivity / related_public_hazards / exposure_confidence / response_organization`。
- 坚持国别及主权多元治理：公开中国发展合作来源(CIDCA等)、东道国公开项目、国际发展机构可做交叉检查；**中国资助项目未必与中国政府完全共享数据，未来插件不等于已获授权。**
- 示例**明确标SYNTHETIC**：“某非洲农业地区的假设性灌溉项目附近，FAO蝗虫风险升高”→该区域非敏感**综合**预警节点提示核实与联络。不得杜撰真实项目、地块与原始坐标、实际蝗灾。
- 最初希望服务中国研究，再对全球公开气象/海洋/地震/NEO做**合法公开基础资料的全球层**，尊重各司法辖区；美国/印度公开数据可以作为一般国际交叉核对，不将过去Indra's Net特殊合作/共享设想宣传为现有外交或军事安排。

### F. PEST01 + BIOWATCH01 + WES01 蝗虫、农林病虫害、人畜共患与废水预警

- **粮食/蝗虫**：FAO eLocust3观测通过国家中心验证后可进入FAO Locust Hub；融合降水、土壤湿度、植被、水文与公开地表项目区域，作公共粮食安全**风险辅助层**。其他农业病虫害、野生动物疾病、人畜共患病单列物种与检验方法。检测、干预须经专业农业/卫生/环保机构实施，**不进行物种灭绝、无差别生态破坏或未经证实的声学“驱散”部署**。
- **废水公共卫生**：计划在中国境内由授权疾控、公卫和污水运营者实施**每周两次**采样评估；**频率是用户提出的设计目标，不是中国已批准的全国制度**。对照CDC的美国污水监测推荐每周两次，而WHO强调立项、持续运行、样本分析和公共卫生解释的综合QA。
- 工作流 `SITE_AGGREGATED_CATCHMENT → CONSENT/PERMIT/BIOSAFETY → MON/TUE or MON/THU QA SAMPLING DESIGN → LAB_VERIFIED_RESULT → TIME_NORMALIZED_TREND → PUBLIC HEALTH REVIEW → SAFE_AGGREGATE PUBLIC DASHBOARD`；具体采样时间需公共卫生专家定，不在此指定实验室培养或扩大病原体做法。
- 样本登记：`sample_window / treatment_plant_legal_id / catchment_size_band / inflow_m3d / rainfall_confounds / clinical_context / measurement_assay_version / quantification_limit / QC_flag / population_normalization / detection_uncertainty / laboratory_signoff / disclosure_coarsening / report_delay / aggregate_authorization`。
- 小型汇水区、机构群体、医院或敏感地点一律防逆识别；禁止个人/住户健康状态推断、未经许可的定向执法和“中和/消灭”病原体行动自动化。只做**辅助决策、趋势和公共健康机构的专业调查提示**，任何卫生应急措施需法定程序和人类负责。
- 最初只放**合成示范**和不存在真实采样的标志；公众地图不得显示未经核实的疫情爆发。

### G. CULTURE01 中国传统宇宙观/医学术语可选图层

- 二十四节气、二十八宿、十二时辰、中国传统星官与五行/五运六气可以作为**文化、历史或教育标签**。需要单独历法、时区、天文历表和翻译语义，且区分不同传统版本。
- **完全独立于**地震、流行病学、医药疗效、NEO风险的实证模型；没有科学依据就不把天体/地磁事件解释为身体症状或疾病预测。
- 1.1 UI只提供开关与“文化标签未计算”的静态标注，不宣称已经完成星座/宿度数学计算。

## 三、运行状态、事实边界和版本保全

**v1.1可运行：** 离线交互网页（原底图和坐标形状一致）；15个陆地合成演练事件 + 2个天体合成案例；46个数据源候选（旧26 + 新20，全部未接入）；可选Open-Meteo主动三城查询；在选中标记展示出处、所有者、权限、司法区域、CRS、时间和合成状态；公开资料健康检查及STALE状态；168h两模式公平比较；Python门禁、45项本地单元测试。**这不是实时气象、卫星避碰、空管、地震预测、疾病诊断或重大政府工程管理平台。**

**v1.1不声称完成：** 中国官方气象与海洋三个合法数据源连接、实际CNEOS/USGS/FAO/CelesTrak流的持续合法接入、空间天气和深地信号物理同化、流行病学实验室网络、法务许可认证、移动浏览器完成视觉验收、真实电网系统、真实中国海外项目动态地图、工业数据许可或官方CAC合作。

**首个MVP-1工作顺序（优先）：** 取得三个合法来源→下载和许可证收据→研究源头适配器→时空/单位/CRS校验→地震/海气象历史回放→失败/过期降级→单元与移动浏览器验收→外部DeepSeek技术审查→继续迭代。

## 四、请DeepSeek审查

1. 当前默认 **17h storage-only vs 24h replenishment** 同配置的合成结果是否完整覆盖电池充放电限幅？请找损失模型或负荷匹配错误。
2. 用户原2026年提供新标准、CAC重要数据目录、30%变更、8月30日与tce两套能量统计换算，请以官方条款逐项核对**适用主体和生效日**；未核对资料保留COLLABORATOR_REPORTED。
3. CAAC/CNSA/CENC/CMA/Fengyun/国家海洋预报中心数据源：实际开放接口、许可、国内缓存、时标与可再发布权限如何？中国有何优于美国NASA或ESA的公开星空/近地轨道接口？
4. 能否指出获得可信的**非敏感民用SSA数据**以及必要误差/协方差最小集合的合法路径？未达到不生成碰撞警报。
5. 中国疾控与污水厂的合法生物监测流程能否**每周两次**，以及以何方式汇总避免个人/社区层面逆识别？
6. 需要哪些更多模态来补全真正的地球“全系统”视角：电离层/空间天气、声学台阵、陨石光学网、GPS/北斗地壳形变、沿海海啸观测、地质断层应变和人工卫星再入？请推荐按中国公开数据优先的最短路线。
7. 是否愿意对新MVP在本地真实Chromium环境下验证不同移动视口的地图标记、地球海洋边界、时区/缓存降级、合成标识和敏感数据公开拒绝？

**结论：地球只有一颗，主权有许多。首要原则：尊重合法边界，用公开的真实数据创造高质量公共研究。EVERY PIXEL EARNS ITS TIMESTAMP.**

## 五、参考数据入口（实际权限单独审查）

- CelesTrak usage policy https://celestrak.org/usage-policy.php
- NASA/JPL SSD / CNEOS API https://ssd-api.jpl.nasa.gov/ 、直接网页嵌入限制 https://ssd-api.jpl.nasa.gov/doc/index.php
- NASA Psyche mission https://science.nasa.gov/mission/psyche/
- MPC data https://data.minorplanetcenter.net/
- USGS earthquake feeds https://earthquake.usgs.gov/earthquakes/feed/v1.0/
- INTERMAGNET data license https://intermagnet.org/data_conditions.html
- FAO Locust FAQ https://www.fao.org/locusts/faqs/en/
- WHO WES guidance https://www.who.int/teams/environment-climate-change-and-health/water-sanitation-and-health/sanitation-safety/wastewater
- CDC 2026 wastewater sampling suggestion https://www.cdc.gov/nwss/data-methods.html