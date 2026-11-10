---
name: question-storming
description: Generate questions before proposing answers — explore what is missing, who defines the problem, and whether the original question is useful. Use when the brief is vague, prematurely solution-focused, or you suspect you are solving the wrong problem — produce better questions and a revised problem statement.
---

# Question Storming

Most bad work starts with a good answer to the wrong question. A brief arrives already framed — "improve onboarding emails," "cut cloud spend," "make the dashboard faster" — and the team competes to answer it. Nobody asks who chose that frame, what evidence supports it, or what would happen if the question were different.

Question storming is the front end of problem solving: produce many questions before permitting any answers, cluster them, rank by what would actually change the work, and rewrite the problem statement. The output is not a solution. It is a better question and a short list of unknowns worth resolving.

## When to use

- The brief is vague, or the ask is a solution with no stated problem behind it.
- The team has jumped to options, estimates, or architecture before agreeing on the problem.
- Several smart people disagree, and the disagreement sounds like different definitions of the same words.
- You suspect the original question is a proxy for a goal nobody has named.
- A project is stalling and the current question has produced only incremental answers.

If unsure whether this is the right method, start with [thinking-router](../thinking-router/SKILL.md) — or see [references/when-not-to-use.md](references/when-not-to-use.md).

## When NOT to use (brief)

- The frame is sound and you need options → use `lateral-thinking`, `scamper`, or `morphological-analysis`.
- You need to test specific inherited beliefs → use `challenge-assumptions`.
- You need to move between levels of abstraction ("why does this matter?" / "how could this happen?") → use `abstraction-laddering`.
- The missing input is a fact about the world → research or measure; questions will not substitute.
- The decision is already locked and cannot change → document assumptions and monitor instead.
- The work is correctness-bound (proof, safety sequence, compliance audit) → use vertical / critical thinking.

## Process

1. **Intake — capture the brief before interpreting it.** Record the request verbatim, who asked, the decision it feeds, the deadline, and what has already been tried or ruled out. In one sentence each, state the stated problem, the goal behind it, and the hard constraints and their owners. Mark what is fact, assumption, and speculation. Ask only for gaps; reuse existing context. See [references/storming.md](references/storming.md).

2. **Generate 20+ questions across six categories.** Cover **clarifying** (what do the words mean?), **reframing** (why this problem, and what is the goal above it?), **stakeholder** (who is affected, who decides, who pays?), **constraint** (what is fixed, by whom, and what if it were not?), **causal** (what produces this, and what evidence supports that?), and **generative** (what if, how might we, what would make this easy?). Generate before judging; no answers, no explanations. Use the prompt bank in [scripts/storm.py](scripts/storm.py) and category detail in [references/question-types.md](references/question-types.md).

3. **Cluster.** Merge duplicates, group by what the answer would change rather than by topic, and give each cluster a one-line "what we do not know about X." Expect 3–6 clusters from 20–40 raw questions. Flag questions that are already answerable from existing evidence, and questions that are really assertions in disguise ("Why is the current process broken?"). See [references/storming.md](references/storming.md).

4. **Rank for usefulness, not novelty.** Score each cluster on **leverage** (how much the answer would change the decision), **tractability** (can it be answered, and cheaply), and **reframing power** (could the answer change the frame itself). Keep the top 5–8 questions; park the rest explicitly. Triage each survivor as answer-now, probe, research, or out-of-scope. See [references/prioritization.md](references/prioritization.md).

5. **Revise the problem statement.** Write **2–3 candidate statements** that each incorporate what the top questions exposed — a changed scope, a different beneficiary, a named constraint, or a reframed goal. Use "How might we …" only when it genuinely widens the space; otherwise use a plain question. Distinct means a different assumption or boundary is in play, not different wording. Mark what evidence would let you choose between them. See [references/examples.md](references/examples.md).

6. **Probe and hand off.** Turn each top question into the cheapest thing that could answer it: query existing data → one conversation with the source or a user → desk research → small prototype. For each probe state the observable, the decision rule, cost, and owner. Then choose one: proceed under a revised statement, run the probes, or hand off to `challenge-assumptions` (hidden beliefs), `abstraction-laddering` (wrong level), or `lateral-thinking` (need new directions). Confirm the next move with the user.

## Rules

- Questions first, answers later. Any answer offered during generation becomes another question: "What evidence would support that?"
- Quantity then quality. Aim for 20+ before clustering; early judgment kills the questions that reframe.
- One question per turn, captured verbatim. No multi-part questions with a preferred answer buried inside.
- Ask about the question, not only about the topic. Who chose this framing, and what would make it obsolete?
- Rank by decision impact, not by how interesting or easy the question is.
- A revised statement must trace to a named question and a named assumption. Rewording is not revision.
- Label fact / assumption / speculation. Questions reveal ignorance; they do not resolve it.
- Honest provenance: name the lineage and call adaptations adaptations. See [references/provenance.md](references/provenance.md).

## Going deeper

- Question categories, stems, and failure modes: [references/question-types.md](references/question-types.md)
- Facilitation — quantity, deferred answers, round-robin, solo/AI mode: [references/storming.md](references/storming.md)
- Prioritization — leverage, tractability, reframing power, triage: [references/prioritization.md](references/prioritization.md)
- Worked example — vague onboarding brief → 20 questions → 2 revised statements: [references/examples.md](references/examples.md)
- When not to use + triage against adjacent methods: [references/when-not-to-use.md](references/when-not-to-use.md)
- Provenance, lineage, and evidence limits: [references/provenance.md](references/provenance.md)
- Question-prompt generator (offline): [scripts/storm.py](scripts/storm.py)
