# Worked Example — Eight Onboarding Concepts

## Intake

**Prompt:** "How might we help a new analyst reach a first useful dashboard within their first day?"

**Audience:** B2B analytics product; analysts join teams that already have data, but the new analyst has no saved views and does not yet know the schema.

**Success:** first saved dashboard created and shared within day one.

**Constraints:** no new headcount; data must stay in the customer's warehouse; brand voice is plain, not gamified; SOC 2 review applies to any new data flow.

**Already tried:** a 12-step setup wizard and a library of help articles. Both have low completion; support tickets concentrate on "which dataset do I start with?".

**Fact / assumption / speculation:** the wizard's completion data is a fact; "analysts want to start from a template" is an assumption; "a peer cohort would lift day-one sharing" is speculation.

## The eight slots

| Slot | Concept (1–2 sentences) | Mechanism | Differs from | Assumption |
|---|---|---|---|---|
| 1 | A human onboarding buddy schedules two 30-minute sessions in week one and builds the first dashboard with the analyst, sharing their screen. | Done-for-you human setup | baseline | The customer has a spare expert for two sessions. |
| 2 | The analyst picks a role (finance, growth, ops) and lands in a prebuilt dashboard populated from their own warehouse schema. | Role-based template gallery | 1: artifact instead of person | Role predicts the first useful view. |
| 3 | Full product for 14 days, then automatic downgrade to the free tier; the first dashboard is kept but advanced features lock. | Reverse trial | 2: commercial trigger | Loss aversion motivates the first dashboard. |
| 4 | The first checklist item is "invite a teammate", and the dashboard is created in a shared workspace by default. | Shared-first default | 2: social artifact | Collaboration is the real activation event. |
| 5 | Connect the warehouse first; the product profiles the schema and generates three candidate dashboards before asking the analyst to configure anything. | Import-first auto-generation | 2: generation instead of selection | Schema profiling is accurate enough to suggest useful views. |
| 6 | New analysts join a weekly 30-minute cohort call with five peers from other companies; they leave with one dashboard each. | Peer cohort | 1: group instead of one-to-one | Cross-company peers will share openly. |
| 7 | The analyst states three questions they need answered; the product composes an onboarding path from the answers and skips everything else. | Goal-composed path | 4: user-authored sequence | Analysts can state useful questions on day one. |
| 8 | No onboarding: a sample workspace opens instantly, contextual tips appear only when the analyst is stuck, and the first real dashboard is created by duplicating and editing a sample. | Zero-setup contextual help | all: no prescribed sequence | Sample data plus tips is enough to reach a real view. |

## Variety audit

- Distinct mechanisms: done-for-you (1), template selection (2), commercial trigger (3), shared default (4), auto-generation (5), peer group (6), goal-composed path (7), zero-setup contextual (8). Eight mechanisms, but 1 and 6 both rely on people; 2, 4, 5, and 8 all intervene at first login.
- Axes touched: actor (human, product, peers), trigger (login, time, stuck, team event), form (service, artifact, default, cohort), incentive (trial loss, sharing), constraint removed (no setup, no configuration).
- Over-represented: in-product interventions (2, 4, 5, 7, 8). Under-represented: pricing and ecosystem.
- Outlier worth keeping: 6 (peer cohort) — the only concept that requires no product change.
- Candidate merge: 2 and 5 both produce a starter dashboard; keep them separate during generation because the mechanism differs (selection vs generation), then merge in clustering only if the probe is shared.

## Clusters

- **Done-for-you:** 1 (human) + 8 (product does the work by removing setup). Cluster name: remove the work, not the user.
- **Start from an artifact:** 2 + 5. Cluster name: first dashboard arrives pre-populated.
- **Commitment and timing:** 3 + 4 + 6. Cluster name: change when or with whom the first dashboard happens.
- **Self-directed:** 7. A singleton — the only concept that asks the analyst to define the goal first.

## Harvest — three concepts and probes

**A. Import-first auto-generation (5).**
Concept: connect the warehouse, let the product profile the schema, and present three candidate dashboards generated from the customer's own tables. The analyst edits one instead of building from blank.
Strongest assumption: schema profiling yields suggestions good enough to edit.
Probe: a two-week fake-door test with five design partners; measure whether the first suggested dashboard is saved or discarded within ten minutes. Signal to change course: fewer than half of sessions edit a suggestion.

**B. Zero-setup sample workspace (8).**
Concept: open into a sample workspace with real-shaped synthetic data; tips appear only on stall; the first real dashboard is a duplicate-and-edit of a sample.
Strongest assumption: analysts will trust a sample enough to duplicate it.
Probe: prototype with ten new analysts; measure time to first saved dashboard and whether they connect real data within the session. Signal: users browse but do not connect data.

**C. Reverse trial (3).**
Concept: give the full product for 14 days, then downgrade to free while keeping the first dashboard and locking advanced features.
Strongest assumption: losing advanced features motivates completion more than an expiring trial does.
Probe: cohort test against the current trial on activation and week-four retention; include a support-volume check, since downgrades generate tickets. Signal: activation rises but retention falls.

## Why not the others

Slots 1 and 6 depend on scarce human availability and were kept as later options rather than first probes. Slot 4 is cheap but likely a variant of the current wizard's sharing step; slot 7 assumes users can articulate goals before seeing data, which contradicts the support tickets. Slot 2 is the safest and is the fallback if 5 fails.

The portfolio is deliberately mixed: B is cheap and strange, A is ambitious and product-heavy, C is commercial and measurable. None is validated; each has a probe and a signal.
