---
id: NOTE-CORE-009
tags: [type/convention]
status: active
created: 2026-01-22
updated: 2026-10-23
---

# Naming

## Hub Files

Each folder has a hub named after the folder, never `_INDEX` or `_MoC`:
`00_Codex/Codex.md`, `10_Context/Context.md`, `10_Context/Billing/Billing.md`.
Every document links its hub; every hub links up to [[HOME]].

## Artifact IDs

The `id` in frontmatter is also the filename for formal documents.

| Type | Pattern | Example |
|------|---------|---------|
| Rule | `RULE-{DOMAIN}-{NNN}` | `RULE-CORE-001` |
| Workflow | `WFLOW-{DOMAIN}-{NNN}` | `WFLOW-PY-003` |
| Policy | `POLICY-{name}` | `POLICY-agent-access` |
| Checklist | `CHECK-{name}` | `CHECK-pr-review` |
| Skill | `SKILL-{name}` | `SKILL-code-review` |
| Agent | `AGENT-{name}` | `AGENT-builder` |
| Case | `CASE-{YYYY}-{NNN}` | `CASE-2026-042` |
| ADR | `ADR-{DOMAIN}-{NNN}-{slug}` | `ADR-PY-001-use-uv` |
| Anything else | `NOTE-{DOMAIN}-{NNN}` | `NOTE-PY-017` |

Notes may keep a human filename (`Event loop.md`) as long as the `id` is set.

## Qualified IDs

Across lakes: `{lake-id}:{id}` — e.g. `shepard:POLICY-agent-access`. See [[Federation]].

**Up:** [[Conventions]]
