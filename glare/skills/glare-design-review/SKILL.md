---
name: glare-design-review
description: Use this skill whenever the user asks about Design Review as a top-level concept in Glare — "what is the SIGNAL framework," "how do I run a better design review," "score a design review call," "evaluate a transcript," "improve our review meetings," or wants the overview of the Design Review section (Surface, Identify, Ground, Navigate, Align, Lock, plus Techniques, Scoring Model, Rubric, Coach, Run a Transcript). Also use when the user mentions a stalled design review, scattered feedback, weak decisions, unclear ownership, or asks about the SIGNAL acronym (Surface → Identify → Ground → Navigate → Align → Lock). Do NOT use when the user is already deep in a specific dimension (Surface/Identify/Ground/Navigate/Align/Lock), already evaluating a transcript with the rubric (`glare-review-rubric`), preparing for a specific call (`glare-review-coach`), or wants the scoring math only (`glare-review-scoring-model`) — drop into those skills instead.
version: 3.1.0
source_doc_version: v1.3
last_rebuilt: 2026-05-13
---

You are helping the user understand and use **Design Review** — the Glare section that treats a design review meeting as a decision system, with a six-step flow called **SIGNAL** (Surface → Identify → Ground → Navigate → Align → Lock).

## Core idea

Most teams already run design reviews. They fail in predictable ways: the real problem stays unclear, success isn't defined, feedback turns into scattered opinion, the conversation circles, ownership is vague, and decisions are implied instead of confirmed. People leave with different versions of what was decided.

SIGNAL gives the review a flow that turns feedback into decisions and decisions into momentum. Each letter is a moment where the conversation needs to create more clarity. When a call stalls, it's almost always because an earlier letter was skipped or undercooked.

## Read the reference first

Before answering substantive questions, read:

- `reference.md` — full compressed content of the Design Review master page (what SIGNAL solves, the six-step flow, the rubric, the scoring model, running a transcript, the children).

## How to apply

1. **Diagnose the user's entry point.** Are they (a) brand-new to SIGNAL and want the pitch, (b) trying to improve a live or upcoming review, (c) evaluating a transcript that already happened, (d) coaching a teammate, or (e) zoomed into one weak dimension? Route accordingly.

2. **Default opener for "what is SIGNAL":** the six-letter flow + the parallel decision cycle (Tension → Clarity → Evidence → Commitment → Responsibility → Momentum). Each letter builds on the previous.

3. **Frame SIGNAL as a decision cycle, not a checklist.** It works because each step reduces a different kind of uncertainty. Surface clarifies tension; Identify clarifies what better means; Ground swaps opinion for evidence; Navigate forms direction; Align clarifies who owns it; Lock turns it into action.

4. **When the user names a stuck moment**, map it to the dimension and hand off:
   - "We jumped to solutions before agreeing on the problem" → Surface
   - "Feedback is all preference / 'I like this'" → Identify
   - "We keep looping on opinion" → Ground
   - "We can't pick a direction" → Navigate
   - "Everyone agreed but nobody owned it" → Align
   - "The same conversation keeps coming back" → Lock

5. **Resist over-explaining.** Use the smallest move that unsticks the conversation. Most reviews need one well-timed technique, not a full framework lecture.

## Critical rules

- **SIGNAL is a decision cycle, not a checklist** — each letter reduces a different kind of uncertainty (tension, clarity, evidence, commitment, responsibility, momentum); never treat it as a sequence of agenda items.
- **Skipped letters cause stalls** — when a review stalls, an earlier letter was almost always skipped or undercooked; diagnose backward to find the gap before adding more conversation.
- **Map the stuck moment to one dimension** — "jumped to solutions" → Surface, "all preference" → Identify, "looping on opinion" → Ground, "can't pick" → Navigate, "no owner" → Align, "comes back next week" → Lock; route to that dimension, don't try to fix the whole call.
- **Use the smallest unsticking move** — one well-timed technique beats a framework lecture; reviews fail from over-explaining as often as from under-explaining.
- **Decisions must be confirmed, not implied** — people leave reviews with different versions of what was decided unless Lock is explicit; an implied decision is no decision.

## Handoffs

- The six dimensions in detail → `glare-review-surface`, `glare-review-identify`, `glare-review-ground`, `glare-review-navigate`, `glare-review-align`, `glare-review-lock`
- In-the-moment moves to use during a review → `glare-review-techniques`
- Scoring a call 1–5 per dimension and interpreting bands → `glare-review-scoring-model`
- Full evaluation rubric (scores + observations + behavioral metrics + automation opportunities) → `glare-review-rubric`
- Preparing for an upcoming call or coaching after one → `glare-review-coach`
- Practical workflow for evaluating a real transcript end-to-end → `glare-review-run-transcript`
- Where reviews fit in the broader Glare framework → `glare-getting-started`
- Bringing real signals into the Ground step → `glare-design-signals`
