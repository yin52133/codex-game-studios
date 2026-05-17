# /milestone-review

Generates a comprehensive milestone progress review including feature completeness, quality metrics, risk assessment, and go/no-go recommendation. Use at milestone checkpoints or when evaluating readiness for a milestone deadline. (source alias: /milestone-review).

## Arguments

- `input`: [milestone-name|current] [--review full|lean|solo]

## Workflow

1. Use the `$codex-game-studios:milestone-review` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/milestone-review <task details>
```
