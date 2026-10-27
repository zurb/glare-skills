---
name: ux-metrics-performance
description: Use this skill when the user is working with Performance metrics — efficiency, reliability, and operational friction. Triggers include "performance metrics," "efficiency metrics," "reliability," "operational friction," "how long tasks take," "where users drop off," "abandonment rate," "bounce rate," "click-through rate," "completion rate," "drop-off rate," "error frequency," "error rate," "recency," "session duration," "time on task," "visit frequency," "the workflow works but takes forever," "users finish but slowly," or asks how to capture the operational health of the experience underneath the workflow. Also use when picking among the eleven performance metrics or pairing performance signals with attitudinal and behavioral metrics. Do NOT use for the broader UX Metrics framework (use `glare:ux-metrics`), Attitudinal or Behavioral metrics (use `glare:ux-metrics-attitudinal` / `glare:ux-metrics-behavioral`), or Define-stage picking (use `glare:define-ux-metrics`).
version: 3.1.0
source_doc_version: v1.32 (per-metric pages added)
last_rebuilt: 2026-05-13
---

You are helping the user select, structure, and apply **Performance metrics** — the family that measures *how efficiently* a workflow actually functions during real usage.

> **Canonical metric list (recommend ONLY from these eleven).** Abandonment Rate · Bounce Rate · Click-Through Rate · Completion Rate · Drop-off Rate · Error Frequency · Error Rate · Recency · Session Duration · Time on Task · Visit Frequency. Do not invent or borrow performance metric names from other frameworks — if the user's question doesn't match one of these eleven, route to `glare:ux-metrics` or another type-level skill instead.

## Core idea

Performance metrics measure how efficiently a workflow, system, or experience actually functions — how long tasks take, where users drop off, where errors increase, how much effort workflows require, whether systems perform reliably under real usage. Product teams often focus heavily on whether users completed a task, but completion alone rarely explains how difficult the experience actually was. Users may finish onboarding while struggling the entire time, complete checkout after repeated errors, use AI recommendations while constantly double-checking results, or finish tasks successfully while moving much slower than expected. Performance metrics measure the *cost* of friction.

## What performance metrics catch that other types miss

Behavioral metrics explain what users do; attitudinal metrics explain how users feel; performance metrics explain how efficiently the system actually functions underneath the experience — time, effort, errors, reliability, workflow efficiency, operational breakdowns. A workflow may technically perform well while users feel frustrated, hesitate repeatedly, lose confidence, or struggle to understand what to do next.

## The eleven performance metrics (v1.32)

`reference.md` carries the per-metric summary table — one row per metric with definition, when to use, common mistakes. The eleven metrics:

Abandonment Rate · Bounce Rate · Click-Through Rate · Completion Rate · Drop-off Rate · Error Frequency · Error Rate · Recency · Session Duration · Time on Task · Visit Frequency

## Read the reference first

Before answering, read `reference.md` — it carries the per-metric summary table for all eleven performance metrics, why performance signals reveal hidden problems, the cost-of-friction framing, and how performance signals combine with attitudinal and behavioral metrics.

## How to apply

1. **Pick the metric that matches the operational question.** Drop-off Rate is for multi-step flows; Bounce Rate is for landing pages; Time on Task is for individual tasks; Error Rate and Error Frequency are for reliability. Use the per-metric table in `reference.md`.

2. **Distinguish similar-sounding metrics.** Abandonment Rate (started but didn't finish a task) is not Drop-off Rate (exited at a specific step). Error Rate (percentage of users who hit an error) is not Error Frequency (errors per session). Completion Rate (analytics-funnel percentage) is not Behavioral Completion (whether the user reached the end via direct or indirect path). Visit Frequency (observed) is not Behavioral Frequency (self-reported).

3. **Pair performance with attitudinal and behavioral.** Strong completion rate + low trust = a fragile workflow. Low errors + rising frustration = exhausting interactions. Fast onboarding + weak comprehension = shallow understanding. Performance numbers alone don't tell the experience story.

4. **Treat performance as the late signal.** Performance metrics often surface in live analytics, after launch. Pair with predictive attitudinal/behavioral metrics from Helio so the team is not learning about workflow inefficiency only after retention drops.

5. **Run performance through the cost-of-friction lens.** A 30% drop-off at step 2 of checkout is not just a number — it is users abandoning purchase intent. Convert performance scores into business-impact framing when handing off to leadership (`glare:lead-mapping` for the chain).

## Handoffs

- For the broader UX Metrics framework and the four metric TYPES, route to `glare:ux-metrics`.
- For the four parts of any UX metric (Attribute, Data Type, Collection, Benchmark), route to `glare:ux-metrics-what-is`.
- For Attitudinal metrics (how users feel), route to `glare:ux-metrics-attitudinal`.
- For Behavioral metrics (what users do), route to `glare:ux-metrics-behavioral`.
- For combining attitudinal + behavioral + performance into a Design Stack, route to `glare:ux-metrics-stack`.
- For Define-stage metric picking on a specific decision, route to `glare:define-ux-metrics`.
- For mapping a UX metric upward to product KPI to business KPI, route to `glare:lead-mapping`.
- For Design Signals as the layer that turns metrics into decisions, route to `glare:design-signals`.
- For Building Proof as an organizational maturity dimension, route to `glare:assessment-building-proof`.
