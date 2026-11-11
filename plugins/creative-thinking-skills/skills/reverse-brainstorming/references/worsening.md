# Generating Worsening Ideas

Reverse brainstorming works only if the bad ideas are concrete. "Make the app worse" produces jokes; "require a 20-minute level test before the first lesson" produces a mechanism you can reverse. The generation step is therefore deliberately negative, deliberately specific, and deliberately unfiltered.

## Frame the target

State the problem as an observed condition, not a wish: "new users download the app and never finish setup," not "improve onboarding." Then name what "worse" means for this problem. Most problems can worsen in four directions:

| Direction | Question | Example |
|---|---|---|
| **More frequent** | How do we make this happen to more people? | Make setup mandatory on every device |
| **More severe** | How do we make each occurrence cost more? | Lose all progress on interruption |
| **More persistent** | How do we keep the problem from ever being fixed? | Hide the failure signal from the team |
| **More contagious** | How does it spread to other people or steps? | Blame the user publicly, so they stop asking for help |

Pick one direction, or run the sweep once per direction if the list is thin.

## Core prompts

Write the blunt question on the board and leave it visible:

- **"How could we guarantee this problem gets worse?"** — the Munger-style inversion, applied to the problem rather than to a goal.
- **"How would we cause this problem from scratch, on purpose?"** — forces a recipe with steps and actors.
- **"What does this problem need in order to survive?"** — then give it exactly that.
- **"How would an indifferent team accidentally worsen it?"** — failures that need no villain.
- **"How would a competitor worsen it for us?"** — adversarial, but with realistic levers.
- **"What would we do if we were paid to make it worse?"** — exposes incentive gradients.
- **"How do we currently make it slightly worse without noticing?"** — turns the problem into observed evidence.

## Domain sweep

Generate at least one idea per domain, then keep going where the list is still thin.

| Domain | Trigger questions |
|---|---|
| **Incentive** | Who is rewarded for the behavior that sustains the problem? What is measured instead of the outcome? |
| **Information** | What is never observed, or reported too late? Who learns about the failure last? |
| **Friction** | Which step demands effort before any benefit? Where can we add a form, approval, or wait? |
| **Sequence** | What could we move before the moment of value? What could we make irreversible? |
| **Ownership** | Which decision has no owner, or two owners who disagree? |
| **Capability** | Which skill, system, or person is load-bearing? What breaks at 2× volume? |
| **Coordination** | Where can two teams' definitions of "done" diverge? Which handoff can drop the message? |
| **Trust** | Where can we ask for trust before evidence, or punish the user for our mistake? |
| **Environment** | Which external condition (network, platform, regulation, supplier) can we depend on unnecessarily? |
| **Psychology** | What does the user actually attend to? Where does friction exceed motivation? |
| **Time** | What decays if nobody maintains it? What is true only at launch? |

## Independence protocol

1. **Write before speaking.** Five to ten minutes of silent writing; one idea per card or line. The first senior comment otherwise anchors the whole list.
2. **Round-robin.** Each person reads one idea per turn until the list is exhausted. No reactions during the round.
3. **Separate passes.** First pass from memory and experience; second pass with the domain sweep. Two passes beat one polished pass.
4. **Target 15–25 ideas** for a meaningful problem. Eight to twelve is a warm-up, not a reverse brainstorm.
5. **Stop** when a new batch only restates mechanisms already on the board.

## Quality tests for a bad idea

A usable bad idea passes all four:

1. **Mechanism** — it says how the problem gets worse, not that it might. "Support is reactive, so the first failure is never fixed" passes; "bad support" fails.
2. **Actor** — a team, a user, a system, a metric, or a policy does it.
3. **Specificity** — you could draw the sequence of events on a whiteboard.
4. **Causal distance** — it is upstream of the problem's persistence, not a restatement of it. "Users don't finish" is the problem, not a cause.

## Keep the awkward ones

Do not filter for politeness, feasibility, legality in jest, or good taste during generation:

- **Absurd ideas** ("delete the product") isolate the single necessary condition.
- **Impolitic ideas** ("blame the user in the empty state") reveal design facts in disguise.
- **Ideas that blame leadership** are usually incentive facts; keep them and reverse them in the next step.
- **Ideas that cost nothing** ("add one more email") are often the most realistic routes.

Mark anything speculative as speculation. At this stage the goal is coverage, not credibility.

## Common mistakes

| Mistake | Symptom | Fix |
|---|---|---|
| Generic negativity | "Bad UX," "poor communication" | Force actor + mechanism |
| Disguised fixes | "We fail because we don't do X," where X is the plan | Restate the condition that keeps X absent |
| Single-cause collapse | Fifteen ideas, one theme | Run the domain sweep |
| Premature ranking | Half the list discarded mid-generation | Rank only after clustering |
| Worsening a different problem | Ideas attack a goal, not the stated condition | Re-read the problem statement before each pass |
| Skipping the boring route | Only dramatic failures appear | Ask what happens on an ordinary Tuesday at 2× scale |
