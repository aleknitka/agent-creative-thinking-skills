# Inverting Back to Design Principles

The payoff of inversion is not the failure list. It is the set of **positive, testable principles** that the failure routes imply. A principle is a standing design condition, not a one-time fix.

## The transformation

For each cluster, run three steps:

1. **Negate the mechanism.** "No one owns activation" becomes "activation has a named owner."
2. **Make it positive and operational.** "Have an owner" becomes "assign one owner per activation step, with a weekly review of the drop-off."
3. **Make it testable.** Add the observable signal and the decision it changes: "signal: step-level conversion reviewed weekly; decision: the owner can change onboarding copy without a release."

If step 3 cannot be completed, you have a slogan, not a principle.

## What a principle contains

| Field | Content | Example |
|---|---|---|
| **Rule** | Positive imperative, one sentence | "Deliver first value before asking for configuration." |
| **Failure route** | The cluster it inverts | "Setup work precedes any value, so users abandon before seeing it." |
| **Signal** | What you would observe if the principle is violated | "Time-to-first-value rises while setup completion falls." |
| **Owner / decision** | Who acts, and what they are allowed to change | "Onboarding PM can reorder steps without a release." |
| **Trade-off** | What the principle costs | "Some configuration moves after first value and must be deferred gracefully." |

The trade-off field matters: a principle with no cost is probably a platitude.

## Good and bad rewrites

| Failure route | Bad principle | Good principle |
|---|---|---|
| Activation has no owner | "Don't neglect activation." | "One owner per activation step; weekly drop-off review with authority to change copy." |
| Setup precedes value | "Make onboarding easier." | "First value within the first session; defer non-essential setup behind a working default." |
| Success is measured as signups | "Measure the right thing." | "Primary metric is 7-day first value, not signup; review it as the launch gate." |
| Support is reactive | "Improve support." | "In-product help at the first two failure points; support tags every activation ticket by step." |
| Accounts arrive without a job | "Target better customers." | "Qualify accounts by an explicit job-to-be-done before onboarding; route the rest to self-serve." |

The bad column restates the failure or names a virtue. The good column names a design condition with an observable consequence.

## Types of principle

- **Structural** — order, defaults, gating, interface ("value before configuration").
- **Informational** — measurement, telemetry, review cadence ("tag every activation ticket by step").
- **Incentive** — who is rewarded for what ("launch gate is first value, not signups").
- **Capability** — skills, capacity, tooling ("onboarding copy changes ship without a release").
- **Selection** — who enters the process at all ("qualify by job-to-be-done").

Most clusters invert into one type; some need two principles (a structural condition plus the measurement that keeps it honest).

## Quality tests

A principle is ready when all five hold:

1. **Actionable** — someone could start tomorrow.
2. **Falsifiable** — a signal would show it is being violated.
3. **Non-trivial** — it changes a decision, order, incentive, or design, not just a document.
4. **Mechanism-linked** — it traces to one cluster and one failure route.
5. **Bounded** — it says where it stops or what it costs; otherwise it becomes an unbounded aspiration.

Reject principles that are:
- the failure negated without an action ("don't lose users");
- a restatement of the goal ("succeed at onboarding");
- a checklist item with no owner or signal;
- a slogan that every team would already claim to follow.

## How many

Keep **3–6**. Fewer means the clusters were thin; more means you are writing tactics. Tactics are fine — put them under the principle that justifies them. If a cluster yields no principle, say so explicitly and mark it as an accepted unknown rather than inventing one.

## From principle to probe

Not every principle deserves immediate action. Rank by:

- **Load-bearing** — if violated, would the other principles matter?
- **Cheap to test** — can you observe the signal within days?
- **Reversible** — can you undo the change?

Take the top one or two into the probe step: smallest change, leading indicator, kill criterion. A principle without a probe is a hope; a probe without a principle is a random experiment.

## Principles vs rules of thumb

A principle should be specific enough to violate. "Be user-centred" cannot be violated in a way you would notice. "First value before configuration" can be — and when it is, you will see it in time-to-value. Prefer the second kind.
