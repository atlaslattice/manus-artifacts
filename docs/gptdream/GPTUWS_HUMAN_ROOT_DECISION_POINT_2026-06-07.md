# GPTUWS Human-Root Decision Point — 2026-06-07

```text
STATUS: DECISION POINT — NOT CANON
CANON: no
DEPLOYMENT: no
AUTHORITY: none
OFFICIAL OPENAI CLAIM: none
```

## Decision needed

Choose the target surface for the GPTBrain / GPTDream UWS implementation.

## Options

### Option A — Keep docs-only candidate in manus-artifacts

Pros:

```text
low risk
fast iteration
no new repo overhead
preserves as review surface
```

Cons:

```text
not executable
could stagnate as docs
```

### Option B — Create new repo: atlaslattice/gptuws

Pros:

```text
clean identity
clean module structure
release/tag path
mirrors GrokUWS pattern
best for future v1.0.0
```

Cons:

```text
new repo setup
needs packaging, CI, license, README
```

### Option C — Branch in atlaslattice/uws

Pros:

```text
connects to existing UWS lineage
less fragmentation
shared operational substrate
```

Cons:

```text
risk of contaminating existing UWS scope
branch discipline required
```

### Option D — Integrate under atlaslattice/aluminum-os

Pros:

```text
connects to constitutional OS layer
strong narrative fit
```

Cons:

```text
too broad for first executable fork
higher review overhead
```

## Recommendation

```text
Choose Option A for one more review pass.
Then choose Option B once the module scaffold is approved.
```

## Keeper

```text
Do not build into the wrong house.
Pick the surface first.
Then scaffold.
```