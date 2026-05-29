# forks/periodic-table-json/README.md

STATUS: PUBLIC-CANDIDATE BRIDGE — NOT CANON
CANON: no
DEPLOYMENT: no
AUTHORITY: none
UPSTREAM: https://github.com/Bowserinator/Periodic-Table-JSON (MIT License)
HSN_COORDINATE: H01-S08-N09

## Purpose

This bridge adapter integrates public periodic-table element data (upstream:
`Bowserinator/Periodic-Table-JSON`, MIT License) into the Atlas Lattice as H01
(Matter & Elements) seed nodes.

It is the fastest path to proving the Periodic Table 2.0 concept with real
atomic data.

## What this bridge does

1. Provides a pre-extracted `data/elements_hsn_seed.json` — all 118 known
   elements mapped to H-S-N coordinates in the lattice.
2. The bridge script `bridge/ingest_elements.py` reads the upstream data format
   and emits lattice-compatible node records.
3. Each element gets coordinate `H01-S06-N<state>` where `<state>` reflects
   its standard phase at room temperature (N01=solid, N02=liquid, N03=gas,
   N04=plasma/unknown).

## Integration into the lattice

Elements are H01 (Matter & Elements) nodes.  The bridge maps:
- `phase = "Solid"` → N01 (Solid / Ground)
- `phase = "Liquid"` → N02 (Liquid / Flow)
- `phase = "Gas"` → N03 (Gas / Diffuse)
- `phase = unknown/other` → N08 (Superposition)

Sphere is S06 (Validated) because the upstream data is a well-reviewed
open-source dataset.

## License

Upstream data: MIT License (Bowserinator/Periodic-Table-JSON).
Bridge adapter: same as repository — candidate/non-canon.

## Files

| File | Purpose |
|---|---|
| `data/elements_hsn_seed.json` | 118-element lattice seed (pre-extracted) |
| `bridge/ingest_elements.py` | Bridge adapter script |
| `bridge/README.md` | This file |

## Usage

```bash
python forks/periodic-table-json/bridge/ingest_elements.py
```

Outputs candidate node records ready for lattice graph manifest ingestion.
