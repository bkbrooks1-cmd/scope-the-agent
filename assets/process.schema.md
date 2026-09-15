# process.json — the shape

The structured record the skill writes after gate 3 and the validator reads. Plain JSON, one object. A reader can hand-write one from the worksheet and run the validator on it.

```json
{
  "process": "Wholesale order fulfillment",
  "date": "2026-09-15",
  "skill_version": "1.0.0",
  "owner": "Owner",
  "cost_today": "About 6 hours a week across two people",
  "if_nothing_changes": "Orders keep slipping in the holiday weeks",
  "trigger": "Order email arrives from a wholesale customer",
  "end_state": "Order released to delivery and invoice sent",
  "steps": [
    {
      "n": 1,
      "name": "Log the order",
      "actor": "Order desk",
      "decision": false,
      "rule": null,
      "rule_stated": null,
      "exceptions": [
        { "what": "Order arrives by phone instead of email", "frequency": "once a week" }
      ],
      "cost_of_wrong": "n/a",
      "wrong_acceptable": "n/a",
      "wrong_looks_like": "Order missing from the sheet on bake day"
    },
    {
      "n": 4,
      "name": "Decide batch order",
      "actor": "Baker",
      "decision": true,
      "rule": null,
      "rule_stated": false,
      "exceptions": [],
      "cost_of_wrong": "A late order, maybe a lost account",
      "wrong_acceptable": "not acceptable",
      "wrong_looks_like": "Two orders finish after their delivery slot"
    }
  ],
  "outputs": [
    {
      "name": "Packed order",
      "customer": "Wholesale customer",
      "requirements": [
        { "text": "Delivered by 7am on the agreed date", "status": "current" },
        { "text": "Item count matches the confirmation email", "status": "proposed" }
      ]
    }
  ],
  "inputs": [
    {
      "name": "Order email",
      "supplier": "Wholesale customer",
      "requirements": [
        { "text": "Names each product, quantity, and delivery date", "status": "current" }
      ]
    }
  ]
}
```

## Fields

| Field | Type | Meaning |
|---|---|---|
| `process` | string | I-2, the name the team uses |
| `date` | string | YYYY-MM-DD |
| `skill_version` | string | From SKILL.md frontmatter |
| `owner` | string | V-4. Never empty; the skill stops before this file exists if nobody owns it |
| `cost_today`, `if_nothing_changes` | string | V-2, V-3. "unmeasured" is a valid value |
| `trigger`, `end_state` | string | Q1 (earlier trigger if found), Q2 |
| `steps[]` | array | Q3 order. 3 to 7 entries; the validator warns under 5 and fails over 7 |
| `steps[].decision` | boolean | true when D-a described a decision, stated or not |
| `steps[].rule` | string or null | The rule verbatim when stated |
| `steps[].rule_stated` | boolean or null | false when D-a said "cannot state it"; null when there is no decision |
| `steps[].exceptions[]` | array of {what, frequency} | D-b. Empty array when none |
| `steps[].cost_of_wrong` | string | D-c first half, "unknown" when the SME could not say, or "n/a" when skipped |
| `steps[].wrong_acceptable` | string | D-c second half: "acceptable", "not acceptable", "conditional: <condition>", "unknown", or "n/a" when no rule was stated. Only "acceptable" or "conditional" can make a step an agent |
| `steps[].wrong_looks_like` | string | D-d |
| `outputs[]` | array | Q4. Each needs a `customer` (Q5) and at least one requirement (Q6) |
| `inputs[]` | array | Q7. Each needs a `supplier` (Q8) and at least one requirement (Q9), or `"requirements": "accepted as-is"` |
| `requirements[].status` | "current" or "proposed" | "proposed" when the SME stated what they would check rather than what is checked |

## Manual check, when the validator cannot run

Answer these five by reading the file:

1. Are there 3 to 7 steps? Over 7 is two processes.
2. Does every output have at least one requirement a person could check by looking?
3. Does every input have a supplier, and either a requirement or the words "accepted as-is"?
4. Does every step have an actor?
5. For every step with `"decision": true`, is there either a `rule` or `"rule_stated": false`? And for every step with a `rule`, is `wrong_acceptable` filled in (not "n/a")?

Any no is a finding. Record findings in run-log.md.
