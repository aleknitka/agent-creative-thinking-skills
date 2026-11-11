#!/usr/bin/env python3
"""
route.py — deterministic helper for thinking-router.

Scores the 38 creative-thinking methods against intake signals and proposes
a ranked shortlist. Runs offline, no dependencies.

Usage:
  python scripts/route.py --need "better question" --appetite medium --time 30 \
    --trigger "vague brief right question" --output "better question" --text "brief is vague, are we asking the right question?"

  python scripts/route.py --need "more ideas" --appetite high --time 20 \
    --text "we have a baseline concept and need varied alternatives like SCAMPER"

  python scripts/route.py --list   # print catalog with groups
"""
from __future__ import annotations

import argparse
import re
import textwrap
from dataclasses import dataclass

# Must match references/catalog.md (38 entries: 27 base + 11 extended).
@dataclass(frozen=True)
class Method:
    slug: str
    name: str
    group: str  # better-question | more-ideas | broader-perspectives | stronger-options
    star: bool
    triggers: str  # free text for substring matching
    output: str  # better-question | more-ideas | broader-perspectives | stronger-options

METHODS: list[Method] = [
    # Reframe — better question (6)
    Method("lateral-thinking", "Lateral Thinking", "better-question", True, "stuck samey dominant idea indirect provocations lateral outside box", "better-question"),
    Method("first-principles", "First-Principles Thinking", "better-question", False, "how it is done convention inherited assumption fundamental constraints", "better-question"),
    Method("challenge-assumptions", "Assumption Challenging", "better-question", True, "overconstrained hidden beliefs assumption inventory false unnecessary reversed", "better-question"),
    Method("question-storming", "Question Storming", "better-question", False, "vague brief questions before answers who defines revised problem statement right question", "better-question"),
    Method("abstraction-laddering", "Abstraction Laddering", "better-question", False, "too narrow too abstract why does it matter how could this happen ladder up down", "better-question"),
    Method("inversion", "Inversion", "better-question", False, "guarantee failure opposite unwanted outcome obstacles", "better-question"),
    # Generate — more ideas (9 base + 5 extended: SIT, C-K, bodystorming, synectics, lotus-blossom)
    Method("scamper", "SCAMPER", "more-ideas", True, "improve existing product workflow substitute combine adapt modify eliminate reverse rearrange", "more-ideas"),
    Method("reverse-brainstorming", "Reverse Brainstorming", "more-ideas", False, "brainstorming stalled make worse", "more-ideas"),
    Method("forced-connections", "Forced Connections", "more-ideas", False, "too similar surprising random stimulus forced connections unrelated word", "more-ideas"),
    Method("analogical-thinking", "Analogical Thinking", "more-ideas", True, "other fields domains structurally similar transfer mechanism analogy", "more-ideas"),
    Method("morphological-analysis", "Morphological Analysis", "more-ideas", True, "dimensions independent choices matrix combinations systematic system", "more-ideas"),
    Method("brainwriting", "Brainwriting", "more-ideas", False, "anchoring early suggestions written batches", "more-ideas"),
    Method("crazy-eights", "Crazy 8s", "more-ideas", False, "quick burst eight rapid alternatives", "more-ideas"),
    Method("constraint-driven-ideation", "Constraint-Driven Ideation", "more-ideas", False, "open brief generic constraints no interface no budget offline", "more-ideas"),
    Method("ideal-final-result", "Ideal Final Result", "more-ideas", False, "incremental insufficient ideal benefit minimal complexity cost harm TRIZ", "more-ideas"),
    Method("systematic-inventive-thinking", "Systematic Inventive Thinking", "more-ideas", False, "closed world inside the box subtraction multiplication division task unification attribute dependency existing components no new resources", "more-ideas"),
    Method("c-k-theory", "C-K Theory", "more-ideas", False, "c-k concept knowledge expansion partition undecidable generative variation exhausted selection design square hatchuel weil restrictive expansive learning agenda", "more-ideas"),
    Method("bodystorming", "Bodystorming", "more-ideas", False, "bodystorming embodied enactment props space role play walkthrough spatial service interaction hard picture handoffs touchpoints friction threshold waiting recovery", "more-ideas"),
    Method("synectics", "Synectics + Excursion", "more-ideas", False, "synectics excursion personal direct symbolic fantasy analogy analogies familiar strange shallow forced connections mechanism springboard gordon prince", "more-ideas"),
    Method("lotus-blossom", "Lotus Blossom", "more-ideas", False, "lotus blossom radial 8x8 centre petals blooms matsumura divergence hierarchical", "more-ideas"),
    # Perspectives — broader perspectives (7 base + 3 extended: rich-picture, causal-loop, liberating-structures)
    Method("six-thinking-hats", "Six Thinking Hats", "broader-perspectives", True, "brainstorming brainstorming criticism critique interrupt interrupting hats white red black yellow green blue modes keep", "broader-perspectives"),
    Method("dreamer-realist-critic", "Disney Creative Strategy", "broader-perspectives", False, "bold vision idea execution route dreamer realist critic phases distinct disney strategy", "broader-perspectives"),
    Method("stakeholder-perspectives", "Stakeholder Perspective-Taking", "broader-perspectives", False, "needs constraints overlooked groups burden tradeoff stakeholder who does this hurt", "broader-perspectives"),
    Method("what-if", "What-If Exploration", "broader-perspectives", True, "blue sky abundant disappeared what if assumption change alternative worlds", "broader-perspectives"),
    Method("scenario-planning", "Scenario Planning", "broader-perspectives", False, "plausible future futures scenario scenarios uncertainties uncertain robust signals planning", "broader-perspectives"),
    Method("backcasting", "Backcasting", "broader-perspectives", False, "desired future backward milestones long-term ambition route backcasting backcast", "broader-perspectives"),
    Method("futures-wheel", "Futures Wheel", "broader-perspectives", False, "immediate consequences consequences of consequences ripple unintended effects wheel second order", "broader-perspectives"),
    Method("rich-picture-catwoe", "Rich Picture + CATWOE", "broader-perspectives", False, "rich picture catwoe customers actors transformation worldview owners environment checkland soft systems messy situation root definition", "broader-perspectives"),
    Method("causal-loop-diagram", "Causal Loop Diagram", "broader-perspectives", False, "causal loop reinforcing balancing feedback delay archetype leverage polarity fix keeps making problem worse structure behavior over time system dynamics fixes that fail shifting burden limits success", "broader-perspectives"),
    Method("liberating-structures", "Liberating Structures", "broader-perspectives", False, "liberating structures 1-2-4-all impromptu networking 15% solutions TRIZ wicked questions ecocycle facilitation micro-structure hierarchy", "broader-perspectives"),
    Method("board-game-abstraction", "Board-Game Abstraction", "broader-perspectives", False, "board game abstraction playable mechanics players board resources loop win loss gamify abstract system politics", "broader-perspectives"),
    # Decide — stronger options (5 base + 2 extended: NGT, dot-voting)
    Method("double-diamond", "Double Diamond", "stronger-options", False, "discover define develop deliver divergence convergence structure diamond", "stronger-options"),
    Method("triz-contradictions", "TRIZ Contradiction Thinking", "stronger-options", False, "contradiction tradeoff trade tradeoffs recurring fixing breaks worsens improving one property worsens another inventive principles separation compromise technical triz", "stronger-options"),
    Method("concept-blending", "Concept Blending", "stronger-options", False, "combine mechanisms synthesized coherent partial ideas strengths blending", "stronger-options"),
    Method("premortem", "Premortem", "stronger-options", True, "already failed failure hypotheses warning signs strengthen before commitment premortem fail", "stronger-options"),
    Method("options-portfolio", "Options Portfolio", "stronger-options", False, "mix achievable ambitious exploratory retain narrowing portfolio experiment robust options", "stronger-options"),
    Method("nominal-group-technique", "Nominal Group Technique", "stronger-options", False, "nominal group technique NGT Delphi silent write round robin clarify vote ranked ranking consensus anonymous expert rating dissent defensible prioritization hierarchy bias", "stronger-options"),
    Method("dot-voting-prioritize", "Dot Voting + Impact-Effort", "stronger-options", False, "dot voting impact effort ICE prioritize N/3 dots keep pivot kill preference ranking", "stronger-options"),
]

NEED_KEYWORDS: dict[str, set[str]] = {
    "better-question": {"vague", "overconstrained", "assumption", "right", "question", "stuck", "reframe", "narrow", "abstract", "why", "brief", "define", "framing"},
    "more-ideas": {"baseline", "concept", "improve", "varied", "alternatives", "scamper", "dimensions", "similar", "anchoring", "modify", "variations", "closed", "subtraction", "synectics", "excursion", "bodystorming", "enactment", "expansion", "partition", "lotus", "blossom", "radial", "blooms", "petals"},
    "broader-perspectives": {"stakeholder", "future", "futures", "scenario", "scenarios", "consequences", "ripple", "what", "uncertain", "uncertainties", "perspectives", "broad", "effects", "hurt", "overlooked", "signals", "criticism", "critique", "interrupt", "interrupting", "vision", "bold", "route", "backcasting", "wheel", "feedback", "loop", "loops", "reinforcing", "balancing", "archetype", "leverage", "rich", "picture", "catwoe", "worldview", "messy", "liberating", "structures", "facilitation", "ecocycle", "wicked", "board", "game", "abstraction", "mechanics", "players", "playable", "gamify"},
    "stronger-options": {"tradeoff", "tradeoffs", "trade", "contradiction", "recurring", "fixing", "breaks", "portfolio", "premortem", "failed", "failure", "candidate", "choose", "commit", "worsens", "robust", "strengthen", "fail", "rank", "ranking", "vote", "voting", "dots", "consensus", "NGT", "Delphi", "prioritize", "prioritization", "keep", "kill", "impact", "effort", "ICE"},
}

GROUP_ALIASES = {
    "better-question": "better-question",
    "reframe": "better-question",
    "better question": "better-question",
    "more-ideas": "more-ideas",
    "more ideas": "more-ideas",
    "generate": "more-ideas",
    "broader-perspectives": "broader-perspectives",
    "broader perspectives": "broader-perspectives",
    "explore": "broader-perspectives",
    "stronger-options": "stronger-options",
    "stronger options": "stronger-options",
    "decide": "stronger-options",
}

def tokenize(s: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", s.lower()))

def infer_need(trigger_tokens: set[str]) -> str | None:
    if not trigger_tokens:
        return None
    scores = {k: len(v & trigger_tokens) for k, v in NEED_KEYWORDS.items()}
    best = max(scores, key=lambda k: scores[k])
    return best if scores[best] > 0 else None

def score_method(m: Method, need: str | None, trigger_tokens: set[str], output_need: str | None, appetite: str, time_min: int | None) -> tuple[float, dict]:
    m_tokens = tokenize(m.triggers + " " + m.slug + " " + m.name)
    overlap = len(trigger_tokens & m_tokens) if trigger_tokens else 0
    if overlap >= 3:
        trigger = 2
    elif overlap >= 1:
        trigger = 1
    else:
        trigger = 1 if (need and m.group == need and trigger_tokens) else 0
        if not trigger_tokens and need and m.group == need:
            trigger = 1

    if output_need:
        output = 2 if m.group == output_need else (1 if need and m.group == need else 0)
    else:
        output = 2 if (need and m.group == need) else 0

    wild = {"lateral-thinking", "what-if", "forced-connections", "ideal-final-result", "constraint-driven-ideation", "synectics", "c-k-theory"}
    if appetite == "low" and m.slug in wild:
        appetite_s = 0
    elif appetite == "high" or m.slug not in wild:
        appetite_s = 1
    else:
        appetite_s = 1

    budgets = {
        "question-storming": 15, "abstraction-laddering": 12, "inversion": 12,
        "challenge-assumptions": 20, "lateral-thinking": 20, "scamper": 20, "premortem": 18,
        "analogical-thinking": 15, "forced-connections": 12, "crazy-eights": 10, "what-if": 15,
        "options-portfolio": 15, "concept-blending": 15, "constraint-driven-ideation": 15,
        "morphological-analysis": 30, "futures-wheel": 25, "stakeholder-perspectives": 25,
        "scenario-planning": 45, "backcasting": 40, "dreamer-realist-critic": 35, "six-thinking-hats": 35,
        "double-diamond": 60, "triz-contradictions": 35, "brainwriting": 20, "reverse-brainstorming": 15,
        "ideal-final-result": 15,
        "systematic-inventive-thinking": 20, "c-k-theory": 30, "bodystorming": 35, "rich-picture-catwoe": 35, "causal-loop-diagram": 35, "synectics": 25, "liberating-structures": 30, "nominal-group-technique": 45, "lotus-blossom": 30, "dot-voting-prioritize": 15,
    }
    if time_min is None:
        time_s = 1
    else:
        budget = budgets.get(m.slug, 20)
        time_s = 1 if time_min >= budget * 0.6 else 0

    star_bonus = 0.15 if m.star else 0.0
    total = trigger * 2 + output * 2 + appetite_s + time_s + star_bonus
    breakdown = {"trigger": trigger, "output": output, "appetite": appetite_s, "time": time_s, "star": star_bonus}
    return total, breakdown

def main() -> None:
    p = argparse.ArgumentParser(description="Thinking-router scorer")
    p.add_argument("--need", help="primary need: better-question | more-ideas | broader-perspectives | stronger-options (aliases: reframe/generate/explore/decide)")
    p.add_argument("--output", help="desired artifact (same values as --need)")
    p.add_argument("--trigger", help="trigger phrases / user wording to match")
    p.add_argument("--text", help="alias for --trigger (free text)")
    p.add_argument("--appetite", choices=["low", "medium", "high"], default="medium")
    p.add_argument("--time", type=int, default=None, help="minutes available")
    p.add_argument("--top", type=int, default=5)
    p.add_argument("--list", action="store_true", help="list catalog and exit")
    p.add_argument("--verbose", action="store_true")
    args = p.parse_args()

    if args.list:
        cur = None
        for m in METHODS:
            if m.group != cur:
                cur = m.group
                print(f"\n## {cur}")
            print(f"  {'★ ' if m.star else '  '}{m.slug:30s} {m.name}")
        return

    need = GROUP_ALIASES.get((args.need or "").lower().strip(), None) if args.need else None
    output_need = GROUP_ALIASES.get((args.output or "").lower().strip(), None) if args.output else need
    trigger_text = args.trigger or args.text or ""
    trigger_tokens = tokenize(trigger_text)

    if not need:
        inferred = infer_need(trigger_tokens)
        if inferred:
            need = inferred
            if not output_need:
                output_need = inferred

    if not need and not trigger_tokens and not output_need:
        print(textwrap.dedent("""
            No signals given. Try:
              python scripts/route.py --need "better question" --text "brief is vague, are we asking the right question?"
              python scripts/route.py --text "stuck on a recurring tradeoff fixing A breaks B"
              python scripts/route.py --need "more ideas" --text "have a baseline concept to improve with SCAMPER"
        """).strip())
        return

    scored = []
    for m in METHODS:
        total, breakdown = score_method(m, need, trigger_tokens, output_need, args.appetite, args.time)
        scored.append((total, m, breakdown))
    scored.sort(key=lambda x: x[0], reverse=True)

    top_n = scored[: args.top]
    print(f"Need: {need or '(inferred)'}  Output: {output_need or need or '(inferred)'}  Appetite: {args.appetite}  Time: {args.time or '—'} min")
    if trigger_text:
        print(f"Triggers: {trigger_text!r}")
    print()
    for rank, (total, m, br) in enumerate(top_n, 1):
        star = " ★" if m.star else ""
        if args.verbose:
            print(f"{rank}. {m.slug} ({m.name}){star} — score {total:.2f}  [trigger={br['trigger']} output={br['output']} appetite={br['appetite']} time={br['time']} star={br['star']}]")
        else:
            print(f"{rank}. {m.slug} ({m.name}){star} — score {total:.2f}")

    best = top_n[0]
    alt = top_n[1] if len(top_n) > 1 else None
    skipped = top_n[2] if len(top_n) > 2 else None
    print()
    print(f"Primary:  {best[1].slug} — {best[1].name}")
    if alt:
        print(f"Alternate:{alt[1].slug} — {alt[1].name} (when you'd pick this instead)")
    if skipped:
        print(f"Not now:  {skipped[1].slug} — strongest contender skipped this time")
    print()
    print("Handoff: pass the routing note (need/method/intake/next artifact) to the next skill.")
    print("Confirm with the user before running the routed method.")

if __name__ == "__main__":
    main()
