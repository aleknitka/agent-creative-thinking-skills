#!/usr/bin/env python3
"""ideal.py — offline helper for ideal-final-result."""
import argparse, json
def main():
    p = argparse.ArgumentParser(description="Ideal final result helper (offline)")
    p.add_argument("--benefit", type=str, default="")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    benefit = args.benefit or "(no benefit stated)"
    ideal = f"{benefit} — with no added complexity, cost, harm, or effort"
    if args.json:
        print(json.dumps({"benefit": benefit, "ideal": ideal, "next": "name barriers, then generate approximation moves"}, indent=2, ensure_ascii=False))
    else:
        print(f"Benefit: {benefit}")
        print(f"Ideal: {ideal}")
        print("Next: name barriers, then generate approximations scored against the ideal.")
if __name__ == "__main__": main()
