# UX Metrics — Reference (top-level Glare framework, v1.32)

## What UX metrics are

UX Metrics are the measurement system teams use to understand how people experience a product, workflow, service, interface, or AI-assisted system. Inside product teams, decisions happen constantly — which concept moves forward, where onboarding breaks down, why users hesitate, whether AI recommendations actually help, which workflow creates less friction, what deserves more investment. Most teams already have data; the harder problem is understanding what the experience actually feels like for users while work is still evolving.

UX metrics help teams evaluate workflows, compare product directions, expose friction, reduce uncertainty, strengthen reviews, and guide decisions earlier — before launch, while concepts and product directions are still moving.

> **Version history of the metric-type taxonomy.**
>
> - **v1.0** — defined **3 types**: Attitudinal · Behavioral · Performance.
> - **v1.1** — briefly proposed a fourth "Perceptual" type. Removed.
> - **v1.3 (canonical, May 2025)** — defined **4 types**: Attitudinal · Behavioral · Performance · **Intelligence** (AI-assisted experience quality). Comprehension and recognition (which v1.1 put under "Perceptual") live inside Behavioral.
> - **v1.32 (May 10, 2026)** — same 4-type taxonomy as v1.3. The v1.32 source folder ships full per-metric subfolders for the first three types only; Intelligence is named in the Overview and Measurement System docs but does not yet have its own subfolder of per-metric docs.

This reference covers the top-level framework. For Define-stage metric *picking* on a specific decision, see `glare:define-ux-metrics`. For each type's per-metric summaries, see `glare:ux-metrics-attitudinal`, `glare:ux-metrics-behavioral`, `glare:ux-metrics-performance`.

## AI increased the need for stronger measurement systems

AI made it easy for teams to generate more ideas, screens, prompts, workflows, prototypes, and experiments. What did not speed up at the same pace was evaluation. Many organizations now produce more output than they can consistently review, compare, or validate. Product reviews fragment. Stakeholders interpret success differently. Teams move quickly while confidence weakens underneath.

UX metrics help teams slow down the right part of the work — evaluation, interpretation, comparison, validation, decision-making. The goal is not more reporting; it is clearer direction under pressure.

---

## When to use

- When the user asks about UX Metrics as a top-level Glare framework.
- When introducing the four UX metric types — Attitudinal · Behavioral · Performance · Intelligence (AI-assisted experience quality).
- When the user wants the overview (Why → What Is → Measurement System → Attitudinal → Behavioral → Performance → Stack → Mapping → Applying).
- When clarifying how UX metrics differ from signals and from business KPIs.
- When the team is comparing UX metrics, signals, and business KPIs and needs the relationships named.
- When introducing UX metrics as the measurement layer underneath Design Signals, AI Skills, Design Reviews, and Decision Maps.

**Don't use when** the user is in Define-stage metric picking on a specific decision (`glare:define-ux-metrics`) or asking about the Need / Use / Prefer / Adopt signal-type taxonomy (`glare:signals-types`).

## The four UX metric types (v1.32)

### Attitudinal — how users feel

Emotional response, trust, confidence, satisfaction, perceived value. These signals often reveal problems before larger business metrics begin changing. Users may complete onboarding while confidence quietly drops; AI recommendations may increase engagement while trust weakens; satisfaction may stay positive while frustration slowly grows.

**Examples (v1.32):** Appeal, Brand Score, Desirability, Expectations, Feeling, Loyalty, Satisfaction, Sentiment, Usefulness.

### Behavioral — what users actually do

Whether users hesitate, get confused, abandon workflows, or complete actions. Users may repeatedly scan navigation before clicking; onboarding may technically succeed while users struggle to understand what happens next; AI-assisted workflows may create hidden confusion even when completion looks high.

**Examples (v1.32):** Completion, Comprehension, Effort, Engagement, Frequency, Intent, Success, Usability.

### Performance — efficiency and reliability

Where systems slow users down or create unnecessary effort. A checkout flow may have strong completion but extremely high effort; users may finish a task successfully while taking much longer than expected; error frequency may rise after introducing AI-generated recommendations.

**Examples (v1.32 Overview):** Abandonment Rate, Bounce Rate, Click-Through Rate, Completion Rate, Drop-off Rate, Error Frequency, Error Rate, Recency, Session Duration, Time on Task, Visit Frequency.

### Intelligence — AI-assisted experience quality

As AI becomes part of product workflows, teams need stronger ways to evaluate whether intelligence improves understanding or simply increases output. Recommendations may appear useful while users quietly lose confidence; AI guidance may speed up workflows while increasing comprehension problems; automated suggestions may increase activity while creating hesitation during decisions.

**Scope (v1.32):**
- recommendation quality
- prompt effectiveness
- AI guidance usefulness
- adaptation quality
- confidence calibration
- workflow assistance

Together, the four types give a full picture: how users feel, what they do, how well the system performs, and whether AI assistance helps. Ignore one and the picture distorts.

---

## How UX metrics fit into Glare

UX Metrics are the measurement layer underneath the larger Glare system. They support:

- Design Signals
- AI Skills
- Design Reviews
- Decision Maps
- organizational assessments

As metrics accumulate across workflows and decisions, patterns become easier to see. Teams begin understanding where users hesitate, where trust weakens, which concepts perform better, where workflows create friction, and what deserves momentum. This helps teams create stronger signals before weak decisions spread further into the product.

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

## The nine sub-areas (v1.32)

The full UX Metrics section is organized into nine connected areas:

1. **Why UX Metrics Matter** — why product teams need stronger evaluation systems as AI increases output, experimentation, and decision complexity. Sub-skill — `glare:ux-metrics-why`.
2. **What Is a UX Metric?** — how UX metrics are structured (User Attribute, Data Type, Collection Method, Benchmark), measured, benchmarked, and interpreted. Sub-skill — `glare:ux-metrics-what-is`.
3. **Measurement System** — how UX Metrics work together as a connected operational system across workflows, reviews, testing, and decision-making. Sub-skill — `glare:ux-metrics-system`.
4. **Attitudinal Metrics** — how users feel (9 metrics). Sub-skill — `glare:ux-metrics-attitudinal`.
5. **Behavioral Metrics** — what users do (8 metrics). Sub-skill — `glare:ux-metrics-behavioral`.
6. **Performance Metrics** — efficiency, friction, reliability (11 metrics). Sub-skill — `glare:ux-metrics-performance`.
7. **UX Metric Stacks** — combining 3-7 metrics together to evaluate workflows, journeys, and product experiences. Sub-skill — `glare:ux-metrics-stack`.
8. **Mapping Design Impact** — connecting UX metrics to product outcomes, business goals, and organizational decisions through Situation → Intent → Outcomes → Results. Sub-skill — `glare:ux-metrics-mapping`.
9. **Applying UX Metrics** — how teams use UX metrics inside testing, reviews, benchmarking, and decision workflows. Sub-skill — `glare:ux-metrics-applying`.

---

## From metrics to decisions

Organizations already have more dashboards, analytics, and feedback than they can consistently interpret. The challenge is not collecting more numbers — it is turning numbers into clearer decisions before momentum disappears. UX Metrics, applied across Glare, help teams compare onboarding flows, identify hesitation before launch, expose friction in AI-assisted workflows, strengthen design reviews, improve stakeholder alignment, reduce rework, validate concepts earlier, and build more confidence in product direction.

Over time, UX Metrics become part of how teams make product decisions together. They help teams compare ideas earlier, spot friction before launch, and build stronger alignment around what deserves momentum. As patterns build, teams gain clearer visibility into what is helping users move forward and where the experience still breaks down.

---

## Source-doc inconsistencies flagged in v1.32

- **Performance Metrics Overview-vs-subfolder mismatch.** The v1.32 Overview lists "Abandonment Rate" as the first Performance metric, but the Performance subfolder ships 11 docs that include both `abandonment-rate` (referenced in the type-level doc table) AND `completion` (which duplicates the Behavioral Completion metric). The type-level Performance doc table lists 11 docs with the same set as the Overview minus "Completion" plus "Abandonment Rate". The `glare:ux-metrics-performance` skill uses the Overview/type-level list as the source of truth.
- **Usefulness doc body collision.** The Attitudinal subfolder doc titled "Usefulness" contains Sentiment-doc body content (likely a copy-paste error in the source). The canonical Usefulness definition is taken from the Attitudinal type-level doc and the v1.0/v1.3 description ("whether the design is practical, sustainable, and aligned with business goals for long-term success").
- **Mapping Design Impact "decisions/" trailing slash.** The Overview's "Mapping Design Impact" bullet ends with a trailing `/` instead of a period — purely cosmetic.
- **Behavioral Metrics doc version banner.** The Behavioral type-level doc carries a "v1.3" version banner inside the body even though the file is v1.32. Treat as a banner-only stale stamp; content matches v1.32.
- **The Overview bullet swap that affected v1.0 — NOT present in v1.32.** Attitudinal correctly lists Appeal/Brand Score/Desirability/Expectations/Feeling/Loyalty/Satisfaction/Sentiment/Usefulness; Behavioral correctly lists Completion/Comprehension/Effort/Engagement/Frequency/Intent/Success/Usability.

---

## Failure modes

These are common ways this skill goes wrong in practice:

- **Single-type measurement.** Anchoring the whole framework on one type (usually Behavioral). The four-type model exists because no single type catches everything — attitudinal leads, behavioral shows action, performance shows cost, intelligence catches AI-assisted experience quality.
- **Skipping Intelligence.** The v1.32 fourth type addresses AI-assisted experiences specifically — recommendation quality, prompt effectiveness, AI guidance usefulness. Treating it as optional misses the central case for v1.32.
- **Confusing UX metrics with business KPIs.** Reporting "retention up" as a UX metric. Retention is a business KPI; UX metrics are the leading attribute-anchored signals that explain *why* retention moved.
- **Routing too late.** Staying in `glare:ux-metrics` when the user is actually in the Define stage for a specific decision (`glare:define-ux-metrics`) or working on a specific metric family (route to the type sub-skill).

## Related key terms

- **Four UX Metric Types** — Attitudinal, Behavioral, Performance, Intelligence (v1.3/v1.32 canonical).
- **Four Parts of a UX Metric** — User Attribute, Data Type, Collection Method, Benchmark (from v1.32 What Is a UX Metric).
- **UX Metric Stack** — a reusable group of 3-7 UX metrics combined to evaluate a larger workflow, feature, product area, or research situation.
- **Design Stack vs Research Stack** — Design Stacks organize metrics around a workflow or product experience; Research Stacks organize metrics around a research method or evaluative process.
- **Confusion Trap, Friction Wall, Trust Gap, Commitment Check** — the four recurring patterns surfaced by stacks.
- **Situation → Intent → Outcomes → Results** — the four stages of mapping design impact, aligned with Define / Measure / Focus / Lead.
- **Signal** — a measurable, trustworthy piece of evidence. The unit of credibility in Glare.
- **Helio** — in-house testing platform; collects attitudinal and behavioral metrics as leading indicators / proxies before launch.

## Source

Drafted from the v1.32 Drive folder (`1F-6tXs88ekDeiAVwhgHujq8HKEoZ13Hz`), all docs dated May 10, 2026:

- *Glare | UX Metrics, Overview v1.32* (`1-bkqUaypPkvzGijTOR1k_R3GpQzrFNVWtM4PiMvaF00`)
- *What is a UX Metric? v1.32* (`1-teouWMYjBy2sltDWjVvP5BXfolBfZe5dzp_zf9qGHk`)
- *Why UX Metrics Matter v1.32* (`1g0lrMvS2ZsgokpS3q7xeIxIaoeuPeqvv6nMpJTIWcoI`)
- *Measurement System v1.32* (`1Ll6Z-4NiIBDu6jBpMQGgKx_SR21YWtRnC1ptsO4KUNU`)
- *Attitudinal / Behavioral / Performance / Stack / Mapping / Applying* (sibling docs in same folder)

Cross-referenced with the existing `glare:define-ux-metrics` skill (v1.6.0) for voice and structure consistency.
