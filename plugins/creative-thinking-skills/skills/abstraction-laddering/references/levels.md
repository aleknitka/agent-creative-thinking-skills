# Levels of Abstraction

Laddering works best when the rungs are labeled, because each level has a different job, a different evidence standard, and a different failure mode. The five levels below are a working vocabulary, not a law of nature.

## The five levels

| Level | Question it answers | Example | Test for "is this the right level?" |
| --- | --- | --- | --- |
| **Vision** | Why do we exist / what future are we aiming at? | "People can do their best work without administrative drag." | Would still be true if this product disappeared. |
| **Purpose** | What need are we serving, for whom? | "New users reach value without needing help." | Names a beneficiary and an outcome. |
| **Function** | What must the system do to serve that purpose? | "Get a user to a first useful result in one session." | Describes a capability, not a feature. |
| **Mechanism** | How does that capability work? | "Ask for one decision at a time; defer configuration until after first value." | Names a causal lever you could change. |
| **Action** | What do we do, concretely, now? | "Remove the workspace-setup step from the first-run flow." | Observable, assignable, testable. |

Two extra rungs often appear and are worth naming:

- **Identity / value** — above vision, the beliefs that make the vision feel worth having. Useful for narrative, dangerous as a design input.
- **Instrumentation** — an action whose only job is to reveal state ("add logging"). Not a mechanism; do not confuse it with one.

## Signatures and tells

**Vision** language is broad, durable, and rarely falsifiable. Tells: "world where," "everyone should be able to," no actor. Use it for direction, never for a probe.

**Purpose** language names a person and a change in their state. Tells: "so that [who] can [outcome]." This is usually the best level for framing a problem.

**Function** language describes a capability independent of implementation. Tells: verbs like *find, decide, recover, coordinate, trust*. If two very different features could serve it, it is a function.

**Mechanism** language names a causal lever. Tells: "because," "by," "when X then Y," a variable that can move. This is where most design work happens.

**Action** language is a concrete change with an owner and a date. Tells: imperative verb, named artifact, done/not-done. If you cannot tell when it is finished, it is not an action.

## Diagnosing where a statement sits

Ask three questions of any statement:

1. **Does it name a beneficiary and an outcome?** If yes, it is at least purpose.
2. **Could several unrelated implementations satisfy it?** If yes, it is above mechanism.
3. **Can you tell tomorrow whether it happened?** If yes, it is action or mechanism.

Statements that pass both 1 and 3 are usually **mixed levels** and must be split. "Increase retention by improving onboarding" pairs a purpose (retention) with a mechanism candidate (onboarding) in one clause; each deserves its own rung.

## Vertical coherence

A ladder is coherent when each lower rung is *sufficient in principle* to contribute to the rung above, and each upper rung *explains why* the lower one matters.

Check each adjacent pair:

- **Downward implication** — "If this mechanism worked, would it plausibly move the function above?" If not, the ladder has a leap.
- **Upward justification** — "Does the rung above give a reason for this rung to exist?" If not, the rung is an orphan.
- **Necessity vs. sufficiency** — lower rungs are usually contributors, not guarantees. State which link is believed and which is proven.

Common structural defects:

- **Missing middle** — vision linked directly to tickets. The unnamed function level is usually the actual design problem.
- **False floor** — treating a mechanism as an action ("improve messaging") when nothing observable changes.
- **False ceiling** — treating a function as a vision ("we need better onboarding"), which blocks the question of *why* onboarding matters.
- **Parallel ladders** — two chains that never meet. Usually two different stakeholders' purposes, and the conflict is the finding.

## Level and evidence

Different levels demand different evidence:

- Vision: narrative and strategy documents; almost never a direct test.
- Purpose: interviews, observed behavior, outcome metrics.
- Function: task analysis, failure observation, comparative designs.
- Mechanism: experiments, instrumentation, causal inference.
- Action: build/run logs, acceptance checks, direct observation.

Mismatching evidence to level is a common error: testing a vision with a click-through rate, or justifying an action with a strategy deck. When a claim crosses levels, mark the link as assumption until tested.
