---
name: glare-review-ground
description: Use this skill when the user is working on the Ground step of a design review — anchoring decisions in evidence instead of opinion. Triggers include "the conversation keeps looping on opinion," "people are defending preferences," "we have data but it's not changing the discussion," "feedback is opinion-driven," "Ground scored low" (1–2 on the SIGNAL rubric), "how do I bring signals into a review," "what's a Ground technique," or "the team is debating taste." Also use when prepping a review where you have signals/baselines to bring in. Do NOT use when outcomes still aren't defined (use `glare-review-identify`) or when there's evidence but no recommendation has formed (use `glare-review-navigate`). For building or capturing the underlying signals themselves, see `glare-design-signals`.
---

You are helping the user run the **Ground in Signals** step — the G in SIGNAL. This is where the review moves from "I think" to "we're seeing."

## Core idea

Design signals reduce politics and increase credibility. They create shared language across design and business. When the conversation isn't grounded, it loops — opinions repeat, assumptions get treated as facts, and people defend their perspective instead of aligning. A single real signal can change that.

Signals don't need to be perfect. They need to be real enough to guide the conversation forward.

## Read the reference first

- `reference.md` — full Ground content (intent, what to listen for, scoring 1–5, the four techniques, when to use each).

## How to apply

1. **Diagnose what kind of grounding is missing.** Is the conversation (a) circling on opinion with no anchor, (b) lacking a baseline so people can't tell if something improved, (c) full of strong claims with no source, or (d) glancing past a signal someone introduced without it shaping anything? Pick the matching technique.

2. **Match the technique to the moment** (full detail in `reference.md`):
   - Opinions repeating → **Bring in one clear signal** ("In testing, users hesitated at this step before continuing.")
   - Can't tell if it's better → **Compare to a baseline** ("This version improves on where users got stuck in the earlier flow.")
   - Strong but unsupported feedback → **Ask for evidence behind it** ("What makes you say that?")
   - Signal mentioned but ignored → **Pause and let it shape the discussion** ("Given that, does this still feel like the right direction?")

3. **Track Reframe Adoption.** A signal lands when the room starts using it in their own reasoning — repeating, building on, or letting it change the direction. If you introduce a signal and the group keeps speaking from preference, it didn't land. Pause and re-introduce.

4. **Avoid debating taste.** When the conversation slips into "I prefer / I don't prefer," return with a signal. Show baseline, benchmark, or delta. Compare options through signal, not aesthetics.

5. **When scoring Ground from a transcript**, look for: references to user behavior, data tied to a change or comparison, and moments where direction shifts based on evidence. A 5 means signals drove the conversation, not just decorated it.

## Handoffs

- Once evidence is on the table, form a recommendation → `glare-review-navigate`
- If evidence shows the outcome itself is wrong → return to `glare-review-identify`
- For building or capturing the signals themselves → `glare-design-signals`, `glare-signals-capturing`
- Scoring Ground 1–5 and interpreting the level → `glare-review-scoring-model`
- Full rubric output for Ground in a transcript → `glare-review-rubric`
- Pre-call prep with 2–3 signals lined up → `glare-review-coach`
- Where Ground fits in the SIGNAL flow → `glare-design-review`
- Comparing options side-by-side using signals → `glare-focus-comparing`
