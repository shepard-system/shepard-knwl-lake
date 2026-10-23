---
id: RULE-CORE-001
tags: [type/rule, domain/core]
status: active
scope: [all]
priority: high
risk: critical
created: 2026-10-23
updated: 2026-10-23
author: architect
aliases: [No secrets]
---

# RULE: RULE-CORE-001

## Trigger

Any human or agent writes or edits a document in any lake.

## Instruction

Never put secrets in a lake: passwords, API keys, tokens, private keys, connection strings with credentials. Reference where the secret lives (secret manager key, env var name) instead.

## Examples

### ✅ Good

- `Connection: env PG_DSN (see secrets manager key db/prod)`

### ❌ Bad

- `postgres://admin:hunter2@db.internal:5432/app`

## Violation Handling

- Severity: critical
- Action: block — remove the secret, rotate it, add a Case.

## Related

- Policies: [[POLICY-agent-access]]

**Up:** [[Statute]]
