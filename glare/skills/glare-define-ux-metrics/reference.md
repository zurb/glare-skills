# UX Metrics — Reference (Glare Define, v1.3)

## Canonical 28 Metrics

When recommending or naming UX metrics, recommend **only** from these 28. Anything else is "outside the canonical 28" and must be flagged with a reason.

### Attitudinal (9) — how users feel

- **Appeal** — strength of attraction or interest the experience generates on first impression.
- **Brand Score** — composite measure of how users perceive and rate the brand.
- **Desirability** — degree to which users want to use, return to, or recommend the experience.
- **Expectations** — alignment between what users anticipate and what they encounter.
- **Feeling** — emotional tone users report after an interaction.
- **Loyalty** — likelihood of repeat use, advocacy, or long-term commitment.
- **Satisfaction** — overall contentment with the experience or outcome.
- **Sentiment** — directional valence (positive / neutral / negative) of expressed user feedback.
- **Usefulness** — perceived value the experience delivers against a user's need.

### Behavioral (8) — what users do

- **Completion** — whether users finish a defined flow or task.
- **Comprehension** — whether users correctly understand content, options, or outcomes.
- **Effort** — perceived or observed work required to reach a goal.
- **Engagement** — depth and quality of interaction with the experience.
- **Frequency** — how often a user performs a behavior in a window of time.
- **Intent** — observable signal of a user's goal or next action.
- **Success** — whether the user achieved the intended outcome of a task.
- **Usability** — overall ease and quality of interacting with the design.

### Performance (11) — efficiency and reliability

- **Abandonment Rate** — share of users who leave a flow before completion.
- **Bounce Rate** — share of sessions that exit after a single page or step.
- **Click-Through Rate** — share of impressions that produced a click on the target element.
- **Completion Rate** — share of users who finish a defined task or flow.
- **Drop-off Rate** — share of users lost at a specific step of a flow.
- **Error Frequency** — count of user-facing errors over a defined window.
- **Error Rate** — share of attempts that produced an error.
- **Recency** — time since a user's last meaningful interaction.
- **Session Duration** — length of a single user session.
- **Time on Task** — time required to complete a defined task.
- **Visit Frequency** — how often a user returns over a defined window.

### Intelligence — in development

The v1.34 UX Metrics framework defines a 4th type for AI-assisted experiences (recommendation quality, prompt effectiveness, AI guidance usefulness, adaptation quality, confidence calibration, workflow assistance), but no canonical per-metric list has shipped yet. Until it does, AI-specific metrics are "outside the canonical 28."

---

## What a UX metric is

A UX metric quantifies how users feel and behave when they interact with your product. Metrics turn concepts like satisfaction, comprehension, and usability into signals you can track, compare, and act on. They are "the grammar of signals" — a 70% completion rate can settle weeks of debate.

> **Version history of the metric-type taxonomy.**
>
> - **v1.0** — defined **3 types**: Attitudinal / Behavioral / Performance.
> - **v1.1** — briefly proposed a fourth "Perceptual" type for comprehension and mental-model fit. Removed.
> - **v1.3 (canonical)** — defines **4 types**: Attitudinal · Behavioral · Performance · **Intelligence** (AI-assisted experience quality, new in v1.3 with the UX Metrics Overview release).
>
> This reference follows the v1.3 four-type taxonomy. Comprehension and recognition (which the v1.1 framing put under "Perceptual") live inside Behavioral. The broader UX Metrics framework (sub-sections, AI workflows, metrics vs signals vs business KPIs) lives in `glare-ux-metrics`; this skill stays focused on Define-stage metric picking.

## Why measure UX

Most teams measure too late or measure the wrong thing. They chase analytics that arrive after the sprint or collect numbers that look good on slides but never guide a decision. Metrics matter because they cut through noise: they reveal what users need, what they actually do, and how well design supports them.

## 4-step discipline

1. **Start small.** Choose one or two metrics tied to a real issue.
2. **Test and learn.** Don't wait for perfect data. One strong result can shape a decision.
3. **Share and align.** Data only matters if the team sees and understands it.
4. **Adjust as you grow.** Metrics should evolve with your product.

---

## When to use

- When picking the numbers that will prove the design worked for a specific decision.
- When choosing among Attitudinal / Behavioral / Performance / Intelligence metrics.
- When sorting metrics across the four lenses — By Type, By Stage, By Time, By Engagement.
- When using the four quality principles (Easy to Understand, Good for Comparison, Use Rates or Ratios, Focus on Behavior) to vet a metric.
- When applying the four comparison filters: Vanity vs Actionable, Qualitative vs Quantitative, Exploratory vs Reporting, Correlated vs Causal.
- When diagnosing mismatches like "high satisfaction + low completion."

**Don't use when** naming the underlying need (use `glare-define-user-needs`) or picking the research instrument (`glare-define-collecting`). For the broader UX Metrics framework or AI/Intelligence metrics, route to `glare-ux-metrics`.

## The four metric types

### Attitudinal — how users feel

Do they trust this? Are they happy? Will they return?

**Examples:** Appeal, Brand Score, Desirability, Expectations, Feeling, Loyalty, Satisfaction, Sentiment, Usefulness.

> **Helio callout (from source):** Collect attitudinal metrics as leading indicators in Helio before your product ships.

### Behavioral — what users do

Are they finishing? Do they engage deeply? Where do they drop off?

**Examples:** Completion, Comprehension, Effort, Engagement, Frequency, Intent, Success, Usability.

> **Helio callout (from source):** Collect behavioral metrics as leading indicators in Helio before analyzing post-launch performance.

### Performance — efficiency and reliability

Is the experience efficient? Where do people get stuck? How well does the product perform?

**Examples (from v1.3 Overview):** Abandonment Rate, Bounce Rate, Click-Through Rate, Completion Rate, Drop-off Rate, Error Frequency, Error Rate, Recency, Session Duration, Time on Task, Visit Frequency.

**Domain breakouts (legacy v1.0 framing, still useful):**

| Sub-area | Example metrics |
|---|---|
| **Marketing** | Avg Time on Page, Avg Session Duration, Pages per Session, Bounce Rate, Exit Rate, Device Type, Event Tracking |
| **eCommerce** | Engagement, Abandonment Rate, Bounce Rate, Store Sessions |
| **Product** | Stickiness, Activation Rate, Feature Usage, Time to Activate, Retention Rate, Click-back Rate |

### Intelligence — AI-assisted experience quality (NEW in v1.3)

As AI becomes part of product experiences, organizations need new ways to measure whether intelligence is actually improving outcomes instead of simply generating more output.

**Scope:**

- recommendation quality
- prompt effectiveness
- AI guidance usefulness
- adaptation quality
- confidence calibration
- workflow assistance

Use Intelligence metrics whenever AI is part of the experience being evaluated — recommendations, generative interfaces, AI guidance, adaptive workflows, decision-support systems.

Together, the four types give a full picture: how users feel, what they do, how well the system performs, and whether AI assistance helps. Ignore one and the picture distorts.

---

## Choosing UX metrics — four principles

Each metric must pass these tests.

### 1. Easy to Understand

If the team cannot explain the metric in one sentence, it will never guide a decision. Time-on-task is clear. Net Promoter Score is clear. A complicated index with three footnotes is not.

*Trap:* presenting numbers that only analysts understand. *Fix:* metrics everyone can repeat back without translation.

### 2. Good for Comparison

Metrics only matter if you can compare them over time, across groups, or between versions. "We got 432 clicks" is trivia. "This version improved comprehension by 27%" is proof.

*Trap:* treating single numbers as progress. *Fix:* metrics that reveal patterns, not snapshots.

### 3. Use Rates or Ratios

Raw counts are vanity. Ratios reveal truth. Ten thousand visits to a landing page looks impressive until you see that 98% bounced.

*Trap:* celebrating big totals. *Fix:* rates that reveal outcomes.

### 4. Focus on Behavior

What people say is often polite fiction. What they do is reality. Users may praise a feature, but if usage stays at zero, the signal is clear.

*Trap:* believing surveys without checking actions. *Fix:* pair attitudinal measures with behavioral proof.

---

## Four critical comparisons (filter)

### Vanity vs. Actionable
Vanity flatters. Actionable guides. Ten thousand page views vs. comprehension rate.

### Qualitative vs. Quantitative
Quantitative shows *what* happened. Qualitative shows *why*. Without both, you have half the story. 80% signup completion looks strong until paired with satisfaction scores showing users were confused while finishing.

### Exploratory vs. Reporting
Reporting metrics arrive after the fact. Exploratory metrics prevent failure before launch. Analytics shows adoption is low — but by then the sprint has moved on. Exploratory signals like comprehension or desirability would have flagged the issue weeks earlier.

### Correlated vs. Causal
Correlation shows a pattern. Causation shows proof. The "Monday usage spike" example: caused by Sunday-night support emails, not the feature itself. Without testing, you improve the wrong thing.

---

## UX Metrics in Practice — four lenses

### By Type — four lenses

- **Attitudinal** — how users feel.
- **Behavioral** — what users do.
- **Performance** — how well the system works.
- **Intelligence** — whether AI-assisted parts of the experience actually improve outcomes (recommendation quality, prompt effectiveness, guidance usefulness, adaptation quality, confidence calibration, workflow assistance). Add this lens when AI is in the experience.

> **Helio callout:** Attitudinal and behavioral metrics can be collected as leading indicators in Helio, giving your team signal before performance data becomes available.

**Diagnostic mismatches:**
- High satisfaction + low completion = people like the idea but can't finish.
- Strong performance + low engagement = system works but no one cares.
- High completion + low satisfaction = users grind through; warning sign for churn.

### By Stage — Predictive, Proxy, Analytics

- **Predictive Metrics** — early warning. Reveal confusion before it turns into churn. A comprehension score on a prototype can save weeks. Logic: "If A happens, B will result, and C should decline."
- **Proxy Metrics** — test-bed proof. Tell you whether users can complete a task in a controlled environment. Logic: "If B happens, C will decline."
- **Analytics** — live report card. What happened once the product hit real traffic. Logic: "C is declining."

> **Helio callout:** Attitudinal and behavioral metrics collected in Helio serve as both predictive signals and proxy metrics, surfacing early user confusion and validating ideas in a controlled environment before launch.

Most teams wait for analytics. By then, the sprint is gone. Predictive and proxy keep you from being blindsided.

### By Time — Leading vs. Lagging

- **Leading Indicators** — forecast what's likely to happen. Examples: clicks/sign-ups during early exposure, prototype usage, survey comprehension, beta feedback.
- **Lagging Indicators** — confirm what happened after launch. Examples: customer satisfaction, revenue, conversion, post-launch task success, retention.

> **Helio callout:** Attitudinal and behavioral metrics collected in Helio serve as leading indicators, giving you user signal weeks before lagging performance metrics arrive.

Leading-only = chasing noise. Lagging-only = learning too late.

### By Engagement — Needs, Behavior, Activity

A progression, not a single number. Confirm need → confirm use → confirm return. Skip a step and you chase illusions.

- **Needs-Based** — does this solve a real problem? Examples: brand score, desirability, usefulness, onboarding completion.
- **Behavior-Based** — are users finishing actions? Examples: completion rate, navigation paths, usage frequency, engagement scores.
- **Activity-Based** — do they keep coming back? Examples: repeat visits, session duration, drop-off rate, recency.

**Diagnostic mismatches:**
- High desirability + low usage = people love the idea but won't adopt.
- Strong usage + weak loyalty = try once and move on.
- Consistent activity + low value = trapped in habit, no real outcome.

---

## Quick checklist (9 items, ninth added 2026-05-06)

1. Can everyone understand the metric in one sentence?
2. Can it be compared across time or groups?
3. Is it a rate or ratio, not just a raw count?
4. Does it capture behavior, not just opinion?
5. Is it actionable, not vanity?
6. Does it pair *what* happened with *why*?
7. Does it fit the timing — predictive, proxy, or analytics?
8. Does it balance leading and lagging signals?
9. **Does it build momentum instead of slowing it down?** *(new in 2026-05-06 source edit)*

---

## Business impact

When metrics are chosen with discipline, design earns credibility. Leaders trust the data. Teams move faster because decisions are grounded, not debated. Predictive signals show what is coming. Proxy signals validate ideas before scale. Analytics confirm impact once live. Together they create resilience.

## Failure modes

These are common ways this skill goes wrong in practice:

- **Picking vanity metrics.** "Page views increased" or "session length doubled" without a comparison or a tie to user behavior. The four filters (Vanity vs Actionable, etc.) exist to catch this — apply them before reporting.
- **Single-type metric stacks.** Tracking only Behavioral (clicks, completion) without Attitudinal (trust, confidence) or Performance (time, errors). The completion rate goes up while trust collapses, and the team won't see it until retention drops.
- **Choosing the metric after the data is in.** Letting available data drive the metric choice rather than choosing metrics to answer a specific decision. The metric should be picked when you frame the decision, not when results arrive.
- **Reporting correlation as causation.** "We launched the new flow AND retention improved" without isolating other factors. The Correlated vs Causal filter is the brake — name what would falsify the causal claim before celebrating it.
- **Treating leading and lagging as interchangeable.** Lagging indicators (retention, revenue) confirm impact; leading indicators (trust, confidence, comprehension) predict it. Use leading indicators to *steer*, lagging to *prove*.

## Related key terms

- **Four UX Metric Types** — Attitudinal, Behavioral, Performance, Intelligence (v1.3 canonical).
- **Four UX Metric Lenses** — By Type, By Stage (Predictive/Proxy/Analytics), By Time (Leading/Lagging), By Engagement (Needs/Behavior/Activity).
- **Vanity vs Actionable / Qualitative vs Quantitative / Exploratory vs Reporting / Correlated vs Causal** — the four metric-comparison filters.
- **Four metric-quality principles** — Easy to Understand · Good for Comparison · Use Rates or Ratios · Focus on Behavior.
- **Signal** — a measurable, trustworthy piece of evidence. The unit of credibility in Glare.
- **Helio** — in-house testing platform; collects attitudinal and behavioral metrics as leading indicators / proxies before launch.
