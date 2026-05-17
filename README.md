# Codex Game Studios

Codex Game Studios is a Codex-native plugin package for structured solo and small-team game development workflows. It ports the studio-style workflow from Claude Code Game Studios into Codex plugin surfaces: skills, commands, role references, templates, rule references, validation scripts, and local marketplace metadata.

## What Is Included

| Area | Count | Location |
| --- | ---: | --- |
| Codex skills | 73 | `plugins/codex-game-studios/skills/` |
| Commands | 73 | `plugins/codex-game-studios/commands/` |
| Role references | 49 | `plugins/codex-game-studios/references/roles/` |
| Hook scripts preserved for manual validation | 12 | `plugins/codex-game-studios/scripts/hooks/` |
| Path-scoped rule references | 11 | `plugins/codex-game-studios/references/rules/` |

The plugin is self-contained. It does not require a local `ref/` checkout to install, remove, or validate.

## Install

From this repository root:

```bash
codex plugin marketplace add .
```

This registers the local marketplace named `codex-game-studios-local`, which exposes the `codex-game-studios` plugin from `plugins/codex-game-studios`.

## Remove

```bash
codex plugin marketplace remove codex-game-studios-local
```

## Validate

Run the self-contained verifier:

```bash
python plugins/codex-game-studios/scripts/validate_port.py
```

The verifier checks:

- plugin manifest JSON and required Codex paths
- marketplace JSON
- 73 skills and 73 matching commands
- command-to-skill references such as `$codex-game-studios:design-system`
- 49 role references
- 12 preserved hook scripts
- 11 rule references
- generated skill frontmatter
- runtime skills and commands for blocked Claude-only terms

For an install/remove smoke test without touching your normal Codex config:

```bash
tmp_home=$(mktemp -d /tmp/codex-game-studios.XXXXXX)
CODEX_HOME="$tmp_home" codex plugin marketplace add .
CODEX_HOME="$tmp_home" codex plugin marketplace remove codex-game-studios-local
rm -rf "$tmp_home"
```

## Usage

After installing the marketplace, use the plugin through Codex skills or commands. Examples:

```text
$codex-game-studios:start
$codex-game-studios:design-system
$codex-game-studios:code-review
```

Command files are available under `plugins/codex-game-studios/commands/` for slash-style command surfaces such as `/start`, `/design-system`, and `/code-review`.

## Design Notes

- `plugins/codex-game-studios/.codex-plugin/plugin.json` is the plugin manifest.
- `.agents/plugins/marketplace.json` is the local marketplace descriptor.
- `plugins/codex-game-studios/references/source-inventory.json` freezes the source counts and names used by validation.
- `design/index.html` and `design/modules/` document the porting specification and conversion contracts.
- Automatic hook registration is intentionally omitted until a verified Codex hook event schema is available. Hook scripts are preserved under `scripts/hooks/` for explicit validation workflows.

## Upstream Credit

This project is a Codex port inspired by and derived from [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios). Full credit goes to the original project for the studio hierarchy, game-development workflow design, agents, skills, templates, and production methodology. The upstream project is MIT licensed; the license copy is preserved at `plugins/codex-game-studios/references/source-docs/UPSTREAM_LICENSE`.
