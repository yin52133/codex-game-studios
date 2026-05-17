# /dev-story

Read a story file and implement it. Loads the full context (story, GDD requirement, ADR guidelines, control manifest), routes to the right programmer agent for the system and engine, implements the code and test, and confirms each acceptance criterion. The core implementation skill — run after /story-readiness, before /code-review and /story-done. (source alias: /dev-story).

## Arguments

- `input`: [story-path]

## Workflow

1. Use the `$codex-game-studios:dev-story` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/dev-story <task details>
```
