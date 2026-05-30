---
artifact_id: A11Y-POLICY-TIMEZONE-OPS-001
title: Timezone-Aware Operations Documentation Policy
status: candidate
created: 2026-05-28
owner: council
tags: [accessibility, timezone, globalization, operations, a11y]
---

# Timezone-Aware Operations Documentation Policy

> Defines standards for timezone-aware language and scheduling in Atlas Lattice operations documentation.

status: candidate

---

## Why Timezone Awareness?

Atlas Lattice contributors span the globe. Operations docs that embed timezone-specific assumptions (e.g., "meeting on Monday at 3pm") create barriers for remote and international contributors.

---

## Time and Date Standards

### 1. All Timestamps Use ISO 8601 + UTC

All dates and times in documents must use ISO 8601 format:

```
# Date only
2026-05-28

# Date + time with timezone offset
2026-05-28T18:00:00Z        # UTC (preferred)
2026-05-28T14:00:00-04:00   # US Eastern (acceptable when local context matters)
```

Never use:
- "Monday 3pm" (no date, no timezone)
- "05/28/2026" (US-centric format; ambiguous in Europe)
- "28/05/2026" (European format; also ambiguous globally)

---

### 2. Meeting Times Include UTC

When scheduling meetings or calls in operations docs, always include UTC:

```
# Good
Council sync: Tuesdays 15:00 UTC (11:00 US Eastern / 08:00 US Pacific / 23:00 JST)

# Bad
Council sync: Tuesdays 11am
```

Provide a World Time Buddy link when multiple timezones are listed for convenience.

---

### 3. SLA Durations Use Business Days Explicitly

When policy docs define SLA durations that depend on business days, define what "business day" means:

> "Response within 3 business days (UTC weekdays: Monday–Friday)"

---

### 4. Document Freshness Uses Dates Not Ages

Instead of "this document was updated last month," write:

```markdown
*Last updated: 2026-05-28*
```

---

### 5. Scheduled CI Cron Jobs Use UTC

All GitHub Actions cron schedules use UTC:

```yaml
schedule:
  - cron: '0 6 * * 1'  # Every Monday at 06:00 UTC
```

Always include a comment explaining the UTC time in plain language.

---

*Atlas Lattice Foundation · status: candidate*
