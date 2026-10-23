---
id: NOTE-CORE-016
tags: [type/convention]
status: active
created: 2026-01-22
updated: 2026-10-24
---

# Visuals

Graph view colors by risk, status and type. Shipped in `.obsidian/graph.json`.

| Query | Color | Meaning |
|-------|-------|---------|
| `tag:#risk/critical` | 🔴 red | Critical risk |
| `[status:deprecated]` | ⚪ gray | Obsolete, kept for history |
| `[status:draft] -path:99_Templates` | 🟡 yellow | Waiting for review |
| `path:00_Codex` | 🟠 orange | Constitution |
| `tag:#type/rule` | 🔵 blue | Rules |
| `tag:#type/skill` | 🟣 purple | Skills |
| `tag:#type/context` | 🟢 green | Context |

The first matching group wins, so the order above is the priority.

Members may add per-domain colors (`tag:#domain/py`) in their own vault.

**Up:** [[Conventions]]
