# /qa-plan

Generate a QA test plan for a sprint or feature. Reads GDDs and story files, classifies stories by test type (Logic/Integration/Visual/UI), and produces a structured test plan covering automated tests required, manual test cases, smoke test scope, and playtest sign-off requirements. Run before sprint begins or when starting a major feature. (source alias: /qa-plan).

## Arguments

- `input`: [sprint | feature: system-name | story: path]

## Workflow

1. Use the `$codex-game-studios:qa-plan` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/qa-plan <task details>
```
