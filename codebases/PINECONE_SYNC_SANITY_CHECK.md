# Pinecone sync sanity check

## Scope

Applies to:

- `codebases/other/artifact_sync.py`
- `codebases/atlas-lattice/artifact_sync.py`

## Environment-gated behavior

- If `PINECONE_API_KEY` is set, Pinecone sync path is attempted.
- If `PINECONE_API_KEY` is not set, Pinecone sync is skipped with:
  - `{"skipped": true, "reason": "PINECONE_API_KEY not set"}`

## Local sanity commands

```bash
python -m py_compile codebases/other/artifact_sync.py codebases/atlas-lattice/artifact_sync.py
```

Optional runtime smoke check (without secrets):

```bash
python codebases/other/artifact_sync.py --verify
python codebases/atlas-lattice/artifact_sync.py --verify
```
