# Worked Example — Guided Onboarding Launch

A B2B SaaS company plans a guided onboarding flow. The premortem is run three weeks before launch, with six people: the growth PM, two engineers, the head of CS, a support lead, and a sales engineer.

## 1. Intake

- **Proposal:** Replace email-only setup with a five-step in-product checklist and progress bar for all new Growth-plan accounts. Ships 16 November 2026.
- **Commitment:** Two engineers, one designer, six CS staff; no new headcount; launch announced to the board.
- **Success measure:** 45% of new accounts reach activation within 14 days (baseline 27%).
- **Failure horizon:** May 2027, six months after launch.

## 2. Declared failure scene

> It is May 2027. Guided onboarding failed. Activation is 22% against a 45% target, support volume is up 40%, two design partners have paused expansion, and the exec sponsor has moved the team to the billing migration.

The scene is stated as fact. Nobody argues about whether it will fail.

## 3. Independently generated reasons (12 of 31, clustered)

| # | Category | Reason |
|---|---|---|
| 1 | Assumption | Most new users do not start at signup — they accept an admin invitation days later, so the checklist appears before they have an account context. |
| 2 | Assumption | The checklist measures setup steps, but customers define value as sending their first invoice; activation is measured at the wrong moment. |
| 3 | Assumption | The progress bar resets when an invited user signs in on a different device. |
| 4 | Coordination | CS is not trained before launch and keeps pointing customers at last quarter's PDF playbook. |
| 5 | Coordination | Sales hands new accounts to implementation, not CS; nobody owns the first 14 days. |
| 6 | Coordination | The in-app help content is owned by marketing, which has not been asked to update it. |
| 7 | Incentive | Support is measured on time-to-close, so agents give manual walkthroughs that close the ticket without teaching the flow. |
| 8 | Incentive | CS bonus is tied to renewal, not activation, so low-touch accounts get no attention until renewal risk appears. |
| 9 | Capability | No funnel events exist beyond signup; the team cannot see where users drop off and will iterate blind. |
| 10 | Capability | The one analytics engineer is shared with two other launches and the dashboard is scheduled for "phase two". |
| 11 | External | A key enterprise customer mandates SSO/SCIM, and procurement blocks the new flow until a compliance review completes. |
| 12 | External | A competitor bundles free onboarding calls, resetting the perceived value of a self-serve checklist. |

## 4. Clusters

Five causal stories, not twelve labels:

1. **Wrong activation moment** (1–3): the flow triggers at signup and measures setup, while real activation begins at invitation acceptance and ends at first invoice.
2. **CS and Sales not enabled** (4–6): the humans who touch new accounts still run the old playbook, with no owner for the first 14 days.
3. **Incentives reward the old path** (7–8): support and CS are paid to close tickets and renew, not to activate.
4. **Blind iteration** (9–10): no instrumentation, so nobody can tell which step fails.
5. **Enterprise SSO dependency** (11–12): a customer-driven requirement can block the rollout, and a competitor can reset value perception.

## 5. Prioritization

| Reason | L | I | L×I | Warning signal | Threshold |
|---|---|---|---|---|---|
| Wrong activation moment | 4 | 4 | 16 | Invite→first-value completion, split by signup vs invite path | < 40% on the invite path for two consecutive weeks |
| CS/Sales not enabled | 4 | 3 | 12 | Share of new accounts with no CS contact in 14 days | > 50% |
| Incentives reward old path | 3 | 4 | 12 | Tickets tagged "manual setup" / "walkthrough" | > 15% of onboarding tickets |
| Blind iteration | 4 | 3 | 12 | Events missing or funnel dashboard stale | Any missing event at week 2; week-2 completion < 25% |
| Enterprise SSO dependency | 2 | 5 | 10 | Procurement/compliance blockers in the pipeline | Any top-20 account freezing rollout |

Top three for hardening: **wrong activation moment** (16), **CS/Sales not enabled** (12), and **blind iteration** (12). The incentive cluster shares a mechanism with CS enablement, so it is hardened in the same package. The SSO dependency is a high-impact wildcard: contain and monitor, do not redesign the flow around it.

## 6. Hardening

| Failure reason | Prevention (changes the plan) | Monitor: signal → threshold → response | Owner | By |
|---|---|---|---|---|
| Wrong activation moment | Redefine activation as "first invoice sent within 14 days of invitation acceptance"; trigger the checklist on invitation acceptance, not signup; persist progress across devices. Launch slips one week. | Invite→first-invoice < 40% for two weeks → pause rollout to new cohorts and review the funnel with five customers. | Growth PM | 2 Nov |
| CS/Sales not enabled + incentives | Train all six CS staff; replace the PDF playbook; make 14-day activation the primary CS metric with ticket-quality as a guardrail; name CS as owner of days 0–14; add in-app "talk to CS" tagged as an activation handoff. | > 50% of new accounts with no CS contact in 14 days, or > 15% manual-setup tickets → retrain and review the comp plan. | Head of CS | 9 Nov |
| Blind iteration | Ship five funnel events and a daily dashboard **before** launch; weekly 30-minute funnel review for eight weeks; define kill criteria in advance. | Missing event, or week-2 completion < 25% → pause rollout, fix instrumentation, do not interpret the funnel. | Analytics lead | 2 Nov |
| Enterprise SSO dependency (accepted) | Run a two-day SSO/SCIM compatibility spike; add a rollback clause for enterprise cohorts; do not gate the general launch on it. | Any top-20 account pausing procurement → switch that cohort to the legacy flow and escalate. | Enterprise PM | 15 Dec |

## 7. What changed

- Launch moved from 9 to 16 November to land instrumentation and training first.
- Activation metric redefined, with a separate invite-path cohort.
- CS compensation changed, with a quality guardrail to prevent gaming.
- Rollout staged 10% → 50% → 100% instead of a single switch.
- Enterprise SSO risk accepted and contained, with an explicit owner and review date — not silently ignored.

## What good looks like

- The failure was asserted, then explained; the team never slid into "will it fail?".
- Reasons named mechanisms and owners, not labels like "adoption risk".
- The top reasons changed real decisions: date, metric, compensation, instrumentation.
- One accepted risk was recorded rather than mitigated for appearances.
- Every monitor had a threshold, a response, and a person — not just a dashboard.

## What this example is not

It is an illustration, not evidence that this launch succeeded. A premortem improves the identification and treatment of plausible failure reasons; it does not predict the future or substitute for a pilot.
