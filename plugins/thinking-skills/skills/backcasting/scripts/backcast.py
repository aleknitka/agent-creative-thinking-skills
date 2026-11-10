#!/usr/bin/env python3
"""backcast.py — offline helper for backcasting."""
import argparse, json
def main():
    p=argparse.ArgumentParser(description="Backcasting helper (offline)")
    p.add_argument("--future", type=str, default="")
    p.add_argument("--json", action="store_true")
    args=p.parse_args()
    if args.json:
        print(json.dumps({"desired_future": args.future or "(no future)", "steps": "walk backward: what must be true the period before? repeat until today"}, indent=2, ensure_ascii=False))
    else:
        print(f"Future: {args.future or '(no future)'}")
        print("Steps: walk backward — what must be true the period before? Repeat until today.")
if __name__=="__main__": main()
