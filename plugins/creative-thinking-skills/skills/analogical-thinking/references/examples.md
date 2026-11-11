# Two Worked Analogies, With Limits

Each example runs the six steps and shows the principle, the breakpoints, and the probe. The limits are not a disclaimer; they are part of the result.

## Example 1 — Onboarding abandoners → airport wayfinding

### Intake

A B2B analytics product loses 40% of new accounts during setup. Users must connect a data source, choose a workspace schema, invite teammates, and build a first dashboard. Most drop off after connecting data. Help is a searchable docs site. The goal is more accounts reaching a first useful dashboard; the constraint is that onboarding cannot require a sales call.

### Abstract to structure

"An agent with partial information must traverse a sequence of decisions toward a destination, under time pressure and low tolerance for backtracking, with sparse human help. State is not visible; each wrong turn raises the chance of abandonment."

### Search

Candidates: airport wayfinding, museum exhibits, IKEA assembly instructions, GPS navigation, hospital patient intake, tax filing. Shortlist airport wayfinding and IKEA instructions. Wayfinding wins because it handles *decision points and confirmation*, not just instruction ordering.

### Map

| Source | Relation | Local | Holds? |
|---|---|---|---|
| Departure board | Shows current position against destination | Progress indicator with named remaining steps | Yes |
| Repeated signage at each decision | Destination and current terminal restated before the choice | Step header restating goal and current state | Holds with adaptation |
| Landmarks | Confirm you are still on the path without a map | Persistent "you are here" summary | Yes |
| Recoverable wrong turns | Return path exists; signs back to main route | Ability to change schema choice without restarting | Absent; must add |
| Signage standards | Consistent vocabulary across all signs | Consistent step names in UI and docs | Partly; docs use different names |

Mechanism: wayfinding works by **restating destination and current state at each decision point, plus making wrong turns recoverable**. The airport does not teach you the terminal layout; it confirms your position at the moment you must choose.

### Limits and breakpoints

| Dependency | Airport | Product | Consequence |
|---|---|---|---|
| Captive audience | Must walk through | Can close the tab | Signage alone cannot retain; need value before friction |
| Decision frequency | Infrequent, high stakes | Frequent, low stakes | Experts will find repeated confirmation annoying |
| Personalization | Impossible | Expected | Static signs underuse available context |
| Physical consistency | Regulated | Easy to drift | Without governance, step names diverge again |

Verdict: mechanism adapts, but only for first-time setup. For repeat users, keep checkpoint confirmation minimal or collapsible.

### Principle and probe

**Principle:** when an agent makes a sequence of low-information choices under abandonment risk, restate destination and current state at each irreversible decision, and make the last choice reversible. It fails when the audience is expert and repeated, or when the agent cannot return.

**Probe:** add a step header ("Step 2 of 4 — choosing schema; this sets how metrics are grouped") and an undo path for schema choice to one onboarding cohort. Measure drop-off at each step and schema-change rate. Falsified if drop-off does not move or if completion time rises without a retention gain.

## Example 2 — Incident dispatch → emergency department triage

### Intake

An on-call platform routes production incidents to engineers. Arrival order drives assignment; the loudest reporter often gets attention first. Some low-severity incidents wait days, while a few severe ones are noticed late. There are limited specialists, and severity is usually unclear at intake. The goal is faster handling of high-cost incidents without starving quieter but important work.

### Abstract to structure

"Multiple arrivals with unknown, unequal urgency compete for a small set of specialized handlers under incomplete information. Delay cost varies by case and is not observable at arrival. Assignment is partly irreversible; reassignment wastes scarce attention."

### Search

Candidates: emergency department triage, air-traffic sequencing, field-service dispatch, restaurant kitchen pass, military casualty evacuation. Shortlist ER triage and kitchen pass. ER triage wins because it handles *unknown urgency plus reserved capacity*; the kitchen pass is better at sequencing but assumes known order times.

### Map

| Source | Relation | Local | Holds? |
|---|---|---|---|
| Acuity sorting | Priority from observed signals, not arrival order | Severity rubric applied at intake | Holds with adaptation |
| Vitals | Independent measurements resist self-report | Automated signals (error rate, affected users) | Partly; many incidents lack clean signals |
| Reassessment | Condition rechecked after initial treatment | Severity review after first diagnosis | Yes |
| Resuscitation bay | Capacity reserved for worst cases | Reserved specialist lane | Yes |
| Escalation criteria | Specialist involvement only when criteria met | Escalation playbook | Yes |
| Legal mandate to treat | Cannot refuse a patient | Can deprioritize indefinitely | Absent |

Mechanism: triage separates **urgency estimation** from **assignment**, uses independent signals where possible, reassesses after new information, and protects capacity for the worst cases. It does not rely on arrival order or on the reporter's claim.

### Limits and breakpoints

| Dependency | ER | Incidents | Consequence |
|---|---|---|---|
| Cost of false negative | Potentially fatal | Usually recoverable | ER over-invests; you can accept more risk |
| Signal quality | Measured vitals | Noisy, sometimes missing | Acuity score needs uncertainty handling and override |
| Parallelism | One patient per bay | Many incidents can be worked in parallel | Queueing model differs; less need for strict sequencing |
| Mandate | Must treat | Can defer | Need an explicit starvation guard, not a legal one |
| Metric gaming | Waiting-time targets can distort | Severity labels can be gamed | Audit labels; rotate reviewers |

Verdict: the sorting-and-reserve mechanism holds; the enforcement mechanism fails. Replace legal mandate with a visible aging rule for deferred incidents.

### Principle and probe

**Principle:** when urgency is unknown at arrival and delay costs differ, classify on independent signals and reversibility rather than on arrival order or reporter volume; reserve a lane for the highest-cost class and age the rest explicitly. It fails when signals are absent or fully self-reported, or when all cases can be parallelized cheaply.

**Probe:** add a two-question intake (customer impact, reversibility) plus an aging alarm for incidents untouched after 24 hours; compare time-to-first-response for high-impact cases and the share of low-severity incidents older than a week. Falsified if high-impact latency does not improve or if aging alarms flood the queue.

## What both examples show

- The transferable part is a **mechanism plus boundary conditions**, not the source's vocabulary.
- The most valuable step is the breakpoint table; it converts "we're like an ER" into a specific design rule and a specific non-rule.
- The probe is small and can fail. An analogy that cannot fail is not being used as evidence.
