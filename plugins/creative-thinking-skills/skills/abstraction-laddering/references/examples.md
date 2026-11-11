# Worked Example — From "Fix Signup" to "Belonging"

This example runs one ladder in both directions, shows the join, and picks a leverage point. The numbers are illustrative, not findings.

## Starting rung (verbatim)

> "Users drop off during signup. Fix the signup form."

This is an action disguised as a problem. It names a solution (fix the form) and a metric (drop-off), but not a purpose or a mechanism.

## Ladder up (why)

| # | Rung | Level | Note |
| --- | --- | --- | --- |
| U0 | Fix the signup form | Action | Verbatim starting statement |
| U1 | New users complete account creation | Function | What the form is supposed to achieve |
| U2 | New users reach a first useful result quickly | Purpose | Why completion matters — value, not the gate |
| U3 | New users feel this product is for someone like them | Purpose | First hint that the issue may be belonging, not friction |
| U4 | People can participate in the community without feeling like outsiders | Vision | Stakeholder and future state named; stop here |

Stop reason: U4 names the ultimate beneficiary and future state; another why ("so people are happy") adds nothing actionable. The upward chain reveals that "fix the form" was never the goal: completion is a proxy for *reaching value and feeling included*.

Evidence labels: U1 is measured (funnel data). U2 is assumption (no cohort analysis yet). U3 is speculation from interview fragments. U4 is vision.

## Ladder down (how)

From U2 ("first useful result quickly"):

| # | Rung | Level | Note |
| --- | --- | --- | --- |
| D1 | Get the user to a meaningful artifact in the first session | Function | Capability, not feature |
| D2 | Ask for only the decisions needed to produce that artifact | Mechanism | Causal lever: minimize up-front decisions |
| D3 | Defer workspace naming and invite-others until after first value | Mechanism | Specific lever |
| D4 | Reorder first-run flow: one decision, generate artifact, then configure | Action | Observable and testable |

From U3 ("feels for someone like them"):

| # | Rung | Level | Note |
| --- | --- | --- | --- |
| E1 | First-run content reflects the user's own context | Function | Capability |
| E2 | Infer context from the entry point instead of asking | Mechanism | Causal lever |
| E3 | Use the landing page's stated use case to seed the first artifact | Action | Observable |

## The join

The upward chain (U2/U3) and the downward chains (D4/E3) meet at **function level**: D1 and E1 are both ways to serve U2–U3. The original statement ("fix the form") sits below the join and is not sufficient for either purpose.

Gap found: there is no rung explaining *why* completion should precede value. The funnel assumes it; the purpose rungs suggest the opposite ordering may serve the user better. That gap is the actual finding.

Contradiction found: "ask for only necessary decisions" (D2) conflicts with the current requirement to name a workspace before generating anything. One of the two must give.

## Leverage choice

Candidates: D2 (defer decisions), E2 (infer context), U2 reframe (success = first artifact, not account).

Scores (1–3):

| Rung | Impact | Control | Evidence |
| --- | --- | --- | --- |
| D2 | 3 | 3 | 2 |
| E2 | 2 | 2 | 1 |
| U2 reframe | 3 | 1 | 2 |

- **D2** is the leverage point: high impact, fully controllable, plausible evidence. It is a short intervention in service of a tall hypothesis (U2).
- **E2** is promising but speculative; run a desk check on entry-point data first.
- **U2** is high impact but low control; it belongs in the advocacy column — socialize the metric change with the owner while D2 runs.

Chosen probe: reorder the first-run flow so an artifact is generated before workspace configuration, for one entry segment.

- Observable: share of new users who produce an artifact within the first session.
- Decision rule: if the artifact rate rises ≥10 points and the completion rate does not fall, keep and extend. If artifact rises but completion falls sharply, investigate the handoff. If neither moves, D2 is not the binding mechanism; return to D1.
- Assumption: users value an artifact more than a configured workspace. Cheap check: exit interviews and existing support tickets.
- Not doing: rewriting the form visuals, adding progress bars.

## What the ladder bought

- The original "fix the form" was replaced by two connected purposes and two mechanism chains.
- The intervention is now tied to a hypothesis and a decision rule, not to a symptom.
- Two structural findings surfaced (missing ordering rationale, a direct contradiction) that a form redesign would have hidden.
- One candidate was correctly routed to advocacy rather than action.

The ladder does not prove U2 or U3. It makes them explicit enough to test, which is the point.
