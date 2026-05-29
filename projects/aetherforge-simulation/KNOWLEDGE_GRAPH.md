# Aetherforge Simulation Knowledge Graph

This document maps the simulation sandbox as a knowledge graph. It is practical infrastructure, not a canon document.

## Graph thesis

The lattice is represented as a graph of typed nodes and typed edges:

- repository nodes describe files and workflows
- domain nodes describe the 12 balanced work domains
- task nodes describe the 144 candidate tasks
- command nodes describe executable validation and simulation commands
- receipt nodes describe deterministic simulation evidence
- boundary nodes describe constraints that prevent drift

## Node classes

| Class | Prefix | Source |
|---|---:|---|
| Project | `project:` | Sandbox README |
| File | `file:` | Repository paths |
| Domain | `domain:` | `task-matrix-12x12.json` |
| Task | `task:` | Expanded matrix task IDs |
| Command | `cmd:` | CLI commands |
| Test | `test:` | Pytest names |
| Boundary | `boundary:` | Matrix boundary block |
| Receipt | `receipt:` | Simulation output |

## Edge classes

| Edge | Meaning |
|---|---|
| `contains` | parent contains child |
| `defines` | file defines object |
| `validates` | test or command validates object |
| `generates` | command generates output |
| `constrains` | boundary limits object |
| `documents` | file documents object |
| `emits` | simulator emits receipt or metric |
| `maps_to` | object maps to related object |

## Core graph spine

```text
project:aetherforge-simulation
  contains file:README.md
  contains file:task-matrix-12x12.json
  contains file:aetherforge_sim.py
  contains file:tests/test_aetherforge_sim.py
  contains file:pyproject.toml
  contains file:.github/workflows/aetherforge-simulation.yml

file:task-matrix-12x12.json
  defines 12 domain nodes
  defines 144 task nodes
  constrained_by boundary:non_canon_simulation

file:aetherforge_sim.py
  expands file:task-matrix-12x12.json
  validates domain/task balance
  generates receipt chain
  emits matrix fingerprint
  emits receipt head

file:tests/test_aetherforge_sim.py
  validates matrix shape
  validates task ID stability
  validates deterministic replay
  validates receipt linkage
  validates CLI JSON behavior
```

## Boundary map

```text
boundary:non_canon_simulation
  constrains project:aetherforge-simulation
  constrains all domain:* nodes
  constrains all task:* nodes
  constrains cmd:simulate
```

## Execution map

```bash
python -m aetherforge_sim validate
python -m aetherforge_sim matrix
python -m aetherforge_sim --json simulate --steps 12 --seed 144
pytest
```

## Generated graph artifact

Run this to export machine-readable nodes and edges:

```bash
python graph_export.py --json > lattice-graph.generated.json
```
