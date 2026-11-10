---
name: premortem
description: Imagine a proposed project has already failed, then generate plausible reasons and work backward to prevention. Use after initial ideation, before commitment — produce failure hypotheses, warning signs, and changes that strengthen the idea while it can still be shaped.
---

# Premortem

A postmortem explains a failure after the fact. A premortem assumes the failure has already happened — then uses that certainty to surface the doubts people withhold while a plan is still being praised.

The failure mode it prevents is the plan everyone privately doubts but nobody names until it is too late to change.

## When to use

- A concrete proposal exists — a launch, migration, reorg, or campaign — and commitment is near.
- The plan has momentum or a confident sponsor, and dissent feels socially costly.
- You want risks tied to **changes in the plan**, not a generic risk register.

If unsure this is the right method, start with [thinking-router](../thinking-router/SKILL.md) — or see [references/when-not-to-use.md](references/when-not-to-use.md).

## When NOT to use (brief)

- No concrete proposal yet — ideation is still open → diverge first; premature critique kills fragile ideas.
- You need in-session caution while exploring a topic → Black hat of `six-thinking-hats`.
- Safety-critical, quantified hazards → formal FMEA / HAZOP / technical risk assessment.
- The decision is locked and nothing can change → track risks, then run a postmortem.

## Process

1. **Intake — reuse before you ask.** Write the proposal in 3–5 sentences: what ships, for whom, by when, who commits resources, the success measure, and hard constraints. Set a failure horizon (e.g., six months after launch). If the proposal is vague, narrow it before proceeding.

2. **Declare the failure scene.** State it in the past tense, unhedged: "It is ⟨date⟩. ⟨Proposal⟩ failed." Add 2–3 sentences of scene — what the failure looks like in numbers, behaviour, and headlines. Never soften it to "underperformed." See [scripts/premortem.py](scripts/premortem.py) for a scene template.

3. **Generate plausible reasons independently.** Everyone silently writes 8–12 reasons **before** any discussion — especially the impolitic ones. Use the five categories as prompts: assumption, coordination, incentive, capability, external. Label facts, assumptions, and speculation. See [references/failure-modes.md](references/failure-modes.md) and [references/facilitation.md](references/facilitation.md).

4. **Cluster.** Merge duplicates, group by causal mechanism (not by department), and give each cluster a one-line causal story ("we measured signups, so nobody owned activation"). Expect 3–6 clusters from 30+ raw reasons.

5. **Prioritize by likelihood × impact.** Score each reason 1–5 on each axis, rank by the product, and keep the top 3–5. For every survivor, name the **warning signal** — the earliest observable indicator that this failure is underway. See [references/prioritization.md](references/prioritization.md).

6. **Harden.** For each top reason, add a **prevention** that changes the plan now and a **monitor** with a threshold, owner, and response. Record accepted risks explicitly. Confirm that at least one change alters the plan, not just the document. See [references/examples.md](references/examples.md).

## Rules

- The failure is asserted, not debated. Ask "why did it fail?", never "will it fail?".
- Generate before discussing — no anchoring on the sponsor's or the loudest person's list.
- Keep facts, assumptions, and speculation labelled; a premortem yields hypotheses, not evidence.
- Reasons must name a mechanism ("CS was measured on ticket closure"), not a label ("execution risk").
- Critique the design, not the author. No blame, no defending the plan.
- Hardening must change likelihood, detectability, or blast radius — not add a checklist item.
- Honest provenance: attribute the method to Klein; call adaptations adaptations. See [references/provenance.md](references/provenance.md).

## Going deeper

- Failure-mode categories and trigger questions: [references/failure-modes.md](references/failure-modes.md)
- Facilitation — independent generation, anti-anchoring, solo/AI mode: [references/facilitation.md](references/facilitation.md)
- Prioritization — scoring anchors, warning signals, tripwires: [references/prioritization.md](references/prioritization.md)
- Worked example (onboarding launch fails at six months): [references/examples.md](references/examples.md)
- When not to use + handoff map: [references/when-not-to-use.md](references/when-not-to-use.md)
- Provenance and evidence limits: [references/provenance.md](references/provenance.md)
- Failure-scene template generator (offline): [scripts/premortem.py](scripts/premortem.py)
