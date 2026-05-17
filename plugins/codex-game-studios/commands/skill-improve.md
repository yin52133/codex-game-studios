# /skill-improve

Improve a skill using a test-fix-retest loop. Runs static checks, proposes targeted fixes, rewrites the skill, re-tests, and keeps or reverts based on score change. (source alias: /skill-improve).

## Arguments

- `input`: [skill-name]

## Workflow

1. Use the `$codex-game-studios:skill-improve` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/skill-improve <task details>
```
