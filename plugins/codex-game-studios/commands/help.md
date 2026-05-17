# /help

Analyzes what is done and the users query and offers advice on what to do next. Use if user says what should I do next or what do I do now or I'm stuck or I don't know what to do (source alias: /help).

## Arguments

- `input`: [optional: what you just finished, e.g. 'finished design-review' or 'stuck on ADRs']

## Workflow

1. Use the `$codex-game-studios:help` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/help <task details>
```
