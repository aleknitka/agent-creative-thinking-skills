#!/usr/bin/env python3
"""ngt.py — offline helper for nominal-group-technique.
Usage:
  python scripts/ngt.py --list --json
  python scripts/ngt.py --ideas ideas.txt --voters 6 --method ranked --json
  python scripts/ngt.py --count 12 --voters 5 --method n3 --seed 7
"""
import argparse, json, random, pathlib, textwrap, re
METHODS = ["ranked", "n3", "delphi"]
SAMPLE = ["intent on invite","delay email 24h","inline demo","remove tutorial","SMS fallback","add progress bar","one-click setup","in-app checklist","peer artifact","pre-config entry","timed nudge","concierge offer"]

def tally(ideas, voters, method, seed):
    rng = random.Random(seed)
    votes = {idea: 0 for idea in ideas}
    if method == "ranked":
        # each voter ranks 5: 5-4-3-2-1
        for _ in range(voters):
            ranked = rng.sample(ideas, min(5, len(ideas)))
            for idx, idea in enumerate(ranked):
                votes[idea] += 5 - idx
    elif method == "n3":
        dots = max(1, len(ideas)//3)
        for _ in range(voters):
            picks = rng.sample(ideas, min(dots, len(ideas)))
            for idea in picks:
                votes[idea] += 1
    elif method == "delphi":
        # simulate 2 rounds median shift
        for _ in range(voters):
            for idea in rng.sample(ideas, len(ideas)):
                votes[idea] += rng.randint(1,5)
    ranked = sorted(votes.items(), key=lambda x: -x[1])
    return ranked, votes

def main():
    p = argparse.ArgumentParser(description="NGT/Delphi ranking helper")
    p.add_argument("--ideas", help="file with one idea per line")
    p.add_argument("--count", type=int, default=None, help="use sample ideas")
    p.add_argument("--voters", type=int, default=5)
    p.add_argument("--method", choices=METHODS, default="ranked")
    p.add_argument("--rounds", type=int, default=2, help="delphi rounds (informational)")
    p.add_argument("--seed", type=int, default=7)
    p.add_argument("--json", action="store_true")
    p.add_argument("--list", action="store_true", help="list methods")
    args = p.parse_args()
    if args.list:
        print(json.dumps([{"method": m, "desc": d} for m, d in zip(METHODS, ["5-4-3-2-1 ranked", "N/3 dots", "Delphi median/IQR"] )], indent=2) if args.json else "\n".join(METHODS))
        return
    if args.ideas:
        ideas = [l.strip() for l in pathlib.Path(args.ideas).read_text().splitlines() if l.strip()]
    else:
        n = args.count or 12
        ideas = SAMPLE[:n] if n <= len(SAMPLE) else SAMPLE + [f"idea {i}" for i in range(len(SAMPLE)+1, n+1)]
    ranked, votes = tally(ideas, args.voters, args.method, args.seed)
    if args.json:
        print(json.dumps({"method": args.method, "voters": args.voters, "ranked": [{"idea": k, "score": v} for k, v in ranked], "dissent": "recorded separately"}, indent=2))
    else:
        for i, (idea, sc) in enumerate(ranked, 1):
            print(f"{i:2d}. {sc:3d}  {idea}")
        print(f"\nmethod={args.method} voters={args.voters} seed={args.seed}")
        print("Log dissent: who disagrees and why — handoff to portfolio/premortem.")
if __name__ == "__main__":
    main()
