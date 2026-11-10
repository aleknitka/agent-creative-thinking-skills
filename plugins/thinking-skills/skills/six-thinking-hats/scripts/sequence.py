#!/usr/bin/env python3
"""
sequence.py — offline helper for six-thinking-hats.

Suggests a hat sequence and time-boxes for a given goal and time budget.
No dependencies, no network.

Usage:
  python scripts/sequence.py --goal exploratory --time 20
  python scripts/sequence.py --goal decision --time 30 --json
  python scripts/sequence.py --list
  python scripts/sequence.py --goal "critique keeps interrupting brainstorming" --time 15
"""
from __future__ import annotations

import argparse
import json
import re

HAT_MEANINGS = {
    "white": "Information — what we know / don't know / need",
    "red": "Feelings & intuition — gut reactions, unstated without justification",
    "yellow": "Benefits & value — where it works and under what conditions",
    "black": "Caution & risks — what could go wrong, what to check",
    "green": "Creativity — alternatives, provocations, modifications",
    "blue": "Process control — focus, sequence, synthesis",
}

SEQUENCES = {
    "quick-gut": {
        "label": "Quick gut check",
        "hats": ["blue", "white", "red", "blue"],
        "minutes": 6,
        "fits": "Early reaction before data exists",
        "keywords": {"gut", "quick", "reaction", "feeling", "intuition", "early"},
    },
    "quick-tension": {
        "label": "Quick decision tension",
        "hats": ["blue", "yellow", "black", "blue"],
        "minutes": 10,
        "fits": "You know the facts; need optimism and caution side by side",
        "keywords": {"tension", "decision", "optimism", "caution", "benefits", "risks"},
    },
    "idea-generation": {
        "label": "Idea generation",
        "hats": ["blue", "white", "green", "blue"],
        "minutes": 12,
        "fits": "Problem is clear; need alternatives fast",
        "keywords": {"idea", "generate", "alternatives", "brainstorm", "creative", "stuck"},
    },
    "exploratory": {
        "label": "Exploratory (discover)",
        "hats": ["blue", "white", "red", "green", "blue"],
        "minutes": 18,
        "fits": "Topic is open; map facts, feelings, possibilities",
        "keywords": {"explore", "exploratory", "discover", "open", "possibilities", "map"},
    },
    "full-evaluation": {
        "label": "Full evaluation (choose)",
        "hats": ["blue", "white", "red", "yellow", "black", "green", "blue"],
        "minutes": 30,
        "fits": "Real decision with tradeoffs and need for new options after critique",
        "keywords": {"evaluate", "evaluation", "choose", "tradeoff", "trade-offs", "decide", "decision"},
    },
    "pre-mortem": {
        "label": "Pre-mortem style",
        "hats": ["blue", "white", "black", "green", "yellow", "blue"],
        "minutes": 22,
        "fits": "Stress-test a plan before committing; Green repairs what Black finds",
        "keywords": {"pre-mortem", "premortem", "stress", "test", "fail", "commit", "risk"},
    },
    "retrospective": {
        "label": "Retrospective",
        "hats": ["blue", "white", "red", "black", "yellow", "green", "blue"],
        "minutes": 28,
        "fits": "Look back honestly, then extract what to keep and change",
        "keywords": {"retrospective", "retro", "look back", "review", "post", "mortem"},
    },
}

# Default time-box per hat (minutes), scaled if total time differs
HAT_BUDGETS = {
    "blue": 2.5,  # open+close split; shown as single entry, note in output
    "white": 5,
    "red": 1.5,
    "yellow": 4,
    "black": 5,
    "green": 8,
}


def tokenize(s: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", s.lower()))


def infer_goal(text: str) -> str | None:
    toks = tokenize(text)
    best = None
    best_score = 0
    for key, seq in SEQUENCES.items():
        score = len(seq["keywords"] & toks)
        # aliases
        if "critic" in text.lower() or "interrupt" in text.lower():
            if key in ("quick-tension", "full-evaluation"):
                score += 2
        if "bold" in text.lower() and "vision" in text.lower():
            if key == "exploratory":
                score += 1
        if "scenarios" in text.lower() or "stakeholder" in text.lower():
            if key == "exploratory":
                score += 1
        if score > best_score:
            best_score = score
            best = key
    return best if best_score > 0 else None


def scale_budgets(hats: list[str], total_minutes: int | None) -> dict[str, float]:
    # Count blue twice if it appears at both open and close
    counts: dict[str, int] = {}
    for h in hats:
        counts[h] = counts.get(h, 0) + 1
    raw = sum(HAT_BUDGETS[h] * counts[h] for h in counts)
    if total_minutes is None or raw == 0:
        return {h: HAT_BUDGETS[h] for h in hats}
    factor = total_minutes / raw
    return {h: round(HAT_BUDGETS[h] * factor, 1) for h in hats}


def main() -> None:
    p = argparse.ArgumentParser(description="Six Thinking Hats sequence helper (offline)")
    p.add_argument("--goal", type=str, default="", help="goal label or free-text description")
    p.add_argument("--time", type=int, default=None, help="total minutes available")
    p.add_argument("--list", action="store_true", help="list known sequences and exit")
    p.add_argument("--json", action="store_true", help="emit JSON")
    args = p.parse_args()

    if args.list:
        for key, seq in SEQUENCES.items():
            print(f"{key:20s} {seq['hats']}  ~{seq['minutes']} min  — {seq['label']}: {seq['fits']}")
        return

    goal_raw = args.goal.strip()
    # direct key match (case-insensitive, dash/space tolerant)
    norm = re.sub(r"[^a-z0-9]+", "-", goal_raw.lower()).strip("-")
    seq_key = None
    for k in SEQUENCES:
        if norm == k or norm == k.replace("-", " ") or goal_raw.lower() == SEQUENCES[k]["label"].lower():
            seq_key = k
            break
    if not seq_key and goal_raw:
        seq_key = infer_goal(goal_raw)
    if not seq_key:
        # default: exploratory if no signal, full-evaluation if time >= 25
        if args.time and args.time >= 25:
            seq_key = "full-evaluation"
        else:
            seq_key = "exploratory"
        hint = f"(inferred — no strong match for {goal_raw!r}; add --goal exploratory|decision|idea etc.)"
    else:
        hint = ""

    seq = SEQUENCES[seq_key]
    hats = seq["hats"]
    budgets = scale_budgets(hats, args.time)
    total = args.time if args.time else seq["minutes"]

    if args.json:
        print(json.dumps({
            "sequence_key": seq_key,
            "label": seq["label"],
            "hats": hats,
            "hat_meanings": {h: HAT_MEANINGS[h] for h in hats},
            "fits": seq["fits"],
            "total_minutes": total,
            "budgets_minutes": budgets,
            "sources": ["Edward de Bono — Six Thinking Hats (1985)", "This repo: references/sequences.md"],
        }, indent=2, ensure_ascii=False))
        return

    print(f"Sequence: {seq['label']}  ({seq_key})")
    print(f"Goal: {goal_raw or '(not specified)'} {hint}")
    print(f"Fits: {seq['fits']}")
    print(f"Time: ~{total} min total")
    print()
    print("Hats in order:")
    for i, h in enumerate(hats, 1):
        meaning = HAT_MEANINGS[h]
        mins = budgets[h]
        marker = "  ← Blue opens" if i == 1 and h == "blue" else ("  ← Blue closes / synthesis" if i == len(hats) and h == "blue" else "")
        print(f"  {i}. {h.upper():6s}  ~{mins} min  — {meaning}{marker}")
    print()
    print("Rules: one hat at a time; Green = no critique, Black = specific risks with checks, Red = brief subjective.")
    print("Next: run the sequence and close with Blue synthesis (per-hat outputs + tension + one next step).")


if __name__ == "__main__":
    main()
