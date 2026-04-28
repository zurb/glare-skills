---
name: glare-focus
description: Use this skill when the user is turning Glare design signals into directional clarity — the Focus facet. Triggers include benchmarking or comparing design versions ("v1 vs v2"), competitor reviews, segment analysis, journey-stage comparisons, platform/device comparisons, building baselines, normalizing UX metrics on a 100-point scale, identifying deltas, or interpreting whether a change actually improved outcomes vs just changed them. Also use when the user mentions Initiatives → Methods → Comparing → Decisions, the 10 comparison lenses (iteration, competitor, timeline, segment, journey, platform, user goals, feature usage, behavioral triggers, season), or the 5-step comparing process (Establish Baseline → Define Benchmark → Normalize → Identify Deltas → Interpret). Do NOT use when the user is still gathering raw findings (use `glare-measure`) or escalating outcomes to leadership/business KPIs (use `glare-lead`).
---

You are helping the user work through the **Focus** facet of Glare — turning design signals into directional clarity through structured benchmarking.

## Core idea

Focus moves teams from planning (**Initiatives**) and measuring (**Methods**) through structured benchmarking (**Comparing**) to acting on proof (**Decisions**). The discipline: use consistent UX metrics across versions, audiences, and competitors to determine whether design changes are actually *improving* outcomes, not just *changing* them.

## Read the reference first

Before answering substantive questions, read:

- `reference.md` — full compressed content of the Focus block, including the 10 Comparison Approaches, the 5-step Comparing process, the normalization rules (100-point scale: Comprehension, Satisfaction, Desirability, Completion, etc.), the delta-table format, and the worked Klean Kanteen / Hydro Flask competitive review example.

## How to apply

1. **Locate the user in the Focus sequence** — Initiatives (defining goals before signals), Methods (planning how to collect), Comparing (analyzing data), Decisions (acting on proof). Don't drift backward; Focus flows in order. Diagnose which bucket the conversation is actually in before answering.

2. **Initiatives — make "why this, why now?" measurable before any signal is collected.** Force both a User Need anchor and a Business Goal anchor, then produce: the **Goal / Outcome / Metric template** (intent + observable shift + 1–2 metrics from the 100-point stack with target delta + audience) and an explicit **kill criterion** (the signal that would end this Initiative). Lock version, date, and audience here so the downstream baseline is repeatable. For depth, hand off to `glare-focus-initiatives`.

3. **Methods — turn the Initiative into a repeatable collection plan.** Lock all **5 levers** explicitly (Cadence, Instruments, Sample Size, Audience recipe, Conditions) and apply the **sample-size rule** sized to detect the kill threshold (floor n=30 attitudinal, n=80–120 behavioral). Stack attitudinal + behavioral + performance, normalize at capture, and version M1 → M2 with a bridge round if any lever shifts. For depth, hand off to `glare-focus-methods`.

4. **Comparing — turn collected signals into proof.** Pick 4–5 of the 10 lenses (most common: Iteration, Competitor, Segment, Journey, Platform), then run the 5 steps: Baseline → Benchmark → **100-point normalization** → **Delta table** (Metric | Baseline | Current | Δ | Signal Interpretation) → Interpret. Tie each meaningful delta to a design decision and reframe the problem when warranted — the **Klean Kanteen reframe** ("new homepage" became "stronger emotional clarity and originality") is the model. For depth, hand off to `glare-focus-comparing`.

5. **Decisions — convert the benchmarked delta into one explicit move.** Require a signal reference as entry, then **pick exactly 1 of 5 moves** (Advance / Refine / Kill / Pivot / Reprioritize) against the criteria-by-delta table. Write the **Decision Record** (initiative ref, method version, signal ref, move, rationale, hand-off, owner+date) and state the **tradeoff** explicitly — what's given up, what's now locked vs flexible. Pivot/Kill spawns the next Initiative. For depth, hand off to `glare-focus-decisions`.

6. **Hand off to `glare-lead`** once the benchmark proves measurable impact and the conversation turns to business KPIs, ROI, or executive reporting.

## Handoffs
- Defining goals before signals → `glare-focus-initiatives`
- Planning how signals get collected → `glare-focus-methods`
- Running the comparison itself → `glare-focus-comparing`
- Acting on benchmarked proof → `glare-focus-decisions`
- Upstream signal collection → `glare-define`, `glare-measure`
- Executive ROI / business KPIs → `glare-lead`
