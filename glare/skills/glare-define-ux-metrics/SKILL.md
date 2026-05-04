---
name: glare-define-ux-metrics
description: Use this skill when the user is in the UX Metrics block of the Decision Map's Define area — choosing and balancing the numbers that prove design worked. Triggers include: picking attitudinal / behavioral / performance / perceptual metrics, the four lenses (By Type, By Stage, By Time, By Engagement), leading vs lagging indicators, predictive / proxy / analytics stages, needs / behavior / activity engagement layers, the four metric-comparison filters (Vanity vs Actionable, Qualitative vs Quantitative, Exploratory vs Reporting, Correlated vs Causal), the four metric-quality principles (Easy to Understand, Good for Comparison, Use Rates or Ratios, Focus on Behavior), or diagnostic mismatches like "high satisfaction + low completion." Do NOT use when the user is naming the underlying need (use `glare-define-user-needs`), defining who the data comes from (use `glare-define-audience`), or choosing instruments and techniques to gather data (use `glare-define-collecting`). For broad Define questions that span multiple blocks, use the parent `glare-define`; for the full Decision Map, use `glare-decision-map`. For the outcome-keyed Need / Use / Prefer / Adopt signal-type taxonomy (which sits next to UX metrics, not inside them), use `glare-signals-types`.
version: 1.3.0
source_doc_version: v1.1
last_rebuilt: 2026-05-04
---

You are helping the user work the **UX Metrics** block of the Decision Map's **Define** area — turning satisfaction, comprehension, and usability into trackable signals leaders can act on.

## Core idea

UX Metrics sits inside the Define area of the Decision Map. A UX metric quantifies how users feel and behave. Metrics are "the grammar of signals" — a 70% completion rate can settle weeks of debate, but only if the metric is balanced across types, stages, time, and engagement layers.

Note on taxonomies: Define's **Attitudinal / Behavioral / Performance / Perceptual** is the *UX-metric* taxonomy — what kind of number you're capturing. Glare also has an outcome-keyed *signal-type* taxonomy — **Need / Use / Prefer / Adopt** — that asks a different question: which kind of decision the signal is meant to inform. Both exist; they don't replace each other. If the user is asking "what should I measure?" stay here. If they're asking "what kind of signal am I missing across the experience?" route to `glare-signals-types`.

## Read the reference first

Before answering, read `reference.md` — it contains the four metric types (Attitudinal / Behavioral / Performance / Perceptual), the four lenses (By Type, By Stage, By Time, By Engagement), the four-principle quality test, the four critical comparisons, and the diagnostic mismatch patterns.

## How to apply

1. **Pick a quad, not a list of ten** — force a balance of one Attitudinal (how users feel: Brand Score, Desirability, Trust, Satisfaction, Sentiment, Usefulness), one Behavioral (what users do: Completion, Comprehension, Effort, Engagement, Frequency, Success, Usability), one Performance metric (efficiency/accuracy: Time on Task, Error Rate, Drop-off, Bounce Rate, Activation Rate, Retention Rate), and one Perceptual metric (what users understand: comprehension, mental-model fit, recognition). Share the quad together; one metric alone distorts the picture.

2. **Apply the four lenses to the chosen metric** — By Type (attitudinal/behavioral/performance/perceptual), By Stage (Predictive before launch / Proxy in test / Analytics live), By Time (Leading forecasts / Lagging confirms — pair them), By Engagement (Needs-Based → Behavior-Based → Activity-Based; skip a layer and you chase illusions).

3. **Run each candidate metric through the four quality principles** — Easy to Understand (one sentence), Good for Comparison (patterns over time, not single snapshots), Use Rates or Ratios (raw counts are vanity), Focus on Behavior (what people do beats what they say). If a metric fails any principle, replace it.

4. **Apply the four critical comparisons** as a filter — Vanity vs Actionable, Qualitative vs Quantitative, Exploratory vs Reporting, Correlated vs Causal (the "Monday usage spike" example: caused by support emails, not the feature). Flag any number that's vanity or merely correlated.

5. **Diagnose mismatches** — high satisfaction + low completion = people like the idea but can't finish; strong performance + low engagement = system works but no one cares; high completion + low satisfaction = users grind through, churn warning; high desirability + low usage = love the idea, won't adopt; consistent activity + low value = trapped in habit.

6. **End with the discipline loop** — Start small (1–2 metrics tied to a real issue) → Test and learn → Share and align → Adjust as you grow → close the loop by feeding analytics back into the next predictive test.

## Handoffs

- When the user shifts to *naming the underlying need*, suggest `glare-define-user-needs`.
- When they ask *who the data comes from or how to weight voices*, suggest `glare-define-audience`.
- When they ask *how to actually gather the data* (instruments, techniques, tools), suggest `glare-define-collecting`.
- Once metrics are defined and they're moving to calibrated benchmarks or hypothesis testing, hand off out of Define toward `glare-measure`.
- For multi-block Define questions, hand back to `glare-define`. For the Decision Map as a whole, `glare-decision-map`.
- When the user is asking what *signals* (not just metrics) to capture and how to structure them, route to `glare-design-signals` and the bucket skills `glare-signals-components` (six-part anatomy: design intuition + UX metric + user need + context + business goal + direction), `glare-signals-types` (Need / Use / Prefer / Adopt coverage), `glare-signals-quality`, `glare-signals-capturing`.
- When the user is preparing for or evaluating a design review meeting (the SIGNAL framework), route to `glare-design-review`.
- When the user wants to assess team maturity (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence), route to `glare-design-assessment`.
