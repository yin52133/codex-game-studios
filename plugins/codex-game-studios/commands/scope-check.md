# /scope-check

Analyze a feature or sprint for scope creep by comparing current scope against the original plan. Flags additions, quantifies bloat, and recommends cuts. Use when user says 'any scope creep', 'scope review', 'are we staying in scope'. (source alias: /scope-check).

## Arguments

- `input`: [feature-name or sprint-N]

## Workflow

1. Use the `$codex-game-studios:scope-check` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/scope-check <task details>
```
