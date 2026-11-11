#!/usr/bin/env python3
"""
rich_picture.py — offline helper for Rich Picture + CATWOE.

No network, no deps. Emits drawing prompts and CATWOE templates.

Usage:
  python scripts/rich_picture.py --situation "clinic at capacity, missed appointments rise"
  python scripts/rich_picture.py --situation "..." --catwoe --json
"""
from __future__ import annotations
import argparse, json
import textwrap

CATWOE_TEMPLATE = """\
CATWOE:
  C (Customers):   who benefits or is harmed — observable
  A (Actors):      who operates the transformation
  T (Transformation): input -> output as a verb
  W (Worldview):   W = the assumption that makes T meaningful
  O (Owners):      who can stop the system
  E (Environment): external constraints

Root definition: "A system owned by [O], operated by [A], to transform [T] for [C], under worldview W = ..., within constraints [E]."
"""

PICTURE_PROMPTS = [
    "Actors: people and groups with stakes or influence",
    "Structures: organization, hierarchy, boundaries",
    "Processes and flows: what moves and where it stalls",
    "Tensions: mark where worldviews clash",
    "Concerns: thought bubbles for what each actor fears",
]

def main():
    p = argparse.ArgumentParser(description="Rich Picture + CATWOE helper (offline)")
    p.add_argument("--situation", type=str, default="", help="situation of concern in 3-5 sentences")
    p.add_argument("--catwoe", action="store_true", help="emit CATWOE template")
    p.add_argument("--json", action="store_true", help="emit JSON")
    args = p.parse_args()

    situation = args.situation.strip() or "(no situation — state where, who cares, what is stuck)"

    if args.json:
        payload = {
            "situation": situation,
            "rich_picture_prompts": PICTURE_PROMPTS,
            "sources": [
                "https://link.springer.com/chapter/10.1007/978-3-031-01919-7_2",
                "https://www.ifm.eng.cam.ac.uk/research/dstools/soft-systems-methodology",
                "https://www.humanedesign.co/guides/systems-thinking/mapping-and-modelling/catwoe",
            ],
        }
        if args.catwoe:
            payload["catwoe_template"] = CATWOE_TEMPLATE
            payload["root_definition_template"] = "A system owned by [O], operated by [A], to transform [T] for [C], under worldview W = ..., within constraints [E]."
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return

    print(f"Situation: {situation}\n")
    print("Rich picture — draw on one page:")
    for pt in PICTURE_PROMPTS:
        print(f"  - {pt}")
    if args.catwoe:
        print("\n" + CATWOE_TEMPLATE)
        print("Probe after CATWOE: the smallest test of W or of T's feasibility.")

if __name__ == "__main__":
    main()
