---
name: ux-metrics
description: Use this skill when the user asks about UX Metrics as a top-level Glare framework — phrases like "what are UX metrics," "the four UX metric types," "Attitudinal — Behavioral — Performance — Intelligence," "AI metrics," "Intelligence metrics," "metrics vs signals vs business KPIs," "how do metrics work across Glare," "UX metric stacks," "what is a UX metric," "why UX metrics matter," "measurement system," "mapping design impact," "applying UX metrics," or wants the overview of the UX Metrics section (Why — What Is — Measurement System — Attitudinal — Behavioral — Performance — Stack — Mapping — Applying). Also use when the user wants to understand how UX metrics power Design Signals, Design Reviews, and AI workflows, or wants to drop into a sub-skill. Do NOT use for Define-stage metric picking on a specific decision (use `glare:define-ux-metrics`) or the Need / Use / Prefer / Adopt signal-type taxonomy (use `glare:signals-types`).
version: 3.1.0
source_doc_version: v1.32
last_rebuilt: 2026-05-13
---

You are helping the user understand and apply **UX Metrics** as a top-level system in Glare — the measurement layer that sits underneath Design Signals and powers every facet of the framework.

## Core idea

UX metrics are measurable ways to understand how people experience a product, workflow, service, interface, or AI-assisted system. They quantify how users feel, what users do, where friction exists, how efficiently tasks work, and whether AI systems actually help users move forward. Inside Glare, UX metrics are the operational measurement layer underneath Design Signals, AI Skills, Design Reviews, Decision Maps, and organizational assessments. They give product, design, research, engineering, and leadership teams a shared way to evaluate the experience while it is still moving — not only after launch.

## Why metrics matter (v1.32)

AI made it easy for teams to generate more ideas, screens, prompts, workflows, prototypes, and experiments. Evaluation did not speed up at the same pace. Many organizations now produce more output than they can consistently review, compare, or validate. Reviews fragment. Stakeholders interpret success differently. Teams move quickly while confidence weakens underneath. UX metrics help teams slow down the right part of the process — evaluation, interpretation, comparison, validation, decision-making — so weak ideas surface earlier and strong ones are protected.

## The four UX metric types

Glare organizes UX metrics into four connected measurement areas. Each helps teams understand a different part of the experience.

- **Attitudinal — how users feel.** Emotional response, trust, confidence, satisfaction, perceived value. Examples — Appeal, Brand Score, Desirability, Expectations, Feeling, Loyalty, Satisfaction, Sentiment, Usefulness.
- **Behavioral — what users actually do.** Whether users move through the experience, hesitate, or abandon. Examples — Completion, Comprehension, Effort, Engagement, Frequency, Intent, Success, Usability.
- **Performance — efficiency, reliability, operational friction.** Where systems slow users down or create unnecessary effort. Examples — Abandonment Rate, Bounce Rate, Click-Through Rate, Completion Rate, Drop-off Rate, Error Frequency, Error Rate, Recency, Session Duration, Time on Task, Visit Frequency.
- **Intelligence — AI-assisted experience quality.** Whether intelligence is actually improving outcomes instead of simply generating more output. Scope — recommendation quality, prompt effectiveness, AI guidance usefulness, adaptation quality, confidence calibration, workflow assistance.

The v1.32 source folder ships full per-metric docs for the first three types. Intelligence is documented in the Overview and Measurement System docs but does not yet have its own subfolder of per-metric docs — it is acknowledged here as the fourth type and will get its own sub-skill once that content lands.

> **Version note.** v1.0 used 3 types. v1.1 briefly added a "Perceptual" type — removed. The canonical taxonomy is the v1.3/v1.32 four-type model above. Comprehension and recognition (which v1.1 grouped under "Perceptual") now live inside Behavioral.

## The new sub-skill library (v1.32)

The UX Metrics section is now organized into nine sub-skills. Each has its own SKILL.md and reference.md. Use this map to route.

1. `glare:ux-metrics-what-is` — the four parts of any UX metric (User Attribute, Data Type, Collection Method, Benchmark) and the trust-during-onboarding example.
2. `glare:ux-metrics-why` — the AI-acceleration argument for why product and design teams need shared measurement now.
3. `glare:ux-metrics-system` — UX metrics as a connected operational system, plus the three recurring patterns (Confusion Traps, Friction Walls, Trust Gaps).
4. `glare:ux-metrics-attitudinal` — the nine attitudinal metrics with definitions, when to use, common mistakes.
5. `glare:ux-metrics-behavioral` — the eight behavioral metrics with definitions, when to use, common mistakes.
6. `glare:ux-metrics-performance` — the eleven performance metrics with definitions, when to use, common mistakes.
7. `glare:ux-metrics-stack` — Design Stacks vs Research Stacks; combining 3-7 metrics into a stack to evaluate a workflow.
8. `glare:ux-metrics-mapping` — Mapping Design Impact through Situation → Intent → Outcomes → Results, leading vs lagging indicators, design impact creating pull.
9. `glare:ux-metrics-applying` — the eight operational use cases (reviews, prioritization, comparison, launch readiness, AI workflow evaluation, stacks, shared language, decision support).

## How UX metrics fit across Glare

| Glare area | What metrics do here |
|---|---|
| **Define** | Clarify what success should look like. UX metrics name the numbers that prove design worked. |
| **Measure** | Validate concepts, hunches, experiments. Metrics are the falsifiability test. |
| **Focus** | Compare directions and expose tradeoffs. Side-by-side metric reads pick the move. |
| **Lead** | Connect design work to measurable outcomes. Chain UX metric → product KPI → business KPI. |
| **Design Signals** | Metrics are the structural layer under the six-piece signal anatomy. |
| **Design Reviews** | Metrics ground the conversation in evidence (the G in SIGNAL). |
| **Design Assessment** | Metrics underpin Building Proof — does design work connect to measurable outcomes. |
| **AI Workflows** | Intelligence metrics measure whether AI features improve outcomes. |
| **Benchmarking** | Metrics enable comparison across versions, competitors, journeys, segments. |

## Read the reference first

Before answering, read `reference.md` — it carries the full v1.32 Overview content (the four types in detail, the seven scope areas of Intelligence, the chain to Design Signals, the from-metrics-to-decisions framing) plus the version history of the metric-type taxonomy.

## How to apply

1. **Orient on the four types.** Walk through Attitudinal · Behavioral · Performance · Intelligence. If AI is part of the experience, Intelligence is non-optional. If a team has only one type, the picture is distorted.

2. **Diagnose what the user actually wants** and route to the right sub-skill. A user asking "what should I measure for onboarding?" wants Define-stage picking (`glare:define-ux-metrics`). A user asking "what is a UX metric?" wants `glare:ux-metrics-what-is`. A user asking "how do I prove design impact?" wants `glare:ux-metrics-mapping` or `glare:lead-mapping`.

3. **Show metrics as the connector.** UX metrics are not just a Define-stage exercise — they are the connective tissue under Signals, Reviews, AI workflows, and assessments. When a user is confused about whether they need "metrics" or "signals" or "KPIs," the answer is usually all three at different layers, with UX metrics as the bridge.

4. **Bring AI metrics in deliberately.** Intelligence metrics are new. When the user mentions AI features, name the six scope areas (recommendation quality · prompt effectiveness · AI guidance usefulness · adaptation quality · confidence calibration · workflow assistance) and pair them with at least one Behavioral or Attitudinal metric so the team is not only looking at the AI in isolation.

5. **End with a concrete next step.** This is a top-level orientation skill — its job is to put the user on the right path. Always close with the named sub-skill or sibling they should drop into next.

## Critical rules

- **Cover all four types or the picture distorts** — Attitudinal, Behavioral, Performance, Intelligence; if a team has only one type, the experience is being measured through a single lens.
- **Intelligence is non-optional when AI is in the experience** — pair Intelligence metrics with at least one Behavioral or Attitudinal metric so AI isn't evaluated in isolation.
- **Don't let users collapse metrics, signals, and KPIs into one word** — they are different layers; UX metrics are the connective tissue between user behavior and business KPIs, not a substitute for either.
- **The canonical taxonomy is the four-type model** — v1.1's "Perceptual" was removed; comprehension and recognition now live inside Behavioral. Don't reintroduce removed categories.
- **Always close with a named handoff** — this is an orientation skill, not a destination; never end a turn without pointing the user to a specific sub-skill or sibling.

## Handoffs

- For the four parts of a UX metric and the trust-during-onboarding example, route to `glare:ux-metrics-what-is`.
- For the AI-acceleration argument behind why measurement matters now, route to `glare:ux-metrics-why`.
- For UX metrics as a connected operational system and the three patterns, route to `glare:ux-metrics-system`.
- For attitudinal / behavioral / performance metrics as families with per-metric summaries, route to `glare:ux-metrics-attitudinal`, `glare:ux-metrics-behavioral`, `glare:ux-metrics-performance`.
- For combining 3-7 metrics into a Design Stack or Research Stack, route to `glare:ux-metrics-stack`.
- For the Situation → Intent → Outcomes → Results chain and design impact creating pull, route to `glare:ux-metrics-mapping`.
- For the eight operational use cases, route to `glare:ux-metrics-applying`.
- For Define-stage metric picking on a specific decision, route to `glare:define-ux-metrics`.
- For the six-piece anatomy of a signal that uses a metric, route to `glare:signals-components`. For the Need / Use / Prefer / Adopt signal-type taxonomy, route to `glare:signals-types`.
- For mapping a UX metric upward to product KPI to business KPI, route to `glare:lead-mapping`. For the Decision Map as a whole, route to `glare:decision-map`.
- For Design Signals as a top-level concept, route to `glare:design-signals`. For Design Reviews, route to `glare:design-review`. For Design Assessment, route to `glare:design-assessment`.
