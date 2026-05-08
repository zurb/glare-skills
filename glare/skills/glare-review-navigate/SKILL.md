---
name: glare-review-navigate
description: Use this skill when the user is working on the Navigate step of a design review — leading the decision and securing commitment. Triggers include "we keep exploring without choosing," "the team won't make a recommendation," "we have signals but can't pick a direction," "ideas keep being treated equally," "Navigate scored low" (1–2 on the SIGNAL rubric), "how do I get to a decision in the room," "what's a Navigate technique," or "the call is almost over and direction is still soft." Also use when prepping a design review or decision meeting where you need to come in with a recommendation. Do NOT use when there's no evidence yet to support a direction (use `glare-review-ground`) or when a decision was made but ownership is unclear (use `glare-review-align`).
version: 1.3.0
source_doc_version: v1.3
last_rebuilt: 2026-05-04
---

You are helping the user run the **Navigate Decisions** step — the N in SIGNAL. This is where the conversation moves from open discussion to a clear path forward.

## Core idea

Direction without agreement creates rework. Decisions not secured in the room reopen later. By Navigate, the team has the problem, the outcome, and the signals — the goal is not to gather more input, it's to bring existing input together into a recommendation people can support.

You are making it easier for the right decision to form.

## Read the reference first

- `reference.md` — full Navigate content (intent, what to listen for, scoring 1–5, the four techniques, when to use each).

## How to apply

1. **Diagnose what's blocking the decision.** Is the room (a) staying open with no recommendation on the table, (b) hesitant after a recommendation because trade-offs are unclear, (c) treating too many options as equal, or (d) assuming agreement without checking? Pick the matching technique.

2. **Match the technique to the moment** (full detail in `reference.md`):
   - Conversation staying open → **State a clear recommendation** ("Based on what we've seen, we recommend moving forward with this approach.")
   - People hesitate → **Frame the tradeoffs** ("This simplifies the experience, but reduces flexibility here. That's the trade we're making.")
   - Too many ideas competing → **Narrow the options** ("Between these two directions, which better solves the problem we outlined?")
   - Agreement assumed → **Check for agreement** ("Does this direction make sense to move forward with?")

3. **Always come with a recommendation, not options alone.** "Based on [signal], we recommend [option] because [reason]. Should we proceed?" Options without a recommendation push the decision back to the room and stall the call.

4. **Track Decision Language.** When participants start using commitment verbs — decide, approve, move forward, commit, that's the direction — Navigate is landing. If the room agrees politely but no one uses decisive language, the direction is still soft.

5. **When scoring Navigate from a transcript**, look for: a clear recommendation made, tradeoffs acknowledged, movement toward a decision, explicit agreement. A 5 means a clear recommendation AND explicit agreement on the record.

## Handoffs

- Once a direction is set, clarify who owns it → `glare-review-align`
- If the team can't recommend because evidence is thin → `glare-review-ground`
- Scoring Navigate 1–5 and interpreting the level → `glare-review-scoring-model`
- Full rubric output for Navigate in a transcript → `glare-review-rubric`
- Pre-call prep that scripts the recommendation → `glare-review-coach`
- Where Navigate fits in the SIGNAL flow → `glare-design-review`
- Comparing options before recommending → `glare-focus-comparing`, `glare-focus-decisions`
