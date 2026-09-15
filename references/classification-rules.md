# Classification rules

Every step gets exactly one label: **script**, **agent**, or **human**. The skill proposes, the user confirms (gate 4), and the confirmed label is what the build prompt uses.

The bias runs toward script and human. Agent is the label that has to be earned, because an agent is the only one of the three that produces a plausible wrong answer without anyone noticing. A script fails loudly. A person asks. An agent improvises around the gap.

## Script

The step has no decision (D-a said "no decision"), or its only decision is a lookup or a comparison a person could write as a table. Same input, same output, every time. Exceptions at a script step are handled by stopping and telling someone, not by deciding.

Do not build an agent for this step. Build a tool, a formula, a query, or a workflow rule. In the build prompt, script steps become tools the agent calls.

## Agent

All three must hold:

1. There is a decision, and D-a stated it as a rule the SME could put in words.
2. D-d stated what wrong looks like, in a way that can be checked after the fact.
3. The second half of D-c was "acceptable" (or "conditional", with the condition carried into the build prompt as a guard). The SME said so. The skill did not infer it. "Unknown" and "not acceptable" both fail this test.

A rule that reads "use judgment", "depends on the situation", "you just know", "case by case", or "ask [name]" fails test 1. Those are the words people use for a decision they have never had to write down. Record them verbatim; they are the most useful line in the inventory.

## Human

Any one of these is enough:

- D-a said "cannot state it", or the rule fails test 1.
- The step is an approval, a sign-off, or a commitment to an outside party (a customer, a regulator, a bank, a vendor) **where this step decides the terms**. A step that only sends what an earlier step already decided is a script; the commitment was made upstream and that upstream step carries the label.
- D-c named a cost the owner would not accept even once: a lost customer, a compliance breach, a safety issue, an irreversible payment.
- The SME asked for a person to stay on it. That is a valid reason. Record it as "SME choice".

## Tie-breaks

| Situation | Label | Note in classification.md |
|---|---|---|
| Decision stated, wrong not stated | human | "Stating what wrong looks like would move this to agent." |
| Decision stated, wrong stated, cost unacceptable | human | "Cost wins." |
| No decision, exceptions more often than one in ten | script | Exception path routes to a human checkpoint. Frequency does not make a step an agent; a decision does. |
| SME wants an agent on a step that fails a test | human | Name the test that failed and the answer that would change it. The user can overrule at gate 4; record "user overrode: [reason]". |
| The decision's only outcomes are "escalate" or "do not escalate", nothing else changes | script | "If condition then escalate" is a rule a table can hold. A rule that also confirms, approves, or chooses is a decision, and the agent tests apply. |
| Cost of wrong "unknown" | human | Nobody can say what a wrong answer costs, so nobody can accept it. Stating the cost would reopen the agent tests. |

## The gate 4 card

Show every step on one card with the proposed label and the one-line reason. The user toggles any label. Do not move on until every label is confirmed. Then count.

## The zero-agent case

If no step is labeled agent after confirmation, say so plainly:

> No step earned an agent. [N] are scripts and [M] need a person. Build a script or a checklist for this process; an agent would add cost and a new way to be wrong without adding a decision it could make.

Then write the packet anyway. Replace build-prompt.md with a one-page spec for the script or checklist (same header block, same input and output contracts, no decision rules section), and project-instructions.md with the same checklist in second person for a Claude Project. Say in run-log.md that no agent was recommended and why. Do not skip to the build prompt to give the user something.
