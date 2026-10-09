# Atlas v0.7 fixture and negative-test plan

**Status:** proposal for review; no simulator code changed. The v0.2-proposal schema and synthetic fixtures are intentionally additive to v0.1.

## Positive structural and arithmetic checks
1. Validate the eligible residue fixture against the proposal schema.
2. Confirm 1,250 wet t × 0.8 dry fraction = 1,000 dry t.
3. Confirm allocatable dry matter = 1,000 − 400 soil/ecological reserve − 200 existing obligation − 100 collection loss = 300 dry t.
4. Confirm allocated routes sum to 300 dry t.
5. Confirm constituent balances reconcile: 63 C input = 30 product + 25 residual + 8 emissions; dry matter 300 = 90 + 195 + 15.
6. Confirm all credits remain zero and all evidence remains synthetic/unknown.

## Required negative tests
- Reject the dedicated-crop fixture because a dedicated energy crop is allocated to SAF while waste_only_base_case=true.
- Reject an unknown feedstock class treated as eligible without an explicit evidence receipt and policy review.
- Reject duplicate lot IDs, allocation IDs, source receipts or overlapping allocation records.
- Reject allocation sum above allocatable mass; reject negative quantities and dry-matter fraction outside [0,1].
- Reject qualified dry mass inconsistent with wet mass × dry fraction.
- Reject current-use quantity not represented in obligations or double-subtracted.
- Reject constituent balance where input differs from products + residuals + emissions + unaccounted beyond declared tolerance.
- Reject a missing basis/unit on gas volume or mixed Nm3, Sm3, bcm and mass-tonne calculations.
- Reject conversion of NBS natural-gas import mass into bcm without a declared composition/density/standard state.
- Reject an agronomy yield stack with duplicated trial population or overlap group and no factorial interaction evidence.
- Reject 20 bcm/y policy target as observed output; reject built capacity as actual production.
- Reject an LNG extraction claim that omits recovered ethane energy from replacement-heat accounting.
- Reject positive resilience credit when probability period or event severity is missing; reject full national GDP loss as project-avoided loss without sector coverage.
- Reject SHRU recovery claim that mixes inlet basis, purity, recovery, pressure or boundary; acoustic detection may not be labeled as sealing.
- Reject sludge/ash construction pathway if treatment, source-specific contaminant assay, leaching, durability, or product acceptance is UNKNOWN/FAIL.
- Reject any credit when ecological veto or data-rights gate is BLOCKED/UNKNOWN.
- Reject duplicate domestic value added, avoided disposal fee, tax transfer, carbon credit or QOL co-benefit across ledgers.

## Cross-ledger checks before simulator integration
Schema validation is necessary but insufficient. Add a deterministic validator for IDs, units, period conversion, conservation, attribution, overlap groups and credit gates. Preserve existing reproduce/validate/current outputs. Add golden tests against pinned baseline commit 85f06406c724067ef917c55761ba5ff4354409ef before adapter work.
