#!/usr/bin/env python3
"""
c-k.py — offline helper for C-K Theory.

Concept/Knowledge expansion helper; no network, no deps.

Usage:
  python scripts/c-k.py --list
  python scripts/c-k.py --concept "a product that activates users without any push message"
  python scripts/c-k.py --concept "an X without Y" --knowledge "invite open rate 62%, activation delay data" --json
"""
from __future__ import annotations
import argparse, json

def main():
    p = argparse.ArgumentParser(description="C-K Concept/Knowledge helper (offline)")
    p.add_argument("--concept", type=str, default="", help="initial concept (undecidable proposition)")
    p.add_argument("--knowledge", type=str, default="", help="knowledge pockets or facts to show as K")
    p.add_argument("--list", action="store_true", help="list the four operators and exit")
    p.add_argument("--json", action="store_true", help="emit JSON")
    args = p.parse_args()

    ops = [
        {"key": "C->C", "name": "Partition C", "prompt": "What property, added to this concept, has no precedent in K? Keep one expansive partition per round."},
        {"key": "C->K", "name": "Disjunction", "prompt": "What K pocket would make this concept decidable — or is there a gap?"},
        {"key": "K->C", "name": "Knowledge to concept", "prompt": "Now that we know X, what new concept can we consider?"},
        {"key": "K->K", "name": "Expand K", "prompt": "What must we learn and how, to decide this?"},
    ]

    if args.list:
        if args.json:
            print(json.dumps(ops, indent=2, ensure_ascii=False))
        else:
            for op in ops:
                print(f"{op['key']} — {op['name']}: {op['prompt']}")
        return

    concept = args.concept.strip() or "(no concept — state it as an undecidable proposition: 'a product that ... without ...')"
    knowledge = args.knowledge.strip()

    if args.json:
        print(json.dumps({
            "concept": concept,
            "knowledge_input": knowledge or "(no K yet — list verifiable facts or pockets)",
            "operators": ops,
            "sources": ["https://openalex.org/W2049599278", "https://openalex.org/W4298440840"],
            "provenance": "C-K (Hatchuel/Weil)"
        }, indent=2, ensure_ascii=False))
        return

    print(f"Concept (C0): {concept}")
    if knowledge:
        print(f"Knowledge (K): {knowledge}")
    else:
        print("Knowledge (K): (none yet — list verifiable facts or pockets)")
    print()
    for op in ops:
        print(f"{op['key']} — {op['name']}: {op['prompt']}")
    print("\nNext: partition C (one expansive), mark disjunction C->K, expand K or log learning agenda, then K->C to re-partition.")

if __name__ == "__main__":
    main()
