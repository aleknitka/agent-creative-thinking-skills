# Worked Example — One Concept → C-Tree → Probes

Initial concept (C0): "An onboarding that guarantees activation without any push message."

## Round 1 — partition C0

- C1 (restrictive): "Without welcome email, but with invite." Precedent in K — invite exists.
- C2 (expansive): "Without any push message at all — no email, no in-app nudge." No precedent in K.

Keep C2 — it forces a K expansion.

## Expand K for C2

Pocket needed: knowledge of how activation happens without push — peer pull, invite-time setup, or environmental trigger. No pocket exists; learning agenda: measure activations that already occur without push (invited via shared artifact).

## Use K to re-partition

From the pocket "shared artifacts carry intent," derive C2a: "Activation is pulled by the teammate's artifact at first open — no system push." This re-partition is K→C.

## Evaluate and shortlist

Keep C2 → C2a as the expansive branch (generative, new K pocket, testable). Discard C1 as refinement of the known. Add C3 (expansive, parallel): "Onboarding is entirely ambient — activation is inferred from artifact creation, not from a message." Branch C3 calls a distinct K pocket (artifact-creation signal).

## Probes

- C2a probe: one artifact-driven first open that suppresses push; signal: activation without push within 24h.
- C3 probe: instrument artifact creation as activation proxy; signal: correlation between artifact event and downstream usage.

Design square after two rounds: rows C0→C2→C2a, columns for pockets "shared artifact intent" and "ambient signal."
