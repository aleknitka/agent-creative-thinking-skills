#!/usr/bin/env python3
"""
bodystorm.py — offline helper for Bodystorming (enactment).

No network, no deps. Emits scene templates and capture prompts.

Usage:
  python scripts/bodystorm.py --scene "clinic check-in for routine visit" --roles "new patient, front-desk, clinician"
  python scripts/bodystorm.py --scene "..." --json
"""
from __future__ import annotations
import argparse, json

def main():
    p = argparse.ArgumentParser(description="Bodystorming enactment helper (offline)")
    p.add_argument("--scene", type=str, default="", help="moment to enact (3-5 sentences: before/during/after)")
    p.add_argument("--roles", type=str, default="", help="comma-separated roles, e.g. 'user, staff, bystander'")
    p.add_argument("--json", action="store_true", help="emit JSON")
    args = p.parse_args()

    scene = args.scene.strip() or "(no scene — state before/during/after and what success looks like)"
    roles = [r.strip() for r in args.roles.split(",") if r.strip()] if args.roles else ["user", "staff", "bystander"]

    payload = {
        "scene": scene,
        "roles": roles,
        "variants": ["nominal (expected path)", "stressed (rushed/low-access/poor info)", "edge (confused/non-standard)"],
        "capture": "Record moment + role + observed friction (hesitate, collide, wait, improvise, recover) before interpreting.",
        "clusters": ["threshold", "handoff", "waiting", "recovery"],
        "sources": ["https://arxiv.org/abs/1308.4978", "https://itk.mitre.org/toolkit-tools/bodystorming/"],
        "provenance": "Bodystorming (enacted ideation); Wang et al. 1308.4978 walking-vs-room pilot",
    }

    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return

    print(f"Scene: {scene}")
    print(f"Roles: {', '.join(roles)}")
    print("Variants: nominal, stressed (rushed/low-access), edge (confused)")
    print("Capture before interpreting; cluster by threshold/handoff/waiting/recovery.")

if __name__ == "__main__":
    main()
