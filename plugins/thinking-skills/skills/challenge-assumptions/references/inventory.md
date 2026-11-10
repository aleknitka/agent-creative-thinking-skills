# Inventory — Finding the Beliefs That Hold the Problem Together

An inventory is a list of assertions that must be true for the current approach — or the current statement of the problem — to make sense. The goal is coverage, not depth: get the unspoken ones onto the table before deciding which deserve a test.

Aim for **8–15 beliefs**. Fewer usually means you have inventoried the solution, not the framing; more usually means you are listing facts and preferences rather than load-bearing beliefs.

## Phrase beliefs as assertions

Weak inventory entries are topics: "onboarding," "pricing," "compliance." You cannot test a topic.

Strong entries are checkable claims with a subject and a predicate:

- Weak: "users don't read"
- Strong: "New users will not complete onboarding without a guided tutorial."
- Weak: "legal"
- Strong: "Any change to the signup flow requires legal review before launch."
- Weak: "manual approval"
- Strong: "A human must approve refunds over $500 before they are paid."

A useful assertion has a direction: you can imagine evidence for it and against it.

## Four families to sweep

### 1. Origin — inherited vs. proven

**Inherited** beliefs arrived by tradition, copying, or path dependence. Nobody currently in the room decided them, and no evidence is on file. They are prime candidates for challenge.

- "We've always done it this way."
- "It's industry standard."
- "That's how the platform works." (Verify: platform *policy*, *default*, or *limitation*?)
- "Customers expect it." (Whose customers, measured when?)

**Proven** beliefs have a traceable test, incident, contract, or physical limit behind them. They can still be over-generalized, but the burden of proof is on the challenger.

- "The API rate-limits at 60 requests/minute; we measured it."
- "The regulator requires retention for seven years."
- "The last two launches without a rollback plan caused outages."

Provenance test: *Who decided this, when, and what evidence did they have?* If the answer is "nobody knows," it is inherited until shown otherwise — not automatically false, just untested.

### 2. Source — stakeholder vs. system

**Stakeholder beliefs** are attributed to people: users, customers, executives, regulators, support staff.

- "Users want fewer clicks."
- "Leadership will not fund anything that touches billing."
- "Support cannot handle a second channel."

Two failure modes: treating a stakeholder *preference* as a *hard constraint*, and treating your own inference as the stakeholder's view. Ask whether the belief was stated by that stakeholder, observed in their behavior, or assumed on their behalf.

**System beliefs** are attributed to mechanisms: tools, policies, contracts, architectures, economics.

- "The CMS cannot publish without an editor role."
- "The contract forbids resale."
- "Our unit economics require a 40% margin."
- "The data is not joinable across those tables."

System beliefs are often partly true and partly scope error. Separate the invariant ("the tool requires an editor role") from the local configuration ("we set it up that way"), and the contract clause from the interpretation of it.

### 3. Boundary — where the box was drawn

Boundary beliefs define what is inside the problem: which users, channels, time horizon, budget, geography, or system are in scope.

- "This must work within the current headcount."
- "The solution has to live in the existing app."
- "We only serve customers in three markets."
- "This quarter is the deadline."

Boundaries are the highest-leverage beliefs because they are usually chosen, not found. Ask: *Is this boundary a real constraint, a negotiated constraint, or a convenience?* A boundary can be real and still negotiable — "the deadline is set by a customer commitment" is different from "the deadline is set because someone picked a date."

Watch for the invisible square: constraints that were never stated but are treated as rules (Nine Dots). Often the boundary is implied by the problem statement's nouns — "the mobile onboarding flow" already excludes web, email, sales-assisted, and partner channels.

### 4. Continuity — sequence and persistence

Continuity beliefs assume the current order, roles, or persistence must continue.

- "Users must create an account before they can see value."
- "The manager approves, then finance pays."
- "This process has to stay in the same system."
- "The data must be complete before analysis starts."

Two questions expose most of them: *Does the order have to be this order?* and *Does the step have to exist at all?* Continuity beliefs often survive because each step's existence is justified by the step before it — a chain with no independent reason at either end.

## Prompt list

Pick the questions that fit; do not mechanically ask all of them.

**Problem statement**
- What does the problem statement take for granted in its nouns and verbs?
- If the problem were solved in a completely different way, what would still have to be true?
- Who framed the problem this way, and who would frame it differently?
- What is the goal behind the stated problem, and does the statement serve it?

**Existence**
- Why does this step/role/rule exist? What was the original reason?
- Is that reason still true, still relevant, and still worth its cost?
- What breaks if we delete it entirely for one case?

**Necessity and degree**
- Is this required, or merely customary? Required by whom, in writing?
- Could a smaller version satisfy the goal — half the approvals, a tenth of the data, one market?
- What is the cheapest exception that would still be legitimate?

**Agency and ownership**
- Who decided this, and do they still hold that position?
- Whose preference is being treated as a rule?
- What would the user, operator, or adversary say this belief gets wrong?

**Boundary**
- What is in scope only because it was named first?
- What adjacent thing is excluded without a stated reason?
- Is the deadline/cost/headcount a constraint or an estimate?

**Continuity**
- Does the sequence have to run in this direction? Could it run in parallel or backwards?
- Which step exists only because the previous step exists?
- What would we keep if we had to rebuild this from scratch tomorrow?

**Evidence**
- What do we actually observe, versus what do we infer?
- What would change our mind? Has anyone looked?
- Is there a cheaper source of truth than opinion — logs, tickets, contracts, one interview?

## Capture table

Use one row per belief. Keep the last column concrete.

| ID | Belief (assertion) | Family | Source / owner | Evidence today | Confidence | If false, what changes? |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | New users cannot reach first value without a guided tutorial | Origin: inherited | "UX best practice", no owner | None on file; 2 anecdotal tickets | Low | Tutorial can be optional or removed; onboarding becomes task-based |
| A2 | Support is staffed only for in-app chat | Source: system | Support lead | Roster + tooling contract | High | A second channel needs budget or self-serve deflection |
| A3 | Launch must fit the current quarter | Boundary | VP Product | Verbal commitment, no external dependency | Medium | Smaller scope or staged launch becomes viable |
| A4 | Account creation must precede any value | Continuity | Legacy flow design | No test; assumed | Low | Guest mode / sandbox-first becomes possible |

Rules for the table:

- **Family** is a lens, not a verdict. One belief can be both inherited and boundary.
- **Evidence today** must be something you could point to. "Everyone knows" is not evidence; write "none."
- **Confidence** is your current credence, not importance. A high-confidence belief can still be the key constraint.
- **If false** is the payoff test. If you cannot name what changes, the belief is decoration and belongs at the bottom of the list.

## Quality checks before testing

1. **Can someone disagree?** If not, it is a fact or a definition, not a belief.
2. **Is it specific enough to test?** "Users dislike onboarding" is not; "users abandon at step 3 because of the password rule" is.
3. **Did you include the problem statement itself?** At least two rows should come from its framing, not from the current solution's mechanics.
4. **Did you include a boundary and a continuity belief?** If not, you probably inventoried the solution's internals only.
5. **Are the obvious ones present?** The strongest constraints are often so obvious they feel embarrassing to write down. Write them anyway.

Next: rank by impact × uncertainty and run the tests in `testing.md`.
