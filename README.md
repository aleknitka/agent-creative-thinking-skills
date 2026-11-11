# agent-thinking-skills

Skills that help agents reason better, think more creatively, and explore ideas more broadly. Distributed as a Claude Code plugin marketplace. Targets **Codex and Claude Code**. 39 skills, a router (37 methods), an example gallery, two agent workflows, and a shared workspace.

## Install

```
/plugin marketplace add <github-user>/agent-thinking-skills
/plugin install thinking-skills@agent-thinking-skills
```

For local development, use the repo path instead: `/plugin marketplace add ./`

## Skills

39 skills (27 base + 10 extended) across four categories plus a router and a divergent-thinking baseline — catalog is 37 methods (27+10). Every skill follows progressive disclosure: YAML front matter (always loaded) → `SKILL.md` body (lean process) → `references/*.md` on demand → `scripts/*.py` offline helpers.

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

### Extended — beyond the 27 (research synthesis)
| Skill | What it does | Use when |
|---|---|---|
| `systematic-inventive-thinking` | SIT's 5 closed-world operators (Subtraction / Multiplication / Division / Task Unification / Attribute Dependency) — no new resource types | Have a concrete system, strict constraints |
| `c-k-theory` | C-K Theory: expand Concept and Knowledge together (restrictive vs expansive partitions) | Variation exhausted; need generative expansion |
| `bodystorming` | Enact with props/space/walkthrough to surface embodied friction | Spatial/service interaction hard to picture |
| `rich-picture-catwoe` | Rich Picture + CATWOE → root definition (Checkland/SSM) | Messy situation, no shared picture |
| `causal-loop-diagram` | Reinforcing/Balancing loops, delays, archetypes, Meadows leverage | Fix keeps making its problem worse |
| `synectics` | Synectics 4 analogies (Personal/Direct/Symbolic/Fantasy) + Excursion → springboards | Familiar analogies stall; need deeper excursion |
| `liberating-structures` | 6 Liberating Structures (1-2-4-All / Impromptu Networking / 15% Solutions / TRIZ / Wicked Questions / Ecocycle) | Hierarchy dominates; need equal-voice protocol |
| `nominal-group-technique` | NGT silent write → round-robin → vote + Delphi anonymized rounds → ranked shortlist with dissent log | Need credible ranking resistant to hierarchy |
| `lotus-blossom` | MY Lotus Blossom 8×8 — centre → 8 petals → 72 blooms with lineage | 8 not enough; need layered breadth |
| `dot-voting-prioritize` | Structured dot voting (N/3) + Impact–Effort + ICE → keep/pivot/kill | Many ideas need visible priority |

Source: `megamouth/research/extended-methods/synthesis.md` (10 from 41 candidates + 7 arXiv/8 OpenAlex; ranks 7–10 in Extended).

### Router & baseline

| Skill | What it does | Use when |
|---|---|---|
| `thinking-router` | Triage into *better question / more ideas / broader perspectives / stronger options*, scores 37 methods (27 base + 10 extended), hands off with user confirmation | Unsure which method fits; "help me think creatively" |
| `divergent-thinking` | 10+ options → lenses → cluster → converge | Need many varied options before choosing one |

Full method list and triggers: `plugins/thinking-skills/skills/thinking-router/references/catalog.md`.
Source catalog: `megamouth/docs/creative-thinking-methodologies.md` (27) + `megamouth/research/extended-methods/synthesis.md` (10 extended) — router catalog is 37.
Examples run offline where noted via `scripts/*.py` (seeded, deterministic, no network).

## Example Gallery

Copy-paste prompts for every category — no setup beyond installing the plugin. Each prompt lists the skill, the artifact it produces, and the offline helper where applicable.

**Start here:** `examples/gallery.md` — Quick start (60 s) → one demo per category → end-to-end `thinking-router → skill → probe` chain → links to catalog, workflows, and `references/provenance.md`.

Offline helpers you can try without an agent:
```bash
python plugins/thinking-skills/skills/thinking-router/scripts/route.py --text "brief is vague, are we asking the right question?"
python plugins/thinking-skills/skills/lateral-thinking/scripts/random_entry.py --count 3 --seed 7 --problem "retention drops in week 2"
python plugins/thinking-skills/skills/scamper/scripts/scamper.py --subject "welcome letter — sent 3 days after signup" --select S,E
```

## Agent Workflows

Single-conversation skills cover most cases; workflows add orchestration when humans and agents run together. Both live in `plugins/thinking-skills/workflows/` and are linked from the relevant `SKILL.md` via `Going deeper`.

| Workflow | Topology | Use |
|---|---|---|
| `brainwriting-workflow.md` | **Parallel** — fan N=3 generators via `task` in one `tasks[]` batch (silent pass1 → self-build pass2), one rotation build pass, then freeze → main-agent cluster (3–6 clusters) → harvest 2–3 concepts + probes | Group anchors early or is spread across timezones; you need 30–100 distinct ideas plus build edges. Otherwise use `skills/brainwriting/SKILL.md` solo. |
| `six-thinking-hats-workflow.md` | **Sequential** — Blue opens (chooses sequence via `scripts/sequence.py`) → chain White→Red→Yellow→Black→Green (parallel participants *inside* each hat, hats strictly sequential) → Blue closes (per-hat outputs → tensions → decision) | Critique interrupts brainstorming; you need one-hat-at-a-time enforced. Otherwise use `skills/six-thinking-hats/SKILL.md` solo. |

`thinking-router` can hand off to either workflow with user confirmation; the handoff note carries intake context.

## Workspace — shared board for humans + agents

Lightweight browser workspace — sticky notes, lanes/columns, drawing, dot voting, timer, clustering, and agent file I/O. No build step, no deps, vanilla JS. Open `workspace/index.html` in a browser; agents and humans share `workspace/boards/<id>.json`.

```
# open
open workspace/index.html              # or: python -m http.server 8000
# ?board=onboarding-q3 → workspace/boards/onboarding-q3.json
```

**Aids:** sticky notes (text, color, votes, fact/assumption/speculation/action/question), lanes/columns (hats, SCAMPER, sheets, phases, storyboard), freehand/line drawing on canvas, dot voting (`+` / lane header), timer (5/10/15 min), clustering by lane/`clusterId`, import/export **JSON** (`boards/_schema.json`) + **PNG**.

**Agent I/O:** read/write `workspace/boards/<id>.json`; file drop or `window.workspace.apply(state)` in the browser; optional `POST /api/state` via the ~40-line companion server when localStorage is not enough. See `workspace/boards/_schema.json` and the demo board `workspace/boards/demo.json`.

**Templates:** blank · six hats · brainwriting (P1·P2·P3) · SCAMPER (7) · crazy-8s (8) · backcasting timeline · morph box. Research note on reuse-vs-build (Scrumlr, Excalidraw, Drawnix, WBO, Retrospected, Kanvana) lives in `megamouth/research/workspace-aids/report.md`.

## Contributing

See [CLAUDE.md](CLAUDE.md) for layout and the progressive-disclosure rules. Start new skills from `templates/skill/` and run `python3 scripts/validate.py`.

Versioning: bump `version` in both `.claude-plugin/marketplace.json` and `plugins/thinking-skills/.claude-plugin/plugin.json` for releases. Current: `0.5.0` (39 skills: 27 base + 10 extended + router + divergent-thinking; 37-method router; gallery + workflows + workspace).
