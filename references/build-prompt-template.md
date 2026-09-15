# Build-prompt template

Write build-prompt.md from the confirmed inventory only. Every slot names the question it came from. No slot is filled from general knowledge of how this kind of process usually works. If a slot has no source answer, write `[not captured in the interview: ask the SME]` and leave it. A gap the reader can see is fixable. A gap you filled is a defect they cannot see.

The target shape is a CLAUDE.md for Claude Code: a file that sits at the root of a project and tells the coding agent what to build and how the built thing must behave. Write it so a reader can paste it in unchanged.

---

```markdown
# [Process name] — agent build prompt

<packet header block from packet-templates.md>

## Purpose
One sentence, from Q4 and Q6: what this agent produces, for whom, to what standard.

## Trigger and end state
- Starts when: [Q1, using the earlier trigger if the follow-up found one]
- Done when: [Q2]

## Input contract
| Input | Source | Required form | If missing or malformed |
|---|---|---|---|
| [Q7] | [Q8] | [Q9] | [from D-b for the step that consumes it: ask the supplier / stop and escalate to <owner> / use the default the SME named. Never invented.] |

Inputs marked "accepted as-is" in Q9 get: "No requirement stated. The agent cannot reject this input. Flagged for the owner."

## Step sequence
One block per step, in Q3 order.

### Step N — [name] — [SCRIPT | AGENT | HUMAN]
- Actor today: [D-a]
- SCRIPT: implement as a tool. Input, output, and the deterministic rule. The agent calls it and does not reinterpret its result.
- AGENT: the agent's responsibility. Decision rule verbatim from D-a. Exceptions from D-b and what to do with each.
- HUMAN: a checkpoint. What the agent hands the person, what it asks, what it waits for, and what it does if no answer comes.

## Decision rules
Verbatim, one per AGENT step, quoted from D-a. No paraphrase. If the rule was stated in two sentences, quote two sentences.

## Exception handling
| Step | Exception | Frequency | Handle or escalate | To whom |
|---|---|---|---|---|
| [step] | [D-b] | [D-b] | [handle only if a rule in D-a covers it; otherwise escalate] | [V-4 owner unless the SME named someone else] |

## Human checkpoints
One per HUMAN step, plus every escalation target above. What is shown, what is asked, what "approved" looks like, and the timeout behavior (wait; do not proceed).

## Output contract
| Output | Customer | Acceptance criterion |
|---|---|---|
| [Q4] | [Q5] | [Q6, verbatim] |

Criteria marked "proposed, not current" keep that mark.

## Eval set
One case per exception (from D-b) and one per output requirement (from Q6). Each case:

- **Case [n] — [name].** Input: [what arrives]. Expected: [what the agent does]. Check: [what a person looks at to call pass or fail].

Written so a person can run it by hand with no tooling.

## Tools it needs
Named, from the inventory only: the systems in Q7 and Q8, and anything a SCRIPT step calls. If the interview named no system for a step, write `[system not named: ask the SME]`.

## Must never do
- Every HUMAN-labeled decision, restated as a prohibition ("Never approve X; hand it to [role].").
- Every "unacceptable" cost from D-c.
- Act on an input that failed its Q9 requirement.
- Invent a value for a missing input.
- Mark an output complete that fails its Q6 criterion.

## Provenance
Built from a scope-the-agent packet on [date], skill version [version]. Elapsed minutes on the nine questions: [n]. Answers marked "from the document" or "secondhand": [list, or "none"]. Labels the user overrode: [list, or "none"].
```
