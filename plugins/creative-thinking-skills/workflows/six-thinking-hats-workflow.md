# Six Thinking Hats — Agent Workflow

Proves the catalog note: "Agent-based workflows may be useful for some methods" — the sequential, single-hat-at-a-time variant.

## Goal

Enforce what asynchronous or single-loop prompting breaks: **one hat at a time, every participant in the same hat, Blue owns sequence and synthesis**. Subagents are not "personalities" in hats — hats are thinking modes; every participant wears the called hat when it is called.

## When this workflow fits

- Brainstorming and criticism keep interrupting each other, or a decision needs both optimism and caution without them competing in the same sentence.
- You want a repeatable, timed sequence that scales beyond one conversation's turn-taking.

Otherwise use the single-conversation `six-thinking-hats/SKILL.md`.

## Topology

```
Blue (open)
 │
 ├─ choose sequence from skills/six-thinking-hats/references/sequences.md
 │  (e.g. quick / exploratory / decision — default: switching to Blue → White → Red → Yellow → Black → Green → Blue)
 │
 ├─ Sequential subagent chain — one participant ensemble per hat
 │   ├─ White  — facts / gaps / unknowns (subagents: 2–3 in parallel *inside* the hat, still White)
 │   ├─ Red    — feelings / intuition (brief, subjective)
 │   ├─ Yellow — benefits / value
 │   ├─ Black  — caution / risks
 │   └─ Green  — creativity / alternatives (may delegate to lateral-thinking/random_entry.py)
 │
 └─ Blue (close) — per-hat outputs → tensions → decision / tensions / next steps with keep/kill signals
```

- **Why sequential chains:** a hat's participants run in parallel *within* the hat, but hats themselves are strictly sequential — Yellow before Black, Green after Black when repairing. Fans whose children depend on each other's results are a race; the Blue sequence is the dependency.
- **Integration owner:** Blue (main agent). Subagents do not call the next hat; they return their hat's output and Blue routes.

## Process (what each agent does)

### Blue — open (main agent)

- Set focus, real goal, time per hat (`scripts/sequence.py --goal exploratory --time 20`), and the chosen sequence. Announce one-hat-at-a-time rule and time-boxes.

### Per-hat participants (subagents, batch per hat)

- **Prompt:** "You are wearing the {White|Red|Yellow|Black|Green} hat. Produce only this hat's output. Rules: one idea per row, label fact/assumption/speculation, no mixing."
- **White** — facts, gaps, unknowns; **Red** — subjective, brief; **Yellow** — benefits + conditions; **Black** — specific risks + required checks; **Green** — alternatives/provocations, quantity before quality.
- Side-by-side participants inside one hat are `task` subagents fanned in one `tasks[]` batch; the hat still stays one mode.

### Blue — close (main agent)

- Summarize per-hat outputs, name tensions (Yellow↔Black is the common one), recommend next steps with signals, and propose handoff (`premortem`, `options-portfolio`, `scamper`). Example trace: `skills/six-thinking-hats/references/examples.md`.

## Interface contract

```yaml
Input to hat participant:
  hat: Yellow
  focus: "Should we ship new onboarding this sprint?"
  constraints: { time: "20 min", forbidden: "no Black during Yellow" }

Output per hat participant:
  rows:
    - { text: "Adoption visible faster where invite exists", tag: "fact" }
    - { text: "Hunch: solo invites will hate the new copy", tag: "subjective" }

Blue synthesis (owner):
  per_hat: { White: [...], Red: [...], Yellow: [...], Black: [...], Green: [...] }
  tensions: [{ between: "Yellow↔Black", tension: "overlap of acknowledged benefit and named risk" }]
  decision: { action: "ship to invited cohort only", signals: ["adoption at 48h"], owner: "onboarding lead" }
```

## Launch sketch (Codex / Claude Code)

```python
# Blue opens, then sequential hat chains with parallel participants inside each hat
for hat in ["White", "Red", "Yellow", "Black", "Green"]:
    tasks = [
        dict(name=f"{hat}{i+1}", task=f"Wear {hat} hat for focus: {{focus}} ...", agent="sonic",
             solutionSpace=f"one fix: produce {hat} outputs only, rows given")
        for i in range(3 if hat != "Red" else 2)
    ]
    # fan per hat, wait, Blue validates one-hat-at-a-time before advancing
# Blue closes: per-hat outputs + tensions + next steps
```

`agent: sonic` is low-reasoning mechanical; scale to 2–3 per hat as the doc's `brainwriting` note intends (“approximate structure without implying independent human perspectives”). Never mix two hats in one `tasks[]` batch.

## Verification

- One hat per turn enforced by Blue — validator checks no Red in White output, no Black in Green.
- Yellow before Black sequencing rule respected (decision vs. exploratory sequence selection).
- Traces use `scripts/sequence.py` for budgeting; tensions explicitly reference per-hat artifacts.

## Progressive disclosure

- This file is the workflow layer; the hub stays `skills/six-thinking-hats/SKILL.md`.
- Detail lives in `references/hats.md`, `references/sequences.md`, `references/facilitation.md` — workflow adds only the sequential orchestration.

## References

- `skills/six-thinking-hats/SKILL.md` + `references/sequences.md` (7 sequences)
- `workflows/brainwriting-workflow.md` — parallel contrast workflow
- `examples/gallery.md` — runnable prompts linking here
