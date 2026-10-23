---
id: POLICY-agent-access
tags: [type/policy, domain/core]
status: active
risk: critical
created: 2026-10-23
updated: 2026-10-23
author: architect
---

# POLICY: agent-access

## Purpose

Agents may write into a lake, but only under human supervision. Nothing an agent writes becomes law without a human.

## Scope

### In Scope

- Every agent, every lake that extends this one.

### Out of Scope

- Human authors (governed by [[Roles]]).

## Policy Statement

1. Agents write directly **only** to `01_Inbox/agents/`.
2. Every agent-written document has `status: draft` and `author: agent/<name>`.
3. Any change outside `01_Inbox/agents/` is made on a git branch and proposed as a pull request. A human merges.
4. Agents never change `status` to `experimental` or `active`, and never edit `00_Codex/`.
5. Agents never read `01_Inbox/private/`.

## Implementation

### Rules

- [[RULE-CORE-001]]

### Technical Controls

- Codex: [[agent-instructions|Agent Instructions]].
- Planned: MCP Hub RBAC blocks agent writes outside `01_Inbox/agents/`.

## Exceptions

None. `risk: critical` — cannot be overridden by member lakes.

## Related

- [[Roles]] · [[Federation]]

**Up:** [[Statute]]
