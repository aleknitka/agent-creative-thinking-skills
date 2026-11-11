#!/usr/bin/env python3
"""vote.py — offline ballot planner and prioritizer for dot-voting-prioritize.

Reads a clustered idea set, computes the N/3 dot budget, tallies provided votes
or simulates a seeded ballot, and optionally adds an Impact–Effort quadrant and
an ICE score. No network, no dependencies.

Idea file format (one per line; blank lines and # comments ignored):

    Guided setup checklist
    CSV import | votes=3 | impact=8 | effort=2 | ease=7 | confidence=8
    Concierge pilot | votes=3 | impact=9 | effort=5 | ease=2 | confidence=7

Fields:
    votes        total dots received (from a real ballot; omit to simulate)
    impact       1-10 (matrix treats >=4 as high on a 1-5 set, >=6 on a 1-10 set)
    effort       1-5, used by --matrix
    ease         1-10, used by --ice
    confidence   1-10, used by --ice

Missing scores are filled with seeded illustrative values and flagged as
synthetic. Use real scores for a real decision.

Usage:
  python scripts/vote.py --list
  python scripts/vote.py --ideas ideas.txt --voters 6
  python scripts/vote.py --ideas ideas.txt --voters 6 --matrix impact-effort
  python scripts/vote.py --ideas ideas.txt --voters 6 --dots 6 --ice --json
  python scripts/vote.py --ideas "A; B; C" --voters 4 --seed 7
"""
from __future__ import annotations

import argparse
import json
import math
import random
import re
import sys
from pathlib import Path

MAX_DOTS = 12
PER_ITEM_CAP = 3
MATRIX_EFFORT_SPLIT = 3  # effort 1-2 low, 3-5 high
DEFAULT_IDEAS = [
    "Guided setup checklist",
    "Invite a teammate during setup",
    "Onboarding progress bar",
    "Pre-filled sample data",
    "Template gallery",
    "Let users skip optional steps",
    "Import existing data from CSV",
    "Interactive product demo",
    "Concierge onboarding for top accounts",
    "SSO setup wizard",
    "90-second video tour",
    "Day-2 email nudge",
    "Personalized path by role",
    "Role presets",
    "In-app chat",
    "Mobile-specific onboarding",
    "Public onboarding API",
    "Gamified badges",
]
FIELD_RE = re.compile(r"^\s*([a-z_]+)\s*=\s*(-?\d+(?:\.\d+)?)\s*$", re.I)


def fail(msg: str) -> "NoReturn":
    print(f"error: {msg}", file=sys.stderr)
    raise SystemExit(2)


def dots_for(count: int) -> int:
    """N/3 rule: one dot per three items, minimum 3, capped at MAX_DOTS."""
    return max(3, min(MAX_DOTS, math.ceil(count / 3)))


def parse_field(text: str) -> tuple[str, float]:
    m = FIELD_RE.match(text)
    if not m:
        fail(f"unrecognized field '{text.strip()}' (expected key=number)")
    return m.group(1).lower(), float(m.group(2))


def load_ideas(source: str) -> list[dict]:
    path = Path(source)
    if path.is_file():
        raw = path.read_text(encoding="utf-8").splitlines()
    else:
        raw = re.split(r"[\n;]", source)
    ideas: list[dict] = []
    seen: dict[str, int] = {}
    for line in raw:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("|")]
        text = parts[0]
        if not text:
            fail("empty idea text before '|'")
        fields: dict[str, float] = {}
        for part in parts[1:]:
            if part:
                key, value = parse_field(part)
                fields[key] = value
        base = text
        seen[base] = seen.get(base, 0) + 1
        if seen[base] > 1:
            text = f"{base} ({seen[base]})"
        ideas.append({"idea": text, **fields})
    if not ideas:
        fail("no ideas found")
    return ideas


def validate(ideas: list[dict], need_effort: bool, need_ice: bool) -> None:
    for n, item in enumerate(ideas, 1):
        for key in ("impact", "ease", "confidence"):
            if key in item and not 1 <= item[key] <= 10:
                fail(f"idea {n}: {key} must be 1-10, got {item[key]:g}")
        if "effort" in item and not 1 <= item["effort"] <= 5:
            fail(f"idea {n}: effort must be 1-5, got {item['effort']:g}")
        if "votes" in item and (item["votes"] < 0 or item["votes"] != int(item["votes"])):
            fail(f"idea {n}: votes must be a non-negative integer")
    if need_effort and not any("effort" in i for i in ideas):
        print("note: no effort values found; using seeded illustrative values", file=sys.stderr)
    if need_ice and not any(k in i for i in ideas for k in ("impact", "ease", "confidence")):
        print("note: no ICE values found; using seeded illustrative values", file=sys.stderr)


def fill_scores(ideas: list[dict], rng: random.Random) -> None:
    """Fill missing matrix/ICE inputs with seeded values, flagged synthetic."""
    for item in ideas:
        item.setdefault("_synthetic", [])
        if "impact" not in item:
            item["impact"] = rng.randint(1, 5)
            item["_synthetic"].append("impact")
        if "effort" not in item:
            item["effort"] = rng.randint(1, 5)
            item["_synthetic"].append("effort")
        if "ease" not in item:
            item["ease"] = rng.randint(1, 10)
            item["_synthetic"].append("ease")
        if "confidence" not in item:
            item["confidence"] = rng.randint(1, 10)
            item["_synthetic"].append("confidence")


def simulate_votes(ideas: list[dict], voters: int, dots: int, rng: random.Random) -> tuple[dict, int]:
    totals = {i: 0 for i in range(len(ideas))}
    spent = 0
    for _ in range(voters):
        counts = [0] * len(ideas)
        affinity = [rng.uniform(0.2, 1.0) for _ in ideas]
        remaining = dots
        while remaining:
            candidates = [i for i in range(len(ideas)) if counts[i] < PER_ITEM_CAP]
            if not candidates:
                break
            choice = rng.choices(candidates, weights=[affinity[i] for i in candidates], k=1)[0]
            counts[choice] += 1
            totals[choice] += 1
            remaining -= 1
            spent += 1
    return totals, spent


def tally(ideas: list[dict], voters: int, dots: int, rng: random.Random) -> tuple[list[int], int, bool]:
    if any("votes" in item for item in ideas):
        return [int(item.get("votes", 0)) for item in ideas], sum(int(i.get("votes", 0)) for i in ideas), False
    totals, spent = simulate_votes(ideas, voters, dots, rng)
    return [totals[i] for i in range(len(ideas))], spent, True


def quadrant(impact: float, effort: float, impact_split: float) -> str:
    high_i = impact >= impact_split
    high_e = effort >= MATRIX_EFFORT_SPLIT
    if high_i and not high_e:
        return "quick win"
    if high_i and high_e:
        return "big bet"
    if not high_i and not high_e:
        return "fill-in"
    return "money pit"


def ice_score(item: dict) -> float:
    return round((item["impact"] + item["confidence"] + item["ease"]) / 3, 1)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Dot-voting + Impact–Effort/ICE prioritizer (offline).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--ideas", default="", help="path to idea file, or inline ';'-separated ideas")
    parser.add_argument("--voters", type=int, default=5, help="number of voters (default 5)")
    parser.add_argument("--dots", default="auto", help="dots per voter: auto (N/3) or an integer")
    parser.add_argument("--matrix", choices=["impact-effort"], help="add Impact–Effort quadrants")
    parser.add_argument("--ice", action="store_true", help="add ICE scores (I+C+E)/3")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    parser.add_argument("--seed", type=int, default=0, help="seed for simulated ballots/scores (default 0)")
    parser.add_argument("--list", action="store_true", help="show the built-in example set and field format")
    args = parser.parse_args()

    if args.list:
        print("Built-in example ideas:")
        for n, text in enumerate(DEFAULT_IDEAS, 1):
            print(f"  {n:2d}. {text}")
        print("\nFile format: idea | votes=3 | impact=8 | effort=2 | ease=7 | confidence=8")
        print("Scores: impact/ease/confidence 1-10, effort 1-5, votes non-negative integer.")
        return 0

    if args.voters < 1:
        fail("--voters must be at least 1")

    ideas = load_ideas(args.ideas) if args.ideas else [
        {"idea": text} for text in DEFAULT_IDEAS
    ]

    if args.dots == "auto":
        dots = dots_for(len(ideas))
    else:
        try:
            dots = int(args.dots)
        except ValueError:
            fail("--dots must be 'auto' or an integer")
        if dots < 1:
            fail("--dots must be at least 1")

    validate(ideas, bool(args.matrix), args.ice)
    rng = random.Random(args.seed)
    votes, spent, simulated = tally(ideas, args.voters, dots, rng)

    for item, count in zip(ideas, votes):
        item["votes"] = count

    if args.matrix:
        fill = random.Random(args.seed + 1)
        for item in ideas:
            item.setdefault("_synthetic", [])
            if "impact" not in item:
                item["impact"] = fill.randint(1, 5)
                item["_synthetic"].append("impact")
            if "effort" not in item:
                item["effort"] = fill.randint(1, 5)
                item["_synthetic"].append("effort")
        max_impact = max(item["impact"] for item in ideas)
        impact_split = 4 if max_impact <= 5 else 6
        for item in ideas:
            item["quadrant"] = quadrant(item["impact"], item["effort"], impact_split)

    if args.ice:
        fill = random.Random(args.seed + 2)
        for item in ideas:
            item.setdefault("_synthetic", [])
            for key in ("impact", "confidence", "ease"):
                if key not in item:
                    item[key] = fill.randint(1, 10)
                    item["_synthetic"].append(key)
        for item in ideas:
            item["ice"] = ice_score(item)
        ice_rank = sorted(ideas, key=lambda x: x["ice"], reverse=True)
        for rank, item in enumerate(ice_rank, 1):
            item["ice_rank"] = rank

    ordered = sorted(
        ideas,
        key=lambda x: (x["votes"], x.get("ice", 0)),
        reverse=True,
    )

    for rank, item in enumerate(ordered, 1):
        item["vote_rank"] = rank

    warnings: list[str] = []
    if simulated:
        warnings.append("votes simulated for planning; use real tallies in a real session")
    if spent < args.voters * dots and simulated:
        warnings.append(
            f"only {spent} of {args.voters * dots} dots allocated "
            f"(per-item cap {PER_ITEM_CAP} reached)"
        )
    if not simulated and spent > args.voters * dots:
        warnings.append(
            f"provided tallies total {spent} dots, above the {args.voters * dots}-dot budget"
        )

    if args.json:
        payload = {
            "ideas": len(ideas),
            "voters": args.voters,
            "dots_per_voter": dots,
            "dots_rule": "max(3, ceil(N/3)) capped at 12",
            "total_dots": args.voters * dots,
            "dots_allocated": spent,
            "votes_simulated": simulated,
            "seed": args.seed,
            "warnings": warnings,
            "results": [
                {
                    "rank": item["vote_rank"],
                    "idea": item["idea"],
                    "votes": item["votes"],
                    **({"impact": item["impact"]} if args.matrix or args.ice else {}),
                    **({"effort": item["effort"], "quadrant": item["quadrant"]} if args.matrix else {}),
                    **(
                        {"confidence": item["confidence"], "ease": item["ease"],
                         "ice": item["ice"], "ice_rank": item["ice_rank"]}
                        if args.ice else {}
                    ),
                    **({"synthetic": sorted(set(item["_synthetic"]))} if item.get("_synthetic") else {}),
                }
                for item in ordered
            ],
        }
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return 0

    print(f"Ideas: {len(ideas)}   Voters: {args.voters}   "
          f"Dots/voter: {dots} (N/3 rule)   Total: {args.voters * dots}")
    if simulated:
        print(f"Votes: simulated (seed {args.seed}) — planning only")
    print()
    header = f"{'#':>3}  {'Votes':>5}  {'Idea':<42}"
    if args.matrix:
        header += f"  {'Imp':>3} {'Eff':>3}  {'Quadrant':<10}"
    if args.ice:
        header += f"  {'ICE':>4} {'Rank':>4}"
    print(header)
    print("-" * len(header))
    for item in ordered:
        line = f"{item['vote_rank']:>3}  {item['votes']:>5}  {item['idea'][:42]:<42}"
        if args.matrix:
            line += f"  {item['impact']:>3g} {item['effort']:>3g}  {item['quadrant']:<10}"
        if args.ice:
            line += f"  {item['ice']:>4.1f} {item['ice_rank']:>4}"
        print(line)
    if any(item.get("_synthetic") for item in ideas):
        print("\nSynthetic inputs were used. Replace them with real scores before deciding.")
    for warning in warnings:
        print(f"Note: {warning}")
    print("\nNext: record keep / pivot / kill with reasons and a probe per kept item.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
