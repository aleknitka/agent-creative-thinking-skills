# Worked Example — "Onboarding Must Be a Tutorial"

This is a constructed composite, not a report from a real company. The numbers are invented to show the method; they are not evidence about any actual product. Label them as illustration if you reuse the example.

## Intake

- **Stated problem:** "Redesign onboarding so more new users complete the six-step tutorial."
- **Goal behind it:** new users reach first value quickly and stay.
- **Told-hard constraints:** the tutorial is required by product policy; support is in-app chat only; the launch is this quarter.
- **Tried already:** shorter copy, progress bar, tooltip redesign. Completion rose; retention did not.
- **Appetite:** medium — willing to change the flow, not the pricing or data model.
- **Problem as assertion:** "New users must complete a guided tutorial before they can use the product, because they otherwise fail to activate."

The phrase "redesign onboarding" already smuggled in a solution. That is the first thing to inventory.

## Inventory (10 beliefs)

| ID | Belief | Family | Source / evidence | Confidence | If false |
| --- | --- | --- | --- | --- | --- |
| A1 | First value requires understanding most features | Origin: inherited | "Best practice"; no test | Low | Teaching fewer things may raise activation |
| A2 | Users must complete a tutorial before using the product | Continuity + boundary | Product policy, no owner cited | Low | Users can start in the product immediately |
| A3 | Tutorial completion causes retention | Origin: inherited | Correlational dashboard only | Low | The metric is a proxy, not a lever |
| A4 | Users abandon because steps are too long | Proven-ish | Funnel shows step-3 drop | Medium | Drop may be intent, not effort |
| A5 | A six-step flow is the smallest viable onboarding | Boundary | Team estimate | Low | A one-task start could work |
| A6 | Support cannot handle users who skip onboarding | System + stakeholder | Anecdote from two agents | Low | Self-serve could carry the load |
| A7 | New users arrive with a task they want to do | Stakeholder | Not measured | Low | If true, task-first onboarding is natural |
| A8 | Account creation must precede any value | Continuity | Legacy architecture | Low | Guest or sandbox-first becomes possible |
| A9 | The quarter deadline is fixed | Boundary | Verbal VP commitment; no external date | Medium | Staged rollout or narrower scope becomes viable |
| A10 | Buyers, not end users, decide setup | Stakeholder | Sales calls | Medium | Admin-led setup could remove end-user onboarding |

A1–A3 and A8 are load-bearing for "redesign the tutorial." A4 looks like a fact about the current flow; it is useful but does not by itself justify a tutorial.

## Pressure-test the top beliefs

Ranking (impact × uncertainty): A2 = 9, A3 = 9, A7 = 6, A8 = 6, A9 = 4.

### A2 — users must complete a tutorial first

- **Falsify:** find a cohort that bypassed the tour (support override, legacy accounts, API-created workspaces) and compare 7-day activation. If bypassers activate at similar rates, the belief is false in practice.
- **Unnecessary:** remove the tour in thought. Does the stated harm ("users fail to activate") have a mechanism, or is it "they might miss features"? If the harm is feature awareness, the goal is not activation and the belief is solving the wrong problem.
- **Reversal:** "users must never see a tutorial." What would make that work? Task templates, an empty state with one obvious action, contextual hints after use.

Result (illustrative): 1,900 accounts created through an integration skipped the tour. Their 7-day activation rate was 41%, versus 39% for tour completers. Label: **fact about this dataset**, not proof of causation — bypassers may differ. Enough to stop treating the tour as a requirement and run a real probe.

### A3 — completion causes retention

- **Falsify:** segment completers by whether they completed on day 0 or were nudged on day 3. If late completers retain like non-completers, completion is a marker of intent, not a cause.
- **Unnecessary:** what would retention look like if the tour existed but nobody counted completion? Remove the metric from the goal and see whether the program still makes sense.
- **Reversal:** "retention causes completion" — engaged users finish tours. Plausible; check which direction the time series supports.

Result (illustrative): day-0 completers retained at 2.3× non-completers, but day-3 nudged completers retained at 1.1×. Label: **assumption revised** — completion is partly a selection effect. Retention is the goal; the tutorial is not the lever.

### A7 — users arrive with a task

- **Falsify:** ask in the signup survey or inspect the first action after account creation. If most first actions are exploratory rather than task-driven, task-first onboarding is a poor fit.
- **Unnecessary:** if users arrive task-less, maybe the product needs a starter artifact, not a task.
- **Reversal:** "users arrive with no task and no intention" — then the job is to create a reason to act, not to teach features.

Result (illustrative): 62% of new workspaces modified the default template within the first session. Label: **assumption supported for one segment**, not all. This points to segment-specific onboarding rather than one flow.

## Reframes

Three distinct statements, each removing a different belief:

1. **How might new users reach first value without ever seeing a tutorial?** (removes A2; mechanism: task-first empty state with one real action and contextual hints)
2. **How might onboarding be measured by time-to-first-value rather than tutorial completion?** (removes A3 as the target; mechanism: instrument the activation event, make the tour optional and unmeasured)
3. **How might the customer's admin set up the workspace so end users need no onboarding at all?** (removes A10 and A2; mechanism: admin templates, import from the customer's existing tool, invite-with-context)

Kept fixed: the goal (faster first value, higher retention), the real constraints (data retention policy, abuse controls), and the quarter deadline for the *first* probe — not for a full redesign.

## Probes

| Probe | Belief | Observation | Decision rule | Cost |
| --- | --- | --- | --- | --- |
| Cohort comparison | A2 | 7-day activation for tour-bypass vs. tour-complete, matched on acquisition channel | Bypass ≥ completion → make tour optional; bypass < completion by >10 pts → keep gate and investigate | 2 hours |
| Session replay + 5 interviews | A7 | First meaningful action after signup | ≥50% start a real task → build task-first empty state; otherwise explore starter artifacts | 2 days |
| Clickable prototype | A2, A5 | 10 target users attempt first value with the tour removed | ≥6 succeed unaided → prototype test with real traffic; ≤3 → tour content is the problem, not the gate | 3 days |
| Instrumentation change | A3 | Retention of day-0 vs. nudged completers | Late completers retain ≈ non-completers → stop using completion as success metric | 1 day |

All labels in the example are **illustrative**. In a real run, cite the query or source for each result and record its scope.

## Decide next

Recommendation: **proceed with reframe 1 and 3 conditionally**, gated by the cohort comparison and five interviews. Do not run a full redesign on the current evidence. Record A3 as a revised assumption (selection effect) and A9 as a real but negotiable boundary.

Handoff: if the task-first direction needs many alternative mechanisms, run `lateral-thinking` inside reframe 1; if the admin-led direction needs a business case, run `premortem` on it. If leadership insists on the tutorial, the artifact to bring is the assumption inventory plus the cohort result — not an opinion about tutorials.

## What made this work

- The inventory included the problem statement's own assumption ("redesign the tutorial"), not just the flow's internals.
- The team tested the belief with existing data before proposing new research.
- The reframes removed different beliefs rather than rewording one.
- Every probe had a decision rule and an owner-sized cost.
- Disconfirming evidence was recorded and used to weaken the belief, not reinterpreted to save it.
