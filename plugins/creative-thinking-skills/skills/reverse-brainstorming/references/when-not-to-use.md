# When Not to Use — Comparisons and Handoffs

Reverse brainstorming is an ideation technique. It is at its best when the team is stuck on *what to try*, not on *what might go wrong*. If the need is analysis, prevention, or variation on an existing design, another method fits better.

## Quick test

Ask: **"Do we need new improvement directions, or do we need to evaluate/harden an existing plan?"**

- New directions, brainstorm stalled → reverse brainstorming.
- Harden a plan near commitment → `premortem`.
- Failure conditions and design principles → `inversion`.
- Alternatives to an existing baseline → `scamper`.
- Many alternatives without a negativity frame → `brainwriting` / `divergent-thinking`.
- The problem itself is unclear → research or `question-storming`.

## Reverse brainstorming vs inversion

They share the inversion move but differ in target and output.

| | Reverse brainstorming | Inversion |
|---|---|---|
| **Question** | "How could we make this problem worse?" | "How could we guarantee this goal fails?" / "How could we reliably produce the unwanted outcome?" |
| **Starting point** | An existing problem | A goal or a harm to avoid |
| **Purpose** | Idea generation | Failure analysis and design |
| **Output** | 2–3 improvement concepts with probes | Clustered failure mechanisms and preventive principles with owners and signals |
| **Rigor** | Light, timeboxed, workshop-friendly | Heavier: coverage check, principle quality tests |
| **Failure mode** | Clever reversals that never become concepts | Platitudes and contrarianism if routes are not mechanisms |

Use reverse brainstorming when the team needs energy and directions. Use inversion when you need conditions you will design against. Do not run both in one session unless you can name the distinct value; the routing logic explicitly warns against shortlisting both without justification.

## vs premortem

A premortem assumes a **specific proposal has failed** and asks why, independently, before commitment. Reverse brainstorming assumes **a problem persists** and asks how to worsen it. Premortem hardens a plan; reverse brainstorming generates candidate plans. Sequence: reverse brainstorm to find directions, enrich, then premortem the chosen concept.

## vs what-if

`what-if` mutates a load-bearing assumption — "what if the constraint were different?" — and explores alternate worlds. Reverse brainstorming stays inside the current world and looks for the worst reliable route within it. Use what-if for possibility and reframing; reverse brainstorming for improvements to a live problem.

## vs brainwriting

Brainwriting is a **format** (silent written idea generation, passing or pooling) with a positive or neutral prompt. Reverse brainstorming is a **prompt direction** (worsen the problem) that can and should be run in brainwriting format. If the group is blocked by hierarchy or airtime, start with brainwriting mechanics; if the ideas are merely generic, change the question to worsening.

## vs SCAMPER

SCAMPER applies seven prescribed operators to an **existing product or process** to produce variations. Reverse brainstorming starts from a **problem** and generates bad ideas first. SCAMPER's "Reverse" operator overlaps superficially, but it rearranges or inverts elements of a baseline; reverse brainstorming inverts a problem's sustaining mechanisms. Use SCAMPER when there is a baseline to stretch; use reverse brainstorming when the baseline is not the issue or does not exist.

## vs six-thinking-hats / Black hat

A Black hat pass raises concerns inside a multi-perspective review. Reverse brainstorming uses negativity as a **generative** device and then deliberately converts it. Black hat output is concerns; reverse brainstorming output is concepts. If the need is a quick critique, use the Black hat.

## Handoff triggers

| Next | Trigger |
|---|---|
| `premortem` | A concept is chosen and commitment is near |
| `inversion` | The team wants durable failure principles, not just ideas |
| `scamper` | The improvement is really a variation on an existing baseline |
| `brainwriting` | Airtime or hierarchy is the blocker, not the question |
| `experiment-design` | A probe needs a hypothesis, sample, and decision rule |
| `options-portfolio` | Several concepts need comparison under uncertainty |
| `question-storming` | The problem statement is still vague or contested |

## Do not use when

- The group cannot suspend judgment — a critique session will hijack the worsen pass.
- The problem is safety-critical and needs formal hazard analysis — use FMEA, HAZOP, or fault-tree analysis.
- There is no agreed problem statement — worsening an ambiguous problem produces arbitrary ideas.
- The decision is already made and the session is theatre — say so instead.
