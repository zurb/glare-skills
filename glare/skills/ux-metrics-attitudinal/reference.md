# Attitudinal Metrics — Reference (v1.32, per-metric pages added)

## When to use

- When the user is working with how users *feel* about an experience — trust, confidence, satisfaction, frustration, desirability.
- When users complete workflows but feel confused, unsure, or disconnected.
- When attitudinal metrics serve as *leading indicators* — trust weakens before retention drops, confidence falls before abandonment rises.
- When picking among the nine canonical attitudinal metrics (Appeal, Brand Score, Desirability, Expectations, Feelings, Loyalty, Satisfaction, Sentiment, Usefulness).
- When attitudinal signals matter most — onboarding, fintech, healthcare, AI-assisted systems, automation, enterprise software.

**Don't use when** the user wants the broader UX Metrics framework (`glare:ux-metrics`), Behavioral or Performance metrics (`glare:ux-metrics-behavioral` / `glare:ux-metrics-performance`), or Define-stage picking on a specific decision (`glare:define-ux-metrics`).

## What attitudinal metrics measure

Attitudinal metrics measure how users feel about an experience — trust, confidence, satisfaction, frustration, desirability, emotional response. Product teams often focus heavily on clicks, completion, engagement, and conversion. Users can technically complete a workflow while still feeling confused, frustrated, unsure, or disconnected. Attitudinal metrics help teams understand what is happening emotionally underneath the workflow, not just what users completed on the surface.

A product may appear successful in analytics while users quietly lose confidence in the experience over time. As AI speeds up production and experimentation, emotional signals become even more important — speed often hides emotional friction until much later.

## Feelings often reveal problems earlier

Attitudinal metrics are often **leading indicators**. They reveal smaller emotional problems before larger business problems appear later. A product may still show strong engagement, healthy completion, and growing usage while users quietly lose trust, confidence, clarity, and emotional connection.

- trust may weaken before retention drops
- confidence may fall before abandonment rises
- frustration may grow before support tickets increase
- users may continue using AI recommendations while quietly doubting the results

Without attitudinal metrics, these problems are easy to miss because surface-level analytics may still appear healthy.

## When attitudinal metrics matter most

Especially during onboarding, fintech workflows, healthcare experiences, AI-assisted systems, automation workflows, and enterprise software — environments where emotional confidence often matters as much as usability.

## The canonical nine attitudinal metrics (v1.32)

This skill recommends ONLY from this canonical list of nine attitudinal metrics. Do not invent or borrow attitudinal metric names from other frameworks.

Appeal · Brand Score · Desirability · Expectations · Feelings · Loyalty · Satisfaction · Sentiment · Usefulness

Per-metric pages follow alphabetical order.

---

### Appeal

**What it measures:** How a design looks and feels at first glance — the gut reaction users have when they see a product before interacting with it.

**When to use:** Visual-impression decisions where style and tone carry real weight — early-stage concepts, layout comparisons, landing pages and marketing screens, brand-refresh validation, A/B testing of visual variations. Use Appeal when first-impression clarity, trust, or excitement needs to land before any interaction.

**How it's calculated / collected:** A 5-point Likert satisfaction question shown immediately after the design (Very Dissatisfied=1 → Very Satisfied=5). Convert each response to its numerical value, sum, divide by number of responses, then divide by 5 to express as a percentage. `Appeal = (Σ Likert ratings / number of responses) ÷ 5`.

**Example values:** Very Good >90%, Good 70–89%, Average 50–69%, Poor 30–49%, Very Poor <30%. Glare's published Getup homepage example landed at 73% (Good) — solid but with headroom for stronger visual hierarchy and brand tone.

**Common mistakes:**
- Confusing Appeal with Desirability — Appeal is the visual first-impression score; Desirability also captures wanting/likelihood to use.
- Reporting a single Appeal score without a benchmark or comparison version (one score in isolation isn't actionable).
- Treating a low Appeal score as "users will never engage" instead of as a visual-tone signal pointing at typography, imagery, or palette choices.

**Related metrics / pairings:** Pairs with **Sentiment** (which positive/negative words users associate with the design) and **Feelings** (emotional reaction). Often shows up alongside **Desirability** in concept tests. Compare Appeal across iterations to see whether visual changes are landing.

**Signal pattern:** "Users rate the redesigned homepage 73% Appeal vs. 58% for the current version, signalling that the cleaner hierarchy and bolder imagery are landing for marketing visitors — but Desirability of the offer itself is still flat, so the visual win isn't yet driving stated intent. Direction: ship the new visual treatment but keep iterating on the offer messaging."

---

### Brand Score

**What it measures:** A combined view of brand strength — the average of three sub-scores: Market Recognition, Sentiment, and Loyalty (NPS-derived).

**When to use:** Brand-level decisions, not page-level usability — brand redesigns, marketing tests, competitive research, positioning checks, campaign-effectiveness evaluation, feature-branding launches. Use Brand Score when you want a single rolled-up number that reflects how the brand is showing up across recognition, feeling, and advocacy.

**How it's calculated / collected:** Three questions: a multiple choice for Market Recognition (% who identify your brand), a multi-select sentiment question (% positive impressions), and an NPS 0–10 likelihood-to-recommend question (converted via `Loyalty = (NPS + 100) / 2`). `Brand Score = average of (Market Recognition %, Sentiment %, Loyalty %)`.

**Example values:** Same Very Good/Good/Average/Poor/Very Poor bands as other attitudinal scores. Glare's Slack homepage example landed at 67% (Average) — strong Recognition (72%) and Sentiment (84%) dragged down by Loyalty at 46%.

**Common mistakes:**
- Reporting Brand Score as a single number without showing the three components — one weak sub-score can mask two strong ones.
- Over-relying on Brand Score for product decisions when only one component is moving the average.
- Treating Brand Score as a substitute for Loyalty alone, or for Sentiment alone — it answers a different question.

**Related metrics / pairings:** Unbundles into **Sentiment**, **Loyalty**, and Market Recognition — always report the three alongside the composite. Pairs with **Feelings** for brand-emotion validation and with **Appeal** for visual-brand work.

**Signal pattern:** "Brand Score is 67% — within range for our category, but the breakdown shows Recognition strong (72%) and Sentiment strong (84%) while Loyalty drags at 46%. The homepage is communicating clearly to existing users but not converting visitors into recommenders. Direction: keep the visual system; rework messaging to address first-time visitor benefits and trust."

---

### Desirability

**What it measures:** How much users *want* what is being offered — emotional pull combined with stated intent to use or recommend.

**When to use:** Early-stage and pre-launch decisions where you need to know if the offering itself sparks interest before any behavior exists — new product or feature launches, homepage and landing-page first impressions, brand or visual updates, prioritization between concepts.

**How it's calculated / collected:** Two questions averaged. (1) Multiple-choice no-limit impression question (count of positive impressions / count of all impressions). (2) Likert likelihood-to-use scale (Very Unlikely=1 → Very Likely=5, average ÷ 5). `Desirability = (Impressions Score + Likelihood Score) / 2`.

**Example values:** Same scoring bands. Glare's Getup outfit-suggestion example earned 86% (Good) — 89% positive impressions and 82% likely-to-use.

**Common mistakes:**
- Confusing Desirability with Adoption — wanting is not using. Desirability is a stated intent signal, not a behavioral one.
- Using Desirability alone to greenlight a feature without behavioral validation.
- Reporting only the impression score or only the likelihood score instead of the average of both.

**Related metrics / pairings:** Pairs with **Appeal** (visual first-impression) and **Intent** (behavioral next-step). When Desirability is high but **Completion** is low, you have a concept-versus-execution gap.

**Signal pattern:** "The new event-based outfit feature lands at 86% Desirability — 89% of participants gave positive impressions and 82% say they'd use it. Pair with prototype Completion testing before scaling; users want the feature, but we have to validate they can complete it. Direction: greenlight build and run a Usability test on the prototype."

---

### Expectations

**What it measures:** How closely the experience matches what users thought would happen — the gap between assumption and delivery.

**When to use:** Anytime users come in with a mental model and we need to know whether the design met it — onboarding flows, new feature rollouts, redesigns, copy and messaging tests, navigation and workflow changes. Especially valuable when copy is making a promise the design has to keep.

**How it's calculated / collected:** Pre-experience free response ("what do you expect to happen?") + post-experience Likert (Failed Expectations=1 → Exceeded Expectations=5). `Expectations Score = (Σ Likert ratings / number of responses) ÷ 5`. The gap between the free-response answers and the actual experience is the diagnostic signal.

**Example values:** Same scoring bands. Glare's Getup example landed at 80% (Good) — 80% met or exceeded expectations, with a few users surprised by clarity and only 3% feeling the feature fell short.

**Common mistakes:**
- Asking only the post-experience rating without the pre-experience free response (the gap is the signal, not the number).
- Treating "exceeded expectations" as automatically good when the original expectation may have been wrong (users can expect too little).
- Using Expectations as a usability score — it's a mental-model fit score, not a task-success score.

**Related metrics / pairings:** Pairs with **Comprehension** (whether users understood) and **Satisfaction** (how they felt at the end). When Expectations are high but Satisfaction is low, the design over-promised. When Expectations match but Completion is low, the design is honest but blocking.

**Signal pattern:** "Pre-experience, users expected a guided quiz with outfit suggestions. Post-experience, 80% said the feature met or exceeded expectations and 3% said it fell short — the mental-model match is working. Direction: keep the current flow; clarify the one ambiguous option (closet suggestion) where neutral responses clustered."

---

### Feelings

**What it measures:** The emotional response a design evokes — focused specifically on the proportion of positive emotions (Trust and Joy) out of an eight-emotion set drawn from Plutchik's wheel.

**When to use:** When emotional impact is part of the goal — brand color tests, onboarding emotional tone, product or feature launches, content or messaging emotional resonance, brand imagery validation. Especially useful when the design needs to reassure, inspire, or build connection.

**How it's calculated / collected:** Multiple-choice question with eight emotion options (Anticipation, Trust, Joy, Surprise, Fear, Disgust, Sadness, Anger), participants select up to three. `Feeling = sum of Trust + Joy selections / sum of all emotion selections`.

**Example values:** Same scoring bands. Glare's Advent palette example landed at 43% (Poor) — top selections were Anticipation, Trust, and Joy, but notable Sadness (10%) and Disgust (8%) flagged emotional dissonance.

**Common mistakes:**
- Using Feelings to answer a usability question — it measures emotional response, not task success.
- Reporting only the positive emotion percentages without surfacing the negative emotions dragging the score down (the negatives are usually the actionable signal).
- Treating Feelings as interchangeable with Sentiment — Feelings uses a fixed emotion set; Sentiment uses descriptor words.

**Related metrics / pairings:** Lives next to **Sentiment** (which words users pick) and **Brand Score** (rolls Sentiment up). Pairs with **Appeal** for visual-tone work.

**Signal pattern:** "The new brand palette scored 43% on Feelings — Anticipation (33%) and Trust (30%) lead, but Sadness (10%) and Disgust (8%) signal the darker tones aren't landing the energetic identity the brand wants. Direction: keep the structure but pair the dark tones with brighter accents and re-test before launch."

---

### Loyalty

**What it measures:** Whether users would recommend the product to others — NPS-based, rescaled to 0–100 for easier comparison alongside other attitudinal metrics.

**When to use:** Long-term perception questions, post-launch retention analysis, product-market-fit signals, segment comparisons, subscription and renewal flows. Loyalty is a *long-arc* attitudinal metric — use it after users have had real experience with the product.

**How it's calculated / collected:** 0–10 likelihood-to-recommend question. Promoters = 9–10, Detractors = 0–6. `NPS = (Promoters − Detractors) / Total × 100`. `Loyalty = (NPS + 100) / 2`.

**Example values:** Same scoring bands. Glare's Advent example landed at 69% Loyalty / NPS 37 — strong early-stage advocacy with trust gaps among power users.

**Common mistakes:**
- Treating Loyalty as a launch metric — it works on long-term perception, not first impressions; running it on a prototype is the wrong tool.
- Conflating high Loyalty with high Satisfaction — loyal users can still be frustrated; satisfied users may not recommend.
- Ignoring the Detractor open responses — that's usually where the actionable signal lives.

**Related metrics / pairings:** Rolls up into **Brand Score**. Pairs with **Satisfaction** (how they felt at the end) and **Frequency** / **Visit Frequency** (whether they actually come back). Conflict warning: do not use Loyalty in place of Satisfaction on a single task.

**Signal pattern:** "Loyalty is 69% (NPS 37) — strong promoters at 50% but 37% Detractors, mostly citing reporting limitations. Direction: prioritise the analytics features detractors are calling out before next renewal cycle; expect Loyalty to be the lagging proof signal."

---

### Satisfaction

**What it measures:** How users feel at the end of an experience — a CSAT-based score answering whether the effort felt worth it.

**When to use:** Post-task evaluation specifically — complex workflows (onboarding, configuration), checkout experiences, feature interactions, post-onboarding emotional checks. Use Satisfaction *after* the task is finished, not mid-flow.

**How it's calculated / collected:** 5-point CSAT scale (Very Dissatisfied → Very Satisfied) immediately after the task. `Satisfaction = (Very Satisfied + Somewhat Satisfied participants) / total responses × 100`. Pair with a "why did you choose that?" qualitative follow-up.

**Example values:** Same scoring bands. Glare's Indiana University degree-search example landed at 71% (Good) — 71% satisfied, only 4% dissatisfied, 25% neutral.

**Common mistakes:**
- Asking Satisfaction at the wrong moment — it must come at task end, not mid-flow.
- Treating high Satisfaction as proof of usability when users may have ground through the task and rated the *outcome* positively while the *experience* was painful (always pair with Effort or Comprehension).
- Reporting Satisfaction without the qualitative follow-up that explains *why*.

**Related metrics / pairings:** Pairs with **Effort** (CES) and **Comprehension**. High Satisfaction + high Effort = users grinding through; high Satisfaction + low Comprehension = users didn't realize they missed something. Rolls up into broader emotional-quality patterns.

**Signal pattern:** "Degree search post-task Satisfaction is 71%, with users praising the clean filter layout but asking for more visual differentiation between program types. Direction: keep the layout; add brief program descriptions and program-type icons before next test cycle."

---

### Sentiment

**What it measures:** How a design makes users feel in the moment — the proportion of positive impressions out of all impressions selected from a paired positive/negative descriptor set.

**When to use:** In-the-moment emotional reads on visuals or content — concept tests, visual reviews, brand updates, design comparisons, post-onboarding or post-checkout reactions, microinteraction validation. Sentiment is fast, blunt, and good for design-direction comparison.

**How it's calculated / collected:** Multiple-choice no-limit descriptor question (e.g., 4 positive + 4 negative words). `Sentiment = positive impressions selected / all impressions selected`.

**Example values:** Same scoring bands. Glare's Indiana University brand-imagery example landed at 92% (Very Good) — Successful (60%), Relevant (56%), Diverse (43%) dominated with only ~14% negative impressions.

**Common mistakes:**
- Counting only positive impressions without the denominator of all impressions (the ratio is the score, not the count).
- Using Sentiment alone to make a launch decision — it's a directional signal, not a comprehensive one.
- Mistaking Sentiment for Loyalty — Sentiment is in-the-moment, Loyalty is forward-looking advocacy.

**Related metrics / pairings:** Rolls up into **Brand Score**. Pairs with **Feelings** (emotion-set version of the same question) and **Appeal** (Likert-version of the same first-impression read). Use Sentiment when you want descriptor words; use Feelings when you want emotion categories.

**Signal pattern:** "Brand-imagery set A scored 92% Sentiment vs 64% for set B — Successful, Relevant, and Diverse drove the positives; set B clustered around 'Confusing' and 'Boring.' Direction: move forward with imagery direction A across homepage and admissions."

---

### Usefulness

**What it measures:** Whether the design is practical, sustainable, and aligned with the business goal it serves — the long-term value signal that asks if a workflow keeps earning its place.

**When to use:** Long-term value evaluation, feature prioritization, post-adoption checks, evaluating whether a workflow is still pulling its weight or quietly becoming dead weight. Usefulness is the longitudinal cousin of Satisfaction and Desirability — those measure feeling at a moment; Usefulness asks if the experience keeps mattering.

**How it's calculated / collected:** *Source-doc note — the v1.32 Attitudinal subfolder doc titled "Usefulness" contains Sentiment-doc body text. The canonical Usefulness definition above is taken from the type-level Attitudinal doc table. In practice Usefulness is collected via Likert "how useful was this feature?" questions paired with frequency self-report and follow-up qualitative on why users keep coming back or stop.*

**Example values:** Same scoring bands as the other attitudinal metrics. Treat Usefulness as a slow-moving longitudinal score rather than a one-time launch number.

**Common mistakes:**
- Conflating Usefulness with Satisfaction — a useful workflow can still be frustrating; a satisfying workflow can still be useless once the novelty fades.
- Using Usefulness as a one-time post-launch check instead of as a longitudinal signal that should be re-measured across the lifecycle.
- Treating Usefulness as a behavioral metric — it's still an attitudinal score; pair it with **Frequency** / **Visit Frequency** for the behavioral proof.

**Related metrics / pairings:** Pairs with **Frequency**, **Visit Frequency**, and **Loyalty**. The three together answer: "Do users find this useful (Usefulness) → do they keep coming back (Visit Frequency) → would they recommend it (Loyalty)?" When Usefulness drops over time but Visit Frequency holds, look for habit-driven usage without real value — a churn risk.

**Signal pattern:** "Six months post-launch, the dashboard's Usefulness self-rating dropped from 78% to 61% even though Visit Frequency held steady. Users are still showing up but no longer rating it as useful — likely habit usage masking value erosion. Direction: re-interview a sample of habitual users, identify which sections still earn their place, and prune."

---

## The four sub-attributes (diagnostic)

Attitudinal metrics are often grouped together, but they measure different parts of the emotional experience. When the user has a soft "users seem unhappy," walk these four to find the actual signal.

### Trust

Whether users feel safe relying on the product, workflow, or recommendation. Especially important when users share sensitive information, AI generates recommendations, financial decisions are involved, or workflows automate important actions. Users may continue using the system while trust quietly weakens — that gap slowly reduces adoption, loyalty, and confidence over time.

### Confidence

Whether users feel sure about what they are doing. Low confidence often appears when onboarding feels unclear, navigation becomes confusing, workflows feel unpredictable, or AI recommendations lack explanation. Users may complete the task successfully while still feeling unsure the entire time, creating hesitation that traditional analytics fail to capture.

### Satisfaction

How users feel after completing the experience — smooth, frustrating, exhausting, rewarding, enjoyable. Satisfaction reflects the emotional quality of the interaction after the work is finished.

### Desirability

Whether users feel emotionally drawn toward the experience — visual appeal, excitement, preference, emotional connection, perceived quality. Two workflows may function equally well while one creates much stronger emotional momentum. This is often the difference between a workflow users tolerate and one they actively want to continue using.

---

## Combining attitudinal with other metrics

A single emotional score rarely explains the full experience. When emotional signals combine with behavioral and performance signals, larger patterns appear:

- **high completion + low confidence** → a trust gap
- **strong engagement + rising frustration** → hidden friction
- **low error rates + weak satisfaction** → workflow fatigue

Over time, these combined patterns help teams identify confusion traps, hesitation, trust breakdowns, weak onboarding experiences, and frustrating AI interactions. Hand off to `glare:ux-metrics-stack` for the stacking patterns.

---

## How attitudinal metrics help teams build better experiences

Attitudinal metrics help teams identify emotional friction earlier, improve onboarding confidence, strengthen trust, compare product directions, validate AI-assisted experiences, improve stakeholder alignment, and create stronger product reviews. Over time, these signals help teams build products that not only function well, but also feel clearer, safer, and more trustworthy.

---

## Helio path

Helio collects attitudinal metrics as **leading indicators** before product ships. Use Helio to capture Appeal, Sentiment, Feelings, Expectations, Desirability, and Satisfaction during prototype and concept testing — the scores serve as both predictive signals and proxy metrics, surfacing emotional friction in a controlled environment before launch.

## Source

Drafted from *Glare | UX Metrics, Attitudinal Metrics v1.32* (Drive doc `1vuyPfZ0HfRO2x9aVdVLuw7SB0WTeglAEWiZJ8kbFtpQ`, May 10, 2026), plus per-metric subfolder docs (`1VQitLkxOsxNXB3IuB5glrf8O9iIhWGVv`):

- Appeal (`1oM01UcVMZSDCOaUmS8PfojofDtc2bHff-0NZjhoHhKM`)
- Brand Score (`1IgdV0fMuLAmD6-XG1PlrN4cUVED8-4RUf8IJEWBT2tc`)
- Desirability (`1QkbVD_fn3z7l_PQjB4aIRxI-llA5CyORZRJGrrVIy8w`)
- Expectations (`185MhX78Mhu0WgRGgpbAOX_R7bdjb1Wxg5dF3dwcywb0`)
- Feelings (`1--4NMWKocOj1R7C8O_0hcpG-InQ3JV1ve5knP6jrNYQ`)
- Loyalty (`1hgFnN-2hzu3pWtKYih7lDERWgagFhh5qbZsxzqcZ6bM`)
- Satisfaction (`1riBOTICZnKLYu8d-9-K_fSaK3KH3YydFaI27Eov_mcA`)
- Sentiment (`1iLVbsMucJ_8OofLAeMfDtjzoLMVwgz8x7eYCki4B43E`)
- Usefulness (`1oZo62aV0EZOTNuQHfoNJV9bmg2oOBPn_nGJ_puh8fyM`) — *body content collision flagged; canonical definition taken from type-level doc*

## Failure modes

These are common ways this skill goes wrong in practice:

- **Inventing attitudinal metrics.** Borrowing names from other frameworks ("delight score," "happiness index") that aren't in the canonical nine. Stick to Appeal, Brand Score, Desirability, Expectations, Feelings, Loyalty, Satisfaction, Sentiment, Usefulness — or route to a different metric type.
- **Treating attitudinal as the whole picture.** High satisfaction with low completion is a recognizable trap — users say it's fine and never come back. Always pair with behavioral and performance metrics.
- **One-shot survey timing.** Capturing satisfaction once at end-of-task and treating it as the trust signal. Trust and confidence change *during* the workflow; capture at multiple moments.
- **Ignoring the leading-indicator nature.** Treating attitudinal as nice-to-have because it lags retention. The opposite is true — attitudinal usually leads, so attitudinal change predicts behavioral change downstream.

