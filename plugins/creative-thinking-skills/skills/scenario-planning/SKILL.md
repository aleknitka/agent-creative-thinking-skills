---
name: scenario-planning
description: Develop several plausible futures around important uncertainties, then explore how choices would perform in each. Use when future conditions are uncertain — produce scenarios, robust options, and signals to watch. Scenarios are possibilities, not predictions.
---

# Scenario Planning

Do not forecast one future. Build several plausible ones, test your choices in each, and keep the options that stay valuable across them.

Scenarios are possibilities, not predictions.

The failure mode it prevents is locking to a single forecast while uncertainty quietly owns the outcome.

## When to use

- The future is uncertain on dimensions that change what "good" means.
- A decision must be robust across several plausible worlds.
- You need scenarios, robust options, and signals to watch.

If unsure this is the right method, start with [thinking-router](../thinking-router/SKILL.md) — or see [references/when-not-to-use.md](references/when-not-to-use.md).

## When NOT to use (brief)

- The future is relatively predictable → plan, not scenario.
- You need the route to one desired future → `backcasting`.
- You need ripple effects of one change → `futures-wheel`.

## Process

1. **Intake — reuse before you ask.** State the focal question, time horizon, stakeholders, and what is at stake. Mark fact / assumption / speculation. See [references/uncertainties.md](references/uncertainties.md).

2. **Name uncertainties.** List driving forces, then rank by impact × uncertainty. Keep the top 2 as axes; the rest are wildcards. See [references/uncertainties.md](references/uncertainties.md) and [scripts/scenarios.py](scripts/scenarios.py).

3. **Build 2–4 scenarios.** Use the two top uncertainties as a 2×2; name each quadrant as a distinct plausible world (not best/worst). Keep each to 3–5 sentences. Wildcards are noted but not multiplied.

4. **Test options across scenarios.** For each candidate choice, score how it performs in each world. Keep options that are robust or option-rich across scenarios; mark brittle bet-on-one-future choices.

5. **Name signals and triggers.** For each scenario, define leading indicators that the world is moving that way. See [references/implications.md](references/implications.md).

6. **Choose and monitor.** Select robust options plus cheap options that hedge. Define the monitoring cadence and the trigger for a course correction. See [references/examples.md](references/examples.md).

## Rules

- Scenarios are not forecasts — keep them plausible, not probable.
- Two axes only for the 2×2; more axes produce more scenarios than anyone can use.
- Every option is tested in every scenario; a scenario without implications is just a story.
- Name signals that would actually be observable.
- Label fact / assumption / speculation.

## Going deeper

- Uncertainties — driving forces, ranking: [references/uncertainties.md](references/uncertainties.md)
- Scenarios — 2×2 construction and world sketches: [references/scenarios.md](references/scenarios.md)
- Implications — scoring options, robust vs brittle: [references/implications.md](references/implications.md)
- Worked example (2×2 → 4 worlds → robust options): [references/examples.md](references/examples.md)
- When not to use + triage: [references/when-not-to-use.md](references/when-not-to-use.md)
- Provenance and lineage: [references/provenance.md](references/provenance.md)
- Scenario helper (offline): [scripts/scenarios.py](scripts/scenarios.py)
