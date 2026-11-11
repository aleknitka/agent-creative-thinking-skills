#!/usr/bin/env python3
"""eights.py — offline eight-slot worksheet generator for the Crazy Eights skill.

Builds the text adaptation of the eight-frame Crazy Eights sheet: eight time
boxes, optional variety seeds, and the fields that keep slots from collapsing
into rewordings. No network, no dependencies, no third-party content.

Usage:
  python scripts/eights.py --prompt "How might we help a new analyst reach a first useful dashboard on day one?"
  python scripts/eights.py --prompt "..." --minutes 8 --constraints "no new headcount; data stays in the warehouse"
  python scripts/eights.py --prompt "..." --no-seeds
  python scripts/eights.py --prompt "..." --json
  python scripts/eights.py --list-seeds
"""
from __future__ import annotations

import argparse
import json
import sys

SEEDS: list[tuple[str, str]] = [
    ("first concrete idea", "Write the first version that fits the slot; do not pick the best one."),
    ("opposite", "Invert the dominant mechanism of slot 1 (add -> remove, opt-in -> default)."),
    ("different actor", "Hand the work to a different person, machine, or community."),
    ("borrowed", "Adapt a mechanism from another industry or domain."),
    ("constraint removed", "Suspend one assumed constraint and say which one."),
    ("extreme", "Set a parameter to 10x or 1/10 (price, speed, frequency, scope)."),
    ("boring baseline", "The do-nothing or keep-as-is option; it is a real comparator."),
    ("cheap and strange", "Lowest-cost concept you would still be willing to test."),
]

FIELDS = ["Concept (1-2 sentences)", "Mechanism (3-6 words)", "Differs from", "Assumption"]


def clock(seconds: float) -> str:
    seconds = int(round(seconds))
    return f"{seconds // 60}:{seconds % 60:02d}"


def slots(minutes: float) -> list[dict[str, str]]:
    total = minutes * 60
    out = []
    for i in range(8):
        out.append(
            {
                "slot": str(i + 1),
                "time": f"{clock(i * total / 8)}-{clock((i + 1) * total / 8)}",
                "seed": SEEDS[i][0],
                "seed_prompt": SEEDS[i][1],
            }
        )
    return out


def worksheet(prompt: str, minutes: float, constraints: str, seeds: bool) -> str:
    per_slot = minutes * 60 / 8
    lines = [
        "Crazy Eights — eight slots, eight minutes",
        "=" * 46,
        f"Prompt: {prompt}",
    ]
    if constraints:
        lines.append(f"Constraints: {constraints}")
    lines += [
        f"Clock: {minutes:g} minutes total ({per_slot:.0f} seconds per slot)",
        "",
        "Fill one slot per time box. No judging, no rewriting, no borrowing time.",
        "A slot is a 1-2 sentence concept plus a mechanism label — not a title.",
        "",
    ]
    if seeds:
        lines += [
            "Variety seeds (prompts, not requirements):",
            *[f"  {i + 1}. {name}: {tip}" for i, (name, tip) in enumerate(SEEDS)],
            "",
        ]
    lines += [
        "| Slot | Time | Concept (1-2 sentences) | Mechanism (3-6 words) | Differs from | Assumption |",
        "|---|---|---|---|---|---|",
    ]
    for s in slots(minutes):
        lines.append(f"| {s['slot']} | {s['time']} |  |  |  |  |")
    lines += [
        "",
        "After the clock:",
        "  1. Read all eight in order without defending them.",
        "  2. Name the mechanism of each; count distinct mechanisms (aim for 4+).",
        "  3. Cluster by mechanism, not wording.",
        "  4. Harvest 2-3 concepts and give each one probe with a signal.",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Crazy Eights eight-slot worksheet (offline)")
    parser.add_argument("--prompt", help='problem as a "How might we..." question')
    parser.add_argument("--minutes", type=float, default=8, help="total minutes (default 8)")
    parser.add_argument("--constraints", default="", help="hard constraints to keep visible")
    parser.add_argument("--no-seeds", action="store_true", help="omit variety seeds")
    parser.add_argument("--list-seeds", action="store_true", help="show the variety seeds and exit")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args()

    if args.list_seeds:
        if args.json:
            print(json.dumps([{"name": n, "prompt": p} for n, p in SEEDS], indent=2))
        else:
            for i, (name, tip) in enumerate(SEEDS, 1):
                print(f"{i}. {name}: {tip}")
        return 0

    if not args.prompt:
        parser.error("--prompt is required (or use --list-seeds)")
    if args.minutes < 1:
        parser.error("--minutes must be at least 1")

    seed_rows = slots(args.minutes)
    if args.no_seeds:
        for row in seed_rows:
            row["seed"] = ""
            row["seed_prompt"] = ""

    if args.json:
        print(
            json.dumps(
                {
                    "method": "crazy-eights",
                    "mode": "text-adaptation",
                    "prompt": args.prompt,
                    "constraints": args.constraints,
                    "minutes": args.minutes,
                    "seconds_per_slot": args.minutes * 60 / 8,
                    "fields": FIELDS,
                    "slots": seed_rows,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(worksheet(args.prompt, args.minutes, args.constraints, not args.no_seeds))
    return 0


if __name__ == "__main__":
    sys.exit(main())
