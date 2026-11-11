# Provenance, Lineage, and Evidence Limits

## Origin

Lotus Blossom is a Japanese brainstorming and idea-organising method developed by **Matsumura Yasuo** (松村寧雄) at **Clover Management Research** in the 1980s. It is usually written in Japanese as 蓮華智慧（ロータス・ブロッサム）or simply the Lotus method, and it was popularised in English through creativity and facilitation literature as the "Lotus Blossom technique".

The name comes from the layout: ideas bloom outward from a center in successive rings, like lotus petals opening. The standard artifact is a sheet divided into a 3×3 grid of 3×3 blocks, with the theme in the middle block. The eight surrounding blocks are angles or sub-themes; each becomes the center of its own block, and eight ideas are written around it.

The method was designed for business planning and quality circles as much as for pure ideation. Matsumura's framing is closer to structured problem decomposition than to free brainstorming: the point is to make a theme's parts visible and then populate each part systematically.

## What is original here

- **The eight-operation expansion prompts** used in layer 3 (first idea, add, remove, invert, combine, magnify, minify, delegate). These are assembled for this skill from general ideation practice and overlap with SCAMPER-family operators. They are not part of Matsumura's published procedure; treat them as optional scaffolding.
- **The default eight petal angles** (actors, moment, place, mechanism, incentive, artifact, constraint, signal). This is a domain-neutral set written for this skill; Matsumura's examples are domain-specific.
- **The timing table, the facilitation variants, colour coding, and the online/offline artifacts.** These are practical adaptations, not canonical instructions.
- **The helper script** (`scripts/lotus.py`) and its JSON schema. Original scaffolding; no third-party content.

No proprietary worksheets, book text, or course materials are reproduced. The method name and the high-level 3×3 radial structure are attributed, not licensed.

## Lineage and neighbours

- **KJ method (Kawakita Jiro)** and Japanese quality-circle practice: structured group sense-making and theme decomposition. Lotus Blossom shares the culture of visible, structured boards.
- **Mind mapping (Buzan)** and **concept fan** diagrams: radial expansion from a center. Lotus Blossom differs by imposing a fixed 8-slot ring at every layer rather than free branching.
- **Morphological analysis (Zwicky)**: also a grid-based expansion, but it enumerates independent dimensions and combinations. Lotus Blossom partitions one theme into angles; it does not model independence.
- **Futures wheel (Glenn)**: radial, but expands consequences of a change rather than ideas under a theme.
- **SCAMPER (Eberle)**: operation-based variation on an existing object. Its operators informed the optional layer-3 prompts here.

The recurring family resemblance is the grid plus the fixed ring. The distinguishing feature of Lotus Blossom is the **recursive 3×3 block**: each petal becomes a center in its own right, which is why a full board reaches 72 slots without changing the rule.

## Evidence limits

This is a **practitioner heuristic, not a validated intervention**. Relevant cautions:

- Controlled evidence for Lotus Blossom specifically is thin. Claims that it produces "more and better" ideas than unstructured brainstorming are not established; the structure plausibly improves coverage and recall of angles, and it plausibly increases conformity to the eight-slot frame.
- The "eight" is arbitrary. It matches the 3×3 geometry and is small enough to fill and large enough to break the first-idea anchor. There is no evidence eight is optimal.
- The 72-slot capacity is a ceiling, not a target. Groups routinely fill fewer slots, and a half-filled board is still useful; treating 72 as a quota invites filler.
- Fixed petals can over-sample the facilitator's framing. If the eight angles are wrong for the domain, the board systematically misses regions. Run a petal check and be willing to replace angles.
- The method separates generation from evaluation structurally but does not prevent evaluation from leaking into layer 3. Facilitation still matters.
- Recursive expansion has a known failure: near-duplicates across petals. Deduplication is part of the method's real work, not an afterthought.

## Attribution in use

When presenting results, say: "Lotus Blossom, developed by Matsumura Yasuo at Clover Management Research, with a text adaptation and expansion prompts added here." Do not present the adaptations as the original method, and do not imply endorsement by Matsumura or Clover Management Research.

If you publish a derivative board or template, attribute the method, note your changes (especially if you replace the eight petals or the layer-3 operations), and keep the distinction between the canonical 3×3 radial structure and your scaffolding.
