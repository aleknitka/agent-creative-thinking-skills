#!/usr/bin/env python3
"""lotus.py — offline helper for lotus-blossom.
Usage:
  python scripts/lotus.py --theme "reduce week-1 drop" --petals 8 --seed 7
  python scripts/lotus.py --theme "onboarding" --export board --json
"""
import argparse, json, random, textwrap
PETALS_DEFAULT = ["intent on invite","timing of nudge","in-app demo","peer proof","progress kept","single field entry","offline-first","concierge fallback"]
BLOOM_STEMS = ["without", "via", "as", "from", "with", "after", "before", "during", "through", "inside"]

def blooms_for_petal(petal, idx, seed):
    rng = random.Random(f"{seed}-{idx}")
    out = []
    for j in range(8):
        stem = rng.choice(BLOOM_STEMS)
        out.append(f"{petal} {stem} idea {idx}-{j+1}")
    return out

def main():
    p = argparse.ArgumentParser(description="Lotus Blossom generator")
    p.add_argument("--theme", required=True, help="centre theme")
    p.add_argument("--petals", nargs="*", default=None, help="8 petal labels (or default)")
    p.add_argument("--seed", type=int, default=7)
    p.add_argument("--json", action="store_true")
    p.add_argument("--export", choices=["json","board"], default="json")
    args = p.parse_args()
    petals = args.petals if args.petals and len(args.petals)==8 else PETALS_DEFAULT
    blooms = {pet: blooms_for_petal(pet, i, args.seed) for i, pet in enumerate(petals)}
    total = 1 + 8 + sum(len(v) for v in blooms.values())
    data = {"centre": args.theme, "petals": petals, "blooms": blooms, "total_cells": total, "descendants": total-1}
    if args.json or args.export=="json":
        print(json.dumps(data, indent=2))
    else:
        print(f"Centre: {args.theme}")
        for i, pet in enumerate(petals):
            print(f"\nP{i+1}: {pet}")
            for b in blooms[pet]:
                print(f"  - {b}")
if __name__ == "__main__":
    main()
