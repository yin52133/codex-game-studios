# /regression-suite

Map test coverage to GDD critical paths, identify fixed bugs without regression tests, flag coverage drift from new features, and maintain tests/regression-suite.md. Run after implementing a bug fix or before a release gate. (source alias: /regression-suite).

## Arguments

- `input`: [update | audit | report]

## Workflow

1. Use the `$codex-game-studios:regression-suite` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/regression-suite <task details>
```
