# Worked Example — Should We Ship the New Onboarding This Sprint?

Timed trace of the full evaluation sequence. Solo or pair with AI; 30-minute window.

## Setup (Blue, 2 min)

- Focus: Should we ship the new onboarding this sprint?
- Goal: Decide with risks visible and alternatives on the table.
- Sequence chosen: White → Red → Yellow → Black → Green → Blue (full evaluation).
- Appetite: medium. Time-boxes announced: White 5, Red 1, Yellow 4, Black 5, Green 8, Blue 5.

## White — Information (5 min)

- Fact: 32% drop-off during tutorial; median completion 4.2 min.
- Fact: 40% of signups arrive via team invite with context; invite is underused.
- Gap: Do users drop because the tutorial is long, or because first value is late?
- Gap: What is the cost of shipping half-finished vs. delaying one sprint?
- Next data to collect: first-value timing vs. tutorial completion (could fetch today).

## Red — Feelings and Intuition (1 min)

- "Uneasy — shipping feels rushed." (subjective)
- "Excited about pre-configured entry, skeptical about peer-propagated." (subjective)
- No justification, no debate. Captured as reactions only.

## Yellow — Benefits and Value (4 min)

- Benefit: New flow reduces steps from 7 to 3 — if tracking of first success holds, time-to-value drops by ~40% (assumption, needs data).
- Benefit: Pre-filled invite context helps the 40% invite segment immediately — condition: invite template ships too.
- Benefit: Smaller surface reduces future maintenance even if initial lift is similar.

## Black — Caution and Risks (5 min)

- Risk: New flow untested with solo signups (no invite) — may shift drop-off rather than reduce it.
- Risk: Analytics for first success is not yet instrumented — we would be flying blind for a sprint.
- Check needed: Define rollback criterion before shipping (instrumentation or backstop).
- Not a dismissal — each risk is paired with a concrete check.

## Green — Creativity and Alternatives (8 min)

- Idea 1: Ship pre-configured entry only for invite segment; keep old flow for solo (hybrid).
- Idea 2: Checklist overlaid on real task — onboarding completes while doing real work.
- Idea 3: Provocation — onboarding has no interface; use peer artifact as entry.
- Quantity before quality; no judging. One provocation pulled from lateral-thinking to unstick.

## Blue — Synthesis and Decision (5 min)

- White: known drop-off + invite context; gaps around first-value timing.
- Red: unease about rushing, excitement about pre-configured.
- Yellow: clear benefits conditional on invite template + instrumentation.
- Black: solo segment risk + missing analytics.
- Green: three alternatives; hybrid is most testable.
- Tension: Yellow vs. Black — value is high for invite segment, risky for solo.
- Decision: Ship hybrid (new flow for invite, old flow for solo) with instrumentation and a one-sprint rollback criterion. Owner: PM + eng. If hybrid fails, revisit with premortem-style Black deepening.
- Dissent captured: Reasonable Black view — delay one sprint to instrument first.

## What good looks like

- One hat at a time, time-boxes respected, Blue called explicitly.
- Yellow paired with conditions, Black paired with checks — not slogans.
- Green raw, Black specific, Red brief, White tagged fact vs. gap.
- Blue names tension and ends with one next step, not a vague continue.
