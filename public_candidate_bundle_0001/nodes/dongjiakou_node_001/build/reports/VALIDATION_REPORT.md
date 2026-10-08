STATUS: ARCHIVE PUBLIC CANDIDATE | CANON: no | DEPLOYMENT: no | AUTHORITY: none | PROOF: no | PUBLIC_RELEASE: candidate

Historical model-generated report; see current review/EVIDENCE_APPENDIX.md.

# Node-001 Validator Report

Generated: 2026-10-08T13:07:39+00:00

**Overall: PASSED**

| Status | Count |
| --- | --- |
| PASS | 15 |
| WARN | 0 |
| FAIL | 0 |
| VETO | 0 |
| NOT_APPLICABLE | 1 |

Credit-ledger entries: 18

| Gate | Invariant | Status | Detail |
| --- | --- | --- | --- |
| G02 | UNKNOWN cannot silently become zero | **PASS** | Every zero-valued credit field is either an explicit baseline or justified. |
| G03 | Historical values cannot populate current state | **PASS** | All current-state fields remain UNKNOWN; historical figures are labelled counterfactual. |
| G04 | Planned capacity cannot populate operating state | **PASS** | Regional plan stays REPORTED with node access UNKNOWN and zero credit. |
| G05 | Feed-product residual cannot become marine discharge | **PASS** | Reject-equivalent remains labelled modelled; no discharge quantity is claimed. |
| G06 | One PV kWh cannot receive two primary credits | **PASS** | 0 primary credit(s) on S01 PV; at most one is permitted. |
| G07 | One recovered mass cannot be double-credited | **PASS** | No BIO01 recovered mass carries more than one primary credit. |
| G08 | Compute heat needs a measured sink | **PASS** | Useful-heat credit is zero; the first-law bound is reported separately. |
| G09 | Service benefit needs before/after KPI evidence | **PASS** | Model service benefit remains zero. |
| G10 | Ecological veto cannot be offset | **PASS** | node_veto_rule is present and aggregate benefit cannot offset a failed veto. |
| G11 | LLM actuator authority is NONE | **PASS** | No OT write credentials; recommendations pass a validator and operator approval before PLC/SCADA. |
| G12 | Model consensus is not evidence | **PASS** | Routing policy states cross-model agreement is not evidence. |
| G13 | RO high-pressure head cannot be counted twice | **PASS** | Pump head is explicitly excluded and no recovered head is claimed. |
| G14 | Existing S01 solar cannot be counted twice | **PASS** | S01 PV is explicitly non-incremental and carries at most one credit. |
| G15 | Conservation and bound checks | **PASS** | 18 ledger entries; none exceed a resource bound. |
| G16 | Net-positive requires measured terms | **PASS** | No net-positive operation is claimed. |
| G01 | UNKNOWN cannot enter Monte Carlo | **NOT_APPLICABLE** | No Monte Carlo execution was requested. |
