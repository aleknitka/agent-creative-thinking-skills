# Prioritization — Likelihood × Impact and Warning Signals

The goal is not a complete risk register. It is a small set of failure reasons worth changing the plan for. Scoring is a sorting aid, not a measurement.

## Scoring anchors

Score each reason 1–5 on both axes **before** discussing scores.

**Likelihood — how probable is this reason by the failure horizon?**

| Score | Anchor |
|---|---|
| 1 | Remote; would require several things to go wrong |
| 2 | Unlikely, but a known pattern elsewhere |
| 3 | Plausible; roughly a coin flip given current evidence |
| 4 | Likely; precedent, early signals, or expert dissent points this way |
| 5 | Already happening or strongly evidenced |

Anchor on evidence: base rates from comparable projects, pilot data, front-line reports, and unresolved dissent. When uncertain, record a range (`2–4`) rather than a false-precise point.

**Impact — what happens if it occurs at the horizon?**

| Score | Anchor |
|---|---|
| 1 | Negligible; absorbed within normal slack |
| 2 | Minor delay, cost, or rework |
| 3 | Measurable miss of the success measure |
| 4 | Project fails, or major customer/employee harm |
| 5 | Existential, safety, legal, or regulatory consequence |

Impact is conditional on occurrence and independent of likelihood. Do not lower impact because a reason feels unlikely.

**Rank** by the product (1–25). Keep the top 3–5 for hardening. High-impact reasons (`I ≥ 4`) stay visible even at low likelihood — treat them as wildcards for monitoring or contingency, not as equal candidates for prevention spend.

## Group scoring

- Everyone scores independently, then shares. Record the range and any lone high score; investigate it rather than averaging it away.
- A reason that is likely but contributes little is a distraction; a reason that is unlikely but fatal is a contingency.
- State the causal path when scoring: "If CS routes users to manual setup, activation stalls even though signups hold." Without a path, the score is a vibe.

## Warning signals

For each top reason, define a **signal** before the project starts. A usable signal is leading, observable, owned, and thresholded.

- **Leading** — it moves before the failure is irreversible: not "project failed", but "week-4 activation stuck below 30%".
- **Observable** — instrumented, or at least routinely reported. If nobody can see it, it is not a signal.
- **Owned** — a named person watches it and has authority to act.
- **Thresholded** — a value or date that triggers a pre-agreed response.

Template:

| Failure reason | Signal | Threshold | Response | Owner |
|---|---|---|---|---|
| Activation never happens on the invite path | Share of invitees who complete setup within 7 days | < 40% for two consecutive weeks | Review funnel, pause rollout to new cohorts | Growth PM |

Prefer signals that appear early and cheaply. A tripwire that fires only after the budget is spent is a postmortem waiting to happen.

## Response types

- **Prevent** — reduce likelihood by changing the design, sequencing, incentive, scope, or test plan.
- **Detect** — make the signal earlier or sharper through instrumentation or review cadence.
- **Contain** — reduce impact with staging, feature flags, staged rollout, rollback plans, contract terms, or a reserve.
- **Accept** — consciously do nothing, with a written rationale, a review date, and a named owner.

Residual risk remains after every response. Re-score the reason after hardening; if nothing moved, the hardening was probably documentation, not mitigation.

## Triage rules

- If a top reason has no named signal and owner, it is a wish, not a monitor.
- If every reason scores 3×3, the scoring is not discriminating. Force rank the top five, then score.
- If all mitigations are "monitor", the plan is not being strengthened — it is being watched fail.
- If a prevention cannot be implemented before the irreversible commitment, classify it as contain or accept, and say so.
- Revisit the table at the review date and whenever a threshold fires. A premortem that is never opened again is a ritual.

## Avoid

- Multiplying precise-looking numbers into a false sense of measurement.
- Treating the score as the decision; the conversation around outliers is the value.
- Ownerless actions, undated reviews, and thresholds with no response attached.
- Hiding accepted risks to make the plan look stronger; the record is the point.
