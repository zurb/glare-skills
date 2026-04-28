# UX Metrics — Reference (extracted from define-compressed.md)

## Glare | Define, UX Metrics v1.0

- **A UX metric quantifies how users feel and behave** — turning satisfaction, comprehension, and usability into trackable signals.
- **Four types (the foundational taxonomy):**
  - **Attitudinal** (how users feel): Brand Score, Desirability, Expectations, Feeling, Helpfulness, Trust, Loyalty, Satisfaction, Reaction, Sentiment, Usefulness
  - **Behavioral** (what users do): Completion, Comprehension, Effort, Engagement, Frequency, Intent, Success, Usability
  - **Performance** (efficiency/accuracy): split into Marketing (Avg Time on Page, Avg Session Duration, Pages per Session, Bounce Rate, Exit Rate, Device Type, Event Tracking), eCommerce (Engagement, Abandonment Rate, Bounce Rate, Store Sessions), and Product (Stickiness, Activation Rate, Feature Usage, Time to Activate, Retention Rate, Click-back Rate)
  - **Perceptual** — what users understand. Examples: Comprehension, Recognition, Mental-Model Fit, Information-Scent. Surfaces gaps where the design works mechanically but users don't grasp it. Added in v1.1.
- **4-step discipline:** Start small (1–2 metrics tied to a real issue) → Test and learn → Share and align → Adjust as you grow.
- **Four principles for choosing metrics** (each metric must pass these tests):
  - **Easy to Understand** — explainable in one sentence; otherwise it won't guide decisions
  - **Good for Comparison** — patterns over time, not single snapshots ("432 clicks" is trivia; "27% comprehension lift" is proof)
  - **Use Rates or Ratios** — raw counts are vanity (10k visits with 98% bounce)
  - **Focus on Behavior** — what people do beats what they say
- **Four critical comparisons:** Vanity vs Actionable; Qualitative vs Quantitative; Exploratory vs Reporting; Correlated vs Causal (the "Monday usage spike" example: caused by support emails, not the feature).
- **UX Metrics in Practice — four lenses (each its own sub-doc):**
  - **By Type** (attitudinal / behavioral / performance / perceptual)
  - **By Stage** (predictive / proxy / analytics)
  - **By Time** (leading / lagging)
  - **By Engagement** (needs / behavior / activity)
- **Quick checklist:** can it be explained in one sentence; comparable; a rate not a count; behavior-grounded; actionable; pairs *what* with *why*; fits timing; balances leading/lagging.

## Glare | Define, UX Metrics, By Type v1.0

- **Four lenses every product can be measured by:** how users feel (attitudinal), what they do (behavioral), how well they can do it (performance), and what they understand (perceptual). Ignore one and the picture distorts.
- **Attitudinal Metrics:** Do they trust this? Are they happy? Will they return? Examples: Brand Score, Desirability, Satisfaction.
- **Behavioral Metrics:** Are they finishing? Do they engage deeply? Where do they drop off? Examples: Completion Rate, Engagement, Usability.
- **Performance Metrics:** Is it efficient? Where stuck? How smoothly? Examples: Time on Task, Error Rate, Drop-off Rate.
- **Diagnostic mismatches (key insight):**
  - High satisfaction + low completion = people like the idea but can't finish.
  - Strong performance + low engagement = system works but no one cares.
  - High completion + low satisfaction = users grind through; warning sign for churn.
- **5-step method:** define the question (perception/action/efficiency) → pick one metric from each type (a trio, not ten) → run a small test → look for mismatches → share the trio together.
- **Traps:** relying on one type; collecting too many signals; treating metrics as static.
- **Proof in practice:** team saw 80% signup completion (looked great), then added satisfaction (most users confused) and time on task (slow/painful) — redesigned for clarity, got faster signups and lasting retention.

## Glare | Define, UX Metrics, By Time v1.0

- **Anticipate Early, Prove Later.** Most teams overweight lagging data because executives recognize it; lagging tells you what already happened when damage is done.
- **Leading Indicators** — forecast what's likely to happen. Are users interested? Do they understand? Will this block them later? Examples: clicks/sign-ups during early exposure, prototype usage, survey comprehension, beta feedback.
- **Lagging Indicators** — confirm what happened after launch. Did adoption hold? Did retention grow? Examples: customer satisfaction, revenue, conversion rates, post-launch task success, retention over time.
- **Why pair them:** leading-only = chasing noise; lagging-only = learning too late. Leading sparks adjustments before launch; lagging proves those adjustments created value.
- **4-step method:** identify the window (anticipate vs evaluate) → pick matching signal → pair them deliberately → connect them (do leading signals correlate with long-term outcomes? recalibrate if not).
- **Traps:** relying only on lagging; over-trusting leading (early excitement ≠ loyalty); not linking the two.
- **Proof in practice:** SaaS collaboration feature had high desirability and beta usage (leading), but adoption plateaued and retention didn't improve (lagging). Mismatch revealed users liked the idea in theory but never built it into workflows; team redirected effort.

## Glare | Define, UX Metrics, By Stage v1.0

- **Three stages of metrics:** Predictive, Proxy, Analytics. A metric useful in testing is useless once live, and vice versa.
- **Predictive Metrics** — leading indicators forecasting outcomes by revealing confusion or friction before launch. Logic: "If A happens, B will result, and C should decline." Example: 70% of users confused by a landing page in a survey.
- **Proxy Metrics** — show how a design performs in controlled settings (usability tests, concept evals). Logic: "If B happens, C will decline." Example: 50% can complete a flow in test.
- **Analytics** — measure live behavior. Logic: "C is declining." Example: time spent in section + completion → design supports the goal. Analytics show *what* but rarely *why*.
- **4-step method:** identify the stage (exploring/testing/live) → pick matching metric → pair them → close the loop (feed analytics into next predictive tests).
- **Traps:** relying only on analytics; trusting proxies too much; forgetting the loop.
- **Proof in practice:** financial app saw 60% drop-off in old onboarding. Predictive tests on prototypes revealed users didn't understand key terms (refined language); proxy usability showed 90% task completion; analytics post-launch confirmed adoption rose, drop-off fell below 20%.

## Glare | Define, UX Metrics, By Engagement v1.0

- **Engagement is a progression, not a single number.** Confirm need → confirm use → confirm return. Skip a step and you chase illusions.
- **Three layers:**
  - **Needs-Based** (customer understanding) — does this solve a real problem; do users see value? Examples: brand score, desirability, usefulness, onboarding completion, power-user feature adoption.
  - **Behavior-Based** (customer behavior) — are users finishing actions; using features meaningfully? Examples: completion rate, navigation paths, usage frequency, engagement scores.
  - **Activity-Based** (customer activity) — do they keep coming back; how long; routine? Examples: repeat visits, session duration, drop-off rate, recency of use.
- **Diagnostic mismatches:**
  - High desirability + low usage = people love the idea but won't adopt.
  - Strong usage + weak loyalty = try once and move on.
  - Consistent activity + low value = trapped in habit, no real outcome.
- **4-step method:** start with needs → layer in behavior → add activity → look for gaps (the lagging layer is your friction point).
- **Traps:** chasing shallow numbers (clicks/time on page); skipping layers (adoption without loyalty = delayed churn); mistaking activity for value.
- **Proof in practice:** productivity tool's collaboration feature had high desirability + promising one-time usage, but repeat use dropped within weeks — excitement was real, loyalty missing.

## Related key terms

- **Four UX Metric Types** — Attitudinal, Behavioral, Performance, Perceptual.
- **Four UX Metric Lenses** — By Type, By Stage (Predictive/Proxy/Analytics), By Time (Leading/Lagging), By Engagement (Needs/Behavior/Activity).
- **Vanity vs Actionable / Qualitative vs Quantitative / Exploratory vs Reporting / Correlated vs Causal** — the four metric-comparison filters.
- **Signal** — a measurable, trustworthy piece of evidence (vs raw "data"). The unit of credibility in Glare.
