# Worked Example — Onboarding Friction, 8 Petals → 72 Slots → Top 5

## Intake

**Theme (center):** "How might we reduce onboarding friction for new analysts in their first week?"

**Audience:** B2B analytics product. Analysts join teams that already have data, but the new analyst has no saved views, does not know the schema, and cannot yet tell which questions matter.

**Success:** first saved dashboard created and shared within the first week (not day one — that was the earlier, unrealistic target).

**Constraints:** no new headcount for customer success; data stays in the customer's warehouse; plain brand voice, no gamified streaks; SOC 2 review for any new data flow.

**Already tried:** a 12-step setup wizard (low completion) and a help-article library (support tickets still concentrate on "which dataset do I start with?").

**Fact / assumption / speculation:** wizard completion data is a fact; "analysts want to start from a template" is an assumption; "peer cohorts lift sharing" is speculation.

## Layer 2 — the eight petals

| # | Petal | Angle |
|---|---|---|
| 1 | Actors | who does the setup work, who is missing |
| 2 | Moment | when in the first week friction bites |
| 3 | Place | where the analyst works: product, inbox, chat, call |
| 4 | Mechanism | how the first dashboard actually gets built |
| 5 | Incentive | what makes sharing feel worth it |
| 6 | Artifact | what object carries guidance: template, checklist, sample |
| 7 | Constraint | which limit can be removed or moved |
| 8 | Signal | how we would know friction dropped |

Check: petals 3 and 6 could overlap around templates; they were kept because 3 is about location of the work and 6 about the object itself. The group accepted the risk and watched for duplicates during pruning.

## Layer 3 — selected blocks

At eight petals the board holds 72 slots. Below are two complete blocks, three partial blocks, and the rest summarised by mechanism.

### Petal 2 — Moment (complete)

| Slot | Idea | Mechanism |
|---|---|---|
| 2.1 | Show a "start here" dashboard the moment the warehouse connects, before any settings. | Zero-config first artifact |
| 2.2 | Ask one question at first login ("What do you need to report on this week?") and build the path from it. | Single-question intake |
| 2.3 | Delay the schema tour until the analyst has opened a real table and gotten stuck. | Just-in-time teaching |
| 2.4 | Put the setup wizard *after* the first dashboard, as a cleanup step. | Reorder setup and value |
| 2.5 | Trigger a buddy invite at the analyst's first failed query, not at signup. | Failure-triggered help |
| 2.6 | Send the first "your team's dashboards" digest on day two, not day one, when the analyst knows enough to care. | Delayed relevance |
| 2.7 | Compress onboarding to a single 10-minute session and move everything else into weekly tips. | Front-load then drip |
| 2.8 | Let the analyst skip onboarding and return to it from a persistent "unfinished setup" nudge. | Skippable sequence |

### Petal 4 — Mechanism (complete)

| Slot | Idea | Mechanism |
|---|---|---|
| 4.1 | Profile the warehouse schema and generate three candidate dashboards. | Import-first auto-generation |
| 4.2 | Role-based template gallery populated from the customer's own tables. | Selection over construction |
| 4.3 | Analyst states three questions; product composes a path and skips the rest. | Goal-composed path |
| 4.4 | Duplicate-and-edit a sample dashboard rather than building from blank. | Edit an artifact |
| 4.5 | A teammate's dashboard is cloned with a diff view showing what to change. | Social cloning |
| 4.6 | Natural-language request ("show weekly active users by plan") produces a draft. | NL-to-dashboard |
| 4.7 | Guided query builder that teaches the schema as the analyst clicks. | Learn-by-querying |
| 4.8 | No onboarding: sample workspace opens instantly, tips appear only on stall. | Zero-setup contextual help |

### Petal 1 — Actors (partial)

| Slot | Idea |
|---|---|
| 1.1 | A customer-side onboarding buddy builds the first dashboard with the analyst. |
| 1.2 | The analyst's manager nominates the first three questions before day one. |
| 1.3 | A peer from another company joins a 30-minute cohort call. |
| 1.4 | Support watches for the first "which dataset?" ticket and calls instead of replying. |
| 1.5 | The product itself acts as the onboarding owner, with no human step. |

### Petal 5 — Incentive (partial)

| Slot | Idea |
|---|---|
| 5.1 | First shared dashboard unlocks a team workspace. |
| 5.2 | Reverse trial: full product for 14 days, then downgrade keeping the first dashboard. |
| 5.3 | Public "first dashboard" recognition inside the customer's team. |
| 5.4 | Setup completion reduces the next invoice by a small amount. |

### Petal 7 — Constraint (partial)

| Slot | Idea |
|---|---|
| 7.1 | Remove the mandatory data-model step from the first week. |
| 7.2 | Remove the need to know SQL entirely for the first dashboard. |
| 7.3 | Move SOC 2 review earlier so template data flows are pre-approved. |
| 7.4 | Treat "no new headcount" as fixed; make the product the onboarding owner. |

### Petals 3, 6, 8 — summarised

**Place:** in-product first-run, email digest, Slack bot, live call, sample workspace, shared workspace, mobile check-in, in-app help panel.
**Artifact:** role template, question checklist, sample dataset, annotated screenshot, diff view, video walkthrough, one-page cheat sheet, saved query.
**Signal:** time to first saved dashboard, first-share rate, "which dataset" ticket count, day-seven return, path-completion rate, template edit rate, cohort call attendance, week-four retention.

Total across the board: **8 petals + 64 sub-ideas = 72 slots.** The sample above shows 37; the rest were generated and are omitted here for length.

## Prune and score

Pruning merged 14 near-duplicates (mostly template selection under petals 4 and 6) and cut 9 constraint violations (new data flows without SOC 2 review, headcount-dependent items). That left 49 survivors.

Criteria fixed at intake, weighted equally: (1) time to first shared dashboard, (2) implementation cost, (3) support-load impact, (4) differentiation from the current wizard, (5) reversibility if it fails.

Top scores clustered around petals 2, 4, and 7 — timing, mechanism, and constraint removal — not around incentives or place. That is itself a finding: the board says friction is mostly *sequence and construction*, not motivation or channel.

## Harvest — top five with probes

**1. Import-first auto-generation (4.1).**
Concept: connect the warehouse; the product profiles the schema and presents three candidate dashboards built from the customer's own tables; the analyst edits one.
Strongest assumption: schema profiling produces suggestions good enough to edit.
Probe: two-week fake-door with five design partners; measure whether the first suggestion is saved or discarded within ten minutes. Kill signal: fewer than half the sessions edit a suggestion.

**2. Duplicate-and-edit a sample (4.4, reinforced by 6.3).**
Concept: new analysts land in a real-shaped sample workspace and create their first real dashboard by duplicating and editing it.
Strongest assumption: analysts trust a sample enough to duplicate it.
Probe: prototype with ten new analysts; measure time to first saved dashboard and whether real data is connected in-session. Kill signal: browsing without connecting data.

**3. Skippable sequence with an unfinished-setup nudge (2.8, 2.4).**
Concept: onboarding is optional from first login; a persistent, dismissible nudge returns the analyst to setup when they are ready, after value rather than before it.
Strongest assumption: skipping setup increases first-week activation instead of leaving users stranded.
Probe: A/B against the current wizard on first-share rate and "which dataset" tickets. Kill signal: activation rises but week-four retention drops.

**4. Just-in-time schema help triggered by the first failed query (2.3, 1.4).**
Concept: no schema tour up front; the first failed query triggers a short, contextual explanation and an offer of a human call.
Strongest assumption: failed queries are frequent enough and legible enough to trigger on.
Probe: instrument failed-query events for two weeks and test the trigger copy on a support cohort. Kill signal: failed queries are too rare or too varied to classify.

**5. Reverse trial (5.2).**
Concept: 14 days of full product, then downgrade to free while keeping the first dashboard and locking advanced features.
Strongest assumption: losing advanced features motivates completion more than an expiring trial.
Probe: cohort test against the current trial on activation and week-four retention, plus a support-volume check. Kill signal: activation up, retention down, tickets up.

Portfolio logic: (1) is ambitious and product-heavy, (2) is cheap and artifact-based, (3) is a sequence change with no new tech, (4) is diagnostic and may produce a negative result cheaply, (5) is commercial and measurable. None is validated.

## Why not the others

The buddy and cohort ideas (1.1, 1.3) scored well on activation but depend on scarce human availability and contradict "no new headcount". The NL-to-dashboard idea (4.6) is attractive but its cost and SOC 2 exposure make it a later bet. Incentive ideas (petal 5) scored low because the tickets point at construction friction, not motivation. The sample-workspace idea (4.8) survives inside concept 2 rather than as a separate probe, since both test trust in synthetic data.

## What the board taught

- Friction concentrated in *when* setup happens and *how* the first dashboard is built; the petals made that visible before scoring.
- Eight petals were enough to separate motivation from construction. A flat list of 72 would have mixed them.
- The prune count (14 merges) was highest between petals 4 and 6 — evidence that "template" and "artifact" overlap in this domain, useful for the next board's petal design.
- Five probes were scheduled; the board itself produced no evidence.
