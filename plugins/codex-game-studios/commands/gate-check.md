# /gate-check

Validate readiness to advance between development phases. Produces a PASS/CONCERNS/FAIL verdict with specific blockers and required artifacts. Use when user says 'are we ready to move to X', 'can we advance to production', 'check if we can start the next phase', 'pass the gate'. (source alias: /gate-check).

## Arguments

- `input`: [target-phase: systems-design | technical-setup | pre-production | production | polish | release] [--review full|lean|solo]

## Workflow

1. Use the `$codex-game-studios:gate-check` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/gate-check <task details>
```
