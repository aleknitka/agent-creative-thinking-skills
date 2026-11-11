---
name: thinking-router
description: Choose the most fitting creative-thinking method for your problem. Use when unsure which technique to use, when a problem could be framed many ways, or when you say "help me think creatively / pick a method / what should we try next" — it diagnoses intent and routes to 1-2 methods from 38 (27 base + 11 extended), then hands off.
---

# Thinking Router

You have 38 methods but one next step. This skill prevents method-shopping and premature commitment — it diagnoses what you actually need, then routes with you to the best-fitting 1-2 methods.

## Process

1. **Intake — reuse before you ask.** Capture in one sentence each: the stated problem, the real goal, hard constraints, what has already been tried, and appetite for unconventional ideas (low / medium / high). Use available context first; ask only what is missing. See [references/diagnostic.md](references/diagnostic.md).

2. **Triage the need.** Map the situation to one primary need:
   - **Better question** — problem is vague, overconstrained, or prematurely solution-focused
   - **More ideas** — you have a starting point and need varied alternatives
   - **Broader perspectives** — future, stakeholders, or side-effects matter
   - **Stronger options** — you have candidates and need to stress-test and choose
   Details: [references/routing-logic.md](references/routing-logic.md).

3. **Score and shortlist.** Using the signals from step 2, score the 38 methods in [references/catalog.md](references/catalog.md) and keep the top 2-3. Prefer methods whose trigger matches best and whose output matches the artifact you need next. Break ties toward the Suggested first 8.

4. **Recommend with tradeoffs.** Present:
   - **Primary** — what it does in one line, why it fits, what you will get, time/effort
   - **Alternate** — when you would pick this instead
   - **Not now** — the strongest contender you are deliberately skipping and why
   Keep generation separate from evaluation; tag speculative claims.

5. **Co-decide and hand off.** Ask the user to confirm, adjust constraints, or swap. On agreement, invoke the chosen skill/workflow directly (or give its one-line invocation for Codex/Claude Code) and pass the intake + routing note as context. If the user wants to stay, run a light first pass of the routed method inside this session. See [references/handoff.md](references/handoff.md).

## Rules

- Decide *with* the user, not for them. Never auto-run a routed method without confirmation.
- If signals are mixed, offer a portfolio pair (e.g., reframe + ideate) or the Double Diamond sequence rather than forcing one.
- Distinguish facts, assumptions, and speculation; do not present invented examples or simulated stakeholder views as evidence.
- Honest provenance: name the method's origin; call adaptations adaptations.
- When only one method is installed, still diagnose — then run its closest available analogue and note the gap.

## Going deeper

- Full method catalog (38: 27 base + 11 extended, with triggers and outputs): [references/catalog.md](references/catalog.md)
- Diagnostic questions and intake template: [references/diagnostic.md](references/diagnostic.md)
- Routing logic, decision tree, and scoring: [references/routing-logic.md](references/routing-logic.md)
- Worked routing examples: [references/example.md](references/example.md)
- Handoff and sequencing patterns: [references/handoff.md](references/handoff.md)
- Runnable helper: [scripts/route.py](scripts/route.py)
- Agent workflows — parallel (brainwriting) and sequential (six hats): [workflows/brainwriting-workflow.md](../../workflows/brainwriting-workflow.md), [workflows/six-thinking-hats-workflow.md](../../workflows/six-thinking-hats-workflow.md)
- Shared workspace — sticky notes, lanes, drawing, votes: [workspace/index.html](../../../../workspace/index.html)
