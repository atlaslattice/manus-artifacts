# GANGASEEK Packet Schema v0.2.2 — Hardening Notes

```text
STATUS: HARDENING NOTES — CANDIDATE — NOT CANON
PURPOSE: preserve v0.2.1 and define receipt-safe corrections for v0.2.2
DATE: 2026-05-22
ISSUE: manus-artifacts#144
DEPLOYMENT: NONE
AUTHORITY: NONE
```

## 0. v0.2.1 preserved status

```yaml
artifact_id: GANGASEEK-PACKET-SCHEMA-v0.2.1
status: vault_ready_candidate
canon_status: not_canon
deployment_status: not_deployable
authority_scope: none
supersedes: GANGASEEK_PACKET_SCHEMA_v0.2.0
blocker_B4: closed
```

v0.2.1 is a strong candidate specimen. v0.2.2 should harden protocol mechanics before broader crosswalk or pilot work.

## 1. Clean wins in v0.2.1

```text
- explicit non-canon / non-deployable posture
- 16-bit SWA field layout declared
- cryptographic envelope introduced
- authority_scope explicitly bounded
- optional calibration fee field kept minimal / tabled
- non-commutation rule preserved as conceptual invariant
- real-company note blocks partnership/compliance overclaim
```

## 2. Hardening issue: Base64 length vs raw byte length

v0.2.1 says:

```yaml
encrypted_sovereign_data:
  pattern: '^[a-zA-Z0-9+/=]{4096}$'
  description: Fixed 4096-byte Base64-encoded ChaCha20-Poly1305 block.
```

Problem:

```text
4096 Base64 characters do not equal 4096 encrypted bytes.
Base64 encodes 3 raw bytes into 4 characters.
4096 raw bytes would encode to 5464 Base64 characters with padding.
4096 Base64 characters represent 3072 raw bytes before padding effects.
```

v0.2.2 correction:

```text
Separate raw byte length from encoded string length.
Declare either:
- ciphertext_padded_bytes: 4096, encoded_length: 5464, or
- encoded_block_chars: 4096, decoded_bytes: 3072.
```

Recommendation:

```yaml
ciphertext_padded_bytes: 4096
encoded_ciphertext_base64_chars: 5464
```

## 3. Hardening issue: AEAD envelope structure

ChaCha20-Poly1305 needs explicit envelope fields.

v0.2.2 should separate:

```yaml
aead_envelope:
  algorithm: CHACHA20_POLY1305
  nonce_base64: null
  aad_base64: null
  ciphertext_base64: null
  tag_base64: null
  padded_plaintext_bytes: 4096
  padding_scheme: fixed_block_padding
```

Do not hide nonce/tag/AAD inside one opaque string unless the serialization contract precisely defines the layout.

## 4. Hardening issue: deterministic padding language

v0.2.1 says:

```text
PKCS#7-style deterministic padding (null vectors)
```

Problem:

```text
PKCS#7 padding and null-vector deterministic padding are distinct concepts.
Deterministic padding can leak structure if not paired with a carefully specified fixed-length block policy.
```

v0.2.2 recommendation:

```text
Use fixed-size padded plaintext blocks.
Define padding bytes explicitly.
Do not call it PKCS#7-style unless it actually follows PKCS#7 semantics.
```

Safer wording:

```text
fixed-block padding to 4096 plaintext bytes before AEAD encryption; padding scheme must be specified and tested.
```

## 5. Hardening issue: SWA mask pattern too narrow

v0.2.1 pattern:

```yaml
swa_mask:
  pattern: '^0x[0-6][a-fA-F0-9]{2}$'
```

Problem:

```text
The declared SWA layout is 16-bit, but the pattern only permits a 12-bit-ish three-hex-digit value from 0x000 to 0x6ff.
```

v0.2.2 correction:

```yaml
swa_mask:
  pattern: '^0x[a-fA-F0-9]{4}$'
```

If RSV bits must be constrained, use a separate validation rule:

```text
(swa_mask & 0xC000) == 0x0000 unless RSV override is explicitly declared.
```

## 6. Hardening issue: O_AI missing from operator enum

v0.2.1 source/target operators:

```yaml
enum: [O_MS, O_GOOGLE, O_STARLINK, O_ALPHA]
```

But current interop architecture includes:

```text
O_AI = OpenAI / ChatGPT / Codex task surface
```

v0.2.2 should include O_AI if the schema is meant to support OpenAI task-surface interoperability.

Recommendation:

```yaml
operator_id:
  enum: [O_AI, O_MS, O_GOOGLE, O_STARLINK, O_ALPHA, O_X]
```

## 7. Hardening issue: O_GOOGLE vs O_ALPHA namespace

v0.2.1 includes both:

```text
O_GOOGLE
O_ALPHA
```

Potential ambiguity:

```text
Are these aliases, distinct lanes, or parent/child namespaces?
```

v0.2.2 should declare:

```text
O_ALPHA = Alphabet parent operator lane
O_GOOGLE = Google-specific product/cloud/ingest lane
```

or collapse one if unnecessary.

## 8. Hardening issue: authority_scope mixes authority with tenancy

v0.2.1:

```yaml
authority_scope:
  enum: [ADVISORY, ENTERPRISE]
```

Problem:

```text
ADVISORY is authority scope.
ENTERPRISE is tenancy/context class, not authority scope.
```

v0.2.2 should separate:

```yaml
authority_scope:
  enum: [NONE, ADVISORY, REVIEW, RATIFICATION, EXECUTION]

tenancy_context:
  enum: [SOVEREIGN, ENTERPRISE, PUBLIC, PRIVATE, RESEARCH]
```

This prevents category collapse.

## 9. Hardening issue: H/S/N versus X/Y/Z notation

v0.2.1 uses crosswalk labels such as:

```text
H12-S7-N5
H5-S2-N8
```

But current lattice notes use:

```text
X = House
Y = semantic container / sphere
Z = state type / authority-bearing distinction
```

v0.2.2 must either:

```text
map H/S/N to X/Y/Z explicitly
```

or declare H/S/N as legacy notation.

Recommended mapping if retained:

```text
H = X / House
S = Y / Sphere or semantic container
N = Z / Node or state type
```

## 10. Hardening issue: Z == 0x0B vs TAG == 0b11

v0.2.1 declares:

```text
TAG[1:0] = 0b11 -> Śūnya absorption at wire layer
Z == 0x0B -> Conceptual egress plane
```

These may coexist if semantics are distinct:

```text
TAG = packet handling class
Z = coordinate plane/state layer
```

v0.2.2 should explicitly state:

```text
TAG controls wire behavior.
Z controls lattice state plane.
They are independent fields.
```

## 11. Proposed v0.2.2 header adjustments

```yaml
header:
  required:
    - provenance_receipt
    - epistemic_label
    - authority_scope
    - tenancy_context
    - source_operator
    - target_operator
    - swa_mask
    - timestamp
  properties:
    authority_scope:
      enum: [NONE, ADVISORY, REVIEW, RATIFICATION, EXECUTION]
    tenancy_context:
      enum: [SOVEREIGN, ENTERPRISE, PUBLIC, PRIVATE, RESEARCH]
    source_operator:
      enum: [O_AI, O_MS, O_GOOGLE, O_STARLINK, O_ALPHA, O_X]
    target_operator:
      enum: [O_AI, O_MS, O_GOOGLE, O_STARLINK, O_ALPHA, O_X]
    swa_mask:
      pattern: '^0x[a-fA-F0-9]{4}$'
```

## 12. Proposed v0.2.2 payload encryption adjustments

```yaml
payload:
  encrypted_sovereign_data:
    type: object
    required:
      - aead_algorithm
      - nonce_base64
      - aad_base64
      - ciphertext_base64
      - tag_base64
      - padded_plaintext_bytes
      - encoded_ciphertext_base64_chars
    properties:
      aead_algorithm:
        enum: [CHACHA20_POLY1305]
      padded_plaintext_bytes:
        const: 4096
      encoded_ciphertext_base64_chars:
        const: 5464
```

Note:

```text
If AEAD tag is included in ciphertext serialization, the encoded length must be recalculated and documented.
```

## 13. Recommended next vector

Before GS_BWP_CROSSWALK_v1.2 or pilot-node architecture:

```text
1. Patch schema mechanics into v0.2.2.
2. Add a tiny validation script for SWA parsing and Base64 length checks.
3. Add one valid and one invalid packet fixture.
4. Only then crosswalk into GS_BWP_CROSSWALK_v1.2.
```

## 14. Keeper line

```text
Best in the world means catching the byte-length bug before the protocol becomes beautiful nonsense.
```

```text
The wire gates packets. The schema gates meaning. Receipts decide what can be trusted.
```
