# Worked Example — Clinic No-Shows, 18 Ideas → 3 Concepts

A three-site community health clinic wants to cut missed appointments. Six weeks, no new headcount, limited EHR changes, 70% of patients on smartphones and 25% without one. Three staff run brainwriting in a 50-minute session: the operations lead (P1), a front-desk supervisor (P2), and a nurse practitioner (P3).

The prompt is written on each sheet: *"How might we reduce missed appointments without adding staff, given limited EHR changes and mixed phone access?"* No examples are circulated.

## Pass 1 — silent, 8 minutes, 3 ideas each

| ID | Idea |
|---|---|
| P1-1 | SMS reminder 48 hours before with "reply 1 to confirm". |
| P1-2 | Same-day morning text with clinic address, entrance, and parking. |
| P1-3 | Ask patients to book the next appointment before they leave. |
| P2-1 | Call patients who missed twice in six months and ask why. |
| P2-2 | Auto-fill cancellations by texting the next three people on a waitlist. |
| P2-3 | Move high no-show slots (Monday 8am) to times patients actually choose. |
| P3-1 | Bus fare reimbursement for patients who need it. |
| P3-2 | Reminder call in the patient's preferred language by a community health worker. |
| P3-3 | Overbook 10% of slots. |

No one speaks. The timer is visible.

## Pass 2 — silent, 5 minutes, extend your own list

| ID | Builds on | Idea |
|---|---|---|
| P1-4 | P1-1 | Make confirmation one tap, no typing; escalate to a voice call if unconfirmed at 24 hours. |
| P1-5 | P1-2 | Add a "running late?" link that moves the appointment later the same day instead of weeks out. |
| P1-6 | P1-3 | At booking, let the patient choose a backup day; offer that slot first if they cancel. |
| P2-4 | P2-1 | Log miss reasons with three codes (transport, childcare, work) and review monthly. |
| P2-5 | P2-2 | Waitlist prioritises patients overdue for preventive care, not first-come. |
| P2-6 | P2-3 | Publish a weekly no-show heatmap by slot and change the schedule every two weeks. |
| P3-4 | P3-1 | Partner with a rideshare voucher accepted by two local services, capped per patient per quarter. |
| P3-5 | P3-2 | Train two front-desk staff as language navigators instead of hiring community workers. |
| P3-6 | P3-3 | Overbook only no-show-heavy slots, and route freed slots to the waitlist. |

Eighteen entries, all verbatim, all with stable IDs.

## Distribute and build — one rotation, 6 minutes

Sheets pass clockwise. Builds are annotations, not new entries, so the raw count stays 18:

- P2 adds to **P1-4**: attach a calendar invite so the confirmation lands in the patient's phone calendar.
- P3 adds to **P2-2**: include a "can you come in two hours?" rapid option in the waitlist text.
- P1 adds to **P3-5**: navigators should work the 24-hour escalation call list, not a separate queue.
- P2 adds to **P1-6**: offer the backup day at the end of the booking call, while the patient is still deciding.
- P3 adds to **P2-6**: split the heatmap by site; one site's Monday problem is another's Friday problem.
- P1 adds to **P3-4**: check whether the voucher scheme is reimbursable before piloting.

No entry is crossed out or rewritten.

## Cluster — frozen board

Three clusters, all 18 entries accounted for.

| Cluster | Theme | Members | Build trail |
|---|---|---|---|
| C1 "Confirmed arrival" | Reach the patient twice, in their language, and make confirming effortless | P1-1, P1-2, P1-4, P1-5, P2-2, P2-5, P3-2, P3-5 | P1-4 → P1-1; P3-5 → P3-2; P2-5 → P2-2 |
| C2 "Attendance logistics" | Remove the concrete obstacle that makes attendance impossible | P2-1, P2-4, P3-1, P3-4 | P2-4 → P2-1; P3-4 → P3-1 |
| C3 "Patient-shaped schedule" | Book and staff the slots patients can actually attend | P1-3, P1-6, P2-3, P2-6, P3-3, P3-6 | P1-6 → P1-3; P2-6 → P2-3; P3-6 → P3-3 |

Spread: every cluster has entries from all three participants, and C1 and C3 contain build edges from more than one author.

## Harvest — three concepts and one probe each

### Concept 1 — The two-touch confirmation loop (C1)

At booking, capture language preference and attach a calendar invite. Send a one-tap SMS 48 hours out; if unconfirmed at 24 hours, a trained front-desk navigator calls in the patient's language. An unconfirmed slot is offered to a care-gap-prioritised waitlist, with a "can you come in two hours?" rapid option.

**Probe:** run on one site for four weeks. **Signal:** ≥60% confirmed at 24 hours and a no-show rate at least 3 points below the site's baseline; if not, test whether the escalation call or the one-tap message is doing the work.

### Concept 2 — Name the obstacle and pay for it (C2)

Every miss gets one of three reason codes at the next contact. Patients with two or more misses in six months get a call that asks what got in the way. Where transport is the code, offer a capped rideshare voucher through two local services; check reimbursement rules first.

**Probe:** call 40 patients with two or more misses, code reasons, and offer vouchers to half. **Signal:** rebook rate within two weeks and whether transport-coded patients actually redeem; if redemption is near zero, the barrier is not price.

### Concept 3 — Build the schedule from attendance data (C3)

Publish a weekly site-level no-show heatmap. Move or retire the worst slots, publish the revised schedule every two weeks, and let patients choose a backup day at booking. Overbook only the historically heavy slots, routing freed time to the waitlist.

**Probe:** two weeks of heatmap data before changing anything, then change the three worst slots per site. **Signal:** no-show rate on those slots versus unchanged slots, with volume checked so the clinic is not simply filling easier slots.

## What good looks like

- Generation stayed silent through both passes; the build pass added combinations rather than opinions.
- The 18 entries were kept verbatim with IDs, so every concept traces back to specific written ideas.
- Build edges identified which ideas resonated across authors — those fed the strongest concepts.
- Three concepts each carry a mechanism, a probe, and a keep/kill signal; none is a theme restated.
- One idea (P3-3, blanket overbooking) survived only in modified form inside C3; the raw version was not adopted.

## What this example is not

It is an illustration, not evidence that these interventions work. The numbers are invented for the example, and the probes are designed to produce evidence, not to confirm the concepts. Run your own baseline before claiming an effect.
