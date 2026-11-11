# Reframe Patterns — Five Moves That Remove a Belief

A reframe is a new statement of the problem in which a specific belief is no longer required. It is not a new idea for solving the same problem; it is a different problem boundary. If the old statement still applies unchanged, nothing was reframed.

Use these after pressure-testing, on the **2–4 beliefs that actually block options**. One belief can yield several reframes; five patterns applied indiscriminately produce noise.

## The five moves

| Pattern | The move | Trigger question | What it changes |
| --- | --- | --- | --- |
| **Negate** | Assume the belief is false | What if the opposite were true? | Removes the belief entirely |
| **Relax** | Weaken the belief to a degree or a subset | Could a partial or conditional version work? | Narrows scope, cost, or strength |
| **Invert** | Reverse the direction of agency or sequence | What if the other party, order, or endpoint did the work? | Changes who acts and when |
| **Re-scope** | Move the boundary of the problem | Is the problem bigger, smaller, or at a different level? | Changes what is inside the box |
| **Re-attribute** | Move ownership of the constraint or the solution | Who else could own this belief or this step? | Changes who must act |

### 1. Negate

State the strict opposite and ask what would have to be true for it to work. Negation is the cleanest test of whether the belief is load-bearing, because it removes the constraint completely rather than negotiating with it.

- Belief: "New users must complete a tutorial before using the product."
- Negate: "New users must never see a tutorial."
- Candidate reframe: "How might new users reach first value with no instruction at all?"
- Mechanism to look for: self-evident UI, task templates, contextual hints after a real action, or a concierge first run.

Risk: negating a real constraint produces fantasy. Run the falsification test first; if the belief is proven, negate the *scope* instead ("no tutorial for returning users") and label the reframe as a relaxation.

### 2. Relax

Weaken the belief along one dimension: frequency, strength, segment, duration, or stage. Relaxation is the safest pattern and often yields the most executable options.

- Belief: "Every refund over $500 needs human approval."
- Relax: "Refunds over $500 need approval only when the customer has no prior purchases."
- Candidate reframe: "How might we auto-approve refunds for established customers while keeping a control where risk is real?"
- Dimensions to vary: who (segment), when (first time vs. repeat), how much (threshold), how long (trial period), how strong (audit after vs. approve before).

Risk: erosion by exception. State explicitly which control remains and why; otherwise relaxation becomes "remove the rule and hope."

### 3. Invert

Reverse the direction: who initiates, who is taught, what runs first, where value appears. Inversion is not the same as negation — the belief can remain true in general while the flow reverses.

- Belief: "The user is taught the product by us."
- Invert: "The product is taught by the user's own first task."
- Candidate reframe: "How might the user's first real task produce the instructions, instead of a tour preceding the task?"
- Other inversions: customer configures instead of vendor; payment after outcome instead of before; data pushed to the user instead of pulled; approval after audit instead of before action.

Risk: reversing a sequence can break dependencies that the original order satisfied. Name what the old order protected (safety, payment, consent) and keep that guarantee explicit.

### 4. Re-scope

Change the size or level of the problem. Shrink it to the smallest case that still matters; expand it to the goal that makes the current problem optional; or move up a level from "how do we make this step better" to "why does this step exist."

- Belief: "We must redesign the six-step onboarding flow."
- Re-scope up: "How might new users get value in their first session, regardless of flow?"
- Re-scope down: "How might one high-intent segment skip onboarding entirely?"
- Re-scope sideways: "How might the buyer's admin set up the workspace so the end user never onboards?"

Risk: scope drift that dodges the original goal. Keep the goal fixed in the reframed statement and say what is deliberately excluded.

### 5. Re-attribute

Move the belief or the work to a different owner: another team, the customer, a partner, the platform, or the user's own context. Many "system constraints" are one team's local configuration; many "user needs" are actually support's needs.

- Belief: "Our support team must hand-hold every new account."
- Re-attribute: "The customer's admin owns setup; our support owns exceptions."
- Candidate reframe: "How might the account admin be equipped to onboard their own team, with support handling only escalations?"
- Other re-attributions: platform default instead of custom build; partner integration instead of internal feature; regulator's actual requirement instead of legal's conservative interpretation; user's existing tools instead of a new one.

Risk: exporting cost to someone with less power or context. Check who bears the new burden and whether they agreed.

## From belief to three statements

Produce **three distinct problem statements** for the chosen reframe set. Format:

> **How might we** [goal] **without** [the belief]?

Then add one line each:

- **Belief removed:** A4 — "account creation must precede value."
- **Mechanism to explore:** guest workspace with save-on-signup.
- **What stays fixed:** the goal (time-to-first-value under 10 minutes) and the real constraints (data retention, abuse limits).

Distinctness test: do the three statements differ in *which belief is gone*, not in adjectives? If two only reword one another, apply a different pattern to the same belief or pick a different belief.

## Worked pattern application

Belief: "Approvals must be manual because auditors require a human decision."

| Pattern | Reframe | Comment |
| --- | --- | --- |
| Negate | "How might we approve without any human decision?" | Only viable if the audit requirement is actually "accountable decision", not "human click" |
| Relax | "How might we automate approvals under $1k and keep humans above?" | Preserves control where risk concentrates |
| Invert | "How might the system decide first and route only exceptions to a human?" | Changes default from approve to exception |
| Re-scope | "How might we remove the need for approval by making the underlying spend impossible to misuse?" | Attacks the reason for control, not the control |
| Re-attribute | "How might the vendor's built-in limit replace our approval step?" | Moves enforcement to the platform |

Each is a different hypothesis about what the auditor actually requires. The inventory should contain that meta-belief — "auditors require a human decision" — as its own row, because it is usually the real constraint.

## Quality checks

- **Named belief.** Every reframe points to an ID in the inventory. No ID, no reframe.
- **Goal preserved.** The goal behind the original problem is unchanged; only the constraint moved.
- **Real constraints respected.** Proven constraints stay, or their challenge is explicitly flagged as speculation needing evidence.
- **Mechanism present.** A reframe without a candidate mechanism is a slogan. One sentence of "this could work because…" is enough at this stage.
- **Not a solution in disguise.** "How might we build feature X" is a solution statement. Keep the reframe at problem level; ideas come later.
- **Three, not thirty.** Three well-chosen statements beat a list. Add more only if each removes a different belief.

## Handoffs

- Need many directions inside one reframe → `lateral-thinking`.
- Need systematic variations on a chosen reframe → `scamper`.
- Need to rebuild from verified constraints → `first-principles`.
- Need to test whether a reframe survives scrutiny → `premortem`.
- Need to choose among reframes with stakeholders → `six-thinking-hats` or `options-portfolio`.
