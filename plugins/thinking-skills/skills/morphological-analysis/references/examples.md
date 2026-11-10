# Worked Example — Onboarding Design Space

Situation: a B2B SaaS product activates only 34% of new accounts. The team has run three onboarding campaigns, all variations of the same email sequence. The design space, not the copy, is the problem.

## 1. Intake

- **Design:** onboarding for self-serve signups at a €49/month tier.
- **Success:** increase 14-day activation (first meaningful use of the core feature) from 34% to 45%.
- **Constraints:** two engineers for six weeks; no unsolicited phone calls in the EU; support team available 9:00–18:00 CET; budget for one messaging tool.
- **Artifact:** a shortlist of concepts for a pilot, not a full program.

## 2. Dimensions

Chosen because each is a decision someone can make independently:

- **D1 Trigger** — what event starts onboarding.
- **D2 Channel** — how the message or help arrives.
- **D3 Timing** — when, relative to the trigger.
- **D4 Owner** — who is responsible for the interaction.

Independence check: any trigger can pair with any channel, timing, and owner in principle. "Message content" was deliberately left out — it is a sub-choice of channel/owner and would triple the box without adding a decision.

## 3. The matrix

| D1 Trigger | D2 Channel | D3 Timing | D4 Owner |
|---|---|---|---|
| D1.1 signup | D2.1 in-app | D3.1 immediate | D4.1 automated |
| D1.2 first login | D2.2 email | D3.2 day 1–3 | D4.2 support |
| D1.3 first value event | D2.3 human call | D3.3 day 7 | D4.3 product |
| D1.4 14-day inactivity | D2.4 SMS/WhatsApp | D3.4 day 30 | D4.4 sales |

Raw size: 4 × 4 × 4 × 4 = **256 combinations**.

## 4. Pruning

Pairwise incompatibilities found:

| Pair | Reason | Removed |
|---|---|---|
| D2.2 email × D3.1 immediate | `latency` — email cannot arrive "immediately" enough to catch the signup moment | 16 |
| D2.3 call × D3.1 immediate | `no-capacity` — no one can call within minutes of signup at self-serve volume | 16 |
| D1.4 inactivity × D2.1 in-app | `no-channel` — the user is not in the app; in-app cannot reach them | 16 |
| D1.4 inactivity × D3.4 day 30 | `contradiction` — 30 days of silence is not a 14-day churn intervention | 16 |

Overlap between the last two pairs removes 4 combinations twice, so **196 survive**.

Also pruned by external filters: D4.4 sales × D1.4 inactivity (`out-of-scope` — self-serve tier has no sales owner), and any D2.3 call outside 9:00–18:00 CET (`not-allowed` operationally, not legally). These further reduce the space; the exact count is less important than recording why.

Note what was *not* pruned: "human call × day 7" feels expensive but is legal and feasible. Expensive is a score, not a contradiction.

## 5. Sample of 10

Chosen for coverage — every option appears at least once, plus baseline, extremes, and the obvious sweet spot.

| ID | Trigger | Channel | Timing | Owner |
|---|---|---|---|---|
| C1 | signup | in-app | immediate | automated |
| C2 | first value event | human call | day 7 | support |
| C3 | 14-day inactivity | SMS/WhatsApp | day 30 | automated |
| C4 | first value event | in-app | day 1–3 | product |
| C5 | signup | email | day 1–3 | automated |
| C6 | first login | human call | day 1–3 | support |
| C7 | 14-day inactivity | human call | day 30 | support |
| C8 | first login | SMS/WhatsApp | immediate | automated |
| C9 | first value event | email | day 30 | product |
| C10 | signup | human call | day 7 | sales |

Coverage: each trigger appears 2–3 times, each channel 2–4 times, each timing 2–3 times, each owner 2–4 times. C1 is the baseline; C2 and C7 are the high-touch extreme; C3 and C8 are the low-cost extreme.

## 6. Scoring sketch

Criteria fixed before scoring: activation lift (0.4), effort (0.3), risk (0.2), strategic fit (0.1).

| Combo | Lift | Effort | Risk | Fit | Weighted |
|---|---|---|---|---|---|
| C1 baseline | 2 | 5 | 5 | 3 | 3.1 |
| C4 value-event guide | 4 | 3 | 4 | 5 | 3.8 |
| C2 value-event call | 5 | 2 | 3 | 4 | 3.8 |
| C3 inactivity rescue | 3 | 4 | 4 | 4 | 3.6 |
| C6 first-login call | 4 | 2 | 3 | 3 | 3.3 |

The tie between C4 and C2 is a signal, not a problem: one is the scalable version, the other the high-touch version of the same insight. That is what synthesis is for.

## 7. Two synthesized concepts

**Concept 1 — Moment-of-Value Handoff** (C4 + C2).
The product watches for the first value event, then shows a short in-app checklist **immediately**; if the checklist is not completed by day 1–3, the account is queued for a support call that references the exact step where the user stopped. Mechanism: event listener → contextual checklist → conditional callback queue. Accepts the tradeoff of instrumentation work plus support capacity. Probe: instrument the event for 50 new accounts and compare completion against the current sequence.

**Concept 2 — Silent Rescue Lane** (C3 + C8).
No onboarding campaign at signup at all. The system waits for 14 days of inactivity, sends a WhatsApp message with a one-tap walkthrough, and escalates to a human call only after a second non-response. Mechanism: inactivity monitor → messaging automation → call escalation at day 30. Accepts lower warmth and reach for much lower cost and no dependence on email. Probe: run on a 10% cohort for six weeks; measure reactivation against a holdout, and check WhatsApp opt-in rate before committing.

## What the example demonstrates

- The dimensions produced combinations nobody had proposed — the team's three campaigns all lived in D2.2 × D3.2.
- Pruning removed contradictions, not preferences; "too expensive" stayed in and lost on score.
- Sampling guaranteed coverage before any scoring happened.
- The two concepts come from different corners (C4/C2 vs C3/C8), so the portfolio tests two mechanisms rather than two copies.
- Every concept ends in a probe that could falsify it.
