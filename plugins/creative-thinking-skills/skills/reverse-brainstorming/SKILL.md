---
name: reverse-brainstorming
description: Brainstorm ways to make a problem worse, then transform those ideas into possible improvements. Use when ordinary brainstorming has stalled and fixes feel generic — apply inversion specifically to idea generation to produce improvements derived from deliberately bad ideas.
---

# Reverse Brainstorming

Direct brainstorming asks "how do we fix this?" and returns variations of the first idea everyone already had. Reverse brainstorming asks the easier question first: **how could we make this problem worse — reliably, deliberately, even absurdly?** Bad ideas are cheap to produce because nobody has to defend them, and they describe the problem's machinery. Each one is then reversed into a direction for improvement.

The move is not pessimism and not a risk review. It is a different search direction for *ideas*: inversion applied to a problem you already have, where the output is candidate improvements rather than prevention principles. It works because "make it worse" bypasses the social cost of proposing a bad fix, and because the resulting ideas are structurally unlike anything the direct question produces.

The failure mode it prevents is a brainstorm that keeps recombining the same three generic fixes.

## When to use

- Brainstorming has stalled; new ideas are rewordings of the first one.
- Fixes feel generic ("communicate better", "add training", "improve UX").
- A group is polite, flat, or blocked and needs permission to be negative.
- You want fresh improvement directions, not another risk register.
- The problem is well stated but nobody can see what keeps it in place.

If unsure this is the right method, start with [thinking-router](../thinking-router/SKILL.md) — or see [references/when-not-to-use.md](references/when-not-to-use.md).

## When NOT to use (brief)

- A concrete proposal is near commitment and needs hardening → `premortem`.
- You want failure principles with owners and signals → `inversion`.
- You have a baseline product or process to vary → `scamper`.
- You need many independent alternatives without a negativity frame → `brainwriting`, `divergent-thinking`.
- The problem is not understood yet → research or `question-storming` first.

## Process

1. **Intake — reuse before you ask.** State the problem verbatim, then in one sentence each: who has it, what "solved" looks like, hard constraints, and what has already been tried. Keep the problem's own wording; do not soften it into a goal. Mark each input **fact / assumption / speculation** and ask only for what is missing.

2. **Worsen — generate deliberately bad ideas.** Ask **"How could we guarantee this problem gets worse?"** and produce **15–25 specific, unfiltered bad ideas**. Generate independently (silent writing) before anyone speaks, and do not judge, fix, or qualify them. Cover several mechanisms, not one theme in fifteen costumes. See [references/worsening.md](references/worsening.md) and [scripts/reverse.py](scripts/reverse.py).

3. **Cluster by mechanism.** Group the bad ideas by *why they work* — incentive, information, friction, sequence, ownership, capability, coordination, trust, environment, time. Keep **3–6 clusters**, each with a one-line causal story. A cluster that only names a symptom is not a cluster.

4. **Reverse each cluster.** Apply reversal operators — negate the mechanism, invert the actor, remove the precondition, re-scope, reverse the sequence, turn the harm into a signal — and rewrite each cluster as an **improvement direction**: actor + action + condition. "Don't hide errors" is not a reversal; "surface import failures at the point of upload" is. See [references/reversal.md](references/reversal.md).

5. **Enrich and de-risk.** Elaborate the **3–5 strongest directions** into one- or two-sentence concepts with a concrete mechanism, the actor who would do it, its cost, and its most likely failure mode. Kill directions whose reversal is only a platitude or restores the original problem.

6. **Harvest 2–3 concepts.** Give each a first probe, a leading signal, and a kill criterion. Label evidence and open questions. Hand off to `premortem`, `experiment-design`, or `options-portfolio` when those fit better; confirm before running another method. A worked example is in [references/examples.md](references/examples.md).

## Rules

- **Separate worsening from reversing.** No fix may enter step 2; no bad idea may be defended in step 4.
- **Independently generate first.** A senior voice or the first list anchors everyone; collect silently, then share.
- **A bad idea names a mechanism and an actor.** "Poor onboarding" is a label; "require admin approval before the first screen" is an idea.
- **Reversals are actions, not negations.** "Improve communication" fails the test.
- **Bad ideas are fiction.** Worsening may be impolitic or absurd; do not attribute malice to real people or teams, and convert blame into a design fact.
- **Keep the problem fixed.** You are worsening *this* problem, not switching to a different one.
- **Visible uncertainty.** Facts, assumptions, and speculation stay distinct; a reversal is a hypothesis, not a validated fix.
- **Honest provenance.** Attribute Osborn, Eberle, and the inversion tradition; call the workflow here an adaptation. See [references/provenance.md](references/provenance.md).

## Going deeper

- How to generate worsening ideas — prompts, domain sweep, quality tests: [references/worsening.md](references/worsening.md)
- Reversal operators that turn bad ideas into improvement directions: [references/reversal.md](references/reversal.md)
- Workshop flow, timing (worsen 10 min, reverse 15 min, enrich 10 min), solo and AI modes: [references/facilitation.md](references/facilitation.md)
- Worked example ("never onboard" → three improvements with probes): [references/examples.md](references/examples.md)
- When not to use, plus comparisons and handoffs: [references/when-not-to-use.md](references/when-not-to-use.md)
- Lineage, attribution, and evidence limits: [references/provenance.md](references/provenance.md)
- Worsening prompt generator and reversal checklist (offline): [scripts/reverse.py](scripts/reverse.py)
