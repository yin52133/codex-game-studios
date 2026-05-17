# /setup-engine

Configure the project's game engine and version. Pins the engine in AGENTS.md, detects knowledge gaps, and populates engine reference docs via WebSearch when the version is beyond the LLM's training data. (source alias: /setup-engine).

## Arguments

- `input`: [engine] | [engine version] | refresh | upgrade [old-version] [new-version] | no args for guided selection

## Workflow

1. Use the `$codex-game-studios:setup-engine` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/setup-engine <task details>
```
