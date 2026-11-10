# agent-thinking-skills

Skills that help agents reason better, think more creatively, and explore ideas more broadly. Distributed as a Claude Code plugin marketplace. Targets **Codex and Claude Code**.

## Install

```
/plugin marketplace add <github-user>/agent-thinking-skills
/plugin install thinking-skills@agent-thinking-skills
```

For local development, use the repo path instead: `/plugin marketplace add ./`

## Skills

29 skills across four categories plus a router and a divergent-thinking baseline. Every skill follows progressive disclosure: YAML front matter (always loaded) → `SKILL.md` body (lean process) → `references/*.md` on demand → `scripts/*.py` offline helpers.

### Reframe the problem

| Skill | What it does | Use when |
|---|---|---|
| `lateral-thinking` | Break dominant patterns with provocations (Po) and movement to fresh frames | Answers feel predictable / stuck on the obvious |
| `first-principles` | Separate fundamentals from inherited assumptions, rebuild from foundations | "This is how it is done" dominates |
| `challenge-assumptions` | Inventory hidden beliefs, test false / unnecessary / reversed, reframe | Problem feels overconstrained |
| `question-storming` | Generate questions before answers, revise the problem statement | Brief is vague / prematurely solution-focused |
| `abstraction-laddering` | Why-up / how-down across vision → action levels | Framing too narrow or too abstract |
| `inversion` | Guarantee failure → extract preventive design principles | Direct reasoning misses obstacles |

### Generate more varied ideas

| Skill | What it does | Use when |
|---|---|---|
| `scamper` | Seven operators on a concrete baseline to produce variations | Baseline exists to improve |
| `reverse-brainstorming` | Worsen deliberately, then reverse into improvements | Brainstorming has stalled |
| `forced-connections` | Random stimulus → forced property mapping → surprising connections | Ideas too similar |
| `analogical-thinking` | Transfer mechanisms from structurally similar domains (not surface features) | Another field may have solved this |
| `morphological-analysis` | Dimensions × options matrix, prune, sample, synthesize | Several independent choices |
| `brainwriting` | Silent written passes, build on others, cluster | Early voices anchor / loud voices dominate |
| `crazy-eights` | Eight distinct concepts in eight minutes (text adaptation) | Quick burst of alternatives needed |
| `constraint-driven-ideation` | Forcing constraints (no budget, offline-only, one day) → transferable insights | Open brief → generic ideas |
| `ideal-final-result` | Ideal benefit with no added cost/harm/complexity, then approximate | Incremental improvement insufficient |

### Explore perspectives and possibilities

| Skill | What it does | Use when |
|---|---|---|
| `six-thinking-hats` | Six modes (White/Red/Yellow/Black/Green/Blue) one at a time | Critique interrupts brainstorming |
| `dreamer-realist-critic` | Three-room Disney strategy (dream → realism → critique, distinct) | Bold idea needs a path to execution |
| `stakeholder-perspectives` | Map needs/constraints per group, name tensions, find better tradeoffs | Solution helps one group, burdens another |
| `what-if` | Mutate one assumption, branch a world, trace, transfer back | Blue-sky / strategic exploration |
| `scenario-planning` | 2× uncertainties → 2×2 worlds, score options per world, signals | Future uncertain |
| `backcasting` | Desired future → backward milestones → near-term actions | Long-term ambition lacks a route |
| `futures-wheel` | Center change → first/second/third-order consequences (opportunities + harms) | Ripple effects matter |

### Turn exploration into stronger options

| Skill | What it does | Use when |
|---|---|---|
| `double-diamond` | Discover → Define → Develop → Deliver; orchestroates other methods | Need both problem discovery and solution exploration |
| `triz-contradictions` | Contradiction + separation / 40 principles to break a recurring tradeoff | Technical tradeoff recurs |
| `concept-blending` | Blend mechanisms (not features) into a coherent concept | Several partial ideas each carry value |
| `premortem` | "Already failed" → independent reasons → prevention/monitoring | Before commitment |
| `options-portfolio` | Achievable / ambitious / exploratory portfolio with a probe each | Broad set needs narrowing |

### Router & baseline

| Skill | What it does | Use when |
|---|---|---|
| `thinking-router` | Triage into *better question / more ideas / broader perspectives / stronger options*, scores 27 methods, hands off with user confirmation | Unsure which method fits; "help me think creatively" |
| `divergent-thinking` | 10+ options → lenses → cluster → converge | Need many varied options before choosing one |

Full method list and triggers: `plugins/thinking-skills/skills/thinking-router/references/catalog.md`.
Source catalog: `megamouth/docs/creative-thinking-methodologies.md`.
Examples run offline where noted via `scripts/*.py` (seeded, deterministic, no network).

## Contributing

See [CLAUDE.md](CLAUDE.md) for layout and the progressive-disclosure rules. Start new skills from `templates/skill/` and run `python3 scripts/validate.py`.

Versioning: bump `version` in both `.claude-plugin/marketplace.json` and `plugins/thinking-skills/.claude-plugin/plugin.json` for releases. Current: `0.2.0` (29 skills).
