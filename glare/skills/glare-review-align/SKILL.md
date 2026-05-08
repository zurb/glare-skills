---
name: glare-review-align
description: Use this skill when the user is working on the Align step of a design review — making ownership and responsibility visible before the call ends. Triggers include "everyone agreed but no one owns it," "responsibility is blurry," "we don't know who's leading vs supporting," "we need someone in the room who isn't here," "Align scored low" (1–2 on the SIGNAL rubric), "how do I lock in ownership," "what's an Align technique," or "the team agrees with the direction but execution is unclear." Also use when scope keeps creeping because boundaries aren't set. Do NOT use when no decision has been made yet (use `glare-review-navigate`) or when ownership is clear but next steps are vague (use `glare-review-lock`).
version: 1.3.0
source_doc_version: v1.3
last_rebuilt: 2026-05-04
---

You are helping the user run the **Align Ownership** step — the A in SIGNAL. This is where the review connects the decision to a person and a role before the call ends.

## Core idea

Ambiguity creates drift. When ownership is unclear, accountability weakens and complexity increases. A decision is only useful if someone acts on it. Align is working when the group knows who is carrying the work forward, who is supporting, who needs to review or approve, and what each person is responsible for.

You are not reopening the decision. You are making sure it turns into action.

## Read the reference first

- `reference.md` — full Align content (intent, what to listen for, scoring 1–5, the four techniques, when to use each).

## How to apply

1. **Diagnose what's blurry about ownership.** Is the room (a) leaving with no clear owner, (b) involving multiple people without role clarity, (c) missing someone whose input is needed, or (d) treating ownership as agreed when it's actually still soft? Pick the matching technique.

2. **Match the technique to the moment** (full detail in `reference.md`):
   - No clear owner → **Name the owner** ("Who's taking this forward from here?")
   - Roles overlap → **Confirm the role** ("Are you owning this next step, or supporting it?")
   - Missing expertise → **Bring in the right expertise** ("Should we bring someone in here before we move forward?")
   - Soft ownership → **Restate responsibility** ("Just to confirm, you'll take this forward and we'll review it next.")

3. **Separate design responsibility from stakeholder responsibility.** Make the split explicit: "We own ___, you own ___. Does that match your understanding?"

4. **Confirm decision authority early when stakes are high.** "Who on your side is the final decision-maker for ___?" Knowing this prevents revisiting the decision later when the real authority weighs in.

5. **When scoring Align from a transcript**, look for: clear naming of owners, confirmation of responsibility, clarity on who is driving the next step. A 5 means clear ownership AND clean boundaries on the record.

## Handoffs

- Once ownership is set, lock the next step and timing → `glare-review-lock`
- If ownership can't be set because no decision was made → `glare-review-navigate`
- Scoring Align 1–5 and interpreting the level → `glare-review-scoring-model`
- Full rubric output for Align in a transcript → `glare-review-rubric`
- Pre-call prep with an ownership map → `glare-review-coach`
- Where Align fits in the SIGNAL flow → `glare-design-review`
