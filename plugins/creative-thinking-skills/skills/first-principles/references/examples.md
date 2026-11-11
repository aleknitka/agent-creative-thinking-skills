# Worked Example: Onboarding Without the Inherited Design

## Situation

A B2B analytics product has flat activation. The team says: "Onboarding needs a seven-step tutorial, a setup wizard, and a five-email drip." Every proposed improvement adds another step, another tooltip, or another email.

Rewrite the goal as an outcome: **a new user reaches first success — their own data answering a real question — in their first session.** The tutorial, wizard, and drip are candidate solutions, not the goal.

## Constraint map

| ID | Assertion | Classification | Evidence and reasoning | Decision |
| --- | --- | --- | --- | --- |
| C1 | A user must authenticate before seeing private data | Invariant (security) | Failure mode is data exposure; required by the product's security model | Keep |
| C2 | Data must be connected or imported before a result can exist | Logical prerequisite | No data, no answer; unavoidable for any flow | Keep |
| C3 | Customer data cannot leave its region | Regulation / contract | Data-residency obligations and enterprise contracts | Keep, verify scope by customer |
| C4 | A first result should be available within minutes, not days | Resource / product goal | Goal chosen by the team for activation; not a physical law | Keep as a design target, label as goal |
| C5 | Onboarding must be a seven-step tutorial | Inherited | No owner can cite a test; it is the current flow | Drop |
| C6 | Setup must collect company size, role, and use case before the first result | Preference / analytics wish | Useful for segmentation, not required for first value | Defer or infer |
| C7 | Emails must go out on days 1, 3, and 5 | Inherited | Copied lifecycle template; no test of effect | Drop from the critical path |
| C8 | Trial must be 14 days | Inherited / pricing choice | Commercial convention, not a constraint | Keep as a policy decision, do not rebuild around it |
| C9 | 62% of users abandon at step 3 | Fact (current design) | Instrumentation from the existing flow | Evidence, not a permanent law |
| C10 | Users who load their own data in session one retain better | Observation (associational) | Cohort analysis; selection effects possible | Treat as promising, test causally |

The fundamental set is small: authentication, data prerequisite, regional handling, and a chosen speed target. The rest were design choices or evidence about the current flow.

## Rebuilt alternatives

**A. Sample-to-own in one session.** Open with a relevant sample dataset and one real question. The user edits the query or uploads a single CSV, and gets a result before any account setup beyond authentication. The wizard, tour, and email dependency disappear. New assumption: a sample question is relevant enough to create intent. Cheapest probe: one cohort, activation defined as a first real question answered; kill if activation does not beat the current flow after a fixed window.

**B. Connect-first with one source.** A single connector to the user's warehouse or tool, automatic schema detection, and the top three questions surfaced from their own data. No tutorial; the product demonstrates value on real data immediately. New assumption: the target segment can complete a connection without help. Probe with the technical segment; watch time-to-connect and support tickets; kill if connection failure dominates.

**C. Concierge for high-value accounts.** A human onboarding call within 24 hours, with the customer's data preloaded before the call. This removes the self-serve assumption for accounts where the deal size justifies the cost. New assumption: activation gains justify the labor cost. Probe with a small account set; compare activation and cost per activated account; kill if the unit economics do not clear the segment's margin.

## Comparison

| Alternative | Inherited defaults removed | Fundamentals satisfied | New assumptions | Cheapest probe | Kill criterion |
| --- | --- | --- | --- | --- | --- |
| A. Sample-to-own | Tutorial, wizard, drip | C1–C4 | Sample relevance | One cohort | No activation lift in window |
| B. Connect-first | Tutorial, manual schema setup | C1–C4 | Self-serve connection | Technical segment pilot | Connection failures dominate |
| C. Concierge | Self-serve requirement | C1–C4 | Labor cost is justified | 20 high-value accounts | Cost per activation too high |

## What was deliberately not removed

Authentication, the data prerequisite, regional handling, and support capacity remain. They are not obstacles to a better flow; they are the conditions the flow must satisfy. Removing them would produce a demo, not a product.

## Probe and next step

Pick one alternative and one cohort. Define activation before launch, set the observation window, and pre-commit the decision rule. Track guardrails: support load, regional compliance, and retention after the first session. If the result is ambiguous, run the next cheapest probe rather than adding steps back.

## Lessons

- Every dropped constraint had an internal owner and no evidence.
- The fundamental list fit on a few lines; the inherited list was longer.
- The alternatives differed by **who does the work** and **whether data arrives before or after the first value moment** — not by tutorial copy.
- The rebuild was only credible because it kept the real constraints, including the boring operational ones.
