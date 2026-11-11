#!/usr/bin/env python3
"""ls.py — offline helper for liberating-structures.

Usage:
  python scripts/ls.py --list
  python scripts/ls.py --structure "1-2-4-All"
  python scripts/ls.py --structure TRIZ --json
"""
import argparse, json, random, textwrap
STRUCTURES = {
    "1-2-4-All": {"purpose": "equal-voice generation", "timing": "12 min (1-2-4-8)", "steps": ["1 min silent (1)", "2 min pairs (2)", "4 min fours (4)", "5 min harvest"]},
    "Impromptu Networking": {"purpose": "rapid connections", "timing": "15 min (3x5)", "steps": ["3 rounds, new pair each", "Q: challenge + success", "2.5 min each way"]},
    "15% Solutions": {"purpose": "immediate agency", "timing": "15 min", "steps": ["5 min silent list", "5 min small groups add", "5 min harvest 15% moves with owner+by-when"]},
    "TRIZ": {"purpose": "surface must-stop via worst-system design", "timing": "25 min (10-10-5)", "steps": ["10 min list ways to guarantee failure", "10 min check what we actually do", "5 min name first must-stop"]},
    "Wicked Questions": {"purpose": "name paradoxes", "timing": "15 min", "steps": ["pairs write 'How is it that we ... and ...?'", "share", "cluster both/and"]},
    "Ecocycle Planning": {"purpose": "portfolio phase clarity", "timing": "30 min", "steps": ["place items Birth/Maturity/Creative Destruction/Renewal", "name rigidity/poverty traps", "next move per item"]},
}
ALIAS = {k.lower().replace(' ', '').replace('-',''): k for k in STRUCTURES}
ALIAS.update({"triz": "TRIZ", "1234": "1-2-4-All", "1-2-4-all": "1-2-4-All", "ecocycle": "Ecocycle Planning", "wicked": "Wicked Questions", "15%": "15% Solutions", "impromptu": "Impromptu Networking"})

def main():
    p = argparse.ArgumentParser(description="Liberating Structures picker")
    p.add_argument("--list", action="store_true", help="list structures")
    p.add_argument("--structure", help="structure name")
    p.add_argument("--json", action="store_true")
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("--random", action="store_true", help="pick random structure")
    args = p.parse_args()
    if args.list or (not args.structure and not args.random):
        data = [{"name": k, **v} for k, v in STRUCTURES.items()]
        if args.json:
            print(json.dumps(data, indent=2))
        else:
            for k, v in STRUCTURES.items():
                print(f"{k:22s} {v['timing']:16s} {v['purpose']}")
        return
    if args.random:
        rng = random.Random(args.seed)
        name = rng.choice(list(STRUCTURES.keys()))
    else:
        key = args.structure.strip().lower().replace(' ', '').replace('-','')
        name = ALIAS.get(key) or ALIAS.get(args.structure.strip().lower()) or args.structure
        if name not in STRUCTURES:
            # fuzzy
            for k in STRUCTURES:
                if key in k.lower().replace(' ','').replace('-',''):
                    name = k; break
    info = STRUCTURES.get(name)
    if not info:
        print(f"Unknown structure: {name}. Try --list"); return
    if args.json:
        print(json.dumps({"name": name, **info}, indent=2))
    else:
        print(f"{name} — {info['purpose']} ({info['timing']})")
        for i, s in enumerate(info['steps'], 1):
            print(f"  {i}. {s}")
if __name__ == "__main__":
    main()
