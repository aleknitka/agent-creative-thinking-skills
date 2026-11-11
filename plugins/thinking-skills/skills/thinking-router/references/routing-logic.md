# Routing Logic — Decision Tree and Scoring

This is the router's judgment. Keep it transparent so the user can correct it.

## 1. Triage — map the situation to one primary need

```
Does the user need...                         Primary need
─────────────────────────────────────────────────────────────
...a better problem statement?                Better question
  vague brief, premature solution,            (reframe)
  overconstrained, "right question?"

...more alternatives from a starting point?   More ideas
  have a concept, ideas feel samey,           (generate)
  dimensions unexplored

...wider view of futures/stakeholders/        Broader perspectives
  consequences/vision?                        (explore)

...to stress-test, combine, or choose         Stronger options
  among candidates?                           (decide)
```

Mixed signals are normal. Pick the *next* artifact the user needs, not the final one. If two needs are equal, propose a *pair* or the `double-diamond` sequence rather than forcing one.

## 2. Score each method (0-3 per signal, sum wins)

For each of the 37 methods (27 base + 10 extended) in the catalog, add points:

| Signal | +2 | +1 | +0 |
|---|---|---|---|
| **Trigger match** — does the user's phrasing echo this method's "when to call it"? | Exact trigger phrase present | Related / partial | No match |
| **Output match** — does the method produce the artifact the user actually needs next? | Produces it directly | Could produce it with adaptation | Different artifact |
| **Appetite fit** — does it respect appetite for unconventional ideas? | Perfect (e.g., lateral/what-if only when appetite ≥ medium) | Tolerable with framing | Too wild or too tame |
| **Time fit** | Fits stated time box | Slight stretch, still workable | Unrealistic for time box |
| **Installed** (tie-breaker) | Skill/references present or general guidance can cover it | — | Would need missing bespoke material |

Weighting: **trigger (×2) + output (×2) + appetite + time + installed** is a good default. `scripts/route.py` implements this.

Suggested time budgets (rough, adapt to user):

| Method | Minutes |
|---|---|
| `question-storming`, `abstraction-laddering`, `inversion` | 10-15 |
| `challenge-assumptions`, `lateral-thinking`, `scamper`, `constraint-driven-ideation`, `premortem` | 15-25 |
| `analogical-thinking`, `forced-connections`, `crazy-eights`, `what-if`, `options-portfolio`, `concept-blending` | 10-20 |
| `morphological-analysis`, `futures-wheel`, `stakeholder-perspectives` | 20-35 |
| `scenario-planning`, `backcasting`, `dreamer-realist-critic`, `six-thinking-hats`, `double-diamond`, `triz-contradictions` | 30-60+ |
| `liberating-structures`, `nominal-group-technique` | 30-60 |  
| `lotus-blossom` | 25-40 |
| `dot-voting-prioritize` | 10-20 |

## 3. Apply guardrails

- **Prefer the Suggested first 8** on ties: `lateral-thinking`, `six-thinking-hats`, `scamper`, `challenge-assumptions`, `analogical-thinking`, `what-if`, `morphological-analysis`, `premortem`. They are chosen for breadth and accessibility.
- **Keep variety honest.** Shortlist 2-3 methods that differ in *mechanism or perspective* (e.g., don't shortlist both `inversion` and `reverse-brainstorming` unless you can justify distinct value).
- **Do not present simulated stakeholder views as research.** If recommending `stakeholder-perspectives`, label outputs as hypotheses to validate.
- **If the user arrived via a direct trigger** ("teach me SCAMPER," "run a premortem"), honor the request and use the router only to suggest a follow-up — don't reroute away.

## 4. Shape the recommendation

For the top 1-2, write:

```
Primary:   <method> — one-line what it does
Why now:   trigger + output match + appetite/time fit (1-2 lines)
You will get: concrete artifact (e.g., "3-5 reframed questions + a revised problem statement")
Effort:    ~N minutes, what the user does
Alternate: <method> — when you'd pick this instead (1 line)
Not now:   <strongest skipped method> — why not this time (1 line)
```

Then **ask** — not assume — before handing off (handoff patterns are in the companion reference, also linked from SKILL.md).

## 5. Edge cases

- **No strong match** → ask one clarifying question and offer a provisional route ("Sounds like a 'better question' need — I'd start with `challenge-assumptions` and revisit after 10 min; or we could jump to `what-if` if you prefer blue-sky"). Never stall.
- **User wants breadth** ("give me options") → route to one generation method first; sequence a second if the first doesn't produce enough variety.
- **User wants depth quickly** ("harden this proposal") → `premortem` or `options-portfolio`; avoid re-opening with `lateral-thinking` unless the proposal is still fluid.
- **Only one method is installed** → still diagnose; run the closest analogue and name the gap explicitly.
