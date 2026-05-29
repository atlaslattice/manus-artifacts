# TIDELOCKBrain Ingestion Pilot

```text
STATUS: INGESTION PILOT SCAFFOLD — CANDIDATE — NOT CANON
PURPOSE: define minimum receipt-first pilot structure for TIDELOCK lane
```

## Pilot sequence

```text
raw/source capture
-> source record
-> parsed events/claims
-> memory packet candidate
-> squad/index visibility update
```

## Compatibility rule

Use existing ingest lane paths (`archive/ingest/...`) for parsed packet outputs.
Use this folder as seat-local organization only.
