# Generating Guaranteed-Failure Ideas

Inversion only works if the failure routes are concrete. A list of "risks" produces a list of worries; a list of **guarantees** produces design conditions. The generation step is therefore deliberately extreme and deliberately unfiltered.

## Two directions

| Direction | Question | Use when |
|---|---|---|
| **Goal inversion** | "How could we guarantee that ⟨goal⟩ fails?" | You have an outcome you want and need obstacles, failure conditions, and preventive principles |
| **Outcome inversion** | "How could we reliably produce ⟨the unwanted outcome⟩?" | You are designing against a known harm (churn, incidents, misinformation, burnout, lost trust) |

State the goal as a verb phrase first. "Improve onboarding" has no predicate to invert; "get 60% of new accounts to first value within 7 days" does.

## The core prompts

Start with the blunt question and write it on the board:

- **"How would I guarantee failure?"** — Munger's formulation: if you want to fail, what would you do?
- **"What would make this impossible?"** — remove the necessary condition rather than adding an obstacle.
- **"How would a competent adversary make this fail?"** — an actor with goals opposed to yours, not a stupid one.
- **"How would a well-meaning team sabotage this?"** — the failures that need no villain.
- **"What would we do if we were paid to fail?"** — reveals incentive gradients.
- **"What did the last five attempts at this do?"** — reuse observed failure routes before inventing new ones.

For outcome inversion, ask: "What is the cheapest, most reliable recipe for ⟨harm⟩?" A recipe is better than a cause: it forces sequence and mechanism.

## Domain sweep

Generate at least one route per domain, then keep going where the list is thin.

| Domain | Trigger questions |
|---|---|
| **Incentive** | Who is rewarded for the opposite? Who bears the cost of failure? Where is the rational workaround? |
| **Information** | What is never measured? What is measured badly? Who learns about the problem last? |
| **Sequencing** | What must happen before value is delivered — and what if it happens later or never? |
| **Capability** | Which skill, system, or person is load-bearing? What breaks at 3× volume? |
| **Ownership** | Which decision has no owner? Which handoff has two? |
| **Coordination** | Where do teams' definitions of "done" diverge? Which dependency sits on the critical path? |
| **Environment** | Which external condition must hold (market, regulation, platform, supplier)? |
| **Psychology** | What does the user actually attend to? Where does friction exceed motivation? |
| **Measurement** | What proxy replaces the real goal? What does the dashboard hide? |
| **Time** | What decays if nobody maintains it? What is true only at launch? |

## Quality tests for a route

A usable route passes all four:

1. **Mechanism** — it says how failure happens, not that it might. "Support is reactive, so the first bad experience is never fixed" passes; "poor support" fails.
2. **Actor** — someone or something does it: a team, a user, a supplier, a metric.
3. **Specificity** — you could draw the sequence of events on a whiteboard.
4. **Causal distance** — it is upstream of the outcome, not a restatement of it. "We fail because activation is low" is the outcome, not a route.

## Keep the awkward ones

Do not filter for politeness, feasibility, or good taste during generation:

- **Absurd routes** ("delete the product") often isolate the single necessary condition.
- **Unethical routes in fiction** ("make cancellation impossible") reveal why real incentives drift that way.
- **Routes that blame the user** are usually design facts in disguise ("users won't read" means the design depends on reading).
- **Routes that blame leadership** are incentive facts; keep them and convert them in step 5.

Mark anything that is speculation rather than observation. The goal is coverage, not credibility, at this stage.

## Volume and independence

- Target **15–25 routes** for a meaningful goal; 8–12 is a review, not an inversion.
- Write them **before** discussing any of them. A senior voice first anchors the list.
- In a group, collect silently, then round-robin one route per person until exhausted.
- Solo or with an AI, generate in one pass without self-editing, then a second pass with the domain sweep. Two passes beat one polished pass.
- Stop when a new batch only restates existing mechanisms.

## Common failure-generation mistakes

| Mistake | Symptom | Fix |
|---|---|---|
| Generic negativity | "Execution risk," "market risk," "alignment" | Force actor + mechanism; reject labels |
| Disguised solutions | "We fail because we don't do X" where X is the plan | Restate as the condition that is absent and why it stays absent |
| Single-cause collapse | The list is one theme in fifteen costumes | Run the domain sweep |
| Premature ranking | Half the list is discarded mid-generation | Rank only after clustering |
| Missing the boring route | Only dramatic failures appear | Ask what happens on an ordinary Tuesday at 3× scale |
| Ignoring the goal | Routes attack a different goal | Re-read the success definition before each pass |
