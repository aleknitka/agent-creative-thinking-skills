#!/usr/bin/env python3
"""{slug} helper — offline."""
import argparse, json
def main():
    p = argparse.ArgumentParser(description="forced-connections helper (offline)")
    p.add_argument("--input", type=str, default="")
    p.add_argument("--json", action="store_true")
    p.add_argument("--list", action="store_true")
    args = p.parse_args()
    if args.list:
        print("forced-connections: helper for Forced Connections")
        return
    if args.json:
        print(json.dumps({"input": args.input or "(no input)", "method": "forced-connections", "next": "follow the skill process"}, indent=2, ensure_ascii=False))
    else:
        print(f"Input: {args.input or '(no input)'}")
        print("Next: follow the skill process; helper is scaffolding only.")
if __name__ == "__main__": main()
