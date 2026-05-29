# forks/color-spectrum/README.md

STATUS: PUBLIC-CANDIDATE BRIDGE — NOT CANON
CANON: no
DEPLOYMENT: no
AUTHORITY: none
UPSTREAM: d3/d3-color (ISC License), open spectral data (public domain)
HSN_COORDINATE: H04-S08-N10

## Purpose

This bridge adapter maps the visible-light color/frequency spectrum to H04
(Color & Spectrum) seed nodes in the Atlas Lattice.

It seeds the **Rainbow Yin-Yang layer** — the chromatic surface of the lattice
that maps hue to frequency coordinates, with Riemann S as the candidate
operator for spectral structure.

## What this bridge provides

1. `data/spectrum_hsn_seed.json` — Named spectral bands + color harmonics
   mapped to H04 H-S-N coordinates.
2. `bridge/ingest_spectrum.py` — Bridge adapter that reads the seed and
   outputs lattice-compatible node records.

## Spectral band → HSN mapping

Each major spectral division becomes an H04-S06-N## node:

| Band | Wavelength (nm) | Frequency (THz) | Node | Rationale |
|---|---|---|---|---|
| Radio | 1m–100km | <0.3 | N03 | Diffuse, ambient, long-range |
| Microwave | 1mm–1m | 0.3–300 GHz | N02 | Flow, propagation medium |
| Infrared | 700–1000nm | 300–430 THz | N01 | Heat/solid-state, ground |
| Red | 620–750nm | 400–484 THz | N06 | Yang, ascending warmth |
| Orange | 590–620nm | 484–508 THz | N10 | Resonant, transitional |
| Yellow | 570–590nm | 508–526 THz | N10 | Resonant, harmonic center |
| Green | 495–570nm | 526–606 THz | N05 | Crystal/ordered, center |
| Cyan | 476–495nm | 606–630 THz | N09 | Entangled, yin-yang bridge |
| Blue | 450–476nm | 630–668 THz | N07 | Yin, receptive, deep |
| Violet | 380–450nm | 668–789 THz | N12 | Transcendent, omega |
| Ultraviolet | 10–380nm | 789 THz–30 PHz | N04 | Plasma, high-energy |
| X-ray | 0.01–10nm | 30 PHz–30 EHz | N04 | Plasma, high-energy |
| Gamma | <0.01nm | >30 EHz | N04 | Plasma, extreme |

Color harmonics (musical octave mapping):
- Rainbow 7-color octave maps to N01–N07 ascending
- The 12-tone chromatic scale maps to N01–N12

## License

Spectral data: public domain scientific reference.
d3-color mapping concepts: ISC License (d3/d3-color).
Bridge adapter: same as repository — candidate/non-canon.

## Files

| File | Purpose |
|---|---|
| `data/spectrum_hsn_seed.json` | Spectral bands + color harmonics seed |
| `bridge/ingest_spectrum.py` | Bridge adapter script |

## Usage

```bash
python forks/color-spectrum/bridge/ingest_spectrum.py --stats
```
