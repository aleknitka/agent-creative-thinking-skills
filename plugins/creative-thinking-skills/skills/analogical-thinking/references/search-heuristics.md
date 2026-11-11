# Finding Far Domains

The goal is a domain that shares your **structural signature** while differing in surface and constraints. Industry adjacency usually gives you a benchmark; structural distance gives you a mechanism.

## Near vs far

| | Near domain | Far domain |
|---|---|---|
| Example for a support queue | Another SaaS company's support queue | Emergency department triage, air-traffic sequencing, restaurant kitchen pass |
| What you get | Best practice, copied features | Causal mechanism, different tradeoffs |
| Risk | You import the same assumptions and constraints | The mechanism depends on conditions you lack |
| Best use | Validate norms, find table stakes | Discover a new operating principle |

Use near domains to calibrate what is normal. Use far domains to change the mechanism. A good session uses both, but the transferable idea usually comes from the far one.

## Distance is structural, not topical

"Far" does not mean unrelated. It means: same relations, different nouns, different constraints. A hospital and a warship can be near if both manage scarce attention under uncertainty. Two SaaS companies can be far if their incentive structures differ completely.

Sweet spot: the source is understandable in an hour, its mechanism is documented, and its constraints differ enough that copying is impossible.

## Candidate domains by structural signature

### Biology and ecology
- Competition, symbiosis, parasitism, succession, niches, immune response, homeostasis, foraging, swarms.
- Prompts: What occupies this niche? What regulates population? What does the immune system do with ambiguous threats? Where is redundancy intentional?

### Logistics and transportation
- Hub-and-spoke, cross-docking, containerization, buffer stock, last-mile, customs, wayfinding, traffic calming, air-traffic sequencing.
- Prompts: Where are buffers placed? What is standardized versus customized? How are exceptions routed? What does a checkpoint verify?

### Emergency response and medicine
- Triage, incident command, reserve capacity, handoff protocols, checklists, surge staffing, isolation, second opinions.
- Prompts: How is urgency estimated under uncertainty? Who can override? What is the cost of a false positive versus a false negative?

### Games and sport
- Matchmaking, tutorials, progression, fog of war, respawn, anti-cheat, drafting, pacing, rubber-banding, officiating.
- Prompts: How is difficulty calibrated? How are newcomers protected without boring experts? What makes failure recoverable?

### Operations and manufacturing
- Kanban, poka-yoke, andon cord, single-minute exchange, statistical process control, gemba, five whys.
- Prompts: How is work made visible? What stops the line? Where is variability absorbed? What is the smallest batch?

### Markets and institutions
- Auctions, insurance, escrow, reputation, standards bodies, clearing, warranties, bonding, licensing.
- Prompts: How is risk priced? Who bears the downside? What aligns incentives when parties cannot verify each other?

### Craft, design, and the arts
- Jigs, dry fitting, rehearsal, improv rules, editorial passes, staging, sound checks.
- Prompts: What is rehearsed versus performed? What cheap artifact stands in for the expensive one? How are revisions sequenced?

### Military and security
- Defense in depth, reconnaissance, rules of engagement, reserves, mission command, fail-safe versus fail-open.
- Prompts: What is the reserve for? Who decides under uncertainty? What is deliberately decentralized?

### Software and systems
- Caching, rate limiting, backpressure, circuit breakers, idempotency, schema migration, canaries, incident command.
- Prompts: What absorbs load? What makes retries safe? How is a partial failure contained?

## Search tactics

1. **Inversion:** who has the opposite constraint? If you must be fast, who is rewarded for slowness and why?
2. **Scale shift:** who solves this with 100× more units, or 100× fewer?
3. **Time shift:** who solved an earlier version of this before the current technology existed? The mechanism is often clearer.
4. **Adversarial shift:** who solves this while someone actively games the system?
5. **Resource shift:** who solves this with no budget, no trust, or no central authority?
6. **Failure shift:** who expects this to fail routinely and has made failure cheap?

## Selection checklist

For each candidate, record:

- Shared relations (at least two).
- Key difference in constraints.
- Whether the mechanism is documented well enough to map honestly.
- Whether you can name a person or text that explains it (or mark it as inference).
- Whether the transfer would be observable in a small probe.

Keep 5–8 candidates, then shortlist 2–3. One or two get the deep mapping treatment.

## Avoid

- Searching only your industry and calling it analogical thinking.
- Choosing domains because they are fun to talk about, then forcing the mapping.
- Using a source you cannot describe accurately; a vague source produces a vague principle.
- Treating a famous metaphor ("the market is an ecosystem") as a finding. It is a hypothesis to test.
