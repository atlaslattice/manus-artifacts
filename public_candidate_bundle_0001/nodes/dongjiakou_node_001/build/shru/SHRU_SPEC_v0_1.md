# Symbiotic Helium Recovery Unit — open interface specification v0.1

STATUS: PUBLIC REVIEW CANDIDATE | CANON: no | DEPLOYMENT: no | AUTHORITY: none | PROOF: no | REALIZED_CREDIT: 0

Prepared2026-10-09UTC /2026-10-08America/Chicago from the user's SHRU and piezo/self-healing concept handoff. Human-readable contract paired with [profile.json](profile.json). This defines a proposed interoperable module, not an industry-ratified standard, certified product, universal retrofit or commissioned unit. No external equipment is connected and no new physical stream is inserted in the Dongjiakou simulator.

## Purpose and architecture

Capture eligible helium-bearing customer streams, condition and purify them to the customer's accepted impurity specification, return qualified gas and measure fresh make-up reduction. Standardize interfaces, evidence and acceptance rather than prescribing a single vendor or universal purification recipe. The concept is complementary to primary supply recovery; Dongjiakou's actual helium feed/output remains unknown.

| Module | Required contract | Evidence needed before acceptance |
|---|---|---|
|M1 Capture/conditioning |Per-process feed ports, stream identity, ownership, flow/pressure/composition/time variability; required upstream abatement and segregation |Representative assays; process-owner permission; exhaust backpressure and compatibility evaluation; collection coverage |
|M2 Purification |Feed-specific train chosen from validated separation/purification options; product, reject and regeneration ports |Impurity-specific removal and recovery over rated conditions; energy/reagents; product qualification and residual fate |
|M3 Buffer/return |Qualified-product storage and customer return; isolation from unqualified gas; measured fresh make-up |Metered inventory, supply stability, accepted delivery purity/pressure and traceable transfer records |
|M4 Monitoring/control |Flow/composition/metrology plus suitable leak sensors; bounded PLC control and read-only AI review interface |Calibration, detection coverage/false alarms/downtime, alarm-to-repair timing, safety/failure-mode tests and independent plant protection |
|R1 Optional smart-seal research |Isolated material/coupon or dedicated research rig; sensing/healing/verification interface |Helium-specific permeability and leak tests, temperature/pressure/vacuum cycling, contamination and repeated-healing evidence; no production integration by this spec |

Do not connect incompatible CVD, etch, implant and leak-test exhaust streams merely because all can contain helium. Separate feed classes until chemistry, abatement, pressure, contamination and process requirements support combination. A pressure-driven acoustic leak detector and a composition/resonance sensor are different instruments; neither guarantees whole-system recovery. A rated enclosure size, utility demand and maintenance clearance follow sizing and hazard review.20/40ft containers and atmospheric-to15bar operation remain unverified suggestions, not mandatory defaults.

## Measurable acceptance

For each accepted operating envelope, record eligible-use coverage, collected helium, separator feed/product/reject, purity-qualified return, customer reuse, fresh make-up, vents/leaks/purges and stock change. Declare normal-volume reference conditions and mass basis. Recovery, purity and system retention are separate measures. Internal recycle is not new primary production and cannot repeatedly receive import-substitution credit.

Reported equipment efficiencies apply only to their stated boundaries. Do not multiply component efficiencies again when a supplier metric already covers the combined boundary. Establish baseline recycling before claiming incremental avoided purchases. Performance target values, achieved performance, operating hours, CAPEX/OPEX, payback and lifecycle benefits remain null pending a feed envelope, supplier proposal and measured acceptance. Broad market figures,12–18month payback, mandatory Chinese/Korean fab recovery claims and85% policy target remain unverified.

Customer acceptance specifies impurities and detection limits, not only a5N/6N headline. Qualification includes relevant particles, moisture, oxygen, nitrogen, hydrogen, neon, hydrocarbons and process-specific contaminants. Assess regeneration and rejects as well as useful product. Preserve QOL's non-compensable safety/ecology/privacy/access/water-product/maintenance gates; efficiency does not waive them.

## AI and smart-seal boundary

The AI/digital twin may review telemetry, flag anomalies, propose maintenance and prepare a source-linked receipt. Its public interface grants no actuator authority. Deterministic, independently qualified plant control and operator procedures govern isolation and equipment operation. No model output commands seal heating, chemical release, capsule injection or valve movement in this research candidate.

R1 is a research extension, with a distinct evidence class. Test actual component conditions: some gas-handling sections are near ambient temperature, while cryogenic components need their own qualified temperature envelopes. Healing demonstrated near−20°C is not validation at LNG or liquid-helium temperatures. Restored electrical continuity or visual crack closure does not establish helium tightness; verify leakage and permeability before and after healing, contaminants/outgassing/particles, thermal load, fatigue, aging, repair time and repeatability. Nanocapsules in process gas or cryogenic fluid are not approved by an untested disclosure.

A0.1% per-seal event probability produces an expected0.001×N events forN comparable seals over the stated exposure:3 for3,000seals, not thousands. A system reliability claim additionally needs exposure duration, dependence/common-cause failures and consequence analysis. No reliability rate is assumed here.

## Source and standards review

1. [Air Liquide modular helium purifier brochure](https://advancedseparations.airliquide.com/sites/alas/files/2023-11/natural-gas-helium-brochure-en-02.22-sd-1.pdf): supplier modular membrane/PSA offerings and conditional recovery/purity ranges. Natural-gas/well-feed examples do not establish contaminated fab-exhaust performance.
2. [Gadro charging/recovery system](https://www.gadrodetection.com/helium-recovery-system/): supplier workpiece leak-test recovery claims; not a whole-fab result. [Existing acoustic/patent review](../review/HELIUM_COLD_SLUDGE_REVIEW_2026-10-09.md) retains Samsung/Lam method descriptions and the corrected patent citation.
3. [Piezoelectric O-ring patent US7180227B2 / US20050156487A1](https://patents.google.com/patent/US7180227B2/en): embedded sensing of seal compression/performance in vacuum systems. Patent evidence does not prove a marketed component or a self-healing seal.
4. Luo et al., [smart-healing paper](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202513641), first onlineOctober12,2025;2026journal issue. Conductive polymer damage sensing, localized Joule heating and AI feedback; no helium containment qualification established by the retrieved abstract.
5. Kotegov, [ACTIS disclosure](https://www.tdcommons.org/dpubs_series/11509/), August27,2026: author explicitly describes a conceptual architecture before prototyping/laboratory experiments. Retain as a research lead, not a working cryogenic repair method.
6. [PIB self-healing photovoltaic sealant study](https://pubs.acs.org/doi/10.1021/am508096c): laboratory light-triggered polymer healing and oxygen/moisture barrier measurements, not measured helium impermeability or semiconductor pressure-boundary qualification.
7. [SEMI S2](https://store-us.semi.org/products/s00200-semi-s2-environmental-health-and-safety-guideline-for-semiconductor-manufacturing-equipment) covers equipment EHS considerations; [SEMI S8](https://store-us.semi.org/products/s00800-semi-s8-safety-guideline-for-ergonomics-engineering-of-semiconductor-manufacturing-equipment) concerns ergonomics. These references do not certify SHRU.
8. [SEMI F106 official listing](https://store-us.semi.org/products/f10600-semi-f106-test-method-for-determination-of-leak-integrity-of-gas-delivery-systems-by-helium-leak-detector) marksF106-0308(reapproved1012) inactive. Select an applicable active test basis with reviewers rather than asserting current compliance.
9. [ISO14644-1 official abstract](https://www.iso.org/standard/53394.html) concerns cleanroom air particle classification, not recycled helium purity. [GB/T16943-2009 official record](https://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7D22BD3A7E05397BE0A0AB82A) shows withdrawalFebruary1,2026. Resolve the applicable current product specification with the gas customer; an old identifier is not present certification.

Only public abstracts/catalogue records were reviewed for standards; full normative clauses were not purchased or reproduced. No vendor endorsement, conformity assessment or patent-rights clearance is claimed.

## Open receipt set and next demonstrator

SHRU-DR01: named customer process and baseline recycling; DR02: separate feed assays and variability; DR03: approved integration/abatement/pressure boundary; DR04: supplier-rated purification and impurity acceptance; DR05: mass-balanced return/make-up/reject telemetry; DR06: utilities, sizing, economics and maintenance; DR07: current standards and independent safety acceptance; DR08: optional smart-seal coupon data and repeated helium-tightness tests.

First demonstrator: an offline, evidence-backed feed profile and an inventory/acceptance review. Next physical step, if independently authorized, is a bounded recovery demonstration appropriate to that feed. R1 remains separate until material tests establish a useful, repeatable helium-specific result. The simulator's existing23 operating requests and QOL requests remain open.
