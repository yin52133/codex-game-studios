# /changelog

Auto-generates a changelog from git commits, sprint data, and design documents. Produces both internal and player-facing versions. (source alias: /changelog).

## Arguments

- `input`: [version|sprint-number]

## Workflow

1. Use the `$codex-game-studios:changelog` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/changelog <task details>
```
