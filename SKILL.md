---
name: scope-the-agent
description: Scope an AI agent before anyone builds it. Interviews the person who does a business process one question at a time, checks the problem is worth solving and that someone owns the outcome, runs a nine-question SIPOC with a clock on it, inventories every decision in the process, draws it as a flowchart, labels each step script / agent / human, and writes the build prompt from the confirmed inventory. Use this whenever someone says "build me an agent that...", "should this be an agent", "automate this process", "scope the agent", "map this process before we automate it", "SIPOC", "write the prompt for an agent that...", or describes a repeating business process they want handed to AI, even if they do not say the word agent.
metadata:
  version: 1.0.0
  author: Brian Brooksby, Brooksby Consulting
  license: CC BY 4.0
---

# Scope the agent

An agent inherits every decision nobody wrote down. This skill writes them down first. It takes one business process, described by the person who does it, and hands back a packet: a one-page SIPOC, a decision inventory, a flowchart, a script / agent / human label on every step, and the prompt that builds the agent. It refuses to write the prompt from a blank description, because a prompt written from a description is a guess with confident formatting.

The skill enforces structure. It cannot enforce truth. If the person answering does not do the work, the map will be clean and wrong.

## What this skill needs

Nothing beyond Claude. It uses what the session has and works without the rest:

- **A structured question tool** (a multiple-choice card) when present, for mode choice, yes/no gates, "who" answers, and label confirmation. When absent, every question is asked in plain chat. The interview never stops for lack of a card.
- **Code execution**, when present, for the clock (`date`), the validator (`scripts/validate_process.py`), and PNG rendering if mermaid-cli happens to be installed. When absent, the clock is asked, the validator becomes the five-question manual check in `assets/process.schema.md`, and the diagram stays as Mermaid text.
- **A folder the session can write to**, when present, for the packet. When absent, the packet files are produced for download.
- **A folder on the user's own computer**, when present, for the optional last step (build the agent). Without it that step is skipped with one line saying why.
- **Lucid tools**, if the session has them, are offered once for a share-ready diagram. Never required.

Everything the skill reads lives in this folder: `references/`, `scripts/`, `assets/`. It reads no configuration, no other skill, and nothing outside its own folder.

## Version

1.0.0. This number goes in the header of every packet file.

## Phases

Read `references/interview-script.md` before Phase 0 and follow it word for word. Every question is asked alone; the next is not sent until the answer is in; each question opens by echoing the previous answer in one line. The order of the nine questions is the method.

### Phase 0 — Intake

Say the sanitization line (I-0). Ask the mode (I-1): live interview, pasted transcript, or pasted document. Ask the process name (I-2). If files can be written, ask where the packet goes (I-3); default is `scope-the-agent-output/<process-name>/` beside the working folder.

Modes 2 and 3 pre-fill answers from the pasted text and then walk every question anyway, showing the draft for correction. Mode 3 prefixes every unconfirmed answer with "From the document:" and that prefix survives into the packet. Never skip a question because the document seemed to answer it.

### Phase 1 — Validate the problem

Four questions (V-1 to V-4): who answers and whether they do the work, what the process costs today, what happens if nothing changes, who owns the outcome.

If nobody owns the outcome, say so in the words of the script, write run-log.md with what was captured, and stop. This is the most common reason an agent gets built and abandoned. Do not soften it and do not continue.

Show the verdict (V-5) and confirm it. **Gate 1.**

### Phase 2 — The nine questions, timed

Read the clock before Q1 and after Q9. Ask the nine questions in this order and no other: start, end, the steps, outputs, customers, what each customer expects from each output, inputs, suppliers, what the process expects from each input. Ask "what happens before that?" once at Q1 and once at Q7.

Three rules that hold the exercise together:

- **More than seven steps is two processes.** Say so and ask which one. Do not proceed past seven. After a cut, ask Q2 again for the half that was kept.
- **Q6 and Q9 are the questions that matter.** They are the only source of acceptance criteria, of the eval set, and of the definition of wrong. Coach them, ask the second-pass question, and do not proceed past an output or an input with no checkable requirement. A requirement is checkable when a person could look at the thing and say yes or no without asking anyone.
- **Outputs before inputs.** A process scoped from what it consumes ends up automating the consumption.

Show the SIPOC page with requirements in their own columns and the elapsed minutes at the bottom (layout in `references/packet-templates.md`). **Gate 2.**

### Phase 3 — Decision inventory and the map

For each step in order, four questions: actor and decision stated as a rule (or "no decision", or "cannot state it"), exceptions and how often each fires, what a wrong result costs and whether the owner would accept that now and then to have the step run unattended (skipped when there is no decision and no exception), and what wrong looks like.

"Cannot state it" is a real answer and the most useful one in the inventory. Record it verbatim. Never help the SME invent a rule they did not have. The "would the owner accept it" half of the cost question is the only thing that can make a step an agent; ask it in those words and take the answer given.

Build `process.json` (`assets/process.schema.md`) in a scratch location and run the validator if code execution is on; otherwise do the manual check. Record the result in run-log.md. The file joins the packet at gate 5.

Draw the flowchart per `references/mermaid-conventions.md`: one subgraph per actor, a diamond where a rule was stated, a marked node where a decision exists and the rule could not be stated. Show it with the inventory table. Preview as an artifact if the session can. Offer Lucid once if the tools exist. **Gate 3.**

### Phase 4 — Classification

Apply `references/classification-rules.md` to every step. Script when there is no decision. Agent only when the rule was stated, wrong was stated, and the SME said the owner would accept an occasional wrong result. Human when the rule could not be stated, the step decides the terms of an approval or an outside commitment, the cost is unacceptable or unknown, or the SME wants a person on it. Cost wins every tie.

Show one card with every step, the proposed label, and a one-line reason. The user toggles. **Gate 4.** Every label is confirmed before anything is written from it.

If no step earned agent, say so in the words of the rules file, recommend a script or a checklist, and write the packet with a script spec in place of the build prompt and the same checklist in second person in place of the project instructions. Do not write an agent prompt for a process that has no agent step in it.

### Phase 5 — The build prompt

From the confirmed inventory only, using `references/build-prompt-template.md`. Every slot names its source question. A slot with no source answer says `[not captured in the interview: ask the SME]`. Decision rules are quoted verbatim. The eval set has one case per exception and one per output requirement. The must-never-do list restates every human decision as a prohibition.

Then `references/project-instructions-template.md` for the same content as Claude Project instructions.

### Phase 6 — The packet

Reconfirm the folder named at intake in one line. **Gate 5.** Then write, each with the header block from `references/packet-templates.md`:

| File | Contents |
|---|---|
| `sipoc.md` | The one page, with elapsed minutes |
| `process.json` | The structured record |
| `process.mmd` | The flowchart. Plus `process.png` only if mermaid-cli rendered it |
| `decision-inventory.md` | The five-column table |
| `classification.md` | Labels, reasons, overrides |
| `build-prompt.md` | The CLAUDE.md-shaped prompt (or the script spec) |
| `project-instructions.md` | The Claude Project version |
| `run-log.md` | Times, gates, flags, and every assumption the skill made |

Present the packet for review. Say where it is. Say what the skill assumed, in the same words as run-log.md.

### Phase 7 — Execute and build the agent (Cowork only)

Read `references/execute-and-build.md`. Offer the step once, in its words, only when the packet is written, at least one step is agent, and the session can write to a folder on the user's computer. Build only on an explicit yes. Run the eval set against the built skill and report pass and fail counts with evidence. Never install anything.

Outside that condition, say the not-available line from that file, which names the reason (no agent step, or no folder on the user's computer) and where to take build-prompt.md instead.

## Hard rules

- One question per message. Never batch. Never reorder the nine.
- Nobody owns the outcome: stop.
- More than seven steps: refuse until it is one process.
- An output or input with no checkable requirement: do not proceed past it.
- Agent is earned by three stated answers, never inferred from what the process "probably" needs.
- Every label is confirmed by the user before it is used.
- The build prompt is written from the inventory. Never from a description, a document, or general knowledge of the process type.
- Never invent a specific. A number, a system, a threshold, or a rule the SME did not supply is a gap, and the packet shows the gap.
- No packet file is written before gate 5, with two exceptions: run-log.md when the exercise stops at "nobody owns it", and process.json to a scratch location so the validator can run. Nothing is built before gate 6.
- Never install, publish, or send anything. The packet is the user's to share.
- Everything the skill needs is in this folder. If a reference file is missing, say which one and stop; do not reconstruct it from memory.

## Attribution

The nine-question sequence is adapted from onesixsigma.com. The process, inputs, outputs, customers framing follows Rummler and Brache. The decision inventory, the classification rules, and the build-prompt shape are the author's. Released under CC BY 4.0 by Brian Brooksby, Brooksby Consulting, with List of Demands issue #6.
