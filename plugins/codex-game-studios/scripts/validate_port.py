#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
INVENTORY = ROOT / "references" / "source-inventory.json"
DISALLOWED_FRONTMATTER = {
    "argument-hint", "user-invocable", "allowed-tools", "tools", "model",
    "maxTurns", "memory", "disallowedTools", "skills",
}


def split_frontmatter(text: str):
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    data = {}
    for line in raw.splitlines():
        if not line.strip() or line.startswith(" "):
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data, text[end + 5 :]


def fail(errors):
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    raise SystemExit(1)


def main():
    errors = []
    try:
        inventory = json.loads(INVENTORY.read_text())
    except Exception as exc:
        fail([f"source inventory JSON failed: {exc}"])

    manifest_path = ROOT / ".codex-plugin" / "plugin.json"
    try:
        manifest = json.loads(manifest_path.read_text())
    except Exception as exc:
        fail([f"manifest JSON failed: {exc}"])

    if manifest.get("name") != "codex-game-studios":
        errors.append("manifest name must be codex-game-studios")
    if manifest.get("skills") != "./skills/":
        errors.append("manifest skills path must be ./skills/")
    if manifest.get("commands") != "./commands/":
        errors.append("manifest commands path must be ./commands/")
    if not manifest.get("interface", {}).get("displayName"):
        errors.append("manifest interface.displayName missing")

    source_skills = sorted(inventory.get("skills", []))
    target_skills = sorted(p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md"))
    commands = sorted(p.stem for p in (ROOT / "commands").glob("*.md"))
    source_roles = sorted(inventory.get("roles", []))
    target_roles = sorted(p.stem for p in (ROOT / "references" / "roles").glob("*.md"))
    source_hooks = sorted(inventory.get("hooks", []))
    target_hooks = sorted(p.name for p in (ROOT / "scripts" / "hooks").glob("*") if p.is_file())
    source_rules = sorted(inventory.get("rules", []))
    target_rules = sorted(p.name for p in (ROOT / "references" / "rules").glob("*.md"))
    expected = inventory.get("expected_counts", {})

    expected_counts = {
        "skills": (expected.get("skills", 73), len(source_skills), len(target_skills)),
        "commands": (expected.get("commands", 73), len(source_skills), len(commands)),
        "roles": (expected.get("roles", 49), len(source_roles), len(target_roles)),
        "hooks": (expected.get("hooks", 12), len(source_hooks), len(target_hooks)),
        "rules": (expected.get("rules", 11), len(source_rules), len(target_rules)),
    }
    for label, (expected, source_count, target_count) in expected_counts.items():
        if source_count != expected:
            errors.append(f"source {label} count {source_count} != {expected}")
        if target_count != expected:
            errors.append(f"target {label} count {target_count} != {expected}")

    if source_skills != target_skills:
        errors.append("target skills do not exactly match source skill names")
    if source_skills != commands:
        errors.append("commands do not exactly match source skill names")
    if source_roles != target_roles:
        errors.append("target roles do not exactly match source agent names")
    if source_hooks != target_hooks:
        errors.append("target hooks do not exactly match source hook names")
    if source_rules != target_rules:
        errors.append("target rules do not exactly match source rule names")

    per_skill = []
    forbidden_runtime_terms = [
        "AskUserQuestion",
        "TodoWrite",
        ".claude",
        "CLAUDE.md",
        "allowed-tools",
        "argument-hint",
        "user-invocable",
        "disallowedTools",
        "maxTurns",
        "Claude session",
    ]
    for path in sorted((ROOT / "skills").glob("*/SKILL.md")):
        skill_text = path.read_text()
        meta, body = split_frontmatter(skill_text)
        name = path.parent.name
        if meta.get("name") != name:
            errors.append(f"{path}: frontmatter name mismatch")
        if "description" not in meta or len(meta["description"].strip()) < 20:
            errors.append(f"{path}: missing useful description")
        leaked = sorted(set(meta) & DISALLOWED_FRONTMATTER)
        if leaked:
            errors.append(f"{path}: Claude-only frontmatter keys remain: {', '.join(leaked)}")
        command_path = ROOT / "commands" / f"{name}.md"
        command_text = command_path.read_text()
        if f"$codex-game-studios:{name}" not in command_text:
            errors.append(f"{command_path}: does not reference matching skill")
        if not command_text.startswith(f"# /{name}\n"):
            errors.append(f"{command_path}: missing command heading # /{name}")
        for section in ["## Arguments", "## Workflow", "## Examples"]:
            if section not in command_text:
                errors.append(f"{command_path}: missing {section}")
        for section in ["## Codex Port Notes", "## Ported Workflow"]:
            if section not in skill_text:
                errors.append(f"{path}: missing {section}")
        for term in forbidden_runtime_terms:
            if term in skill_text:
                errors.append(f"{path}: forbidden runtime term remains: {term}")
            if term in command_text:
                errors.append(f"{command_path}: forbidden runtime term remains: {term}")
        per_skill.append({"name": name, "skill": str(path.relative_to(ROOT)), "command": str(command_path.relative_to(ROOT))})

    for json_path in [ROOT / ".codex-plugin" / "plugin.json", REPO / ".agents" / "plugins" / "marketplace.json"]:
        try:
            json.loads(json_path.read_text())
        except Exception as exc:
            errors.append(f"{json_path}: JSON failed: {exc}")

    if errors:
        fail(errors)

    report = {
        "status": "passed",
        "plugin": str(ROOT),
        "counts": {
            "skills": len(target_skills),
            "commands": len(commands),
            "roles": len(target_roles),
            "hooks": len(target_hooks),
            "rules": len(target_rules),
        },
        "validated_skill_commands": per_skill,
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
