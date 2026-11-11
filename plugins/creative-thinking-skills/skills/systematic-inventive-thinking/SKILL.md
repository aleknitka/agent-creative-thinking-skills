---
name: systematic-inventive-thinking
description: Apply SIT's five closed-world operators — Subtraction, Multiplication, Division, Task Unification, Attribute Dependency — to transform an existing product or component without adding new resources. Use when you have a concrete system, must innovate inside strict constraints, or want disciplined alternatives to open-ended ideation and tradeoff analysis.
---

# Systematic Inventive Thinking (SIT)

Stay inside the box — then change it. SIT uses five formal operators to mutate what already exists without importing new kinds of resources, so every idea is testable against the current system.

The failure mode it prevents is open-ended variation that is creative but unbuildable, and tradeoff balancing that accepts the current architecture as given.

## When to use

- You have a concrete product, service, or component to improve.
- Constraints are strict: no new headcount, budget, or technology class.
- SCAMPER feels too open-ended; you want five disciplined moves.
- The problem is not a tradeoff to break (TRIZ) but a system to transform.

If unsure this is the right method, start with [thinking-router](../thinking-router/SKILL.md) — or see [references/when-not-to-use.md](references/when-not-to-use.md).

## When NOT to use (brief)

- No concrete system is defined → scope it or use `question-storming`.
- You need breadth before structure → `divergent-thinking` or `brainwriting`.
- The block is a recurring technical contradiction → `triz-contradictions`.
- You need stakeholder or future lenses → `stakeholder-perspectives`, `scenario-planning`.

## Process

1. **Intake — define the closed world.** List the system, its components, and its immediate environment as it exists today (3–5 sentences). Name hard limits that bound the solution. See [references/facilitation.md](references/facilitation.md).

2. **Choose the operator.** Pick one of the five; run one at a time. See [references/operators.md](references/operators.md) and [scripts/sit.py](scripts/sit.py).

3. **Apply the operator to generate a virtual product.** Follow the operator's recipe to produce a seemingly infeasible form — keep it as written before judging. No feasibility filtering yet.

4. **Enrich and make feasible.** Add back the minimal change needed to resolve the infeasibility, often by reassigning value, time, or condition. The change must stay within the closed world or its near environment.

5. **Evaluate.** Check for qualitative change, usefulness, and feasibility. Keep 2–3 candidates; discard variants without a new benefit or that smuggle in a new resource type.

6. **Probe and decide next.** Define the smallest probe, its signal, and the owner. Hand off to `premortem` before commitment or `scamper` for further variation on the chosen candidate. See [references/examples.md](references/examples.md).

## Rules

- Closed world: the list of components and environment is fixed at intake; adding a new kind of resource is not allowed.
- One operator at a time — never blend two virtual products before enrichment.
- Qualitative change required: the virtual product must behave differently, not just have more or less of the same.
- Keep the mechanism visible; an idea without a testable change is a slogan.
- Label fact / assumption / speculation.
- Honest provenance: attribute SIT to Horowitz and Goldenberg; call this workflow an adaptation. See [references/provenance.md](references/provenance.md).

## Going deeper

- The five operators — recipes, prompts, and checks: [references/operators.md](references/operators.md)
- Facilitation — timing, inside-the-box discipline, and solo/AI mode: [references/facilitation.md](references/facilitation.md)
- Worked example (one system → five virtual products → two probes): [references/examples.md](references/examples.md)
- When not to use — triage vs SCAMPER/TRIZ/lateral: [references/when-not-to-use.md](references/when-not-to-use.md)
- Provenance, lineage, and evidence limits: [references/provenance.md](references/provenance.md)
- Operator helper (offline): [scripts/sit.py](scripts/sit.py)
