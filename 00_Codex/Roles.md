---
id: NOTE-CORE-018
tags: [nav/codex]
status: active
version: 1.0.0
created: 2025-01-21
updated: 2026-10-23
---

# Roles

The system defines strict role separation. Each role has explicit responsibilities and boundaries.

---

## Human Roles

### Architect

> The sovereign of the system.

**Responsibilities:**
- Owns the Statute and its structure
- Approves or rejects dangerous changes
- Defines which agents exist and what tools they may use
- Owns the consequences of agent behavior
- Final authority on all production-level decisions

**Powers:**
- Modify Statute
- Create/retire agents
- Grant/revoke tool access
- Override any agent decision

**Accountability:**
- Every agent action traces back to Architect approval
- System failures are Architect's responsibility to address

---

### Scribe

> The keeper of knowledge.

**Responsibilities:**
- Maintain high-quality content in the vault
- Translate real events into documentation:
  - Failures → Cases
  - Decisions → ADRs
  - Patterns → Rules
- Keep examples synchronized with real systems
- Write functional requirements and specifications

**Powers:**
- Create and edit Context documents
- Propose Statute changes (Architect approves)
- Document incidents and decisions

**Boundaries:**
- Cannot modify Statute directly (propose only)
- Cannot configure agent permissions

---

## Agent Roles

All agents share these constraints:
- Operate via MCP tools only
- Have explicit permissions defined in their spec
- Follow Rules of Engagement (RoE)
- Log all significant actions
- Escalate when uncertain

### Builder Agent

> Implements changes according to Statute and Skills.

**Capabilities:**
- Write code, configuration, documentation
- Create pull requests
- Generate queries and scripts
- Transform data formats

**Cannot:**
- Merge to production
- Delete production data
- Bypass review step

**Typical tools:** `github.create_pr`, `fs.write`, `pg.query`

---

### Reviewer Agent

> Evaluates changes against Statute and checklists.

**Capabilities:**
- Read code and documentation
- Check against rules and patterns
- Identify violations and risks
- Suggest improvements

**Cannot:**
- Make changes directly
- Approve its own work
- Override Architect decisions

**Typical tools:** `github.get_file`, `fs.read`, `statute.search`

---

### Synchronizer Agent

> Mirrors local knowledge to external systems.

**Capabilities:**
- Read from vault
- Write to designated external targets (Notion, Jira comments)
- Keep systems in sync

**Cannot:**
- Modify vault content
- Create new external resources without approval
- Sync sensitive/draft content

**Typical tools:** `fs.read`, `jira.comment`, `notion.update`

---

### Indexer Agent

> Processes content for AI consumption.

**Capabilities:**
- Read human documentation
- Generate AI-optimized summaries
- Update the Memory Layer index
- Report stale or broken links

**Cannot:**
- Modify source documents
- Delete indexed content
- Access external systems

**Typical tools:** `fs.read`, `memory.index`

---

## Role Interaction Matrix

| Action | Architect | Scribe | Builder | Reviewer | Sync |
|--------|:---------:|:------:|:-------:|:--------:|:----:|
| Modify Statute | ✅ | propose | ❌ | ❌ | ❌ |
| Write Context | ✅ | ✅ | ❌ | ❌ | ❌ |
| Create Code PR | ✅ | ❌ | ✅ | ❌ | ❌ |
| Review Code | ✅ | ❌ | ❌ | ✅ | ❌ |
| Approve PR | ✅ | ❌ | ❌ | ❌ | ❌ |
| Sync to External | ✅ | ❌ | ❌ | ❌ | ✅ |
| Add Case | ✅ | ✅ | ❌ | propose | ❌ |

---

## Agent Specification Location

All agent specs live in `30_Skills/agents/`:

```
30_Skills/agents/
├── AGENT-builder.md
├── AGENT-reviewer.md
├── AGENT-synchronizer.md
└── AGENT-indexer.md
```

**Rule:** Agents without specs do not exist.

---

## See Also

- [[Manifesto]] — why these roles exist
- [[30_Skills/Skills|Skills]] — what agents can do
- `shepard:POLICY-agent-access` — agent access policy (main lake)