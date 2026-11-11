# Reversal — Turning Bad Ideas into Improvement Directions

A bad idea is a compressed statement about a condition that sustains the problem. Reversal reads that condition out and asks what would have to be true for the opposite to hold. The output is a **direction**, not a finished solution: actor, action, and the condition the action changes.

## Work at cluster level first

Reverse **clusters**, not each of the twenty-five bad ideas. Five to six clusters yield five to six directions with distinct mechanisms; twenty-five individual reversals yield twenty-five variations of "do the opposite" and exhaust the group. Drop back to individual ideas only when one is unusually specific and does not fit its cluster.

## The operators

Apply one operator per cluster, then try a second if the first yields a platitude.

| Operator | Question | Bad idea → direction |
|---|---|---|
| **Negate the mechanism** | If X makes it worse, what standing condition removes X? | "Hide errors in a log" → "surface each error at the point of action" |
| **Invert the actor** | Who should act here instead of the current actor? | "User must configure everything" → "system supplies defaults; user only confirms" |
| **Remove the precondition** | What must exist for the bad idea to work, and can we delete it? | "Setup needs an admin" → "no admin role in the first-run path" |
| **Re-scope** | Apply the harm to a smaller or larger slice — what changes? | "Reset all progress on interruption" → "resume from the last completed step" |
| **Reverse the sequence** | What if the last step came first? | "Teach features, then let them try" → "let them try, teach at the point of need" |
| **Turn the harm into a signal** | If the bad idea hides something, what would exposing it enable? | "Support replies with a link after 48h" → "stall detection triggers one-tap help in-session" |
| **Amplify to absurdity, then subtract** | What is the smallest version of the opposite that still works? | "Send seven emails" → "send zero; put the one needed message in-product" |

The first four do most of the work. Sequence reversal and harm-as-signal are the ones groups usually miss; try them explicitly on every cluster.

## From direction to concept

A reversal is still abstract. Promote it to a concept only when it has all four:

1. **An actor** — a role, a system, or a policy that would do it.
2. **An action with a mechanism** — "default the language from the device locale," not "personalize."
3. **The condition it changes** — which of the bad idea's mechanisms it removes or offsets.
4. **A cost and a plausible failure mode** — what it takes, and how it could backfire.

Example: "surface import failures at upload" becomes "validate the file client-side and show the exact failing row before the user leaves the page; cost: one extra validation pass; risk: false rejections on unusual but valid files."

## Quality tests

| Test | Fails when | Fix |
|---|---|---|
| Actionable | "Communicate better," "improve UX" | Name actor and action |
| Mechanism preserved | The direction does not touch why the bad idea worked | Re-read the bad idea's causal story |
| Not a negation | Only "don't do X" | Rewrite as what is done instead |
| Not a double reversal | The direction restores the original problem | Check against the problem statement |
| Non-trivial | It is what any competent team would already do | Keep it, but mark it as a baseline idea, not a harvest |
| Feasible enough to probe | Impossible within constraints | Keep as a "if constraints changed" note, not a concept |

## Keep the implausible ones visible

Some reversals are correct but unaffordable, unlawful, or outside the team's authority. Do not discard them silently: list them as **deferred directions** with the constraint that blocks them. They are often the most useful input to a later constraint-challenging session, and they show the group that the exercise was not rigged toward the safe answer.

## Common mistakes

- **Reversing the wording instead of the mechanism.** "Don't make onboarding long" is not a direction.
- **Stopping at the first polite reversal.** The first one is usually the baseline idea; try a second operator.
- **Treating a reversal as validated.** It is a hypothesis; enrichment and a probe come next.
- **Balancing every bad idea.** You do not owe the list symmetry; harvest the directions with distinct mechanisms.
- **Letting the author of a bad idea defend it.** The cluster belongs to the group, not to whoever wrote the card.
