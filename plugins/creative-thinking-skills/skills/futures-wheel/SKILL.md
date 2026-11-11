---
name: futures-wheel
description: Map a change's immediate consequences, then the consequences of those consequences — including both opportunities and unintended effects. Use when an idea could have broad ripple effects — produce a map of first-, second-, and later-order possibilities.
---

# Futures Wheel

Put the change in the center. Ring it with first-order consequences. Ring each of those with second-order effects. Keep going until the map starts restating itself.

The failure mode it prevents is seeing only the intended effect while second- and third-order consequences arrive unpriced.

## When to use

- A change could have broad or delayed effects.
- You need the ripple map before you commit.
- Unintended effects are the real risk, not the intended one.

If unsure this is the right method, start with [thinking-router](../thinking-router/SKILL.md) — or see [references/when-not-to-use.md](references/when-not-to-use.md).

## When NOT to use (brief)

- The future is uncertain across many worlds → `scenario-planning`.
- You need the route to one desired future → `backcasting`.
- You need failure causes before commitment → `premortem`.

## Process

1. **Intake — reuse before you ask.** State the central change in one sentence, whose change it is, and the horizon. Mark fact / assumption / speculation. See [references/mapping.md](references/mapping.md).

2. **First-order consequences.** List 5–8 direct effects — behavioral, economic, social, environmental — including opportunities and harms. Keep each to one sentence with an actor. See [references/mapping.md](references/mapping.md) and [scripts/wheel.py](scripts/wheel.py).

3. **Second-order consequences.** For each first-order, list 2–3 consequences of that consequence. Keep the map honest: include what gets worse, not just benefits.

4. **Third-order and later.** For the strongest branches, add one more ring. Stop when a ring produces only restatements or speculation without a mechanism.

5. **Name opportunities and risks.** For each branch, mark the opportunity, the unintended effect, and the feedback loop it may create.

6. **Prioritize signals.** Choose the 2–3 most load-bearing branches and define a leading indicator per branch that would tell you early which effect dominates. See [references/examples.md](references/examples.md).

## Rules

- Keep each consequence to one sentence with an actor — "users churn" is not an entry.
- Include opportunities and harms at every ring; one-sided wheels hide the real risk.
- Name feedback loops where a consequence feeds back on the center.
- Stop when restatements appear — not every branch goes three rings.
- Label fact / assumption / speculation.
- Honest provenance: call adaptations adaptations. See [references/provenance.md](references/provenance.md).

## Going deeper

- Mapping — center, rings, notation: [references/mapping.md](references/mapping.md)
- Consequences — first/second/third order, feedback: [references/consequences.md](references/consequences.md)
- Worked example (one change → three rings): [references/examples.md](references/examples.md)
- When not to use + triage: [references/when-not-to-use.md](references/when-not-to-use.md)
- Provenance and lineage: [references/provenance.md](references/provenance.md)
- Wheel helper (offline): [scripts/wheel.py](scripts/wheel.py)
