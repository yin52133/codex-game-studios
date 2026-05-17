# /test-setup

Scaffold the test framework and CI/CD pipeline for the project's engine. Creates the tests/ directory structure, engine-specific test runner configuration, and GitHub Actions workflow. Run once during Technical Setup phase before the first sprint begins. (source alias: /test-setup).

## Arguments

- `input`: [force]

## Workflow

1. Use the `$codex-game-studios:test-setup` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/test-setup <task details>
```
