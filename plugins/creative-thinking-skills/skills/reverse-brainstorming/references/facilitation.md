# Facilitation — Workshop, Solo, and Human–AI

The method has one non-negotiable structural rule: **worsening and reversing are separate passes.** The moment someone says "we could just do the opposite," the energy drops and the list collapses into the obvious fixes. Protect the separation with timeboxes and a visible agenda.

## Standard agenda (50 minutes, 4–8 people)

| Phase | Time | Activity | Output |
|---|---|---|---|
| Intake | 5 min | Read the problem verbatim; confirm who has it and what solved looks like | One agreed problem statement |
| Worsen | 10 min | Silent writing, then round-robin; no discussion | 15–25 bad ideas |
| Cluster | 5 min | Affinity grouping by mechanism; name each cluster | 3–6 clusters with causal stories |
| Reverse | 15 min | One operator per cluster; write directions on a second board | 5–8 directions |
| Enrich | 10 min | Elaborate 3–5 directions into concepts with cost and failure mode | 3–5 concepts |
| Harvest | 5 min | Vote, choose 2–3, define probe and signal | Decisions and owners |

If the group is large, split into tables for worsening, then merge lists before clustering. If time is short, cut enrichment, not the separation.

## Preparation

- **Room or board:** two separate surfaces — one for bad ideas, one for directions. Never reverse on the same board; the visual separation is the method.
- **Prompt visible:** "How could we guarantee this problem gets worse?" stays on screen for the whole worsening pass.
- **Materials:** one idea per card or one line per row; a timer the group can see.
- **People:** include someone close to the problem and at least one outsider. The outsider writes the "obvious" bad ideas the insiders have stopped noticing.
- **Framing sentence:** "For the next ten minutes we are trying to make this worse. Nothing said here is a proposal, and nobody is accountable for it." This permission is what makes the technique work.

## Worsen pass (10 min)

- Two minutes of silence to start, then round-robin one idea per person.
- No reactions, no "yes but," no fixing. The facilitator writes and does not evaluate.
- Push for specificity when an idea is a label: "What exactly makes it worse? Who does it?"
- Run the domain sweep only if the list stalls before fifteen ideas.
- End on time even if the list feels incomplete; the second pass happens during clustering if needed.

## Reverse pass (15 min)

- Read each cluster's causal story aloud before reversing it.
- Assign one operator per cluster (negate, invert actor, remove precondition, re-scope, reverse sequence, harm-as-signal) so the directions do not converge.
- Write the direction as **actor + action + condition**; the facilitator rejects negations and platitudes.
- Do not evaluate feasibility yet. If someone raises cost, park it on a "constraints" list and continue.
- Aim for 5–8 directions, not one per bad idea.

## Enrich pass (10 min)

- Pick the 3–5 directions with distinct mechanisms. Distinctness means a different actor or a different causal lever, not different wording.
- For each: one-sentence concept, who acts, rough cost, most likely failure mode, and what would have to be true.
- Mark directions that are baseline ideas ("we should already do this") separately from novel ones.
- Drop or defer anything that cannot be described without jargon.

## Harvest (5 min)

- Dot-vote or a 2×2 (novelty × feasibility); keep a portfolio, not only the safest concept.
- Choose 2–3 concepts. For each: first probe, leading signal, kill criterion, owner.
- Record the deferred directions and the constraints that blocked them.

## Solo mode (25–35 min)

1. Write the problem verbatim and the four worsening directions (5 min).
2. Worsen in two timed passes of five minutes each — first from memory, then with the domain sweep — without editing (10 min).
3. Cluster on paper; name each cluster with a causal sentence (5 min).
4. Reverse each cluster with a different operator; write directions as actor + action + condition (10 min).
5. Enrich the best three and choose one probe (5 min).

Solo work benefits from a deliberate delay: put the bad-idea list aside for an hour before reversing, so the reversal pass is not just the generation pass continued.

## Human–AI mode (15–25 min)

- **Human sets the frame.** Provide the problem verbatim, who has it, constraints, and what has been tried. Ask for worsening ideas only — not fixes.
- **AI generates a broad worsening list.** Require mechanisms and actors; reject labels and ask for a second pass across domains the first pass missed.
- **Human clusters.** The clustering decision is where judgment matters; do not delegate it silently.
- **AI drafts candidate reversals per cluster.** Expect generic first drafts; ask for a second operator per cluster and for the cost and failure mode of each.
- **Human selects and probes.** Keep 2–3 concepts, label assumptions, and decide the next experiment. The AI's list is input, not evidence.

Prompts that help: "Give twenty ways to make this problem worse, each with an actor and a mechanism; do not include fixes." Then: "For each cluster, apply a different reversal operator and give one direction with cost and failure mode."

## Anti-patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| Reversing during generation | List collapses to obvious fixes | Two boards, strict timeboxes |
| Evaluating bad ideas | People self-censor | Explicit immunity for the worsen pass |
| One theme in twenty costumes | No new mechanisms | Domain sweep, coverage check |
| Reversing every idea | Shallow one-to-one fixes | Cluster first, reverse clusters |
| Skipping enrichment | Clever directions, no action | Concepts need actor, cost, failure mode |
| Only safe reversals survive | Exercise validates the status quo | Keep deferred directions visible |
