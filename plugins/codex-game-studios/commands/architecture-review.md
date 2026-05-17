# /architecture-review

Validates completeness and consistency of the project architecture against all GDDs. Builds a traceability matrix mapping every GDD technical requirement to ADRs, identifies coverage gaps, detects cross-ADR conflicts, verifies engine compatibility consistency across all decisions, and produces a PASS/CONCERNS/FAIL verdict. The architecture equivalent of /design-review. (source alias: /architecture-review).

## Arguments

- `input`: [focus: full | coverage | consistency | engine | single-gdd path/to/gdd.md]

## Workflow

1. Use the `$codex-game-studios:architecture-review` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/architecture-review <task details>
```
