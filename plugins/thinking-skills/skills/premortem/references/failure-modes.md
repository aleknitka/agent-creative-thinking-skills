# Failure Modes — Five Categories to Search

The categories are **prompts for generation**, not a taxonomy to complete. Their job is to pull reasons out of corners the plan does not usually discuss. Better to overgenerate and merge later than to finish a tidy checklist.

## 1. Assumption failures

The plan treats something as true that was never tested: user behaviour, demand, timing, cost, platform stability, adoption by the target segment, or the causal link between output and outcome.

**Trigger questions**

- Which belief, if false, makes the whole plan pointless?
- What did we assume about **who** does **what**, **when**, and **why**?
- What would falsify that assumption cheaply, and why haven't we done it?
- Which "obvious" fact is actually a projection or a hope?

**Examples**

- Activation is defined at signup, but most users first arrive days later via an admin invitation.
- The plan assumes a migration window the platform's rate limits do not allow.
- Demand is inferred from survey intent, not from a paid pilot.

**Early signal:** assumptions never written down; pilot conversion below the historical baseline; the same "we'll see" in every review.

## 2. Coordination failures

The work spans people, teams, vendors, approvals, or systems — and a handoff, dependency, or decision right is missing or ambiguous.

**Trigger questions**

- Who must do what, by when, for this to ship? Which handoff has no owner?
- What breaks if one team is late, or if two teams interpret the interface differently?
- Which approval, contract, or data flow is on the critical path?
- Who has the decision right when the plan meets reality?

**Examples**

- Customer Success is not trained before launch and routes users to last quarter's playbook.
- The API contract changes between teams without a versioned spec.
- Launch sequencing assumes sales and marketing switch on the same day.

**Early signal:** missed internal milestones; unclear ownership in notes; integration tests skipped or "done manually for now".

## 3. Incentive failures

People and teams optimise for what they are measured and rewarded on, which may differ from what the plan needs.

**Trigger questions**

- Who is rewarded if this succeeds — and who is rewarded for something that conflicts with it?
- What is each stakeholder optimising: bookings, tickets, utilisation, headcount, risk avoidance?
- Who bears the cost of failure, and who captures the upside?
- Where would a rational person work around the new process?

**Examples**

- Support is measured on time-to-close, so agents give manual walkthroughs that close tickets but bypass the new onboarding.
- Sales is paid on bookings, not activation, and sells use cases the product cannot deliver.
- A platform team is rewarded for uptime, so it blocks the experiment that would improve activation.

**Early signal:** shadow processes, metric gaming, "just this once" exceptions, private dashboards that disagree with official ones.

## 4. Capability failures

The team lacks the skills, capacity, tooling, time, or attention the plan requires — including the ability to tell whether it is working.

**Trigger questions**

- Do we have the skills and capacity to execute at this quality, given everything else in flight?
- Which single person or system is load-bearing, and what happens if they are unavailable?
- Can we observe the outcome we care about, at the granularity needed to act?
- Is the scope plausible at the team's demonstrated velocity?

**Examples**

- No analytics event exists for the drop-off the plan is supposed to improve.
- One engineer owns the only integration and is also on call for the legacy system.
- A ten-week scope is planned against a team that has never shipped in under sixteen.

**Early signal:** rising defect or rework rate; growing backlog; repeated heroics; instrumentation deferred to "phase two".

## 5. External failures

Events outside the team's control change the premise: regulation, market, competitors, platforms, suppliers, customers' own organisations, or security incidents.

**Trigger questions**

- What outside change would make this plan obsolete or non-compliant?
- Which platform, regulator, or enterprise customer can change the rules mid-flight?
- What happens if the market, funding climate, or competitor moves?
- Which supplier or dependency has no substitute?

**Examples**

- A key enterprise customer mandates SSO/SCIM, so procurement blocks the new flow until compliance review.
- A platform deprecates the API the integration depends on.
- A competitor makes the paid feature free, resetting willingness to pay.

**Early signal:** policy consultations, vendor roadmaps, customers' procurement checklists, funding freezes, competitor announcements.

## Using the categories well

- **Failures combine.** "CS wasn't trained because support is measured on ticket closure and no one owned activation" is one causal story spanning coordination, incentive, and assumption. Cluster by that mechanism, not by category label.
- **Deliberately skew.** If the list is heavy on external reasons, the group is probably avoiding what it controls. If it is heavy on capability, check for blame disguised as analysis.
- **Record wildcards separately.** Low-likelihood, high-impact events deserve a contingency or monitor, not an equal share of the mitigation budget.
- **Push past labels.** "Communication" and "execution" are not reasons. Ask what specifically would not happen, who would not do it, and what signal would show it first.
