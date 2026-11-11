#!/usr/bin/env python3
"""lotus.py — offline Lotus Blossom board generator.

Three layers: one central theme -> up to eight petals -> eight sub-ideas per
petal. At eight petals the board holds 8 + 64 = 72 idea slots. No network, no
dependencies, no third-party content.

Usage:
  python scripts/lotus.py --theme "onboarding friction" --petals 8
  python scripts/lotus.py --theme "onboarding friction" --fill blank --export board
  python scripts/lotus.py --theme "onboarding friction" --seed 7 --export json
  python scripts/lotus.py --list
"""
from __future__ import annotations

import argparse
import json
import random
import sys
import textwrap

# Eight petal angles plus two alternates for smaller or regenerated boards.
ANGLES: list[tuple[str, str]] = [
    ("Actors", "Who does the work, who is affected, who is missing?"),
    ("Moment", "When in the journey does this happen, and what precedes it?"),
    ("Place", "Where does it happen: channel, environment, physical context?"),
    ("Mechanism", "How does it actually work, step by step?"),
    ("Incentive", "What makes someone want to do it, or stop avoiding it?"),
    ("Artifact", "What object, document, or interface carries the idea?"),
    ("Constraint", "Which limit could be removed, moved, or turned into an asset?"),
    ("Signal", "How would anyone know it worked, early and cheaply?"),
    ("Ritual", "What repeatable practice makes it stick after the launch?"),
    ("Story", "How is it explained, framed, and remembered?"),
]

# Eight expansion operations applied inside every petal.
OPERATIONS: list[tuple[str, str]] = [
    ("first concrete idea", "Write the first workable idea; do not pick the best one."),
    ("add", "Add a missing actor, step, resource, or touchpoint."),
    ("remove", "Remove or omit the element entirely; keep the rest unchanged."),
    ("invert", "Invert the direction, default, order, or incentive."),
    ("combine", "Combine it with a neighbouring step, idea, or channel."),
    ("magnify", "Scale it up tenfold: frequency, scope, intensity, duration."),
    ("minify", "Scale it down toward zero: cost, effort, time, footprint."),
    ("delegate", "Hand it to a different actor, machine, or community."),
]

POSITIONS = ["NW", "N", "NE", "W", "E", "SW", "S", "SE"]
CELL_W = 22


def fit(text: str, width: int = CELL_W) -> str:
    return textwrap.shorten(text, width=width, placeholder="…")


def build_petals(count: int, seed: int | None) -> list[dict]:
    if count < 1 or count > 8:
        raise ValueError("--petals must be between 1 and 8")
    rng = random.Random(seed)
    angles = ANGLES[:8] if count == 8 else rng.sample(ANGLES, count)
    if count == 8 and seed is not None:
        rng.shuffle(angles)
    return [
        {
            "id": i + 1,
            "position": POSITIONS[i] if count == 8 else f"P{i + 1}",
            "angle": angle,
            "focus": focus,
        }
        for i, (angle, focus) in enumerate(angles)
    ]


def build_slots(petals: list[dict], fill: str, seed: int | None) -> None:
    rng = random.Random(None if seed is None else seed + 1)
    for petal in petals:
        ops = OPERATIONS[:]
        if fill == "random":
            rng.shuffle(ops)
        slots = []
        for j, (name, tip) in enumerate(ops):
            slots.append(
                {
                    "slot": j + 1,
                    "operation": name if fill != "blank" else "",
                    "prompt": f"{tip} Focus on: {petal['angle'].lower()}."
                    if fill != "blank"
                    else "",
                }
            )
        petal["slots"] = slots


def render_block(title: str, slots: list[dict], width: int = CELL_W) -> list[str]:
    sep = "+" + "+".join("-" * width for _ in range(3)) + "+"
    cells = [fit(s["prompt"] or "…", width) for s in slots]
    cells += ["…"] * (8 - len(cells))

    def row(a: str, b: str, c: str) -> str:
        return "|" + "|".join(f" {fit(x, width):<{width - 1}}" for x in (a, b, c)) + "|"

    return [
        sep,
        row(cells[0], cells[1], cells[2]),
        sep,
        row(cells[3], title, cells[4]),
        sep,
        row(cells[5], cells[6], cells[7]),
        sep,
    ]


def text_output(theme: str, petals: list[dict], capacity: int) -> str:
    lines = [
        "Lotus Blossom — one theme, eight petals, eight sub-ideas each",
        "=" * 62,
        f"Central theme: {theme}",
        f"Capacity: {len(petals)} petals + {len(petals) * 8} sub-ideas = {capacity} idea slots",
        "",
        "Layer 1 — the theme; layer 2 — petals (angles); layer 3 — concrete ideas.",
        "Generate top-down. Do not judge a slot before its petal is full.",
        "",
    ]
    for p in petals:
        lines += [f"PETAL {p['id']} [{p['position']}] {p['angle']}", f"  Angle: {p['focus']}"]
        for s in p["slots"]:
            label = f"{p['id']}.{s['slot']}"
            if s["prompt"]:
                lines.append(f"  {label:<5} {s['operation']}: {s['prompt']}")
            else:
                lines.append(f"  {label:<5} ____________________________________________")
        lines.append("")
    lines += [
        "After the board: prune → score → harvest top 5 → give each one probe.",
    ]
    return "\n".join(lines)


def board_output(theme: str, petals: list[dict]) -> str:
    lines = ["CENTER — theme and its eight petals", ""]
    center_slots = [{"prompt": p["angle"]} for p in petals]
    center_slots += [{"prompt": ""} for _ in range(8 - len(center_slots))]
    lines += render_block(theme, center_slots)
    lines.append("")
    for p in petals:
        lines += [f"PETAL {p['id']} [{p['position']}] — {p['angle']}", ""]
        lines += render_block(p["angle"], p["slots"])
        lines.append("")
    return "\n".join(lines)


def payload(theme: str, petals: list[dict], seed: int | None, fill: str) -> dict:
    return {
        "method": "lotus-blossom",
        "theme": theme,
        "petal_count": len(petals),
        "seed": seed,
        "fill": fill,
        "derived_capacity": len(petals) + len(petals) * 8,
        "layers": [
            "1: central theme",
            "2: eight petals (angles that partition the theme)",
            "3: eight concrete ideas per petal",
        ],
        "petals": petals,
        "next": [
            "Prune duplicates and infeasible slots; record why each was cut.",
            "Score survivors against 3-5 criteria fixed before generation.",
            "Harvest the top five and give each one probe plus a kill signal.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Lotus Blossom 8x8 radial board generator (offline)"
    )
    parser.add_argument("--theme", help="central theme or question for the board")
    parser.add_argument(
        "--petals", type=int, default=8, help="number of petals, 1-8 (default 8)"
    )
    parser.add_argument(
        "--fill",
        choices=["random", "blank"],
        default="random",
        help="random = seeded operation prompts; blank = empty idea slots",
    )
    parser.add_argument("--seed", type=int, default=None, help="seed for reproducibility")
    parser.add_argument(
        "--export",
        choices=["text", "board", "json"],
        default="text",
        help="output format (default text)",
    )
    parser.add_argument("--json", action="store_true", help="alias for --export json")
    parser.add_argument("--list", action="store_true", help="list angles and operations")
    args = parser.parse_args()

    if args.list:
        print("Petal angles (layer 2):")
        for name, tip in ANGLES:
            print(f"  {name:<12} {tip}")
        print("\nExpansion operations (layer 3):")
        for name, tip in OPERATIONS:
            print(f"  {name:<20} {tip}")
        print("\nAt 8 petals the board holds 8 + 64 = 72 idea slots.")
        return 0

    if not args.theme:
        parser.error("--theme is required (or use --list)")
    if args.petals < 1 or args.petals > 8:
        parser.error("--petals must be between 1 and 8")

    theme = args.theme.strip()
    petals = build_petals(args.petals, args.seed)
    build_slots(petals, args.fill, args.seed)
    capacity = len(petals) + len(petals) * 8

    if args.json or args.export == "json":
        print(json.dumps(payload(theme, petals, args.seed, args.fill), indent=2, ensure_ascii=False))
    elif args.export == "board":
        print(board_output(theme, petals))
    else:
        print(text_output(theme, petals, capacity))
    return 0


if __name__ == "__main__":
    sys.exit(main())
