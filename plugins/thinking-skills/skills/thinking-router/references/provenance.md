# Provenance — Thinking Router

## Lineage

The router is original synthesis for this repository. The method catalog it scores is `megamouth/docs/creative-thinking-methodologies.md` (27) plus 10 extended methods from `research/extended-methods/synthesis.md` — 37 total grouped into Reframe / Generate / Explore / Decide, plus the Suggested first 8.

Each routed method carries its own lineage (de Bono — Lateral Thinking / Six Thinking Hats; Osborn — brainstorming; Eberle — SCAMPER; Altshuller — TRIZ; Rohrbach — 6-3-5 brainwriting; Knapp — Crazy Eights / Design Sprint; Wack/Schwartz — Scenario Planning; Robinson — Backcasting; Glenn — Futures Wheel; British Design Council — Double Diamond, and others). See the routed skill's `references/provenance.md` for method-specific attribution.

## Adaptations in this skill

- The four-need triage (*better question / more ideas / broader perspectives / stronger options*), the scoring model (trigger ×2 + output ×2 + appetite + time + installed), time budgets, guardrails (Suggested first 8 tie-break, variety rule), the intake template, and the routing-note / handoff / sequencing patterns are practical adaptations for orchestrating single-method skills. The `scripts/route.py` catalog and scorer implement this judgment deterministically and offline.
- The overlap / handoff guidance ("methods overlap intentionally") is editorial synthesis for this marketplace, not a claim about the source catalog.

## Evidence and limits

- The triage and scoring are heuristics for choosing the next method, not a validated decision model. The scorer is deterministic and transparent so the user can correct it; it does not estimate success probabilities.
- When routing to `stakeholder-perspectives` (or any hypothesis-generating method), label outputs as hypotheses to validate, not as user research. The same visible-uncertainty rule (facts / assumptions / speculation) applies to the router's recommendation itself.

## Permissions note

No third-party checklists, inventories, or long verbatim are bundled. The included `scripts/route.py` catalog reproduces the source doc's method names in a compact trigger/keyword table for offline scoring — no proprietary assessment items. If bundled word lists are ever added, use only MIT-compatible or public-domain sources.
