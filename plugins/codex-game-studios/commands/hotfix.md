# /hotfix

Emergency fix workflow that bypasses normal sprint processes with a full audit trail. Creates hotfix branch, tracks approvals, and ensures the fix is backported correctly. (source alias: /hotfix).

## Arguments

- `input`: [bug-id or description]

## Workflow

1. Use the `$codex-game-studios:hotfix` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/hotfix <task details>
```
