STATUS: ARCHIVE PUBLIC CANDIDATE | CANON: no | DEPLOYMENT: no | AUTHORITY: none | PROOF: no | PUBLIC_RELEASE: candidate

Recovered historical Manus artifact. Current review decisions: [build/review/EVIDENCE_APPENDIX.md](https://github.com/atlaslattice/manus-artifacts/blob/master/public_candidate_bundle_0001/nodes/dongjiakou_node_001/build/review/EVIDENCE_APPENDIX.md).

# Unresolved UNKNOWN Ledger

Generated: 2026-10-07T02:36:55+00:00

> UNKNOWN remains UNKNOWN. Every entry below is either an unestablished quantity or an explicit zero-credit baseline. Nothing here may be backfilled from aggregate node performance.

## Counts

| Group | Count |
| --- | --- |
| desalination unknowns | 10 |
| compute unknown parameters | 11 |
| components | 8 |
| green direct unknowns | 5 |

## Desalination unknowns

- `whole_site_SEC_kWh_m3`
- `delta_aux_kWh_m3`
- `current_measured_recovery_fraction`
- `current_feed_and_reject_stream_map`
- `current_brine_composition`
- `fouling_rate_and_cleaning_frequency`
- `current_CIP_and_additive_chemistry`
- `current_ecological_monitoring_primary_data`
- `hydraulic_unused_head_profile`
- `roof_structural_and_interconnection_limits`

## Compute unknown parameters

| Parameter | State |
| --- | --- |
| `L_IT_load_factor` | UNKNOWN_0_TO_1 |
| `actual_PUE` | UNKNOWN_GE_1 |
| `WUE` | UNKNOWN |
| `compute_cooling_water_source` | UNKNOWN |
| `hourly_solar_compute_overlap` | UNKNOWN |
| `PV_curtailment` | NOT_ESTABLISHED |
| `useful_heat_capture_fraction` | UNKNOWN |
| `coolant_supply_return_temperature` | UNKNOWN |
| `CIP_temperature_setpoint` | UNKNOWN |
| `CIP_thermal_demand` | UNKNOWN |
| `heat_pump_COP` | UNKNOWN |

## Component evidence profile

| Component | Type | Evidence profile | Credit | Node access |
| --- | --- | --- | --- | --- |
| W01_DESAL | desalination | EXISTING_RECEIPT_BACKED | None | None |
| G01_REGIONAL_GREEN | generation | OFFICIAL_PLAN_REGIONAL_ACCESS_UNKNOWN | 0 | UNKNOWN |
| S01_ROOFTOP_PV | generation | EXECUTED_TECHNICAL_SENSITIVITY | None | None |
| B01_STORAGE | storage | SPECIFIED_ZERO_CREDIT | 0 | None |
| C01_COMPUTE | compute_and_control_plane | EXECUTED_PARAMETRIC_TECHNICAL_SENSITIVITY | None | None |
| P01_PORT_LOADS | port_loads | REGIONAL_PLAN_EXISTS_LOAD_SET_UNRESOLVED | None | None |
| GRID01 | grid_interface | POLICY_PATHWAY_VERIFIED_NODE_CONTRACT_UNKNOWN | None | None |
| BIO01_BIOMETABOLIC | organics_wastewater_nutrient_recovery_composting | PROPOSED_ARCHITECTURE_EXECUTED_PARAMETRIC_TRANSFER_FUNCTION_ZERO_CREDIT | 0 | None |

## Explicit zero-credit baselines

- RUN_0.retrofit_credit.* — no retrofit credit assigned
- RUN_2.baseline.hydro_credit_GWh_year = 0 — no receipt identifies unused head
- RUN_3.heat_credit.baseline_useful_heat_GWhth = 0 — no measured thermal sink
- RUN_4A.baseline_credit.* = 0 — no feedstock, chemistry or off-take receipt
- S02.baseline_credit = 0 — no hourly PV/load/curtailment trace
- INTEGRATED_NODE_PROFILE.green_direct_status.energy_credit = 0 — node allocation UNKNOWN

## Data required to close

### desalination

- plant-specific 2026 electricity tariff / settlement receipt
- whole-site SEC and delta_aux measurements
- current measured recovery fraction
- feed and reject stream map
- brine composition
- fouling rate and CIP history
- primary ecological monitoring data
- unused hydraulic head profile
- roof structural and interconnection limits

### compute

- CIP_temperature_setpoint
- CIP_thermal_demand
- L_IT_load_factor
- PV_curtailment
- WUE
- actual_PUE
- compute_cooling_water_source
- coolant_supply_return_temperature
- heat_pump_COP
- hourly_solar_compute_overlap
- useful_heat_capture_fraction

### biometabolic

- Node-001 feedstock allocation or on-node generation receipt
- biogas quantity and CH4 composition
- actual conversion/use path
- digestate nutrient mass and product assay
- verified reclaimed-water reuse displacement

### grid

- node allocation in MW / MWh under the direct-green pathway
- contract price and settlement rules
- eligible load set

