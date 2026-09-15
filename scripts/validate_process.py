#!/usr/bin/env python3
"""Validate a scope-the-agent process.json.

Standard library only. Run:

    python3 validate_process.py path/to/process.json

Prints findings and a summary line. Exit code 0 when nothing fails,
1 when at least one check fails, 2 when the file cannot be read.

Checks (same five as the manual check in assets/process.schema.md):
  1. Step count: 3 to 7. Under 5 warns. Over 7 fails ("two processes").
  2. Every output has a customer and at least one checkable requirement.
  3. Every input has a supplier and a requirement, or is marked accepted as-is.
  4. Every step has an actor.
  5. Every step with a decision has a rule or rule_stated == false, and
     every step with a rule records whether the owner would accept an
     occasional wrong result (wrong_acceptable).
"""

import json
import re
import sys
from pathlib import Path

# A requirement is "checkable" when it carries something a person could
# look at and answer yes or no: a number, a time word, a format word, or
# a pass/fail phrase. This is a coarse test on purpose; the interviewer
# holds the real bar. It exists to catch "accurate" and "on time" on their own.
CHECKABLE = re.compile(
    r"(\d|\bby\b|\bwithin\b|\bbefore\b|\bafter\b|\bevery\b|\beach\b|\bno\b|"
    r"\bnone\b|\ball\b|\bmatches?\b|\bequals?\b|\bformat\b|\bfield\b|"
    r"\bcolumn\b|\bsigned\b|\bapproved\b|\bpresent\b|\bmissing\b|"
    r"\bpass\b|\bfail\b|\bam\b|\bpm\b|\bday|\bhour|\bminute|\bweek|"
    r"\bmonth|\bpercent|%|\bowner\b|\bdue date\b|\bdate\b|\bonly\b|"
    r"\bignore|\bexclud|\bmust\b|\blocked\b|\bcounts?\b|\bclosed\b|"
    r"\blocation\b|\bper\b|\bcontains?\b|\bincludes?\b|\bnames?\b)",
    re.IGNORECASE,
)

VAGUE = re.compile(
    r"^\s*(accurate|correct|on time|timely|complete|good|right|up to date|"
    r"current|clean|proper|reasonable|quality)\s*\.?\s*$",
    re.IGNORECASE,
)


def checkable(text):
    if not isinstance(text, str) or not text.strip():
        return False
    if VAGUE.match(text):
        return False
    return bool(CHECKABLE.search(text))


def load(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"ERROR: file not found: {path}")
        sys.exit(2)
    except json.JSONDecodeError as e:
        print(f"ERROR: not valid JSON: {e}")
        sys.exit(2)


def validate(p):
    fails, warns = [], []

    # 1. Step count
    steps = p.get("steps") or []
    n = len(steps)
    if n == 0:
        fails.append("1 steps: none listed (Q3)")
    elif n > 7:
        fails.append(f"1 steps: {n} listed. That is two processes; cut it at a handoff and scope one (Q3)")
    elif n < 3:
        fails.append(f"1 steps: only {n}. A process this short is a step in a bigger one (Q3)")
    elif n < 5:
        warns.append(f"1 steps: {n} listed. Fine if nothing is hiding between them (Q3)")

    # 2. Outputs
    outputs = p.get("outputs") or []
    if not outputs:
        fails.append("2 outputs: none listed (Q4)")
    for o in outputs:
        name = o.get("name", "<unnamed output>")
        if not o.get("customer"):
            fails.append(f"2 output '{name}': no customer (Q5)")
        reqs = o.get("requirements") or []
        good = [r for r in reqs if checkable(r.get("text") if isinstance(r, dict) else r)]
        if not good:
            fails.append(
                f"2 output '{name}': no checkable requirement. "
                f"Need a number, deadline, format, or pass/fail test (Q6)"
            )

    # 3. Inputs
    inputs = p.get("inputs") or []
    if not inputs:
        fails.append("3 inputs: none listed (Q7)")
    for i in inputs:
        name = i.get("name", "<unnamed input>")
        if not i.get("supplier"):
            fails.append(f"3 input '{name}': no supplier (Q8)")
        reqs = i.get("requirements")
        if isinstance(reqs, str) and reqs.strip().lower() == "accepted as-is":
            warns.append(f"3 input '{name}': accepted as-is. The agent cannot reject it (Q9)")
            continue
        reqs = reqs or []
        good = [r for r in reqs if checkable(r.get("text") if isinstance(r, dict) else r)]
        if not good:
            fails.append(
                f"3 input '{name}': no checkable requirement and not marked accepted as-is (Q9)"
            )

    # 4 and 5. Steps
    for s in steps:
        label = f"step {s.get('n', '?')} '{s.get('name', '<unnamed>')}'"
        if not s.get("actor"):
            fails.append(f"4 {label}: no actor (D-a)")
        if s.get("decision") is True:
            if not s.get("rule") and s.get("rule_stated") is not False:
                fails.append(
                    f"5 {label}: decision with no rule and not flagged rule_stated=false (D-a)"
                )
            if s.get("rule_stated") is False:
                warns.append(f"5 {label}: decision exists, rule could not be stated. Marked node in the diagram")
            if s.get("rule"):
                wa = str(s.get("wrong_acceptable") or "").strip().lower()
                if wa in ("", "n/a"):
                    fails.append(
                        f"5 {label}: rule stated but 'would the owner accept an occasional wrong result' "
                        f"was not recorded (D-c second half). Agent cannot be earned without it"
                    )
                elif wa == "unknown":
                    warns.append(f"5 {label}: owner acceptance of a wrong result is unknown; classifies as human until stated")

    return fails, warns


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        sys.exit(2)
    p = load(Path(argv[1]))
    fails, warns = validate(p)
    for w in warns:
        print(f"WARN  {w}")
    for f in fails:
        print(f"FAIL  {f}")
    name = p.get("process", "<unnamed process>")
    steps = len(p.get("steps") or [])
    print(
        f"SUMMARY  {name}: {steps} steps, {len(p.get('outputs') or [])} outputs, "
        f"{len(p.get('inputs') or [])} inputs, {len(fails)} fail, {len(warns)} warn"
    )
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main(sys.argv)
