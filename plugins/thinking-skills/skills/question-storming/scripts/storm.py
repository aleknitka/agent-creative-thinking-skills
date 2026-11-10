#!/usr/bin/env python3
"""storm.py — offline helper for question-storming."""
import argparse, json
STEMS = {
    "clarifying": ["What does X actually mean?", "How would we know X happened?"],
    "reframing": ["Why this problem now?", "What goal is this in service of?"],
    "stakeholder": ["Who is affected and who decides?", "Who pays the cost of this framing?"],
    "constraint": ["What is fixed, by whom, and what if it were not?", "Which deadline is real?"],
    "causal": ["What produces this outcome, and what evidence supports that?", "What correlates but does not cause?"],
    "generative": ["What if ...?", "How might we make this 10x easier?"],
}
def main():
    p = argparse.ArgumentParser(description="Question-storm helper (offline)")
    p.add_argument("--brief", type=str, default="")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    if args.json:
        print(json.dumps({"brief": args.brief or "(no brief)", "categories": STEMS}, indent=2, ensure_ascii=False))
    else:
        print(f"Brief: {args.brief or '(no brief)'}")
        for cat, stems in STEMS.items():
            print(cat + ":")
            for s in stems: print(f"  - {s}")
if __name__ == "__main__": main()
