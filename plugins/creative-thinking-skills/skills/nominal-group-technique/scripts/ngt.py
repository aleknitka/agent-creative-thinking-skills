#!/usr/bin/env python3
"""ngt.py — offline NGT/Delphi planner and deterministic tally dry run.

Loads an idea list (or synthesises placeholders) and generates seeded ballots
so a facilitator can rehearse the aggregation rules, output format, and dissent
record before the real session. Every ballot is synthetic: this is a rehearsal
tool, not evidence about the ideas.

Methods:
  ranked  each voter ranks the ideas; top five score 5-4-3-2-1
  n3      each voter gets max(3, min(12, ceil(N/3))) dots, max 3 per idea
  delphi  1-5 ratings over anonymous rounds, summarised by median and IQR

Usage:
  python scripts/ngt.py --ideas ideas.txt --voters 7 --method ranked --seed 7
  python scripts/ngt.py --count 12 --voters 7 --method n3
  python scripts/ngt.py --count 12 --voters 9 --method delphi --rounds 3
  python scripts/ngt.py --list-methods
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import statistics
import sys
from dataclasses import asdict, dataclass

METHODS = ("ranked", "n3", "delphi")
MAX_DOTS_PER_IDEA = 3
RANK_POINTS = (5, 4, 3, 2, 1)
DELPHI_SCALE = (1, 5)
DEFAULT_CONSENSUS = 70.0


@dataclass
class Idea:
    id: str
    text: str


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def latent(text: str) -> float:
    """Stable 1-5 quality-like value derived from the idea text.

    Used only to make synthetic ballots non-uniform and reproducible across
    Python runs (unlike hash()). It carries no meaning about the real idea.
    """
    digest = hashlib.sha256(text.encode("utf-8")).digest()
    return 1.0 + 4.0 * int.from_bytes(digest[:8], "big") / 2**64


def quantile(values: list[int], q: float) -> float:
    """Linear-interpolated quantile; safe for small samples."""
    ordered = sorted(values)
    if len(ordered) == 1:
        return float(ordered[0])
    pos = (len(ordered) - 1) * q
    low, high = math.floor(pos), math.ceil(pos)
    if low == high:
        return float(ordered[low])
    return ordered[low] + (ordered[high] - ordered[low]) * (pos - low)


def describe(vals: list[int], consensus_band: float = 1.0) -> dict:
    med = statistics.median(vals)
    q1, q3 = quantile(vals, 0.25), quantile(vals, 0.75)
    within = sum(1 for v in vals if abs(v - med) <= consensus_band)
    return {
        "median": round(float(med), 1),
        "q1": round(q1, 1),
        "q3": round(q3, 1),
        "iqr": round(q3 - q1, 1),
        "spread": max(vals) - min(vals),
        "high": sum(1 for v in vals if v >= 4),
        "low": sum(1 for v in vals if v <= 2),
        "consensus_pct": round(100.0 * within / len(vals), 1),
    }


# --------------------------------------------------------------------------- #
# Ballot generation
# --------------------------------------------------------------------------- #


def ranked_ballots(ideas: list[Idea], voters: int, rng: random.Random) -> list[dict]:
    ballots = []
    for voter in range(1, voters + 1):
        jitter = {idea.id: rng.gauss(0.0, 1.1) for idea in ideas}
        order = sorted(
            ideas, key=lambda idea: latent(idea.text) + jitter[idea.id], reverse=True
        )
        points = {idea.id: 0 for idea in ideas}
        for position, idea in enumerate(order[: len(RANK_POINTS)]):
            points[idea.id] = RANK_POINTS[position]
        ballots.append(
            {
                "voter": voter,
                "ranking": [idea.id for idea in order],
                "points": points,
            }
        )
    return ballots


def n3_budget(idea_count: int) -> int:
    return max(3, min(12, math.ceil(idea_count / 3)))


def n3_ballots(
    ideas: list[Idea], voters: int, rng: random.Random
) -> tuple[list[dict], int]:
    budget = n3_budget(len(ideas))
    ballots = []
    for voter in range(1, voters + 1):
        counts = {idea.id: 0 for idea in ideas}
        dots: list[str] = []
        while len(dots) < budget:
            pool = [
                idea
                for idea in ideas
                if counts[idea.id] < MAX_DOTS_PER_IDEA
            ]
            if not pool:
                break
            weights = [latent(idea.text) + 1.0 for idea in pool]
            pick = rng.choices(pool, weights=weights, k=1)[0]
            counts[pick.id] += 1
            dots.append(pick.id)
        ballots.append(
            {"voter": voter, "dots": dots, "by_idea": dict(counts)}
        )
    return ballots, budget


def delphi_rounds(
    ideas: list[Idea], voters: int, rounds: int, rng: random.Random
) -> list[dict]:
    bias = [rng.gauss(0.0, 0.55) for _ in range(voters)]
    previous: dict[str, list[int]] | None = None
    history = []
    for rnd in range(1, rounds + 1):
        scores: dict[str, list[int]] = {}
        for idea in ideas:
            values = []
            base = latent(idea.text)
            for voter in range(voters):
                if previous is None:
                    raw = base + bias[voter] + rng.gauss(0.0, 1.0)
                else:
                    prior = previous[idea.id][voter]
                    group_median = statistics.median(previous[idea.id])
                    noise = rng.gauss(0.0, max(0.3, 1.0 - 0.2 * (rnd - 1)))
                    raw = prior + 0.35 * (group_median - prior) + noise
                values.append(int(clamp(round(raw), *DELPHI_SCALE)))
            scores[idea.id] = values
        summary = {idea.id: describe(scores[idea.id]) for idea in ideas}
        history.append({"round": rnd, "scores": scores, "summary": summary})
        previous = scores
    return history


# --------------------------------------------------------------------------- #
# Tallying
# --------------------------------------------------------------------------- #


def tally_ranked(ideas: list[Idea], ballots: list[dict], top: int) -> dict:
    points = {idea.id: 0 for idea in ideas}
    firsts = {idea.id: 0 for idea in ideas}
    lasts = {idea.id: 0 for idea in ideas}
    for ballot in ballots:
        for idea_id, value in ballot["points"].items():
            points[idea_id] += value
        if ballot["ranking"]:
            firsts[ballot["ranking"][0]] += 1
            lasts[ballot["ranking"][-1]] += 1

    order = sorted(
        ideas, key=lambda idea: (-points[idea.id], -firsts[idea.id], idea.id)
    )
    rows = []
    for rank, idea in enumerate(order, start=1):
        rows.append(
            {
                "rank": rank,
                "id": idea.id,
                "text": idea.text,
                "points": points[idea.id],
                "firsts": firsts[idea.id],
                "lasts": lasts[idea.id],
            }
        )
    selected = rows[:top]
    boundary_tie = (
        len(rows) > top
        and top > 0
        and rows[top - 1]["points"] == rows[top]["points"]
    )

    dissent = []
    outsiders = rows[top:]
    supported = [row for row in outsiders if row["firsts"] > 0]
    if supported:
        runner = max(supported, key=lambda row: (row["points"], row["firsts"]))
        dissent.append(
            f"{runner['id']} missed the cut with {runner['points']} points and "
            f"{runner['firsts']} first-place vote(s); log the minority case."
        )
    reservations = [row for row in selected if row["lasts"] > 0]
    for row in reservations:
        dissent.append(
            f"{row['id']} was ranked last by {row['lasts']} voter(s) despite "
            f"finishing {row['rank']}; record the reservation."
        )
    if boundary_tie:
        dissent.append(
            f"Tie at the cut line between {rows[top - 1]['id']} and "
            f"{rows[top]['id']} on {rows[top]['points']} points; apply the "
            "tie-break agreed before the vote."
        )
    return {
        "rows": rows,
        "top": [row["id"] for row in selected],
        "dissent": dissent,
        "boundary_tie": boundary_tie,
    }


def tally_n3(
    ideas: list[Idea], ballots: list[dict], budget: int, top: int
) -> dict:
    dots = {idea.id: 0 for idea in ideas}
    supporters = {idea.id: 0 for idea in ideas}
    for ballot in ballots:
        for idea_id, value in ballot["by_idea"].items():
            dots[idea_id] += value
            if value:
                supporters[idea_id] += 1

    order = sorted(
        ideas, key=lambda idea: (-dots[idea.id], -supporters[idea.id], idea.id)
    )
    rows = []
    for rank, idea in enumerate(order, start=1):
        rows.append(
            {
                "rank": rank,
                "id": idea.id,
                "text": idea.text,
                "dots": dots[idea.id],
                "voters": supporters[idea.id],
            }
        )
    selected = rows[:top]
    boundary_tie = (
        len(rows) > top
        and top > 0
        and rows[top - 1]["dots"] == rows[top]["dots"]
    )
    dissent = []
    if rows[top:]:
        runner = rows[top]
        if runner["dots"] > 0:
            dissent.append(
                f"{runner['id']} is the closest outsider ({runner['dots']} dots "
                f"from {runner['voters']} voter(s)); check it against the cut line."
            )
    for row in selected:
        if row["voters"] <= max(1, len(ballots) // 3):
            dissent.append(
                f"{row['id']} reached the top {top} on {row['dots']} dots from "
                f"only {row['voters']} voter(s); verify breadth of support."
            )
    if boundary_tie:
        dissent.append(
            f"Tie at the cut line between {rows[top - 1]['id']} and "
            f"{rows[top]['id']}; apply the tie-break agreed before the vote."
        )
    return {
        "rows": rows,
        "top": [row["id"] for row in selected],
        "dissent": dissent,
        "budget": budget,
        "boundary_tie": boundary_tie,
    }


def tally_delphi(
    ideas: list[Idea],
    history: list[dict],
    top: int,
    consensus_target: float,
) -> dict:
    final = history[-1]["summary"]
    first = history[0]["summary"]
    order = sorted(
        ideas,
        key=lambda idea: (
            -final[idea.id]["median"],
            final[idea.id]["iqr"],
            -final[idea.id]["high"],
            idea.id,
        ),
    )
    rows = []
    for rank, idea in enumerate(order, start=1):
        stats = final[idea.id]
        rows.append(
            {
                "rank": rank,
                "id": idea.id,
                "text": idea.text,
                **stats,
                "delta_from_round_1": round(
                    stats["median"] - first[idea.id]["median"], 1
                ),
            }
        )
    selected = rows[:top]
    dissent = []
    for row in selected:
        if row["iqr"] >= 2.0:
            dissent.append(
                f"{row['id']} ranks {row['rank']} but has IQR {row['iqr']}: the "
                "panel is split, so report the disagreement rather than a single score."
            )
        if row["low"] > 0:
            dissent.append(
                f"{row['id']} drew {row['low']} rating(s) of 2 or less; name the "
                "minority objection in the record."
            )
    near_misses = 0
    for row in rows[top:]:
        if row["high"] >= max(2, len(history[0]["scores"][row["id"]]) // 2):
            dissent.append(
                f"{row['id']} missed the cut at median {row['median']} but "
                f"{row['high']} voter(s) rated it 4 or 5; preserve the dissent."
            )
            near_misses += 1
            if near_misses == 2:
                break

    stable = 0
    if len(history) > 1:
        previous = history[-2]["summary"]
        for idea in ideas:
            if final[idea.id]["median"] == previous[idea.id]["median"]:
                stable += 1
    unresolved = [row["id"] for row in rows if row["consensus_pct"] < consensus_target]
    return {
        "rows": rows,
        "top": [row["id"] for row in selected],
        "dissent": dissent,
        "rounds": len(history),
        "stable_medians": stable,
        "unresolved": unresolved,
        "consensus_target": consensus_target,
    }


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #


def truncate(text: str, width: int = 46) -> str:
    clean = " ".join(text.split())
    return clean if len(clean) <= width else clean[: width - 1] + "…"


def render_ranked(result: dict, meta: dict) -> str:
    lines = [
        "NGT/Delphi dry run — ranked vote (5-4-3-2-1 for the top five)",
        f"Ideas: {meta['idea_count']} | Voters: {meta['voters']} | "
        f"Seed: {meta['seed']}",
        "",
        "NOTE: synthetic ballots for rehearsal only — not evidence about the ideas.",
        "",
        f"{'#':>3}  {'ID':<4} {'Points':>6} {'#1':>3} {'#Last':>5}  Idea",
    ]
    for row in result["rows"]:
        lines.append(
            f"{row['rank']:>3}  {row['id']:<4} {row['points']:>6} "
            f"{row['firsts']:>3} {row['lasts']:>5}  {truncate(row['text'])}"
        )
    lines += ["", f"Top {len(result['top'])}: {', '.join(result['top'])}"]
    lines += render_dissent(result)
    return "\n".join(lines)


def render_n3(result: dict, meta: dict) -> str:
    lines = [
        "NGT/Delphi dry run — N/3 dot vote"
        f" (budget {result['budget']} dots per voter, max 3 per idea)",
        f"Ideas: {meta['idea_count']} | Voters: {meta['voters']} | "
        f"Seed: {meta['seed']}",
        "",
        "NOTE: synthetic ballots for rehearsal only — not evidence about the ideas.",
        "",
        f"{'#':>3}  {'ID':<4} {'Dots':>5} {'Voters':>6}  Idea",
    ]
    for row in result["rows"]:
        lines.append(
            f"{row['rank']:>3}  {row['id']:<4} {row['dots']:>5} "
            f"{row['voters']:>6}  {truncate(row['text'])}"
        )
    lines += ["", f"Top {len(result['top'])}: {', '.join(result['top'])}"]
    lines += render_dissent(result)
    return "\n".join(lines)


def render_delphi(
    result: dict, meta: dict, history: list[dict], ideas: list[Idea]
) -> str:
    lines = [
        "NGT/Delphi dry run — Delphi ratings (1-5, median + IQR)",
        f"Ideas: {meta['idea_count']} | Voters: {meta['voters']} | "
        f"Rounds: {result['rounds']} | Seed: {meta['seed']}",
        "",
        "NOTE: synthetic ballots for rehearsal only — not evidence about the ideas.",
        "",
        f"{'#':>3}  {'ID':<4} {'Median':>6} {'IQR':>4} {'Cons.':>6}  Idea",
    ]
    for row in result["rows"]:
        lines.append(
            f"{row['rank']:>3}  {row['id']:<4} {row['median']:>6.1f} "
            f"{row['iqr']:>4.1f} {row['consensus_pct']:>5.0f}%  "
            f"{truncate(row['text'])}"
        )
    if len(history) > 1:
        last = history[-1]["summary"]
        previous = history[-2]["summary"]
        shifts = [
            abs(last[idea.id]["median"] - previous[idea.id]["median"])
            for idea in ideas
        ]
        lines.append(
            f"\nStability: {result['stable_medians']}/{meta['idea_count']} medians "
            f"unchanged in the final round; max shift {max(shifts):.1f}."
        )
    lines.append(
        f"Consensus target: {result['consensus_target']:.0f}% of ratings within "
        f"±1 of the median. Items below target: "
        f"{', '.join(result['unresolved']) if result['unresolved'] else 'none'}."
    )
    lines += ["", f"Top {len(result['top'])}: {', '.join(result['top'])}"]
    lines += render_dissent(result)
    return "\n".join(lines)


def render_dissent(result: dict) -> list[str]:
    lines = ["", "Dissent and close calls (record them, do not suppress them):"]
    if result["dissent"]:
        lines += [f"- {item}" for item in result["dissent"]]
    else:
        lines.append(
            "- None detected by the tally. Confirm in the room that silence is "
            "not suppressed disagreement."
        )
    return lines


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def load_ideas(path: str, count: int | None) -> list[Idea]:
    if path:
        with open(path, encoding="utf-8") as handle:
            lines = [line.strip() for line in handle.read().splitlines() if line.strip()]
    else:
        total = count or 12
        lines = [
            f"Placeholder idea {index} — replace with a real option"
            for index in range(1, total + 1)
        ]
    if len(lines) < 2:
        raise ValueError("need at least 2 ideas to rank")
    return [Idea(id=f"I{index}", text=text) for index, text in enumerate(lines, 1)]


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Plan an NGT/Delphi ranking and run a deterministic synthetic tally. "
            "Use --ideas for a real export or --count for placeholder ideas."
        )
    )
    parser.add_argument("--ideas", help="UTF-8 file with one idea per line")
    parser.add_argument(
        "--count",
        type=int,
        help="number of placeholder ideas when --ideas is omitted (default 12)",
    )
    parser.add_argument("--voters", type=int, default=7, help="number of ballots")
    parser.add_argument(
        "--method", choices=METHODS, default="ranked", help="aggregation method"
    )
    parser.add_argument(
        "--rounds",
        type=int,
        default=None,
        help="Delphi rounds (default 3 for delphi, 1 otherwise)",
    )
    parser.add_argument("--seed", type=int, default=42, help="deterministic seed")
    parser.add_argument(
        "--top", type=int, default=3, help="size of the shortlist (default 3)"
    )
    parser.add_argument(
        "--consensus",
        type=float,
        default=DEFAULT_CONSENSUS,
        help="Delphi consensus target as percent within +/-1 of median (default 70)",
    )
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument(
        "--list",
        "--list-methods",
        dest="list_methods",
        action="store_true",
        help="describe methods and exit",
    )
    args = parser.parse_args()

    if args.list_methods:
        print(
            "ranked  Each voter ranks every idea; the top five score 5-4-3-2-1. "
            "Best for 8-20 items.\n"
            "n3      Each voter gets max(3, min(12, ceil(N/3))) dots, at most 3 "
            "per idea. Fast, visible, tolerates more items.\n"
            "delphi  1-5 ratings across anonymous rounds; report median, IQR, and "
            "the share within +/-1 of the median. Use when voters are dispersed."
        )
        return 0

    if args.ideas and args.count is not None:
        parser.error("use either --ideas or --count, not both")
    if args.voters < 2:
        parser.error("--voters must be at least 2")
    if args.top < 1:
        parser.error("--top must be at least 1")
    if args.count is not None and args.count < 2:
        parser.error("--count must be at least 2")
    if args.rounds is not None and args.rounds < 1:
        parser.error("--rounds must be at least 1")
    if args.method != "delphi" and args.rounds not in (None, 1):
        parser.error("--rounds applies to --method delphi; NGT votes once")
    if not 0 <= args.consensus <= 100:
        parser.error("--consensus must be between 0 and 100")

    try:
        ideas = load_ideas(args.ideas, args.count)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    rounds = args.rounds if args.rounds is not None else (3 if args.method == "delphi" else 1)
    if args.method == "delphi" and rounds < 2:
        parser.error("Delphi needs at least 2 rounds to provide feedback")

    rng = random.Random(args.seed)
    payload: dict = {
        "method": args.method,
        "seed": args.seed,
        "voters": args.voters,
        "rounds": rounds,
        "idea_count": len(ideas),
        "ideas": [asdict(idea) for idea in ideas],
    }

    if args.method == "ranked":
        ballots = ranked_ballots(ideas, args.voters, rng)
        result = tally_ranked(ideas, ballots, args.top)
        payload.update(ballots=ballots, ranking=result["rows"], top=result["top"],
                       dissent=result["dissent"], boundary_tie=result["boundary_tie"])
        text = render_ranked(result, payload)
    elif args.method == "n3":
        ballots, budget = n3_ballots(ideas, args.voters, rng)
        result = tally_n3(ideas, ballots, budget, args.top)
        payload.update(ballots=ballots, budget=budget, ranking=result["rows"],
                       top=result["top"], dissent=result["dissent"],
                       boundary_tie=result["boundary_tie"])
        text = render_n3(result, payload)
    else:
        history = delphi_rounds(ideas, args.voters, rounds, rng)
        result = tally_delphi(ideas, history, args.top, args.consensus)
        payload.update(
            rounds=len(history),
            history=history,
            ranking=result["rows"],
            top=result["top"],
            dissent=result["dissent"],
            stable_medians=result["stable_medians"],
            unresolved=result["unresolved"],
            consensus_target=args.consensus,
        )
        text = render_delphi(result, payload, history, ideas)

    print(json.dumps(payload, indent=2, ensure_ascii=False) if args.json else text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
