# Testing — Falsify, Remove, Reverse

Testing a belief is not asking whether it sounds reasonable. It is asking what would count as evidence against it, then getting as close to that evidence as the budget allows.

Do not test the whole inventory. Rank first.

## Rank: impact × uncertainty

Score each belief 1–3 on two axes:

- **Impact** — how much of the option space closes if the belief holds, or opens if it does not. 1 = cosmetic; 3 = blocks every alternative.
- **Uncertainty** — how little you actually know. 1 = verified fact; 3 = pure convention with no evidence.

Prioritize score ≥ 6. A high-impact belief you are certain about is a constraint to design around, not a test target. A low-impact belief you are unsure about is trivia. One or two very high-impact beliefs are often enough to reframe the problem.

| | Low uncertainty | Medium | High uncertainty |
| --- | --- | --- | --- |
| **High impact** | Design around it; record the evidence | Test now | Test now |
| **Medium impact** | Accept and monitor | Test if cheap | Test if cheap |
| **Low impact** | Ignore | Ignore | Ignore |

## The three tests

For each prioritized belief, run all three. They probe different failures: a belief can be true yet unnecessary, or false yet harmless.

### 1. Falsification test — "What would prove this wrong?"

Turn the belief into a prediction and look for the cheapest observation that could contradict it.

Steps:

1. Restate as a prediction: "If A3 is true, then we should observe ___."
2. Name the disconfirming observation: "We would be surprised to see ___."
3. Find the cheapest place that observation already exists: analytics, tickets, contracts, logs, prior experiments, one person who does the work.
4. Decide in advance what result would count as refutation.

Example: "New users cannot reach value without a tutorial." Prediction: users who skip the tour fail to activate. Disconfirming observation: a cohort with the tour dismissed still reaches the activation event at similar rates. Existing data may already answer this — check before designing a study.

Beware the confirmation reflex: a handful of examples that fit the belief is not evidence, especially when nobody counted the cases that did not fit.

### 2. Unnecessary test — "If this disappeared, would the goal still be met?"

Some beliefs are true but not load-bearing. The step exists, the rule is enforced, the approval happens — and yet the goal could be met without it, or with a much lighter version.

Steps:

1. State the goal the belief is supposed to serve.
2. Remove the belief in thought: describe the process or design without it.
3. Ask which harm actually appears. If the harm is speculative, name the mechanism and who bears it.
4. Try a bounded exception: one customer segment, one week, one low-risk case.

The question is not "is this useful?" but "is this necessary for *this* goal at *this* cost?" Many controls are useful in general and unnecessary in the specific case.

### 3. Reversal test — "What if the opposite were true?"

This is the generative test. Assume the belief is false or inverted and see what becomes possible. Reversal does not require believing the inversion; it is a structured way to find options the current frame hides.

Steps:

1. Write the strict negation: "onboarding must be a tutorial" → "onboarding must not be a tutorial."
2. Write the functional inversion: "the user is taught the product" → "the product teaches itself / the user teaches the product."
3. Ask what mechanism would make the inversion work, even badly.
4. Keep the mechanisms that survive; discard the theater.

Reversal is where this skill meets idea generation, but the output here is a *candidate reframe*, not a finished idea. Move to `reframe-patterns.md` for the structured forms, and to `lateral-thinking` or `scamper` if you need many directions.

## Evidence discipline

### Hierarchy (roughly, strongest first)

1. **Direct observation / instrumented behavior** — logs, analytics, transaction records, test results.
2. **Primary documents** — contracts, regulations, policies, schemas, price lists.
3. **Structured interviews with the people who do the work** — what they actually do, not what they say the rule is.
4. **Domain expert judgment** — useful for narrowing, weak as proof.
5. **Analogy, anecdote, and intuition** — hypothesis generators only.

Higher is not always affordable. The rule is to know which level you are standing on and label it.

### Labels

Tag every claim in the working artifact:

- **Fact** — verified in a source you can cite.
- **Assumption** — currently believed, untested or partly tested.
- **Speculation** — a guess offered to generate options.

Never upgrade a label because a claim is repeated or because a senior person said it. Promotion requires evidence.

### Common evidence traps

- **Survivorship** — talking only to users who completed the flow.
- **Anecdote as base rate** — three complaints do not establish prevalence.
- **Policy vs. practice** — the written rule and the actual workaround often differ; ask to see the workaround.
- **Stated vs. revealed preference** — what people say they want versus what they choose when it costs them something.
- **Frozen metrics** — a dashboard that has not been checked against the underlying events.
- **Vendor documentation as capability** — "the platform supports it" may mean an enterprise tier or a future release.

## Probe sizing

Choose the smallest probe that can change a decision. Size by the decision at stake, not by what would be scientifically ideal.

| Tier | Typical cost | Good for | Examples |
| --- | --- | --- | --- |
| Desk check | 15–60 min | Beliefs with existing evidence somewhere | Query analytics; read the contract clause; inspect the schema; search tickets |
| One conversation | 30–60 min | Stakeholder and practice beliefs | Ask the operator how exceptions are handled; ask one customer to walk through the last time |
| Prototype / dry run | Half a day to a week | Necessity and continuity beliefs | Clickable flow with the step removed; manual run of the process for one case; role-play the approval |
| Bounded pilot | One to four weeks | High-impact beliefs that only real use can settle | One segment, one market, feature flag, manual concierge version |

If the cheapest probe costs more than the decision is worth, do not probe — decide under uncertainty, state the assumption, and set a review trigger.

## Decision rules

Write the interpretation *before* running the probe. Otherwise every result becomes confirmation.

Template:

> If we observe **X**, we keep the belief and stop testing it.
> If we observe **Y**, we reframe around its absence.
> If we observe **Z**, the probe was inconclusive; we either accept the belief provisionally or run the next tier.

Example: "If ≥60% of tour-dismissing users still reach the activation event within 7 days, drop the mandatory tour. If 30–60%, run a task-based onboarding prototype. If <30%, keep the tour and investigate step-level drop-off."

A probe with no decision rule is activity, not evidence.

## Guardrails

- Never test a safety, legal, privacy, or financial-control assumption in production. Use a desk check, a dry run with synthetic data, or the accountable expert.
- Do not run an experiment whose failure harms people who did not consent to being experimented on.
- Do not let a successful probe over-generalize: one segment, one week, one version. State the scope of what you learned.
- Record negative results. A refuted belief is a durable asset; an unrecorded one gets re-litigated next quarter.
- Stop when the decision is clear. More evidence past that point is procrastination with a dashboard.

Next: turn surviving load-bearing beliefs into reframes in `reframe-patterns.md`.
