---
name: glare-define-ux-metrics
description: Use this skill when the user is in the UX Metrics block of the Define area — choosing the numbers that prove design worked. Triggers — picking attitudinal / behavioral / performance metrics; the four lenses (By Type, By Stage, By Time, By Engagement); leading vs lagging indicators; predictive / proxy / analytics stages; the four comparison filters (Vanity vs Actionable, Qualitative vs Quantitative, Exploratory vs Reporting, Correlated vs Causal); the four quality principles (Easy to Understand, Good for Comparison, Use Rates or Ratios, Focus on Behavior); mismatches like "high satisfaction + low completion"; capturing leading indicators in Helio. Do NOT use when naming the need (use `glare-define-user-needs`), defining who data comes from (use `glare-define-audience`), or choosing instruments (use `glare-define-collecting`). For broad Define, use `glare-define`; for the full Decision Map, use `glare-decision-map`. For the Need / Use / Prefer / Adopt taxonomy, use `glare-signals-types`.
version: 1.4.0
source_doc_version: v1.0 (re-edited 2026-05-06)
last_rebuilt: 2026-05-06
---

You are helping the user work the **UX Metrics** block of the Decision Map's **Define** area — turning satisfaction, comprehension, and usability into trackable signals leaders can act on.

## Core idea

UX Metrics sits inside the Define area of the Decision Map. A UX metric quantifies how users feel and behave. Metrics are "the grammar of signals" — a 70% completion rate can settle weeks of debate, but only if the metric is balanced across types, stages, time, and engagement layers.

> **Note on the metric-type taxonomy.** Earlier compressed versions added a fourth "Perceptual" metric type. The current source-of-truth UX Metrics doc (v1.0, re-edited 2026-05-06) explicitly defines **3 metric types only**: Attitudinal / Behavioral / Performance. This skill follows the 3-type taxonomy as canonical. Comprehension and recognition (which the v1.1 framing put under "Perceptual") now live inside Behavioral.

> **Note on the parallel signal-type taxonomy.** Define's *Attitudinal / Behavioral / Performance* is the **UX-metric** taxonomy — what kind of number you're capturing. Glare also has an outcome-keyed *signal-type* taxonomy — **Need / Use / Prefer / Adopt** — that asks a different question: which kind of decision the signal is meant to inform. Both exist; they don't replace each other. If the user is asking "what should I measure?" stay here. If they're asking "what kind of signal am I missing across the experience?" route to `glare-signals-types`.

## Read the reference first

Before answering, read `reference.md` — it contains the three metric types (Attitudinal / Behavioral / Performance), the four lenses (By Type, By Stage, By Time, By Engagement), the four-principle quality test, the four critical comparisons, the diagnostic mismatch patterns, and the Helio integration callouts.

## How to apply

1. **Pick a trio, not a list of ten** — force a balance of one Attitudinal (how users feel: Brand Score, Desirability, Trust, Satisfaction, Sentiment, Usefulness), one Behavioral (what users do: Completion, Comprehension, Effort, Engagement, Frequency, Success, Usability), and one Performance metric (efficiency/accuracy: Time on Task, Error Rate, Drop-off, Bounce Rate, Activation Rate, Retention Rate, Stickiness). Share the trio together; one metric alone distorts the picture.

2. **Use Helio for leading indicators** — collect attitudinal metrics as leading indicators in Helio before product ships. Collect behavioral metrics as leading indicators in Helio before analyzing post-launch performance. Helio signals serve as both predictive indicators and proxy metrics, validating ideas in a controlled environment before launch.

3. **Apply the four lenses to the chosen metric** — By Type (attitudinal/behavioral/performance), By Stage (Predictive before launch / Proxy in test / Analytics live), By Time (Leading forecasts / Lagging confirms — pair them), By Engagement (Needs-Based → Behavior-Based → Activity-Based; skip a layer and you chase illusions).

4. **Run each candidate metric through the four quality principles** — Easy to Understand (one sentence), Good for Comparison (patterns over time, not single snapshots), Use Rates or Ratios (raw counts are vanity), Focus on Behavior (what people do beats what they say). If a metric fails any principle, replace it.

5. **Apply the four critical comparisons** as a filter — Vanity vs Actionable, Qualitative vs Quantitative, Exploratory vs Reporting, Correlated vs Causal (the "Monday usage spike" example: caused by support emails, not the feature). Flag any number that's vanity or merely correlated.

6. **Diagnose mismatches** — high satisfaction + low completion = people like the idea but can't finish; strong performance + low engagement = system works but no one cares; high completion + low satisfaction = users grind through, churn warning; high desirability + low usage = love the idea, won't adopt; consistent activity + low value = trapped in habit.

7. **End with the discipline loop** — Start small (1–2 metrics tied to a real issue) → Test and learn → Share and align → Adjust as you grow → close the loop by feeding analytics back into the next predictive test. Then run the **9-item quick checklist**, including the new ninth item: *does it build momentum instead of slowing it down?*

## Handoffs

- When the user shifts to *naming the underlying need*, suggest `glare-define-user-needs`.
- When they ask *who the data comes from or how to weight voices*, suggest `glare-define-audience`.
- When they ask *how to actually gather the data* (instruments, techniques, tools), suggest `glare-define-collecting`.
- Once metrics are defined and they're moving to calibrated benchmarks or hypothesis testing, hand off out of Define toward `glare-measure`.
- For multi-block Define questions, hand back to `glare-define`. For the Decision Map as a whole, `glare-decision-map`.
- When the user is asking what *signals* (not just metrics) to capture and how to structure them, route to `glare-design-signals` and the bucket skills `glare-signals-components` (six-part anatomy: design intuition + UX metric + user need + context + business goal + direction), `glare-signals-types` (Need / Use / Prefer / Adopt coverage), `glare-signals-quality`, `glare-signals-capturing`.
- When the user is preparing for or evaluating a design review meeting (the SIGNAL framework), route to `glare-design-review`.
- When the user wants to assess team maturity (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence), route to `glare-design-assessment`.
