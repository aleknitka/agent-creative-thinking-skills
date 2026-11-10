# Worked example

A product team receives the brief: **"We need a better onboarding email
sequence."** It is a solution with no stated problem. The team is two days
from committing to a copy and cadence overhaul.

## 1. Intake

- Brief, verbatim: "We need a better onboarding email sequence."
- Requester: head of growth.
- Decision it feeds: whether to rebuild the five-email sequence this quarter.
- Already tried: subject-line tests (+2% opens), one reorder of emails.
- Success measure: unknown; growth tracks "activation," undefined.
- Constraints: existing email tool, no engineering time this quarter, launch
  in six weeks.
- Facts: open rate 41%; activation (first project created) 28% at 14 days.
- Assumptions: email is the bottleneck; more/better email will move
  activation.
- Speculation: users "forget" to return; sequence timing is wrong.

## 2. Twenty-plus questions

**Clarifying**
1. What exactly counts as "activated," and where is that event recorded?
2. Is 28% good, bad, or unknown relative to our own history and peers?
3. What does "better" mean — opens, clicks, activation, or revenue?
4. Which five emails exist today, and what does each ask the user to do?
5. Is the sequence the only onboarding touchpoint, or one of several?

**Reframing**
6. If the sequence were perfect, what would change in the business?
7. Why is email the chosen intervention rather than in-product guidance?
8. What is the goal above activation — retention, expansion, or support cost?
9. What would make the email sequence unnecessary?
10. Why now; what changed this quarter?

**Stakeholder**
11. Who reads these emails: the buyer, the admin, or the end user?
12. Who decided email was the problem, and what did they observe?
13. Who owns activation today, and who is accountable for the 28%?
14. Which new accounts are excluded from the metric, and why?
15. What do support and sales hear from users who stall?

**Constraint**
16. Which is fixed: the email tool, the six-week launch, or the no-engineering
    rule — and who can change each?
17. What could we ship without engineering time that is not email?
18. What is the cost of sending more email to unengaged accounts?

**Causal**
19. Where in the first 14 days do users stop, and is it one step or many?
20. Do users who never open email activate at a different rate from openers?
21. Did activation change when the sequence last changed?
22. What did users who activated do that stalled users did not?
23. Is "forgot to return" evidenced, or inferred from silence?

**Generative**
24. What if onboarding had no emails and relied on the first session alone?
25. How might we create first value before the first email arrives?
26. What is the smallest intervention that would test the forgetting
    hypothesis?
27. What would a user who is hostile to email do?

## 3. Clusters

- **A. Definition and baseline** (1–4, 14): activation is undefined, so no
  intervention can be evaluated.
- **B. Channel hypothesis** (5, 7, 9, 20, 24): email may be incidental; the
  evidence linking email behavior to activation is missing.
- **C. Moment of stall** (16, 19, 22, 26): we do not know where or why users
  stop, so timing and content changes are guesses.
- **D. Ownership and goal** (6, 8, 10, 12, 13): the business goal and the
  accountable owner are unstated.

Questions 11, 15, 17, 18, 21, 23, 25, 27 were parked or folded into the above.

## 4. Ranking

| Cluster | Leverage | Tractability | Reframing | Triage |
|---|---|---|---|---|
| A. Definition | 3 | 3 | 3 | Answer now |
| B. Channel hypothesis | 3 | 2 | 3 | Probe |
| C. Moment of stall | 3 | 2 | 2 | Probe |
| D. Ownership and goal | 3 | 3 | 2 | Answer now |

Top questions:

1. What is the activation event, and can we segment the 28% by behavior?
2. Do email openers and non-openers activate at different rates?
3. Where in the first 14 days do stalled accounts stop?
4. What business outcome is activation supposed to serve, and who owns it?

## 5. Revised problem statements

**Statement A — same scope, sharper target.**
"How might we get new accounts to first value within 14 days, using whichever
touchpoint their behavior shows they respond to?"
Email becomes one candidate channel; the target is first value, not sends.

**Statement B — diagnostic, prior to any rebuild.**
"Which new accounts stall before first value, at what step, and what would let
us intervene at that moment?"
This makes the email rebuild conditional on evidence and reframes the task
from content production to diagnosis.

A third, rejected candidate — "How might we improve onboarding emails to lift
activation?" — was rejected because it preserves the unexamined channel
assumption and cannot fail.

## 6. Probes

- **Definition (answer now):** growth analyst confirms the activation event
  and produces a cohort by signup source and first-session behavior. Decision
  rule: if activation varies more by cohort than by email engagement, the
  channel hypothesis weakens.
- **Channel (probe):** compare 14-day activation for openers vs. non-openers,
  controlling for signup source. Decision rule: a gap under 5 points means
  email is not the lever.
- **Stall point (probe):** instrument or manually reconstruct the first-session
  path for 20 stalled accounts. Decision rule: if most stall before the first
  project, rewrite the problem around first-session setup, not email.
- **Goal (answer now):** one conversation with the head of growth to name the
  outcome and accountable owner.

## Outcome

The team does not rebuild the sequence yet. It spends one week on definitions
and the stall-point probe, then revises the statement again. The deliverable
of question storming is this redirection, not an email plan.
