# Attitudinal Metrics — Reference (v1.32)

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

---

## The nine attitudinal metrics (v1.32)

| Metric | Definition | When to use | Common mistakes |
|---|---|---|---|
| **Appeal** | How a design looks and feels at first glance — the gut reaction users have before interacting. | Early-stage concepts, layout comparisons, landing pages, marketing screens, brand-refresh validation, A/B testing of visual variations. | Confusing Appeal with Desirability (Appeal is purely visual first-impression; Desirability is wanting the offering); reporting a single Appeal score with no benchmark; treating low Appeal as "users will never engage" instead of as a visual-tone signal. |
| **Brand Score** | A combined view of brand strength averaging recognition, sentiment, and loyalty (NPS-derived). | Brand redesigns, marketing tests, competitive research, positioning checks, campaign-effectiveness evaluation, feature-branding launches. | Reporting Brand Score without showing the three component scores (recognition, sentiment, loyalty); over-relying on it for product decisions when one component is dragging the average; treating it as a substitute for Loyalty alone. |
| **Desirability** | How much people *want* what you're offering — emotional pull and stated intent to use. | New product or feature launches, homepage / landing page first impressions, brand or visual updates, prioritization between concepts. | Confusing Desirability with Adoption (wanting is not using); using Desirability alone to greenlight a feature without behavioral validation; not pairing the impression score with the likelihood-to-use score. |
| **Expectations** | How closely the experience matches what users thought would happen — gap between assumption and delivery. | Onboarding flows, new feature rollouts, redesigns where users come in with mental models, copy and messaging tests, navigation and workflow changes. | Asking only the post-experience rating without the pre-experience free response (the gap is the signal); treating "exceeded expectations" as automatically good when the original expectation may have been wrong. |
| **Feeling** | The emotional response a design evokes — focused on positive emotions Trust and Joy out of an eight-emotion set. | Brand color tests, onboarding emotional tone, product / feature launches, content or messaging emotional resonance, brand imagery validation. | Using Feeling to answer a usability question (it measures emotional response, not task completion); reporting only the positive emotions without the negatives that pulled the score down. |
| **Loyalty** | Whether users would recommend the product (NPS-based, scaled to 0-100). | Long-term perception, post-launch retention analysis, product-market-fit signals, segment comparisons, subscription and renewal flows. | Treating Loyalty as a launch metric (it works on long-term perception, not first impressions); conflating high Loyalty with high satisfaction (loyal users can still be frustrated); ignoring the Detractor comments which usually carry the actionable signal. |
| **Satisfaction** | How users feel at the end of an experience — CSAT-based score for whether the effort felt worth it. | Post-task evaluation, complex workflows (onboarding, configuration), checkout experiences, feature interactions, post-onboarding emotional check. | Asking Satisfaction at the wrong moment (it must come at task end, not mid-flow); treating high Satisfaction as proof of usability when users may have ground through; not pairing with comprehension or effort. |
| **Sentiment** | How a design makes users feel in the moment — proportion of positive impressions out of all impressions selected. | Concept tests, visual reviews, brand updates, design comparisons, post-onboarding / post-checkout reactions, microinteraction validation. | Counting only positive impressions without the denominator of all impressions; using Sentiment alone to make a launch decision; mistaking it for Loyalty (Sentiment is in-the-moment, Loyalty is forward-looking). |
| **Usefulness** | Whether the design is practical, sustainable, and aligned with business goals for long-term success. | Long-term value evaluation, feature prioritization, post-adoption check, evaluating whether a workflow keeps earning its place. | Conflating Usefulness with Satisfaction (a useful workflow can still be frustrating); using Usefulness as a one-time check instead of as a longitudinal signal. *(Source-doc note — the v1.32 Attitudinal subfolder doc titled "Usefulness" contains Sentiment-doc body text; the canonical Usefulness definition is taken from the Attitudinal type-level doc table.)* |

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

Over time, these combined patterns help teams identify confusion traps, hesitation, trust breakdowns, weak onboarding experiences, and frustrating AI interactions. Hand off to `glare-ux-metrics-stack` for the stacking patterns.

---

## How attitudinal metrics help teams build better experiences

Attitudinal metrics help teams identify emotional friction earlier, improve onboarding confidence, strengthen trust, compare product directions, validate AI-assisted experiences, improve stakeholder alignment, and create stronger product reviews. Over time, these signals help teams build products that not only function well, but also feel clearer, safer, and more trustworthy.

---

## Helio path

Helio collects attitudinal metrics as **leading indicators** before product ships. Use Helio to capture Appeal, Sentiment, Feeling, Expectations, Desirability, and Satisfaction during prototype and concept testing — the scores serve as both predictive signals and proxy metrics, surfacing emotional friction in a controlled environment before launch.

## Source

Drafted from *Glare | UX Metrics, Attitudinal Metrics v1.32* (Drive doc `1vuyPfZ0HfRO2x9aVdVLuw7SB0WTeglAEWiZJ8kbFtpQ`, May 10, 2026), plus per-metric subfolder docs (`1VQitLkxOsxNXB3IuB5glrf8O9iIhWGVv`):

- Appeal (`1oM01UcVMZSDCOaUmS8PfojofDtc2bHff-0NZjhoHhKM`)
- Brand Score (`1IgdV0fMuLAmD6-XG1PlrN4cUVED8-4RUf8IJEWBT2tc`)
- Desirability (`1QkbVD_fn3z7l_PQjB4aIRxI-llA5CyORZRJGrrVIy8w`)
- Expectations (`185MhX78Mhu0WgRGgpbAOX_R7bdjb1Wxg5dF3dwcywb0`)
- Feeling (`1--4NMWKocOj1R7C8O_0hcpG-InQ3JV1ve5knP6jrNYQ`)
- Loyalty (`1hgFnN-2hzu3pWtKYih7lDERWgagFhh5qbZsxzqcZ6bM`)
- Satisfaction (`1riBOTICZnKLYu8d-9-K_fSaK3KH3YydFaI27Eov_mcA`)
- Sentiment (`1iLVbsMucJ_8OofLAeMfDtjzoLMVwgz8x7eYCki4B43E`)
- Usefulness (`1oZo62aV0EZOTNuQHfoNJV9bmg2oOBPn_nGJ_puh8fyM`) — *body content collision flagged; canonical definition taken from type-level doc*
