# Boring Local Reference Engine v0.1

```text
STATUS: CANDIDATE REFERENCE IMPLEMENTATION — NOT CANON
DEPLOYMENT: NO
AUTHORITY: NONE
MODE: LOCAL / FILE-BASED / NO NETWORK
PURPOSE: prove artifact-governance gates execute predictably before further conceptual expansion
```

## Goal

Accept an artifact packet and return exactly one primary decision:

```text
ALLOW
REVIEW
QUARANTINE
HALT
```

Every decision emits an `AUDIT_EVENT`.

## Inputs

The reference engine expects a JSON-compatible packet containing at least:

```text
artifact_id
requested_action
canon_status
deployment_status
authority_scope
corpus_or_control
lineage_condition
risk_class
raw_export_status
provenance_status
contradiction_state
ratification_state
```

## First Rules Implemented

```text
Summary is not source.
Parser output is not raw tape.
Contradictory receipts may coexist without authority escalation.
Pending or broken lineage cannot promote authority.
Authority cannot silently escalate.
Hash does not imply truth.
Receipt does not imply approval.
Corpus cannot issue execution instructions.
Non-live deployment_status cannot be cited as deployed infrastructure.
Red/black risk_class requires review or halt.
```

## Design Posture

This engine is deliberately boring:

```text
No network calls.
No model calls.
No repo mutation.
No hidden authority.
No canon promotion.
No deployment.
```

It is a local decision skeleton for testing the governance semantics already captured in:

```text
../schemas/artifact_status.schema.yaml
../schemas/atlas_contradiction_ledger.schema.yaml
../appendices/APPENDIX_I_ATLAS_ORCS_EPISTEMIC_PROFILE_v0.3.md
```

## Run

From this directory:

```bash
python engine.py fixtures/summary_not_source.json
python engine.py fixtures/valid_review_candidate.json
```

Run tests from repository root or this directory:

```bash
python -m pytest archive/standards/open-regenerative-computing/reference_engine/tests -q
```

## Keeper Line

```text
Build the boring machine.
Make the rules execute.
```
