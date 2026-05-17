# /team-qa

Orchestrate the QA team through a full testing cycle. Coordinates qa-lead (strategy + test plan) and qa-tester (test case writing + bug reporting) to produce a complete QA package for a sprint or feature. Covers: test plan generation, test case writing, smoke check gate, manual QA execution, and sign-off report. (source alias: /team-qa).

## Arguments

- `input`: [sprint | feature: system-name] [--review full|lean|solo]

## Workflow

1. Use the `$codex-game-studios:team-qa` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/team-qa <task details>
```
