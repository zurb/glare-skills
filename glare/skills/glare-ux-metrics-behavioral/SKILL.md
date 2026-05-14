---
name: glare-ux-metrics-behavioral
description: Use this skill when the user is working with Behavioral metrics — what users actually do inside the workflow. Triggers — phrases like "behavioral metrics," "what users do," "users hesitate," "users abandon," "navigation breakdowns," "how do users actually move through this," "users repeatedly scan," "click patterns," "completion," "comprehension," "effort," "engagement," "frequency," "intent," "success," "usability," "users finished but it took forever," or asks how to capture interaction behavior across a workflow. Also use when the user is picking among the eight behavioral metrics, debugging where a workflow breaks down at the click level, or pairing behavioral signals with attitudinal and performance metrics. Do NOT use for the broader UX Metrics framework (use `glare-ux-metrics`), Attitudinal or Performance metrics specifically (use `glare-ux-metrics-attitudinal` / `glare-ux-metrics-performance`), or Define-stage picking on a specific decision (use `glare-define-ux-metrics`).
version: 3.1.0
source_doc_version: v1.32 (per-metric pages added)
last_rebuilt: 2026-05-13
---

You are helping the user select, structure, and apply **Behavioral metrics** — the family that measures what users *do* while interacting with a product.

> **Canonical metric list (recommend ONLY from these eight).** Completion · Comprehension · Effort · Engagement · Frequency · Intent · Success · Usability. Do not invent or borrow behavioral metric names from other frameworks — if the user's question doesn't match one of these eight, route to `glare-ux-metrics` or another type-level skill instead.

## Core idea

Behavioral metrics measure what users actually do — where they hesitate, how they move through workflows, where navigation breaks down, where they abandon tasks, what actions create momentum. Product teams often assume users will follow the path that was designed for them. Real behavior often looks very different — users repeatedly scan navigation, hesitate before clicking, skip important content, abandon onboarding halfway through, loop through the same screens, complete tasks slowly while feeling unsure. Behavioral metrics catch what users are *actually* doing inside the workflow, not what teams hoped they would do. They reveal friction, hesitation, and confusion that users may never directly describe themselves.

## When behavioral metrics matter most

Behavioral metrics help teams move beyond simple scoreboards toward what is actually changing user behavior — stronger clarity may improve onboarding completion, reduced effort may improve engagement, clearer navigation may improve discoverability, fewer workflow steps may reduce abandonment. Use them across onboarding, navigation, AI-assisted workflows, search systems, dashboards, and enterprise experiences.

## The eight behavioral metrics (v1.32)

`reference.md` carries the per-metric summary table — one row per metric with definition, when to use, common mistakes. The eight metrics:

Completion · Comprehension · Effort · Engagement · Frequency · Intent · Success · Usability

## Read the reference first

Before answering, read `reference.md` — it carries the per-metric summary table for all eight behavioral metrics, why behavioral signals reveal real growth levers, the workflow-pattern diagnostics, and how behavioral signals combine with attitudinal and performance signals to reveal larger patterns.

## How to apply

1. **Pick the metric that matches the workflow stage.** Comprehension and Intent fit early concept testing. Success and Completion fit usability tests on prototypes. Usability fits multi-step flows. Engagement and Frequency fit longer-term retention questions. Use the per-metric table in `reference.md`.

2. **Distinguish Success from Completion.** Success measures whether users can do *one specific interaction* (find a button, use a filter). Completion measures whether they reach the *end of a flow*. Usability averages multiple Success scores together. The three are not interchangeable.

3. **Use behavioral signals to expose hidden problems.** A workflow may complete at 87% but with repeated hesitation — a Success-test heatmap will surface where the hesitation is. A high engagement score may mask low Comprehension. The per-metric mistakes column in `reference.md` flags these traps.

4. **Pair behavioral with attitudinal.** High engagement + low trust = hesitation. Strong completion + rising frustration = workflow fatigue. Repeated navigation loops + weak confidence = confusion. The combined view is the point — see `glare-ux-metrics-stack`.

5. **Use Helio for behavioral leading indicators.** Helio captures behavioral metrics as leading indicators in prototype and concept tests before analyzing post-launch performance. This is the canonical Glare path for catching behavioral problems while they are still cheap to fix.

## Handoffs

- For the broader UX Metrics framework and the four metric TYPES, route to `glare-ux-metrics`.
- For the four parts of any UX metric (Attribute, Data Type, Collection, Benchmark), route to `glare-ux-metrics-what-is`.
- For Attitudinal metrics (how users feel), route to `glare-ux-metrics-attitudinal`.
- For Performance metrics (efficiency and reliability), route to `glare-ux-metrics-performance`.
- For combining attitudinal + behavioral + performance into a Design Stack, route to `glare-ux-metrics-stack`.
- For Define-stage metric picking on a specific decision, route to `glare-define-ux-metrics`.
- For mapping a UX metric upward to product KPI to business KPI, route to `glare-lead-mapping`.
- For Design Signals as the layer that turns metrics into decisions, route to `glare-design-signals`.
- For research questioning that produces these signals, route to `glare-measure-questioning`.
