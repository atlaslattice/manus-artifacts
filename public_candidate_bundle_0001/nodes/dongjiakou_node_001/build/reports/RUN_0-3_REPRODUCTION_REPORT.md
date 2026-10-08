STATUS: ARCHIVE PUBLIC CANDIDATE | CANON: no | DEPLOYMENT: no | AUTHORITY: none | PROOF: no | PUBLIC_RELEASE: candidate

Historical model-generated report; see current review/EVIDENCE_APPENDIX.md.

# Run 0-3 Reproduction Report

Generated: 2026-10-08T13:07:39+00:00  
Reference head: `4756036f9c428fa3aa1d4cea552ae03367523fb5`  
Overall: **ALL_RUNS_REPRODUCED**

| Run | Title | Checks | Matched | Status |
| --- | --- | --- | --- | --- |
| RUN_0 | Desalination nameplate baseline | 19 | 19 | **REPRODUCED** |
| RUN_0.2 | Dated 2025 operating-volume calibration | 12 | 12 | **REPRODUCED** |
| RUN_1 | Rooftop PV technical sensitivity | 20 | 20 | **REPRODUCED** |
| RUN_2 | Unused-head hydro parametric sensitivity | 25 | 24 | **REPRODUCED_WITH_ANNOTATED_DIVERGENCE** |
| RUN_3 | C01 compute facility transfer function | 47 | 47 | **REPRODUCED** |
| RUN_4A | BIO01 organics and nutrient-recovery transfer functions | 20 | 20 | **REPRODUCED** |
| S02 | BESS equivalence transfer function | 12 | 12 | **REPRODUCED** |

Totals: 154/155 derived values reproduced across 7 runs.
Annotated divergences preserved (not overwritten): 1.
Unexplained divergences: 0.

## Annotated divergences

These are values where the committed artifact and the reproduced value disagree beyond machine precision. Both are preserved; the committed artifact is not overwritten.

### `stream_basis.average_flow_m3_s` (RUN_2)

- Kind: **DEFECT_IN_COMMITTED_ARTIFACT**
- Committed: `0.56855619`
- Reproduced: `0.568556570268899`
- Relative difference: `6.688e-07`
- Detail: The committed value implies 17,929,988.0 m3/year rather than the stated 17,930,000 m3/year stream basis. The correct quotient 17930000 / (365*24*3600) = 0.568556570268899 rounds to 0.56855657 at eight decimals, so 0.56855619 appears to be a digit-transposition slip (19 vs 57).
- Resolution: Preserve both values; do not overwrite the committed artifact. The divergence is isolated: the Run 2 sensitivity table is computed from the annual volume and head directly and does not consume this field, so no downstream figure is affected. Flagged for S10/GPT confirmation and recorded in the failure ledger.

## RUN_0 — Desalination nameplate baseline

Model: `run0.baseline`  
Artifact: `RUN_0_BASELINE_v0_1.json`

| Path | Committed | Reproduced | Rel. diff | Tol | Status |
| --- | --- | --- | --- | --- | --- |
| `artifact_id` | DJK-NODE-001-RUN-0-v0.1 | DJK-NODE-001-RUN-0-v0.1 | — | 0 | MATCH |
| `coefficients_per_U.annual_product_m3` | 36500000 | 36500000.0 | 0.00e+00 | 0 | MATCH |
| `coefficients_per_U.annual_process_train_energy_GWh` | 80.3 | 80.3 | 0.00e+00 | 0 | MATCH |
| `coefficients_per_U.annual_chemical_cost_CNY_upper_bound` | 5475000 | 5475000.0 | 0.00e+00 | 0 | MATCH |
| `mass_balance["0.45"].feed_m3_day` | 222222.22222222222 | 222222.22222222222 | 0.00e+00 | 0 | MATCH |
| `mass_balance["0.45"].product_m3_day` | 100000 | 100000.0 | 0.00e+00 | 0 | MATCH |
| `mass_balance["0.45"].reject_equivalent_m3_day` | 122222.22222222222 | 122222.22222222222 | 0.00e+00 | 0 | MATCH |
| `mass_balance["0.45"].annual_feed_m3_per_U` | 81111111.1111111 | 81111111.1111111 | 0.00e+00 | 0 | MATCH |
| `mass_balance["0.45"].annual_reject_equivalent_m3_per_U` | 44611111.11111111 | 44611111.11111111 | 0.00e+00 | 0 | MATCH |
| `mass_balance["0.50"].feed_m3_day` | 200000 | 200000.0 | 0.00e+00 | 0 | MATCH |
| `mass_balance["0.50"].reject_equivalent_m3_day` | 100000 | 100000.0 | 0.00e+00 | 0 | MATCH |
| `mass_balance["0.50"].annual_feed_m3_per_U` | 73000000 | 73000000.0 | 0.00e+00 | 0 | MATCH |
| `mass_balance["0.50"].annual_reject_equivalent_m3_per_U` | 36500000 | 36500000.0 | 0.00e+00 | 0 | MATCH |
| `U1_reference_not_operating_claim.annual_product_m3` | 36500000 | 36500000.0 | 0.00e+00 | 0 | MATCH |
| `U1_reference_not_operating_claim.annual_process_train_energy_GWh` | 80.3 | 80.3 | 0.00e+00 | 0 | MATCH |
| `U1_reference_not_operating_claim.annual_chemical_cost_CNY_upper_bound` | 5475000 | 5475000.0 | 0.00e+00 | 0 | MATCH |
| `retrofit_credit.S01_solar` | 0 | 0 | 0.00e+00 | 0 | MATCH |
| `retrofit_credit.C01_compute` | 0 | 0 | 0.00e+00 | 0 | MATCH |
| `retrofit_credit.resource_recovery` | 0 | 0 | 0.00e+00 | 0 | MATCH |

## RUN_0.2 — Dated 2025 operating-volume calibration

Model: `run0.operating_2025`  
Artifact: `RUN_0_OPERATING_2025_v0_2.json`

| Path | Committed | Reproduced | Rel. diff | Tol | Status |
| --- | --- | --- | --- | --- | --- |
| `artifact_id` | DJK-NODE-001-RUN-0-OPERATING-2025-v0.2 | DJK-NODE-001-RUN-0-OPERATING-2025-v0.2 | — | 0 | MATCH |
| `reported_product_supply_m3` | 17930000 | 17930000.0 | 0.00e+00 | 0 | MATCH |
| `derived_utilization_U` | 0.4912328767 | 0.4912328767123288 | 2.51e-11 | 1e-08 | MATCH |
| `derived_process_train_energy_GWh` | 39.446 | 39.446 | 0.00e+00 | 0 | MATCH |
| `derived_annual_chemical_cost_CNY_upper_bound` | 2689500 | 2689500.0 | 0.00e+00 | 0 | MATCH |
| `mass_balance_using_reported_technology_recovery_range["0.45"].annual_feed_m3` | 39844444.4444 | 39844444.44444444 | 1.12e-12 | 1e-08 | MATCH |
| `mass_balance_using_reported_technology_recovery_range["0.45"].annual_product_m3` | 17930000 | 17930000.0 | 0.00e+00 | 0 | MATCH |
| `mass_balance_using_reported_technology_recovery_range["0.45"].annual_reject_equivalent_m3` | 21914444.4444 | 21914444.44444444 | 2.03e-12 | 1e-08 | MATCH |
| `mass_balance_using_reported_technology_recovery_range["0.50"].annual_feed_m3` | 35860000 | 35860000.0 | 0.00e+00 | 0 | MATCH |
| `mass_balance_using_reported_technology_recovery_range["0.50"].annual_reject_equivalent_m3` | 17930000 | 17930000.0 | 0.00e+00 | 0 | MATCH |
| `economics.historical_2018_2020_tariff_CNY_kWh` | 0.555 | 0.555 | 0.00e+00 | 0 | MATCH |
| `economics.historical_tariff_counterfactual_only_CNY_for_2025_process_energy` | 21892530 | 21892530.000000004 | 1.70e-16 | 1e-12 | MATCH |

## RUN_1 — Rooftop PV technical sensitivity

Model: `run1_solar.run`  
Artifact: `RUN_1_SOLAR_v0_1.json`

| Path | Committed | Reproduced | Rel. diff | Tol | Status |
| --- | --- | --- | --- | --- | --- |
| `artifact_id` | DJK-NODE-001-RUN-1-SOLAR-v0.1 | DJK-NODE-001-RUN-1-SOLAR-v0.1 | — | 0 | MATCH |
| `site_inputs.desalination_workshop_footprint_m2` | 17474.32 | 17474.32 | 0.00e+00 | 0 | MATCH |
| `site_inputs.effective_active_module_coverage_fraction` | 0.6 | 0.6 | 0.00e+00 | 0 | MATCH |
| `site_inputs.active_module_area_m2` | 10484.592 | 10484.591999999999 | 1.73e-16 | 1e-12 | MATCH |
| `local_generation_reference.reference_capacity_MWp` | 12.4956 | 12.4956 | 0.00e+00 | 0 | MATCH |
| `local_generation_reference.reference_generation_MWh_year` | 14022.86 | 14022.86 | 0.00e+00 | 0 | MATCH |
| `local_generation_reference.derived_yield_kWh_per_kWp_year` | 1122.223823 | 1122.2238227856205 | 1.91e-10 | 1e-08 | MATCH |
| `cases.S01_A.module_efficiency_fraction` | 0.23 | 0.23 | 0.00e+00 | 0 | MATCH |
| `cases.S01_A.DC_capacity_MWp` | 2.41145616 | 2.4114561599999997 | 1.84e-16 | 1e-08 | MATCH |
| `cases.S01_A.annual_generation_GWh` | 2.70619355 | 2.7061935503551324 | 1.31e-10 | 1e-08 | MATCH |
| `cases.S01_A.fraction_of_2025_UF_RO_process_energy` | 0.0686050183 | 0.0686050182618043 | 5.57e-10 | 1e-08 | MATCH |
| `cases.S01_A.historical_0_555_tariff_counterfactual_CNY` | 1501937.42 | 1501937.4204470986 | 2.98e-10 | 1e-08 | MATCH |
| `cases.S01_A.location_based_CO2_avoided_tonnes_using_2023_Shandong_factor` | 1675.4 | 1675.4044270248623 | 2.64e-06 | 1e-05 | MATCH |
| `cases.S01_B_SEA_SHIELD.module_efficiency_fraction` | 0.248 | 0.248 | 0.00e+00 | 0 | MATCH |
| `cases.S01_B_SEA_SHIELD.DC_capacity_MWp` | 2.600178816 | 2.6001788159999997 | 1.71e-16 | 1e-08 | MATCH |
| `cases.S01_B_SEA_SHIELD.annual_generation_GWh` | 2.917982611 | 2.9179826108177083 | 6.25e-11 | 1e-08 | MATCH |
| `cases.S01_B_SEA_SHIELD.fraction_of_2025_UF_RO_process_energy` | 0.0739741066 | 0.07397410664751074 | 6.42e-10 | 1e-08 | MATCH |
| `cases.S01_B_SEA_SHIELD.historical_0_555_tariff_counterfactual_CNY` | 1619480.35 | 1619480.3490038281 | 6.15e-10 | 1e-08 | MATCH |
| `cases.S01_B_SEA_SHIELD.location_based_CO2_avoided_tonnes_using_2023_Shandong_factor` | 1806.52 | 1806.523034357243 | 1.68e-06 | 1e-05 | MATCH |
| `carbon_boundary.Shandong_2023_average_grid_factor_kgCO2_kWh` | 0.6191 | 0.6191 | 0.00e+00 | 0 | MATCH |

## RUN_2 — Unused-head hydro parametric sensitivity

Model: `run2_hydro.run`  
Artifact: `RUN_2_HYDRO_v0_1.json`

| Path | Committed | Reproduced | Rel. diff | Tol | Status |
| --- | --- | --- | --- | --- | --- |
| `artifact_id` | DJK-NODE-001-RUN-2-HYDRO-v0.1 | DJK-NODE-001-RUN-2-HYDRO-v0.1 | — | 0 | MATCH |
| `stream_basis.annual_volume_m3` | 17930000 | 17930000.0 | 0.00e+00 | 0 | MATCH |
| `stream_basis.average_flow_m3_s` | 0.56855619 | 0.568556570268899 | 6.69e-07 | 1e-08 | ANNOTATED_DIVERGENCE |
| `physics.rho_kg_m3` | 1000 | 1000.0 | 0.00e+00 | 0 | MATCH |
| `physics.g_m_s2` | 9.80665 | 9.80665 | 0.00e+00 | 0 | MATCH |
| `physics.ideal_energy_GWh_per_m_head_at_eta_1` | 0.0488425651 | 0.04884256513888889 | 7.96e-10 | 1e-08 | MATCH |
| `physics.illustrative_energy_GWh_per_m_head_at_eta_0_8` | 0.0390740521 | 0.03907405211111111 | 2.84e-10 | 1e-08 | MATCH |
| `physics.illustrative_average_power_kW_per_m_head_at_eta_0_8` | 4.46050823 | 4.460508231861999 | 4.17e-10 | 1e-08 | MATCH |
| `physics.illustrative_process_energy_fraction_per_m_head_at_eta_0_8` | 0.0009905707 | 0.0009905707070707072 | 7.14e-09 | 1e-08 | MATCH |
| `illustrative_eta_0_8_sensitivity[0].H_m` | 1 | 1.0 | 0.00e+00 | 0 | MATCH |
| `illustrative_eta_0_8_sensitivity[0].annual_energy_GWh` | 0.0390740521 | 0.03907405211111111 | 2.84e-10 | 1e-08 | MATCH |
| `illustrative_eta_0_8_sensitivity[0].average_power_kW` | 4.46050823 | 4.460508231861999 | 4.17e-10 | 1e-08 | MATCH |
| `illustrative_eta_0_8_sensitivity[0].fraction_of_2025_UF_RO_process_energy` | 0.0009905707 | 0.0009905707070707072 | 7.14e-09 | 1e-08 | MATCH |
| `illustrative_eta_0_8_sensitivity[1].annual_energy_GWh` | 0.1953702606 | 0.19537026055555556 | 2.27e-10 | 1e-08 | MATCH |
| `illustrative_eta_0_8_sensitivity[1].average_power_kW` | 22.30254116 | 22.302541159309996 | 3.09e-11 | 1e-08 | MATCH |
| `illustrative_eta_0_8_sensitivity[1].fraction_of_2025_UF_RO_process_energy` | 0.0049528535 | 0.004952853535353536 | 7.14e-09 | 1e-08 | MATCH |
| `illustrative_eta_0_8_sensitivity[2].annual_energy_GWh` | 0.3907405211 | 0.3907405211111111 | 2.84e-11 | 1e-08 | MATCH |
| `illustrative_eta_0_8_sensitivity[2].average_power_kW` | 44.60508232 | 44.60508231861999 | 3.09e-11 | 1e-08 | MATCH |
| `illustrative_eta_0_8_sensitivity[2].fraction_of_2025_UF_RO_process_energy` | 0.0099057071 | 0.009905707070707072 | 2.96e-09 | 1e-08 | MATCH |
| `illustrative_eta_0_8_sensitivity[3].annual_energy_GWh` | 0.7814810422 | 0.7814810422222223 | 2.84e-11 | 1e-08 | MATCH |
| `illustrative_eta_0_8_sensitivity[3].average_power_kW` | 89.21016464 | 89.21016463723998 | 3.09e-11 | 1e-08 | MATCH |
| `illustrative_eta_0_8_sensitivity[3].fraction_of_2025_UF_RO_process_energy` | 0.0198114141 | 0.019811414141414144 | 2.09e-09 | 1e-08 | MATCH |
| `illustrative_eta_0_8_sensitivity[4].annual_energy_GWh` | 1.9537026056 | 1.9537026055555555 | 2.27e-11 | 1e-08 | MATCH |
| `illustrative_eta_0_8_sensitivity[4].average_power_kW` | 223.02541159 | 223.02541159309996 | 1.39e-11 | 1e-08 | MATCH |
| `illustrative_eta_0_8_sensitivity[4].fraction_of_2025_UF_RO_process_energy` | 0.0495285354 | 0.04952853535353535 | 9.38e-10 | 1e-08 | MATCH |

## RUN_3 — C01 compute facility transfer function

Model: `run3_compute.run`  
Artifact: `RUN_3_COMPUTE_v0_2.json`

| Path | Committed | Reproduced | Rel. diff | Tol | Status |
| --- | --- | --- | --- | --- | --- |
| `artifact_id` | DJK-NODE-001-RUN-3-COMPUTE-v0.2 | DJK-NODE-001-RUN-3-COMPUTE-v0.2 | — | 0 | MATCH |
| `supersedes` | RUN_3_COMPUTE_v0_1.json | RUN_3_COMPUTE_v0_1.json | — | 0 | MATCH |
| `baseline.operating_year` | 2025 | 2025 | 0.00e+00 | 0 | MATCH |
| `baseline.UF_RO_process_energy_GWh` | 39.446 | 39.446 | 0.00e+00 | 0 | MATCH |
| `baseline.average_UF_RO_process_power_MW` | 4.5029680365 | 4.502968036529681 | 6.59e-12 | 1e-08 | MATCH |
| `baseline.S01_A_PV_GWh_year` | 2.70619355 | 2.70619355 | 0.00e+00 | 0 | MATCH |
| `baseline.S01_B_PV_GWh_year` | 2.917982611 | 2.917982611 | 0.00e+00 | 0 | MATCH |
| `reference_scenario.PUE` | 1.25 | 1.25 | 0.00e+00 | 0 | MATCH |
| `reference_scenario.load_factor_L` | 1 | 1 | 0.00e+00 | 0 | MATCH |
| `tiers[0].case_id` | C01-PILOT-100 | C01-PILOT-100 | — | 0 | MATCH |
| `tiers[0].IT_capacity_kW` | 100 | 100.0 | 0.00e+00 | 0 | MATCH |
| `tiers[0].IT_energy_GWh_at_L1` | 0.876 | 0.876 | 0.00e+00 | 0 | MATCH |
| `tiers[0].facility_energy_GWh_at_L1_PUE1` | 0.876 | 0.876 | 0.00e+00 | 0 | MATCH |
| `tiers[0].facility_energy_GWh_at_L1_PUE1_25` | 1.095 | 1.095 | 0.00e+00 | 0 | MATCH |
| `tiers[0].process_energy_share_at_PUE1` | 0.0222075749 | 0.02220757491253866 | 5.65e-10 | 1e-08 | MATCH |
| `tiers[0].process_energy_share_at_PUE1_25` | 0.0277594686 | 0.027759468640673326 | 1.47e-09 | 1e-08 | MATCH |
| `tiers[0].S01_A_annual_energy_ratio_to_facility_at_PUE1_25` | 2.4714096347 | 2.4714096347031966 | 1.29e-12 | 1e-08 | MATCH |
| `tiers[0].S01_B_annual_energy_ratio_to_facility_at_PUE1_25` | 2.6648243023 | 2.664824302283105 | 6.34e-12 | 1e-08 | MATCH |
| `tiers[0].grid_only_location_CO2_t_at_PUE1_25` | 677.9145 | 677.9145 | 0.00e+00 | 1e-08 | MATCH |
| `tiers[0].IT_heat_first_law_upper_bound_GWhth` | 0.876 | 0.876 | 0.00e+00 | 0 | MATCH |
| `tiers[1].case_id` | C01-PILOT-250 | C01-PILOT-250 | — | 0 | MATCH |
| `tiers[1].IT_capacity_kW` | 250 | 250.0 | 0.00e+00 | 0 | MATCH |
| `tiers[1].IT_energy_GWh_at_L1` | 2.19 | 2.19 | 0.00e+00 | 0 | MATCH |
| `tiers[1].facility_energy_GWh_at_L1_PUE1_25` | 2.7375 | 2.7375 | 0.00e+00 | 0 | MATCH |
| `tiers[1].process_energy_share_at_PUE1` | 0.0555189373 | 0.05551893728134665 | 3.36e-10 | 1e-08 | MATCH |
| `tiers[1].process_energy_share_at_PUE1_25` | 0.0693986716 | 0.06939867160168331 | 2.43e-11 | 1e-08 | MATCH |
| `tiers[1].S01_A_annual_energy_ratio_to_facility_at_PUE1_25` | 0.9885638539 | 0.9885638538812787 | 1.89e-11 | 1e-08 | MATCH |
| `tiers[1].S01_B_annual_energy_ratio_to_facility_at_PUE1_25` | 1.0659297209 | 1.065929720913242 | 1.24e-11 | 1e-08 | MATCH |
| `tiers[1].grid_only_location_CO2_t_at_PUE1_25` | 1694.78625 | 1694.78625 | 0.00e+00 | 1e-08 | MATCH |
| `tiers[2].case_id` | C01-500 | C01-500 | — | 0 | MATCH |
| `tiers[2].IT_capacity_kW` | 500 | 500.0 | 0.00e+00 | 0 | MATCH |
| `tiers[2].facility_energy_GWh_at_L1_PUE1_25` | 5.475 | 5.475 | 0.00e+00 | 0 | MATCH |
| `tiers[2].process_energy_share_at_PUE1_25` | 0.1387973432 | 0.13879734320336662 | 2.43e-11 | 1e-08 | MATCH |
| `tiers[2].S01_A_annual_energy_ratio_to_facility_at_PUE1_25` | 0.4942819269 | 0.4942819269406393 | 8.22e-11 | 1e-08 | MATCH |
| `tiers[2].S01_B_annual_energy_ratio_to_facility_at_PUE1_25` | 0.5329648605 | 0.532964860456621 | 8.14e-11 | 1e-08 | MATCH |
| `tiers[2].grid_only_location_CO2_t_at_PUE1_25` | 3389.5725 | 3389.5725 | 0.00e+00 | 1e-08 | MATCH |
| `tiers[3].case_id` | C01-1000 | C01-1000 | — | 0 | MATCH |
| `tiers[3].IT_capacity_kW` | 1000 | 1000.0 | 0.00e+00 | 0 | MATCH |
| `tiers[3].facility_energy_GWh_at_L1_PUE1_25` | 10.95 | 10.95 | 0.00e+00 | 0 | MATCH |
| `tiers[3].process_energy_share_at_PUE1_25` | 0.2775946864 | 0.27759468640673324 | 2.43e-11 | 1e-08 | MATCH |
| `tiers[3].S01_A_annual_energy_ratio_to_facility_at_PUE1_25` | 0.2471409635 | 0.24714096347031966 | 1.20e-10 | 1e-08 | MATCH |
| `tiers[3].S01_B_annual_energy_ratio_to_facility_at_PUE1_25` | 0.2664824302 | 0.2664824302283105 | 1.06e-10 | 1e-08 | MATCH |
| `tiers[3].grid_only_location_CO2_t_at_PUE1_25` | 6779.145 | 6779.145 | 0.00e+00 | 1e-08 | MATCH |
| `anti_double_counting.existing_S01_PV_is_incremental_to_node` | False | False | 0.00e+00 | 0 | MATCH |
| `heat_credit.baseline_useful_heat_GWhth` | 0 | 0 | 0.00e+00 | 0 | MATCH |
| `result.C01_is_energy_source` | False | False | 0.00e+00 | 0 | MATCH |
| `result.C01_net_positive` | NOT_PROVEN | NOT_PROVEN | — | 0 | MATCH |

## RUN_4A — BIO01 organics and nutrient-recovery transfer functions

Model: `run4a_biometabolic.run`  
Artifact: `RUN_4A_BIOMETABOLIC_v0_1.json`

| Path | Committed | Reproduced | Rel. diff | Tol | Status |
| --- | --- | --- | --- | --- | --- |
| `artifact_id` | DJK-NODE-001-RUN-4A-BIOMETABOLIC-v0.1 | DJK-NODE-001-RUN-4A-BIOMETABOLIC-v0.1 | — | 0 | MATCH |
| `local_food_waste_reference.cumulative_food_waste_tonnes` | 260000 | 260000.0 | 0.00e+00 | 0 | MATCH |
| `local_food_waste_reference.cumulative_biogas_m3` | 5260000 | 5260000.0 | 0.00e+00 | 0 | MATCH |
| `local_food_waste_reference.derived_reference_biogas_m3_tonne` | 20.2307692308 | 20.23076923076923 | 1.52e-12 | 1e-08 | MATCH |
| `food_waste_transfer_function.illustrative_cases[0].feed_tonnes_day` | 1 | 1.0 | 0.00e+00 | 0 | MATCH |
| `food_waste_transfer_function.illustrative_cases[0].annual_feed_tonnes` | 365 | 365.0 | 0.00e+00 | 0 | MATCH |
| `food_waste_transfer_function.illustrative_cases[0].reference_biogas_m3_year` | 7384.23076923 | 7384.230769230769 | 1.04e-13 | 1e-08 | MATCH |
| `food_waste_transfer_function.illustrative_cases[1].annual_feed_tonnes` | 1825 | 1825.0 | 0.00e+00 | 0 | MATCH |
| `food_waste_transfer_function.illustrative_cases[1].reference_biogas_m3_year` | 36921.1538462 | 36921.153846153844 | 1.25e-12 | 1e-08 | MATCH |
| `food_waste_transfer_function.illustrative_cases[2].annual_feed_tonnes` | 3650 | 3650.0 | 0.00e+00 | 0 | MATCH |
| `food_waste_transfer_function.illustrative_cases[2].reference_biogas_m3_year` | 73842.3076923 | 73842.30769230769 | 1.04e-13 | 1e-08 | MATCH |
| `food_waste_transfer_function.illustrative_cases[3].annual_feed_tonnes` | 9125 | 9125.0 | 0.00e+00 | 0 | MATCH |
| `food_waste_transfer_function.illustrative_cases[3].reference_biogas_m3_year` | 184605.769231 | 184605.76923076922 | 1.25e-12 | 1e-08 | MATCH |
| `food_waste_transfer_function.illustrative_cases[4].annual_feed_tonnes` | 18250 | 18250.0 | 0.00e+00 | 0 | MATCH |
| `food_waste_transfer_function.illustrative_cases[4].reference_biogas_m3_year` | 369211.538462 | 369211.53846153844 | 1.25e-12 | 1e-08 | MATCH |
| `wastewater_transfer_function.theoretical_methane_ceiling_STP_m3_per_kg_biodegradable_COD_removed` | 0.35 | 0.35 | 0.00e+00 | 0 | MATCH |
| `baseline_credit.food_waste_feed_tonnes_day` | 0 | 0 | 0.00e+00 | 0 | MATCH |
| `baseline_credit.biogas_m3_year` | 0 | 0 | 0.00e+00 | 0 | MATCH |
| `baseline_credit.struvite_credit` | 0 | 0 | 0.00e+00 | 0 | MATCH |
| `baseline_credit.compost_credit` | 0 | 0 | 0.00e+00 | 0 | MATCH |

## S02 — BESS equivalence transfer function

Model: `s02_bess.run`  
Artifact: `S02_BESS_TRANSFER_FUNCTION_v0_1.json`

| Path | Committed | Reproduced | Rel. diff | Tol | Status |
| --- | --- | --- | --- | --- | --- |
| `artifact_id` | DJK-NODE-001-S02-BESS-v0.1 | DJK-NODE-001-S02-BESS-v0.1 | — | 0 | MATCH |
| `baseline_credit` | 0 | 0 | 0.00e+00 | 0 | MATCH |
| `S01_annual_generation_GWh.A` | 2.70619355 | 2.70619355 | 0.00e+00 | 0 | MATCH |
| `S01_annual_generation_GWh.B` | 2.917982611 | 2.917982611 | 0.00e+00 | 0 | MATCH |
| `average_solar_energy_MWh_day.A` | 7.414228904 | 7.414228904109589 | 1.48e-11 | 1e-08 | MATCH |
| `average_solar_energy_MWh_day.B` | 7.994472907 | 7.994472906849315 | 1.88e-11 | 1e-08 | MATCH |
| `intuitive_energy_only_equivalence[0].BESS_MWh` | 4 | 4.0 | 0.00e+00 | 0 | MATCH |
| `intuitive_energy_only_equivalence[0].days_of_average_S01_A` | 0.5395 | 0.5395031704217904 | 5.88e-06 | 0.0001 | MATCH |
| `intuitive_energy_only_equivalence[0].days_of_average_S01_B` | 0.5003 | 0.5003456821490977 | 9.13e-05 | 0.0001 | MATCH |
| `intuitive_energy_only_equivalence[1].BESS_MWh` | 8 | 8.0 | 0.00e+00 | 0 | MATCH |
| `intuitive_energy_only_equivalence[1].days_of_average_S01_A` | 1.079 | 1.0790063408435808 | 5.88e-06 | 0.0001 | MATCH |
| `intuitive_energy_only_equivalence[1].days_of_average_S01_B` | 1.0007 | 1.0006913642981954 | 8.63e-06 | 0.0001 | MATCH |

