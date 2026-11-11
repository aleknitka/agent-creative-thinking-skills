# Worked Example — Guaranteeing That Users Never Onboard

A consumer language-learning app has a setup problem: people install after an ad, open the app once, and never finish setup, so they never take a lesson. The team has tried "better onboarding copy" twice. Direct brainstorming keeps returning the same three fixes: shorten the form, add a progress bar, improve the tutorial. Reverse brainstorming starts from the other side.

## Step 1 — Intake

- **Problem (verbatim):** "People who install the app never finish setup, so they never take a first lesson."
- **Who:** new users aged 18–35, mostly arriving from a paid social ad on mobile.
- **Solved looks like:** ≥40% of installs complete setup and one lesson in the first session.
- **Constraints:** two mobile engineers, no human onboarding, current analytics stack.
- **Tried:** shorter copy, a progress bar, a five-screen feature tour.
- **Labels:** the 12% completion rate is **fact**; "the form is too long" is **assumption**; "ads bring low-intent users" is **speculation**.

## Step 2 — Worsen (17 bad ideas, unfiltered)

| ID | Bad idea |
|---|---|
| W1 | Require an account, a level test, and notification permission before showing any lesson. |
| W2 | Make the level test 20 minutes with no skip button. |
| W3 | Require email confirmation before any content unlocks. |
| W4 | Show a paywall immediately after the first tap. |
| W5 | Ask twelve goal questions and ignore every answer. |
| W6 | Reset progress when the app is backgrounded. |
| W7 | Autoplay an unskippable three-minute brand video at launch. |
| W8 | Show a tutorial carousel about features instead of a lesson. |
| W9 | Make the first lesson use vocabulary from lesson nine. |
| W10 | Send seven emails in three days, all "complete your profile." |
| W11 | Put the only continue button below the fold, in grey-on-grey. |
| W12 | Require a stable connection for setup and fail silently offline. |
| W13 | Ask users to choose a "learning path" from jargon they have never seen. |
| W14 | Let one broken Android keyboard block the name field. |
| W15 | Force full completion: no back button, no save-and-exit. |
| W16 | Show a "you haven't finished setup" banner three days later. |
| W17 | Have support reply with a help-centre link 48 hours later. |

## Step 3 — Cluster by mechanism

| Cluster | Causal story | Bad ideas |
|---|---|---|
| **C1 — Value withheld behind a ritual** | Setup asks for commitment and configuration before demonstrating anything worth committing to, so users leave at the first cost. | W1, W2, W3, W7, W8, W13 |
| **C2 — No recovery from interruption** | Any interruption destroys progress or fails silently, so a partial setup is wasted and never resumed. | W6, W12, W14, W15 |
| **C3 — Inputs that are never used** | Setup collects goals, level, and path but does not adapt content, so the questions feel like a form, not a benefit. | W5, W9, W13 |
| **C4 — Nagging instead of helping** | Reminders escalate on a schedule while nothing in the product removes the blocker. | W10, W16, W17 |
| **C5 — Paywall before proof** | The price appears before the user has experienced any value. | W4 |

W6 and W12 are the kind of route a positive plan never names: neither is a feature, and both are standing conditions. W4 is deliberately left as its own cluster so its reversal is not swallowed by C1.

## Step 4 — Reverse (one operator per cluster)

| Cluster | Operator | Improvement direction |
|---|---|---|
| C1 | Reverse the sequence | Let the user take a 90-second lesson before creating an account; defer signup to the save point. |
| C2 | Remove the precondition | Persist setup locally and resume at the exact step; remove the requirement for a stable connection during setup. |
| C3 | Invert the actor | Ask one goal question, then let the system choose the first lesson content from it; replace the level test with a three-item adaptive check after the first lesson. |
| C4 | Turn the harm into a signal | Detect an in-session stall and offer one-tap help at that step instead of scheduled emails. |
| C5 | Re-scope | Move the paywall after the first completed lesson, not after the first tap. |

W10 and W17 do not reverse into anything new — "send fewer emails" and "answer faster" are baseline ideas. They are recorded as baseline, not harvested.

## Step 5 — Enrich and de-risk

1. **Lesson zero.** A short first lesson runs before signup; the account is created only when the user saves progress. *Actor:* mobile client. *Cost:* rework of the first-run flow and anonymous progress storage. *Risk:* account-creation rate falls and marketing loses attribution; mitigate with a deferred signup prompt at save.
2. **Resume anywhere.** Setup state is stored locally, one decision per screen, save-and-exit on every step, offline-tolerant. *Actor:* mobile client + analytics. *Cost:* two engineering weeks. *Risk:* local state conflicts on reinstall; mitigate with a merge prompt.
3. **One question, used.** A single goal question changes the first lesson's content; the level test moves after the first lesson as a three-item adaptive check. *Actor:* content + client. *Cost:* content variants per goal. *Risk:* poor first-lesson fit for users who answer carelessly; mitigate by inferring from behavior after lesson one.

Deferred direction: "paywall after first lesson" (C5) is a pricing experiment, not an onboarding change; it needs a commercial decision.

## Step 6 — Harvest

| Concept | Probe | Leading signal | Kill criterion |
|---|---|---|---|
| Lesson zero | 20% cohort, no signup gate before lesson one | First-lesson completion in session | D7 retention falls, or account creation drops more than 10% |
| Resume anywhere | Ship local progress + save-and-exit | Resume rate after backgrounding; drop-off per step | No change in completion after two weeks |
| One question, used | A/B one goal question vs. current twelve questions | Setup completion and lesson-one accuracy | Accuracy falls without a completion gain |

Mark C3's content variants as **speculation** until lesson-one accuracy data exists, and keep the ads' intent level unmeasured rather than blaming it.

## What the reversal bought

The direct list (shorter form, progress bar, better tour) addressed C1's surface only. Worsening surfaced C2 and C4 — interruption and help — which the positive question had never made visible, and it turned a vague "personalize" wish into a testable change in C3. The three harvested concepts are not the opposite of the bad list; they are the mechanisms the bad list exposed.
