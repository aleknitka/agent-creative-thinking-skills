---
name: abstraction-laddering
description: Move upward by asking "why does this matter?" and downward by asking "how could this happen?" to explore different levels of a problem. Use when framing is too narrow or too abstract — produce connected goals, problem frames, and concrete interventions at multiple levels.
---

# Abstraction Laddering

Problems get stuck at one altitude. Too low, and every answer is a patch: "fix the signup form," "add a reminder," "make the button blue." Too high, and every answer is a slogan: "improve belonging," "delight users," "be more strategic." Neither level can be tested, and the two do not connect.

Abstraction laddering moves deliberately between levels, using **why** questions to climb toward purpose and **how** questions to descend toward mechanism. The output is not a single answer but a coherent ladder: goals at several altitudes, each connected to a concrete intervention you can run.

## When to use

- The problem statement is a solution in disguise or a tactical patch.
- The goal is abstract language with no mechanism or next action.
- Stakeholders argue past each other from different levels (vision vs. ticket).
- You need a reframe that stays connected to what is actionable.
- You must decide *where* to intervene, not just what to do.

If unsure whether this is the right method, start with [thinking-router](../thinking-router/SKILL.md) — or see [references/when-not-to-use.md](references/when-not-to-use.md).

## When NOT to use (brief)

- Hidden beliefs and inherited constraints block the options → `challenge-assumptions`.
- You need many new ideas once the frame is sound → `lateral-thinking` or `scamper`.
- You are diagnosing why an observed failure happened → causal analysis (five whys, fault tree), not this.
- The problem is correctness-bound (proof, safety sequence, compliance) → vertical / critical thinking.
- A decision is already framed and options must be compared → `premortem` / options portfolio.

## Process

1. **Intake — capture the rung you were handed.** Write the statement **verbatim**, then in one sentence each: the goal it is supposed to serve, the evidence behind it, who owns the outcome, and the current altitude (too narrow / too abstract / mixed). Do not clean up the phrasing yet; you need the starting rung. Reuse existing context and ask only for gaps.

2. **Ladder up (why).** Ask **"Why does this matter?"** and **"What is this in service of?"** three to five times. Each answer must be a goal or outcome, not a restated solution. Stop when a further why adds no new stakeholder or purpose, becomes universal ("so people are happy"), or leaves the scope you can influence. Record the stop reason. Method and stop rules: [references/laddering.md](references/laddering.md).

3. **Ladder down (how).** From the chosen higher rung ask **"How could this happen?"** and **"What would have to be true?"** Decompose into mechanisms, conditions, and actions — not a task list. Each step down should be a plausible cause or enabling condition of the rung above. Stop at something observable and testable. Levels and their signatures: [references/levels.md](references/levels.md).

4. **Map the levels.** Put every rung in one column, high to low, and label it: **vision / purpose / function / mechanism / action**. Then check vertical coherence: does each lower rung plausibly serve the one above? Flag gaps (a goal with no mechanism), leaps (a tactic attached to a distant vision), contradictions (two rungs that do not imply each other), and orphans (actions serving no stated goal). A ladder is a chain of implication, not a pile of statements.

5. **Choose the leverage point.** Score candidate rungs on **impact** (how much changes if this moves), **controllability** (can you actually act here), and **evidence** (how well supported the link is). Prefer a rung where all three are adequate, then design the intervention at that level and one supporting move above or below it. Do not aim only high (noble, untestable) or only low (testable, irrelevant). Selection guide: [references/leverage.md](references/leverage.md).

6. **Probe.** Turn the chosen intervention into an observable test: what changes, for whom, by when, and what result means keep / adjust / abandon. State the assumption the rung depends on and the cheapest way to check it. If the probe fails, return to step 2 or 3 — the ladder usually shows which link was wrong. Worked example: [references/examples.md](references/examples.md).

## Up or down?

Go **up** when the statement is a solution looking for a problem, when local fixes keep recurring, or when you cannot say what the work is *for*.

Go **down** when the goal is real but vague, when agreement exists on the goal but not the mechanism, or when the next step is unclear.

Go **both** when the ladder is broken in the middle: the vision and the tickets do not imply each other. Ladder down from the goal and up from the action until the two chains meet.

## Rules

- Ask **why** about purpose, never about cause. "Why did signup drop?" is diagnosis; "Why does signup matter?" is laddering.
- Every up-answer must be a goal, not a rewording of the solution. "Because we need a better form" is not a purpose.
- Every down-answer must be a mechanism or enabling condition, not an owner or a deadline.
- Do not skip rungs. A jump from vision to ticket hides the missing function level — that gap is often the finding.
- Keep the original statement verbatim in the artifact; reframing is a step, not a silent substitution.
- Label **fact / assumption / speculation**; a ladder built on unlabeled guesses is a plausible story, not an analysis.
- Choose leverage honestly: impact without control is fantasy; control without impact is busywork.
- Honest provenance: distinguish the classical technique from this adaptation. See [references/provenance.md](references/provenance.md).

## Going deeper

- Laddering technique — why-up / how-down, prompts, and when to stop: [references/laddering.md](references/laddering.md)
- Levels — vision, purpose, function, mechanism, action and their signatures: [references/levels.md](references/levels.md)
- Leverage — scoring and choosing the intervention level: [references/leverage.md](references/leverage.md)
- Worked example — "fix signup" ↔ "belonging": [references/examples.md](references/examples.md)
- When not to use + triage against related methods: [references/when-not-to-use.md](references/when-not-to-use.md)
- Provenance, lineage, and evidence limits: [references/provenance.md](references/provenance.md)
- Prompt helper (offline): [scripts/ladder.py](scripts/ladder.py)
