# UX Metrics — Reference (Glare Define, v1.0 re-edited 2026-05-06)

## What a UX metric is

A UX metric quantifies how users feel and behave when they interact with your product. Metrics turn concepts like satisfaction, comprehension, and usability into signals you can track, compare, and act on. They are "the grammar of signals" — a 70% completion rate can settle weeks of debate.

> **Compatibility note.** A v1.1 iteration of this doc briefly added a fourth "Perceptual" metric type covering comprehension and mental-model fit. The current source-of-truth UX Metrics doc — v1.0, re-edited 2026-05-06 — explicitly defines **3 metric types only**: Attitudinal, Behavioral, Performance. This reference follows the 3-type taxonomy as canonical. Comprehension is now categorized as a Behavioral metric.

## Why measure UX

Most teams measure too late or measure the wrong thing. They chase analytics that arrive after the sprint or collect numbers that look good on slides but never guide a decision. Metrics matter because they cut through noise: they reveal what users need, what they actually do, and how well design supports them.

## 4-step discipline

1. **Start small.** Choose one or two metrics tied to a real issue.
2. **Test and learn.** Don't wait for perfect data. One strong result can shape a decision.
3. **Share and align.** Data only matters if the team sees and understands it.
4. **Adjust as you grow.** Metrics should evolve with your product.

---

## The three metric types

### Attitudinal — how users feel

Do they trust this? Are they happy? Will they return?

**Examples:** Brand Score, Desirability, Expectations, Feeling, Helpfulness, Trust, Loyalty, Satisfaction, Reaction, Sentiment, Usefulness.

> **Helio callout (from source):** Collect attitudinal metrics as leading indicators in Helio before your product ships.

### Behavioral — what users do

Are they finishing? Do they engage deeply? Where do they drop off?

**Examples:** Completion, Comprehension, Effort, Engagement, Frequency, Intent, Success, Usability.

> **Helio callout (from source):** Collect behavioral metrics as leading indicators in Helio before analyzing post-launch performance.

### Performance — efficiency and accuracy

Is the experience efficient? Where do people get stuck? How well does the product perform?

| Sub-area | Example metrics |
|---|---|
| **Marketing** | Avg Time on Page, Avg Session Duration, Pages per Session, Bounce Rate, Exit Rate, Device Type, Event Tracking |
| **eCommerce** | Engagement, Abandonment Rate, Bounce Rate, Store Sessions |
| **Product** | Stickiness, Activation Rate, Feature Usage, Time to Activate, Retention Rate, Click-back Rate |

Together, these three types give a full picture: how users feel, what they do, how well they can do it. Ignore one and the picture distorts.

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

### By Type — three lenses

- **Attitudinal** — how users feel.
- **Behavioral** — what users do.
- **Performance** — how well the system works.

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

## Related key terms

- **Three UX Metric Types** — Attitudinal, Behavioral, Performance.
- **Four UX Metric Lenses** — By Type, By Stage (Predictive/Proxy/Analytics), By Time (Leading/Lagging), By Engagement (Needs/Behavior/Activity).
- **Vanity vs Actionable / Qualitative vs Quantitative / Exploratory vs Reporting / Correlated vs Causal** — the four metric-comparison filters.
- **Four metric-quality principles** — Easy to Understand · Good for Comparison · Use Rates or Ratios · Focus on Behavior.
- **Signal** — a measurable, trustworthy piece of evidence. The unit of credibility in Glare.
- **Helio** — in-house testing platform; collects attitudinal and behavioral metrics as leading indicators / proxies before launch.
