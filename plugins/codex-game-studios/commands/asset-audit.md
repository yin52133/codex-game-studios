# /asset-audit

Audits game assets for compliance with naming conventions, file size budgets, format standards, and pipeline requirements. Identifies orphaned assets, missing references, and standard violations. (source alias: /asset-audit).

## Arguments

- `input`: [category|all]

## Workflow

1. Use the `$codex-game-studios:asset-audit` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/asset-audit <task details>
```
