# /content-audit

Audit GDD-specified content counts against implemented content. Identifies what's planned vs built. (source alias: /content-audit).

## Arguments

- `input`: [system-name | --summary | (no arg = full audit)]

## Workflow

1. Use the `$codex-game-studios:content-audit` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/content-audit <task details>
```
