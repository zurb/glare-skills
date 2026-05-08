# UX Metrics — Reference (top-level Glare framework, v1.3)

## What UX metrics are

UX metrics are measurable ways to understand how people experience a product, workflow, service, or interface. They quantify how users feel, what users do, where friction exists, how efficiently tasks work, and whether AI systems help users move forward.

Inside Glare, UX metrics are foundational. They sit underneath Design Signals and create a shared structure for how teams collect, interpret, compare, and discuss user data across the Decision Map, Design Signals, Design Reviews, AI workflows, assessments, benchmarking systems, and product decisions.

> **Version history of the metric-type taxonomy.**
>
> - **v1.0** — defined **3 types**: Attitudinal · Behavioral · Performance.
> - **v1.1** — briefly proposed a fourth "Perceptual" type for comprehension and mental-model fit. Removed.
> - **v1.3 (canonical, source May 6, 2025)** — defines **4 types**: Attitudinal · Behavioral · Performance · **Intelligence** (AI-assisted experience quality, NEW). Comprehension and recognition (which v1.1 put under "Perceptual") live inside Behavioral.

This reference covers the top-level framework. For Define-stage metric *picking* on a specific decision, see `glare-define-ux-metrics`.

## An open metrics system

Glare provides an open system of UX metrics teams can apply using their existing tools and workflows, or through Helio, which already includes many of these metrics directly inside the platform for testing, benchmarking, signal generation, and evaluation.

UX metrics transform reactions, behaviors, and performance into evidence teams can compare, discuss, and act on. As metrics accumulate, patterns begin to emerge — completion declines, comprehension weakens, satisfaction improves, retention increases. Those patterns help teams identify friction, strengthen direction, and make decisions with greater confidence. Over time, UX metrics create shared visibility around what is actually happening in the experience, helping organizations move from assumptions and opinions toward measurable evidence.

## Why UX metrics matter

Data is everywhere, but clarity is still rare.

AI accelerated the number of concepts, experiments, prototypes, and AI-assisted workflows teams can generate. What did not accelerate at the same pace was validation, alignment, and organizational confidence. That gap creates friction. Weak ideas survive too long, strong ideas stall in debate, and decisions drift without clear evidence.

UX metrics help teams:

- evaluate direction
- compare ideas
- expose friction
- reduce decision risk
- connect design work to measurable outcomes

Instead of waiting for post-launch analytics, teams can validate concepts earlier, compare competing directions, and build stronger signals while decisions are still being made.

---

## The four UX metric types

### Attitudinal — how users feel

Emotional response and perceived value. Trust, happiness, willingness to return.

**Examples:** Appeal, Brand Score, Desirability, Expectations, Feeling, Loyalty, Satisfaction, Sentiment, Usefulness.

> **Helio callout:** Collect attitudinal metrics as leading indicators in Helio before your product ships.

### Behavioral — what users actually do

Whether users successfully move through the experience or abandon it along the way.

**Examples:** Completion, Comprehension, Effort, Engagement, Frequency, Intent, Success, Usability.

> **Helio callout:** Collect behavioral metrics as leading indicators in Helio before analyzing post-launch performance.

### Performance — efficiency and reliability

Where systems slow users down or create unnecessary effort. Operational friction.

**Examples (v1.3 Overview):** Abandonment Rate, Bounce Rate, Click-Through Rate, Completion Rate, Drop-off Rate, Error Frequency, Error Rate, Recency, Session Duration, Time on Task, Visit Frequency.

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

## The four lenses (Metric Structures)

### By Type

Attitudinal · Behavioral · Performance · Intelligence — the four-type lens above. Force coverage; one metric alone distorts.

**Diagnostic mismatches:**
- High satisfaction + low completion = people like the idea but can't finish.
- Strong performance + low engagement = system works but no one cares.
- High completion + low satisfaction = users grind through; warning sign for churn.

### By Stage — Predictive · Proxy · Analytics

- **Predictive Metrics** — early warning. Reveal confusion before it turns into churn. A comprehension score on a prototype can save weeks. Logic — "If A happens, B will result, and C should decline."
- **Proxy Metrics** — test-bed proof. Tell you whether users can complete a task in a controlled environment. Logic — "If B happens, C will decline."
- **Analytics** — live report card. What happened once the product hit real traffic. Logic — "C is declining."

> **Helio callout:** Attitudinal and behavioral metrics collected in Helio serve as both predictive signals and proxy metrics, surfacing early user confusion and validating ideas in a controlled environment before launch.

Most teams wait for analytics. By then, the sprint is gone. Predictive and proxy keep you from being blindsided.

### By Time — Leading vs. Lagging

- **Leading Indicators** forecast what's likely to happen. Examples — clicks/sign-ups during early exposure, prototype usage, survey comprehension, beta feedback.
- **Lagging Indicators** confirm what happened after launch. Examples — customer satisfaction, revenue, conversion, post-launch task success, retention.

Leading-only = chasing noise. Lagging-only = learning too late.

### By Engagement — Needs · Behavior · Activity

A progression, not a single number. Confirm need → confirm use → confirm return. Skip a step and you chase illusions.

- **Needs-Based** — does this solve a real problem? Examples — brand score, desirability, usefulness, onboarding completion.
- **Behavior-Based** — are users finishing actions? Examples — completion rate, navigation paths, usage frequency, engagement scores.
- **Activity-Based** — do they keep coming back? Examples — repeat visits, session duration, drop-off rate, recency.

**Diagnostic mismatches:**
- High desirability + low usage = people love the idea but won't adopt.
- Strong usage + weak loyalty = try once and move on.
- Consistent activity + low value = trapped in habit, no real outcome.

---

## The four critical comparisons (filter)

### Vanity vs. Actionable
Vanity flatters. Actionable guides. Ten thousand page views vs. comprehension rate.

### Qualitative vs. Quantitative
Quantitative shows *what* happened. Qualitative shows *why*. Without both, you have half the story. 80% signup completion looks strong until paired with satisfaction scores showing users were confused while finishing.

### Exploratory vs. Reporting
Reporting metrics arrive after the fact. Exploratory metrics prevent failure before launch. Analytics shows adoption is low — but by then the sprint has moved on. Exploratory signals like comprehension or desirability would have flagged the issue weeks earlier.

### Correlated vs. Causal
Correlation shows a pattern. Causation shows proof. The "Monday usage spike" example — caused by Sunday-night support emails, not the feature itself. Without testing, you improve the wrong thing.

---

## The four quality principles

Each metric must pass these tests.

1. **Easy to Understand** — if the team cannot explain the metric in one sentence, it will never guide a decision.
2. **Good for Comparison** — patterns over time, across groups, between versions. "We got 432 clicks" is trivia. "This version improved comprehension by 27%" is proof.
3. **Use Rates or Ratios** — raw counts are vanity. Ratios reveal truth. Ten thousand visits looks impressive until you see 98% bounced.
4. **Focus on Behavior** — what people say is often polite fiction. What they do is reality.

---

## The seven sub-sections (planned)

The full UX Metrics section is organized into seven areas that help teams build stronger measurement systems over time.

### 1. Types
The major categories of UX metrics and what each reveals — the four-type taxonomy above (Attitudinal · Behavioral · Performance · Intelligence). Foundation for everything else.

### 2. Metric Structures
How metrics evolve across time, stages, engagement, and comparison models — the four lenses above. Teaches teams to think structurally about measurement, not just pick a metric.

### 3. Building Metrics
Creating metric systems tied to user needs, workflows, and business outcomes. Overlaps with `glare-define-ux-metrics` for picking metrics in the Define area, and with `glare-signals-components` for embedding metrics inside the six-piece signal anatomy.

### 4. Operationalizing Metrics
Using baselines, benchmarking, scorecards, and comparative testing inside product work. Where measurement becomes part of the operating cadence — sprint reviews, dashboards, monthly readouts. Overlaps with `glare-measure` and `glare-focus-comparing`.

### 5. Using with Design Signals
Connecting metrics to signals, decisions, and measurable direction. Metrics are the structural layer underneath signals — see `glare-signals-components` for the full six-piece anatomy (design intuition + UX metric + user need + context + business goal + direction).

### 6. UX Metric Stacks
Reusable metric systems for common product surfaces — onboarding, navigation, dashboards, checkout flows, AI workflows, mobile, e-commerce, marketing. Pre-built stacks teams can adapt rather than building from scratch every sprint. Overlaps with `glare-measure-concepts` (the 200+ Concept catalog).

### 7. AI + Metrics
How AI changes evaluation, scoring consistency, prompt quality, and signal generation. Practical guidance for measuring AI features (Intelligence type) and using AI in measurement workflows. Overlaps with `glare-ai-workflows`.

---

## How UX metrics fit across Glare

UX metrics support every part of the framework:

| Glare area | What metrics do here |
|---|---|
| **Define** | Clarify what success should look like. UX metrics name the numbers that prove design worked. |
| **Measure** | Validate concepts, hunches, experiments. Metrics are the falsifiability test. |
| **Focus** | Compare directions and expose tradeoffs. Side-by-side metric reads pick the move. |
| **Lead** | Connect design work to measurable outcomes. Chain UX metric → product KPI → business KPI. |
| **Design Signals** | Metrics are the structural layer under the six-piece signal anatomy. |
| **Design Reviews** | Metrics ground the conversation in evidence (the G in SIGNAL). |
| **Design Assessment** | Metrics underpin Building Proof — does the team's design work connect to measurable outcomes? |
| **AI Workflows** | Intelligence metrics measure whether AI features improve outcomes. |
| **Benchmarking** | Metrics enable comparison across versions, competitors, journeys, segments. |

---

## From metrics to decisions

Organizations already have more data than they can interpret. The challenge is not collecting numbers — it's turning numbers into clear decisions before momentum disappears.

That is where UX metrics create value inside Glare. They help teams:

- see friction earlier
- compare ideas faster
- reduce uncertainty
- strengthen signals
- protect momentum
- prove impact more clearly

Over time, measurement stops being something teams report on after the work is finished. It becomes part of how teams decide what deserves to move forward.

---

## Quick checklist (9 items)

1. Can everyone understand the metric in one sentence?
2. Can it be compared across time or groups?
3. Is it a rate or ratio, not just a raw count?
4. Does it capture behavior, not just opinion?
5. Is it actionable, not vanity?
6. Does it pair *what* happened with *why*?
7. Does it fit the timing — predictive, proxy, or analytics?
8. Does it balance leading and lagging signals?
9. Does it build momentum instead of slowing it down?

---

## Related key terms

- **Four UX Metric Types** — Attitudinal, Behavioral, Performance, Intelligence (v1.3 canonical).
- **Four UX Metric Lenses** — By Type, By Stage (Predictive/Proxy/Analytics), By Time (Leading/Lagging), By Engagement (Needs/Behavior/Activity).
- **Four metric-comparison filters** — Vanity vs Actionable, Qualitative vs Quantitative, Exploratory vs Reporting, Correlated vs Causal.
- **Four metric-quality principles** — Easy to Understand · Good for Comparison · Use Rates or Ratios · Focus on Behavior.
- **Seven sub-sections** — Types · Metric Structures · Building Metrics · Operationalizing Metrics · Using with Design Signals · UX Metric Stacks · AI + Metrics.
- **Signal** — a measurable, trustworthy piece of evidence. The unit of credibility in Glare.
- **Helio** — in-house testing platform; collects attitudinal and behavioral metrics as leading indicators / proxies before launch.

## Source

Drafted from *Glare | UX Metrics, Overview v1.3* (Drive doc 1efa33k8WND9QEybJ9pWdXNZn-8vtOF5rvuOKZMf8TsU, May 6, 2025). The four-type taxonomy and the seven sub-sections come directly from that source. Cross-referenced with the existing `glare-define-ux-metrics` skill (v1.6.0) for voice and structure consistency.
