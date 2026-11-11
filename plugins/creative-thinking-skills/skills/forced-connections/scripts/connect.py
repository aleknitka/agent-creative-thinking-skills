#!/usr/bin/env python3
"""connect.py — offline seeded stimulus generator for forced-connections.

Draws a concrete stimulus from original banks (word / object / image / concept)
and prints forcing prompts. No network, no dependencies, deterministic with
--seed.

Usage:
  python scripts/connect.py                              # one mixed stimulus
  python scripts/connect.py --type word --seed 4         # reproduce a draw
  python scripts/connect.py --type concept --count 5     # five candidates
  python scripts/connect.py --problem "onboarding is slow"
  python scripts/connect.py --json --count 3
  python scripts/connect.py --list                       # show all banks
  python scripts/connect.py --list word                  # show one bank

Banks are original and short. Expand only with MIT-compatible or
public-domain sources (see references/provenance.md).
"""
from __future__ import annotations

import argparse
import json
import random
import sys

WORD_BANK: list[str] = [
    "nose", "telescope", "river", "knot", "compass", "orchard", "lantern",
    "bicycle", "echo", "harbor", "mushroom", "postcard", "mirror", "anchor",
    "comet", "ladder", "thimble", "avalanche", "quilt", "harvest", "desert",
    "carousel", "volcano", "passport", "antenna", "fossil", "whistle",
    "lighthouse", "canyon", "umbrella", "beehive", "cathedral", "turnstile",
    "satellite", "papyrus", "kiln", "coral", "turntable", "archipelago",
    "sundial", "trellis", "obelisk", "ferry", "glacier", "bazaar",
    "periscope", "windmill", "pagoda", "harpsichord", "compost", "escrow",
    "ratchet", "sieve", "foghorn", "seedbank", "scaffold", "abacus",
    "tidepool", "foundry", "cartridge", "weathervane",
]

OBJECT_BANK: list[str] = [
    "turnstile", "tea strainer", "padlock", "seed packet", "fire escape",
    "library date stamp", "door hinge", "thermostat", "ratchet strap",
    "anchor chain", "clothes peg", "chalk line", "spirit level", "dimmer switch",
    "smoke alarm", "corkscrew", "colander", "measuring tape", "bicycle pump",
    "safety pin", "cable tie", "shutter", "sundial", "plumb bob",
    "flypaper", "water filter", "ticket punch", "wind-up timer",
    "combination lock", "mousetrap", "bookmark", "snow shovel",
    "postage scale", "drain trap", "lighthouse lens", "train timetable",
]

IMAGE_BANK: list[str] = [
    "a tide pool at low tide, water receding from the rocks",
    "a bridge being repainted one section at a time",
    "a night market with numbered stalls and a single queue",
    "a beehive cross-section with capped and open cells",
    "a library shelf of due-date cards, some untouched for years",
    "a rooftop rainwater tank with an overflow pipe",
    "a theatre fly system with ropes, weights, and counterweights",
    "a harbour at dawn, boats waiting for the lock to open",
    "a potter's wheel with a half-thrown bowl",
    "a field of contour lines drawn on a hillside",
    "a repair café with disassembled appliances on trestle tables",
    "a railway signal box with levers and an interlocking frame",
    "a greenhouse with vents that open by wax actuator",
    "a moth trap at night, funnel and collecting jar",
]

CONCEPT_BANK: list[str] = [
    "escrow", "succession", "quorum", "keystone species", "seed dormancy",
    "dead reckoning", "airlock", "contour lines", "trophic cascade",
    "temperature inversion", "right of way", "sunk cost", "cartography",
    "erosion", "osmosis", "feedback loop", "flywheel", "path dependence",
    "tragedy of the commons", "circuit breaker", "crop rotation", "annealing",
    "pasteurization", "dry stone walling", "coppicing", "ballast",
    "watershed", "estuary", "moraine", "aqueduct", "tidal locking",
    "grafting", "fallow period", "siltation",
]

BANKS: dict[str, list[str]] = {
    "word": WORD_BANK,
    "object": OBJECT_BANK,
    "image": IMAGE_BANK,
    "concept": CONCEPT_BANK,
}

PROPERTY_PROMPTS = [
    ("Material / parts", "What is it made of? What are its pieces?"),
    ("Affordances", "What does it let you do, forbid, or make effortful?"),
    ("Structural", "What is its shape, boundary, or layering?"),
    ("Temporal", "What is its lifecycle, cadence, or latency?"),
    ("Relational", "Who operates it, who benefits, what does it separate?"),
    ("Quantity / ratio", "What must be balanced or proportioned?"),
    ("Failure", "How does it break, jam, stall, or get defeated?"),
]

FORCING_PROMPTS = [
    "List 8-10 literal properties before interpreting the stimulus.",
    "For each property: if the problem had this property, what would change?",
    "Complete: 'This is like the stimulus because ...' with a causal clause.",
    "Steal the verb: what action does the stimulus suggest, and where would it apply?",
    "Reject the draw if you can say in one sentence why it is relevant to your domain.",
]


def pick(bank: str, count: int, seed: int | None) -> list[dict]:
    rnd = random.Random(seed)
    kinds = list(BANKS) if bank == "mixed" else [bank]
    out: list[dict] = []
    for i in range(count):
        kind = rnd.choice(kinds)
        # sample without replacement within a single draw batch when possible
        pool = BANKS[kind]
        already = [o["stimulus"] for o in out if o["type"] == kind]
        choices = [x for x in pool if x not in already] or pool
        out.append({"type": kind, "stimulus": rnd.choice(choices), "_i": i})
    for o in out:
        o.pop("_i", None)
    return out


def render(stimuli: list[dict], problem: str) -> str:
    lines: list[str] = []
    if problem:
        lines.append(f"Problem: {problem.strip()}")
        lines.append("")
    if len(stimuli) == 1:
        s = stimuli[0]
        lines.append(f"Stimulus [{s['type']}]: {s['stimulus']}")
        lines.append("")
        lines.append("Do not interpret it yet. Inventory its literal properties:")
        for label, prompt in PROPERTY_PROMPTS:
            lines.append(f"  - {label}: {prompt}")
        lines.append("")
        lines.append("Then force the connection:")
        for p in FORCING_PROMPTS:
            lines.append(f"  - {p}")
    else:
        lines.append(f"{len(stimuli)} candidates — pick one without curating for relevance:")
        for n, s in enumerate(stimuli, 1):
            lines.append(f"  {n}. [{s['type']}] {s['stimulus']}")
        lines.append("")
        lines.append("Record the chosen stimulus, its source, and the other candidates.")
    lines.append("")
    lines.append("Next: property inventory -> property mapping -> analogy sprint "
                 "(see references/forcing.md).")
    return "\n".join(lines)


def main() -> None:
    p = argparse.ArgumentParser(description="Forced-connections stimulus generator (offline, seeded)")
    p.add_argument("--type", choices=["word", "object", "image", "concept", "mixed"],
                   default="mixed", help="bank to draw from (default: mixed)")
    p.add_argument("--count", type=int, default=1,
                   help="number of candidate stimuli (default 1)")
    p.add_argument("--seed", type=int, default=None, help="seed for reproducibility")
    p.add_argument("--problem", type=str, default="", help="optional problem statement to frame the draw")
    p.add_argument("--json", action="store_true", help="emit JSON instead of text")
    p.add_argument("--list", nargs="?", const="all", choices=["all", *BANKS],
                   help="print a bank (default: all) and exit")
    args = p.parse_args()

    if args.list:
        names = list(BANKS) if args.list == "all" else [args.list]
        for name in names:
            print(f"# {name}")
            for item in BANKS[name]:
                print(item)
            print()
        return

    if args.count < 1:
        print("error: --count must be >= 1", file=sys.stderr)
        sys.exit(2)

    stimuli = pick(args.type, args.count, args.seed)

    if args.json:
        payload = {
            "problem": args.problem or "",
            "stimuli": stimuli,
            "property_prompts": [{"category": c, "prompt": q} for c, q in PROPERTY_PROMPTS],
            "forcing_prompts": FORCING_PROMPTS,
            "next": "Inventory properties, map them to the problem, then evaluate novelty x usefulness.",
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return

    print(render(stimuli, args.problem))


if __name__ == "__main__":
    main()
