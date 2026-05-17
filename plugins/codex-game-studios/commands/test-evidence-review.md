# /test-evidence-review

Quality review of test files and manual evidence documents. Goes beyond existence checks — evaluates assertion coverage, edge case handling, naming conventions, and evidence completeness. Produces ADEQUATE/INCOMPLETE/MISSING verdict per story. Run before QA sign-off or on demand. (source alias: /test-evidence-review).

## Arguments

- `input`: [story-path | sprint | system-name]

## Workflow

1. Use the `$codex-game-studios:test-evidence-review` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/test-evidence-review <task details>
```
