#!/usr/bin/env python3
"""brainwrite.py — offline sheet, timing, and rotation generator for brainwriting.

Generates blank worksheets and the 6-3-5 rotation schedule so a session can
start without designing the paperwork. No network, no dependencies.

Usage:
  python scripts/brainwrite.py --problem "reduce clinic no-shows"
  python scripts/brainwrite.py --mode small --people 4
  python scripts/brainwrite.py --mode async --people 8 --json
  python scripts/brainwrite.py --list-modes

Modes:
  635   6 people, 3 ideas, 5 minutes, 6 rounds (defaults; overridable)
  small pass 1 + pass 2 + one rotation
  solo  three timed passes on one sheet
  async silent generation window, then a build window
"""
from __future__ import annotations

import argparse
import json
import sys
import textwrap
from dataclasses import dataclass, asdict

MODES = ("635", "small", "solo", "async")


@dataclass
class Plan:
    mode: str
    people: int
    ideas: int
    rounds: int
    minutes: int

    @property
    def writing_minutes(self) -> int:
        return self.rounds * self.minutes

    @property
    def slots(self) -> int:
        return self.people * self.ideas * self.rounds

    def rotation(self) -> list[list[int]]:
        """Return rotation[r][person] = sheet owner held in round r (1-indexed)."""
        return [
            [(person - (rnd - 1)) % self.people for person in range(self.people)]
            for rnd in range(1, self.rounds + 1)
        ]


def default_plan(mode: str, people: int | None) -> Plan:
    if mode == "635":
        return Plan(mode, people or 6, 3, 6, 5)
    if mode == "small":
        return Plan(mode, people or 4, 3, 2, 5)
    if mode == "solo":
        return Plan(mode, 1, 3, 3, 7)
    return Plan(mode, people or 6, 3, 1, 0)


def clean(text: str) -> str:
    return " ".join(text.split()).strip()


def sheet(plan: Plan, owner: int, problem: str, width: int = 26) -> str:
    """Render one blank worksheet for the given participant (1-indexed)."""
    lines = [
        f"Problem: {problem}",
        f"Participant: P{owner}",
        "-" * (16 + (width + 3) * plan.ideas),
    ]
    for rnd in range(1, plan.rounds + 1):
        cells = []
        for i in range(1, plan.ideas + 1):
            label = f"{rnd}{chr(96 + i)}"
            cells.append(f"{label}: " + "." * max(4, width - len(label) - 3))
        lines.append(f"R{rnd:<3} | " + " | ".join(cells) + " |")
    if plan.mode == "solo":
        lines += [
            "",
            "Pass 1: breadth. Pass 2: extend your own best entries.",
            "Pass 3: write as a customer, a sceptic, and a budget owner.",
        ]
    return "\n".join(lines)


def schedule(plan: Plan) -> str:
    if plan.mode == "solo":
        return (
            "Solo passes:\n"
            "  1. 10 ideas, 10 minutes, no editing\n"
            "  2. 2 mutations of your 5 most interesting entries, 5 minutes\n"
            "  3. simulated perspectives (customer, sceptic, budget owner), 5 minutes\n"
            "  Then cluster. Do not evaluate before pass 3 completes."
        )
    if plan.mode == "async":
        return (
            "Async protocol:\n"
            "  Brief posted once, with constraints and target; no examples.\n"
            "  Silent generation window: 24-48 h, one column per participant.\n"
            f"  Build window: 24 h; prefix entries 'build on #<id>:'.\n"
            "  Facilitator freezes and exports the board.\n"
            "  Clusters circulated before any discussion."
        )
    lines = ["Rotation (sheet owner each participant holds per round):"]
    header = "  Round | " + " | ".join(f"P{p}" for p in range(1, plan.people + 1))
    lines += [header, "  " + "-" * (len(header) - 2)]
    for rnd, row in enumerate(plan.rotation(), start=1):
        lines.append(
            f"  {rnd:>5} | " + " | ".join(f"S{o + 1}" for o in row)
        )
    lines.append("  Pass sheets clockwise after each timed round.")
    return "\n".join(lines)


def plan_text(plan: Plan, problem: str, sheets: bool) -> str:
    parts = [
        "Brainwriting plan",
        "=" * 60,
        f"Mode:     {plan.mode}",
        f"People:   {plan.people}",
        f"Ideas:    {plan.ideas} per person per round",
        f"Rounds:   {plan.rounds}",
        f"Writing:  {plan.minutes} min per round"
        + (f" ({plan.writing_minutes} min total)" if plan.writing_minutes else ""),
        f"Slots:    {plan.slots} idea slots (capacity, not guaranteed output)",
        "",
        schedule(plan),
    ]
    if sheets and plan.mode not in ("async",):
        for owner in range(1, plan.people + 1):
            parts += ["", f"--- Sheet {owner} ---", sheet(plan, owner, problem)]
    return "\n".join(parts)


def main() -> int:
    p = argparse.ArgumentParser(
        description="Generate brainwriting worksheets, timing, and rotation schedules."
    )
    p.add_argument("--problem", default="(write the prompt here)", help="session prompt")
    p.add_argument("--mode", default="635", choices=MODES, help="session mode")
    p.add_argument("--people", type=int, default=None, help="number of participants")
    p.add_argument("--ideas", type=int, default=None, help="ideas per person per round")
    p.add_argument("--rounds", type=int, default=None, help="number of rounds")
    p.add_argument("--minutes", type=int, default=None, help="minutes per round")
    p.add_argument("--json", action="store_true", help="machine-readable output")
    p.add_argument("--no-sheets", action="store_true", help="plan only, no worksheets")
    p.add_argument("--list-modes", action="store_true", help="describe modes and exit")
    args = p.parse_args()

    if args.list_modes:
        print(
            textwrap.dedent(
                """\
                635   6 people x 3 ideas x 5 min x 6 rounds -> 108 idea slots in ~30 min.
                small Pass 1 (5 ideas), pass 2 (extend own), one rotation; 45-60 min total.
                solo  Three timed passes on one sheet; 30-40 min.
                async Silent generation window, then build window, then freeze.
                """
            ).rstrip()
        )
        return 0

    if args.people is not None and args.people < 1:
        p.error("--people must be at least 1")

    plan = default_plan(args.mode, args.people)
    if args.ideas is not None:
        plan.ideas = max(1, args.ideas)
    if args.rounds is not None:
        plan.rounds = max(1, args.rounds)
    if args.minutes is not None:
        plan.minutes = max(0, args.minutes)
    problem = clean(args.problem) or "(write the prompt here)"

    if args.json:
        payload = asdict(plan)
        payload.update(
            {
                "problem": problem,
                "writing_minutes": plan.writing_minutes,
                "slots": plan.slots,
                "rotation": plan.rotation(),
                "sheets": []
                if args.no_sheets or plan.mode == "async"
                else [sheet(plan, o, problem) for o in range(1, plan.people + 1)],
                "schedule": schedule(plan),
            }
        )
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print(plan_text(plan, problem, sheets=not args.no_sheets))
    return 0


if __name__ == "__main__":
    sys.exit(main())
