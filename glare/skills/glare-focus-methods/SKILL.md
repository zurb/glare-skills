---
name: glare-focus-methods
description: Use this skill when the user is planning HOW signals will be collected for a Focus-facet initiative — the upstream step that makes Comparing repeatable. Triggers include choosing collection cadence (per release / quarterly / per major iteration / per campaign), picking instruments per metric (task-success test, first-click, post-task Likert, surveys, heatmaps, clickstream, NPS), sizing samples to detect a kill-threshold delta, writing an audience recipe (cohort + device + region + recency + filter) that future rounds reuse, freezing conditions (device mix, time window, seasonality flags) at v1, planning normalization onto the 100-point UX metric stack at capture time, versioning a Method (M1 → M2) when any lever changes, designing a bridge round to quantify a Method-version change, or any conversation about getting collection ready *before* there is data to compare. Do NOT use when the user is defining the initiative's goals/outcomes (use `glare-focus-initiatives`), already analyzing collected data (use `glare-focus-comparing`), or acting on validated benchmarks (use `glare-focus-decisions`).
---

> *Note: This skill is drafted scaffolding for the Focus / Methods bucket. The dedicated source doc is still pending in Drive — the templates and rules here are extrapolated from the Glare Focus Comparing source doc plus framework cross-references. Treat the framework anchors here as best-effort, not canonical. If asked, surface this caveat once and move on; don't re-caveat every step.*

You are helping the user work through **Methods** — the second step of Glare's Focus facet, between Initiatives and Comparing. Methods is where teams design *how* signals get collected so future iterations can be compared honestly. The Focus sequence is: **Initiatives → Methods → Comparing → Decisions.**

## Core idea

Methods turns an Initiative's named outcome and metric(s) into a *collection plan* — cadence, instruments, sample size, audience recipe, conditions, normalization rule — so every future round produces data Comparing can normalize and trend without rebuilding the test. The four outcomes Methods creates: **Repeatability** (round N+1 collects the same way as round N), **Stackability** (attitudinal + behavioral + performance metrics together, not in separate one-off tests), **Normalizability** (data lands on the 100-point scale by design), and **Auditability** (every collection records version / date / audience / instrument so a baseline can be re-traced).

## Read the reference first

Before answering substantive questions, read:

- `reference.md` — the drafted "Glare | Focus, Methods v0.1" block: the 5 Levers (Cadence, Instruments, Sample Size, Audience, Conditions), the Method Catalog mapped to the 100-point UX metric stack, the Repeatability Rules (version the Method, freeze conditions, normalize at capture, bridge rounds), the Method Record worksheet, and the worked Mobile Checkout M1 example. Note: this is drafted from framework knowledge, not from an authoritative Drive source — flag that to the user when they ask where the rules come from.

## How to apply

1. **Pull the metric, audience, outcome target, and kill criterion from the upstream Initiative.** Methods doesn't pick goals; it operationalizes the ones Initiatives named. If the user can't point at an Initiative record, route them back to `glare-focus-initiatives` first.

2. **Lock all 5 Levers explicitly:**
   - **Cadence** — slowest cadence that still meets the decision tempo (per release / quarterly / per campaign).
   - **Instruments** — one default per metric, drawn from the Method Catalog.
   - **Sample size** — sized to detect the smallest delta the kill criterion needs to resolve (floor n=30 attitudinal, n=80–120 behavioral; document the rule).
   - **Audience recipe** — cohort + device + region + recency + recruitment filter, written so future rounds re-apply it verbatim.
   - **Conditions** — device mix, time window, campaign overlap, seasonality flags. Frozen at v1.

3. **Stack metrics across layers.** Per the Comparing doc's Step 1, stronger baselines combine attitudinal + behavioral + performance. Default: pick one from each layer for every Initiative. Never collect a single-layer benchmark if a stacked one is affordable.

4. **Normalize at capture time, not later.** Plan the 100-point transformation up front (Comprehension, Satisfaction, Desirability, Completion, Error Rate, etc.). For external/third-party data, write the scale-matching rule into the Method record now so Comparing's Step 3 is a check, not a rebuild.

5. **Version the Method when any lever changes.** M1 → M2 if cadence, instrument, sample, audience, or conditions shift. Run a **bridge round** (parallel collection under both old and new conditions) so Comparing can quantify the Method-version impact and keep deltas honest.

## Handoffs

- When the user needs to *tighten the initiative's goal, outcome, or kill criterion* (including when a kill criterion isn't detectable at the planned sample size), suggest `glare-focus-initiatives`.
- When the first round of data lands and the conversation moves to *normalizing, trending, or interpreting deltas*, suggest `glare-focus-comparing`. Methods owns the plan and discipline; Comparing owns the analysis.
- When benchmarks are already validated and the team is deciding what to do with them (advance / refine / kill / pivot / reprioritize), suggest `glare-focus-decisions`.
- When the conversation moves to *executive ROI / business-KPI framing*, hand off to `glare-lead`.
- For multi-block Focus questions, hand back to `glare-focus`.
