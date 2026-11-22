# Council Plan Hash Binding and Split Verifier Contract — v0.1

**STATUS: CANDIDATE SOURCE REFERENCE / NOT RATIFIED / NOT DEPLOYED / AUTHORITY NONE**

Historical request: issue #89 (May 20, 2026). This document and the accompanying offline checker were authored November 22, 2026. Neither a signed decision nor a live Council execution system is represented by this source package.

## Problem and invariant

A text label such as "approved plan" is not proof that execution followed the same planner-selected instructions. A plan hash can bind bytes for *comparison*, and independent verifier lanes can record different evidence requirements, but **a hash, self-declared verifier result, reviewer label or PR never authenticates a human decision**.

**Rule:** every candidate execution packet and verifier report MUST carry exactly the SHA-256 digest of the same canonicalized, source-pinned candidate plan. Mismatch = HOLD, no retry or side effect. A matching digest still permits only an offline structural review outcome.

## Canonicalization scope

The reference checker `plan_hash_candidate.py` accepts only UTF-8 JSON object bytes with `status=candidate` and `canon=false`. It strictly rejects duplicate JSON keys, non-finite and floating-point values, objects larger than 256 KiB, excess depth, excessively large integers and non-JSON objects. It serializes accepted content with UTF-8, sorted keys, no extra whitespace and no ASCII-only transliteration, then computes SHA-256. The JSON profile is **Python-local and not RFC 8785/JCS**; a production cross-language system requires an independently agreed canonical serialization edition, test vectors and cryptographic key/signature rules.

Hash the original *approved plan edition* and store the actual source bytes, rights and receipt under a separately authenticated system. The present reference does not persist original plans, receive model tool credentials, or verify external storage.

## Three non-authorizing packet surfaces

```json
{
  "candidate_plan": {"status": "candidate", "canon": false, "steps": [{"id": 1, "type": "synthetic"}]},
  "execution": {
    "plan_sha256": "<exact canonical plan SHA-256>",
    "dry_run_only": true,
    "effects_executed": false,
    "source_ref": "synthetic:plan"
  },
  "logic_verifier": {
    "lane": "logic_verifier",
    "plan_sha256": "<same digest>",
    "verdict": "PASS",
    "evidence_ref": "synthetic:logic-review"
  },
  "security_verifier": {
    "lane": "security_verifier",
    "plan_sha256": "<same digest>",
    "verdict": "PASS",
    "evidence_ref": "synthetic:security-review"
  }
}
```

### Logic verifier

Tests internal consistency, plan/implementation conformance, evidence references, expected outputs, exception handling and reproducibility. A "PASS" is a statement by a reviewer, not independently authenticated by this local checker. Proof that code really ran and produced the claimed outcomes is a separate receipt requirement.

### Security verifier

Independently inspects source rights, privacy classes, injection risk, authorized tool capabilities, sandbox constraints, sensitive side effects, external provider and device permissions, revocation and stop controls. It cannot be replaced by the logic lane. A "PASS" is equally unverified without host identity and signed review evidence.

### Optional canon/release verifier

An independent governance/human-root review must adjudicate rights, historical CANON and release authority *outside* this local module. The two technical lanes cannot silently make the human decision. Extra verifier semantics can be proposed separately but should not be smuggled into a status field.

## Exact outcome definitions

- `HOLD`: missing/malformed candidate JSON, hash mismatch in any lane, missing evidence, uncertain mode, actual effects already executed, failed verifier, wrong reviewer lane or missing source pointer.
- `STRUCTURAL_CANDIDATE_READY_NOT_AUTHORIZED`: input shapes and plan hashes agree, both self-declared verifier packets report PASS, and dry-run/effects flags are correct. **Still no execution, authorizing signature or ratification**.
- Every output fixes `host_execution_permitted=false, approval_granted=false, canon=false, deployed=false`. No function dispatches tools, writes state, imports private Play/Dream/Imagine bodies, spends money, or publishes a conclusion.

## Reproducible tests

```bash
cd archive/boot/council
python -m unittest -v test_plan_hash_candidate.py
```

On November 22, 2026, **23/23 synthetic negative/positive tests passed locally** on exact GitHub-blob-matched files:

- checker Git blob `ae5ea5f2ca38905ef33569a6a0a9e13f6ef6f06a`
- tests Git blob `f386b85726f271eacdbb2d54d31fca5c10afbf48`

No hosted GitHub Actions runner admission, real reviewer credential, actual plan-run lineage, independent code/security reviewer or production permission gate was tested. The source package is independently revertible and can be extended after a true host policy integration.

## Engineering follow-through required

Before any production effect, add: authenticated principals and expiring/revocable scopes; immutable source-plan capture; JCS or versioned canonicalization with cross-language vectors; unforgeable independent review receipts/signatures and conflict-of-interest protection; exact tool/side-effect boundary; environment pinning; drift detection; comprehensive negative tests; audit and rollback; explicit human-root policy decision. A local script MUST NOT serve as the final authorization system.

**Keeper:** Same plan, different eyes. Two passes are evidence; neither is a crown.
