#!/usr/bin/env python3
"""premortem.py — offline failure-scene and worksheet generator for premortem.

The premortem's core move is stating the failure as fact, then asking why it
happened. This helper builds that frame from a few facts so the exercise does
not drift into "what might go wrong?".

Usage:
  python scripts/premortem.py --proposal "guided onboarding launch" \
      --date "May 2027" --success "45% activation within 14 days" \
      --consequence "support volume is up 40% and two design partners have paused"

  python scripts/premortem.py --proposal "ERP migration" --scene   # scene only
  python scripts/premortem.py --list-categories                    # generation prompts
  python scripts/premortem.py --proposal "pricing change" --json   # machine-readable

No network, no dependencies, no third-party content.
"""
from __future__ import annotations

import argparse
import json
import sys
import textwrap

CATEGORIES: list[tuple[str, list[str]]] = [
    (
        "assumption",
        [
            "Which belief, if false, makes the whole plan pointless?",
            "What did we assume about who does what, when, and why?",
            "What would falsify that assumption cheaply?",
        ],
    ),
    (
        "coordination",
        [
            "Which handoff has no owner?",
            "What breaks if one team is late or interprets the interface differently?",
            "Which approval, contract, or data flow is on the critical path?",
        ],
    ),
    (
        "incentive",
        [
            "Who is rewarded for something that conflicts with this plan?",
            "Who bears the cost of failure, and who captures the upside?",
            "Where would a rational person work around the new process?",
        ],
    ),
    (
        "capability",
        [
            "Do we have the skills and capacity to execute at this quality?",
            "Which single person or system is load-bearing?",
            "Can we observe the outcome at the granularity needed to act?",
        ],
    ),
    (
        "external",
        [
            "What outside change would make this obsolete or non-compliant?",
            "Which platform, regulator, or customer can change the rules mid-flight?",
            "Which dependency has no substitute?",
        ],
    ),
]


def clean(text: str) -> str:
    return " ".join(text.split()).strip()


def sentence(text: str) -> str:
    """Clean text and ensure it ends with terminal punctuation."""
    text = clean(text)
    if not text:
        return ""
    if text[-1] not in ".!?":
        text += "."
    return text


def capitalise(text: str) -> str:
    return text[:1].upper() + text[1:] if text else text


def failure_scene(
    proposal: str,
    date: str,
    success: str = "",
    consequence: str = "",
) -> str:
    proposal = clean(proposal) or "The project"
    proposal = proposal.rstrip(".!?")
    date = clean(date) or "six months from now"

    lines = [
        f"It is {date}. {capitalise(proposal)} failed.",
    ]
    if clean(success):
        lines.append(
            f"The success measure — {clean(success).rstrip('.')} — was missed."
        )
    else:
        lines.append("The success measure was missed.")
    if clean(consequence):
        lines.append(capitalise(sentence(consequence)))
    else:
        lines.append("The rollout is paused and the team has been reassigned.")
    return " ".join(lines)


def worksheet(
    proposal: str,
    date: str,
    success: str = "",
    consequence: str = "",
    reasons: int = 10,
) -> str:
    proposal = clean(proposal) or "the project"
    date = clean(date) or "six months from now"
    scene = failure_scene(proposal, date, success, consequence)

    parts: list[str] = [
        "# Premortem worksheet",
        "",
        "## 1. Intake",
        "",
        f"- **Proposal:** {sentence(proposal)}",
        f"- **Failure horizon:** {sentence(date)}",
        f"- **Success measure:** {sentence(success) if clean(success) else '⟨define one before starting⟩'}",
        "- **Commitment:** ⟨who commits what, by when⟩",
        "- **Hard constraints:** ⟨budget, headcount, compliance, dependencies⟩",
        "",
        "Confirm the proposal is concrete enough to fail in a *specific* way.",
        "If not, narrow it before continuing.",
        "",
        "## 2. Declared failure scene",
        "",
        "> " + scene,
        "",
        "State it as fact. Do not soften to \"underperformed\" or debate whether it will fail.",
        "",
        f"## 3. Generate {reasons} plausible reasons independently",
        "",
        "Silent writing first — no discussion, no shared document, no peeking.",
        "Use the categories as prompts; label fact / assumption / speculation.",
        "",
    ]

    for name, prompts in CATEGORIES:
        parts.append(f"**{name.capitalize()}**")
        parts.append("")
        for prompt in prompts:
            parts.append(f"- {prompt}")
        parts.append("")

    parts += [
        f"Target: {reasons} reasons per person, including the impolitic ones.",
        "",
        "## 4. Cluster",
        "",
        "Merge duplicates and group by causal mechanism, not by department.",
        "Give each cluster a one-line causal story.",
        "",
        "| Cluster | Causal story | Raw reasons merged |",
        "|---|---|---|",
        "| | | |",
        "",
        "## 5. Prioritize by likelihood × impact",
        "",
        "Score independently first, then discuss outliers. Keep the top 3–5.",
        "",
        "| Failure reason | Category | L (1–5) | I (1–5) | L×I | Warning signal | Threshold |",
        "|---|---|---|---|---|---|---|",
        "| | | | | | | |",
        "",
        "## 6. Harden",
        "",
        "Every top reason gets a prevention that changes the plan now and a monitor",
        "with a signal, threshold, response, owner, and date. Record accepted risks.",
        "",
        "| Failure reason | Prevention (plan change) | Signal → threshold → response | Owner | By |",
        "|---|---|---|---|---|",
        "| | | | | |",
        "",
        "## Check before closing",
        "",
        "- The failure was asserted, not debated.",
        "- Generation happened before discussion.",
        "- Reasons name mechanisms, not labels.",
        "- At least one decision changed: scope, date, metric, incentive, or instrumentation.",
        "- Every monitor has an owner and a threshold.",
        "- Accepted risks are written down with a review date.",
        "",
    ]
    return "\n".join(parts)


def main() -> None:
    p = argparse.ArgumentParser(
        description="Offline failure-scene and worksheet generator for premortem"
    )
    p.add_argument(
        "--proposal",
        "-p",
        default="the project",
        help="the concrete proposal that is assumed to have failed",
    )
    p.add_argument(
        "--date",
        "-d",
        default="six months from now",
        help="failure horizon, phrased as a date or milestone (e.g. 'May 2027')",
    )
    p.add_argument(
        "--success",
        "-s",
        default="",
        help="the success measure that was missed",
    )
    p.add_argument(
        "--consequence",
        "-c",
        default="",
        help="one or two sentences describing what failure looks like",
    )
    p.add_argument(
        "--reasons",
        "-n",
        type=int,
        default=10,
        help="target number of reasons per person (default 10, minimum 8)",
    )
    p.add_argument(
        "--scene",
        action="store_true",
        help="print only the declared failure scene",
    )
    p.add_argument(
        "--list-categories",
        action="store_true",
        help="print the five failure-mode categories and prompts",
    )
    p.add_argument(
        "--json",
        action="store_true",
        help="emit a JSON object instead of Markdown",
    )
    args = p.parse_args()

    if args.list_categories:
        for name, prompts in CATEGORIES:
            print(f"{name}:")
            for prompt in prompts:
                print(f"  - {prompt}")
        return

    if args.reasons < 8:
        print("error: --reasons must be at least 8", file=sys.stderr)
        sys.exit(2)

    scene = failure_scene(args.proposal, args.date, args.success, args.consequence)

    if args.scene:
        print(scene)
        return

    if args.json:
        out = {
            "proposal": clean(args.proposal),
            "failure_horizon": clean(args.date),
            "success_measure": clean(args.success),
            "consequence": clean(args.consequence),
            "scene": scene,
            "categories": [{"name": n, "prompts": pr} for n, pr in CATEGORIES],
            "worksheet": worksheet(
                args.proposal, args.date, args.success, args.consequence, args.reasons
            ),
        }
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return

    print(
        textwrap.dedent(
            worksheet(
                args.proposal, args.date, args.success, args.consequence, args.reasons
            )
        )
    )


if __name__ == "__main__":
    main()
