# Laddering — Why Up, How Down

Laddering is a two-directional interview with yourself or a stakeholder. Upward questions ask what a statement is *for*; downward questions ask what would *make it happen*. The value comes from doing both on the same statement, so the resulting rungs are linked rather than collected.

## The two moves

| Direction | Question | Answer should be | Typical failure |
| --- | --- | --- | --- |
| Up | "Why does this matter?" | A goal, outcome, or stakeholder need | Restating the solution |
| Up | "What is this in service of?" | Purpose one level broader | A slogan no one can act on |
| Down | "How could this happen?" | A mechanism, condition, or action | A task list or owner |
| Down | "What would have to be true?" | An enabling condition | A restated goal |

The pair is asymmetric. Up is about **intent**; down is about **causality**. Do not let one borrow the other's question. "Why did this fail?" is a causal question and belongs to diagnosis, not laddering.

## Ladder up: the why chain

Start from the statement exactly as given.

1. Write the statement verbatim.
2. Ask: *Why does this matter?* Write the answer as a sentence with a subject and an outcome: "So returning users can reach their saved work without re-entering details."
3. Ask the same question of that answer. Repeat three to five times.
4. Stop at the rung that names the stakeholder and purpose you are actually serving.

Useful follow-ups when an answer stalls:

- "Who is this for, and what do they get?"
- "If this worked perfectly, what would be different?"
- "What would we stop caring about if this were solved?"
- "Which higher commitment does this serve?"

Push for the **first useful abstraction**, not the ultimate one. Most problems have a natural ceiling around purpose: the customer need or organizational commitment that makes the work worth doing. Above that lies vision and values, which are usually too broad to guide design.

## Ladder down: the how chain

From a chosen goal, ask what would bring it about.

1. Restate the goal as a desired state.
2. Ask: *How could this happen?* Answer with a mechanism, not a project: "New users get a first useful result before being asked to configure anything."
3. Ask again of the mechanism: "What would have to be true for that?" Keep decomposing into conditions.
4. Stop when you reach something you can observe tomorrow: a behavior, a screen, a policy, a model output.

Useful follow-ups when an answer stalls:

- "What is the smallest version of this that would still test the idea?"
- "What has to be true of the user / system / context for this to work?"
- "What currently prevents this from happening?"
- "How would we know it happened?"

Downward answers should get **more specific and more testable** at each step. If they get longer but not more observable, you are listing tasks, not decomposing mechanism.

## Stop rules

Stop going up when any of these holds:

- The answer names the ultimate beneficiary and there is no further stakeholder to add.
- The next why produces a universal ("so people are happy," "so the company succeeds").
- The next why leaves the scope you can influence or measure.
- Another why would only restate the same purpose in grander words.

Stop going down when any of these holds:

- The rung is observable and testable within your budget.
- Further decomposition requires knowledge you do not have; record the unknown and probe it.
- You have reached a single owner or scheduled action with no remaining mechanism question.
- You are writing task tickets rather than causal conditions.

Record *why* you stopped. A ladder that stops because of budget is different from one that stops because purpose was reached, and the difference matters when the frame is revisited.

## Working the ladder

- **Record each rung as a full sentence.** Fragments hide missing subjects and outcomes.
- **Do one direction first, then the other.** Climbing from a tactic and descending from a goal produce different material; run both if the middle is unclear.
- **Keep a column for evidence.** Mark each rung fact / assumption / speculation. Ladders amplify whatever they are built on.
- **Look for the join.** The finding is often where the upward chain from the action and the downward chain from the goal fail to meet.
- **Do not average levels.** A statement that mixes goal and tactic ("reduce churn by adding a dashboard") must be split into its rungs before it can be evaluated.

## Common failure modes

- **Solution laundering** — the "why" answer is the same solution with a benefit clause. Ask what outcome the solution would produce, then ladder from the outcome.
- **Slogan ceiling** — stopping at "delight customers." Force the next question: delight them *how*, and *which* customers, in service of what?
- **Premature specificity** — descending to a feature before naming the function it serves.
- **Infinite regress** — refusing to stop until a cosmic purpose is reached. Stop at the useful ceiling.
- **Ladder as org chart** — replacing mechanism questions with "who owns this?" Ownership is a rung below action, not a substitute for it.
- **Ignoring the base rate** — building an elegant ladder for a problem that data says is small.
