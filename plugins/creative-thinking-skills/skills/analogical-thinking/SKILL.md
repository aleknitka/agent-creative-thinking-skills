---
name: analogical-thinking
description: Look for structurally similar problems in other fields and transfer the underlying mechanism — not surface features. Use when another domain may have solved this structurally, ideas feel domain-locked, or you need a transferable principle with limits — not a copy.
---

# Analogical Thinking

Borrow a mechanism, not a metaphor. The failure mode this skill prevents is the surface analogy: two situations share vocabulary or a visual shape, so you copy the visible features and inherit none of the causal machinery that made the source work.

The output is a **transferable principle with stated limits and a probe** — not "we should be more like an airport."

## When to use

- Another field plausibly faces the same *relation* under different constraints.
- Your ideas are all variations of the industry's standard answer.
- A metaphor keeps getting used ("this is our air-traffic control") without anyone checking whether it holds.
- You need a design principle that survives the trip back to your context.

If you only need surprise, use `forced-connections`; if you want to stretch an existing baseline, use `scamper`. See [references/when-not-to-use.md](references/when-not-to-use.md).

## Process

1. **Intake.** State the problem in 3–5 sentences: what happens, who acts, what the goal is, what can change, and the hard constraints. Keep the domain nouns for now; do not solution-hunt.
2. **Abstract to structure.** Rewrite it with the nouns removed as **function, flow, constraint, and feedback**: what transforms, what moves between whom, what bounds the space, what adjusts on error. Aim for 1–3 sentences. See [references/abstraction.md](references/abstraction.md).
3. **Search far domains.** Pick sources by matching that structural signature — not by industry resemblance. Generate 5–8 candidate domains, deliberately including two or three that feel distant. See [references/search-heuristics.md](references/search-heuristics.md).
4. **Map the mechanism.** Align *relations* (causes, sequences, feedback loops), not objects. Write the mapping explicitly: source element → your element → relation it carries. Name the mechanism and the exact place it would plug in. See [references/mapping.md](references/mapping.md).
5. **Check limits and breakpoints.** Find where the source mechanism depends on conditions you lack — scale, incentives, regulation, cost of failure, information quality, time pressure. Mark each dependency as holds, adapt, or fails. See [references/mapping.md](references/mapping.md) and the worked limits in [references/examples.md](references/examples.md).
6. **Harvest a principle and a probe.** State the principle as "when relation X holds, mechanism Y produces Z" plus its boundary conditions. Define the smallest local probe that would test the mechanism, and what result would falsify it.

## Rules

- **Structure before source.** No domain search until step 2 is written down; otherwise you will select a flattering analogy and reverse-engineer the problem to fit it.
- **Relations over objects.** Shared objects are not a mapping. If the analogy only survives by renaming things, it is a metaphor.
- **One or two deep transfers beat ten shallow ones.** Depth means a named causal mechanism plus a breakpoint analysis.
- **Mismatch is the deliverable.** A principle that states where it stops working is more useful than an exact-looking copy.
- **Keep the source honest.** Do not invent how another field works; mark uncertain claims about it as inference.
- **Probe, don't adopt.** The probe is a small reversible test, not a rollout.

## Going deeper

- Abstracting a problem to mechanism (function / flow / constraint / feedback): [references/abstraction.md](references/abstraction.md)
- Choosing and searching far domains, with prompt sets: [references/search-heuristics.md](references/search-heuristics.md)
- Structure mapping, mapping table, and failure modes: [references/mapping.md](references/mapping.md)
- Two worked analogies with limits: [references/examples.md](references/examples.md)
- When not to use this method, and handoffs: [references/when-not-to-use.md](references/when-not-to-use.md)
- Lineage, evidence, and adaptations: [references/provenance.md](references/provenance.md)
- Offline helper — far-domain suggestions and mapping checklist: [scripts/analogy.py](scripts/analogy.py)
