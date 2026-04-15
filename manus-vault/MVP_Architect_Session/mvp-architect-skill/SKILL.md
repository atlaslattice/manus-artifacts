---
name: mvp-architect
description: Strategic MVP design and killer feature identification for cross-platform consensus. Use when reviewing technical specifications, designing MVPs for multi-stakeholder buy-in (especially Microsoft/Google/Apple), identifying politically neutral features, or proposing platform-agnostic architectures.
license: Complete terms in LICENSE.txt
---

# MVP Architect

This skill provides a systematic workflow for analyzing technical specifications and designing Minimum Viable Products (MVPs) that achieve cross-platform consensus among major tech ecosystems.

## When to Use This Skill

Use this skill when:
- Reviewing technical specifications or project requirements from a strategic perspective
- Designing MVPs that need buy-in from multiple competing platforms (Microsoft, Google, Apple)
- Identifying "killer features" that provide universal value without threatening any single ecosystem
- Proposing platform-agnostic architectures that make all platforms more valuable
- De-scoping features that appear proprietary or controlling

## Core Principles

### The Switzerland Strategy

The goal is to become the **neutral intermediary** that connects walled gardens without competing with them. Think of it as becoming "digital Switzerland" - indispensable, trusted, and non-threatening to all parties.

**Key characteristics of neutral MVPs:**
- Solve problems none of the platforms can solve alone without appearing anti-competitive
- Make every platform MORE valuable by connecting them to others
- Use open standards and platform-agnostic protocols
- Demonstrate clear technical achievement that commands respect
- Avoid imposing proprietary protocols or control mechanisms

### Political Neutrality Test

Before including any feature in an MVP, ask:
1. Does this favor one ecosystem over others?
2. Does this threaten any platform's control of their ecosystem?
3. Does this require proprietary standards or protocols?
4. Could this be perceived as competitive rather than complementary?

If the answer to any question is "yes," the feature should be de-scoped or redesigned.

## The MVP Architect Workflow

### Phase 1: Analyze the Original Specification

Read the technical specification thoroughly and identify:
- **Core components** and their priorities
- **Dependencies** (existing systems, APIs, databases, ontologies)
- **Timeline** and resource constraints
- **Stated goals** and success metrics
- **Unstated assumptions** about platform relationships

Create a summary table of all components with their complexity and dependencies.

### Phase 2: Identify the Killer Feature

The killer feature must satisfy ALL of these criteria:
1. **Universal Problem**: Solves a pain point experienced by users across all platforms
2. **Politically Neutral**: Makes every platform more valuable without threatening control
3. **Technically Impressive**: Demonstrates significant engineering achievement
4. **Powerful Demo**: Can be shown in a compelling, easy-to-understand demonstration
5. **Clear Value Proposition**: Benefits are immediately obvious to all stakeholders

**Common killer feature patterns:**
- **Cross-device continuity**: Seamless state handoff between different ecosystems
- **Universal interoperability**: Data/workflow portability across platforms
- **Neutral orchestration**: Coordination layer that doesn't favor any platform
- **Open standards implementation**: Reference implementation of emerging standards

### Phase 3: Design the MVP Scope

Create a focused scope using this framework:

| Component | MVP Status | Justification |
| :--- | :--- | :--- |
| [Component Name] | IN SCOPE / DE-SCOPED | [Why it's essential or why it should wait] |

**De-scoping guidelines:**
- Remove features that impose proprietary protocols
- Defer complex multi-agent or AI routing systems
- Postpone features that require undefined dependencies
- Eliminate anything that could be seen as "taking control"

**In-scope guidelines:**
- Focus on the killer feature and its core engine
- Include a clean, well-documented SDK in multiple languages
- Provide proof-of-concept demo applications
- Ensure cross-platform compatibility from day one

### Phase 4: Assess Timeline Feasibility

Re-evaluate the timeline based on the focused MVP scope:
- Identify dependencies that could block progress
- Flag overly optimistic estimates
- Suggest phased delivery if timeline is unrealistic
- Propose specific milestones with concrete deliverables

### Phase 5: Create the Strategic Proposal

Write a comprehensive proposal document that includes:

1. **Strategic Goal**: Frame the MVP as achieving neutrality and consensus
2. **The Killer Feature**: Name it, describe it, explain why it wins consensus
3. **MVP Scope Table**: Clear IN SCOPE / DE-SCOPED breakdown with justifications
4. **Feasibility Assessment**: Timeline, dependencies, and risk analysis
5. **Demo Strategy**: How to present this to the major platforms
6. **Next Steps**: Concrete actions to begin development

## Output Format

Create a professional markdown document with:
- Clear section headings using the Phase 5 structure
- Tables for component analysis and scope decisions
- Blockquotes for key strategic principles
- Professional, academic writing style
- Specific, actionable recommendations

## Example Application

**Input**: A specification for a "Notion AI Kernel Integration" with protocol enforcement, cross-device continuity, sphere routing, and unified SDK.

**Output**: 
- **Killer Feature**: "Continuity Bridge" - platform-agnostic cross-device state handoff
- **De-scoped**: Protocol enforcement (too controlling), Sphere router (too proprietary)
- **In-scope**: Continuity engine + SDK
- **Justification**: Makes all platforms more valuable by connecting them, politically neutral, powerful demo potential

## Key Success Metrics

A successful MVP proposal should:
- Reduce scope by 40-60% while increasing strategic value
- Identify a single killer feature that all parties want
- Eliminate political friction points
- Provide a realistic timeline with concrete milestones
- Create excitement about the demo potential
