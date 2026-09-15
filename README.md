# scope-the-agent

A Claude skill that interviews you about one business process, tells you which steps deserve an agent, and writes the prompt that builds it. It ships free with issue #6 of *List of Demands*, "Scope the agent before you build it." Install takes five minutes. The interview takes about an hour, and the skill times it.

An agent inherits every decision you did not write down. This skill writes them down first.

## What it does

You pick one process and answer questions one at a time. The skill checks that the problem is worth solving and that someone owns the outcome, and it stops if nobody does. Then it runs the nine SIPOC questions in order, with a clock on them, and refuses to go past seven steps or past an output nobody can describe a good version of. Then it asks four questions about every step: who does it, what they decide and whether that decision can be stated as a rule, what goes wrong and how often, what a wrong result costs and whether the owner would live with that now and then, and what wrong looks like. It draws the process as a flowchart with one lane per person and a marked node wherever a decision exists that nobody could put into words.

Then it labels every step. Script when there is no decision. Human when the rule cannot be stated, or the step is an approval, or being wrong is not acceptable. Agent only when you stated the rule, stated what wrong looks like, and said the cost of an occasional wrong answer is one you would take. You confirm every label. If no step earns the agent label, it says so and tells you to build a script or a checklist instead.

From the confirmed labels it writes a build prompt shaped for Claude Code, and the same content as instructions for a Claude Project, with the decision rules quoted word for word, an exception table, the human checkpoints, acceptance criteria taken from what your customers said they expect, a test set with one case per exception, and a list of things the agent must never do.

You get eight files in a folder you name. Inside Cowork, it offers one more step: build the agent as a skill and run the test set against it. It only does that if you say yes.

## What it does not do

It cannot verify your answers. If the person answering does not do the work, the map will be clean, the labels will be confident, and both will be wrong. The person who does the job answers the questions. Anyone else answers wrong.

It does not build the agent unless you are in Cowork and say the words. It does not send your answers anywhere. It does not read anything on your computer that you did not paste in. It does not need any other skill, connector, or file to run.

## Install in five minutes

1. Download `scope-the-agent.zip` from the Releases tab on this page.
2. In Claude, open Settings, then Capabilities, and turn on **Code execution and file creation**. The skill runs without it, but the clock and the validator need it.
3. Open **Customize**, then **Skills**, then **Create skill**, and upload the zip. `SKILL.md` has to be at the root of the zip, and it is.
4. Start a new chat and type: `scope an agent for [your process]`.

One upload covers claude.ai, the desktop app, and Cowork. Skills are available on Free, Pro, Max, Team, and Enterprise plans.

If you would rather not install anything, `pasteable-prompt.md` is the same method as one prompt. Paste it into any AI chat tool. You lose the file packet, the validator, and the build step, and you keep the questions, the rules, and the prompt.

`worksheet.md` is the nine questions and the decision-inventory columns on one page, for running the interview on paper first.

## What you get

| File | What it is |
|---|---|
| `sipoc.md` | The one page: suppliers, inputs, process, outputs, customers, with the requirements at both edges and the elapsed minutes at the bottom |
| `process.json` | The same thing as data, so the validator can check it |
| `process.mmd` | The flowchart as Mermaid text. Paste it into mermaid.live to see it. A PNG appears beside it only if mermaid-cli is installed where the skill ran |
| `decision-inventory.md` | Every step: actor, decision as a rule, exceptions and frequency, cost of wrong, what wrong looks like |
| `classification.md` | The script / agent / human label on every step, the reason, and anything you overrode |
| `build-prompt.md` | The CLAUDE.md-shaped prompt for Claude Code |
| `project-instructions.md` | The same content for a Claude Project |
| `run-log.md` | The clock, every gate, and every assumption the skill made |

## Test the install

With code execution on, ask Claude to run:

```
python3 scripts/validate_process.py scripts/sample-process.json
```

A working install prints one warning about a step whose rule could not be stated, and a summary line ending in `0 fail, 1 warn`. That sample is a fictional bakery. Yours will not be.

## Where the method comes from

The nine-question sequence is adapted from onesixsigma.com. The framing of a process as inputs, process, outputs, and customers follows Geary Rummler and Alan Brache. The problem-validation gate, the decision inventory, the classification rules, and the build-prompt shape are mine. The one-hour claim is mine too, and the skill measures it every run so you can check it.

## Subscribe

This skill is free with a free subscription to *List of Demands*, a weekly issue on what breaks when a company outgrows its processes and what to do about it before buying a tool or building an agent. Subscribe here: https://brianbrooksby.substack.com/

If you run the skill on a real process, reply to the issue with your elapsed minutes. Nobody has published a number for how long the first SIPOC takes, and I would like to.

## License

CC BY 4.0. Use it, change it, ship it, credit it. See `LICENSE`.

---

Built by Brian Brooksby, Brooksby Consulting, for *List of Demands* issue #6.
