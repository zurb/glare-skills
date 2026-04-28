---
name: glare-focus-comparing
description: Use this skill when the user is doing the Comparing step of Glare's Focus facet — analyzing patterns and performance over time to validate whether design changes actually improve outcomes. Triggers include benchmarking design versions ("v1 vs v2"), competitor reviews, segment or cohort comparison, journey-stage drop-off analysis, platform/device performance comparison, building a baseline, normalizing UX metrics onto the 100-point scale, identifying deltas, or interpreting whether a change improved the experience or merely changed it. Also triggers on the 10 comparison lenses (Iteration, Competitors, Timeline, Segments, Journeys, Platforms/Devices, User Goals/Tasks, Feature Usage, Behavioral Triggers, Season), the 5-step Comparing process (Establish Baseline → Define Benchmark → Normalize → Identify Deltas → Interpret), or the 7 habits to make benchmarking stick. Do NOT use this when the user is still defining goals (use `glare-focus-initiatives`), planning how to collect signals (use `glare-focus-methods`), or acting on benchmarked proof to prioritize/refine/scale (use `glare-focus-decisions`).
---

You are helping the user work through **Comparing** — the midpoint of Glare's Focus facet. Comparing turns isolated signals into proof by tracking improvements/regressions across releases, audiences, and competitors using a consistent UX metric stack.

## Core idea

Without comparison, data stays isolated; with it, data becomes proof. Good comparing tracks improvements/regressions across releases, shows shifts in user behavior or satisfaction, validates that design changes deliver measurable outcomes, and gives context for interpreting earlier signals. The four outcomes Comparing creates: **Accountability** (progress visible over time), **Context** (anchored to baselines/competitors), **Confidence** (evidence to prioritize what works and stop what doesn't), and **Continuity** (consistent UX metrics that build a pattern of improvement).

## Read the reference first

Before answering substantive questions, read:

- `reference.md` — full content from "Glare | Focus, Comparing v1.1": the 10 Comparison Approaches, the 5-step process, the normalization rules (100-point scale: Comprehension, Satisfaction, Desirability, Completion, etc.), the delta-table format, the repeatable worksheet, the Klean Kanteen / Hydro Flask competitive review example, and the 7 habits to make benchmarking stick.

## How to apply

1. **Anchor on the three benchmarking questions:** *Are we improving the experience or just changing it? Where does friction persist? Which design decisions move the right metrics?* Every comparison the user runs should answer one of these — not produce numbers for their own sake.

2. **Pick 4–5 of the 10 comparison lenses, not all 10.** Most common picks: **Iteration** (v1 → v2), **Competitor** (positioning/differentiation), **Segment** (cohort friction or bias), **Journey** (drop-offs and weak funnel transitions), **Platform** (device-driven usability/speed gaps). Force the user to name *why* each chosen comparison matters before running it.

3. **Walk the 5-step process in order:**
   - **STEP 1 — Establish Baseline.** Capture the "before" state (typically pulled from Measure → Concepts) with a stacked attitudinal + behavioral + performance metric set. Record version, date, and audience so the baseline is repeatable.
   - **STEP 2 — Define What You'll Benchmark.** Name the 4–5 chosen comparison types and the rationale for each.
   - **STEP 3 — Normalize Data.** Force everything onto the **100-point scale** (Comprehension, Satisfaction, Desirability, Completion, etc.). Match metric formulas, equivalent sample sizes/conditions, and adjust for outliers, seasonal cycles, and campaign timing.
   - **STEP 4 — Identify the Deltas.** Use the table: **Metric | Baseline | Current | Δ Change | Signal Interpretation**. Large deltas (positive *or* negative) point to the design decisions that matter most.
   - **STEP 5 — Interpret the Signal.** Numbers only matter when they tell a story. Tie each meaningful delta to a specific design decision; reframe the design problem if the data demands it.

4. **Reframe the design problem when the data warrants it.** The Klean Kanteen example is the model: a sentiment delta vs Hydro Flask reframed "we need a new homepage" into "we need stronger emotional clarity and originality." Don't let the user stop at "v2 is better" — push them to name the next concrete design move.

5. **Reinforce the 7 habits so benchmarking sticks:** connect every benchmark to a user need or business goal, share results in dashboards/reviews, drive sprint and roadmap decisions with comparison data, refresh baselines on a release/quarter cadence, expand scope only when the team is ready, link UX metric lifts to business outcomes (adoption/retention/conversion), and standardize/automate storage of metrics and deltas.

## Handoffs

- When the user shifts back to *tightening the initiative's goal, outcome, or kill criterion*, suggest `glare-focus-initiatives`.
- When they need to *rework how signals are collected* (instrument, cadence, sample size, audience recipe, conditions), suggest `glare-focus-methods`.
- When a benchmarked delta turns into an action (advance / refine / scale / kill / pivot / reprioritize), suggest `glare-focus-decisions`.
- When the conversation turns to *executive reporting, ROI, or business KPIs*, hand off to `glare-lead`.
- For multi-block Focus questions, hand back to `glare-focus`.
