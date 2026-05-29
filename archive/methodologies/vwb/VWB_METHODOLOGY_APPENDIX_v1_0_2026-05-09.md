# VWB Methodology Appendix v1.0

**Subtitle:** Contracted-Acreage Water Positivity and Water Enrichment Credit Issuance Under ORCS  
**Date:** 2026-05-09  
**Status:** Candidate methodology appendix / not canon / not an issued credit standard  
**Scope:** Volumetric Water Benefit, Water Positivity Index, Water Enrichment Credits, ORCS, contracted acreage, farmer-protective measurement infrastructure  
**Convenor:** Dave Sheldon / Atlas Lattice  
**Mathematical refinement:** GPT  
**Structural hardening:** Claude  
**Council context:** Gemini / Copilot / GitHub / other Council reviewers where relevant  

## Evidence Boundary

```text
methodology appendix = candidate technical methodology
model review = evaluator signal
contract template = implementation scaffold
credit issuance = requires verified measurement and governance approval
canon = only after Council / human-root review
```

Do not claim this appendix by itself creates, issues, verifies, sells, or retires Water Enrichment Credits.

## 1. Purpose and Scope

This appendix defines a candidate methodology for calculating **Volumetric Water Benefit (VWB)** and facility-level **Water Positivity Index (WPI_facility)** for ORCS-style regenerative compute / water / agriculture deployments using contracted acreage.

The core purpose is to prevent vague “water positive” claims by requiring:

- explicit formula terms
- auditable measurement protocols
- facility-vs-basin metric separation
- contract-based adoption evidence
- seasonal use verification
- credit issuance rules
- known limitations

This methodology is designed for **contracted-acreage water positivity**, not full basin hydrology.

## 2. Canonical VWB Formula

The canonical formula should remain clean:

```math
VWB = (W_r \cdot \eta_t \cdot \gamma_r \cdot \lambda_r) + (W_{baseline} \cdot \alpha \cdot \beta \cdot S_f \cdot \lambda_a) - W_c
```

Where:

- the first term measures recovered/reused water benefit
- the second term measures avoided conventional water demand through contracted agricultural substitution
- the final term subtracts facility water consumption

This is the public/canonical API layer.

## 3. Variable Definitions

| Variable | Meaning | Notes |
|---|---|---|
| `VWB` | Volumetric Water Benefit | Net water benefit credited to the facility/project. |
| `W_r` | Recovered water volume | Treated/recovered water available for beneficial use. |
| `η_t` | Treatment efficiency | Fraction meeting applicable quality/use threshold. |
| `γ_r` | Reuse eligibility factor | Fraction of recovered water eligible for counted reuse. |
| `λ_r` | Recovered-water delivery effectiveness factor | Composite adjustment for distribution, pumping, and storage losses. |
| `W_baseline` | Baseline conventional water demand | Baseline water use for the contracted acreage/practice displaced. |
| `α` | Adoption factor | Fraction of contracted acreage/practice actually adopted. |
| `β` | Substitution efficiency | Effectiveness of replacement water/practice vs conventional baseline. |
| `S_f` | Seasonal fulfillment factor | Fraction of seasonal timing/delivery/use requirement fulfilled. |
| `λ_a` | Agricultural delivery/use effectiveness factor | Composite adjustment for distribution, emitter, storage, and evaporation losses. |
| `W_c` | Facility water consumption | Total facility water consumption that must be subtracted. |

## 4. Measurement Protocols

### 4.1 Recovered Water Term

For:

```math
W_r \cdot \eta_t \cdot \gamma_r \cdot \lambda_r
```

Required evidence:

- flow meter records for recovered water
- treatment-quality sampling logs
- reuse eligibility classification
- distribution/pumping/storage loss measurements or conservative assumptions
- timestamped delivery records
- audit trail linking recovered volume to beneficial use

### 4.2 Agricultural Avoidance Term

For:

```math
W_{baseline} \cdot \alpha \cdot \beta \cdot S_f \cdot \lambda_a
```

Required evidence:

- contracted acreage records
- baseline crop/practice water use model
- farmer adoption records
- substitution practice documentation
- seasonal delivery/use records
- field verification or remote sensing where appropriate
- delivery-loss adjustment
- contract compliance logs

### 4.3 Facility Consumption Term

For:

```math
W_c
```

Required evidence:

- facility water meters
- source category: municipal / groundwater / surface / recycled / other
- cooling/process/domestic split where applicable
- monthly and annual totals
- anomalies and maintenance events

## 5. λ Decomposition

The clean canonical formula should publish `λ_r` and `λ_a`, while the appendix exposes their internal implementation layers.

### 5.1 Recovered-Water Delivery Effectiveness

```math
\lambda_r = \lambda_{r,distribution} \cdot \lambda_{r,pumping} \cdot \lambda_{r,storage}
```

Where:

| Component | Meaning |
|---|---|
| `λ_r,distribution` | Loss/efficiency factor across recovered-water distribution network. |
| `λ_r,pumping` | Pumping system delivery reliability/efficiency adjustment. |
| `λ_r,storage` | Storage loss/spillage/availability adjustment. |

### 5.2 Agricultural Delivery / Use Effectiveness

```math
\lambda_a = \lambda_{a,distribution} \cdot \lambda_{a,emitter} \cdot \lambda_{a,storage} \cdot \lambda_{a,evaporation}
```

Where:

| Component | Meaning |
|---|---|
| `λ_a,distribution` | Delivery network loss/efficiency factor to contracted acreage. |
| `λ_a,emitter` | Irrigation emitter/application efficiency factor. |
| `λ_a,storage` | Storage availability/loss factor before field use. |
| `λ_a,evaporation` | Evaporation/weather-adjusted loss factor. |

### 5.3 API / Internals Principle

```text
Clean API. Inspectable internals.
```

The canonical methodology should expose the clean formula for communication and registry use, while auditors/operators can inspect λ subcomponents in project appendices.

## 6. WPI_facility vs WPI_basin

Claude’s refinement is adopted: WPI must be split into facility and basin metrics.

### 6.1 Facility Water Positivity Index

```math
WPI_{facility} = \frac{VWB_{contracted}}{W_w}
```

Where:

- `VWB_contracted` is VWB generated through the contracted project boundary.
- `W_w` is project/facility water demand.

Interpretation:

```text
WPI_facility measures facility-level water-positive performance against project demand.
```

A facility may be water-positive within the contracted methodology boundary without proving basin-wide water positivity.

### 6.2 Basin Water Positivity Index

```math
WPI_{basin}
```

Reserved for a later basin hydrology model.

`WPI_basin` must account for basin-scale hydrology, return flows, groundwater dynamics, seasonal scarcity, third-party impacts, ecological flow requirements, rebound effects, and governance constraints.

### 6.3 Anti-PR-Blur Guardrail

Do not allow generic “WPI” branding to imply basin-level benefit.

Required public language:

```text
This project reports WPI_facility. It does not claim WPI_basin unless a separate basin hydrology model has been completed and reviewed.
```

## 7. Contract Architecture as Measurement Infrastructure

Doctrine 16 candidate:

```text
Contract Architecture as Measurement Infrastructure
```

The farmer contract is not only ethics or procurement. It is part of the measurement system.

A farmer-protective contracted-acreage bundle proves or supports:

- `α` adoption
- `β` substitution efficiency
- `S_f` seasonal delivery/use
- WEC eligibility
- community legitimacy
- dispute resolution
- compensation integrity
- auditability

## 8. Eight-Element Farmer-Protective Bundle

A contract architecture suitable for VWB/WEC issuance should include at minimum:

1. **Clear acreage/practice definition**
   - which parcels/practices are enrolled
   - what baseline is being displaced

2. **Adoption evidence clause**
   - required records, inspections, or remote-sensing evidence for `α`

3. **Substitution efficiency clause**
   - practice-specific evidence for `β`
   - conservative defaults where evidence is incomplete

4. **Seasonal delivery/use clause**
   - timing and volume records for `S_f`

5. **Farmer compensation and floor protection**
   - avoids extracting water value without fair payment

6. **No-harm / fallback clause**
   - protects farmers against delivery failure, crop risk, or infrastructure malfunction

7. **Audit and data-rights clause**
   - defines what data can be collected, shared, anonymized, or published

8. **Dispute and community legitimacy clause**
   - local resolution path
   - community/association engagement where applicable

## 9. WEC Issuance Rules

Water Enrichment Credits should not issue from projected or rhetorical benefits alone.

Minimum WEC issuance requirements:

```text
measured W_r or verified baseline displacement
validated treatment/use eligibility
verified contracted acreage adoption
seasonal fulfillment evidence
λ component assumptions disclosed
facility consumption subtracted
double-counting check
public/private data boundary respected
audit record created
human-root / governance review completed
```

### 9.1 Credit Boundary

Credits are issued only for the project boundary and time period measured.

### 9.2 Conservative Defaults

Where evidence is incomplete, use conservative default factors or mark credits as pending/unissued.

### 9.3 No Double Counting

The same VWB volume cannot be claimed by multiple facilities, farmers, agencies, or registries.

## 10. Audit Cadence

Recommended cadence:

| Audit Type | Frequency | Purpose |
|---|---|---|
| Meter reconciliation | monthly | Confirm `W_r`, `W_c`, delivery totals. |
| Treatment-quality verification | monthly or per permit | Confirm `η_t` and use eligibility. |
| Contract/adoption audit | seasonal | Confirm `α`. |
| Substitution-efficiency review | seasonal/annual | Confirm or update `β`. |
| λ component review | seasonal/annual | Confirm delivery/use loss factors. |
| WEC issuance audit | per issuance batch | Confirm credit eligibility. |
| Basin risk review | annual or project change | Prevent facility claims from drifting into basin claims. |

## 11. Known Limitations

This methodology does not by itself prove:

- basin-wide water positivity
- ecological restoration
- aquifer recovery
- regulatory approval
- social legitimacy beyond contracted participants
- long-term hydrological permanence
- physical deployment readiness
- credit market acceptance

Known risks:

- baseline inflation
- rebound effects
- seasonal mismatch
- double counting
- delivery loss underestimation
- farmer data extraction
- PR misuse of `WPI_facility` as basin-scale claim
- carbon/water credit stacking confusion

## 12. Co-Attribution and Provenance

This appendix should not be presented as a single-model artifact.

Recommended provenance line:

```text
Convenor: Dave Sheldon / Atlas Lattice
Mathematical refinement: GPT
Structural hardening: Claude
Council context: Gemini / Copilot / GitHub / other reviewers where relevant
```

## 13. Strongest Safe Claim

> VWB Methodology Appendix v1.0 defines a candidate contracted-acreage water-positivity methodology under ORCS, with a clean canonical formula, inspectable λ decomposition, facility-vs-basin metric separation, contract-based measurement infrastructure, and WEC issuance guardrails. It does not by itself issue credits, prove basin positivity, or establish deployment readiness.

## 14. Promotion Requirements

Before promotion beyond candidate methodology:

```text
[ ] S1/GPT claim calibration review
[ ] S2/Claude constitutional/legal wording review
[ ] S3/Grok adversarial baseline/double-counting review
[ ] S4/Gemini simulation/measurement protocol review
[ ] S5/DeepSeek sovereignty/local-water-governance review where applicable
[ ] S7/Copilot schema/test implementation review
[ ] S10 ruling on credit issuance status labels
[ ] human-root review
```

## Status

Candidate methodology appendix. Not canon. No credits issued by this artifact.
