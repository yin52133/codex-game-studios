# /story-readiness

Validate that a story file is implementation-ready. Checks for embedded GDD requirements, ADR references, engine notes, clear acceptance criteria, and no open design questions. Produces READY / NEEDS WORK / BLOCKED verdict with specific gaps. Use when user says 'is this story ready', 'can I start on this story', 'is story X ready to implement'. (source alias: /story-readiness).

## Arguments

- `input`: [story-file-path or 'all' or 'sprint']

## Workflow

1. Use the `$codex-game-studios:story-readiness` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/story-readiness <task details>
```
