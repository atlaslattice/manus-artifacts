# Stars 2.0 — OIST macroscopic spin-force observation (external evidence pocket)

**Recorded:** 2026-10-10  
**Status:** EXTERNAL_REPORTED_MEASUREMENT / RESEARCH_NOTE / NON_CANON  
**Atlas deployment:** NONE  
**Deuteron energy-harvest validation:** NONE  
**Change type:** Additive source note. No alteration to the spin-1 ergotropy simulator or physics assumptions.

## Original sources and provenance

- Nayak, A.; Kim, D.; Tian, S.; Twamley, J. (2026), *Spin-force from a Nitrogen-Vacancy ensemble drives a 100 mg levitated resonator*, **Science Advances** (7 October 2026). DOI: https://doi.org/10.1126/sciadv.aeh0566
- OIST institute release (8 October 2026): https://www.oist.jp/news-center/news/2026/10/8/first-observation-quantum-spins-shifting-centimeter-scale-object-lab
- Preprint (18 May 2026): https://arxiv.org/abs/2605.17750
- Research data/analysis archive: https://doi.org/10.5061/dryad.4xgxd25q4
- Secondary article brought into this research conversation: https://www.sciencealert.com/for-the-first-time-ever-quantum-spins-shift-a-centimeter-scale-object

## What the external experiment reports

- **Carrier:** electron spins associated with nitrogen-vacancy (NV) defect centers in diamond, not deuteron nuclear spins.
- **Suspension:** a **diamagnetically levitated graphite plate**, connected by a carbon-fiber rod to an NV-containing diamond near a magnet; not acoustic levitation.
- **Drive:** repeated optical spin initialization/polarization, using a pulsed green laser (OIST describes 50 mW).
- **Coupling:** spin-dependent magnetic force in an applied field gradient exerts mechanical force on the connected assembly.
- **Measurement:** interferometric center-of-mass displacement in a **128 mg** oscillator, with reported amplitudes **exceeding 100 nm**.
- **Interpretation:** demonstrated, externally driven spin-to-macroscopic-motion coupling. It is not a demonstration of gravitational quantum superposition, power generation, or extraction of net-positive work.

The paper title's `100 mg` is a rounded mass class; the preprint and data describe 128 mg.

## Relation to existing deuteron hypothesis

| Comparison | OIST (reported) | Stars 2.0 deuteron proposal |
| --- | --- | --- |
| Spin | NV-associated electron spins | deuteron nuclear spin, I=1 |
| Support | diamagnetic levitation | proposed acoustic/vibroacoustic suspension |
| Excitation | pulsed optical pumping | proposed magnetic/resonant excitation |
| Output | measured spin-driven displacement | hypothesized kinetic/electrical recovery |
| Net power | not demonstrated | unverified |
| Fusion | not required for reported movement | not part of proposed spin-harvest mechanism |

Transfer of OIST's force magnitude to deuterons is **NOT ESTABLISHED**. Electron and nuclear magnetic moments, polarization efficiency, coupling geometry, gradients, damping, and drive losses differ substantially. Resemblance is a lead for conventional physics simulation, not evidence for an anomalous energy source.

## Energy accounting boundary

External input to spin preparation and periodic driving is explicit. A force and a displacement alone do not establish harvested work or cyclic net electrical output.

For a hypothetical full cycle, distinguish:

`E_drive + E_controls + E_suspension + E_reset + E_other ` versus `E_recovered`.

Any net-positive claim needs calibrated energy input/output, proper cycle boundaries, losses, and an identified energy reservoir. The OIST research reports neither such a net-positive cycle nor deuteron harvesting.

Existing Atlas conventional baseline remains authoritative for the proposed spin-1 model:

- `gamma_d/(2*pi) ≈ 6.53569 MHz/T`
- `ΔE = h * (gamma_d/(2*pi)) * B`
- thermal-equilibrium spin-state **ergotropy = 0**;
- nonpassive prepared states may contain extractable work, but preparation/reset cannot be ignored.

See `README.md` and `simulate_deuteron_spin_ergotropy_v0_1.py` in this directory.

## Archival decision

**Include as:** external experimental analogue — spin-dependent mechanical coupling at macroscopic resonator mass.  
**Do not promote to:** demonstration of deuteron spin harvesting; acoustic levitation result; self-powered spin device; net energy; physics breakthrough for Stars 2.0; Atlas deployment.  
**Follow-up:** optional literature comparison in future; no new simulation, lab work, expenses, or inference job authorized by this receipt.

**Status:** EXTERNAL EVIDENCE · ANALOGUE ONLY · NON_CANON · ZERO REALIZED CREDIT.
