---
name: review-scoring-model
description: Use this skill when the user wants the SIGNAL scoring rubric itself — the 1–5 scale per dimension, the score bands /30, the calibration rules, and how to interpret the result. Triggers include "how do I score a design review," "what does a 3 mean for Surface," "what's a Leading score," "score bands," "SIGNAL rubric calibration," "how do I know where to improve from a score," or "explain the 1–5 scale." Also use when the user has scores and wants to interpret them ("we scored 17/30 — what does that mean?"). Do NOT use when the user wants to actually evaluate a transcript end-to-end with observations and behavioral metrics — use `glare:review-rubric` for that. Do NOT use for in-the-moment techniques — use `glare:review-techniques` and the dimension skills.
version: 3.1.0
source_doc_version: v1.3
last_rebuilt: 2026-05-13
---

You are helping the user use the **SIGNAL Scoring Model** — the 1–5 scale for evaluating each part of a design review.

## Core idea

Each part of SIGNAL is scored from 1 to 5 based on two things: how clearly the step showed up, and how much it shaped the direction of the call. The total is /30. **The goal is not to get a perfect score — it's to see how the conversation held together and where the team can improve the next review.**

Patterns across the six sections matter more than the total. Look for the step where clarity first dropped — that's usually the best place to improve.

## Read the reference first

- `reference.md` — full scoring content (per-dimension 1–5 tables, score bands /30, calibration rules, behavioral metrics, what the score should produce).

## How to apply

1. **Set the calibration up front.** 3 is the most common score. Reserve 5 for truly exceptional and 1 for clear failures. Score each dimension independently — don't let one part bleed into others.

2. **Use the section scales** (full text in `reference.md`):
   - **5 Leading** — clear, consistent, actively shapes how the group thinks and decides
   - **4 Strong** — clear and influences direction, with minor gaps
   - **3 Functional** — present and working, but not shaping the conversation meaningfully
   - **2 Emerging** — shows up briefly but does not influence direction
   - **1 Reactive** — mostly absent

3. **Interpret the total /30 with bands:**
   - 25–30 Leading — strong clarity across the full decision flow
   - 19–24 Advancing — worked well overall, a few gaps softened clarity or momentum
   - 13–18 Functional — useful moments, but several steps were weak or underdeveloped
   - 6–12 Reactive — lacked structure, decisions unclear or not secured

4. **Find the first weak point** in the SIGNAL flow. That's usually where the next improvement should happen. The first weak letter cascades — fixing it lifts everything downstream.

5. **Tie scores to behavioral signals** (Talk Time, Problem Ownership, Decision Language, Reframe Adoption, Closing Clarity). These don't get scored, but they explain *why* a section scored high or low.

## Output the score should produce

A scored review should give the team more than a number. It should produce: total score, score band, section scores, short summary of the call pattern, where clarity first dropped, strengths to keep, weak points to improve, and the **primary improvement** for the next call.

## Handoffs

- Full evaluation including observations, quotes, and behavioral metrics → `glare:review-rubric`
- The actual end-to-end transcript workflow → `glare:review-run-transcript`
- Per-dimension scoring tables and what each level looks like → `glare:review-surface`, `glare:review-identify`, `glare:review-ground`, `glare:review-navigate`, `glare:review-align`, `glare:review-lock`
- Coaching once you have scores → `glare:review-coach`
- Where this fits in Design Review → `glare:design-review`
