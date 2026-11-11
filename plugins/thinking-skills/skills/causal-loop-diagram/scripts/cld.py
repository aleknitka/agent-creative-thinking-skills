#!/usr/bin/env python3
"""
cld.py — offline helper for Causal Loop Diagram (feedback).

No network, no deps. Emits structure prompts and leverage checks.

Usage:
  python scripts/cld.py --behavior "activation flat while reminders rise" --horizon "6 months"
  python scripts/cld.py --behavior "..." --json
"""
from __future__ import annotations
import argparse, json
import textwrap

def main():
    p = argparse.ArgumentParser(description="Causal Loop Diagram helper (offline)")
    p.add_argument("--behavior", type=str, default="", help="problematic behavior over time")
    p.add_argument("--horizon", type=str, default="", help="time horizon, e.g. 6 months")
    p.add_argument("--json", action="store_true", help="emit JSON")
    args = p.parse_args()

    behavior = args.behavior.strip() or "(no behavior — state what persists or oscillates)"
    horizon = args.horizon.strip() or "(no horizon — name the time window)"

    prompts = {
        "variables": "List 6–10 quantities that can go up or down (not events).",
        "links": "For each link, state the mechanism and mark polarity +/– and delay ||.",
        "loops": "Close the loops — label R (reinforcing) or B (balancing), count loops, mark delays.",
        "archetypes": "Compare to Shifting the Burden / Fixes that Fail / Limits to Growth / Success to the Successful.",
        "leverage": "Rank by Meadows level 12→1 — numbers lowest, paradigm highest — then probe the top 1–2.",
    }

    payload = {
        "behavior": behavior,
        "horizon": horizon,
        "prompts": prompts,
        "provenance": "CLD (System Dynamics, Forrester; Meadows leverage points)",
        "sources": [
            "https://link.springer.com/chapter/10.1007/978-3-031-01919-7_2",
            "https://www.ifm.eng.cam.ac.uk/research/dstools/soft-systems-methodology",
        ],
    }

    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return

    print(f"Behavior: {behavior}")
    print(f"Horizon: {horizon}")
    print()
    for k, v in prompts.items():
        print(f"- {k}: {v}")
    print("\nNext: name variables, mark +/– and ||, close R/B loops, then choose leverage before the delay.")

if __name__ == "__main__":
    main()
