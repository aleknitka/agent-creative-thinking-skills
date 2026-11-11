#!/usr/bin/env python3
"""
random_entry.py — offline seeded random-entry stimulus picker for lateral-thinking.

Provides the "arising" provocation operator (random word / object / concept)
without calling an LLM or the network. Deterministic with --seed.

Usage:
  python scripts/random_entry.py                       # one random word
  python scripts/random_entry.py --count 5 --seed 42   # five words, reproducible
  python scripts/random_entry.py --seed 7 --problem "onboarding takes too long"
  python scripts/random_entry.py --list                 # show the word bank
  python scripts/random_entry.py --json --count 3       # JSON array for tool use

Word bank is original and short; replace or expand only with MIT-compatible
or public-domain sources (see references/provenance.md).
"""
from __future__ import annotations

import argparse
import json
import random
import sys

WORD_BANK: list[str] = [
    # 48 curated nouns — evocative, concrete, MIT-safe, no external wordlist
    "nose", "telescope", "river", "knot", "compass", "orchard", "lantern",
    "bicycle", "echo", "harbor", "mushroom", "postcard", "mirror", "anchor",
    "comet", "ladder", "thimble", "avalanche", "quilt", "harvest", "desert",
    "carousel", "volcano", "passport", "antenna", "fossil", "whistle",
    "lighthouse", "canyon", "umbrella", "beehive", "cathedral", "turnstile",
    "satellite", "papyrus", "kiln", "coral", "turntable", "archipelago",
    "sundial", "trellis", "obelisk", "ferry", "glacier", "bazaar",
    "periscope", "windmill", "pagoda", "harpsichord",
]

# Clean any accidental leading spaces
WORD_BANK = [w.strip() for w in WORD_BANK]


def pick_words(count: int = 1, seed: int | None = None) -> list[str]:
    rnd = random.Random(seed)
    if count == 1:
        return [rnd.choice(WORD_BANK)]
    # sample without replacement when possible
    if count <= len(WORD_BANK):
        return rnd.sample(WORD_BANK, count)
    # with replacement if asking for more than the bank
    return [rnd.choice(WORD_BANK) for _ in range(count)]


def provocation_for(word: str, problem: str) -> str:
    subject = problem.strip().split()[0] if problem.strip() else "it"
    return f"Po, {subject} is like a {word} — what if it behaved like one?"


def main() -> None:
    p = argparse.ArgumentParser(description="Random-entry stimulus picker (offline, seeded)")
    p.add_argument("--count", type=int, default=1, help="how many words to emit")
    p.add_argument("--seed", type=int, default=None, help="seed for reproducibility")
    p.add_argument("--problem", type=str, default="", help="optional problem phrase to frame a Po")
    p.add_argument("--list", action="store_true", help="print the word bank and exit")
    p.add_argument("--json", action="store_true", help="emit JSON array instead of lines")
    args = p.parse_args()

    if args.list:
        for w in WORD_BANK:
            print(w)
        return

    if args.count < 1:
        print("error: --count must be >= 1", file=sys.stderr)
        sys.exit(2)

    words = pick_words(args.count, args.seed)

    if args.json:
        if args.problem:
            out = [{"word": w, "provocation": provocation_for(w, args.problem)} for w in words]
        else:
            out = words
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return

    for w in words:
        if args.problem:
            print(provocation_for(w, args.problem))
        else:
            print(w)


if __name__ == "__main__":
    main()
