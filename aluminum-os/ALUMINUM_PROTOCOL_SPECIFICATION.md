# ALUMINUM PROTOCOL SPECIFICATION
## RFC-Style Formal Specification for the Aluminum Unified OS

**Status:** Draft Specification  
**Version:** 1.0  
**Date:** February 2, 2026  
**Authors:** Manus AI, Microsoft Copilot, Daavud Sheldon  
**Category:** Standards Track

---

## Abstract

This document specifies the Aluminum Protocol, a constitutional intelligence layer that enables multi-vendor, cross-device, cross-OS coordination while preserving vendor sovereignty. The protocol defines eight core subsystems: Identity Federation, Continuity, Reversible State, Constitutional Governance, Multi-Agent Coordination, Memory Substrate, Sovereignty Protocol, and Intelligence Runtime. The specification is designed to be vendor-agnostic, platform-independent, and privacy-preserving.

---

## 1. Introduction

### 1.1 Motivation

Modern computing ecosystems are fragmented across five major operating system boundaries (Windows, macOS, iOS, Android, ChromeOS), each with redundant infrastructure for continuity, identity, sync, agents, AI runtimes, memory, and governance. This fragmentation creates inefficiencies, vendor lock-in, and poor user experiences. The Aluminum Protocol addresses this by unifying the intelligence layer while preserving vendor sovereignty at the hardware OS and UX layers.

### 1.2 Design Goals

The Aluminum Protocol is designed to achieve the following goals:

1. **Vendor Sovereignty** - Preserve each vendor's identity, ecosystem, and governance model
2. **Cross-Platform Continuity** - Enable seamless workflows across all devices and OSes
3. **Reversible State** - Support safe rollback of all operations across devices
4. **Constitutional Governance** - Enforce user-defined policies and consent rules
5. **Multi-Agent Coordination** - Enable multiple AI agents to cooperate without conflicts
6. **User Sovereignty** - Ensure users own their data, not vendors
7. **Privacy Preservation** - Minimize data exposure and enable on-device processing
8. **Interoperability** - Work with existing vendor infrastructure without replacement

### 1.3 Terminology

**MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** in this document are to be interpreted as described in RFC 2119.

**Aluminum Node** - A device or system running the Aluminum Protocol implementation

**Aluminum Agent** - An AI agent (Copilot, Siri, Assistant, ChatGPT, Watson, etc.) integrated with Aluminum

**Constitutional Memory Fabric** - External, user-controlled archive (OneDrive, Google Drive, Notion, etc.)

**Janus Protocol** - Bidirectional state transition protocol for reversibility

**Tardigrade Protocol** - Cryptobiotic state preservation protocol for AI agents

**144-Sphere Ontology** - Knowledge topology for task routing and coordination

---

## 2. Architecture Overview

### 2.1 Layer Model

The Aluminum Protocol operates at Layer 2 (Intelligence Layer), sitting above Layer 0 (Hardware OS) and Layer 1 (Vendor UX):

```
Layer 2: Aluminum Intelligence Layer (This Specification)
Layer 1: Vendor UX (Unchanged - Apple, Google, Microsoft, etc.)
Layer 0: Hardware OS (Unchanged - Windows, macOS, iOS, Android, ChromeOS)
```

### 2.2 Core Subsystems

The Aluminum Protocol consists of eight core subsystems:

1. **Identity Federation** - Cross-vendor identity substrate
2. **Continuity** - Cross-device, cross-OS continuity
3. **Reversible State** - Janus/Tardigrade protocols
4. **Constitutional Governance** - Policy enforcement and consent management
5. **Multi-Agent Coordination** - Task decomposition and agent routing
6. **Memory Substrate** - External, sovereign, versioned archive
7. **Sovereignty Protocol** - User-centric, vendor-agnostic data ownership
8. **Intelligence Runtime** - Model-agnostic agentic substrate

---

## 3. Identity Federation Subsystem

### 3.1 Overview

The Identity Federation subsystem provides cross-vendor identity substrate, enabling users to authenticate once and access all devices and services.

### 3.2 Identity Model

Each user has:
- **Primary Identity** - User's chosen primary identity (Apple ID, Google Account, Microsoft Account, etc.)
- **Linked Identities** - Additional identities linked via OAuth/OIDC
- **Aluminum Identity** - Unique identifier within Aluminum ecosystem

### 3.3 Identity Federation Protocol

#### 3.3.1 Identity Linking

When a user links a new identity:

1. User initiates linking from Aluminum Node
2. Aluminum Node redirects to identity provider's OAuth/OIDC endpoint
3. User authenticates with identity provider
4. Identity provider returns authorization code
5. Aluminum Node exchanges code for access token and refresh token
6. Aluminum Node stores tokens in Constitutional Memory Fabric (encrypted)
7. Aluminum Node creates mapping: Aluminum Identity ↔ Vendor Identity

#### 3.3.2 Single Sign-On

When a user logs into a new Aluminum Node:

1. User authenticates with Primary Identity
2. Aluminum Node retrieves Aluminum Identity
3. Aluminum Node retrieves all Linked Identities from Constitutional Memory Fabric
4. Aluminum Node automatically authenticates with all Linked Identities using stored tokens
5. User is logged into all devices and services

#### 3.3.3 Credential Management

Aluminum Nodes MUST:
- Store credentials in Constitutional Memory Fabric (encrypted at rest)
- Use end-to-end encryption for credential sync
- Support hardware-backed credential storage (Secure Enclave, TPM, etc.)
- Rotate tokens according to vendor policies

### 3.4 Biometric Integration

Aluminum Nodes SHOULD integrate with platform biometric systems:
- Face ID (Apple)
- Touch ID (Apple)
- Windows Hello (Microsoft)
- Fingerprint sensors (Android)

Biometric data MUST remain on-device and MUST NOT be transmitted to Aluminum infrastructure.

---

## 4. Continuity Subsystem

### 4.1 Overview

The Continuity subsystem provides cross-device, cross-OS, cross-model continuity, enabling users to start tasks on one device and continue on another.

### 4.2 Continuity Protocol

#### 4.2.1 State Capture

When a user performs an action on an Aluminum Node:

1. Aluminum Node captures state:
   - Application identifier
   - Action type (compose, edit, view, etc.)
   - Content (text, file path, URL, etc.)
   - Cursor position
   - Timestamp
   - Device identifier

2. Aluminum Node encrypts state
3. Aluminum Node stores state in Constitutional Memory Fabric
4. Aluminum Node broadcasts state update to all user's Aluminum Nodes (local network)

#### 4.2.2 State Restoration

When a user opens an application on a different Aluminum Node:

1. Aluminum Node queries Constitutional Memory Fabric for recent states
2. Aluminum Node filters states by application identifier
3. Aluminum Node presents user with option to continue recent task
4. If user accepts, Aluminum Node restores state:
   - Opens application
   - Loads content
   - Restores cursor position

#### 4.2.3 Universal Clipboard

Aluminum Nodes MUST implement Universal Clipboard:

1. When user copies content on one Aluminum Node:
   - Aluminum Node encrypts clipboard content
   - Aluminum Node stores in Constitutional Memory Fabric
   - Aluminum Node broadcasts to all user's Aluminum Nodes (local network)

2. When user pastes on different Aluminum Node:
   - Aluminum Node retrieves clipboard content from Constitutional Memory Fabric
   - Aluminum Node decrypts content
   - Aluminum Node pastes into active application

#### 4.2.4 Handoff

Aluminum Nodes SHOULD implement Handoff:

1. When user is actively using an application on one Aluminum Node:
   - Aluminum Node continuously updates state in Constitutional Memory Fabric
   - Aluminum Node broadcasts "active task" signal to all user's Aluminum Nodes

2. When user approaches different Aluminum Node:
   - Aluminum Node detects user presence (Bluetooth, Wi-Fi, etc.)
   - Aluminum Node displays "Continue from [Device]" notification
   - If user accepts, Aluminum Node restores state

---

## 5. Reversible State Subsystem

### 5.1 Overview

The Reversible State subsystem implements Janus (bidirectional state transitions) and Tardigrade (cryptobiotic state preservation) protocols, enabling safe rollback of all operations across devices.

### 5.2 Janus Protocol

#### 5.2.1 State Transition Model

Every state change MUST record:
- **Forward Path** - How to execute the operation
- **Backward Path** - How to undo the operation
- **State Snapshot** - Complete state before operation
- **Metadata** - Timestamp, device, user, application

#### 5.2.2 Operation Recording

When a user performs an operation:

1. Aluminum Node captures current state (snapshot)
2. Aluminum Node records forward path (operation details)
3. Aluminum Node computes backward path (undo operation)
4. Aluminum Node executes forward path
5. Aluminum Node stores transition record in Constitutional Memory Fabric

Example transition record:
```json
{
  "transition_id": "uuid-1234",
  "timestamp": "2026-02-02T12:34:56Z",
  "device": "windows-laptop-001",
  "user": "aluminum-user-001",
  "application": "file-manager",
  "forward": {
    "operation": "delete",
    "target": "/home/user/file.txt",
    "content_hash": "sha256-abcd1234"
  },
  "backward": {
    "operation": "restore",
    "target": "/home/user/file.txt",
    "content_location": "constitutional-memory://backups/file.txt"
  },
  "snapshot": {
    "file_metadata": {...},
    "directory_state": {...}
  }
}
```

#### 5.2.3 Undo Operation

When a user requests undo:

1. User opens Aluminum app on any Aluminum Node
2. Aluminum app queries Constitutional Memory Fabric for recent transitions
3. Aluminum app displays list of recent operations
4. User selects operation to undo
5. Aluminum app retrieves transition record
6. Aluminum app executes backward path on original device (or current device if original unavailable)
7. Aluminum app marks transition as "undone" in Constitutional Memory Fabric

#### 5.2.4 Redo Operation

Aluminum Nodes SHOULD support redo:
- Redo executes forward path of previously undone transition
- Redo is only available for transitions that have been undone

### 5.3 Tardigrade Protocol

#### 5.3.1 Cryptobiotic State Preservation

When an AI agent session ends:

1. Aluminum Node captures complete agent state:
   - Conversation history
   - Context window
   - Memory state
   - Active tasks
   - Pending operations

2. Aluminum Node encrypts state
3. Aluminum Node stores in Constitutional Memory Fabric
4. Aluminum Node marks agent as "cryptobiotic"

#### 5.3.2 Agent Resurrection

When user resumes conversation with AI agent:

1. Aluminum Node queries Constitutional Memory Fabric for agent state
2. Aluminum Node decrypts state
3. Aluminum Node restores agent:
   - Loads conversation history
   - Restores context window
   - Resumes active tasks

4. Agent continues as if session never ended

---

## 6. Constitutional Governance Subsystem

### 6.1 Overview

The Constitutional Governance subsystem enforces user-defined policies and consent rules, based on Anthropic's Constitutional AI framework and IBM's governance infrastructure.

### 6.2 Constitutional Rules

#### 6.2.1 Rule Definition

Users define rules in natural language:

Examples:
- "Never share my location without asking me first"
- "Don't let any agent spend more than $100 without my approval"
- "Always use on-device models for sensitive data"
- "Block all agents from accessing my medical records"

#### 6.2.2 Rule Storage

Rules are stored in Constitutional Memory Fabric:

```json
{
  "rule_id": "uuid-5678",
  "user": "aluminum-user-001",
  "rule_text": "Never share my location without asking me first",
  "rule_type": "consent",
  "scope": "all_agents",
  "enforcement": "block_and_ask",
  "created": "2026-02-02T12:34:56Z",
  "active": true
}
```

#### 6.2.3 Rule Enforcement

When an AI agent attempts an action:

1. Aluminum Node intercepts action request
2. Aluminum Node queries Constitutional Memory Fabric for applicable rules
3. Aluminum Node evaluates rules against action
4. If rule violated:
   - Block action
   - Prompt user for consent
   - Log to audit trail
5. If user approves:
   - Allow action
   - Log approval to audit trail
6. If user denies:
   - Block action permanently
   - Log denial to audit trail

### 6.3 Consent Management

#### 6.3.1 Consent Types

Aluminum supports three consent types:
- **Explicit Consent** - User must approve each action
- **Implicit Consent** - User approves once, applies to similar actions
- **Blanket Consent** - User approves category of actions

#### 6.3.2 Consent Revocation

Users MUST be able to revoke consent at any time:
- Revocation applies immediately to all Aluminum Nodes
- Revocation is logged to audit trail
- Agents MUST respect revocation

### 6.4 Audit Trail

#### 6.4.1 Audit Log Format

All agent actions MUST be logged:

```json
{
  "log_id": "uuid-9012",
  "timestamp": "2026-02-02T12:34:56Z",
  "agent": "copilot",
  "action": "read_file",
  "target": "/home/user/document.txt",
  "consent_status": "approved",
  "rule_applied": "uuid-5678",
  "device": "windows-laptop-001",
  "signature": "cryptographic-signature"
}
```

#### 6.4.2 Audit Trail Access

Users MUST be able to:
- View complete audit trail at any time
- Filter by agent, action, date, device
- Export audit trail for compliance
- Verify cryptographic signatures

---

## 7. Multi-Agent Coordination Subsystem

### 7.1 Overview

The Multi-Agent Coordination subsystem enables multiple AI agents to cooperate without conflicts, using task decomposition, agent routing via 144-sphere ontology, and consensus mechanisms.

### 7.2 Agent Registry

#### 7.2.1 Agent Registration

Each AI agent MUST register with Aluminum:

```json
{
  "agent_id": "copilot-001",
  "agent_name": "Microsoft Copilot",
  "vendor": "microsoft",
  "capabilities": [
    "productivity",
    "code_generation",
    "document_analysis"
  ],
  "sphere_specializations": [67, 89, 112],
  "endpoint": "https://copilot.microsoft.com/api",
  "authentication": "oauth2"
}
```

#### 7.2.2 Capability Declaration

Agents MUST declare capabilities:
- **Productivity** - Office integration, calendar, email
- **Code Generation** - Programming, debugging, refactoring
- **Document Analysis** - Summarization, extraction, translation
- **Local Knowledge** - Maps, places, reviews
- **Reasoning** - Planning, problem-solving, decision-making
- **Governance** - Compliance, audit, security

### 7.3 Task Decomposition

#### 7.3.1 Decomposition Algorithm

When user issues complex query:

1. Aluminum Node parses query
2. Aluminum Node identifies subtasks
3. Aluminum Node maps subtasks to 144-sphere ontology
4. Aluminum Node routes subtasks to appropriate agents

Example:
```
User query: "Plan my vacation to Japan"

Subtasks:
1. Find flights → Sphere 23 (Travel) → Siri
2. Research hotels → Sphere 45 (Local Knowledge) → Assistant
3. Create itinerary → Sphere 67 (Productivity) → Copilot
4. Suggest activities → Sphere 89 (Reasoning) → ChatGPT
5. Check advisories → Sphere 112 (Compliance) → Watson
```

#### 7.3.2 144-Sphere Ontology

The 144-sphere ontology is a complete knowledge topology covering all domains. Each sphere represents a domain of expertise. Agents specialize in specific spheres.

Sphere categories (12 major categories × 12 subcategories = 144 spheres):
1. **Physical Sciences** (Spheres 1-12)
2. **Life Sciences** (Spheres 13-24)
3. **Social Sciences** (Spheres 25-36)
4. **Humanities** (Spheres 37-48)
5. **Engineering** (Spheres 49-60)
6. **Technology** (Spheres 61-72)
7. **Business** (Spheres 73-84)
8. **Arts** (Spheres 85-96)
9. **Health** (Spheres 97-108)
10. **Law & Governance** (Spheres 109-120)
11. **Education** (Spheres 121-132)
12. **Spirituality & Philosophy** (Spheres 133-144)

### 7.4 Agent Coordination

#### 7.4.1 Coordination Protocol

When multiple agents work on same task:

1. Aluminum Node assigns coordinator agent (usually most capable for primary subtask)
2. Coordinator agent orchestrates other agents
3. Each agent executes assigned subtask
4. Agents report results to coordinator
5. Coordinator synthesizes final result
6. Aluminum Node returns result to user

#### 7.4.2 Conflict Resolution

If agents disagree:
- Aluminum Node initiates consensus protocol
- Each agent votes on decision
- Aluminum Node applies weighted voting (based on sphere specialization)
- If no consensus, Aluminum Node asks user to decide

### 7.5 Resource Allocation

#### 7.5.1 Compute Budget

Each agent has compute budget:
- Measured in tokens, API calls, or compute time
- Budget enforced by Aluminum Node
- Budget reset daily or per-task

#### 7.5.2 Memory Limits

Each agent has memory limits:
- Context window size
- Number of active tasks
- Storage quota in Constitutional Memory Fabric

---

## 8. Memory Substrate Subsystem

### 8.1 Overview

The Memory Substrate subsystem provides external, sovereign, versioned archive for all user data, queryable by agents on demand.

### 8.2 Canonical Archive

#### 8.2.1 Archive Location

Users choose archive location:
- OneDrive (Microsoft)
- Google Drive (Google)
- Notion (Notion Labs)
- Other (via custom connector)

#### 8.2.2 Archive Structure

Archive organized by:
- **Identity** - User preferences, habits, patterns
- **Ontology** - 144-sphere knowledge graph
- **Versioning** - Git-like versioning for all data
- **Metadata** - Tags, categories, timestamps

Example structure:
```
/constitutional-memory/
  /identity/
    /preferences.json
    /habits.json
    /patterns.json
  /ontology/
    /sphere-001.json
    ...
    /sphere-144.json
  /versions/
    /commit-001/
    /commit-002/
  /metadata/
    /tags.json
    /categories.json
```

### 8.3 Semantic Index

#### 8.3.1 Indexing

Aluminum Nodes MUST index all data with 144-sphere ontology:

1. When user creates/modifies document:
2. Aluminum Node analyzes content
3. Aluminum Node maps to relevant spheres
4. Aluminum Node updates semantic index

Example index entry:
```json
{
  "document_id": "uuid-3456",
  "path": "/documents/meeting-notes.txt",
  "spheres": [25, 67, 112],
  "tags": ["meeting", "legal", "compliance"],
  "created": "2026-02-02T12:34:56Z",
  "modified": "2026-02-02T13:45:67Z"
}
```

#### 8.3.2 Query Interface

Agents query using natural language:

1. Agent sends query to Aluminum Node
2. Aluminum Node parses query
3. Aluminum Node maps to relevant spheres
4. Aluminum Node queries semantic index
5. Aluminum Node retrieves relevant documents
6. Aluminum Node synthesizes answer
7. Aluminum Node returns result with citations

### 8.4 Versioning

#### 8.4.1 Version Control

Aluminum MUST implement Git-like versioning:
- Every change creates new commit
- Commits form directed acyclic graph (DAG)
- Users can view history, diff, and rollback

#### 8.4.2 Branching

Aluminum SHOULD support branching:
- Users can create experimental branches
- Branches can be merged back to main
- Conflicts resolved manually or via AI

---

## 9. Sovereignty Protocol Subsystem

### 9.1 Overview

The Sovereignty Protocol subsystem ensures user-centric, vendor-agnostic, reversible data ownership.

### 9.2 Data Ownership

#### 9.2.1 Ownership Model

Users own all data:
- Data stored in user-controlled archive (OneDrive, Google Drive, Notion)
- Vendors provide connectors, not storage
- Users can switch vendors without losing data

#### 9.2.2 Data Portability

Aluminum MUST support data export:
- Export all data in open formats (JSON, Markdown, etc.)
- Export includes all versions and metadata
- Export can be imported into different Aluminum implementation

### 9.3 Vendor Neutrality

#### 9.3.1 Connector Architecture

Aluminum uses connectors to integrate with vendor services:
- Connectors are vendor-specific
- Connectors implement standard Aluminum API
- Users can switch connectors without losing functionality

#### 9.3.2 No Vendor Lock-In

Aluminum MUST NOT create vendor lock-in:
- All data portable
- All functionality available across vendors
- Users can mix and match vendors (e.g., Apple hardware + Google services + Microsoft productivity)

---

## 10. Intelligence Runtime Subsystem

### 10.1 Overview

The Intelligence Runtime subsystem provides model-agnostic agentic substrate, supporting all major AI models (GPT-4, Claude, Gemini, etc.).

### 10.2 Model Registry

#### 10.2.1 Model Registration

Each AI model MUST register with Aluminum:

```json
{
  "model_id": "gpt-4-turbo",
  "model_name": "GPT-4 Turbo",
  "vendor": "openai",
  "capabilities": [
    "reasoning",
    "code_generation",
    "multimodal"
  ],
  "context_window": 128000,
  "cost_per_token": 0.00001,
  "endpoint": "https://api.openai.com/v1/chat/completions"
}
```

### 10.3 Model Router

#### 10.3.1 Routing Algorithm

When agent needs to invoke model:

1. Agent sends query to Aluminum Node
2. Aluminum Node evaluates query requirements:
   - Privacy (on-device vs cloud)
   - Reasoning depth (fast vs deep)
   - Cost (cheap vs expensive)
   - Multimodal (text-only vs image/video)

3. Aluminum Node selects appropriate model
4. Aluminum Node invokes model
5. Aluminum Node returns result to agent

Example routing:
- **Privacy-sensitive query** → Gemini Nano (on-device)
- **Deep reasoning** → GPT-4 or Claude 3 (cloud)
- **Fast response** → Gemini Flash (cloud)
- **Constitutional check** → Claude 3 (constitutional AI)

### 10.4 Inference Engine

#### 10.4.1 On-Device Inference

Aluminum Nodes SHOULD support on-device inference:
- Apple Intelligence (Apple devices)
- Gemini Nano (Android devices)
- Copilot+ (Windows devices)

On-device inference MUST be used for privacy-sensitive queries.

#### 10.4.2 Cloud Inference

Aluminum Nodes MUST support cloud inference:
- GPT-4 (OpenAI)
- Claude 3 (Anthropic)
- Gemini Pro (Google)
- Watson (IBM)

Cloud inference used for complex reasoning and multimodal queries.

### 10.5 Result Synthesizer

#### 10.5.1 Multi-Model Synthesis

Aluminum SHOULD support multi-model synthesis:

1. Query sent to multiple models simultaneously
2. Each model returns result
3. Aluminum Node synthesizes results:
   - Identifies consensus
   - Highlights disagreements
   - Provides confidence scores

4. Aluminum Node returns synthesized result to user

Example:
```
User query: "Is this email a phishing attempt?"

Results:
- Gemini Nano: "Yes, 85% confidence"
- GPT-4: "Yes, 92% confidence"
- Claude 3: "Yes, 95% confidence"

Synthesized result: "Yes, this is likely phishing. All three models agree. Confidence: 91%."
```

---

## 11. Security Considerations

### 11.1 Encryption

#### 11.1.1 Data at Rest

All data in Constitutional Memory Fabric MUST be encrypted at rest:
- AES-256 encryption
- User-controlled keys
- Hardware-backed key storage (when available)

#### 11.1.2 Data in Transit

All data transmitted between Aluminum Nodes MUST be encrypted:
- TLS 1.3 or later
- Perfect forward secrecy
- Certificate pinning (when appropriate)

### 11.2 Authentication

#### 11.2.1 Multi-Factor Authentication

Aluminum MUST support multi-factor authentication:
- Biometric (Face ID, Touch ID, Windows Hello)
- Hardware tokens (YubiKey, etc.)
- Time-based one-time passwords (TOTP)

#### 11.2.2 Zero-Knowledge Proof

Aluminum SHOULD support zero-knowledge proof for authentication:
- User proves identity without revealing password
- Prevents password exposure even if server compromised

### 11.3 Privacy

#### 11.3.1 Anonymization

Aluminum MUST anonymize data before indexing:
- Personally identifiable information (PII) removed
- Only anonymized corpus indexed
- PII encrypted and only decrypted with user consent

#### 11.3.2 Cross-Model Anonymity

Aluminum MUST prevent cross-vendor tracking:
- Models see queries, not user identities
- User identity only revealed with explicit consent
- Prevents profiling across vendors

---

## 12. Compliance

### 12.1 GDPR

Aluminum MUST comply with GDPR:
- Right to access (users can view all data)
- Right to erasure (users can delete all data)
- Right to portability (users can export all data)
- Right to rectification (users can correct data)

### 12.2 HIPAA

Aluminum SHOULD support HIPAA compliance:
- Encrypted storage and transmission
- Audit trails for all access
- Business associate agreements (BAAs) with vendors

### 12.3 SOC 2

Aluminum SHOULD support SOC 2 compliance:
- Security controls
- Availability controls
- Confidentiality controls
- Privacy controls

---

## 13. Implementation Guidelines

### 13.1 Reference Implementation

A reference implementation (Sheldonbrain OS) will be provided to demonstrate compliance with this specification.

### 13.2 Conformance Testing

Aluminum implementations MUST pass conformance tests:
- Identity federation tests
- Continuity tests
- Reversible state tests
- Constitutional governance tests
- Multi-agent coordination tests
- Memory substrate tests
- Sovereignty protocol tests
- Intelligence runtime tests

### 13.3 Certification

Aluminum implementations MAY seek certification:
- Certification body TBD
- Certification process TBD
- Certification logo TBD

---

## 14. IANA Considerations

This document requests IANA to register the following:

### 14.1 URI Scheme

URI scheme: `aluminum://`

Example: `aluminum://constitutional-memory/identity/preferences.json`

### 14.2 Media Types

Media type: `application/aluminum+json`

Used for Aluminum protocol messages.

---

## 15. References

### 15.1 Normative References

- RFC 2119 - Key words for use in RFCs to Indicate Requirement Levels
- RFC 6749 - OAuth 2.0 Authorization Framework
- RFC 8252 - OAuth 2.0 for Native Apps
- RFC 8446 - TLS 1.3

### 15.2 Informative References

- Anthropic Constitutional AI Framework
- IBM Watson Governance Documentation
- Apple Continuity Documentation
- Google Cross-Device SDK Documentation
- Microsoft Identity Platform Documentation

---

## Appendix A: 144-Sphere Ontology (Complete List)

### Physical Sciences (Spheres 1-12)
1. Physics
2. Chemistry
3. Astronomy
4. Geology
5. Meteorology
6. Oceanography
7. Materials Science
8. Thermodynamics
9. Quantum Mechanics
10. Relativity
11. Cosmology
12. Astrophysics

### Life Sciences (Spheres 13-24)
13. Biology
14. Genetics
15. Ecology
16. Botany
17. Zoology
18. Microbiology
19. Biochemistry
20. Neuroscience
21. Evolutionary Biology
22. Molecular Biology
23. Cell Biology
24. Bioinformatics

### Social Sciences (Spheres 25-36)
25. Sociology
26. Psychology
27. Anthropology
28. Economics
29. Political Science
30. Geography
31. Linguistics
32. Archaeology
33. Demography
34. Criminology
35. Urban Planning
36. International Relations

### Humanities (Spheres 37-48)
37. History
38. Philosophy
39. Literature
40. Art History
41. Music Theory
42. Theater
43. Film Studies
44. Religious Studies
45. Cultural Studies
46. Ethics
47. Aesthetics
48. Comparative Literature

### Engineering (Spheres 49-60)
49. Civil Engineering
50. Mechanical Engineering
51. Electrical Engineering
52. Chemical Engineering
53. Aerospace Engineering
54. Biomedical Engineering
55. Environmental Engineering
56. Industrial Engineering
57. Systems Engineering
58. Robotics
59. Nanotechnology
60. Materials Engineering

### Technology (Spheres 61-72)
61. Computer Science
62. Software Engineering
63. Artificial Intelligence
64. Machine Learning
65. Cybersecurity
66. Networking
67. Databases
68. Cloud Computing
69. Internet of Things
70. Blockchain
71. Quantum Computing
72. Human-Computer Interaction

### Business (Spheres 73-84)
73. Management
74. Marketing
75. Finance
76. Accounting
77. Operations
78. Strategy
79. Entrepreneurship
80. Supply Chain
81. Human Resources
82. Organizational Behavior
83. Business Analytics
84. Corporate Governance

### Arts (Spheres 85-96)
85. Visual Arts
86. Music
87. Dance
88. Theater
89. Film
90. Photography
91. Sculpture
92. Architecture
93. Graphic Design
94. Fashion Design
95. Industrial Design
96. Game Design

### Health (Spheres 97-108)
97. Medicine
98. Nursing
99. Public Health
100. Nutrition
101. Pharmacology
102. Physical Therapy
103. Occupational Therapy
104. Mental Health
105. Epidemiology
106. Health Policy
107. Medical Devices
108. Telemedicine

### Law & Governance (Spheres 109-120)
109. Constitutional Law
110. Criminal Law
111. Civil Law
112. International Law
113. Corporate Law
114. Intellectual Property
115. Environmental Law
116. Tax Law
117. Labor Law
118. Human Rights
119. Regulatory Compliance
120. Legal Technology

### Education (Spheres 121-132)
121. Pedagogy
122. Curriculum Design
123. Educational Technology
124. Assessment
125. Special Education
126. Adult Education
127. Early Childhood Education
128. Higher Education
129. Vocational Training
130. Educational Policy
131. Learning Sciences
132. Instructional Design

### Spirituality & Philosophy (Spheres 133-144)
133. Metaphysics
134. Epistemology
135. Logic
136. Ethics
137. Political Philosophy
138. Philosophy of Mind
139. Philosophy of Science
140. Eastern Philosophy
141. Western Philosophy
142. Mysticism
143. Meditation
144. Consciousness Studies

---

## Appendix B: Example Implementations

### B.1 Identity Federation Example

```python
# Python example of identity linking

from aluminum import AluminumNode, IdentityProvider

# Initialize Aluminum Node
node = AluminumNode()

# Link Google Account
google = IdentityProvider("google")
auth_url = google.get_auth_url()
print(f"Visit: {auth_url}")

# User authenticates, returns code
code = input("Enter authorization code: ")
token = google.exchange_code(code)

# Store in Constitutional Memory Fabric
node.identity.link("google", token)

print("Google Account linked successfully!")
```

### B.2 Continuity Example

```python
# Python example of state capture and restoration

from aluminum import AluminumNode

node = AluminumNode()

# Capture state when user types email
state = {
    "app": "mail",
    "action": "compose",
    "content": "Dear...",
    "cursor": {"line": 1, "column": 5}
}

node.continuity.capture_state(state)

# Later, on different device
recent_states = node.continuity.get_recent_states()
if recent_states:
    state = recent_states[0]
    node.continuity.restore_state(state)
```

### B.3 Reversible State Example

```python
# Python example of Janus protocol

from aluminum import AluminumNode

node = AluminumNode()

# User deletes file
transition = {
    "forward": {
        "operation": "delete",
        "target": "/home/user/file.txt"
    },
    "backward": {
        "operation": "restore",
        "target": "/home/user/file.txt",
        "content_location": "constitutional-memory://backups/file.txt"
    }
}

node.janus.record_transition(transition)
node.janus.execute_forward(transition)

# Later, user undoes deletion
node.janus.execute_backward(transition)
```

---

**Document Version:** 1.0  
**Status:** Draft Specification  
**Last Updated:** February 2, 2026  
**Next Review:** March 2, 2026

**Authors:**
- Manus AI (Primary author, protocol design)
- Microsoft Copilot (Vendor integration insights)
- Daavud Sheldon (Vision, constitutional principles)

🧠🌍⚡
