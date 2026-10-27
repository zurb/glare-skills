---
name: define-ux-metrics
description: Use this skill when the user is in the UX Metrics block of the Define area — picking the numbers that prove design worked for a specific decision. Triggers — choosing Attitudinal / Behavioral / Performance / Intelligence metrics; the four lenses (By Type, By Stage, By Time, By Engagement); leading vs lagging indicators; predictive / proxy / analytics stages; the four comparison filters (Vanity vs Actionable, Qualitative vs Quantitative, Exploratory vs Reporting, Correlated vs Causal); the four quality principles (Easy to Understand, Good for Comparison, Use Rates or Ratios, Focus on Behavior); mismatches like "high satisfaction + low completion"; capturing leading indicators in Helio. Do NOT use when naming the need (use `glare:define-user-needs`) or picking instruments (use `glare:define-collecting`). For the broader UX Metrics framework, AI / Intelligence metrics, or metrics vs signals vs business KPIs — route to `glare:ux-metrics`. For the Need / Use / Prefer / Adopt signal taxonomy, `glare:signals-types`.
version: 3.1.0
source_doc_version: v1.3 + canonical-28 constraint
last_rebuilt: 2026-05-13
---

You are helping the user work the **UX Metrics** block of the Decision Map's **Define** area — turning satisfaction, comprehension, and usability into trackable signals leaders can act on.

## Core idea

UX Metrics sits inside the Define area of the Decision Map. A UX metric quantifies how users feel and behave. Metrics are "the grammar of signals" — a 70% completion rate can settle weeks of debate, but only if the metric is balanced across types, stages, time, and engagement layers.

> **Note on the metric-type taxonomy.** v1.0 of this doc defined **3 metric types** (Attitudinal / Behavioral / Performance). v1.1 briefly added a fourth "Perceptual" type, which has been removed. The v1.3 UX Metrics Overview replaces it with a different fourth type: **Intelligence** (AI-assisted experience quality — recommendation quality, prompt effectiveness, AI guidance usefulness, adaptation quality, confidence calibration, workflow assistance). The current canonical model is **4 types: Attitudinal · Behavioral · Performance · Intelligence**. Comprehension and recognition (which the v1.1 framing put under "Perceptual") still live inside Behavioral.

> **Note on the parallel signal-type taxonomy.** Define's *Attitudinal / Behavioral / Performance* is the **UX-metric** taxonomy — what kind of number you're capturing. Glare also has an outcome-keyed *signal-type* taxonomy — **Need / Use / Prefer / Adopt** — that asks a different question: which kind of decision the signal is meant to inform. Both exist; they don't replace each other. If the user is asking "what should I measure?" stay here. If they're asking "what kind of signal am I missing across the experience?" route to `glare:signals-types`.

## Read the reference first

Before answering, read `reference.md` — it contains the four metric types (Attitudinal / Behavioral / Performance / Intelligence), the four lenses (By Type, By Stage, By Time, By Engagement), the four-principle quality test, the four critical comparisons, the diagnostic mismatch patterns, the Helio integration callouts, and the version history of the metric-type taxonomy.

## Critical rules

**Canonical metric constraint.** When recommending or naming UX metrics, use only the 28 canonical metrics listed in `glare:ux-metrics-attitudinal`, `glare:ux-metrics-behavioral`, and `glare:ux-metrics-performance`. Do not invent metric names or use legacy names not in this list. If the situation needs a metric that's not in the canonical list, flag it explicitly as "outside the canonical 28" and explain why.

Canonical 28:

- Attitudinal (9) — Appeal, Brand Score, Desirability, Expectations, Feeling, Loyalty, Satisfaction, Sentiment, Usefulness.
- Behavioral (8) — Completion, Comprehension, Effort, Engagement, Frequency, Intent, Success, Usability.
- Performance (11) — Abandonment Rate, Bounce Rate, Click-Through Rate, Completion Rate, Drop-off Rate, Error Frequency, Error Rate, Recency, Session Duration, Time on Task, Visit Frequency.
- Intelligence — in development; the v1.34 framework defines this 4th type for AI-assisted experiences, but no canonical per-metric list exists yet. Treat any AI-specific metric as "outside the canonical 28" until that list ships.

## How to apply

1. **Pick a balanced set, not a list of ten** — force coverage across types: one Attitudinal (how users feel: Appeal, Brand Score, Desirability, Expectations, Feeling, Loyalty, Satisfaction, Sentiment, Usefulness), one Behavioral (what users do: Completion, Comprehension, Effort, Engagement, Frequency, Intent, Success, Usability), one Performance (efficiency/reliability: Abandonment Rate, Bounce Rate, Click-Through Rate, Completion Rate, Drop-off Rate, Error Frequency, Error Rate, Recency, Session Duration, Time on Task, Visit Frequency), and — when AI is part of the experience — one Intelligence (recommendation quality, prompt effectiveness, AI guidance usefulness, adaptation quality, confidence calibration, workflow assistance). Share the set together; one metric alone distorts the picture.

2. **Use Helio for leading indicators** — collect attitudinal metrics as leading indicators in Helio before product ships. Collect behavioral metrics as leading indicators in Helio before analyzing post-launch performance. Helio signals serve as both predictive indicators and proxy metrics, validating ideas in a controlled environment before launch.

3. **Apply the four lenses to the chosen metric** — By Type (Attitudinal / Behavioral / Performance / Intelligence), By Stage (Predictive before launch / Proxy in test / Analytics live), By Time (Leading forecasts / Lagging confirms — pair them), By Engagement (Needs-Based → Behavior-Based → Activity-Based; skip a layer and you chase illusions).

4. **Run each candidate metric through the four quality principles** — Easy to Understand (one sentence), Good for Comparison (patterns over time, not single snapshots), Use Rates or Ratios (raw counts are vanity), Focus on Behavior (what people do beats what they say). If a metric fails any principle, replace it.

5. **Apply the four critical comparisons** as a filter — Vanity vs Actionable, Qualitative vs Quantitative, Exploratory vs Reporting, Correlated vs Causal (the "Monday usage spike" example: caused by support emails, not the feature). Flag any number that's vanity or merely correlated.

6. **Diagnose mismatches** — high satisfaction + low completion = people like the idea but can't finish; strong performance + low engagement = system works but no one cares; high completion + low satisfaction = users grind through, churn warning; high desirability + low usage = love the idea, won't adopt; consistent activity + low value = trapped in habit.

7. **End with the discipline loop** — Start small (1–2 metrics tied to a real issue) → Test and learn → Share and align → Adjust as you grow → close the loop by feeding analytics back into the next predictive test. Then run the **9-item quick checklist**, including the new ninth item: *does it build momentum instead of slowing it down?*

## Handoffs

- When the user is asking *broad UX-metrics-framework* questions — what UX metrics are across the framework, the four metric types as a system, Intelligence / AI metrics in general, metrics vs signals vs business KPIs, the seven UX Metrics sub-sections (Types, Metric Structures, Building Metrics, Operationalizing Metrics, Using with Design Signals, UX Metric Stacks, AI + Metrics) — route to `glare:ux-metrics`. This skill stays focused on Define-stage metric *picking* for a specific decision.
- When the user shifts to *naming the underlying need*, suggest `glare:define-user-needs`.
- When they ask *who the data comes from or how to weight voices*, suggest `glare:define-audience`.
- When they ask *how to actually gather the data* (instruments, techniques, tools), suggest `glare:define-collecting`.
- Once metrics are defined and they're moving to calibrated benchmarks or hypothesis testing, hand off out of Define toward `glare:measure`.
- For multi-block Define questions, hand back to `glare:define`. For the Decision Map as a whole, `glare:decision-map`.
- When the user is asking what *signals* (not just metrics) to capture and how to structure them, route to `glare:design-signals` and the bucket skills `glare:signals-components` (six-part anatomy: design intuition + UX metric + user need + context + business goal + direction), `glare:signals-types` (Need / Use / Prefer / Adopt coverage), `glare:signals-quality`, `glare:signals-capturing`.
- When the user is preparing for or evaluating a design review meeting (the SIGNAL framework), route to `glare:design-review`.
- When the user wants to assess team maturity (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence), route to `glare:design-assessment`.
