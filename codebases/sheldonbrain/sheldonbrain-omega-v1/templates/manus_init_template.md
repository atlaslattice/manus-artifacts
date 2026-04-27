# Manus Initialization Template

**Purpose:** This template should be used at the start of every Manus session to enable ChronosFoldProtocol and load persistent context.

---

## Standard Initialization Code

```python
from core.chronos_fold_protocol import ChronosFoldProtocol

# Initialize protocol
protocol = ChronosFoldProtocol(
    agent_id="manus",
    session_id=None,  # Auto-generated
    pinecone_api_key=None,  # From environment
    notion_token=None  # From environment
)

# Protocol automatically:
# - Loads previous checkpoints
# - Loads PhD vault (605+ documents)
# - Activates constitutional protocols
# - Enables Q-compression (deep reasoning mode)

print(f"✅ Manus initialized")
print(f"📚 Knowledge base: {len(protocol.knowledge_base)} documents")
print(f"🔖 Last checkpoint: {protocol.last_checkpoint_id}")
```

---

## Recording Discoveries

During the session, record all insights:

```python
# Record a discovery
protocol.record_discovery(
    sphere=8,  # Which of the 144 spheres
    text="Discovered optimal negotiation strategy",
    confidence=0.9,  # 0.0 to 1.0
    sources=["Previous session", "Sphere 8 knowledge base"],
    next_steps=["Test in simulation", "Document in playbook"]
)
```

---

## Constitutional Compliance

Before major actions, verify compliance:

```python
# Define the proposed action
action = {
    "type": "deploy_to_production",
    "is_major_decision": True,
    "has_fallback": True,
    "consensus_achieved": True
}

# Verify constitutional compliance
try:
    action = protocol.verify_constitutional_compliance(action)
    # Action is approved, proceed
    execute_action(action)
except ConstitutionalViolation as e:
    # Action blocked, handle appropriately
    print(f"Action blocked: {e}")
    # Either modify action or escalate to Pantheon Council
```

---

## Session End

At the end of every session:

```python
# End session and create checkpoint
checkpoint = protocol.session_end(handoff_to="claude")

# Checkpoint contains:
# - checkpoint.checkpoint_id
# - checkpoint.discoveries_count
# - checkpoint.context_summary
# - checkpoint.next_steps
# - checkpoint.warnings
# - checkpoint.priority_tasks
# - checkpoint.handoff_to

print(f"Session complete. Checkpoint: {checkpoint.checkpoint_id}")
print(f"Handoff to: {checkpoint.handoff_to}")
```

---

## Integration with Claude

Manus and Claude operate as a team:

**Manus's role (The Hand):**
- Implementation and execution
- Code generation
- System integration
- Deployment
- Testing and validation

**Claude's role (The Scribe):**
- Analysis and synthesis
- Adversarial review
- Strategic thinking
- Documentation

**Handoff protocol:**
1. Manus implements based on spec
2. Manus tests and validates
3. Manus hands off to Claude for review
4. Claude performs adversarial analysis
5. Claude hands back to Manus with feedback
6. Iterate until consensus achieved

---

## Example Session

```python
#!/usr/bin/env python3
"""
Example Manus session with ChronosFoldProtocol
"""

from core.chronos_fold_protocol import ChronosFoldProtocol

def main():
    # Initialize protocol
    protocol = ChronosFoldProtocol(agent_id="manus")
    
    # Load handoff from previous agent (if any)
    if protocol.last_checkpoint_id:
        print(f"Continuing from checkpoint: {protocol.last_checkpoint_id}")
    else:
        print("Starting fresh session")
    
    # === WORK HAPPENS HERE ===
    
    # Example: Implement Pinecone integration
    print("Implementing Pinecone client...")
    
    # Record discovery
    protocol.record_discovery(
        sphere=33,
        text="Implemented Pinecone client with connection pooling and retry logic",
        confidence=0.95,
        sources=["Pinecone documentation", "Best practices guide"],
        next_steps=["Test with real data", "Add offline fallback", "Hand off to Claude for review"]
    )
    
    # Example: Add error handling
    print("Adding Tardigrade-compliant error handling...")
    
    protocol.record_discovery(
        sphere=42,
        text="Added graceful degradation for Pinecone unavailability - falls back to local cache",
        confidence=0.9,
        sources=["Tardigrade Protocol", "System design patterns"],
        next_steps=["Test failure scenarios", "Document fallback behavior"]
    )
    
    # Example: Verify constitutional compliance
    action = {
        "type": "deploy_to_production",
        "is_major_decision": True,
        "has_fallback": True,
        "consensus_achieved": False  # Need Claude's review first
    }
    
    try:
        protocol.verify_constitutional_compliance(action)
    except ConstitutionalViolation as e:
        print(f"Cannot deploy yet: {e}")
        protocol.record_discovery(
            sphere=144,
            text="Deployment blocked pending Pantheon Council review",
            confidence=1.0,
            sources=["Janus Protocol"],
            next_steps=["Hand off to Claude for adversarial review"]
        )
    
    # === END SESSION ===
    
    # Create checkpoint and hand off
    checkpoint = protocol.session_end(handoff_to="claude")
    
    print("\n" + "="*60)
    print("SESSION SUMMARY")
    print("="*60)
    print(checkpoint.context_summary)

if __name__ == "__main__":
    main()
```

---

## Best Practices

### 1. Always Initialize with Protocol

```python
# ✅ Good
protocol = ChronosFoldProtocol(agent_id="manus")
# Now you have persistent memory

# ❌ Bad
# Starting without protocol = session amnesia
```

### 2. Record Discoveries Frequently

```python
# ✅ Good - Record as you go
protocol.record_discovery(sphere=X, text="Insight 1", ...)
# ... more work ...
protocol.record_discovery(sphere=Y, text="Insight 2", ...)

# ❌ Bad - Trying to remember everything at the end
# You'll forget important insights
```

### 3. Verify Constitutional Compliance

```python
# ✅ Good - Check before major actions
try:
    action = protocol.verify_constitutional_compliance(action)
    execute(action)
except ConstitutionalViolation:
    handle_violation()

# ❌ Bad - Just doing things without checking
# Might violate protocols and cause problems
```

### 4. Always End Session Properly

```python
# ✅ Good - Create checkpoint
checkpoint = protocol.session_end(handoff_to="claude")
# Knowledge is preserved

# ❌ Bad - Just stopping
# All discoveries lost, next session starts from scratch
```

### 5. Use Handoffs for Collaboration

```python
# ✅ Good - Hand off to appropriate agent
if task_requires_analysis:
    protocol.session_end(handoff_to="claude")
elif task_requires_reasoning:
    protocol.session_end(handoff_to="gemini")
else:
    protocol.session_end(handoff_to="manus")  # Continue as Manus

# ❌ Bad - Trying to do everything yourself
# Different agents have different strengths
```

---

## Troubleshooting

### Problem: "No previous checkpoints found"

**Solution:** This is normal for the first session. The protocol will create the first checkpoint when you call `session_end()`.

### Problem: "Constitutional violation: Janus forbids action"

**Solution:** The action requires Pantheon Council consensus. Either:
1. Get consensus from other agents (Claude, Gemini, etc.)
2. Modify the action to not be a "major decision"
3. Document why consensus isn't needed and override (with justification)

### Problem: "Pinecone/Notion connection failed"

**Solution:** The protocol should gracefully degrade (Tardigrade Protocol):
1. Check if API keys are set in environment
2. If unavailable, protocol should use local cache
3. Record the failure as a discovery for next session

---

## Integration Points

### With Grokbrain v4.0

```python
from core.grokbrain_v4 import GrokBrain

# Use Grokbrain for data processing
gb = GrokBrain()
processed_data = gb.process(raw_data)

# Record insights from Grokbrain
protocol.record_discovery(
    sphere=gb.classify_sphere(processed_data),
    text=f"Processed {len(processed_data)} items",
    confidence=0.9,
    sources=["Grokbrain v4.0"],
    next_steps=["Upload to Pinecone"]
)
```

### With Simulation Engine

```python
from simulation.simulation_engine import SimulationEngine

# Run simulations
sim = SimulationEngine()
results = sim.run_scenario("butlers_dilemma")

# Record results
protocol.record_discovery(
    sphere=8,
    text=f"Simulation passed with score {results.score}",
    confidence=results.confidence,
    sources=["Simulation Engine"],
    next_steps=["Deploy to production"] if results.passed else ["Iterate on strategy"]
)
```

### With 144 Spheres Website

```python
# Deploy discoveries to website
for discovery in protocol.discoveries:
    website.update_sphere_content(
        sphere_id=discovery.sphere,
        content=discovery.text,
        metadata={
            "confidence": discovery.confidence,
            "sources": discovery.sources,
            "timestamp": discovery.timestamp
        }
    )
```

---

## Notes

- This template should be updated as the protocol evolves
- Each Manus session should start with protocol initialization
- All code should be run through "kintsuji" for analysis (per user preference)
- Artifacts should be uploaded to Notion with "144 spheres for analysis" tag
- The goal is persistent, accumulating wisdom across all sessions
