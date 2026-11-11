#!/usr/bin/env python3
"""gameify.py — offline helper for board-game-abstraction.

Turns a problem statement into a suggested board-game abstraction.
No network, no dependencies, no third-party content.

Usage:
  python scripts/gameify.py --problem "onboarding drops 32% before first value"
  python scripts/gameify.py --problem "capacity bottleneck" --mechanic push-your-luck --seed 7
  python scripts/gameify.py --problem "capacity" --mechanic worker-placement --json
  python scripts/gameify.py --list
"""
from __future__ import annotations

import argparse
import json
import random
import re
import sys
import textwrap

MECHANICS: list[dict] = [
    {"slug": "worker-placement", "name": "Worker Placement", "pressure": "queue / contention / queue-jumping", "reveal": "where contention is real vs imagined", "hint": ["queue", "contention", "blocking", "slot", "capacity", "bottleneck", "waiting"]},
    {"slug": "resource-management", "name": "Resource Management", "pressure": "shared scarce budget / capacity", "reveal": "which scarcity drives behavior", "hint": ["budget", "resource", "capacity", "scarce", "tradeoff", "allocation"]},
    {"slug": "push-your-luck", "name": "Push-Your-Luck", "pressure": "repeated small risk / drift", "reveal": "where risk accumulates invisibly", "hint": ["risk", "drift", "repeated", "gamble", "chance", "luck", "retry", "stall"]},
    {"slug": "co-op-hidden-info", "name": "Co-op with Hidden Info", "pressure": "silos vs commons", "reveal": "what silos cost when stakes are shared", "hint": ["silo", "commons", "hidden", "coordination", "cooperate", "silos", "information"]},
    {"slug": "deck-building", "name": "Deck-Building", "pressure": "competence snowballs", "reveal": "how advantage compounds", "hint": ["snowball", "advantage", "competence", "learning", "compounds"]},
    {"slug": "track-race", "name": "Track Race", "pressure": "threshold / activation", "reveal": "where activation stalls", "hint": ["activation", "threshold", "track", "onboarding", "progress", "race", "drop"]},
    {"slug": "trading-auction", "name": "Trading / Auction", "pressure": "negotiation / deal-making", "reveal": "what each side actually values", "hint": ["negotiation", "deal", "auction", "trading", "value", "price"]},
    {"slug": "event-deck", "name": "Event Deck", "pressure": "shock / volatility", "reveal": "how robust the loop is to shocks", "hint": ["shock", "volatility", "event", "random", "volatile", "uncertainty"]},
]

BOARDS = ["Queue", "Track", "Map", "Market"]
RESOURCES = ["Intent", "Attention", "Capacity", "Trust", "Budget", "Slots", "Time", "Tokens"]
PLAYERS = ["Newcomer", "Helper", "Gatekeeper", "System"]

def pick_mechanic(problem: str, seed: int | None) -> dict:
    toks = set(re.findall(r"[a-z0-9]+", problem.lower()))
    best = None
    best_score = -1
    for m in MECHANICS:
        hints = set(m["hint"])
        score = len(toks & set(h.lower() for h in m["hint"])) + (1 if m["slug"] in toks else 0)
        # small tie-break via seed
        if score > best_score:
            best_score = score
            best = m
    if best_score == 0:
        rng = random.Random(seed)
        return rng.choice(MECHANICS)
    return best

def suggest(problem: str, mechanic_slug: str | None, seed: int | None) -> dict:
    rng = random.Random(seed)
    if mechanic_slug and mechanic_slug not in ("auto", "random"):
        mech = next((m for m in MECHANICS if m["slug"] == mechanic_slug), None)
        if not mech:
            # alias
            alias = {"worker": "worker-placement", "push": "push-your-luck", "co-op": "co-op-hidden-info", "co-op-hidden-info": "co-op-hidden-info", "deck": "deck-building", "track": "track-race", "trading": "trading-auction", "event": "event-deck"}
            mech = next((m for m in MECHANICS if m["slug"] == alias.get(mechanic_slug, "")), None)
        if not mech:
            print(f"Unknown mechanic '{mechanic_slug}'. Try --list", file=sys.stderr)
            sys.exit(2)
    else:
        mech = pick_mechanic(problem, seed)
    board = rng.choice(BOARDS)
    resources = rng.sample(RESOURCES, 3)
    players = rng.sample(PLAYERS, k=rng.randint(2, 4))
    # tailor small suggestions by mechanic
    if mech["slug"] == "track-race":
        board = "Track"
    elif mech["slug"] == "worker-placement":
        board = "Queue"
    elif mech["slug"] == "co-op-hidden-info":
        resources = ["Trust", "Capacity", "Information"]
    return {
        "problem": problem,
        "mechanic": {"slug": mech["slug"], "name": mech["name"], "pressure": mech["pressure"], "reveals": mech["reveal"]},
        "abstraction": {
            "players": players,
            "resources": resources,
            "board": board,
            "loop": "More pressure without relief → less resource → more pressure (R with delay ||)",
            "win": "Reach end of track / fill board in <=12 turns",
            "loss": "Stall x3 or resource 0",
        },
        "one_page_rules": [
            "Setup: place all tokens at start; shuffle problem-specific deck.",
            "Turn: spend 1 resource to act — Invite/Act/Rest (rename to your domain).",
            "Cost: each Act without the scarce resource risks a stall (push-your-luck).",
            "Bust: 3 consecutive stalls → lose 1 progress / lose resource.",
            "Win/Loss as above — both must be reachable.",
        ],
        "playtest": ["honest play (balanced)", "greedy (exploit best action)", "co-op (help action converts)"],
        "transfer_prompt": "For each divergence, write: what this mechanic teaches about the real system (label fact/assumption/speculation) and the probe that would test it.",
        "seed": seed,
    }

def main() -> int:
    p = argparse.ArgumentParser(description="Board-game abstraction helper")
    p.add_argument("--problem", help="problem statement to abstract")
    p.add_argument("--mechanic", default=None, help="mechanic slug or auto/random")
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("--json", action="store_true", help="emit JSON")
    p.add_argument("--list", action="store_true", help="list mechanics")
    args = p.parse_args()
    if args.list:
        data = [{"slug": m["slug"], "name": m["name"], "pressure": m["pressure"], "reveals": m["reveal"]} for m in MECHANICS]
        if args.json:
            print(json.dumps(data, indent=2))
        else:
            for m in MECHANICS:
                print(f"{m['slug']:20s} {m['name']:25s} pressure: {m['pressure']:30s} reveals: {m['reveal']}")
        return 0
    if not args.problem:
        p.print_help()
        print("\nExamples:\n  --problem \"onboarding drops 32% before first value\" --seed 7\n  --problem \"capacity bottleneck\" --mechanic worker-placement --json", file=sys.stderr)
        return 2
    data = suggest(args.problem, args.mechanic, args.seed)
    if args.json:
        print(json.dumps(data, indent=2))
    else:
        print(f"Problem: {data['problem']}")
        print(f"Mechanic: {data['mechanic']['name']} ({data['mechanic']['slug']}) — pressure: {data['mechanic']['pressure']}")
        print(f"Reveals: {data['mechanic']['reveals']}")
        print(f"Players: {', '.join(data['abstraction']['players'])}")
        print(f"Resources: {', '.join(data['abstraction']['resources'])}")
        print(f"Board: {data['abstraction']['board']}  Loop: {data['abstraction']['loop']}")
        print(f"Win: {data['abstraction']['win']}  Loss: {data['abstraction']['loss']}")
        print("Rules:")
        for i, r in enumerate(data['one_page_rules'], 1):
            print(f"  {i}. {r}")
        print("Playtest: " + ", ".join(data['playtest']))
        print(f"Transfer: {data['transfer_prompt']}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
