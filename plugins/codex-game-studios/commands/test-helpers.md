# /test-helpers

Generate engine-specific test helper libraries for the project's test suite. Reads existing test patterns and produces tests/helpers/ with assertion utilities, factory functions, and mock objects tailored to the project's systems. Reduces boilerplate in new test files. (source alias: /test-helpers).

## Arguments

- `input`: [system-name | all | scaffold]

## Workflow

1. Use the `$codex-game-studios:test-helpers` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/test-helpers <task details>
```
