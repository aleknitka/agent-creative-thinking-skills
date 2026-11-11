# Handoff and Sequencing

## How to hand off well

A handoff is a one-paragraph routing note. Write it so the next method can start without re-asking the user.

**Routing note template:**

```
Via thinking-router — Need: <better question | more ideas | broader perspectives | stronger options>
Method: <primary> (alt: <alternate>)
Trigger match: <why>
Intake: <one-line problem + goal + constraints + appetite + time>
Next artifact: <what the next method should produce>
```

In **Claude Code**, invoke the skill directly. With the current repo layout:

```
Skill tool: thinking-router hands off to, e.g., divergent-thinking
Pass the routing note as the first message to the next skill
```

In **Codex** or other hosts, give the user the invocation verbatim and the routing note to paste.

If the user prefers to stay in the router session, run a *light first pass* of the routed method (one round of its process) and offer to continue or switch.

## Sequencing patterns (when one method is not enough)

| Situation | Sequence | Why |
|---|---|---|
| Vague brief, then need ideas | `question-storming` → `scamper` / `analogical-thinking` / `crazy-eights` | Fix the question first, then diverge |
| Stuck despite good framing | `lateral-thinking` → `scamper` | Break the dominant idea, then systematize variations |
| Many dimensions | `morphological-analysis` → `concept-blending` → `options-portfolio` | Map the space → synthesize → choose a portfolio |
| Bold vision, no route | `what-if` → `backcasting` | Explore worlds, then walk backward to milestones |
| Uncertain futures | `scenario-planning` → `premortem` / `options-portfolio` | Make choices robust, then harden them |
| Critique kills ideation | `six-thinking-hats` (Green isolated) or `brainwriting` first | Protect generation before evaluation |
| Tradeoff loop | `triz-contradictions` → `premortem` | Resolve the contradiction before hardening |
| Needs discovery + delivery | `double-diamond` orchestrating any of the above | Full discover-define / develop-deliver loop |

Prefer **one handoff at a time**. Only propose a sequence when the user's time budget allows it — say so explicitly.

## What to do when there is no installed skill for the top pick

1. Name the gap honestly ("`triz-contradictions` isn't installed; here's the closest analogue").
2. Run the analogue and carry the routing note forward.
3. Suggest installing or authoring the missing skill when the user has time.

Example analogue map:

| Top pick not installed | Run instead |
|---|---|
| `lateral-thinking` | `divergent-thinking` + lenses (invert, constrain, borrow) |
| `question-storming` / `abstraction-laddering` | `challenge-assumptions` prompts |
| `scenario-planning` / `backcasting` / `futures-wheel` | `what-if` + structured "consequences" trace |
| `triz-contradictions` | `options-portfolio` with contradiction explicitly named |
| `concept-blending` | manual synthesis from `scamper` outputs |
| `six-thinking-hats` | isolate generation (no critique) then structured black-hat pass (`premortem`) |

## Confirm before you run

End every routing recommendation with an explicit choice:

> "Want to go with **primary**, swap to **alternate**, or adjust the constraints/time/appetite and reroute?"

Never auto-run without a yes.

## Provenance note

Name the origin when you hand off (e.g., "de Bono — lateral thinking," "Altshuller — TRIZ," "Osborn — brainwriting roots of SCAMPER"). It helps the user decide how much weight to give the scaffold.
