#!/usr/bin/env python3
"""decompose.py - offline helper for the first-principles skill.

Extract candidate constraints from a problem statement and suggest a
classification: physical, regulatory, resource, invariant, inherited, or
preference. The output is a starting table for judgment, not a verdict.
Every label is a hypothesis to verify with the accountable owner.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

TYPE_ORDER = ("physics", "regulation", "resource", "invariant", "inherited", "preference")

CUES = {
    "physics": (
        r"\b(physics|physical|thermodynamic|speed of light|speed of sound|gravity|"
        r"latency|bandwidth|throughput|energy|heat|mass|weight|distance|voltage|"
        r"memory|cpu|gpu|storage limit|hardware limit|manufactur\w*|precision|"
        r"material strength|materials?|battery|bandwidth)\b"
    ),
    "regulation": (
        r"\b(law|legal|lawsuit|regulation|regulatory|compliance|compliant|gdpr|hipaa|"
        r"sox|pci|contract|contractual|statutory|jurisdiction|license|permit|tax|"
        r"export control|data residency|court order|mandated by law|terms of service)\b"
    ),
    "resource": (
        r"\b(budget|cost|costs|price|spend|headcount|staffing|capacity|deadline|"
        r"timeline|schedule|quota|inventory|supply|dollars?|euros?|fte|"
        r"per month|per year|at most|no more than|maximum|minimum|limited to|"
        r"within \d+|within (?:a|one|two|three|four|five|six|seven|eight|nine|ten)\b)\b"
    ),
    "invariant": (
        r"\b(invariant|integrity|safety|security|privacy|auditable|audit trail|atomic|"
        r"idempotent|monotonic|non-?negative|unique|reconcil\w*|consisten\w*|"
        r"no data loss|cannot lose|must not lose|never lose|must remain|always remain|"
        r"uptime|zero downtime|high availability|durab\w*)\b"
    ),
    "inherited": (
        r"\b(we(?:'ve| have) always|always done|that(?:'s| is) how|how we do|"
        r"industry standard|best practice|standard practice|convention|legacy|"
        r"existing|incumbent|current (?:process|flow|system|tool)|competitor\w*|"
        r"everyone (?:does|uses)|company policy|internal policy|policy|process|"
        r"approval|sign-?off|template|default|traditionally|used to|because we use)\b"
    ),
    "preference": (
        r"\b(prefer\w*|ideally|nice to have|would like|wish|want to|comfort\w*|"
        r"brand|aesthetic|convenien\w*|should probably|better if|optional|bonus|"
        r"delight\w*)\b"
    ),
}

COMPILED = {name: re.compile(pattern, re.I) for name, pattern in CUES.items()}

MODAL = re.compile(
    r"\b(must|have to|has to|had to|cannot|can't|can not|required?|requires?|requiring|"
    r"need(?:s|ed)? to|only|always|never|within|deadline|budget|maximum|minimum|"
    r"no more than|at (?:most|least)|limited to|restricted to|before|after|"
    r"by (?:law|policy|contract|regulation)|policy|standard|comply|compliance|"
    r"depend(?:s|ed)? on|because|ideally|prefer\w*|nice to have|would like|want to)\b",
    re.I,
)

SPLIT = re.compile(r"(?<=[.!?])\s+|\n+|;\s+|,\s+(?:and|but)\s+", re.I)
BULLET = re.compile(r"^\s*(?:[-*\u2022]|\d+[.)])\s+")

QUESTIONS = {
    "physics": "What measurement or law establishes this limit, and under what conditions?",
    "regulation": "Which exact rule, contract, or clause covers this case, and does its scope reach here?",
    "resource": "Is the level fixed, or is it a tradeoff? Who controls the number and period?",
    "invariant": "What failure mode does this prevent, and is this the only acceptable control?",
    "inherited": "Who chose this, when, what did it solve then, and would we choose it again?",
    "preference": "Whose preference is this, and what would we trade to honor it?",
    "unclassified": "Which law, measurement, obligation, or invariant would make this true?",
}

NEXT_STEP = {
    "physics": "Verify the measurement and treat it as hard until disproved.",
    "regulation": "Verify the text and scope with the accountable owner; keep until then.",
    "resource": "Verify the level and controller; trade off explicitly.",
    "invariant": "Verify the failure mode and keep the invariant.",
    "inherited": "Test owner, date, and current need; likely droppable.",
    "preference": "Name the preference and make the trade explicit.",
    "unclassified": "Investigate before the rebuild; do not assume it is fundamental.",
}

NOTES = (
    "This helper flags the constraint family that the wording resembles; it cannot "
    "know whether the claim is true. Replace every suggested label with evidence.",
    "Internal policy is inherited unless an external obligation requires it. "
    "An external regulation is not a preference.",
    "For each row ask: who owns it, who could waive it, and what observation would "
    "refute it? Record the answers in the capture table.",
)


@dataclass
class Candidate:
    id: str
    text: str
    kind: str
    signal: str
    question: str
    next_step: str


def normalize(text: str) -> str:
    text = BULLET.sub("", text.strip())
    text = re.sub(r"\s+", " ", text)
    if text and text[-1] not in ".?!":
        text += "."
    return text


def split_candidates(text: str) -> list[str]:
    parts = [normalize(p) for p in SPLIT.split(text) if p and p.strip()]
    seen: set[str] = set()
    out: list[str] = []
    for part in parts:
        if len(part.split()) < 2 or not MODAL.search(part):
            continue
        key = part.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(part)
    return out


def classify(text: str) -> tuple[str, str]:
    for kind in TYPE_ORDER:
        match = COMPILED[kind].search(text)
        if match:
            return kind, match.group(0)
    return "unclassified", ""


def build(candidates: list[str]) -> list[Candidate]:
    rows: list[Candidate] = []
    seen: set[str] = set()
    for text in candidates:
        text = normalize(text)
        key = text.lower()
        if not text or key in seen:
            continue
        seen.add(key)
        kind, signal = classify(text)
        rows.append(
            Candidate(
                id=f"C{len(rows) + 1}",
                text=text,
                kind=kind,
                signal=signal,
                question=QUESTIONS[kind],
                next_step=NEXT_STEP[kind],
            )
        )
    return rows


def esc(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def render_markdown(problem: str, rows: list[Candidate]) -> str:
    out = ["# Constraint classification", ""]
    out.append(f"**Problem.** {problem.strip() or '(none provided)'}")
    out.append("")
    if not rows:
        out.append(
            "No candidate constraints were detected. Rewrite the problem as checkable "
            "assertions using words like *must*, *cannot*, *within*, *only*, or *never*, "
            "or pass candidates with `--constraint`."
        )
        out.append("")
        out.extend(f"- **{note}**" for note in NOTES)
        return "\n".join(out) + "\n"

    out.append(
        f"**Candidates.** {len(rows)} extracted. Labels are hypotheses, not verdicts."
    )
    out.append("")
    out.append("| # | Candidate | Suggested type | Signal | Question to settle | Next step |")
    out.append("| --- | --- | --- | --- | --- | --- |")
    for row in rows:
        signal = f'matched "{esc(row.signal)}"' if row.signal else "modal/limit wording only"
        out.append(
            f"| {row.id} | {esc(row.text)} | {row.kind} | {signal} | "
            f"{esc(row.question)} | {esc(row.next_step)} |"
        )
    out.append("")
    counts = {}
    for row in rows:
        counts[row.kind] = counts.get(row.kind, 0) + 1
    summary = ", ".join(f"{kind} {counts[kind]}" for kind in TYPE_ORDER if kind in counts)
    if "unclassified" in counts:
        summary += f", unclassified {counts['unclassified']}"
    out.append(f"**Summary.** {summary}.")
    out.append("")
    out.extend(f"- {note}" for note in NOTES)
    return "\n".join(out) + "\n"


def render_json(problem: str, rows: list[Candidate]) -> str:
    return json.dumps(
        {
            "problem": problem.strip(),
            "count": len(rows),
            "candidates": [asdict(row) for row in rows],
            "notes": list(NOTES),
        },
        indent=2,
    )


def list_types() -> str:
    lines = ["# Constraint families", "", "| Type | Question to settle | Next step |", "| --- | --- | --- |"]
    for kind in (*TYPE_ORDER, "unclassified"):
        lines.append(f"| {kind} | {QUESTIONS[kind]} | {NEXT_STEP[kind]} |")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Extract and suggest classifications for constraints in a problem statement.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            '  decompose.py "We must launch within six weeks. GDPR requires EU data to stay in region."\n'
            "  decompose.py --file problem.txt --json\n"
            '  decompose.py "Onboarding must be a tutorial" --constraint "Budget is fixed at 50k"'
        ),
    )
    parser.add_argument("problem", nargs="*", help="problem statement text")
    parser.add_argument("--file", type=Path, help="read the problem statement from a file")
    parser.add_argument(
        "--constraint",
        action="append",
        default=[],
        metavar="TEXT",
        help="add an explicit candidate (repeatable)",
    )
    parser.add_argument("--json", action="store_true", help="emit JSON instead of Markdown")
    parser.add_argument("--list-types", action="store_true", help="show the classification legend")
    args = parser.parse_args(argv)

    if args.list_types:
        sys.stdout.write(list_types())
        return 0

    if args.file:
        try:
            text = args.file.read_text()
        except OSError as exc:
            parser.error(f"cannot read {args.file}: {exc}")
    elif args.problem:
        text = " ".join(args.problem)
    elif not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        parser.error("provide problem text, --file, or pipe it on stdin")

    candidates = split_candidates(text) + [normalize(c) for c in args.constraint]
    rows = build(candidates)
    output = render_json(text, rows) if args.json else render_markdown(text, rows)
    sys.stdout.write(output if output.endswith("\n") else output + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
