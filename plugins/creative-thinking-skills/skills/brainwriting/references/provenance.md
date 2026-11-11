# Provenance — Attribution, Lineage, and Evidence Limits

## The 6-3-5 method

- **Bernd Rohrbach**, a German marketing consultant, published the 6-3-5 method in the trade magazine *Absatzwirtschaft* in **1968** (some secondary sources date it 1969). The name encodes **6 participants, 3 ideas each, 5 minutes per round**. Six rotations of the sheets produce six sheets of 18 entries — **108 idea slots in about 30 minutes**.
- Rohrbach's stated aim was to overcome the weaknesses of verbal brainstorming: production blocking (waiting for a turn), evaluation apprehension, and domination by fluent or senior speakers. Writing in parallel and passing sheets gives every participant equal airtime and makes every contribution legible and attributable.
- The 108 figure is a **slot count**, not a guarantee: blank cells, illegible entries, and duplicates reduce the usable total. Treat it as capacity, not output.

## The structured-group lineage: Warfield

- **John N. Warfield** developed **Interactive Management (IM)** from the 1970s onward, combining facilitation, computer support, and "consensus methodologies" to help heterogeneous stakeholder groups work on complex problems. Brainwriting was one of the consensus methodologies used in IM sessions, alongside the Nominal Group Technique and the Options Field Method.
- Warfield's design commitments overlap strongly with this skill: equal voice regardless of status, independent written contribution before group synthesis, explicit facilitation, and a record that can be revisited. IM's situation-room practice (the "Demosophia") is a historical example of separating generation from evaluation at scale.
- **Do not claim Warfield invented brainwriting.** Rohrbach's 6-3-5 predates IM's published use, and the written-ideas-before-discussion principle also appears independently in the nominal group technique (Delbecq & Van de Ven, 1971) and in quality-circle practice. Brainwriting has multiple lineages; this skill treats them as convergent, not singular.

## Related lineage worth naming

- **Alex Osborn** popularised verbal brainstorming (1953) and its four rules — defer judgment, go for quantity, encourage wild ideas, combine and improve. Brainwriting keeps the rules and changes the medium; "combine and improve" becomes the explicit build pass.
- **Nominal Group Technique** (Delbecq & Van de Ven, 1971) independently formalised silent written generation followed by round-robin sharing and voting. Its influence is visible in the quiet-first and round-robin rules here.
- **Horst Geschka** and others at Battelle and in German industry extended written idea-generation variants (including brainwriting-pool and card-based methods) in the 1970s. Attribution varies by variant; treat the family as a cluster of adaptations rather than one canonical procedure.

## What is original here

The following are practical workflow adaptations for this repository, not Rohrbach's or Warfield's text:

- The six-step process: intake, silent pass 1, silent pass 2 on one's own list, distribute-and-build, cluster, harvest-and-probe.
- The **second solo pass** as a standard step, and the rule that builds must cite the ID they extend.
- The **async protocol** (silent generation window, build window, freeze, cluster before discussion).
- The **clustering output format**, build-edge tracking, and the cluster-to-concept sentence pattern.
- The clinic worked example, the comparison tables, facilitation scripts, and anti-anchoring rules.
- The sheet and rotation generator in `scripts/brainwrite.py`.

Attribute the core method to Rohrbach and the equal-voice, facilitated-group tradition to Warfield and the nominal-group lineage; attribute the elaborations above to this skill as adaptations.

## Evidence and limits

- **Quantity.** Controlled comparisons consistently find that interacting verbal brainstorming groups produce fewer ideas than nominal groups (individuals generating alone whose ideas are later pooled). Diehl and Stroebe's work (1987) identified production blocking, evaluation apprehension, and social loafing as causes; meta-analytic reviews (e.g., Mullen, Johnson & Salas, 1991) support a productivity loss in interactive groups. Brainwriting is designed to capture the nominal-group advantage while retaining a group's knowledge pool.
- **Quality is not guaranteed.** More ideas do not automatically yield better ones. Studies of idea generation frequently find a quantity–quality trade-off in *selection*: groups often choose feasible, familiar ideas over original ones. That is why this skill separates harvest from evaluation and asks for probes.
- **Builds can converge.** Reading others' entries stimulates combinations but also pulls writers toward the existing semantic field. The two-pass structure (own list first) mitigates this; it does not eliminate it.
- **Facilitation effects are large.** A senior voice during generation, circulating examples, or clustering by author can erase the method's advantage. The protocol, not the label, is what matters.
- **No head-to-head proof for this exact workflow.** The specific sequence here (two solo passes, one build rotation, cluster, probe) is an adaptation assembled from the literature and practice; it has not been validated as a single intervention. Do not cite it as an evidence-based protocol.
- **AI-assisted mode is not equivalent.** A language model generating "six perspectives" produces correlated text from one model, not independent human contributions. It can help with breadth, transcription, and clustering; it cannot reproduce the social-independence benefit.
- **Do not cite the worked example's numbers as findings.** They are invented for illustration.

## Permissions note

No third-party text is reproduced beyond short attributed facts. The method is summarised and linked; the helper script generates blank templates and rotation schedules only and bundles no proprietary checklist or worksheet.
