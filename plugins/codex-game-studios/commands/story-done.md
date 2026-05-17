# /story-done

End-of-story completion review. Reads the story file, verifies each acceptance criterion against the implementation, checks for GDD/ADR deviations, prompts code review, updates story status to Complete, and surfaces the next ready story from the sprint. (source alias: /story-done).

## Arguments

- `input`: [story-file-path] [--review full|lean|solo]

## Workflow

1. Use the `$codex-game-studios:story-done` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/story-done <task details>
```
