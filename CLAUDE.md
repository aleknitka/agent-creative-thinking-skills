# agent-thinking-skills

A Claude Code plugin marketplace of skills for creative thinking and better agent reasoning.

## Layout

- `.claude-plugin/marketplace.json` - marketplace catalog (lists plugins)
- `plugins/<plugin>/.claude-plugin/plugin.json` - plugin manifest
- `plugins/<plugin>/skills/<skill>/SKILL.md` - one skill per directory
- `plugins/<plugin>/skills/<skill>/references/` - on-demand detail
- `templates/skill/` - copy to start a new skill
- `scripts/validate.py` - run before committing

## Progressive disclosure (required)

1. **Frontmatter `description`** is always in context. Say what and when, with trigger phrases. Max 1024 chars.
2. **`SKILL.md` body** loads when the skill triggers. Keep it a lean process (under ~100 lines, hard cap 500).
3. **`references/*.md`** load only when needed. One topic per file, linked directly from SKILL.md (no nested chains).

## Adding a skill

1. `cp -r templates/skill plugins/thinking-skills/skills/<name>`
2. Edit SKILL.md; `name` must equal the directory name.
3. `python3 scripts/validate.py`
4. Bump `version` in both `plugin.json` and `marketplace.json` for releases.
