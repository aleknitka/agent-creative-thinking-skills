#!/usr/bin/env python3
"""ls.py - offline picker and step printer for Liberating Structures.

Summarises six facilitation micro-structures used by the liberating-structures
skill: 1-2-4-All, Impromptu Networking, 15% Solutions, TRIZ, Wicked Questions,
and Ecocycle Planning. Entirely offline, no dependencies.

Usage:
  python scripts/ls.py --list
  python scripts/ls.py --list --json
  python scripts/ls.py --structure 1-2-4-All
  python scripts/ls.py --structure triz --json
  python scripts/ls.py --seed 7            # reproducible random pick
  python scripts/ls.py --seed 7 --json

Descriptions are original paraphrase, not reproduced text from
liberatingstructures.com or the book. No worksheets are bundled.
"""
from __future__ import annotations

import argparse
import json
import re
import random
import sys

STRUCTURES: list[dict] = [
    {
        "slug": "1-2-4-all",
        "name": "1-2-4-All",
        "aliases": ["1-2-4-all", "124all", "one-two-four-all"],
        "purpose": "Engage everyone at once in generating and synthesising ideas, scaling from silent individual work to pairs, quads, and the whole group.",
        "time": "12-20 min",
        "people": "6-100+",
        "output": "Themes, questions, and ranked options that survived two rounds of synthesis.",
        "steps": [
            "State one answerable question and the output format; start a 1-minute silent round.",
            "Everyone writes alone; no talking, fragments allowed.",
            "Pairs (2 min each) exchange notes; restate the other's point before adding your own.",
            "Pairs join into quads (4 min); cluster and name the strongest items.",
            "Quads report only what is new, contested, or missing; harvest on one board.",
        ],
        "failure_signals": [
            "The silent minute becomes whispering or phone-checking.",
            "Pairs self-select by seniority instead of counting off.",
            "Quads read their full lists instead of synthesising.",
            "The facilitator adds content during the harvest.",
        ],
    },
    {
        "slug": "impromptu-networking",
        "name": "Impromptu Networking",
        "aliases": ["impromptu-networking", "impromptu", "networking"],
        "purpose": "Build connection quickly and surface the challenges people actually carry before the agenda starts.",
        "time": "15-25 min",
        "people": "8-100+",
        "output": "A pattern list of shared challenges, overlaps, and resources.",
        "steps": [
            "Pose one question, e.g. 'What challenge are you working on right now?'",
            "Everyone finds a partner they do not know well; one speaks for 2 minutes.",
            "Switch; the second person speaks for 2 minutes; listener asks one clarifying question.",
            "New partner and repeat for a total of three rounds.",
            "Harvest one pattern, resource, or overlap per person; capture as a list, not minutes.",
        ],
        "failure_signals": [
            "People keep the same partner across rounds.",
            "The round becomes a pitch or status update.",
            "The harvest is skipped, leaving no artifact.",
            "The room is too loud for pairs to hear each other.",
        ],
    },
    {
        "slug": "15-percent-solutions",
        "name": "15% Solutions",
        "aliases": ["15-percent-solutions", "15percent", "15", "fifteen-percent"],
        "purpose": "Turn 'nothing can change' into concrete action each person can take inside their existing discretion.",
        "time": "20-30 min",
        "people": "5-30",
        "output": "Owned first moves with a first step and a date.",
        "steps": [
            "Restate the challenge and the constraint: no new resources, budget, or mandate.",
            "Each person writes their own 15%: what they can do now with what they already have.",
            "In threes, each person shares for 2 minutes; others ask only 'what would make that easier?' and 'what is the first 30 minutes?'",
            "Sharpen each action until it has a first step, an owner, and a date.",
            "Harvest on one board; log shared blockers as escalation items, not reasons to wait.",
        ],
        "failure_signals": [
            "Actions ask for budget, headcount, or leadership permission.",
            "Small groups turn into complaint sessions.",
            "Actions are aspirations ('improve onboarding') rather than first moves.",
            "No action carries a date.",
        ],
    },
    {
        "slug": "triz",
        "name": "TRIZ",
        "aliases": ["triz", "ls-triz", "wreck-the-org", "wreck-the-organisation", "stop-doing"],
        "purpose": "Surface and stop the practices that reliably produce failure, by designing the worst outcome first.",
        "time": "45-60 min",
        "people": "6-30",
        "output": "A stop list with owners and replacement behaviours.",
        "steps": [
            "State the goal positively, e.g. 'customers onboard within a week'.",
            "Ask: what would we do to guarantee the worst possible result? Generate a long, specific list.",
            "Vote for the five to seven actions that would most reliably produce failure.",
            "Ask which of these the group is already doing, at least partially. No defending yet.",
            "Build a stop list: what stops, who owns it, and what replaces it.",
            "Schedule a review against the stop list, not against intentions.",
        ],
        "failure_signals": [
            "Worst-result ideas are jokes or caricatures.",
            "The 'are we already doing this?' turn is skipped.",
            "The stop list says 'communicate better' instead of naming a practice.",
            "No one owns the stopping, or a senior person vetoes items during generation.",
        ],
    },
    {
        "slug": "wicked-questions",
        "name": "Wicked Questions",
        "aliases": ["wicked-questions", "wicked", "paradox"],
        "purpose": "Articulate competing commitments that are both true, so the group manages the tension instead of pretending to resolve it.",
        "time": "25-40 min",
        "people": "5-20",
        "output": "Two or three tested 'How can we ... and ...?' questions used as standing frames.",
        "steps": [
            "Each person writes tensions they experience as 'we need X, but we also need Y'.",
            "In pairs, combine and sharpen the tensions; drop any where one side is only a preference.",
            "Craft each candidate as 'How can we ... and ... simultaneously?'",
            "Test: is either side false? Can it be answered by choosing one side? Does it describe daily experience?",
            "Select two or three survivors and post them where later decisions can refer to them.",
        ],
        "failure_signals": [
            "One side is a strawman, producing a fake paradox.",
            "The group starts solving instead of holding the tension.",
            "Questions are abstract enough to fit any organisation.",
            "The selected questions are never referenced again.",
        ],
    },
    {
        "slug": "ecocycle-planning",
        "name": "Ecocycle Planning",
        "aliases": ["ecocycle-planning", "ecocycle", "lifecycle", "portfolio-lifecycle"],
        "purpose": "Place a portfolio on a lifecycle map so renewal and stopping become visible decisions rather than omissions.",
        "time": "60-120 min",
        "people": "6-30",
        "output": "A lifecycle map plus one or two destruction and renewal decisions with owners.",
        "steps": [
            "Draw a figure-eight: gestation/birth, maturity, creative destruction, renewal.",
            "Mark the poverty trap (stuck in gestation) and the rigidity trap (stuck in maturity).",
            "Place every activity, project, or commitment on the map, sized by effort.",
            "Diagnose starvation in gestation, protection in maturity, and gaps in renewal.",
            "Choose one or two items for creative destruction and name what is released and how.",
            "Choose one or two renewal seeds with the smallest experiment that would justify them; assign owners and a review date.",
        ],
        "failure_signals": [
            "Everything is placed in maturity.",
            "Only failed projects are named for destruction; finished successes are protected.",
            "The map becomes a status report with no lifecycle decisions.",
            "Renewal boxes hold ideas nobody is resourced to try.",
            "The group leaves without deciding to stop anything.",
        ],
    },
]


def normalise(text: str) -> str:
    return re.sub(r"[^a-z0-9]", "", text.lower())


def find_structure(query: str) -> dict | None:
    needle = normalise(query)
    if not needle:
        return None
    for structure in STRUCTURES:
        keys = [structure["name"], structure["slug"], *structure["aliases"]]
        if any(normalise(k) == needle for k in keys):
            return structure
    # prefix / substring fallback, e.g. "1-2" or "eco"
    matches = [
        s for s in STRUCTURES
        if any(needle in normalise(k) for k in [s["name"], s["slug"], *s["aliases"]])
    ]
    return matches[0] if len(matches) == 1 else None


def summary(structure: dict) -> dict:
    return {
        "name": structure["name"],
        "slug": structure["slug"],
        "purpose": structure["purpose"],
        "time": structure["time"],
        "people": structure["people"],
        "output": structure["output"],
    }


def print_structure(structure: dict) -> None:
    print(f"{structure['name']}")
    print(f"  Purpose: {structure['purpose']}")
    print(f"  Time:    {structure['time']}   Group: {structure['people']}")
    print(f"  Output:  {structure['output']}")
    print("  Steps:")
    for i, step in enumerate(structure["steps"], 1):
        print(f"    {i}. {step}")
    print("  Watch for:")
    for signal in structure["failure_signals"]:
        print(f"    - {signal}")


def list_text() -> None:
    width = max(len(s["name"]) for s in STRUCTURES)
    print(f"{'Structure'.ljust(width)}  {'Time'.ljust(9)}  Purpose")
    print(f"{'-' * width}  {'-' * 9}  {'-' * 40}")
    for s in STRUCTURES:
        print(f"{s['name'].ljust(width)}  {s['time'].ljust(9)}  {s['purpose']}")


def main() -> int:
    p = argparse.ArgumentParser(
        description="Offline picker for six Liberating Structures (no network)."
    )
    p.add_argument("--list", action="store_true", help="list the six structures and exit")
    p.add_argument("--structure", metavar="NAME", help="print steps for a structure by name or alias")
    p.add_argument("--seed", type=int, default=None, help="seed for a reproducible random pick")
    p.add_argument("--json", action="store_true", help="emit JSON instead of text")
    args = p.parse_args()

    if args.list:
        if args.json:
            print(json.dumps([summary(s) for s in STRUCTURES], indent=2))
        else:
            list_text()
        return 0

    if args.structure:
        structure = find_structure(args.structure)
        if structure is None:
            names = ", ".join(s["name"] for s in STRUCTURES)
            print(f"error: unknown structure '{args.structure}'. Known: {names}", file=sys.stderr)
            return 2
        if args.json:
            print(json.dumps(structure, indent=2))
        else:
            print_structure(structure)
        return 0

    # No explicit action: random pick, reproducible with --seed.
    rnd = random.Random(args.seed)
    structure = rnd.choice(STRUCTURES)
    if args.json:
        payload = dict(structure)
        payload["seed"] = args.seed
        print(json.dumps(payload, indent=2))
    else:
        label = f"seed {args.seed}" if args.seed is not None else "unseeded"
        print(f"Random pick ({label}):")
        print_structure(structure)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
