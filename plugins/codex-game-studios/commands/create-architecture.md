# /create-architecture

Guided, section-by-section authoring of the master architecture document for the game. Reads all GDDs, the systems index, existing ADRs, and the engine reference library to produce a complete architecture blueprint before any code is written. Engine-version-aware: flags knowledge gaps and validates decisions against the pinned engine version. (source alias: /create-architecture).

## Arguments

- `input`: [focus-area: full | layers | data-flow | api-boundaries | adr-audit] [--review full|lean|solo]

## Workflow

1. Use the `$codex-game-studios:create-architecture` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/create-architecture <task details>
```
