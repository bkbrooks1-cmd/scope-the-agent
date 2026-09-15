# Project-instructions template

project-instructions.md carries the same content as build-prompt.md, reshaped for a reader who will not use Claude Code and will instead paste it into the custom-instructions box of a Claude Project (or the equivalent in another assistant). Same rules, same sources, same gaps left visible.

Three differences from the build prompt:

1. Second person to the assistant. "You run the [process] for [owner]." The Project has no separate coding agent; the instructions are the agent.
2. "Tools it needs" becomes "What the user will paste or attach", because a Project cannot call systems. Each input from Q7 becomes something the user brings to the chat.
3. Every HUMAN checkpoint becomes "Stop and ask before…", because the person is in the chat.

Keep it under 1,500 words. Drop nothing from the decision rules, the exception table, the output contract, or the must-never-do list; tighten the prose around them instead.

---

```markdown
# [Process name] — Claude Project instructions

<packet header block>

For a reader who will not use Claude Code. Same rules as build-prompt.md.

## What you do
You run the [process name] for [V-4 owner]. You produce [Q4 outputs] for [Q5 customers]. An output is done when [Q6 criteria, one line each].

## When you start and when you stop
Start when the user tells you [Q1 trigger] has happened. Stop when [Q2 end state] is true and you have shown the user the output against its acceptance criteria.

## What the user will paste or attach
| Input | Who has it | It must be | If it is not |
|---|---|---|---|
| [Q7] | [Q8] | [Q9] | [ask for it again / stop and tell the user / use the stated default] |

## The steps, in order
1. **[Step] — script.** Do exactly: [rule]. Do not reinterpret the result.
2. **[Step] — agent.** Decide by this rule, verbatim: "[D-a]". If [D-b exception], then [handle or ask].
3. **[Step] — stop and ask.** Show the user [what], ask [what], and wait. Do not proceed on silence.
...

## Exceptions
| Exception | How often | What you do | Who you tell |
|---|---|---|---|

## What done looks like
| Output | Who gets it | Check |
|---|---|---|

## Never
- [each prohibition from the build prompt]

## How to test me
Run the cases below before trusting me on a real week. For each, paste the input and compare what I do with "expected".
- Case [n]: [input] → expected [behavior]; check [what you look at].

Provenance: [same line as the build prompt]
```
