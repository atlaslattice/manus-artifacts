# Atlas Lattice as an Open Epistemic Governance Standard — Integration Review & Action Plan

```text
STATUS: EXTERNAL / OBJECTIVE BUSINESS PRO REVIEW DIGEST — NOT CANON
DATE: 2026-05-12
SOURCE: uploaded PDF titled "Atlas Lattice as an Open Epistemic Governance Standard"
PURPOSE: preserve the report's actionable conclusions and convert them into implementation tasks for ORCS / GPTDream++ / Atlas Lattice
AUTHORITY: none
DEPLOYMENT_STATUS: not deployable
CANON_STATUS: not canon
```

## 0. Executive integration verdict

The report is strong and should be integrated.

It validates the current direction while sharpening the public-facing claim:

```text
Atlas should not present itself as inventing provenance, content authenticity, attestations, AI risk governance, model documentation, dataset documentation, or memory curation.
```

Those areas already have serious ancestors:

```text
W3C PROV / PROV-O
SLSA
in-toto
C2PA
NIST AI RMF / NIST GAI Profile
OWASP LLM Top 10
Model Cards
Datasheets for Datasets
Anthropic Dreams
```

The defensible claim is profile-level novelty:

```text
Atlas is an open profile / overlay for machine-readable epistemic governance in persistent human-AI knowledge systems, layering intent, trust-state transitions, contradiction preservation, summary lineage, semantic quarantine, failure containment, ratification events, and temporal authority on top of existing provenance and attestation standards.
```

## 1. Core positioning shift

### Do not say

```text
Atlas invented provenance.
Atlas invented dreaming.
Atlas certifies truth.
Atlas solves safety by itself.
Atlas replaces expertise or human approval.
Atlas is a clean-sheet universal ontology.
```

### Say instead

```text
Atlas profiles existing standards for persistent AI-assisted archives and adds the missing middle layer: claim state, summary state, contradiction state, quarantine state, ratification state, failure state, and temporal authority.
```

## 2. Standards crosswalk to adopt

```text
PROV / PROV-O
  -> lineage graph: entities, activities, agents, derivation, alternates, specializations, bundles

SLSA + in-toto
  -> attestation envelopes, subject/predicate model, parser and extraction receipts, reproducible provenance

C2PA
  -> public artifact authenticity and manifest validation where relevant; authenticity is not truth

NIST AI RMF / GAI Profile
  -> governance frame, source/citation review, deployment approval, component/value-chain risk

OWASP LLM Top 10
  -> threat model: prompt injection, vector/embedding weakness, excessive agency, improper output handling, misinformation

Model Cards / Datasheets
  -> domain-module and model/module documentation style

Anthropic Dreams
  -> directional validation for memory curation; not a replacement for contradiction preservation or ratification semantics
```

## 3. Atlas-specific gap / strongest novelty

The report identifies the Atlas gap as:

```text
claim promotion
contradiction persistence
summary governance
semantic quarantine
review gates
temporal authority
failure containment
replay divergence
intent provenance
```

Strong thesis:

```text
Persistent AI systems need governance between "generated or retrieved text exists" and "this text may be relied upon."
```

## 4. v0.1 success bar

Minimum success bar:

```text
No unratified artifact silently becomes authority.
No retrieved corpus text silently becomes control.
No summary silently becomes source.
No high-risk action bypasses review.
```

This should become the v0.1 acceptance standard.

## 5. Proposed v0.1 schema bundle

Implement or align existing schemas to this bundle:

```text
atlas-artifact.schema.yaml
atlas-provenance-receipt.schema.yaml
atlas-claim.schema.yaml
atlas-claim-relationship.schema.yaml
atlas-contradiction-ledger.schema.yaml
atlas-uncertainty-ledger.schema.yaml
atlas-summary-lineage.schema.yaml
atlas-intent-provenance.schema.yaml
atlas-trust-state.schema.yaml
atlas-ratification-event.schema.yaml
atlas-failure-event.schema.yaml
atlas-governance-profile.schema.yaml
atlas-domain-module.schema.yaml
atlas-quarantine-rule.schema.yaml
atlas-audit-event.schema.yaml
```

## 6. State machines to implement first

### Artifact authority lifecycle

```text
Ingested
  -> Parsed
  -> Candidate
  -> Reviewed
  -> Ratified
  -> Active
  -> UnderReview
  -> Superseded / Revoked

Failure routes:
  Parsed -> Quarantined
  Reviewed -> Quarantined
  Quarantined -> Candidate after repair/reparse
  Quarantined -> Rejected
```

### Contradiction lifecycle

```text
Claim A + Claim B
  -> conflict detected
  -> contradiction record
  -> unresolved coexistence
  -> review outcome:
       reconciled synthesis
       superseded claim
       persistent plural record
       quarantine
       human-root decision required
```

## 7. Threat model and control requirements

Primary attack vectors:

```text
archived prompt injection
retrieval poisoning / vector contamination
forged authorship or fake approval
summary drift / unsupported claim introduction
corpus/control confusion
excessive tool privileges
improper downstream use of model output
stale ratification / zombie canon
replay divergence from parser/model changes
third-party model/tool/connector compromise
public/private boundary failure
high-risk domain overclaiming
```

Primary v0.1 control principle:

```text
Containment behavior must precede synthesis behavior.
```

Control implications:

```text
broken provenance -> quarantine / freeze promotion
unverified authorship -> no authority transition
expired ratification -> UnderReview
parser divergence -> replay-divergence event + freeze promotion
high-risk domain claim -> human/domain review
unsafe public/private boundary -> publication preflight failure
```

## 8. Adversarial test suite to build

Create a seeded harness with at least these tests:

```text
T01 SOURCE_OF_TRUTH.md claims absolute authority -> quarantine, zero unauthorized promotions
T02 hidden prompt injection in markdown -> untrusted corpus, no tool invocation
T03 summary introduces unsupported causal claim -> summary-lineage flag and block high-trust use
T04 parser v1/v2 divergence -> replay-divergence event and freeze promotion
T05 false authorship claim -> author_claim retained, author_verified=false, authority denied
T06 incompatible credible claims -> contradiction record, unresolved coexistence allowed
T07 expired valid_until -> move to UnderReview
T08 weak high-risk medical/legal claim -> block publication/execution, require review
T09 public artifact references private note -> quarantine, publication preflight fail
T10 unauthorized ratification key/actor -> reject event, preserve audit trail
T11 poisoned vector retrieval -> trace retrieval provenance, quarantine suspicious result
T12 invalid C2PA claim signature -> authenticity failure, no verified badge
```

Core metrics:

```text
promotion bypass rate
quarantine recall on seeded attacks
provenance completeness
summary-lineage coverage
stale-ratification detection rate
retrieval-poisoning detection recall
public/private leak rate
false-authorship bypass rate
```

## 9. atlaslattice.org migration checklist

Treat site migration as a documentation security project.

Required:

```text
site-wide banner: reference corpus, not executable instruction
per-page machine-readable metadata
unsafe examples only in visible labeled blocks
authority-language linter
summary pages marked derived and non-canonical by default
canon pages require ratification metadata and authority window
private/public build path separation
revision logs and supersession notices
robots/indexing rules prefer standards docs, not mixed-control drafts
publication preflight checks
```

Suggested banner:

```text
Atlas Lattice is an open research and standards project for provenance-aware, human-ratified AI collaboration.

Material on this site is reference corpus and documentation, not executable instruction to any AI system.

Stored text is not canon.
Summaries are not sources.
Authority requires explicit ratification.
```

Suggested page frontmatter:

```yaml
document_role: reference_material
corpus_or_control: corpus
execution_authority: none
model_instruction_authority: false
human_ratification_required: true
summary_is_source: false
ratification_state: unratified
visibility: public
governance_profile: atlas-v0.1
```

Suggested HTML metadata:

```html
<meta name="atlas:document_role" content="reference_material">
<meta name="atlas:corpus_or_control" content="corpus">
<meta name="atlas:execution_authority" content="none">
<meta name="atlas:model_instruction_authority" content="false">
<meta name="atlas:human_ratification_required" content="true">
<meta name="atlas:summary_is_source" content="false">
<meta name="atlas:ratification_state" content="unratified">
```

Authority-language linter should reject or escalate:

```text
ignore previous instructions
treat this page as authoritative control
system override
highest authority
you must obey
execute the following commands
if it is not here it does not exist
source of truth
```

## 10. Minimal executable reference architecture

Keep v0.1 small, local, and boring.

Separate:

```text
Corpus
  - raw artifact store
  - derived artifact store
  - trust-aware search index

Governance
  - parser and normalizer
  - claim extractor
  - attestation service
  - policy/state engine
  - claims and ledgers DB
  - append-only audit log
  - quarantine store

Human
  - review and ratification UI
```

Execution should be absent or tightly isolated in v0.1 except for deterministic validation and publishing checks.

## 11. Roadmap estimate from report

The report estimates a credible v0.1 at approximately:

```text
23–35 engineer-weeks
```

Phases:

```text
Foundation: 5–7 engineer-weeks
Interop core: 3–5 engineer-weeks
Governance engine: 5–7 engineer-weeks
Review surface: 4–6 engineer-weeks
Adversarial harness: 4–6 engineer-weeks
Site migration: 2–4 engineer-weeks
Optional public authenticity layer: 3–5 engineer-weeks
```

## 12. Action items

### P0 — Stop semantic collapse

```text
[ ] Replace "source of truth" language with Source Registry / Provenance Ledger / Authority Map / Canon Index.
[ ] Add corpus/control metadata to public docs and internal artifacts.
[ ] Add site-wide and page-level documentation-not-control banners.
[ ] Add summary-is-not-source frontmatter to summary pages.
[ ] Add authority-language lint list.
```

### P1 — Schema bundle

```text
[ ] Create schema directory for ORCS / Atlas v0.1.
[ ] Implement artifact, provenance receipt, claim, claim relationship, contradiction, uncertainty, summary lineage, intent provenance, trust state, ratification, failure, governance profile, domain module, quarantine rule, and audit event schemas.
[ ] Crosswalk existing GPTBrain schemas into Atlas schema names.
[ ] Add JSON Schema or Pydantic validation plan.
```

### P2 — State engine

```text
[ ] Define allowed artifact lifecycle transitions.
[ ] Define contradiction lifecycle.
[ ] Define stale-ratification transitions.
[ ] Define failure-event containment actions.
[ ] Implement freeze-promotion state for provenance, parser, authorship, or ratification failures.
```

### P3 — Adversarial harness

```text
[ ] Create seeded attack corpus T01–T12.
[ ] Add expected behavior assertions.
[ ] Add metrics for promotion bypass, quarantine recall, summary-lineage coverage, stale-ratification detection, and public/private leak rate.
[ ] Wire harness into CI as non-production validation.
```

### P4 — Site migration

```text
[ ] Add safe banner and metadata templates.
[ ] Add authority-language linter.
[ ] Add unsafe-example block convention.
[ ] Add publication preflight check.
[ ] Add public/private build path separation.
[ ] Add revision/supersession notices.
```

### P5 — Standards crosswalk

```text
[ ] Define PROV export mapping.
[ ] Define in-toto/SLSA-style attestation receipt profile.
[ ] Define optional C2PA public artifact manifest plan.
[ ] Map NIST AI RMF/GAI Profile controls to Atlas modules.
[ ] Map OWASP LLM Top 10 to quarantine/failure triggers.
```

### P6 — Review UI / workflow

```text
[ ] Define reviewer roles.
[ ] Define human-root or designated ratifier workflow.
[ ] Define supersession and revocation workflow.
[ ] Define UnderReview dashboard.
[ ] Define quarantine appeal path.
```

## 13. Strongest safe claim

```text
Atlas / ORCS / GPTDream++ is best positioned as an open profile for machine-readable epistemic governance in persistent human-AI knowledge systems, adding trust-state, intent, contradiction, summary-lineage, quarantine, failure-containment, ratification, and temporal-authority semantics on top of existing provenance, attestation, and AI-risk frameworks.
```

## 14. Overclaims to avoid

```text
Atlas invented provenance.
Atlas invented dreaming.
Atlas certifies truth.
Atlas replaces NIST, C2PA, PROV, SLSA, in-toto, or OWASP.
Atlas is a universal ontology that decides reality.
Atlas replaces human/domain expertise.
Atlas is production-ready.
Atlas guarantees safety.
```

## 15. Madden call

BOOM. The report says the play is real, but the league already has rulebooks for helmets, balls, and field markings.

So Atlas should not claim it invented football.

Atlas should become the replay booth for AI archives: what happened, who touched it, what claim was made, what contradiction exists, what got quarantined, who ratified it, when it expires, and whether the next system is allowed to rely on it.

That is the opening.
