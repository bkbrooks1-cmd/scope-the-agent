# Interview script

Every question below is asked on its own. Do not send the next one until the answer is in. Where a question repeats per output, per input, or per step, each repeat is its own message. Open each question by echoing the previous answer in one line so the SME can correct it without a separate "is that right?"

When the session has a structured question tool (a multiple-choice card), use it for: the intake mode, yes/no gates, "who" answers (offer roles already named, plus Other), and label confirmation. Use plain text for everything else. When no such tool exists, ask the same words in chat and read the reply. Never let the absence of a card stop the interview.

The order is the method. Do not reorder, merge, or skip a question because the answer seems obvious or because a pasted document appears to cover it.

---

## Phase 0 — Intake

**I-0. Sanitization (said once; not a question).**

> One thing before we start. Anonymize client, vendor, and people names as you answer: "the distributor", "the scheduler", "the ERP". The packet you get at the end is yours to share, so keep out anything you would not want in it.

**I-1. Mode.**

> How do you want to work?
> 1. Live interview. I ask, you answer, one question at a time. About an hour.
> 2. You paste a transcript of someone walking through the process. I pre-fill the answers and you correct them.
> 3. You paste an SOP or process document. I pre-fill, and every answer is flagged "from the document, not from you" until you confirm it.

**I-2. Name.**

> What is the process called, in the words your team uses for it?

**I-3. Packet location.** Ask only when the session can write files.

> Where should the packet go? Default is a folder called `scope-the-agent-output/<process-name>/` next to where we are working.

### Pre-fill rule for modes 2 and 3

Read the pasted text once. Draft an answer for every question in Phases 1 and 2, and for every step in Phase 3, that the text supports. Leave blank whatever it does not support; never fill a blank from general knowledge of how this kind of process usually works. Then walk the questions in the same order as a live interview. Show the draft answer and ask: "Correct this, or say yes."

In mode 3, prefix every draft with **From the document:** until the SME confirms or rewrites it. Confirmation is authorship: once the SME says yes, the prefix drops. run-log.md lists which answers were confirmed from the document unchanged and which the SME rewrote, so the provenance survives without cluttering the packet. A document describes how the process is supposed to run; the SME describes how it runs.

When the drafted Q3 has more than seven steps, fire the Q3 gate as the draft is shown, before asking the SME to confirm it. Do not ask someone to confirm a list you are about to refuse.

---

## Phase 1 — Validate the problem

**V-1. Authorship.**

> Do you do this process yourself, supervise the person who does, or neither?

If neither:

> Who does it, and can they answer these questions instead? If not, we can continue, but every answer gets flagged "secondhand" in the packet, and the map will be as good as your guess.

**V-2. Cost today.**

> What does this process cost today? Give whatever you actually have: hours per week, number of people, dollars, error rate, how often it runs late. A rough number beats none. If you have no number, say so and I will write "unmeasured".

If the SME gives a number without a period ("2 to 3 hours"), ask which: per run, per week, or in total. Do not assume it.

**V-3. Do nothing.**

> If nothing changes for the next year, what happens?

**V-4. Owner.**

> Who owns the outcome? One name or role. The person who gets the call when it goes wrong.

If the answer is nobody, everyone, a committee, "it depends", or the SME cannot name one:

> Nobody owns the outcome. That is the most common reason an agent gets built and then abandoned: there is no one to tell it when it is wrong, and no one who notices when it stops. Find the owner, then come back. I have saved what we have so far to run-log.md so you do not repeat it.

Then stop. Write run-log.md with the answers so far and the reason for stopping. Do not continue to Phase 2. If the SME names an owner in the same session, resume from V-5.

**V-5. The verdict (shown, then confirmed). Gate 1.**

One paragraph: the cost, the do-nothing consequence in the SME's own words (not a shortened version; the first live run cut it and was sent back), the owner, the authorship level. Then one of:

> Worth scoping. Starting the nine questions. I will note the time.

or, when V-2 is unmeasured and V-3 is "nothing much":

> This one may not be worth an agent. The cost is unmeasured and nothing breaks if it stays manual. I will scope it if you want, but the packet will say that.

Ask the SME to confirm before starting Phase 2. Only V-4 stops the exercise; V-5 informs it.

---

## Phase 2 — The nine questions (timed)

Record the time before Q1. Run `date` if code execution is available; otherwise ask: "What time is it where you are? I am timing the nine questions." Record it again the moment the Q9 answers are complete. The elapsed minutes go in sipoc.md and run-log.md.

Never ask about inputs before outputs. Outputs first tells you what the process is for; inputs first tells you what it consumes, and a process scoped from what it consumes ends up automating the consumption.

**Q1. When does the process start?**

> What is the trigger: the event, message, or time that makes someone begin?

Then, once:

> What happens before that? Is there an earlier event that actually starts it, like a promise someone made or a form that arrived days earlier?

Take the answer and move on. Do not ask a third time. If the follow-up found an earlier trigger, record both and mark the earlier one as the start.

**Q2. When does the process end?**

> What is true when it is done? Something you could point to: a record updated, a thing shipped, a person told.

**Q3. What is the process?**

> List the steps in order, five to seven of them, each starting with a verb. Big steps, not keystrokes.

Gate, more than seven:

> That is two processes. Which one are we scoping today? Tell me where to cut it and I will take that half.

Repeat until seven or fewer. Do not proceed past seven. After a cut, ask Q2 again for the half that was kept ("The process now ends at [last kept step]. What is true when that is done?"), because the end state the SME gave belonged to the whole.

Coach, fewer than five (once only):

> Is there a step hiding between [step X] and [step Y]? If not, [N] steps is fine.

**Q4. What are the outputs?**

> What comes out? Goods, services, records, decisions, or consequences. Everything the process produces that someone else picks up.

**Q5. Who is the customer of each output?**

One message per output:

> Who receives [output]? A role, not a name.

When the same customer takes every output, confirm once: "Same customer for all of them?"

**Q6. What does each customer expect from each output?**

This question and Q9 are the two that decide whether the agent can be judged. Everything downstream (acceptance criteria, the eval set, the definition of "wrong") is built from these two answers. Spend the time here.

One message per output:

> What does [customer] expect from [output]? Give me something checkable: a number, a deadline, a format, a pass/fail test. "Accurate" and "on time" are not requirements until you say what accurate and on time mean. Example: "every open item has an owner and a due date" is checkable; "it is up to date" is not.

After the first answer for each output, once:

> What else would [customer] check before they trusted it? Anything they have sent back or complained about?

Gate: an output with no checkable requirement blocks the exercise.

> I cannot scope an agent to produce [output] if nobody can say what a good one looks like. What would you check to know it is right? If it has never been checked, tell me what you would check, and I will mark it "proposed, not current".

Do not proceed until every output has at least one checkable requirement. A requirement is checkable when a person could look at the output and say yes or no without asking anyone.

**Q7. What inputs are required?**

> What has to be there for the process to run? Think in six kinds: people, machines or systems, materials or data, methods or rules, measurements, and conditions outside your control.

Then, once:

> What happens before that? Is there an input that arrives earlier than you are thinking of, one that is already in place by the time the trigger fires?

**Q8. Who supplies each input?**

One message per input:

> Who or what supplies [input]? A role, a system, or an outside party.

**Q9. What does the process expect from each input?**

Same weight as Q6. A process that cannot say what it needs from its inputs cannot tell the agent when to stop, and an agent that does not know when to stop improvises.

One message per input:

> What has to be true about [input] for the process to work? Format, timing, completeness, a threshold. Example: "meeting minutes arrive as a document within one day of the meeting, with action items marked" is a requirement; "the minutes" is not.

After the first answer for each input, once:

> What arrives wrong most often with [input], or does not arrive at all, and what do you do then?

The "does not arrive" half feeds the input contract's missing-field column. Without it, the build prompt has to leave that cell as a gap.

Gate, same as Q6, with one difference: push once with the coaching line, and if the SME still says the input is whatever arrives, write "accepted as-is" and move on. Flag it in run-log.md as a place the agent will have no way to reject bad input. An input can be accepted as-is; an output cannot, because nobody can build to an output with no definition of good.

**Read the clock.** Record minutes and seconds. Then show the SIPOC page: suppliers, inputs, process, outputs, customers, with a requirements column beside inputs and beside outputs, the trigger and end state above, the elapsed minutes below. Use the layout in packet-templates.md.

**Gate 2.**

> Anything wrong on this page? Fix it now; everything after this is built on it.

---

## Phase 3 — Decision inventory, one step at a time

For each step from Q3, in order. Say which step this is and how many remain.

**D-a. Actor and decision.**

> Step [N] of [total], [step name]. Who does it? And what do they decide while doing it? State the decision as a rule: "if X then Y". If they decide nothing, say "no decision". If they decide something but you cannot put it in words, say "cannot state it" and that is a real answer.

When the SME describes an approval or a meeting where the outcome is agreed by people in the room, record it as "cannot state it (decided in the room)" and say so in the echo, so the SME can object. A group decision is not a rule.

**D-b. Exceptions.**

> What goes wrong or arrives different at this step, and roughly how often for each? "Once a week", "one in fifty", "twice ever" all work.

If exceptions are named without a frequency, ask once: "Roughly how often, for each?" Take "not stated" only after that. The eval set gets one case per exception, and an exception with no frequency cannot be prioritized.

**D-c. Cost of wrong, and whether the owner would wear it.** Skip when D-a was "no decision" and D-b was "nothing". "Unknown" is a valid answer to either half.

> If this step comes out wrong and nobody catches it, what does it cost? Money, hours, a customer, a relationship, a compliance problem. Or "nothing much".

Then, when D-a stated a rule:

> Would the owner accept that happening now and then, if it meant this step ran without a person? Yes, no, or "only if...".

Record the second half as acceptable, not acceptable, conditional (with the condition), or unknown. This is the answer that decides whether the step can be an agent; the rules file will not infer it.

**D-d. What wrong looks like.**

> How would you know this step came out wrong? What would you see?

After the last step, draw the flowchart per mermaid-conventions.md and show it with the inventory table (packet-templates.md).

**Gate 3.**

> Does the map match how it actually runs? Anything drawn that does not happen, or anything that happens and is not drawn?

---

## Gates 4, 5, 6

Gate 4 is the classification card (classification-rules.md). Gate 5 is a one-line reconfirmation of the folder named at I-3, and it is the moment the packet is written. Gate 6 is the explicit yes before "Execute and build the agent" (execute-and-build.md). Nothing else is confirmed; answers are corrected through the echo at the top of the next question.

Read the clock at every gate when code execution is on, and write the time into run-log.md. "About 19:25" is what the first live run recorded because the clock was only read for the nine questions.
