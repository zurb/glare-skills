---
name: glare-review-rubric
description: Use this skill when the user wants to evaluate a design review or client call using the full SIGNAL rubric — scoring call quality, diagnosing where conversations broke down, and producing a structured evaluation report. Triggers include pasting a call transcript, asking to review or score a call, requesting a SIGNAL evaluation, asking about call quality, wanting to understand what went wrong on a specific call, or asking for the rubric output. Also use when the user mentions Surface/Identify/Ground/Navigate/Align/Lock dimensions, talk time ratio, problem ownership, decision language, or reframe adoption together. Do NOT use when the user wants to prepare for an upcoming call or coach someone on behavioral improvements — use `glare-review-coach` instead. Do NOT use for internal standups, async Slack/email threads, or purely informational calls where no decisions were being made.
---

Evaluate a design review or client call using the full SIGNAL rubric. This is a lightweight offline version of the Call Rubric tool in the Glare Playground / Ray app — same definitions, same scoring, no app required.

This is not just a scorecard. It diagnoses where conversations broke down, why it matters, and what to do differently next time.

## Read the reference first

- `reference.md` — full rubric (inputs, dimension definitions, scoring tables, behavioral metric definitions, exact output structure with examples, scoring calibration, common issues).

## When to use

- After any design review or client call (paste transcript)
- When a project feels stalled or unclear and you want to trace it back to a conversation
- For coaching call performance with a team member
- Quick evaluation when you don't have the Glare Playground / Ray app open

## When NOT to use

- Internal standups or team syncs (no decision cycle to evaluate)
- Async Slack/email threads (SIGNAL evaluates live conversation dynamics)
- Calls where no decisions were being made (purely informational)
- When you need historical tracking across calls (use the Glare Ray app instead)

## Inputs

- Call transcript (full text, speaker-attributed)
- Optional: identify speakers as "us" (team) vs "client" / stakeholder

If speakers aren't identified, ask before guessing — misattribution breaks the behavioral metrics.

## How to apply

1. **Confirm transcript quality first.** If under ~500 words: say so, give observations without numeric scores. If one-sided (only one party captured): note the limitation, score what's observable. If speakers aren't tagged: ask before guessing.

2. **Score each dimension independently** using the per-letter rubric in `reference.md`. 3 is the most common score. Reserve 5 for truly exceptional, 1 for clear failures. Every claim must be anchored to a verbatim quote.

3. **Extract the four behavioral metrics:**
   - **Talk Time Ratio** — word count split between team and client
   - **Problem Ownership** (client only) — count + level + 2–3 quotes + interpretation
   - **Decision Language** (client only) — count + tone + 2–3 quotes + interpretation
   - **Reframe Adoption** — count + rate + each reframe with adopted/not + interpretation

4. **Use the exact output structure** from `reference.md`. Open with Summary, then S → I → G → N → A → L (each: prose intro → Key Observations → "Why this isn't a 5"), then Behavioral Metrics, then Strengths / Improvement Areas / Primary Improvement, then Automation Opportunities.

5. **Goal:** improve how the next call is run, not just rate the last one.

## Output structure (high level)

1. Summary (total /30, band, pattern headline, SIGNAL flow assessment)
2. Six dimension evaluations (S → I → G → N → A → L) — each has prose intro, Key Observations as bold-title + verbatim blockquote, and "Why this isn't a 5"
3. Behavioral Metrics (talk time, problem ownership, decision language, reframe adoption)
4. Strengths (2–4)
5. Improvement Areas (2–4)
6. Primary Improvement (the single most important change for next call)
7. Automation Opportunities (3 specific moments that could be automated with Glare Blocks)

## Critical rules (from `reference.md`)

- Every dimension MUST include at least one direct quote
- 1–3 quotes per dimension max
- Do not invent or paraphrase quotes
- If no quote supports a dimension: "No direct evidence found in transcript."
- Blockquote attribution MUST use a real speaker name
- Each Key Observation = bold title + verbatim blockquote, NO description paragraph after
- Include both what went RIGHT and what went WRONG
- Close each dimension with "Why this isn't a 5" (or "Why this is a [score]" for scores below 3)

## Handoffs

- Just the scoring scale + bands + calibration → `glare-review-scoring-model`
- Practical end-to-end transcript workflow (3 paths: Skill, Prompt, Ray app) → `glare-review-run-transcript`
- Coaching after the rubric — what to change behaviorally → `glare-review-coach`
- Per-dimension techniques to fix the weak letter → `glare-review-surface`, `glare-review-identify`, `glare-review-ground`, `glare-review-navigate`, `glare-review-align`, `glare-review-lock`
- Where this fits in the framework → `glare-design-review`
