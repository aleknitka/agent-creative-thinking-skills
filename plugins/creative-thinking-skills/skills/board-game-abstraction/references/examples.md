# Worked Example — Onboarding → "Intent Race"

## Intake

Problem: invites carry no intent, activation uninstrumented, 32% drop before first value. Constraint: invite email is org-mandated. Hurt: new team waits on setup, loses week 1.

## Cast and Board

- **Players:** New Hire, Buddy, Admin, System (dealer)
- **Resources:** Intent (0–3), Attention (2/turn), Setup Slots (3 total)
- **Board:** Track race 0→6 (activation); Event deck: "manager ping", "calendar clash", "tool down"
- **Loop:** More invites without intent → less attention → less intent → more invites (R with delay || at attention)

## Mechanic

**Push-your-luck + Track race.** Each turn: draw Intent card (0–1) or bank progress. Push too often without intent → stall (lose 1 progress). Intent adds +1 to next draw.

## 1-Page Rules

Setup: track at 0, Intent 0, Attention 2. System shuffles Intent deck (4×0, 4×1) + Event draws.
Turn: spend 1 Attention to (a) Invite (draw Intent), (b) Act (advance if Intent≥1), or (c) Rest (recover Attention, +1 Intent if buddy helps). Bust: 3 consecutive invites without banking → stall back 1. Win: track 6 in ≤12 turns. Loss: stalls ×3 or Attention 0 with track <3.

What each rule abstracts: Invite=real invite, Attention=team bandwidth, stall=retry cost.

## Three Plays

1. **Honest:** banks early → wins slowly, Attention preserved.
2. **Greedy:** draws 4 without banking → busts twice, loses.
3. **Co-op (buddy helps):** Rest actions convert to Intent → wins fastest.

## Transfer (fact/assumption/speculation)

- Fact: stalling after repeated invites without intent is real — retry cost exists.
- Assumption: 1 Attention/turn models real bandwidth — test with time-boxed data.
- Probe: "Pre-intent gate adds 1 Intent before first invite — cuts stalls 50% in 2-week cohort?" (owner + signal: track≥3 rate).
- Handoff: strongest probe to `premortem` if fear of intent-gating friction; else `causal-loop-diagram` for leverage of Intent loop.
