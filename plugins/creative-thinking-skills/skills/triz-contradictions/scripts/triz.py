#!/usr/bin/env python3
"""triz.py — offline helper for triz-contradictions."""
import argparse, json
PRINCIPLES = ["segmentation","extraction","prior action","feedback","asymmetry","universality"]
def main():
    p=argparse.ArgumentParser(description="TRIZ helper (offline)")
    p.add_argument("--contradiction", type=str, default="")
    p.add_argument("--json", action="store_true")
    args=p.parse_args()
    c = args.contradiction or "improving A worsens B"
    if args.json:
        print(json.dumps({"contradiction": c, "principles": PRINCIPLES, "separations": ["space","time","condition","scale"]}, indent=2, ensure_ascii=False))
    else:
        print(f"Contradiction: {c}")
        print("Principles sample: " + ", ".join(PRINCIPLES))
        print("Separations: space, time, condition, scale")
if __name__=="__main__": main()
