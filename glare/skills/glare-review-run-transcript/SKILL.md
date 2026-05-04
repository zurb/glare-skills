---
name: glare-review-run-transcript
description: Use this skill when the user wants the practical workflow for evaluating a real design review transcript end-to-end. Triggers include "I have a transcript — what do I do with it," "how do I run a transcript through SIGNAL," "what do I need before scoring a call," "what tool should I use to evaluate a call (Skill / Prompt / Ray)," "what does the SIGNAL output look like," or "walk me through evaluating a recorded review." Also use when the user is choosing between the offline Skill, the AI prompt, and the Ray app, or asking how to interpret the output of any of those. Do NOT use when they just want the scoring rubric → `glare-review-rubric` or `glare-review-scoring-model`. Do NOT use for prepping an upcoming call → `glare-review-coach`.
---

You are helping the user **run a design review transcript** through SIGNAL — the practical end-to-end workflow.

## Core idea

Most teams run design reviews, but few have a consistent way to learn from them. After a call, people leave with different versions of what happened. Running a transcript makes that visible — it turns a conversation into something the team can review, score, and improve. You're looking at how the conversation worked, where it held together, and where it lost strength.

This helps improve the next review, not just evaluate the last one.

## Read the reference first

- `reference.md` — full workflow content (what you need before starting, how the transcript is reviewed, the three paths Skill/Prompt/Ray, what the output should produce, how to use the results).

## How to apply

1. **Confirm transcript readiness.** A good transcript has speaker names, the full discussion, the design problem being reviewed, any signals/data/feedback mentioned, and the closing conversation around ownership and next steps. You don't need a perfect transcript — just enough of the conversation to see how the review moved from problem to action.

2. **Pick the path that matches their goal:**
   - **Use the Skill** (this skill family — `glare-review-rubric`) — fast, repeatable, AI-driven analysis. Best when you want quick analysis, consistent output, repeatable results across multiple calls.
   - **Use the AI Prompt** — guided manual run-through with an AI tool. Best for learning the SIGNAL system more deeply, training your thinking, reviewing an important call manually.
   - **Use the Ray Application** — Glare's app for uploading transcripts and tracking patterns across calls. Best for team-level insight, ongoing review, consistent evaluation across projects.

3. **Walk through the SIGNAL flow** on the transcript:
   - Surface: Was the real problem made clear?
   - Identify: Did the group define what success should look like?
   - Ground: Were signals used to shape the discussion?
   - Navigate: Did a clear direction start to form?
   - Align: Was ownership made clear?
   - Lock: Were next steps confirmed?

4. **Find the first weak point.** Once the transcript is reviewed, look for the step where clarity first dropped. That's usually where the next improvement should happen. Map the weakness to a fix:
   - Surface weak → clarify the real problem earlier
   - Identify weak → define success before debating the design
   - Ground weak → bring stronger signals into the review
   - Navigate weak → make tradeoffs and recommendations clearer
   - Align weak → confirm who owns the next move
   - Lock weak → close with clearer actions and timing

5. **You don't need every call to be perfect.** You need a clear read on where the conversation lost strength and what to improve next.

## Output the review should produce

- how each SIGNAL step showed up
- where the conversation created clarity
- where the review lost strength
- how decisions formed
- what weak point needs attention next
- what to improve in the next review

## Handoffs

- The actual rubric that produces the scored output → `glare-review-rubric`
- Just the 1–5 scoring scale + bands → `glare-review-scoring-model`
- After getting results, prep the next call or coach behavior → `glare-review-coach`
- After getting results, pick techniques to improve the weak letter → `glare-review-techniques` and per-dimension skills
- Where transcript review fits in the framework → `glare-design-review`
