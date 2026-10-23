---
id: NOTE-CORE-015
tags: [type/convention]
status: active
created: 2026-01-22
updated: 2026-10-23
---

# Metadata

## Required Frontmatter

Every document, no exceptions:

```yaml
---
id: NOTE-PY-001        # unique in the lake, never changes
tags: [type/note]      # at least one type/ tag
status: draft          # draft | experimental | active | deprecated
created: 2026-10-23
updated: 2026-10-23    # bump on every meaningful edit — indexers rely on it
author: architect      # architect | <name> | agent/<name>
---
```

## Optional Fields

| Field | Purpose |
|-------|---------|
| `aliases` | Alternative names for search and linking |
| `source` | Origin: ticket, PR, conversation, URL |
| `scope` | Agents or workflows a rule applies to |
| `priority`, `risk` | Rules and policies |
| `overrides` | Qualified ID this document replaces ([[Federation]]) |
| `llm-ready` | `true` when the note is clean enough for agents to rely on |
| `reviewed-by`, `reviewed-at` | Human review stamp |

Index state (embeddings, weights, links) lives in the Memory Layer, never in frontmatter.

## Tags

| Prefix | Examples |
|--------|----------|
| `nav/` | `nav/home`, `nav/codex` |
| `type/` | `type/rule`, `type/skill`, `type/adr` |
| `domain/` | `domain/core`, `domain/py` |
| `maturity/` | `maturity/seedling`, `maturity/evergreen` |
| `risk/` | `risk/low`, `risk/critical` |

## Status Lifecycle

| Status | Meaning |
|--------|---------|
| `draft` | Work in progress. Not enforced. |
| `experimental` | In testing, only for agents named in `scope`. |
| `active` | **Law.** Enforced. |
| `deprecated` | Obsolete. Kept for history, never deleted. |

**Up:** [[Conventions]]
