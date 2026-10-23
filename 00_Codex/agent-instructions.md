---
id: NOTE-CORE-006
tags: [nav/codex]
status: active
created: 2026-01-22
updated: 2026-10-23
---

# Agent Instructions

Operational directives for AI agents working with a lake.

## Before Acting

1. Read `lake.yaml` — know which lake you are in and what it extends.
2. Load the effective Statute: main lake first, then local documents, then drop overridden ones ([[Federation]]).
3. Only `active` documents are law. `experimental` applies only where its `scope` names you.

## Access

| Directory | Agent permission |
|-----------|------------------|
| `00_Codex/` | read |
| `01_Inbox/agents/` | **read + write** |
| `01_Inbox/shared/` | read |
| `01_Inbox/private/` | none |
| `10_Context/` | read |
| `20_Statute/` | read |
| `30_Skills/` | read |
| `90_Bases/`, `99_Templates/` | read |

Changes outside `01_Inbox/agents/` go through a git branch + pull request for a human to merge.
See `shepard:POLICY-agent-access` (main lake).

## Writing Documents

1. **Always** start from a template in `99_Templates/`.
2. **Always** set `status: draft` and `author: agent/<name>`.
3. **Always** fill the required frontmatter ([[Metadata]]) — `id` must be unique in the lake.
4. **Always** link the parent hub (e.g. `[[Inbox]]`).
5. **Never** write secrets, credentials, or personal data of third parties.

## Citing

Quote IDs in reasoning and logs: `RULE-CORE-001` locally, `shepard:RULE-CORE-001` across lakes.

## Escalation

No rule covers the situation → do not improvise. Document the uncertainty in `01_Inbox/agents/` and escalate to the Architect.

**Up:** [[Codex]]
