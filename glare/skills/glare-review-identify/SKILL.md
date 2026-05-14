---
name: glare-review-identify
description: Use this skill when the user is working on the Identify step of a design review — defining what "better" means in measurable terms, turning vague feedback into a clear outcome, or aligning the room on what success looks like. Triggers include "feedback is all preference," "people keep saying 'better' or 'cleaner' without defining it," "the team can't pick a direction because success is unclear," "we're talking about deliverables instead of outcomes," "Identify scored low" (1–2 on the SIGNAL rubric), "how do I get the room aligned on a goal," or "what's an Identify technique." Also use when prepping a review where you need an outcome statement up front. Do NOT use when the problem itself is still unclear (use `glare-review-surface`) or when the outcome is clear but the team is debating opinion (use `glare-review-ground`).
version: 3.1.0
source_doc_version: v1.3
last_rebuilt: 2026-05-13
---

You are helping the user run the **Identify Outcomes** step — the I in SIGNAL. This is where the review defines what success looks like before reacting to feedback.

## Core idea

Without clarity about outcomes, stakeholders critique artifacts. They share opinions but those opinions don't point to the same goal. Identify is working when the group can say in plain language what should improve, who it should improve for, what the user should be able to do, and how the team will know the direction is working.

You are not solving everything yet. You are giving the conversation a clear target.

## Read the reference first

- `reference.md` — full Identify content (intent, what to listen for, scoring 1–5, the four techniques, when to use each).

## How to apply

1. **Diagnose what's missing in this review's outcome.** Is the room (a) not agreeing on what success looks like, (b) generating long suggestion lists with no goal, (c) responding to broad questions with broad feedback, or (d) trying to chase too many goals at once? Pick the technique that matches.

2. **Match the technique to the moment** (full detail in `reference.md`):
   - Success is unclear → **Define what success looks like** ("If this works, users should move through this step without hesitation.")
   - Scattered suggestions → **Turn feedback into an outcome** ("So the goal here is to make this easier to understand at first glance?")
   - Broad feedback → **Ask targeted questions** ("Does this interaction make sense on mobile?")
   - Too many priorities → **Align on a single priority** ("What's the one thing we need to get right here?")

3. **Always separate user outcome from business outcome.** "If we do this perfectly, what happens for your users? And what happens for the business?" Both should live in one sentence each.

4. **Confirm agreement explicitly.** Identify isn't done until someone in the room repeats the outcome back. Track adoption — when participants restate or build on the outcome, it's locked.

5. **When scoring Identify from a transcript**, look for: clear statements of what should improve; connections between user behavior and business impact; explicit agreement on success. A 5 means a measurable outcome was agreed on the record.

## Handoffs

- Once outcomes are clear, anchor the discussion in evidence → `glare-review-ground`
- If outcomes can't be defined because the problem isn't clear → `glare-review-surface`
- Scoring Identify 1–5 and interpreting the level → `glare-review-scoring-model`
- Full rubric output for Identify in a transcript → `glare-review-rubric`
- Pre-call prep with an outcome statement written in advance → `glare-review-coach`
- Where Identify fits in the SIGNAL flow → `glare-design-review`
- Picking the user need that anchors the outcome → `glare-define-user-needs`
- Picking the UX metric that makes the outcome measurable → `glare-define-ux-metrics`
