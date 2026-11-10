# Stripping to Fundamentals

The goal is not "no constraints". It is the smallest set of constraints that any acceptable solution must satisfy, plus the outcome that defines success. Everything else is either a consequence, a description of the incumbent, or a choice.

## Decompose the statement first

- **Separate outcome from solution.** Replace artifact nouns with the change they are supposed to produce: "onboarding wizard" becomes "new user reaches first value"; "approval committee" becomes "spend stays within budget while decisions are timely".
- **Split compounds.** "Must be fast and cheap" is two claims with different evidence. "Must be secure and easy" is at least two invariants and a preference.
- **Separate the job from the implementation.** "Because we use vendor X" describes a choice, not a requirement. Ask what job vendor X is doing.
- **Work backward from the value moment.** What must be true at the instant the outcome occurs? Which of those things are prerequisites, and which are ceremony?

## The why-ladder

For each candidate constraint, ask "why must this be true?" and record the answer verbatim. Then ask it again of the answer, up to three to five levels.

Stop when the answer is one of:

- a physical or engineering limit with a measurement and conditions;
- an external obligation with an owner and a text;
- a resource ceiling with a number, period, and controller;
- an invariant with a named failure mode;
- a decision: "someone chose this". Mark it inherited and record the owner and date if known.

If the answer is "that's how we do it", you have found an inherited constraint, not a foundation. If the answer is another policy, keep climbing.

### Avoiding infinite regress

The why-ladder is a tool, not a cosmology exercise. It becomes useless when it turns into "why is there anything at all".

- **Stop at actionable evidence.** The last useful "why" is the one that names a test, owner, or measurement. Beyond that you are writing history or philosophy.
- **Ask "what would change my mind?" at each level.** If nothing could, stop; you have reached a definition or a value, not an empirical constraint.
- **Branch, do not average.** A constraint often has several necessary conditions. Track each branch; do not collapse them into one chain.
- **Watch motivated stopping.** The ladder is easy to abandon at the answer that is convenient. Have someone else check the stopping point on load-bearing items.
- **Do not force a single root cause.** The "five whys" pattern works for linear failures. For systemic problems the answers fan out; switch from a chain to the constraint map.

## Minimum fundamental set

Put every retained item through these questions:

- **Does it bind every possible solution?** If some solutions avoid it, it is a requirement or a preference, not a fundamental.
- **Is it a consequence of another constraint?** Merge it into its parent; do not count it twice.
- **Does it describe only the incumbent?** Move it to the dropped log.
- **Can it be satisfied in more than one way?** That is a requirement to meet, not a constraint to preserve.
- **What is the irreducible outcome?** If this did not happen, the problem is unsolved no matter how elegant the design. That sentence anchors the rebuild.

## Rewrite the problem

Use a single sentence:

> Achieve **[outcome]** for **[who]** subject only to **[fundamentals]**.

Then list what you deliberately left out and why. Keep a dropped-constraint log with columns: item, why dropped, what evidence would bring it back. The log protects against forgetting a real limit and against quietly re-importing a convention.

## Mini example

Claim: "Expense approvals must take three days because finance reviews them."

- Why must finance review? "To prevent overspend."
- Why does that require a human review? "It doesn't; the limit does." The review is one implementation.
- Fundamental: spend per team must stay within an allocated budget, and unusual spend needs a record.
- Rebuild space: pre-approved envelopes, automated policy checks, post-hoc audit, delegated limits.
- Inherited: the three-day queue and the review meeting.

The three-day wait was never the constraint. The budget ceiling and audit obligation were.

## Signals you stripped too far

- The design violates a measurement, law, or safety invariant.
- It requires coordination that no one can supply.
- It assumes behavior contradicted by observation.
- It only works if everyone changes at once.
- You removed a control without understanding its failure mode.

## Signals you did not strip enough

- Every alternative still contains the same inherited step.
- The constraint list is dominated by items owned inside the organization.
- The "must" count did not fall after classification.
- The rebuild looks like the incumbent with new labels.
- You cannot name the irreducible outcome in one sentence.
