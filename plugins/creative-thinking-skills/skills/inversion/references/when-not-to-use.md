# When NOT to Use Inversion — and What to Use Instead

Inversion is a **search-direction change**: generate guaranteed failure, then convert it into principles. It fits goals, strategies, designs, and beliefs that are stated in positive terms. It does not fit every kind of reasoning problem.

## Quick triage

| Your situation | Better fit | Why |
|---|---|---|
| A concrete proposal is near commitment and you need it hardened | `premortem` | Premortem declares one specific failure as fact, generates reasons independently, and prioritizes by likelihood × impact; it is a pre-commitment ritual, not a principle-derivation method |
| You need many alternatives or novel options | `divergent-thinking`, `what-if`, `scamper` | Inversion produces failure routes; it does not widen the option space |
| You need one assumption tested cheaply | Experiment, pilot, base rates | A failure route is a hypothesis; evidence beats more speculation |
| You need quantified, auditable hazard analysis | FMEA, HAZOP, fault-tree analysis | Standards-based, severity/probability-rated; inversion is qualitative and cannot certify safety |
| The premise itself is suspect | `challenge-assumptions` | Inversion accepts the goal and maps failure; challenge-assumptions questions whether the goal is the right one |
| The problem is vague and needs reframing | `thinking-router`, problem restatement | Inversion needs a predicate; "improve things" has nothing to negate |
| A decision is locked and cannot change | Risk tracking, postmortem | Principles with no authority to act are decoration |
| The task is to choose among 3–5 options | Decision matrix, `options-portfolio` | Inversion stress-tests one goal or design; comparison needs shared criteria |

## Inversion vs premortem

Both use failure imagination; they differ in premise and output.

| | Premortem | Inversion |
|---|---|---|
| **Starting point** | A concrete plan with a decision date | A goal, strategy, design, or belief |
| **Premise** | "It is ⟨date⟩. It failed." | "How could we guarantee failure?" |
| **Scope** | One proposal, one horizon | A goal and its unwanted outcome |
| **Generation** | Reasons the proposal failed, independently written | Routes to guaranteed failure across ten domains |
| **Output** | Prioritized risks, warning signals, hardening changes | Clustered mechanisms and positive design principles |
| **When** | Before commitment, when change is still cheap | Early, when designing the approach, or when positive planning stalls |
| **Risk** | Defence session if facilitation slips | Platitudes and contrarianism if routes are not mechanisms |

Use premortem when there is a proposal to harden. Use inversion when there is no proposal yet, or when you want principles that apply beyond one launch. Running a premortem and then inverting its output is a reasonable sequence: premortem hardens the plan; inversion harvests transferable principles.

## Inversion vs reverse brainstorming

Reverse brainstorming is a **group activity**: ask "how could we cause this problem?" to break a creative block, then reverse the answers into ideas. Inversion is the broader reasoning discipline that contains that activity and goes further:

- It includes **goal inversion** and **outcome inversion**, not only "cause the problem."
- Its output is **principles with owners and signals**, not a list of ideas.
- It requires clustering by mechanism and a probe, so it does not stop at clever reversal.

If you only need energy and idea volume in a workshop, reverse brainstorming is lighter. If you need design conditions you will act on, use inversion.

## Inversion vs what-if

`what-if` mutates a load-bearing assumption to explore alternative worlds and transfers insight back. Inversion deliberately seeks the **worst reliable route** inside the current world. What-if asks "what if the constraint were different?"; inversion asks "how would we guarantee failure under this constraint?" Use what-if for possibility; inversion for prevention and design principles.

## Inversion vs Black hat (six-thinking-hats)

The Black hat applies caution inside a multi-perspective exploration. Inversion is a dedicated failure search with an explicit inversion frame and a conversion step. The Black hat produces concerns; inversion produces failure mechanisms and principles. For a routine idea review, a Black hat pass is enough.

## Inversion vs challenge-assumptions

`challenge-assumptions` inventories and tests the beliefs a plan rests on. Inversion assumes the goal is fixed and asks what would defeat it. The two pair well: challenge-assumptions finds the belief; inverting it tests what would have to be true for the opposite. If the doubt is about the goal itself, start there.

## Handoff triggers

| Next | Trigger |
|---|---|
| `premortem` | A concrete proposal exists and commitment is near |
| `challenge-assumptions` | The inversion keeps circling one foundational belief |
| `divergent-thinking` / `scamper` | Failure routes reveal a need for new options |
| `options-portfolio` | Several preventive principles compete for limited capacity |
| Experiment / pilot | A principle's signal can be observed cheaply |
| Formal FMEA/HAZOP | A failure route is a safety or regulatory hazard |
| `thinking-router` | Signals are mixed or you are unsure which method fits |

## The contrarianism trap

Inversion is not "argue the opposite." Symptoms of misuse:

- The output is a debate position ("actually, onboarding is fine") rather than a failure map.
- Routes attack the people, not the design.
- Every route is already known and the list adds nothing — you needed evidence, not more imagination.
- Principles are written as negations ("don't lose users") and nobody can act on them.

**Rule:** the goal stays fixed, the routes must be mechanisms, and the output must change a decision. If none of those hold, you are performing scepticism, not inverting.
