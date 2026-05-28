# KG Domain Subgraphs
Status: Candidate
Date: 2026-05-28

Domain-level subgraphs for Wave 3 topology expansion with typed edges.

## Systems subgraph (20 nodes)

Nodes: 20

```mermaid
graph TD
  AOS4[Aluminum OS v4.0] -->|supports| AOS3[Aluminum OS v3.0]
  AOS4 -->|depends| UB[Unified Field]
  UB -->|supports| SBARCH[SheldonBrain Architecture]
  SBARCH -->|implements| BZ[BAZINGA Launch Decree]
  BZ -->|supports| START[START_HERE]
  START -->|supports| ROADMAP[Roadmap]
  ROADMAP -->|depends| TOP50[Top 50 Board]
  TOP50 -->|depends| TOP10[Top 10 Board]
  TOP50 -->|supports| QUEST[Public Questboard]
  QUEST -->|supports| WEEKLY[Weekly Delta Template]
  AOS4 -->|supports| TRUST[Trust Charter]
  TRUST -->|depends| CANONB[Canon Boundary]
  CANONB -->|supports| CANONL[Canon Lifecycle]
  CANONL -->|depends| QUALITY[Quality Gates]
  QUALITY -->|tests| VALIDATE[Validation Playbook]
  VALIDATE -->|tests| TESTS[Tests README]
  TESTS -->|supports| REF[Reference Impl]
  REF -->|depends| SCHEMAS[Schemas README]
  SCHEMAS -->|supports| GPT[GPTDream README]
  GPT -->|supports| AOS4
```

## Governance subgraph (15 nodes)

Nodes: 15

```mermaid
graph TD
  GREAD[Governance README] -->|supports| WORKFLOW[Council Review Workflow]
  WORKFLOW -->|depends| DRIGHTS[Decision Rights Matrix]
  DRIGHTS -->|supports| RACI[Decision Rights RACI]
  WORKFLOW -->|supports| PROMO[Canon Promotion SOP]
  WORKFLOW -->|supports| REVOKE[Canon Revocation Process]
  PROMO -->|depends| REGISTER[Canon Candidate Register]
  REVOKE -->|depends| REGISTER
  RISK[Risk Register] -->|supports| HEAT[Risk Heatmap]
  HEAT -->|depends| INCIDENT[Incident Severity Ladder]
  INCIDENT -->|depends| RUNBOOK[Incident Response Runbook]
  RETAIN[Retention Policy] -->|supports| RETAINM[Retention Class Matrix]
  SUCCESS[Succession Stewardship] -->|supports| DRILL[Steward Succession Drill]
  FIRE[GOV Fire Drills] -->|supports| TABLETOP[Tabletop Scenario Deck]
  MISSION[Mission Control Cadence] -->|supports| WEEKSCRIPT[Mission Control Weekly Script]
  WEEKSCRIPT -->|depends| PACKET[Council Meeting Packet Template]
```

## GPTDream++ / Spec subgraph (15 nodes)

Nodes: 15

```mermaid
graph TD
  GREADME[archive/spec/gptdream/README] -->|supports| APPA[Appendix A]
  GREADME -->|supports| APPB[Appendix B]
  GREADME -->|supports| APPC[Appendix C]
  GREADME -->|supports| APPD[Appendix D]
  GREADME -->|supports| APPE[Appendix E]
  GREADME -->|supports| APPF[Appendix F]
  GREADME -->|supports| APPG[Appendix G]
  GREADME -->|supports| APPH[Appendix H]
  GREADME -->|supports| APPI[Appendix I]
  GREADME -->|supports| APPJ[Appendix J]
  GREADME -->|depends| AORCS[schemas/atlas_orcs/v0_1]
  GREADME -->|depends| OAI[schemas/o_ai/v0_1]
  GREADME -->|depends| NTHREAD[schemas/native_thread/v0_1]
  GREADME -->|implements| EXEC[reference_impl/execution_gate]
  EXEC -->|tests| ADV[tests/adversarial]
```

## TIDELOCKBrain subgraph (10 nodes)

Nodes: 10

```mermaid
graph TD
  TREADME[TIDELOCKBrain README] -->|supports| DJ1000[DREAM_JOURNAL_1000Y]
  TREADME -->|supports| WR1000[WAKE_REPORT_1000Y]
  TREADME -->|supports| DJ100[100Y Dream Journal]
  TREADME -->|supports| WR100[100Y Wake Report]
  TREADME -->|supports| DELTA100[100Y Delta Extraction]
  DJ1000 -->|supports| WR1000
  DJ100 -->|supports| WR100
  WR100 -->|supports| DELTA100
  WR1000 -->|depends| REM8[REM8 Protocol]
  REM8 -->|depends| WAKE[WAKE_REPORT_TEMPLATE]
```
