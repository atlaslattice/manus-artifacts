# Glossary of Terms
Status: Candidate
Date: 2026-05-26

This glossary is the single authoritative term reference for the Manus archive program.
When a term appears across multiple documents, this file governs the canonical definition.
All domain primers, governance docs, and reader guides should link here for consistency.

## Authority and dispute process

- Source of truth: this file is the active Candidate glossary authority for repository terminology.
- Dispute intake: open a documented glossary dispute in governance review channels with the conflicting term, context, and proposed definition.
- Decision path: domain steward review -> council review -> adjudication by @atlaslattice for contested authority outcomes.
- Preservation rule: deprecated definitions are not deleted; they are retained with supersession notes and forward pointers.

---

## Archive Program Terms

**Adjudication**
The final authority action performed by @atlaslattice to approve canon transitions.
Adjudication is required for any artifact moving to Canon or Deprecated status.

**Aetherforge**
The execution framework and game metaphor used to make archive work engaging and
traceable. The Metatron's Cube structure (five rings of ten tasks) organizes archive
improvement work into named, trackable categories.

**Artifact**
Any discrete document, protocol, spec, report, or operational template committed to
the repository. An artifact has a lifecycle state, a steward, a domain, and a lineage.

**Archive Program**
The full set of artifacts, governance structures, and operational rhythms that make up
the public Manus archive on GitHub.

**Candidate**
The default public lifecycle state. An artifact is Candidate if it is stable enough to
publish and review, but has not yet been ratified and adjudicated as Canon.
See [CANON_LIFECYCLE.md](./CANON_LIFECYCLE.md).

**Canon**
The highest active authority state for an artifact. Canon requires full council
ratification and adjudication by @atlaslattice. Canon artifacts may be published to
the website canon destination. See [CANON_LIFECYCLE.md](./CANON_LIFECYCLE.md).

**Canon Boundary**
The rule set that defines what makes GitHub the authoritative substrate versus relay
layers like Drive or Notion. See [CANON_BOUNDARY.md](./CANON_BOUNDARY.md).

**Canon Decision Log**
A durable, queryable record of council and adjudication decisions about canon status.
Format defined in [CANON_DECISION_LOG_FORMAT.md](./CANON_DECISION_LOG_FORMAT.md).

**Changelog**
A per-domain or root-level record of what changed and when.
Root changelog: [../CHANGELOG.md](../CHANGELOG.md).

**Council**
The governing body responsible for review, ratification, and adjudication of artifacts.
Includes the Trinity Council, Pantheon Council, and domain stewards as applicable.

**Domain**
One of six primary archive categories: Systems, Projects, Governance, Research,
Health, Vault. See [ARCHIVE_TAXONOMY.md](./ARCHIVE_TAXONOMY.md).

---

## Lifecycle Terms

**Archived**
A preservation state for artifacts that were once active or canonical but are now
historical. Archived artifacts remain accessible but are not current authority.

**Deprecated**
A warning state for artifacts that should not be used operationally.
Deprecation includes an explicit rationale and, where possible, a replacement path.

**Draft**
The earliest lifecycle state. Drafts are under active development and should not be
cited as authoritative doctrine.

**Lifecycle**
The sequence of states an artifact moves through: Draft → Candidate → Canon →
Archived / Deprecated. See [CANON_LIFECYCLE.md](./CANON_LIFECYCLE.md).

**Supersession**
The act of a newer artifact replacing an older one in authority.
The older artifact should be linked from the newer as its predecessor (supersedes),
and the older should link forward to the newer (superseded_by).

---

## Systems Terms

**Aluminum OS**
The constitutional substrate for regenerative computing. The primary systems doctrine
in this archive. See [primers/ALUMINUM_OS_PRIMER.md](./primers/ALUMINUM_OS_PRIMER.md).

**BAZINGA**
Constitutional middleware and launch protocols. Handles constitutional activation,
boot events, and launch decrees.

**GPTBrain**
The AI agent memory, dream, and coordination substrate. Includes the memory palace,
REM protocols, and swarm orchestration architecture.
See [primers/GPTBRAIN_PRIMER.md](./primers/GPTBRAIN_PRIMER.md).

**Memory Palace**
The structured long-term memory architecture for GPTBrain agents. Provides indexed,
queryable memory with decay and reinforcement mechanisms.

**REM Protocol**
The dream state processing protocol for GPTBrain. REM artifacts (dream journals,
wake reports) are generated during REM-8 and related protocol cycles.

**SheldonBrain**
The system architecture and knowledge substrate layer built on top of GPTBrain.
Provides higher-level reasoning, routing, and system integration.

**Swarm**
The multi-agent architecture in GPTBrain. Individual named brain folders (AsterBrain,
LumenBrain, TIDELOCKBrain, etc.) form the swarm. See [STEWARDSHIP_MAP.md](./STEWARDSHIP_MAP.md).

---

## Governance Terms

**Adjudication** — see above under Archive Program Terms.

**Canon Conflict**
When two or more artifacts assert authority over the same subject with incompatible
claims. Resolution follows [../governance/CANON_CONFLICT_RESOLUTION.md](../governance/CANON_CONFLICT_RESOLUTION.md).

**Decision Rights**
The authority map defining who can create, edit, promote, archive, or deprecate
artifacts. See [../governance/DECISION_RIGHTS_MATRIX.md](../governance/DECISION_RIGHTS_MATRIX.md).

**Fire Drill**
A tabletop governance exercise rehearsing response to specific failure scenarios.
See [../governance/GOVERNANCE_FIRE_DRILLS.md](../governance/GOVERNANCE_FIRE_DRILLS.md).

**Incident**
A governance, canon, or trust event requiring formal response.
Runbook at [../governance/INCIDENT_RESPONSE_RUNBOOK.md](../governance/INCIDENT_RESPONSE_RUNBOOK.md).

**Mission Control**
The operating cadence for recurring governance activities: weekly standups, monthly
reviews, quarterly all-council, annual audit. See [../governance/MISSION_CONTROL_CADENCE.md](../governance/MISSION_CONTROL_CADENCE.md).

**Provenance**
The traceable chain of evidence supporting a claim. High-impact claims require
provenance per [../governance/PROVENANCE_REQUIREMENTS.md](../governance/PROVENANCE_REQUIREMENTS.md).

**Retention Policy**
Rules governing artifact immutability, supersession chains, and long-term preservation.
See [../governance/RETENTION_POLICY.md](../governance/RETENTION_POLICY.md).

**Risk Register**
A live catalog of governance and quality risks.
See [../governance/RISK_REGISTER.md](../governance/RISK_REGISTER.md).

**Steward**
The named person or role responsible for a domain or artifact's accuracy, freshness,
and lifecycle management. See [STEWARDSHIP_MAP.md](./STEWARDSHIP_MAP.md).

**Succession**
The process of transferring stewardship safely when a steward is unavailable.
Protocol: [../governance/SUCCESSION_STEWARDSHIP.md](../governance/SUCCESSION_STEWARDSHIP.md).

---

## Navigation Terms

**Best of Archive**
A curated set of high-signal artifacts for public readers.
See [BEST_OF_ARCHIVE.md](./BEST_OF_ARCHIVE.md).

**Doctrine Map**
A cross-reference connecting systems, projects, council decisions, and research.
See [DOCTRINE_MAP.md](./DOCTRINE_MAP.md).

**Frontmatter**
The YAML metadata block at the top of a document. Schema defined in
[METADATA_SCHEMA.md](./METADATA_SCHEMA.md).

**Lineage**
The traceable chain of document evolution through supersession.
See [ARTIFACT_LINEAGE.md](./ARTIFACT_LINEAGE.md).

**Maturity Map**
A visual/tabular overview of archive domain coverage and quality.
See [ARCHIVE_MATURITY_MAP.md](./ARCHIVE_MATURITY_MAP.md).

**Primer**
A domain-specific introduction for newcomers. Primers are in [primers/](./primers/).

**Relay Layer**
A working or drafting surface (Drive, Notion) that is not a canon authority.
GitHub is the canonical substrate; relay layers serve coordination only.

**Scorecard**
A quality snapshot for a domain or artifact family.
See [ARTIFACT_SCORECARDS.md](./ARTIFACT_SCORECARDS.md).

---

*Manus Archive Program — Status: Candidate — 2026-05-26*
