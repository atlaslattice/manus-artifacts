# v2.1 Wire / Overlay Integrity Scan

```text
STATUS: INTEGRITY SCAN — CANDIDATE — NOT CANON
PURPOSE: simulated/mental audit pass on v2.1 wire and overlay boundary claims
ISSUE: manus-artifacts#97
DEPLOYMENT: no
AUTHORITY: none
```

## 0. Scope

This scan evaluates the stated posture, not the undiscovered source files.

Repository search did not locate the asserted vaulted v2.1 source filenames at scan time. Therefore this scan is a boundary-hygiene review of the current described state, not checksum verification.

## 1. Confirmed separation

```text
Wire Spec = packet gating / low-level coordinate mechanics
Creative Overlay = inspirational and interpretive guidance
D0/Z0 manifest = external provenance surface
z = 0 = valid wire coordinate
```

## 2. Boundary checks

| Check | Result | Notes |
|---|---|---|
| Wire spec treated as canon? | pass | marked not canon |
| Wire spec treated as deployed? | pass | no deployment claim |
| Overlay treated as executable? | pass | explicitly non-executable |
| Overlay merged with wire semantics? | pass_with_watch | must continue to keep separated |
| D0/Z0 manifest treated as authority? | pass_with_watch | external receipt surface only |
| z=0 erased as null? | pass | explicitly preserved as valid coordinate |
| Checksums available? | incomplete | pending receipt/source-file verification |

## 3. Main risk

```text
The primary risk is not bad theory.
The primary risk is metadata ambiguity between wire behavior and creative overlay meaning.
```

## 4. Required next receipts

```text
1. Locate or create the actual v2.1 wire spec source file.
2. Locate or create the actual v2.1 overlay source file.
3. Add vault headers directly to both source files.
4. Compute SHA-256 for both source files using external deterministic tooling.
5. Update V2_1_MANIFEST_INDEX.yaml with real checksums and commit lineage.
```

## 5. Integrity verdict

```text
BOUNDARY: clean
CHECKSUMS: pending
CANON: no
DEPLOYMENT: no
RISK: low if checksum placeholders are not mistaken for receipts
```

## 6. Keeper line

```text
A placeholder is not a receipt.
A vault header is not a ratification.
A beautiful overlay is not a wire gate.
```
