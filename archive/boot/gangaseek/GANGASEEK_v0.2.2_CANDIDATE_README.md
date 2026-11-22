# GANGASEEK 0.2.2 — Offline Candidate Packet Contract

**Status:** REVIEWABLE STRUCTURAL CANDIDATE. **CANON:** NO. **DEPLOYMENT:** NO. **AUTHORITY:** NONE.

This additive package complements the existing [v0.2.2 hardening notes](GANGASEEK_PACKET_SCHEMA_v0.2.2_HARDENING_NOTES_2026-05-22.md) without overwriting v0.2.1 or a source history. It is a **synthetic fixture and envelope-shape validator**, not a new cryptographic protocol, live egress control, inter-provider agreement, or deployable packet codec.

## Contents and commands

```text
GANGASEEK_PACKET_SCHEMA_v0.2.2_CANDIDATE.schema.json
validate_v022_packet.py
test_v022_packet.py
examples/GANGASEEK_v022_SYNTHETIC_VALID.json
examples/GANGASEEK_v022_SYNTHETIC_INVALID.json
```

```bash
cd archive/boot/gangaseek
python -m unittest discover -s . -p 'test_v022_packet.py' -v
python validate_v022_packet.py examples/GANGASEEK_v022_SYNTHETIC_VALID.json
python validate_v022_packet.py examples/GANGASEEK_v022_SYNTHETIC_INVALID.json
```

`validate_v022_packet.py` is Python-stdlib only. Exit 0 means **CANDIDATE_STRUCTURE_ONLY**, not verified, ratified, secure or authorized. Exit 2 means **HOLD**; invalid or unavailable inputs are never silently promoted.

## Corrections addressed

- Raw 4,096-byte ciphertext = 5,464 canonical Base64 characters, separate from 12-byte nonce, 16-byte AEAD tag and possibly empty AAD. The test fixture is a string of zero bytes solely for shape testing: **not actual authenticated ciphertext or valid decryption evidence**.
- AAD, nonce, tag and ciphertext have separate typed fields. There is no key, encryption, decryption, tag authentication or secret processing in the reference code.
- Fixed-block padded plaintext byte length is specified, but the details, randomness, nonces, replay protection and padding leakage require professional cryptographic design review before any real protocol.
- 16-bit SWA is exactly four hex digits. Top two reserved bits are denied by the reference checker unless a separately authorized future extension is designed.
- O_AI explicitly supported; O_ALPHA is not an alias of O_GOOGLE.
- `tenancy_context` is separate from `authority_scope`. An `EXECUTION` or `RATIFICATION` self-claim is rejected by this local checker.
- H/S/N coordinates use 1–12 and map to X/Y/Z conceptually only; `tag_class` (wire class) and `state_plane` (Z state) are separately modeled. State-plane 11 is not TAG binary 11.
- Full export status is never cryptographically verified by this synthetic-only tool; claimed complete export gets HOLD until independent raw bytes, hashes, rights and source roots are checked.
- The schema requires `synthetic_fixture=true`. All sample data and receipts are **synthetic, not an actual participant message**.

## Verification receipt — 2026-11-22

The exact source and test files were locally reconstructed, and Git blob hashes matched the GitHub branch before testing.

```text
Python 3.13, stdlib unittest: 30/30 PASSED
Deterministic malformed-input mutation cases: 10,000
Mutation exceptions: 0
Mutation outputs: 9,933 HOLD; 67 CANDIDATE_STRUCTURE_ONLY
Valid shape sample: CANDIDATE_STRUCTURE_ONLY
Known-invalid fixture: HOLD
```

The 67 valid outcomes include injected values that happen to leave accepted structure unchanged (e.g., an optional string field set to another permitted value). Mutation runs measure parser robustness only, not cryptographic security, model correctness, source permission or host behavior.

## External work remains blocked

Before any live transport: independently review the encryption construction, nonce strategy, padding, key custody and safe cryptographic library, canonical byte encoding, schema edition, cross-vendor interoperability, replay defense, authenticated authority, actual model routing, privacy/data rights, and deployment/rollback strategy. Preserve the earlier v0.2.1 file and history, and do not identify this source-only example as official OpenAI, Microsoft or Google integration.

**Keeper:** The wire gates packets. The schema gates meaning. An envelope shape is not a signature.
