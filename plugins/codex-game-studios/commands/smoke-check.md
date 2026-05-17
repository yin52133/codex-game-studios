# /smoke-check

Run the critical path smoke test gate before QA hand-off. Executes the automated test suite, verifies core functionality, and produces a PASS/FAIL report. Run after a sprint's stories are implemented and before manual QA begins. A failed smoke check means the build is not ready for QA. (source alias: /smoke-check).

## Arguments

- `input`: [sprint | quick | --platform pc|console|mobile|all]

## Workflow

1. Use the `$codex-game-studios:smoke-check` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/smoke-check <task details>
```
