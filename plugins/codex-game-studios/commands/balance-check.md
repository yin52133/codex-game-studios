# /balance-check

Analyzes game balance data files, formulas, and configuration to identify outliers, broken progressions, degenerate strategies, and economy imbalances. Use after modifying any balance-related data or design. Use when user says 'balance report', 'check game balance', 'run a balance check'. (source alias: /balance-check).

## Arguments

- `input`: [system-name|path-to-data-file]

## Workflow

1. Use the `$codex-game-studios:balance-check` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/balance-check <task details>
```
