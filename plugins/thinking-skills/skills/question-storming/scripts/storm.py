#!/usr/bin/env python3
"""storm.py — offline question-prompt generator for the question-storming skill.

Emits question stems across the six categories so a storm does not collapse
into one kind of question. The prompts are starting points, not a finished
storm: rewrite them against the actual brief, then add your own. No network,
no dependencies.

Usage:
  python scripts/storm.py
  python scripts/storm.py --brief "improve onboarding emails" --count 24
  python scripts/storm.py --category reframing,stakeholder --per-category 6
  python scripts/storm.py --brief "cut cloud spend" --seed 7 --json
  python scripts/storm.py --list
"""
from __future__ import annotations

import argparse
import json
import random
import sys

CATEGORIES: list[tuple[str, list[str]]] = [
    (
        "clarifying",
        [
            "What exactly does each key term in the brief mean here?",
            "What would count as a concrete example of the goal?",
            "What is in scope, and what is explicitly out?",
            "What does success look like in observable terms, and who judges it?",
            "What is the unit, denominator, or baseline for the measure?",
            "Which words in the brief would two stakeholders define differently?",
        ],
    ),
    (
        "reframing",
        [
            "What is the goal above this problem, and why pursue it now?",
            "If this question were answered perfectly, what would change?",
            "Why this question rather than a neighboring one?",
            "What is the opposite question, and when would it be more useful?",
            "Who framed this question, and what did they leave out?",
            "What would make this question unnecessary?",
        ],
    ),
    (
        "stakeholder",
        [
            "Who is affected, and who has actually been asked?",
            "Who decides, who pays, and who does the work?",
            "Whose definition of the problem currently wins, and why?",
            "Who benefits if the current situation continues?",
            "Which user or group is assumed but never named?",
            "What would the least powerful affected person say the problem is?",
        ],
    ),
    (
        "constraint",
        [
            "What is fixed, and who has the authority to fix it?",
            "Which constraints are physics, which are policy, and which are habit?",
            "What would we do with twice the budget or half the time?",
            "Which constraint was imposed without a recorded reason?",
            "Who bears the cost of satisfying this constraint?",
            "What would have to be true for the constraint to disappear?",
        ],
    ),
    (
        "causal",
        [
            "What is the evidence that this is a problem, and how was it collected?",
            "What mechanism would produce this outcome?",
            "When did it start, and what changed around then?",
            "Where does it happen most, and where does it not happen at all?",
            "What would we expect to see if the proposed cause were true?",
            "What else could produce the same observation?",
        ],
    ),
    (
        "generative",
        [
            "What if the main constraint did not exist?",
            "How might we reach the goal with no new tooling?",
            "What would make this easy rather than merely possible?",
            "What is the simplest version that would teach us something?",
            "Who has solved an analogous problem, and what did they assume?",
            "What if we did nothing?",
        ],
    ),
]


def fail(msg: str) -> "NoReturn":
    print(f"error: {msg}", file=sys.stderr)
    raise SystemExit(2)


def select(
    pools: dict[str, list[str]], names: list[str], count: int
) -> list[tuple[str, str]]:
    """Round-robin across categories so a small count keeps coverage."""
    selected: list[tuple[str, str]] = []
    round_no = 0
    while len(selected) < count:
        added = False
        for name in names:
            pool = pools[name]
            if round_no < len(pool):
                selected.append((name, pool[round_no]))
                added = True
                if len(selected) == count:
                    break
        if not added:
            break
        round_no += 1
    return selected


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Emit question prompts for a question-storming pass."
    )
    parser.add_argument("--brief", default="", help="the brief to keep in view")
    parser.add_argument(
        "--count", type=int, default=24, help="total questions to emit (default 24)"
    )
    parser.add_argument(
        "--per-category",
        type=int,
        default=None,
        help="emit this many per category instead of --count",
    )
    parser.add_argument(
        "--category",
        default="",
        help="comma-separated subset of categories (default: all)",
    )
    parser.add_argument("--seed", type=int, default=None, help="shuffle stems")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument("--list", action="store_true", help="list categories and exit")
    args = parser.parse_args()

    if args.list:
        for name, stems in CATEGORIES:
            print(f"{name} ({len(stems)} prompts)")
        return 0

    known = [name for name, _ in CATEGORIES]
    if args.category:
        names = [c.strip().casefold() for c in args.category.split(",") if c.strip()]
        unknown = [c for c in names if c not in known]
        if unknown:
            fail(f"unknown category: {', '.join(unknown)} (known: {', '.join(known)})")
        if not names:
            fail("--category was empty")
    else:
        names = known

    if args.per_category is not None:
        if args.per_category < 1:
            fail("--per-category must be at least 1")
        count = args.per_category * len(names)
    else:
        if args.count < 1:
            fail("--count must be at least 1")
        count = args.count

    rng = random.Random(args.seed) if args.seed is not None else None
    pools: dict[str, list[str]] = {}
    for name, stems in CATEGORIES:
        pool = list(stems)
        if rng is not None:
            rng.shuffle(pool)
        if args.per_category is not None:
            pool = pool[: args.per_category]
        pools[name] = pool

    selected = select(pools, names, count)
    if not selected:
        fail("no prompts selected")

    if args.json:
        payload = {
            "brief": args.brief or None,
            "questions": [
                {"category": category, "question": question}
                for category, question in selected
            ],
        }
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return 0

    if args.brief:
        print(f"Brief: {args.brief}")
        print()
    for name in names:
        questions = [q for category, q in selected if category == name]
        if not questions:
            continue
        print(f"{name.upper()}")
        for question in questions:
            print(f"- {question}")
        print()
    print(
        f"{len(selected)} prompts. Rewrite against the brief and add your own; "
        "generate before judging."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
