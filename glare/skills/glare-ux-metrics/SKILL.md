---
name: glare-ux-metrics
description: Use this skill when the user asks about UX Metrics as a top-level Glare framework — phrases like "what are UX metrics," "the four UX metric types," "Attitudinal · Behavioral · Performance · Intelligence," "AI metrics," "Intelligence metrics," "metrics vs signals vs business KPIs," "how do metrics work across Glare," "build a metric system," "operationalize metrics," "UX metric stacks," "benchmarking with metrics," "AI + metrics," or wants the overview of the seven UX Metrics sub-sections (Types, Metric Structures, Building Metrics, Operationalizing Metrics, Using with Design Signals, UX Metric Stacks, AI + Metrics). Also use when the user wants to understand how UX metrics power Design Signals, Design Reviews, AI workflows, and benchmarking systems across the framework. Do NOT use for Define-stage metric picking on a specific decision (use `glare-define-ux-metrics`) or for the Need / Use / Prefer / Adopt signal-type taxonomy (use `glare-signals-types`).
version: 1.6.0
source_doc_version: v1.3
last_rebuilt: 2026-05-08
---

You are helping the user understand and apply **UX Metrics** as a top-level system in Glare — the measurement layer that sits underneath Design Signals and powers every facet of the framework.

## Core idea

UX metrics are measurable ways to understand how people experience a product, workflow, service, or interface. They quantify how users feel, what users do, where friction exists, how efficiently tasks work, and — newly in v1.3 — whether AI systems actually help users move forward.

Inside Glare, UX metrics are foundational. They create a shared structure for how teams collect, interpret, compare, and discuss user data across the Decision Map, Design Signals, Design Reviews, AI workflows, assessments, benchmarking systems, and product decisions. User data is normally inconsistent across organizations — different definitions, fragmented metrics, disconnected dashboards, conflicting interpretations of success. Glare brings structure to that complexity.

## Why metrics matter

Data is everywhere, but clarity is still rare. AI accelerated the number of concepts, experiments, prototypes, and AI-assisted workflows teams can generate. What did not accelerate at the same pace was validation, alignment, and organizational confidence. That gap creates friction — weak ideas survive too long, strong ideas stall in debate, and decisions drift without clear evidence.

UX metrics help teams evaluate direction, compare ideas, expose friction, reduce decision risk, and connect design work to measurable outcomes. Instead of waiting for post-launch analytics, teams can validate concepts earlier, compare competing directions, and build stronger signals while decisions are still being made.

## The four UX metric types

Glare organizes UX metrics into four primary types. The taxonomy moved from three types (v1.0) to four in v1.3, with **Intelligence** added for AI-assisted experience quality.

- **Attitudinal — how users feel.** Emotional response and perceived value. Examples — Appeal, Brand Score, Desirability, Expectations, Feeling, Loyalty, Satisfaction, Sentiment, Usefulness.
- **Behavioral — what users actually do.** Whether users move through the experience or abandon it. Examples — Completion, Comprehension, Effort, Engagement, Frequency, Intent, Success, Usability.
- **Performance — efficiency, reliability, operational friction.** Where systems slow users down or create unnecessary effort. Examples — Abandonment Rate, Bounce Rate, Click-Through Rate, Completion Rate, Drop-off Rate, Error Frequency, Error Rate, Recency, Session Duration, Time on Task, Visit Frequency.
- **Intelligence — AI-assisted experience quality (NEW in v1.3).** Whether intelligence is actually improving outcomes instead of simply generating more output. Scope — recommendation quality, prompt effectiveness, AI guidance usefulness, adaptation quality, confidence calibration, workflow assistance.

Together, the four types give a full picture: how users feel, what they do, how well the system performs, and whether AI assistance helps. Ignore one and the picture distorts.

## Where UX metrics fit in Glare

UX metrics support every part of the framework:

- **Define** — clarify what success should look like before work begins.
- **Measure** — validate concepts, hunches, and experiments.
- **Focus** — compare directions and expose tradeoffs.
- **Lead** — connect design work to measurable outcomes leaders can act on.

UX metrics also power Design Signals (they're the structural layer underneath the six-piece signal anatomy), Design Reviews, benchmarking systems, AI-assisted evaluations, continuous discovery workflows, and organizational assessments. As signals accumulate, teams gain stronger visibility into what is working, where friction exists, and which decisions deserve momentum.

## The seven sub-sections (planned)

The full UX Metrics section is organized into seven areas that help teams build stronger measurement systems over time:

1. **Types** — the major categories of UX metrics and what each reveals (Attitudinal · Behavioral · Performance · Intelligence).
2. **Metric Structures** — how metrics evolve across time, stages, engagement, and comparison models (the four lenses).
3. **Building Metrics** — creating metric systems tied to user needs, workflows, and business outcomes.
4. **Operationalizing Metrics** — using baselines, benchmarking, scorecards, and comparative testing inside product work.
5. **Using with Design Signals** — connecting metrics to signals, decisions, and measurable direction.
6. **UX Metric Stacks** — reusable metric systems for onboarding, navigation, dashboards, checkout flows, AI workflows, and more.
7. **AI + Metrics** — how AI changes evaluation, scoring consistency, prompt quality, and signal generation.

This skill ships the top-level orientation. Sub-sections are planned in the v1.3 source and arriving incrementally — when a user asks for one, point them at the relevant Glare facet skill that already covers most of it (Building Metrics overlaps with `glare-define-ux-metrics`, Operationalizing overlaps with `glare-measure`, Using with Signals overlaps with `glare-signals-components`).

## From metrics to decisions

Organizations already have more data than they can interpret. The challenge is not collecting numbers — it's turning numbers into clear decisions before momentum disappears. UX metrics, applied across Glare, help teams see friction earlier, compare ideas faster, reduce uncertainty, strengthen signals, protect momentum, and prove impact more clearly. Over time, measurement stops being something teams report on after the work is finished and becomes part of how teams decide what deserves to move forward.

## Read the reference first

Before answering, read `reference.md` — it contains the version history of the metric-type taxonomy, full details on each of the four types (including the Intelligence type added in v1.3), the four lenses (Type, Stage, Time, Engagement), the four critical comparisons, the four quality principles, the seven planned sub-sections in detail, and the diagnostic mismatch patterns.

## How to apply

1. **Orient on the four types.** When a user is choosing what to measure for the first time or reviewing an existing dashboard, walk through Attitudinal · Behavioral · Performance · Intelligence. If AI is part of the experience, Intelligence is non-optional. If a team has only one type, the picture is distorted.

2. **Show where metrics live in the framework.** UX metrics are not just a Define-stage exercise — they're the connective tissue under Signals, Reviews, AI workflows, and assessments. When a user is confused about whether they need "metrics" or "signals" or "KPIs," the answer is usually all three at different layers, with UX metrics as the connector.

3. **Pick the right next move.**
   - For **picking metrics for a specific decision** in Define, hand off to `glare-define-ux-metrics`.
   - For **building a hunch or running questioning against a metric**, hand off to `glare-measure-hunches` or `glare-measure-questioning`.
   - For **mapping a UX metric upward to product KPI to business KPI**, hand off to `glare-lead-mapping`.
   - For **the six-piece anatomy of a signal that uses a metric**, hand off to `glare-signals-components`.
   - For **the Need / Use / Prefer / Adopt signal-type taxonomy** (a different question — not what to measure, but what kind of signal you're missing), hand off to `glare-signals-types`.

4. **Bring AI metrics in deliberately.** Intelligence metrics are new and unfamiliar — when the user mentions AI features, name the six scope areas (recommendation quality · prompt effectiveness · AI guidance usefulness · adaptation quality · confidence calibration · workflow assistance) and pair them with at least one Behavioral or Attitudinal metric so the team isn't only looking at the AI in isolation.

5. **End with a concrete next step.** This is a top-level orientation skill — its job is to put the user on the right path. Always close with the named skill they should drop into next.

## Handoffs

- For Define-stage metric picking on a specific decision, route to `glare-define-ux-metrics`.
- For the Need / Use / Prefer / Adopt signal-type taxonomy, route to `glare-signals-types`.
- For the six-piece signal anatomy, route to `glare-signals-components`.
- For the Decision Map as a whole, route to `glare-decision-map`.
- For Design Signals as a top-level concept, route to `glare-design-signals`.
- For Design Reviews, route to `glare-design-review`.
- For Design Assessment (team / org maturity), route to `glare-design-assessment`.
- For onboarding and "what is Glare," route to `glare-get-started`.
