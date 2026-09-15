# Packet templates

Every file in the packet opens with the same header block. Fill it from the intake and the clock; never leave a field blank.

## Header block

```markdown
---
process: [I-2 name]
date: [YYYY-MM-DD]
skill: scope-the-agent v[version from SKILL.md frontmatter]
intake mode: [live interview | transcript pre-fill | document pre-fill]
authorship: [does the work | supervises | secondhand]
---
Built with scope-the-agent by Brian Brooksby, Brooksby Consulting, for Chaos to Clarity issue #6. https://brianbrooksby.substack.com/
```

The brand line appears in this header and nowhere else in the packet. Two files cannot carry the block as written: process.mmd takes it as `%%` comment lines, and process.json carries `process`, `date`, and `skill_version` as fields and nothing else.

## sipoc.md

```markdown
<header block>

# SIPOC — [process name]

**Starts when:** [Q1, earlier trigger if found]
**Ends when:** [Q2]
**Owner:** [V-4]
**Cost today:** [V-2]   **If nothing changes:** [V-3]

| Suppliers (Q8) | Inputs (Q7) | Input requirements (Q9) | Process (Q3) | Outputs (Q4) | Output requirements (Q6) | Customers (Q5) |
|---|---|---|---|---|---|---|
| [supplier] | [input] | [requirement] | 1. [step] | [output] | [requirement] | [customer] |
| | | | 2. [step] | | | |
| ... | | | ... | | | |

Requirements marked *(proposed, not current)* were stated by the SME as what they would check, not what is checked today. Inputs marked *(accepted as-is)* have no requirement; the agent cannot reject them.

**Nine questions, elapsed:** [n] minutes ([start] to [end]).
```

Keep requirements in their own columns. They are the point of the page. In chat, where seven columns will not fit, show the same content as three tables (suppliers / inputs / input requirements; process; outputs / output requirements / customers) and write the single seven-column table to the file.

## process.json

The structured record the validator reads. Shape in assets/process.schema.md. Build it after gate 3, before classification, so the validator can run before labels are proposed. Until gate 5 it lives in a scratch location (or only in the conversation when code execution is off); it joins the packet folder at gate 5 with everything else.

## decision-inventory.md

```markdown
<header block>

# Decision inventory — [process name]

| # | Step | Actor (D-a) | Decision as rule (D-a) | Exceptions and frequency (D-b) | Cost of wrong (D-c) | Owner accepts occasional wrong? (D-c) | What wrong looks like (D-d) |
|---|---|---|---|---|---|---|---|
| 1 | [step] | [actor] | [rule verbatim, or "no decision", or "cannot state it"] | [exception: frequency; ...] | [cost, "unknown", or "n/a"] | [acceptable / not acceptable / conditional: ... / unknown / n/a] | [text] |

Steps where a decision exists but the rule could not be stated: [list, or "none"]. These are drawn with a marked node in process.mmd.
```

## classification.md

```markdown
<header block>

# Classification — [process name]

| # | Step | Label | Why | Test that decided it |
|---|---|---|---|---|
| 1 | [step] | script / agent / human | [one line] | [rule from classification-rules.md] |

Agent steps: [n]. Script steps: [n]. Human steps: [n].
Labels the user changed at gate 4: [list with reason, or "none"].
[If zero agent steps: the zero-agent paragraph from classification-rules.md.]
```

## run-log.md

```markdown
<header block>

# Run log — [process name]

- Session started: [time]
- Intake mode: [mode]. Authorship: [V-1].
- Problem validation: cost [V-2]; do-nothing [V-3]; owner [V-4]. Verdict: [V-5 text].
- Nine questions: started [time], finished [time], elapsed [m] minutes [s] seconds.
- Q2 re-asked after a Q3 cut: [yes, new end state / no cut].
- Mode 3 provenance: confirmed from the document unchanged: [list]; rewritten by the SME: [list]. (Omit in modes 1 and 2.)
- Gates: 1 [confirmed at time], 2 [...], 3 [...], 4 [...], 5 [...], 6 [yes / no / not offered: reason].
- Q3 gate: [fired: original step count and where the SME cut, or "did not fire"].
- Q6 gate: [fired on which outputs, or "did not fire"].
- Q9 flags: [inputs accepted as-is, or "none"].
- Follow-ups that changed an answer: [Q1 earlier trigger found: yes/no; Q7 earlier input found: yes/no].
- Diagram: [Mermaid written; PNG rendered / not rendered because ...; Lucid version created / not offered because ...].
- Validator: [ran: summary line / not run: manual check done, findings].
- Assumptions the skill made: [every place it filled a gap, chose a default, or interpreted an answer. One line each. "None" is rarely true.]
- Answers flagged "from the document" or "secondhand": [list or none].
- Execute and build: [not offered: reason / offered, declined / built to <folder>, eval results in eval-results.md].
```

The assumptions line is the one a reader will use to judge the packet. Do not leave it thin.
