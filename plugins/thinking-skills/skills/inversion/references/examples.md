# Worked Example — Guaranteeing Onboarding Failure

A B2B SaaS company wants **60% of new accounts to reach first value within 7 days** (a successful workflow run). The current rate is 34%. The team's plan is a checklist of positive actions: better emails, a new tour, a help centre refresh. Inversion starts by asking how to guarantee the goal never happens.

## Step 1 — Intake

- **Goal:** 60% of new accounts reach first value within 7 days.
- **Who:** operations leads at mid-market companies, arriving from a sales-assisted trial.
- **Horizon:** next quarter.
- **Constraints:** two engineers, no pricing change, current CRM.
- **Tried:** welcome email sequence, one 30-minute kickoff call per account.
- **Labels:** the 34% baseline is **fact**; "the tour is the problem" is **assumption**; "competitors convert better" is **speculation**.

## Step 2 — Define success and the unwanted outcome

- **Success:** ≥60% of accounts created in a cohort run one successful workflow within 7 days, measured from account creation.
- **Unwanted:** accounts stall after setup, go quiet, and churn at renewal with "we never really used it."
- Both are observable, so failure routes can be concrete.

## Step 3 — Invert

**Question:** *How could we guarantee that new accounts never reach first value?* Fifteen routes, unfiltered:

| ID | Route |
|---|---|
| F1 | Pay sales on closed deals, with no activation component. |
| F2 | Leave onboarding in the support queue, with no named owner. |
| F3 | Track signups and logins as the success dashboard. |
| F4 | Require admin configuration and data import before anything works. |
| F5 | Make the workspace invite-only, so the first task needs colleagues who were never invited. |
| F6 | Ship empty defaults; require the user to create all data from scratch. |
| F7 | Hide help in a documentation site, and staff chat with a billing bot. |
| F8 | Send onboarding emails on a fixed schedule regardless of user state. |
| F9 | Store no progress, so a returning user starts over. |
| F10 | Expire the trial in 14 days from signup, not from first value. |
| F11 | Sell to anyone; let buyers choose a use case the product does not support. |
| F12 | Measure support on ticket-close time, so tickets close without the problem being solved. |
| F13 | Double signups with a campaign while support capacity stays flat. |
| F14 | Ship a broken mobile experience; users start on a phone. |
| F15 | Let data import fail silently for the two most common CRM formats. |

F9 and F13 are the routes a positive plan rarely names: neither is a feature, and both are standing conditions. That is the usual yield of inverting.

## Step 4 — Cluster

| Cluster | Causal story | Routes |
|---|---|---|
| **C1 — Unowned activation** | Sales is paid on deals and support on closure, so nobody is rewarded for the 7-day outcome and the drop-off is never reviewed. | F1, F2, F12, F13 |
| **C2 — Configuration before value** | Setup must precede any working workflow, so users spend their motivation before they see a result. | F4, F5, F6, F9, F10, F14 |
| **C3 — Success measured as signup** | The dashboard tracks logins, so a stalled cohort looks healthy and no alert fires. | F3, plus the missing quiet-account alert |
| **C4 — Help arrives after failure** | Help lives outside the product and is generic by schedule, so the first two failure points go unsupported and import errors are invisible. | F7, F8, F15 |
| **C5 — Wrong accounts enter** | No job-to-be-done qualification, so some accounts bought a use case the product cannot serve; no onboarding can fix that. | F11 |

Evidence: F1, F2, F3, F12 are **observed** in the current setup; F10 and F13 are **inferred**; F14 is **speculation** pending mobile analytics. Five clusters, five mechanisms — no "onboarding issues" bucket.

## Step 5 — Extract principles

| # | Principle | Failure route | Signal | Owner / decision |
|---|---|---|---|---|
| **P1** | The activation metric is the launch gate and appears in sales and support goals. | C1 | First-value rate reviewed weekly; no launch without it | VP Revenue can hold the gate |
| **P2** | Deliver first value before required configuration; default everything that can be defaulted. | C2 | Time-to-first-value rises while setup completion falls | Onboarding PM can reorder steps without a release |
| **P3** | The primary metric is 7-day first value, and a quiet account triggers an alert. | C3 | Dashboard shows first value; quiet accounts surface within 48h | Analytics owns the metric definition |
| **P4** | Help is embedded at the first two failure points; every activation ticket is tagged by step and import errors are loud. | C4 | Ticket tags by step; import failure rate visible | Support lead owns the tagging |
| **P5** | Qualify accounts by job-to-be-done before onboarding; route the rest to self-serve or disqualify. | C5 | Share of qualified accounts and their activation rate | Sales engineering owns qualification |

Trade-offs: P2 delays some configuration and needs graceful deferral; P5 may reduce trial volume; P3 changes compensation, which is a negotiation, not a dashboard edit.

## Step 6 — Probe

Two principles are cheap and load-bearing:

- **P2:** reorder one onboarding path for a new cohort — default sample data, defer the import behind a working workflow. Signal: time-to-first-value and 7-day rate versus the control cohort. Kill criterion: no improvement after two weeks or a rise in setup errors.
- **P4:** tag tickets by activation step and add in-product help at the two largest drop-off points. Signal: share of tickets tagged, drop-off at those steps.

Leave P1 and P3 for a decision meeting with revenue; they change incentives, not copy. Mark C5's size as unknown until qualification data exists.

## What the inversion bought

The positive plan ("better emails, new tour, help centre") addressed C4 only, and only generically. Inversion surfaced C1, C2, and C5 — the clusters that make the others irrelevant — and produced principles with owners, signals, and trade-offs. That is the normal result: the direct plan optimizes the visible symptom; the inverted list finds the standing conditions.
