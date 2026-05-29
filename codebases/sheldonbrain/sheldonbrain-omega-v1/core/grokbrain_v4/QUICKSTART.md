---
artifact_id: ARTIFACT-CODEBASES-SHELDONBRAIN-SHELDONBRAIN-OMEGA-V1-CORE-GROKBRAIN-V4-QUICKSTART-MD-2026-05-29
title: 🚀 Grokbrain v4.0 - Quick Start Guide
status: CANDIDATE
owner: atlaslattice
created: 2026-05-29
last_updated: 2026-05-29
source_of_truth: GitHub
---
# 🚀 Grokbrain v4.0 - Quick Start Guide

## 5-Minute Setup

### 1. Install Dependencies
```bash
./setup.sh
# Or manually:
pip install -r requirements.txt
```

### 2. Configure API Keys
```bash
# Get your public IP
curl https://api.ipify.org

# Edit .env
nano .env
```

Add your keys:
```env
XAI_API_KEY=sk-xai-your-key-here
OPENAI_API_KEY=sk-your-openai-key-here  # Optional
ALLOWED_IP=your.public.ip.here
DEV_BYPASS=1  # Set to 0 for production
```

### 3. Test with Sample Data
```bash
python main.py --sample
```

Expected output:
```
🧠 Starting Grokbrain Pipeline...
STEP_1: Quarantine filtering
STEP_2: Artifact creation
STEP_3: Auto-parsing to 144-sphere grid
...
✅ GROKBRAIN V4.0 PIPELINE COMPLETE
📊 Total artifacts: 4
🌐 Items categorized: 8
📁 Projects detected: 4
🔮 Spheres populated: 6/144
```

### 4. View Results
```bash
# View parsed grid
cat parsed/parsed_grids.json | jq .

# View project aggregates
ls parsed/*.json

# View god-specific data
ls parsed/by_god/

# View code spheres
ls parsed/code_spheres/
```

### 5. Launch GUI
```bash
streamlit run app.py
```

Opens at `http://localhost:8501`

---

## Process Your Own Data

### 1. Add Your Chat Exports
```bash
# Place JSON/TXT files in:
./exports/

# Supported formats:
# - {"messages": [{"role": "user", "content": "..."}, ...]}
# - Raw text with Human:/Assistant: markers
```

### 2. Run Full Pipeline
```bash
python main.py --full
```

### 3. Upload to xAI Collections
```bash
python main.py --upload-xai
```

### 4. Query Your Knowledge Base
```bash
python main.py --query "Sheldonium dynamics for Mars ecosuits"
```

---

## Common Commands

```bash
# Sample mode (test)
python main.py --sample

# Full pipeline (process all exports)
python main.py --full

# Upload to xAI
python main.py --upload-xai

# Query with dual AI consensus
python main.py --query "your question"

# Interactive demo (R2D2, C3PO, MarsTerraformer)
python main.py --demo

# Launch web GUI
streamlit run app.py
```

---

## Understanding Output

### parsed_grids.json
```json
[
  [  // Category 0: Natural Sciences
    [  // Subset 0: Physics
      {
        "content": "Input: ... Output: ...",
        "tags": {
          "sphere": "Physics",
          "element": "Hydrogen (1)",
          "god": "Zeus (thunder/energy-H)",
          "sphere_number": 1,
          "numerology_overlays": {...}
        },
        "metadata": {...}
      }
    ],
    [...], // 11 more subsets
  ],
  [...],  // 11 more categories
]
```

### Project Files (e.g., mars_terraforming.json)
```json
{
  "aggregate": {
    "timeline": [
      {
        "content": "...",
        "timestamp": "2024-..."
      }
    ]
  },
  "report": "Aggregated 15 entries...",
  "entry_count": 15,
  "time_range": {
    "start": "2024-01-01...",
    "end": "2024-11-16..."
  }
}
```

### God Forks (e.g., by_god/zeus.json)
```json
[
  {
    "content": "Physics-related conversation...",
    "tags": {
      "god": "Zeus (thunder/energy-H)",
      "sphere": "Physics",
      ...
    }
  },
  ...
]
```

---

## Troubleshooting

### No artifacts created?
- Check files exist in `./exports/`
- Verify JSON format is correct
- Check file permissions

### IP whitelisting error?
```bash
# Get your IP
curl https://api.ipify.org

# Add to .env
echo "ALLOWED_IP=your.ip.here" >> .env

# Or bypass for development
echo "DEV_BYPASS=1" >> .env
```

### xAI API errors?
- Verify `XAI_API_KEY` in `.env`
- Check key permissions at https://x.ai/api
- Note: Some endpoints may not be available yet

### Qdrant errors?
```bash
# Reset vector database
rm -rf qdrant_db/
python main.py --sample
```

---

## Next Steps

1. ✅ Run sample mode
2. ✅ Add your chat exports
3. ✅ Process with `--full`
4. ✅ Explore in GUI
5. ✅ Upload to xAI (optional)
6. ✅ Query your knowledge base

---

## Architecture Overview

```
Chat Exports
    ↓
Quarantine Filter (removes chaos)
    ↓
Artifact Creation (input/output pairs)
    ↓
Qdrant Vector DB (embeddings)
    ↓
144-Sphere Classification
    ↓
├── Project Detection
├── God Fork (phase 1.5)
├── Code Spheres
├── White Paper Spheres
└── Gamma.app Spheres
    ↓
xAI Collections API
    ↓
Dual AI Consensus (Grok + GPT)
```

---

## Security Reminder

🔒 **NEVER** commit:
- `.env` file
- Your chat exports
- API keys
- Processed data with IP

The `.gitignore` is configured to protect you, but always double-check before committing!

---

**Questions?** Check the full [README.md](README.md)

**Ready to build your knowledge empire? Let's go! 🧠**
