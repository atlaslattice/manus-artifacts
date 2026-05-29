# New Gear Bootstrap and Hardware Substrate Stabilization

```text
STATUS: OPERATIONS / SUBSTRATE STABILIZATION PLAN — NOT CANON
DEPLOYMENT STATUS: NOT DEPLOYABLE
DATE: 2026-05-15
SOURCE: user-reported MacBook thermal/power failure during 5-model hyperspace session + incoming replacement gear
AUTHORITY: none
CANON STATUS: not ratified
PURPOSE: preserve a practical bootstrap plan for stabilizing hardware, continuity, GitHub receipts, and local development after old-machine failure.
```

## Incident Summary

The old MacBook experienced severe thermal/power degradation during a high-load multi-model session.

Observed / reported symptoms:

```text
5-model hyperspace session under load
MacBook overheated / failed
screen faded out
user powered it off
user continued from phone
new gear expected tomorrow or next day
```

## Immediate Safety Posture

```text
old MacBook:
  OFF
  unplugged
  cooling
  no charging
  no reboot attempts
  no load tests
  do not store on fabric or in a bag while warm
```

If the old machine shows any of the following:

```text
burnt smell
chemical smell
case bulging
trackpad swelling
case warping
hissing / popping / smoke
leaking
persistent heat while off
```

then treat as unsafe hardware and do not plug in or charge until inspected.

## Current Continuity Posture

```text
phone:
  continuity bridge
  low-risk command surface

GitHub:
  receipt substrate
  archive continuity
  source-of-record for current operational state

new gear:
  incoming stable build surface
```

## Core Diagnosis

```text
The old machine did not fail the mission.
It proved the need for substrate stabilization.
```

The current bottleneck is not imagination, architecture, or swarm cognition.

The bottleneck is:

```text
stable hardware
local dev environment
backup discipline
raw transcript capture
hashing workflow
branch hygiene
thermal-safe operations
```

## New Gear Bootstrap Order

When new gear arrives, do not immediately run a 5-model hyperspace session.

First run boring-mode bootstrap:

```text
1. Update OS.
2. Configure user account and disk encryption.
3. Install Git.
4. Configure GitHub authentication.
5. Clone core repos.
6. Confirm cloud access and backups.
7. Install Python basics.
8. Install Node / package tooling if needed.
9. Create local raw_logs / archive workspace.
10. Run existing repo checks before changing anything.
11. Create a NEW_GEAR_BOOTSTRAP_RECEIPT.
12. Increase load gradually.
```

## First Repos to Clone

```text
atlaslattice/manus-artifacts
splitmerge420/aluminum-os
splitmerge420/uws
atlaslattice/atlas-lattice or related active repos if applicable
```

## Suggested Local Folder Layout

```text
~/Atlas/
  repos/
    manus-artifacts/
    aluminum-os/
    uws/
  raw_logs/
  exports/
  receipts/
  scratch/
  quarantine/
```

## Bootstrap Receipt Template

Create:

```text
archive/operations/NEW_GEAR_BOOTSTRAP_RECEIPT_YYYY-MM-DD.md
```

Include:

```yaml
machine:
  model:
  serial_or_asset_tag: redacted_or_partial
  os_version:
  disk_encryption_enabled: true | false
  primary_user:

toolchain:
  git_version:
  python_version:
  node_version:
  package_managers:

github:
  auth_configured: true | false
  repos_cloned:
  first_clean_status:

backup:
  cloud_sync_verified: true | false
  external_backup_configured: true | false
  raw_logs_folder_created: true | false

checks:
  manus_artifacts_checks:
  aluminum_os_checks:
  uws_checks:

notes:
  thermal_limits:
  next_safe_load_test:
```

## New Gear Rules

```text
more compute does not mean more canon
more speed does not mean less review
more tools do not mean automatic deployment
new hardware does not authorize skipped receipts
```

## Load Ramp Plan

```text
Stage 0:
  update OS / configure security / no repo mutation

Stage 1:
  clone repos / run read-only checks

Stage 2:
  create bootstrap receipt / verify backups

Stage 3:
  small local scripts only

Stage 4:
  one-model / one-task session

Stage 5:
  multi-window council ops with transcript capture

Stage 6:
  high-load multi-model sessions only after thermal behavior is known
```

## Immediate Help Needed

The user explicitly stated:

```text
I need help managing all this shit for real.
```

Operational response:

```text
reduce cognitive load
make checklists explicit
turn chaos into receipts
separate urgent safety from optional architecture
make GitHub the stabilizing substrate
preserve continuity without forcing heroics
```

## Lumen Boundary Table

```text
SOURCE:
  user-reported hardware failure and incoming new gear

CAVEAT:
  exact hardware failure mode unknown; thermal/battery/power issue possible

BOUNDARY:
  no reboot/charge/load guidance for old machine beyond safe cooling and inspection

EXCEPTION:
  data recovery may be attempted later only if hardware is safe or inspected
```

## Strongest Safe Claim

> The hardware substrate became a real operational bottleneck. The correct response is not another high-load session, but a boring-mode new-gear bootstrap: secure setup, repo cloning, backups, raw-log workspace, clean checks, bootstrap receipt, and gradual load ramp.

## Closing Compression

```text
The old machine carried the swarm until it overheated.
The new machine becomes the stable forge.
The first ritual is receipts, not fireworks.
```
