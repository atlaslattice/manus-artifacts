---
artifact_id: SYNTHESIS-FORK-REGISTRY-2026-05-29
title: Fork & Synthesis Registry — H-S-N Seed Upstreams
status: CANDIDATE
owner: atlaslattice
created: 2026-05-29
last_updated: 2026-05-29
source_of_truth: GitHub
canon: "NO"
domain: synthesis
hsn_coordinate: H12-S01-N01
---
# Fork & Synthesis Registry — H-S-N Seed Upstreams

> **STATUS:** CANDIDATE | **CANON:** NO | **AUTHORITY:** NONE

This registry tracks external open-source upstreams that have been adapted into
Atlas Lattice H-S-N seed data. Each entry records provenance, license, adapter
mapping, and review state.

---

## Registered Upstreams

### 1. Periodic Table JSON

| Field | Value |
|---|---|
| upstream | `Bowserinator/Periodic-Table-JSON` |
| license | MIT |
| lattice domain | H01 — Elements & Isotopes |
| adapter | `archive/synthesis/data/elements_hsn_seed.json` |
| review_state | candidate |
| receipt | `archive/synthesis/receipts/RECEIPT_PERIODIC_TABLE_2026-05-29.md` |

**H-S-N mapping:**
- H = 01 (Elements & Isotopes domain)
- S = element period number (S01–S07; lanthanides S08, actinides S09)
- N = group number capped to 1–12 (groups 13–18 → N01–N06)

**Theoretical extension (elements 119–144):**
- S10: period 8 s-block (119 Uue, 120 Ubn) — N01–N02
- S11: superactinides first 12 (121–132) — N01–N12
- S12: superactinides 133–138 + period 8 d-block 139–144 — N01–N12
- All 26 entries marked `"theoretical": true` and `"canon": "NO"`
- Source: IUPAC systematic naming convention (candidate only — not yet synthesized)
- Total: **144 elements** filling one full H01 face (12 × 12 = 144 addressable cells)

### 2. Frequency Spectrum Bands

| Field | Value |
|---|---|
| upstream | ITU-R band designations (public domain) |
| license | public domain |
| lattice domain | H02 — Frequency & Resonance |
| adapter | `archive/synthesis/data/frequency_hsn_seed.json` |
| review_state | candidate |
| receipt | `archive/synthesis/receipts/RECEIPT_FREQUENCY_SPECTRUM_2026-05-29.md` |

**H-S-N mapping:**
- H = 02 (Frequency & Resonance domain)
- S = spectrum band family (S01 radio, S02 microwave, S03 IR, S04 visible, S05 UV, S06 X-ray, S07 gamma, S08 infrasound, S09 audible, S10 ultrasound, S11 Schumann, S12 gravitational)
- N = sub-band within family

### 3. Color Harmonic Spectrum

| Field | Value |
|---|---|
| upstream | CIE standard observer data (public domain) + `colour-science/colour` mappings |
| license | public domain / BSD-3 |
| lattice domain | H03 — Color & Harmonic Spectrum |
| adapter | `archive/synthesis/data/color_hsn_seed.json` |
| review_state | candidate |
| receipt | `archive/synthesis/receipts/RECEIPT_COLOR_HARMONIC_2026-05-29.md` |

**H-S-N mapping:**
- H = 03 (Color & Harmonic Spectrum domain)
- S = color family (S01 red, S02 orange, S03 yellow, S04 green, S05 cyan, S06 blue, S07 violet, S08 IR-adjacent, S09 UV-adjacent, S10 white/broadband, S11 black/null, S12 harmonic overlay)
- N = shade / harmonic variant (N01 fundamental, N02–N12 harmonics/shades)

### 4. Acoustic Resonance Reference

| Field | Value |
|---|---|
| upstream | `librosa/librosa` frequency constants (ISC license) + ANSI acoustic bands |
| license | ISC / public domain |
| lattice domain | H04 — Acoustic Resonance |
| adapter | `archive/synthesis/data/acoustic_hsn_seed.json` |
| review_state | candidate |
| receipt | `archive/synthesis/receipts/RECEIPT_ACOUSTIC_RESONANCE_2026-05-29.md` |

**H-S-N mapping:**
- H = 04 (Acoustic Resonance domain)
- S = octave band (S01 = sub-bass, …, S08 = high treble; S09–S12 = ultrasound octaves)
- N = note within octave (N01=C, N02=C#, N03=D, N04=D#, N05=E, N06=F, N07=F#, N08=G, N09=G#, N10=A, N11=A#, N12=B)

---

## Coordinate Boundary

```text
These are candidate coordinate assignments.
Coordinate ≠ canon.  Coordinate ≠ proof.
All mappings require review before carrying scientific weight.
```

## Open Source Credits

| Project | Author | License |
|---|---|---|
| Periodic-Table-JSON | Bowserinator | MIT |
| colour-science/colour | colour-science contributors | BSD-3 |
| librosa | librosa contributors | ISC |
| ITU-R band table | ITU | public domain |
| CIE standard observer | CIE | public domain |
