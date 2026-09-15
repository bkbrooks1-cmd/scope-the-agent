# Execute and build the agent

This step runs only when all three are true: the packet has been written (gate 5 passed), at least one step is labeled agent, and the session can write files into a folder on the user's own computer (a connected folder). That last condition is how the skill knows it is inside Cowork. When any of the three is false, say one line and stop:

> The build step is not available here because [no step earned an agent, so there is nothing to build as one | this session cannot write to a folder on your computer]. Take build-prompt.md into Claude Code, or project-instructions.md into a Claude Project, and build from there.

Do not offer a zip, an artifact, or a workaround.

## The offer (gate 6)

After presenting the packet for review, ask once:

> One more step, if you want it: **Execute and build the agent.** I will build it as a Cowork skill (a SKILL.md plus references) in a folder you name, run the eval set against it, and report what passed and what failed. Nothing gets installed. Say yes to build, or no to stop here.

Build only on an explicit yes. "Sure", "go ahead", "yes" count. Silence, "maybe", "what would that look like" do not; answer the question and ask again.

Then ask for the folder. Default: `<packet folder>/built-agent/`.

## What gets built

A skill folder in the same shape as this one:

```
<folder>/
├── SKILL.md
└── references/
    ├── decision-rules.md      ← the Decision rules section of build-prompt.md, verbatim
    ├── exceptions.md          ← the Exception handling and Human checkpoints sections
    ├── contracts.md           ← Input contract and Output contract
    └── eval-set.md            ← the Eval set section, one case per heading
```

SKILL.md for the built agent:

- Frontmatter: `name` from the process name (lowercase, hyphens), `description` that names the trigger from Q1 and the outputs from Q4 so the skill fires when the user describes that work.
- Body, in order: what it needs (the inputs from Q7, named as things the user provides or connects; if a system was named, say the user connects it, never assume it is connected); the trigger and end state; the step sequence from build-prompt.md with SCRIPT steps written as deterministic instructions, AGENT steps carrying their verbatim rule, and HUMAN steps written as "stop and ask"; the must-never-do list as hard rules.
- Point to each reference file where its content is needed.
- No path outside its own folder. No reference to scope-the-agent; the provenance line names the interview date, not this skill. It stands alone.
- The "one question per ask" rule in the built SKILL.md means one checkpoint per message; a checkpoint script may carry two fields (type and owner, say) when the interview asked for them together.

## Running the eval set

For each case in eval-set.md:

1. If subagents are available, give one a fresh context with only the built skill folder and the case's input, and ask it to run the skill on that input and return what it did.
2. If not, run the case inline: read the built SKILL.md, take the case's input, do what the skill says, and record the result.
3. Grade pass or fail against the case's "check" line. Quote the evidence.

Inputs that name a system the session cannot reach (an email account, an ERP) are run with the case's stated input as a paste. The eval tests the rules, not the connection.

## The report

Write `<folder>/eval-results.md`:

```markdown
<packet header block>

# Eval results — [process name]

| Case | Input | Expected | Result | Pass/fail | Evidence |
|---|---|---|---|---|---|

Passed: [n] of [total]. Failed: [n].
Failures, one line each: what the built agent did, and which rule in build-prompt.md it did not follow or which rule was missing.
```

Say the counts in chat and point to the file. Do not fix the built agent and re-run in the same breath; the user decides whether a failure is a bug in the build or a gap in the interview. Most are the second.
