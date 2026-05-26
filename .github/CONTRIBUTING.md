# Contributing to manus-artifacts

## Canon Boundary Rules

**GitHub is the durable canonical substrate.** Google Drive and Notion are
relay/working-vault layers — not authority sources. Always commit to GitHub
first; downstream sync to Drive/Notion follows.

## Before You Change Anything

1. Read the master brain map: [`archive/boot/COUNCIL_BRAIN_INDEX.md`](../archive/boot/COUNCIL_BRAIN_INDEX.md)
2. Read the relevant seat spec in [`archive/boot/seats/`](../archive/boot/seats/)
3. For swarm-brain assignments check: [`archive/boot/gptbrain/agents/CHILDREN_OF_THE_SWARM_SQUAD_INDEX_2026-05-10.md`](../archive/boot/gptbrain/agents/CHILDREN_OF_THE_SWARM_SQUAD_INDEX_2026-05-10.md)
4. For TIDELOCKBrain (S7) changes read: [`archive/boot/gptbrain/TIDELOCKBrain/README.md`](../archive/boot/gptbrain/TIDELOCKBrain/README.md)
5. For REM-8 / dream-protocol changes read: [`archive/boot/gptbrain/REM8_DREAM_PROTOCOL.md`](../archive/boot/gptbrain/REM8_DREAM_PROTOCOL.md)

## Local Validation

Run these before pushing if you touched `archive/boot/gptbrain/**`:

```bash
cd archive/boot/gptbrain/reference_impl
python -m pytest -q
bash run_checks.sh
```

Validate workflow YAML locally:

```bash
python - <<'EOF'
import yaml, pathlib, sys
errors = []
for f in pathlib.Path(".github/workflows").glob("*.yml"):
    try:
        yaml.safe_load(f.read_text())
    except yaml.YAMLError as e:
        errors.append(f"{f}: {e}")
if errors:
    [print(f"ERROR: {e}", file=sys.stderr) for e in errors]
    sys.exit(1)
print("All workflow files are valid YAML.")
EOF
```

## Pull Request Checklist

- [ ] No merge-conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) in committed files
- [ ] No secrets, credentials, or API keys committed
- [ ] Workflow YAML files pass the syntax check above
- [ ] Changes to `archive/` are **additive only** — never delete canon documents
- [ ] GPTBrain checks pass if `archive/boot/gptbrain/**` was modified
- [ ] Tucker/Gemini adapter remains `REPO_TRACE_ONLY, DRY_RUN_ONLY` unless explicitly promoted
