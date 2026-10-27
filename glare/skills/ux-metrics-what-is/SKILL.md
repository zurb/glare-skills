---
name: ux-metrics-what-is
description: Use this skill when the user asks what a UX metric actually IS or how one is structured — phrases like "what is a UX metric," "what counts as a UX metric," "anatomy of a UX metric," "the four parts of a UX metric," "User Attribute — Data Type — Collection Method — Benchmark," "how is a UX metric built," "how do I structure a UX metric," "explain UX metrics simply," "UX metric vs analytics number," "UX metric vs KPI," "trust during onboarding example," "how do metrics turn fuzzy ideas into signals," "why does a metric need a benchmark," or "70 percent completion — is that good." Also use when the user is trying to write their first UX metric, debug a metric that feels incomplete, or distinguish a usable UX metric from a raw analytics number. Do NOT use for the four metric TYPES (use `glare:ux-metrics`), Define-stage metric picking (use `glare:define-ux-metrics`), or stacking metrics together (use `glare:ux-metrics-stack`).
version: 3.1.0
source_doc_version: v1.32
last_rebuilt: 2026-05-13
---

You are helping the user understand the **anatomy of a UX metric** — the four parts that turn a fuzzy reaction into something teams can measure, compare, and act on.

## Core idea

A UX metric is a way to measure how people experience a product, workflow, or system. Without measurement, teams rely on opinions, assumptions, stakeholder reactions, gut feelings, or surface-level analytics. With a UX metric, teams can move from "this feels confusing" to a measured score on trust, comprehension, effort, satisfaction, or any other attribute that names what the experience is actually doing for users. In Glare, every UX metric is built from four connected parts. Each part is small on its own; together they turn raw information into something clearer, comparable, and actionable.

## The four parts of a UX metric (v1.32)

1. **User Attribute** — what is being measured. The part of the experience the metric is about. This connects the metric back to the user need or experience the team wants to understand. An onboarding redesign may care about confidence, comprehension, and trust; a checkout workflow may care about effort, completion, and clarity.
2. **Data Type** — the family of signal being collected. Almost always one of three groups (the v1.32 Four Parts doc folds Intelligence into the broader framework but uses three groups here for measurement structure):
   - *Attitudinal* — confidence, trust, satisfaction, desirability — emotional response and perception.
   - *Behavioral* — clicks, navigation behavior, engagement, hesitation, completion patterns — interaction behavior across the workflow.
   - *Performance* — completion rate, time on task, error rate, abandonment, workflow efficiency — operational friction and efficiency.
3. **Collection Method** — where the information comes from. Usability testing, surveys, analytics, interviews, session recordings, AI-assisted evaluations. Different collection methods reveal different problems — analytics surface abandonment and slower onboarding; interviews surface hesitation and confidence concerns. The collection method shapes what kind of understanding the metric produces.
4. **Benchmark** — the comparison point that gives the number meaning. A 70% completion score may sound strong, but not if the previous workflow scored 88%, or if competitors consistently score higher. Benchmarks may include previous versions, industry averages, competitor comparisons, internal targets, or earlier test results. Without a benchmark, the metric is trivia.

## The trust-during-onboarding example (canonical v1.32 worked example)

A team wants to know whether users feel confident during onboarding. The four parts:

- **Attribute** — Trust
- **Data Type** — Attitudinal
- **Collection Method** — Post-test survey
- **Benchmark** — Previous onboarding flow / competitor onboarding / target confidence score

At first the onboarding flow may look successful because completion stays high. The UX metric reveals lower confidence, weaker trust, rising hesitation, and confusion during setup. Without the metric, the team would have assumed the onboarding was healthy because users finished the workflow. The metric explains how the experience actually felt.

## Read the reference first

Before answering, read `reference.md` — it carries the full v1.32 What Is a UX Metric content (each of the four parts in detail, the full trust example, why metrics turn fuzzy ideas into signals, and how metrics become more valuable together).

## How to apply

1. **Use the four parts as a build checklist.** When a user is writing their first UX metric or debugging one that "feels off," walk through Attribute → Data Type → Collection Method → Benchmark. The most common failure is missing a benchmark — the team has a number but no comparison point, so the number cannot guide a decision.

2. **Tie the Attribute back to the audience and need.** The Attribute is not arbitrary — it should connect to the user need being explored (from `glare:define-user-needs`) and the workflow under evaluation. A fintech onboarding flow is more likely to need Trust than a marketing landing page; a checkout flow is more likely to need Effort than Satisfaction.

3. **Match Data Type to question, not to convenience.** Attitudinal data answers "how do users feel," Behavioral data answers "what do users do," Performance data answers "how efficiently does the workflow run." If the team picks the wrong type, the metric will not answer the actual question. Engagement is not a substitute for Trust.

4. **Pick a Collection Method that matches the workflow stage.** Helio surveys and prototype tests work as Predictive / Proxy collection methods before launch. Live analytics works as a Lagging method after launch. Most teams over-rely on analytics and learn too late.

5. **Always state the Benchmark out loud.** The most common mistake is reporting a single number with no comparison ("we got 73%"). Make the benchmark explicit — previous version score, competitor score, internal target, earlier test result. If no benchmark exists, the next move is to establish one before the metric is reported again.

6. **Single metric is rarely enough.** A single UX metric explains one small part of the experience. When metrics work together inside a UX Metric Stack, larger patterns emerge (high completion + low confidence = trust problem; strong engagement + rising effort = friction; low errors + weak comprehension = hidden confusion). Hand off to `glare:ux-metrics-stack` once the four parts are in place.

## Handoffs

- For the broader UX Metrics framework and the four metric TYPES, route to `glare:ux-metrics`.
- For Define-stage metric picking on a specific decision (the four lenses, vanity vs actionable, etc.), route to `glare:define-ux-metrics`.
- For combining 3-7 metrics into a Design Stack or Research Stack, route to `glare:ux-metrics-stack`.
- For the per-metric definitions of attitudinal, behavioral, and performance metrics, route to `glare:ux-metrics-attitudinal`, `glare:ux-metrics-behavioral`, `glare:ux-metrics-performance`.
- For why measurement matters now (the AI-acceleration argument), route to `glare:ux-metrics-why`.
- For UX metrics as a connected operational system, route to `glare:ux-metrics-system`.
- For the six-piece anatomy of a Design Signal that uses a metric, route to `glare:signals-components`.
- For mapping a UX metric upward to product KPI to business KPI, route to `glare:lead-mapping`. For the Decision Map as a whole, route to `glare:decision-map`.
