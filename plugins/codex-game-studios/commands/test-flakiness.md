# /test-flakiness

Detect non-deterministic (flaky) tests by reading CI run logs or test result history. Aggregates pass rates per test, identifies intermittent failures, recommends quarantine or fix, and maintains a flaky test registry. Best run during Polish phase or after multiple CI runs. (source alias: /test-flakiness).

## Arguments

- `input`: [ci-log-path | scan | registry]

## Workflow

1. Use the `$codex-game-studios:test-flakiness` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/test-flakiness <task details>
```
