# Example Gallery

One runnable prompt per category plus an end-to-end chain. Copy the prompt into Codex or Claude Code after installing `thinking-skills`; the listed skill(s) will handle the rest. Helpers are offline under `plugins/thinking-skills/skills/<skill>/scripts/`.

> New? Start with **Quick start** below, then pick one category. Unsure which fits → run `thinking-router` first.

## Quick start (60 s)

```
/plugin marketplace add <github-user>/agent-thinking-skills
/plugin install thinking-skills@agent-thinking-skills

# Then in any conversation:
> Help me think creatively about our onboarding — not sure which method fits.
# → thinking-router triages into better question / more ideas / broader perspectives / stronger options
#   and hands off to 1–2 skills with user confirmation.
```

Offline helpers you can run without an agent:

```bash
python plugins/thinking-skills/skills/thinking-router/scripts/route.py --text "brief is vague, are we asking the right question?"
python plugins/thinking-skills/skills/lateral-thinking/scripts/random_entry.py --count 3 --seed 7 --problem "retention drops in week 2"
python plugins/thinking-skills/skills/scamper/scripts/scamper.py --subject "onboarding email (welcome letter) — sent 3 days after signup" --select S,E
```

---

## 1 · Reframe the problem

### Lateral thinking — stuck on the obvious
**Prompt:**
> Our retention offer is always "10% off next month." It works once, then churn returns. Break the dominant pattern and find unexpected directions — we can be weird here.

**Skill:** `lateral-thinking` → dominant idea (`retention == discount`) → 5 `Po:` across ≥3 operators → movement → 3–5 frames + probes.  
**Expected artifact:** new boxes ("retention as progress kept, not price cut"), not tweaked discounts.

### Challenge assumptions — every option looks impossible
**Prompt:**
> Every option to shorten onboarding is blocked: "we can't skip KYC," "legal says email only," "users expect the tutorial." What's actually fixed vs. inherited?

**Skill:** `challenge-assumptions` → inventory (inherited / stakeholder / boundary / continuity) → pressure-test false / unnecessary / reversed → reframe patterns.  
**Helper:** `python plugins/thinking-skills/skills/challenge-assumptions/scripts/inventory.py --problem "must email users before activation"`

### Question storming — vague brief
**Prompt:**
> Brief is "make onboarding better." Before solutions — help us ask better questions and rewrite the problem statement.

**Skill:** `question-storming` → 20+ questions across six categories → cluster → rank by leverage/tractability/reframe → 2–3 revised statements + probes.

### First principles / Abstraction laddering / Inversion
**Prompts:**
> `first-principles` — Which constraints around activation are physics/regulation vs. copied convention? Rebuild from fundamentals.  
> `abstraction-laddering` — "Fix the signup button" feels too low. Climb to purpose, then ladder back down to mechanisms.  
> `inversion` — How would we *guarantee* this launch fails? Turn those routes into design principles.

---

## 2 · Generate more varied ideas

### SCAMPER — you have a baseline
**Prompt:**
> Baseline: welcome letter by post 5 days after signup. Run SCAMPER to produce systematic variations — need 10+ concrete tweaks, then a shortlist.

**Skill:** `scamper` (all 7 or selective 3–4) with `scripts/scamper.py`.  
**Helpers:** `python plugins/thinking-skills/skills/scamper/scripts/scamper.py --subject "welcome letter ..." --select SCAMPER`

### Reverse brainstorming — brainstorming stalled
**Prompt:**
> Brainstorming is stuck on polite ideas. How would we *guarantee* users miss the onboarding window? Flip those into improvements.

**Skill:** `reverse-brainstorming` — worsen 15–25 → cluster by mechanism → reverse via negate / invert actor / re-scope.

### Forced connections — ideas too similar
**Prompt:**
> Ideas keep circling "send another reminder." Force a random stimulus to break the cluster.

**Skill:** `forced-connections` + `python plugins/thinking-skills/skills/forced-connections/scripts/connect.py --pick random --json`

### Analogical thinking — another domain solved this
**Prompt:**
> Another field may have solved this structurally — hospital wayfinding, logistics routing, game matchmaking. Map the mechanism, not the surface feature, and state limits.

**Skill:** `analogical-thinking` (function / flow / constraint / feedback → far-domain search → structure map → breakpoints → principle + probe).

### Morphological analysis / Brainwriting / Crazy 8s
**Prompts:**
> `morphological-analysis` — Trigger × channel × timing × owner = combinations. Build the box, prune, sample, synthesize.  
> `brainwriting` — *Use the agent workflow when the group anchors early — see `plugins/thinking-skills/workflows/brainwriting-workflow.md`.* Silent passes, then synthesize (also works with AI passes).  
> `crazy-eights` — Eight distinct onboarding concepts in eight minutes — variety check required.

---

## 3 · Explore perspectives and possibilities

### Six Thinking Hats — critique interrupts brainstorming
**Prompt:**
> We need optimism and caution without them interrupting each other. Run the hats once over this decision — keep one hat at a time.

**Skill:** `six-thinking-hats` — Blue opens/closes, one hat per turn, peer workflow `workflows/six-thinking-hats-workflow.md`.  
**Helper:** `python plugins/thinking-skills/skills/six-thinking-hats/scripts/sequence.py --goal exploratory --time 20`

### Disney Creative Strategy — bold idea, no path
**Prompt:**
> Dream a bold onboarding that feels obvious in hindsight, make it realistic, then criticize it usefully — three rooms, no mixing.

**Skill:** `dreamer-realist-critic` — dreamer → realist → critic → revise.

### Stakeholder perspectives — who bears the cost?
**Prompt:**
> This speeds up support but may hurt finance. Who pays the cost we are not seeing? Map needs/constraints per group, name tensions, find better tradeoffs.

**Skill:** `stakeholder-perspectives` — hypotheses to validate, not user research.

### What-if / Scenario planning / Backcasting / Futures wheel
**Prompts:**
> `what-if` — What if support had zero cost for a month? What breaks or becomes newly valuable?  
> `scenario-planning` — Two uncertainties × 2 → four worlds; score each option per world, name signals.  
> `backcasting` — Desired onboarding in 3 years → step backward to quarterly milestones.  
> `futures-wheel` — Put the change in the center, ring first/second/third-order effects with risks and opportunities.

---

## 4 · Turn exploration into stronger options

### Double Diamond — need both problem and solution
**Prompt:**
> Need both the right problem and the right solution. Run the full Discover → Define → Develop → Deliver, sequencing other methods inside the diamonds.

**Skill:** `double-diamond` orchestrates, e.g. `question-storming → morphological-analysis → premortem`.

### TRIZ contradictions — recurring tradeoff
**Prompt:**
> Speed vs. accuracy keeps recurring — faster onboarding worsens setup errors. Name the contradiction and break it, don't balance it.

**Skill:** `triz-contradictions` — technical vs. physical, separation by space/time/condition/scale, 40 principles.

### Concept blending / Premortem / Options portfolio
**Prompts:**
> `concept-blending` — Blend two partial parents (pre-configured entry + peer artifact) — mechanism, not feature pile.  
> `premortem` — It's 6 months later, the launch failed. Independent reasons, then prevention + monitoring with owners.  
> `options-portfolio` — Broad set → achievable / ambitious / exploratory portfolio, one probe each.

---

## 5 · Extended & convergence (6 + 4 beyond the 27)

### Systematic Inventive Thinking — strict constraints

**Prompt:**
> We have an invite system with fixed components — no new budget or channel. Mutate it inside the closed world.

**Skill:** `systematic-inventive-thinking` → pick one SIT operator (Subtraction / Multiplication / Division / Task Unification / Attribute Dependency) → virtual product → enrich → probe.  
**Helper:** `python plugins/thinking-skills/skills/systematic-inventive-thinking/scripts/sit.py --list`

### C-K Theory — variation exhausted

**Prompt:**
> We've tried every variant of the invite — need generative expansion, not selection. Build a C-tree and name the missing K.

**Skill:** `c-k-theory` → restrictive vs expansive partitions → K pockets → design square → probe.

### Bodystorming — service you can't picture

**Prompt:**
> Walk through the activation as bodies in space — where do people hesitate, collide, wait, or recover?

**Skill:** `bodystorming` → space + props → walkthrough → friction clusters → spatial probe.

### Rich Picture + CATWOE — messy situation

**Prompt:**
> No one shares the same picture of why capacity fails. Draw the mess, then define the system with CATWOE.

**Skill:** `rich-picture-catwoe` → rich picture → CATWOE → root definition → debate.

### Causal Loop Diagram — fix makes problem worse

**Prompt:**
> More reminders → less attention → lower activation. Map the loops and find leverage.

**Skill:** `causal-loop-diagram` → variables → polarity + delays → R/B loops → archetypes → leverage map.

### Synectics — familiar analogies stall

**Prompt:**
> "Onboarding as invitation" is tired. Make the familiar strange with four analogies, then excursion.

**Skill:** `synectics` → personal / direct / symbolic / fantasy → excursion → springboards.

### Liberating Structures — hierarchy dominates

**Prompt:**
> 14 people, senior voices dominate. Run a fair micro-structure sequence.

**Skill:** `liberating-structures` → choose 1-2 of 1-2-4-All / Impromptu Networking / 15% Solutions / TRIZ / Wicked Questions / Ecocycle → timed run → harvest.  
**Helper:** `python plugins/thinking-skills/skills/liberating-structures/scripts/ls.py --list`

### Nominal Group Technique / Delphi — need defensible ranking

**Prompt:**
> 14 fixes competing for one quarter — need credible, bias-resistant ranking with dissent logged.

**Skill:** `nominal-group-technique` → silent write → round-robin → clarify → vote (5-4-3-2-1 or N/3) / Delphi median-IQR → tally + dissent.  
**Helper:** `python plugins/thinking-skills/skills/nominal-group-technique/scripts/ngt.py --count 12 --voters 6 --method ranked --json`

### Lotus Blossom — need 30–70 ideas with lineage

**Prompt:**
> 8 ideas aren't enough but morph box is too combinatorial. Bloom radial 8×8.

**Skill:** `lotus-blossom` → centre → 8 petals → each petal 8 blooms (=72) → prune → harvest 3–5.  
**Helper:** `python plugins/thinking-skills/skills/lotus-blossom/scripts/lotus.py --theme "reduce week-1 drop" --json`

### Dot Voting + Impact–Effort — too many, need visible priority

**Prompt:**
> 18 candidates on the wall — need a quick shortlist that shows effort honestly.

**Skill:** `dot-voting-prioritize` → N/3 dots (simultaneous) → impact–effort plot → ICE where data exists → keep/pivot/kill + owners.  
**Helper:** `python plugins/thinking-skills/skills/dot-voting-prioritize/scripts/vote.py --count 18 --voters 6 --impact-effort --json`

---

## End-to-end chain (copy-paste ready)

> You are the `thinking-router`. Triage whether we need a better question, more ideas, broader perspectives, or stronger options for: "Onboarding drops 32% before first value; invites carry no intent, activation is uninstrumented." Score 37 methods, shortlist 2–3, then hand off to the primary with user confirmation. If we pick lateral-thinking, carry the intake forward; end with a probe.
>
> After the router hands off, continue as that skill and produce its artifact (Po set, box, scenarios, etc.) — one hat/operator at a time, no rewordings.

---

## Where to look next

- Method catalog with triggers: `plugins/thinking-skills/skills/thinking-router/references/catalog.md`
- Agent workflows: `plugins/thinking-skills/workflows/brainwriting-workflow.md` and `six-thinking-hats-workflow.md`
- Offline helpers: `plugins/thinking-skills/skills/<skill>/scripts/` (`--list`, `--json`, `--seed`)
- Design principles + provenance: each skill's `references/provenance.md`
