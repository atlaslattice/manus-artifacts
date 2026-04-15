# ALUMINUM v2.1 – KERNEL + PLUGIN ARCHITECTURE
## Build-Ready Specification for Manus Implementation

**Version:** 2.1  
**Date:** February 2, 2026  
**Authors:** Daavud Sheldon, Manus AI, Microsoft Copilot  
**Status:** BUILD-READY - IMPLEMENTATION IN PROGRESS

---

## Executive Summary

Aluminum v2.1 represents the transition from architectural vision to **build-ready implementation**. This specification defines the canonical "syscalls" of the Aluminum Intelligence OS—the kernel interface that all plugins, agents, and applications must use to participate in the unified intelligence layer.

**Key Innovation:** Rather than building yet another standalone application, Aluminum v2.1 establishes a **kernel + plugin architecture** where existing applications (Outlook, Gmail, OneDrive, Google Drive, etc.) become **plugins** that attach to a unified intelligence substrate. This approach preserves vendor sovereignty while enabling cross-platform coordination, constitutional governance, and universal reversibility.

**Build Target:** The judgment-enforcer webapp serves as the reference implementation, demonstrating how the Aluminum kernel can coordinate multiple agents and plugins within a single, unified interface.

---

## 1. Aluminum Kernel Interface (v2.1)

The Aluminum Kernel provides five canonical APIs that form the foundation of the intelligence layer. Every plugin, agent, and application must interact with these APIs to participate in the Aluminum ecosystem.

### 1.1 Intent Routing API

**Purpose:** Determine which agent or plugin should handle a user's intent based on context, capabilities, and constraints.

**Conceptual Signature:**

**Input:**
- `intent_text` (string) - Natural language description of user's goal
- `context_snapshot` (JSON) - Current state including:
  - `active_app` - Currently focused application
  - `selection` - Selected text, files, or objects
  - `user_state` - User preferences, history, and context
  - `device_info` - Device type, capabilities, location
- `constraints` (JSON) - Execution constraints including:
  - `time_limit` - Maximum execution time
  - `risk_level` - Acceptable risk threshold
  - `device_restrictions` - Device-specific limitations
  - `privacy_requirements` - Data handling requirements

**Output:**
- `selected_agent` (string) - Identifier of chosen agent/plugin (e.g., "OutlookPlugin", "GmailPlugin", "ResearchAgent")
- `plan` (JSON array) - Ordered list of actions, each containing:
  - `step_id` - Unique identifier for this step
  - `action_schema` - Structured action definition (see Executor Adapter API)
  - `dependencies` - Prerequisites for this step
  - `estimated_duration` - Expected execution time
- `confidence` (float, 0-1) - Confidence score for this routing decision
- `alternatives` (JSON array) - Alternative agents/plans if primary fails

**Implementation Notes for Manus:**

Implement this as a **router service** that maintains a registry of available plugins and their capabilities. The router should:

1. Parse the intent using natural language understanding
2. Query the plugin registry for candidates
3. Score each candidate based on capabilities, context, and constraints
4. Select the highest-scoring candidate
5. Generate an execution plan by querying the selected plugin's intent handler
6. Return the plan with confidence score

The router must be extensible—new plugins register their capabilities dynamically, and the router automatically considers them for future intents.

**Example Flow:**

```
User: "Send email to John about the project update"

Intent Routing API receives:
{
  "intent_text": "Send email to John about the project update",
  "context_snapshot": {
    "active_app": "ProjectManagementTool",
    "selection": "Q4 Roadmap Document",
    "user_state": {
      "primary_email": "outlook",
      "recent_contacts": ["john@company.com"]
    }
  },
  "constraints": {
    "time_limit": 30000,
    "risk_level": "low",
    "privacy_requirements": "corporate"
  }
}

Intent Routing API returns:
{
  "selected_agent": "OutlookPlugin",
  "plan": [
    {
      "step_id": "1",
      "action_schema": {
        "target": "Outlook",
        "operation": "compose_message",
        "parameters": {
          "to": "john@company.com",
          "subject": "Project Update",
          "body": "[Generated from Q4 Roadmap]",
          "attachments": ["Q4_Roadmap.pdf"]
        }
      }
    }
  ],
  "confidence": 0.95,
  "alternatives": ["GmailPlugin"]
}
```

---

### 1.2 Policy Kernel API

**Purpose:** Determine whether a proposed plan is allowed, requires approval, or must be blocked based on constitutional rules and user preferences.

**Conceptual Signature:**

**Input:**
- `plan` (JSON array) - List of actions from Intent Routing API
- `context` (JSON) - Execution context including:
  - `user_id` - User identifier
  - `device_id` - Device identifier
  - `app_context` - Application state
  - `risk_profile` - Computed risk assessment
- `policy_version` (string) - Version of constitutional rules to apply

**Output:**
- `decision` (enum) - One of:
  - `"allow"` - Execute immediately
  - `"requires_approval"` - User must approve before execution
  - `"block"` - Execution forbidden
- `rationale` (string) - Human-readable explanation of decision
- `logging_directives` (JSON) - What to log and where:
  - `log_level` - Verbosity of logging
  - `destinations` - Where to write logs (provenance, audit trail, etc.)
  - `retention_policy` - How long to retain logs
- `required_approvals` (JSON array) - If decision is "requires_approval":
  - `approver_id` - Who must approve
  - `approval_type` - Type of approval required
  - `timeout` - How long to wait for approval

**Implementation Notes for Manus:**

Start with a **3-class classifier** similar to the Symbiote governance system:

1. **Safe** - Low-risk actions that can execute immediately (reading data, searching, displaying information)
2. **Approval Required** - Medium-risk actions that need user confirmation (sending messages, modifying files, making purchases)
3. **Blocked** - High-risk actions that violate constitutional rules (sharing private data without consent, deleting critical files, etc.)

Expose this as a **kernel service** that every adapter must call before executing any action. The Policy Kernel maintains the user's constitutional rules and applies them consistently across all plugins and agents.

**Example Constitutional Rules:**

```
- "Never share my location without asking"
- "Always require approval before spending money"
- "Block any action that deletes files older than 30 days"
- "Require biometric approval for financial transactions"
- "Log all actions that access medical records"
```

**Example Flow:**

```
Policy Kernel receives:
{
  "plan": [
    {
      "action_schema": {
        "target": "Outlook",
        "operation": "send_message",
        "parameters": {
          "to": "john@company.com",
          "subject": "Project Update",
          "attachments": ["Q4_Roadmap.pdf"]
        }
      }
    }
  ],
  "context": {
    "user_id": "daavud",
    "device_id": "chromebook_1",
    "risk_profile": "medium"
  },
  "policy_version": "v1.0"
}

Policy Kernel returns:
{
  "decision": "requires_approval",
  "rationale": "Sending email with attachment requires user confirmation per constitutional rule #7",
  "logging_directives": {
    "log_level": "detailed",
    "destinations": ["provenance", "audit_trail"],
    "retention_policy": "7_years"
  },
  "required_approvals": [
    {
      "approver_id": "daavud",
      "approval_type": "explicit_consent",
      "timeout": 300000
    }
  ]
}
```

---

### 1.3 Provenance API

**Purpose:** Establish lineage for every artifact and action, creating an immutable audit trail that enables accountability, debugging, and reversibility.

**Conceptual Signature:**

**Input:**
- `artifact_type` (enum) - Type of artifact:
  - `"message"` - Email, chat message, etc.
  - `"file"` - Document, image, etc.
  - `"event"` - Calendar event, reminder, etc.
  - `"state_change"` - System state modification
  - `"approval"` - User approval record
  - `"policy_decision"` - Policy Kernel decision
- `content_hash` (string) - Cryptographic hash of artifact content
- `parents` (array of artifact IDs) - Artifacts that led to this one
- `produced_by` (JSON) - Agent/model that created this artifact:
  - `agent_id` - Identifier of agent/plugin
  - `model_version` - Version of AI model used
  - `plugin_version` - Version of plugin
- `policy_regime` (JSON) - Constitutional context:
  - `constitution_version` - Version of rules applied
  - `rules_triggered` - Specific rules that applied
  - `policy_decision_id` - Reference to Policy Kernel decision
- `executor` (string) - Executor that performed the action (e.g., "ChromeOS_DOM_Adapter_v1")
- `timestamps` (JSON) - Temporal metadata:
  - `created_at` - When artifact was created
  - `modified_at` - When artifact was last modified
  - `executed_at` - When action was executed
- `approvals` (array) - Approval signatures if required:
  - `approver_id` - Who approved
  - `approval_type` - Type of approval
  - `signature` - Cryptographic signature
  - `timestamp` - When approved

**Output:**
- `artifact_id` (string) - Immutable identifier for this artifact
- `provenance_record_location` (URI) - Where the full provenance record is stored

**Implementation Notes for Manus:**

Implement as a **write-once, append-only log** that creates an immutable audit trail. Every action, artifact, and decision must be logged through the Provenance API. The provenance records enable:

1. **Accountability** - Who did what, when, and why
2. **Debugging** - Trace the lineage of any artifact back to its origin
3. **Reversibility** - Undo operations by following the provenance chain
4. **Compliance** - Demonstrate GDPR, HIPAA, SOC 2 compliance
5. **Trust** - Users can inspect the provenance of any artifact

The Provenance API should support queries like:
- "Show me all artifacts created by Agent X in the last 24 hours"
- "What actions led to the creation of this file?"
- "Which constitutional rules were triggered for this decision?"
- "Who approved this transaction?"

**Example Flow:**

```
Provenance API receives:
{
  "artifact_type": "message",
  "content_hash": "sha256:a3f2b1...",
  "parents": ["artifact_123", "artifact_456"],
  "produced_by": {
    "agent_id": "OutlookPlugin",
    "model_version": "gpt-4-turbo",
    "plugin_version": "v1.2.0"
  },
  "policy_regime": {
    "constitution_version": "v1.0",
    "rules_triggered": ["rule_7"],
    "policy_decision_id": "policy_789"
  },
  "executor": "ChromeOS_DOM_Adapter_v1",
  "timestamps": {
    "created_at": "2026-02-02T10:30:00Z",
    "executed_at": "2026-02-02T10:30:15Z"
  },
  "approvals": [
    {
      "approver_id": "daavud",
      "approval_type": "explicit_consent",
      "signature": "sig_xyz...",
      "timestamp": "2026-02-02T10:30:10Z"
    }
  ]
}

Provenance API returns:
{
  "artifact_id": "artifact_999",
  "provenance_record_location": "aluminum://provenance/artifact_999"
}
```

---

### 1.4 State / Version Control API

**Purpose:** Treat conversations, artifacts, and system state as versioned entities that can be branched, merged, diffed, and reverted.

**Core Operations:**

**1. Branch**
- **Signature:** `branch(target_id, label) → new_branch_id`
- **Purpose:** Create a new branch from an existing state
- **Use Case:** "Try a different approach to this conversation without losing the original"

**2. Merge**
- **Signature:** `merge(source_branch, target_branch, strategy) → merged_state + conflict_report`
- **Purpose:** Combine two branches into a single state
- **Strategies:**
  - `"ours"` - Prefer target branch in conflicts
  - `"theirs"` - Prefer source branch in conflicts
  - `"manual"` - Require user resolution of conflicts
- **Use Case:** "Combine insights from two parallel research threads"

**3. Diff**
- **Signature:** `diff(a, b) → structured_diff`
- **Purpose:** Compute structured difference between two states
- **Output:** JSON describing:
  - Added elements
  - Removed elements
  - Modified elements
  - Metadata changes
- **Use Case:** "Show me what changed in this conversation"

**4. Revert**
- **Signature:** `revert(target_id, snapshot_id) → restored_state`
- **Purpose:** Restore a previous state
- **Use Case:** "Undo the last 5 messages in this conversation"

**Implementation Notes for Manus:**

Start with **conversational version control** as the primary use case:

1. **Branch a conversation thread** - User can explore alternative responses without losing the original thread
2. **Diff two conversation versions** - Show what changed between two points in a conversation
3. **Revert to pre-change state** - Undo messages, actions, or decisions

Later, extend to:
- **File version control** - Track changes to documents, spreadsheets, etc.
- **System state version control** - Snapshot and restore entire system configurations
- **Multi-agent coordination version control** - Track how different agents contributed to a result

**Example Flow:**

```
User: "Branch this conversation to explore a different approach"

State/Version Control API receives:
{
  "operation": "branch",
  "target_id": "conversation_123",
  "label": "alternative_approach"
}

State/Version Control API returns:
{
  "new_branch_id": "conversation_123_branch_1",
  "snapshot_id": "snapshot_456",
  "parent_id": "conversation_123"
}

---

Later, user: "Show me the diff between the two approaches"

State/Version Control API receives:
{
  "operation": "diff",
  "a": "conversation_123",
  "b": "conversation_123_branch_1"
}

State/Version Control API returns:
{
  "diff": {
    "added_messages": [
      {"id": "msg_789", "content": "Let's try a different approach..."}
    ],
    "removed_messages": [],
    "modified_messages": [
      {"id": "msg_456", "old_content": "...", "new_content": "..."}
    ]
  }
}

---

Later, user: "Revert to the original conversation"

State/Version Control API receives:
{
  "operation": "revert",
  "target_id": "conversation_123_branch_1",
  "snapshot_id": "snapshot_456"
}

State/Version Control API returns:
{
  "restored_state": "conversation_123",
  "reverted_changes": ["msg_789", "msg_456"]
}
```

---

### 1.5 Executor Adapter API

**Purpose:** Provide a unified interface for executing actions across different platforms (OS, web, apps) with consistent error handling, logging, and reversibility.

**Action Schema:**

Every action executed through the Executor Adapter must conform to this schema:

```json
{
  "target": "string",           // e.g., "Outlook", "Gmail", "ChromeTab", "FileSystem"
  "selector": "string",          // DOM selector, API endpoint, or resource path
  "operation": "string",         // e.g., "click", "set_value", "send_message", "move_file"
  "parameters": {},              // Operation-specific parameters
  "preconditions": [],           // Optional: conditions that must be true before execution
  "postconditions": [],          // Optional: conditions that must be true after execution
  "idempotency_key": "string"    // Optional: ensures action executes only once
}
```

**Conceptual Signature:**

**Input:**
- `action_schema` (JSON) - Structured action definition (see above)

**Output:**
- `result` (JSON) - Execution result including:
  - `success` (boolean) - Whether action succeeded
  - `data` - Result data (if any)
  - `error` - Error details (if failed)
- `receipts` (JSON array) - Execution receipts:
  - `log_entries` - Log messages
  - `artifact_ids` - Provenance artifact IDs
  - `screenshots` - Screenshots of execution (if applicable)
- `undo_handle` (string, optional) - Handle for reversing this action

**Implementation Notes for Manus:**

The ChromeOS DOM adapter in the Symbiote system is already a **v1 Executor Adapter**. Generalize it to support:

1. **Multiple targets** - Not just Chrome DOM, but also:
   - Native OS operations (file system, notifications, etc.)
   - API calls (REST, GraphQL, etc.)
   - Other browsers (Firefox, Safari, etc.)
   - Mobile platforms (Android, iOS)

2. **Consistent error handling** - All executors return the same error format

3. **Automatic logging** - All actions are logged via Provenance API

4. **Reversibility** - When possible, return an `undo_handle` that can be used to reverse the action

5. **Preconditions and postconditions** - Validate state before and after execution

**Example Flow:**

```
Executor Adapter receives:
{
  "action_schema": {
    "target": "Outlook",
    "selector": "#compose-button",
    "operation": "click",
    "parameters": {},
    "preconditions": [
      {"type": "element_visible", "selector": "#compose-button"}
    ],
    "postconditions": [
      {"type": "element_visible", "selector": "#compose-window"}
    ]
  }
}

Executor Adapter returns:
{
  "result": {
    "success": true,
    "data": {
      "compose_window_id": "window_123"
    }
  },
  "receipts": {
    "log_entries": ["Clicked compose button at 10:30:15"],
    "artifact_ids": ["artifact_999"],
    "screenshots": ["screenshot_123.png"]
  },
  "undo_handle": "undo_compose_click_123"
}
```

---

## 2. Aluminum Plugin Architecture – "One Hub"

The Aluminum Plugin Architecture replaces standalone applications with **plugins** that attach to the kernel. Instead of running Outlook, Gmail, OneDrive, and Google Drive as separate apps, users interact with a **unified hub** where these services appear as plugins providing messaging, calendar, files, and other capabilities.

### 2.1 Plugin Types

Aluminum defines several standard plugin types, each representing a category of functionality:

**1. Messaging Plugin**
- Handles email, chat, and other messaging
- Examples: Outlook, Gmail, Teams, Slack

**2. Calendar Plugin**
- Manages events, meetings, and schedules
- Examples: Outlook Calendar, Google Calendar

**3. Files Plugin**
- Provides file storage and synchronization
- Examples: OneDrive, Google Drive, Dropbox, Local FileSystem

**4. Docs Plugin**
- Enables document creation and editing
- Examples: Word, Google Docs, Notion

**5. Tasks Plugin**
- Manages todos, projects, and task lists
- Examples: Microsoft Planner, Google Tasks, Todoist, Asana

**6. Notes Plugin**
- Captures quick notes and ideas
- Examples: OneNote, Google Keep, Apple Notes

**7. Contacts Plugin**
- Manages people and relationships
- Examples: Outlook Contacts, Google Contacts

**8. Intelligence Plugin**
- Provides AI capabilities and reasoning
- Examples: Copilot, ChatGPT, Claude, Gemini

### 2.2 Plugin Interface

Every plugin must implement the following interface to participate in the Aluminum ecosystem:

**1. Registration Descriptor**

When a plugin registers with the kernel, it provides a descriptor:

```json
{
  "plugin_id": "string",              // Unique identifier (e.g., "outlook_plugin_v1")
  "plugin_name": "string",            // Human-readable name (e.g., "Microsoft Outlook")
  "plugin_version": "string",         // Semantic version (e.g., "1.2.0")
  "capabilities": [                   // What this plugin can do
    "messaging.read",
    "messaging.send",
    "messaging.search",
    "calendar.read",
    "calendar.create"
  ],
  "supported_accounts": [             // Which account types it supports
    "Microsoft",
    "Office365"
  ],
  "required_permissions": [           // What permissions it needs
    "dom_access",
    "api_access"
  ],
  "executor_type": "string"           // How it executes actions (e.g., "dom", "api", "native")
}
```

**2. Intent Handlers**

Plugins must implement two methods for intent handling:

**`can_handle(intent) → boolean + score`**

Determines if this plugin can handle a given intent and how well:

```javascript
can_handle(intent) {
  // Parse intent
  // Check if capabilities match
  // Return score (0-1) indicating confidence
  
  return {
    can_handle: true,
    score: 0.95,
    rationale: "This plugin can send emails via Outlook"
  };
}
```

**`handle(intent, context) → plan`**

Generates an execution plan for the intent:

```javascript
handle(intent, context) {
  // Generate list of actions
  // Return structured plan
  
  return {
    plan: [
      {
        step_id: "1",
        action_schema: {
          target: "Outlook",
          operation: "send_message",
          parameters: { /* ... */ }
        }
      }
    ],
    estimated_duration: 5000,
    required_permissions: ["messaging.send"]
  };
}
```

**3. Executor Bindings**

Plugins use the **Executor Adapter API** to perform actions. They don't execute directly—they generate action schemas that the Executor Adapter executes.

**4. Provenance Hooks**

Plugins must call the **Provenance API** for every message, file, event, or other artifact they create or modify.

### 2.3 One Hub UI Model

The "One Hub" is a unified interface where all plugins render their views. Instead of switching between Outlook, Gmail, OneDrive, and Google Drive, users see a single interface with panels for:

- **Messaging** - Unified inbox showing Outlook + Gmail
- **Calendar** - Unified calendar showing all events
- **Files** - Unified file browser showing OneDrive + Google Drive
- **Notes** - Unified notes from Keep + OneNote
- **Agent Console** - AI agents and their conversations

**Data Model:**

The One Hub organizes work into **Workstreams**:

```json
{
  "workstream": {
    "id": "string",
    "title": "string",
    "description": "string",
    "participants": [
      {"type": "human", "id": "daavud"},
      {"type": "agent", "id": "copilot"},
      {"type": "agent", "id": "gemini"}
    ],
    "artifacts": [
      {"type": "message", "id": "msg_123", "plugin": "outlook"},
      {"type": "file", "id": "file_456", "plugin": "onedrive"},
      {"type": "task", "id": "task_789", "plugin": "planner"}
    ],
    "plugins_involved": ["outlook", "onedrive", "planner"],
    "created_at": "2026-02-02T10:00:00Z",
    "updated_at": "2026-02-02T10:30:00Z"
  }
}
```

**Panel Types:**

Each panel type renders artifacts from one or more plugins:

- **Messaging Panel** - Shows messages from Outlook + Gmail plugins
- **Calendar Panel** - Shows events from Outlook Calendar + Google Calendar plugins
- **Files Panel** - Shows files from OneDrive + Google Drive plugins
- **Notes Panel** - Shows notes from Keep + OneNote plugins
- **Agent Console Panel** - Shows conversations with AI agents

**Implementation Notes for Manus:**

Think of the One Hub as a **canvas** where plugins render their views. The canvas provides:

1. **Layout management** - Panels can be resized, moved, hidden
2. **State synchronization** - Changes in one panel update related panels
3. **Unified search** - Search across all plugins
4. **Unified notifications** - Notifications from all plugins in one place

All business logic goes through the kernel—plugins are just views.

---

## 3. Messaging Plugin Interface (Outlook + Gmail – Phase 3 Target)

The Messaging Plugin is the first "Plugin Wrap" target for implementation. It demonstrates how to wrap existing applications (Outlook, Gmail) as Aluminum plugins.

### 3.1 Unified Message Schema

All messaging plugins must map their native message format to the Aluminum Unified Message Schema:

```json
{
  "message_id": "string",              // Unique identifier
  "thread_id": "string",               // Conversation thread identifier
  "from": {
    "name": "string",
    "address": "string",               // Email address
    "account_type": "string"           // "Microsoft" or "Google"
  },
  "to": [                              // Array of recipients
    {"name": "string", "address": "string"}
  ],
  "cc": [                              // Array of CC recipients
    {"name": "string", "address": "string"}
  ],
  "bcc": [                             // Array of BCC recipients
    {"name": "string", "address": "string"}
  ],
  "subject": "string",
  "body": {
    "html": "string",                  // HTML version
    "text": "string"                   // Plain text version
  },
  "attachments": [                     // Array of file references
    {
      "file_id": "string",
      "filename": "string",
      "mime_type": "string",
      "size_bytes": "number"
    }
  ],
  "timestamp_sent": "ISO8601",
  "timestamp_received": "ISO8601",
  "labels": ["string"],                // Tags/labels/folders
  "source_system": "string",           // "Outlook" or "Gmail"
  "raw_metadata": {}                   // Original metadata from source system
}
```

**Implementation Notes for Manus:**

Create adapters that transform native message formats:

**Outlook Adapter:**
```javascript
function outlookToUnified(outlookMessage) {
  return {
    message_id: outlookMessage.id,
    thread_id: outlookMessage.conversationId,
    from: {
      name: outlookMessage.from.emailAddress.name,
      address: outlookMessage.from.emailAddress.address,
      account_type: "Microsoft"
    },
    // ... map other fields
    source_system: "Outlook"
  };
}
```

**Gmail Adapter:**
```javascript
function gmailToUnified(gmailMessage) {
  return {
    message_id: gmailMessage.id,
    thread_id: gmailMessage.threadId,
    from: {
      name: parseEmailName(gmailMessage.payload.headers.from),
      address: parseEmailAddress(gmailMessage.payload.headers.from),
      account_type: "Google"
    },
    // ... map other fields
    source_system: "Gmail"
  };
}
```

### 3.2 Messaging Plugin Operations

Every messaging plugin must support these operations:

**1. list_threads(filter)**
- Lists conversation threads
- Supports filtering by:
  - Date range
  - Sender/recipient
  - Labels/folders
  - Read/unread status
  - Has attachments
- Returns array of thread summaries

**2. get_thread(thread_id)**
- Retrieves full conversation thread
- Returns all messages in thread
- Includes all metadata and attachments

**3. send_message(message)**
- Sends a new message or reply
- Supports:
  - New messages
  - Replies
  - Forwards
  - Attachments
- Returns message_id of sent message

**4. apply_label(message_id, label)**
- Applies label/tag/folder to message
- Creates label if it doesn't exist
- Returns updated message

**5. archive(message_id)**
- Archives message (removes from inbox)
- Message remains searchable
- Returns success status

**6. search(query)**
- Searches messages
- Supports:
  - Full-text search
  - Metadata search (sender, date, etc.)
  - Advanced queries
- Returns array of matching messages

**Implementation Notes for Manus:**

All operations must:

1. **Go through Policy Kernel** - Check if operation is allowed
2. **Log via Provenance API** - Record every operation
3. **Execute via Executor Adapter** - Use DOM or API to perform action
4. **Return undo_handle** - Enable reversibility when possible

**Example Flow:**

```javascript
async function send_message(message) {
  // 1. Check policy
  const policy_decision = await policyKernel.check({
    plan: [{
      action_schema: {
        target: "Outlook",
        operation: "send_message",
        parameters: message
      }
    }]
  });
  
  if (policy_decision.decision === "block") {
    throw new Error(policy_decision.rationale);
  }
  
  if (policy_decision.decision === "requires_approval") {
    await requestApproval(policy_decision.required_approvals);
  }
  
  // 2. Execute action
  const result = await executorAdapter.execute({
    action_schema: {
      target: "Outlook",
      operation: "send_message",
      parameters: message
    }
  });
  
  // 3. Log provenance
  const artifact_id = await provenanceAPI.log({
    artifact_type: "message",
    content_hash: hashMessage(message),
    produced_by: {
      agent_id: "OutlookPlugin",
      plugin_version: "v1.0.0"
    },
    executor: "ChromeOS_DOM_Adapter_v1",
    policy_decision_id: policy_decision.id
  });
  
  // 4. Return result with undo handle
  return {
    message_id: result.data.message_id,
    artifact_id: artifact_id,
    undo_handle: result.undo_handle
  };
}
```

### 3.3 Unified Messaging Stream

**Goal:** A single "Messages" panel that shows Outlook + Gmail threads in a unified view.

**Features:**

1. **Unified inbox** - All messages from all accounts
2. **Thread consolidation** - Messages about the same topic grouped together
3. **Cross-account search** - Search across all accounts simultaneously
4. **Unified compose** - Send from any account
5. **Smart filtering** - Filter by source, date, sender, etc.
6. **Unified labels** - Apply labels that work across accounts

**Implementation Notes for Manus:**

Build three components:

**1. Outlook Plugin**
- Implements Messaging Plugin Interface
- Wraps Outlook web interface or API
- Maps Outlook messages to Unified Message Schema

**2. Gmail Plugin**
- Implements Messaging Plugin Interface
- Wraps Gmail web interface or API
- Maps Gmail messages to Unified Message Schema

**3. Unified Messages View**
- Consumes Unified Message Schema
- Displays messages from all plugins
- Provides unified operations (compose, search, filter)

**Data Flow:**

```
Outlook Web → Outlook Plugin → Unified Message Schema → Unified Messages View
Gmail Web → Gmail Plugin → Unified Message Schema → Unified Messages View
```

---

## 4. Provenance + Reversibility Kernel (Killer Feature #0)

**Killer Feature #0** establishes provenance, approvals, and reversibility as **first-class kernel services**. This is not an optional feature—it is the foundation of trust, accountability, and safety in the Aluminum ecosystem.

### 4.1 Core Principles

**1. No Artifact Without Lineage**

Every artifact (message, file, event, state change) must have a provenance record that answers:
- Who created it?
- When was it created?
- What led to its creation?
- Which constitutional rules applied?
- Who approved it (if required)?

**2. No Execution Without Policy Decision**

Every action must be evaluated by the Policy Kernel before execution. The policy decision is logged and becomes part of the provenance record.

**3. Every Action Yields an Auditable Receipt**

After execution, the system generates a receipt containing:
- What was executed
- When it was executed
- Who executed it
- What the result was
- Where the provenance record is stored

**4. Reversibility When Possible**

When an action can be reversed, the system returns an `undo_handle` that can be used to revert the action. Reversibility is a best-effort feature—not all actions can be undone (e.g., sending an email), but the system should provide undo handles whenever possible.

### 4.2 Implementation Pattern

For every action in the Aluminum ecosystem, follow this pattern:

**Step 1: Policy Check**
```javascript
const policy_decision = await policyKernel.check({
  plan: [action],
  context: execution_context
});

if (policy_decision.decision === "block") {
  throw new Error(policy_decision.rationale);
}

if (policy_decision.decision === "requires_approval") {
  await requestApproval(policy_decision.required_approvals);
}
```

**Step 2: Execute Action**
```javascript
const result = await executorAdapter.execute({
  action_schema: action
});
```

**Step 3: Log Provenance**
```javascript
const artifact_id = await provenanceAPI.log({
  artifact_type: "...",
  content_hash: "...",
  produced_by: {...},
  policy_regime: {
    policy_decision_id: policy_decision.id
  },
  executor: "...",
  timestamps: {...}
});
```

**Step 4: Store Undo Handle**
```javascript
if (result.undo_handle) {
  await storeUndoHandle(artifact_id, result.undo_handle);
}
```

**Step 5: Return Receipt**
```javascript
return {
  success: true,
  artifact_id: artifact_id,
  undo_handle: result.undo_handle,
  provenance_record: `aluminum://provenance/${artifact_id}`
};
```

### 4.3 Reversibility Strategies

Different types of actions require different reversibility strategies:

**1. Immediate Undo (Local State)**
- Example: Typing text, moving windows, changing settings
- Strategy: Store previous state, restore on undo
- Latency: <100ms

**2. Deferred Undo (Remote State)**
- Example: Sending email, creating file, scheduling event
- Strategy: Store compensating action, execute on undo
- Latency: 100ms-5s
- Note: May not be possible for all actions (e.g., sent emails)

**3. Snapshot Undo (Complex State)**
- Example: Multi-step workflows, agent conversations
- Strategy: Create snapshots at key points, restore on undo
- Latency: 1-10s

**4. Provenance-Based Undo (Audit Trail)**
- Example: Debugging, compliance investigations
- Strategy: Use provenance records to reconstruct history
- Latency: 10s-1min

---

## 5. Build Order for Manus (Phase 3 – "Live Substrate")

This section defines the exact implementation steps for building Aluminum v2.1 in the judgment-enforcer webapp.

### Step 1: Kernel Skeleton (Week 1-2)

**Goal:** Implement stubs for all five kernel APIs.

**Tasks:**

1. **Create kernel directory structure**
```
server/
  aluminum/
    kernel/
      intent-routing.ts      // Intent Routing API
      policy-kernel.ts       // Policy Kernel API
      provenance.ts          // Provenance API
      version-control.ts     // State/Version Control API
      executor-adapter.ts    // Executor Adapter API
    types/
      kernel.ts              // TypeScript types for kernel APIs
    utils/
      plugin-registry.ts     // Plugin registration and discovery
```

2. **Implement stub APIs**
- Each API returns mock data
- TypeScript interfaces define contracts
- No real execution yet—just structure

3. **Create plugin registry**
- Plugins can register capabilities
- Intent router can query registry
- Simple in-memory implementation

4. **Add kernel tests**
- Unit tests for each API
- Integration tests for plugin registration
- Test data fixtures

**Deliverable:** Kernel skeleton with passing tests

---

### Step 2: ChromeOS Executor Adapter (Week 3-4)

**Goal:** Stabilize the Symbiote DOM adapter and integrate it as an Executor Adapter.

**Tasks:**

1. **Normalize DOM action schema**
- Define standard action types (click, input, scroll, etc.)
- Map Symbiote actions to Executor Adapter schema
- Add preconditions and postconditions

2. **Add undo support**
- Store previous state before actions
- Generate undo handles
- Implement undo operations

3. **Wire into Policy Kernel**
- Call Policy Kernel before every action
- Handle approval requests
- Log policy decisions

4. **Wire into Provenance API**
- Log every action
- Store artifact IDs
- Link to policy decisions

5. **Add error handling**
- Consistent error format
- Retry logic
- Fallback strategies

**Deliverable:** ChromeOS Executor Adapter integrated with kernel

---

### Step 3: Messaging Plugins (Week 5-8)

**Goal:** Build Outlook and Gmail plugins with unified messaging view.

**Tasks:**

1. **Define Unified Message Schema**
- TypeScript interface
- Validation logic
- Test fixtures

2. **Build Outlook Plugin**
- Implement plugin interface
- Map Outlook messages to unified schema
- Implement all messaging operations
- Add tests

3. **Build Gmail Plugin**
- Implement plugin interface
- Map Gmail messages to unified schema
- Implement all messaging operations
- Add tests

4. **Build Unified Messages View**
- React component for message list
- Thread view
- Compose interface
- Search and filter

5. **Integration testing**
- Test Outlook plugin end-to-end
- Test Gmail plugin end-to-end
- Test unified view with both plugins

**Deliverable:** Working unified messaging with Outlook + Gmail

---

### Step 4: Conversational Version Control (Week 9-10)

**Goal:** Implement branch/diff/revert for conversations and agent plans.

**Tasks:**

1. **Implement State/Version Control API**
- Branch operation
- Merge operation
- Diff operation
- Revert operation

2. **Add conversation versioning**
- Store conversation snapshots
- Track conversation branches
- Compute conversation diffs

3. **Add UI for version control**
- Branch button in conversation UI
- Diff viewer
- Revert button

4. **Add agent plan versioning**
- Store plan snapshots
- Track plan branches
- Compute plan diffs

5. **Integration testing**
- Test branching conversations
- Test diffing conversations
- Test reverting conversations

**Deliverable:** Working conversational version control

---

### Step 5: Biometric Binding (Week 11-12, Optional)

**Goal:** Treat biometrics as identity signals for approval workflows.

**Tasks:**

1. **Define biometric identity model**
- Biometric signals as identity factors
- Not magic locks, just additional verification

2. **Integrate with Policy Kernel**
- Certain actions require biometric approval
- Biometric approval logged in provenance

3. **Add biometric approval UI**
- Prompt for biometric when required
- Show approval status

4. **Testing**
- Test biometric approval flow
- Test fallback to non-biometric approval

**Deliverable:** Biometric approval for high-risk actions

---

## 6. Success Metrics

**Phase 3 (Live Substrate) Success Criteria:**

1. **Kernel APIs Operational**
   - All 5 kernel APIs implemented and tested
   - Plugin registry working
   - 100% test coverage for kernel

2. **Messaging Plugins Working**
   - Outlook plugin functional
   - Gmail plugin functional
   - Unified messaging view operational
   - Can send/receive messages through both plugins

3. **Provenance + Reversibility**
   - All actions logged via Provenance API
   - All actions checked via Policy Kernel
   - Undo handles generated when possible
   - Can revert at least 80% of actions

4. **Conversational Version Control**
   - Can branch conversations
   - Can diff conversations
   - Can revert conversations
   - UI for version control working

5. **Performance**
   - Intent routing: <100ms
   - Policy check: <50ms
   - Provenance logging: <20ms
   - Action execution: <500ms (DOM), <200ms (API)

6. **User Experience**
   - Unified messaging feels native
   - Version control is intuitive
   - Undo works reliably
   - No noticeable latency

---

## 7. Next Surfaces to Light Up

After completing Phase 3, the following surfaces are ready for implementation:

**1. Calendar Plugin Spec**
- Unified calendar across Outlook + Google Calendar
- Event creation, modification, deletion
- Meeting scheduling with conflict detection
- Cross-calendar availability

**2. Files Plugin Spec**
- Unified file browser across OneDrive + Google Drive + Local FS
- File operations (create, move, delete, share)
- Version control for files
- Cross-storage search

**3. Docs Plugin Spec**
- Unified document editing across Word + Google Docs + Notion
- Real-time collaboration
- Version control for documents
- Cross-platform formatting

**4. Tasks Plugin Spec**
- Unified task management across Planner + Tasks + Todoist
- Task creation, assignment, completion
- Project management
- Cross-platform sync

**5. Intelligence Plugin Spec**
- Unified AI interface across Copilot + ChatGPT + Claude + Gemini
- Multi-agent coordination
- Constitutional governance for AI
- Provenance for AI-generated content

---

## 8. Architectural Principles

These principles guide all Aluminum development:

**1. Kernel First**
- All functionality goes through kernel APIs
- No direct plugin-to-plugin communication
- Kernel enforces constitutional rules

**2. Vendor Neutrality**
- No plugin is favored over another
- All plugins have equal access to kernel
- User chooses default plugins

**3. Provenance Always**
- Every artifact has lineage
- Every action is logged
- Audit trail is immutable

**4. Reversibility When Possible**
- Generate undo handles whenever possible
- Store compensating actions
- Enable safe experimentation

**5. Constitutional Governance**
- User defines rules in natural language
- Policy Kernel enforces rules consistently
- Rules apply to all plugins and agents

**6. Progressive Enhancement**
- Start with basic functionality
- Add advanced features incrementally
- Always maintain backward compatibility

---

## 9. Conclusion

Aluminum v2.1 represents the transition from architectural vision to build-ready implementation. The kernel APIs, plugin architecture, and messaging plugin specification provide a concrete foundation for building the unified intelligence layer.

**The key insight:** Rather than building yet another standalone application, Aluminum establishes a **kernel + plugin architecture** where existing applications become plugins that attach to a unified intelligence substrate. This approach preserves vendor sovereignty while enabling cross-platform coordination, constitutional governance, and universal reversibility.

**The path forward:** Implement the kernel skeleton, stabilize the ChromeOS executor adapter, build the messaging plugins, and add conversational version control. Each step builds on the previous, creating a solid foundation for the complete Aluminum ecosystem.

**The promise:** By the end of Phase 3, users will have a working unified messaging system that demonstrates the power of the Aluminum architecture—one intelligence layer, multiple vendor skins, zero redundancy.

---

**Document Version:** 2.1  
**Date:** February 2, 2026  
**Authors:** Daavud Sheldon, Manus AI, Microsoft Copilot  
**Status:** BUILD-READY - IMPLEMENTATION IN PROGRESS

**Next Steps:**
1. Create todo.md with all Phase 3 tasks
2. Implement kernel skeleton (Week 1-2)
3. Stabilize ChromeOS executor adapter (Week 3-4)
4. Build messaging plugins (Week 5-8)
5. Add conversational version control (Week 9-10)

**Let's build Aluminum.** 🔥🚀⚡
