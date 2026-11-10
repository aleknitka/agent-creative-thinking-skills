---
name: triz-contradictions
description: Frame a challenge as a contradiction — improving one property worsens another — and use inventive principles or separation strategies to seek alternatives to the tradeoff. Use when a recurring technical tradeoff blocks progress — produce a contradiction statement and candidate ways to resolve it.
---

# TRIZ Contradiction Thinking

Name the tradeoff that keeps recurring, state it as a contradiction, and seek ways to break it — not balance it. Improving one property should not have to worsen the other.

The failure mode it prevents is accepting a tradeoff as inevitable while alternatives exist outside the current design's assumptions.

## When to use

- Improving one property reliably worsens another — the tradeoff recurs.
- The team has tried balancing and the result keeps disappointing both sides.
- You need a contradiction statement and candidate ways to resolve it.

If unsure this is the right method, start with [thinking-router](../thinking-router/SKILL.md) — or see [references/when-not-to-use.md](references/when-not-to-use.md).

## When NOT to use (brief)

- No recurring technical tradeoff is visible → another method fits better.
- The tradeoff is between stakeholder needs, not technical properties → `stakeholder-perspectives`.
- Near commitment → `premortem`.

## Process

1. **Intake — reuse before you ask.** State the system, its purpose, and the tradeoff that recurs. Mark fact / assumption / speculation. See [references/contradiction.md](references/contradiction.md).

2. **State the contradiction.** Write: if we improve [A], then [B] worsens, because [mechanism]. Distinguish technical contradiction (two properties) from physical contradiction (one property must be both X and not-X). See [references/contradiction.md](references/contradiction.md) and [scripts/triz.py](scripts/triz.py).

3. **Apply separation or principles.** Try separation by space, time, condition, or scale. For inventive principles, scan the 40 for candidates that address improving A without harming B. See [references/principles.md](references/principles.md) and [references/separation.md](references/separation.md).

4. **Generate candidate resolves.** For each promising principle or separation, sketch one concrete design that breaks the tradeoff — mechanism, not slogan.

5. **Evaluate ideality.** Rank candidates by how much of the benefit is preserved, cost added, and harm introduced. Keep those that move toward ideal final result.

6. **Probe.** Choose the closest practical resolve and define its signal and decision rule. See [references/examples.md](references/examples.md).

## Rules

- State the contradiction observably — property A and property B, with mechanism.
- Separate technical from physical contradictions; the method differs.
- Every candidate must be a design, not a restatement of the tradeoff.
- Label fact / assumption / speculation.
- Honest provenance: attribute TRIZ to Altshuller. See [references/provenance.md](references/provenance.md).

## Going deeper

- Contradiction — technical vs physical, statement template: [references/contradiction.md](references/contradiction.md)
- Inventive principles — scanning the 40: [references/principles.md](references/principles.md)
- Separation — space, time, condition, scale: [references/separation.md](references/separation.md)
- Worked example (speed vs accuracy tradeoff → resolves): [references/examples.md](references/examples.md)
- When not to use + triage: [references/when-not-to-use.md](references/when-not-to-use.md)
- Provenance and lineage: [references/provenance.md](references/provenance.md)
- TRIZ helper (offline): [scripts/triz.py](scripts/triz.py)
