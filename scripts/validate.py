#!/usr/bin/env python3
"""Validate the marketplace, plugin manifests, and skills.

Checks JSON manifests, SKILL.md frontmatter, progressive-disclosure limits,
and that relative links in SKILL.md resolve. Exit code 1 on any error.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAX_DESC = 1024
MAX_BODY_LINES = 500
errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def load_json(path: Path):
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as e:
        err(f"{path.relative_to(ROOT)}: {e}")


def frontmatter(text: str):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm


def check_skill(skill_dir: Path) -> None:
    rel = skill_dir.relative_to(ROOT)
    md = skill_dir / "SKILL.md"
    if not md.exists():
        return err(f"{rel}: missing SKILL.md")
    text = md.read_text()
    fm = frontmatter(text)
    if fm is None:
        return err(f"{rel}/SKILL.md: missing frontmatter")
    name, desc = fm.get("name", ""), fm.get("description", "")
    if name != skill_dir.name:
        err(f"{rel}/SKILL.md: name '{name}' must match directory '{skill_dir.name}'")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
        err(f"{rel}/SKILL.md: name must be lowercase-hyphenated")
    if not desc:
        err(f"{rel}/SKILL.md: missing description")
    elif len(desc) > MAX_DESC:
        err(f"{rel}/SKILL.md: description over {MAX_DESC} chars")
    if len(text.splitlines()) > MAX_BODY_LINES:
        err(f"{rel}/SKILL.md: over {MAX_BODY_LINES} lines; move detail to references/")
    for target in re.findall(r"\]\(((?!https?:|#)[^)]+)\)", text):
        if not (skill_dir / target).exists():
            err(f"{rel}/SKILL.md: broken link {target}")


def main() -> int:
    market = load_json(ROOT / ".claude-plugin" / "marketplace.json")
    if market:
        for key in ("name", "owner", "plugins"):
            if key not in market:
                err(f"marketplace.json: missing '{key}'")
        for p in market.get("plugins", []):
            src = ROOT / p.get("source", "")
            if not (src / ".claude-plugin" / "plugin.json").exists():
                err(f"marketplace.json: plugin '{p.get('name')}' has no plugin.json at {p.get('source')}")
                continue
            manifest = load_json(src / ".claude-plugin" / "plugin.json")
            if manifest and manifest.get("name") != p.get("name"):
                err(f"plugin '{p.get('name')}': name mismatch with plugin.json")
            for skill in sorted((src / "skills").glob("*/")):
                check_skill(skill)
    for e in errors:
        print(f"ERROR {e}")
    print("OK" if not errors else f"{len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
