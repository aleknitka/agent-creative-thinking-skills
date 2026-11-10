# Worked Example — Onboarding Takes Too Long

A compact end-to-end trace of the 6-step lateral-thinking process. Timings are illustrative for a 25-minute pass.

## 1. Intake (1 min)

- **Stated problem:** Onboarding takes too long; users drop off before first success.
- **Real goal:** Users reach first meaningful outcome quickly and feel competent.
- **Hard constraints:** Cannot require sales-assisted setup; must work for self-serve.
- **Appetite:** medium — stranger ideas welcome if they lead to a small probe.

## 2. Dominant idea (3 min)

> **Dominant idea:** We are optimizing *time-to-completion of a guided tutorial* by *adding explanations and progress bars* because we assume *users must be taught the product before they can succeed*.

- Taken for granted: onboarding = tutorial; progress is linear; more guidance is better.
- Boundary drawn at: inside the product, during first session.
- Real goal behind the stated problem: first success, not tutorial completion.

## 3. Provocations (5 min)

Using 4 operators, deliberately wrong:

1. `Po, onboarding has no tutorial.` *(escape)*
2. `Po, the product onboards the user downstream of itself — success happens before first open.` *(reversal + distortion)*
3. `Po, onboarding happens 1000× faster — in under 3 seconds.` *(exaggeration)*
4. `Po, onboarding is like a mushroom — it spreads underground and appears where conditions are right.` *(arising — random word "mushroom" from the offline picker `scripts/random_entry.py`)*
5. `Po, new users are already experts.` *(wishful thinking)*

No judging yet.

## 4. Movement (10 min)

Two most intriguing Pos moved:

**Po 1: `Po, onboarding has no tutorial`**

- Extract principle: competence via doing, not instruction.
- Difference: zero UI vs. guided tour → keep: zero UI.
- Moment-to-moment: user opens on real work → first action is the real task → help is contextual, not sequential → tour is unnecessary.
- **Direction A:** Embed learning inside the first real task (checklist on real data).

**Po 2: `Po, success happens before first open`**

- Extract principle: configuration precedes entry.
- Special circumstances: works when intent is known (invite, import, template).
- Positive aspect: instant relevance — no "empty state."
- **Direction B:** Pre-configured entry — invitation/import carries intent so the product opens on the user's work.

**Po 4: `Po, onboarding is like a mushroom`**

- Extract principle: grow from existing networks, not a central path.
- Positive aspect: appears where conditions (social context) are right.
- **Direction C:** Peer-propagated onboarding — a teammate's artifact invites and orients.

## 5. Harvest — 3 distinct frames + probes (5 min)

Each is a different mechanism/assumption challenged, tagged for uncertainty.

| # | Frame (new "box") | Mechanism | Assumption challenged | Fact / assumption / speculation | Small probe |
|---|---|---|---|---|---|
| 1 | **Learn by doing** | Checklist overlaid on real task, not a separate tour | "Users must be taught before doing" | Fact: drop-off correlates with tutorial length; assumption: checklist is sufficient; speculation: real-task framing improves retention | One real-data checklist that completes onboarding as the user does the task |
| 2 | **Pre-configured entry** | Import/template/invite pre-fills intent; open on real work | "Onboarding starts inside the product, on first open" | Fact: 40% of signups arrive via invite; assumption: intent can be captured at invite time | One invite template that skips the tour entirely |
| 3 | **Peer-propagated** | A teammate's shared artifact is the entry point | "Onboarding is solo and in-product" | Fact: teams that invite early retain better (internal data); speculation: artifact as orientation reduces time-to-value | One shareable artifact that doubles as orientation |

Distinctness check: each differs in **mechanism** (in-task help vs. pre-configuration vs. social propagation) and **assumption challenged**, not just phrasing.

## 6. Decide next (1 min)

- **Deepen** Frame 2 if intent capture is cheap — it has the shortest probe.
- **Combine** with `analogical-thinking` (how do games handle "play before tutorial"?) or `scamper` on the chosen frame.
- **Harden** with `premortem` before committing: "Frame 2 has already failed — why?"

## What good looks like

- Pos are visibly wrong and labelled `Po:`.
- Movement is shown, not skipped.
- Frames are not rewordings; each names a new box and a probe you could run this week.
- No claim is presented as evidence without a tag.

> Random-entry word bank used in this example: `scripts/random_entry.py`.
