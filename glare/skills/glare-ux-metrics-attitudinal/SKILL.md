---
name: glare-ux-metrics-attitudinal
description: Use this skill when the user is working with Attitudinal metrics — how users feel about an experience. Triggers — phrases like "attitudinal metrics," "how users feel," "trust," "satisfaction," "confidence," "desirability," "loyalty," "sentiment," "appeal," "feeling," "expectations," "usefulness," "brand score," "NPS," "CSAT," "users finished but felt confused," "attitudinal vs behavioral," "users may complete but not trust," or asks how to capture emotional response and perceived value. Also use when the user is picking among the nine attitudinal metrics, debugging which emotional signal to measure, or pairing emotional signals with behavioral and performance metrics inside a stack. Do NOT use for the broader UX Metrics framework (use `glare-ux-metrics`), Behavioral or Performance metrics specifically (use `glare-ux-metrics-behavioral` / `glare-ux-metrics-performance`), or Define-stage picking on a specific decision (use `glare-define-ux-metrics`).
version: 2.2.0
source_doc_version: v1.32
last_rebuilt: 2026-05-10
---

You are helping the user select, structure, and apply **Attitudinal metrics** — the family that measures how users *feel* about the experience.

## Core idea

Attitudinal metrics measure how users feel about an experience — trust, confidence, satisfaction, frustration, desirability, emotional response. Product teams often focus on clicks, completion, engagement, and conversion, but users can technically complete a workflow while still feeling confused, frustrated, unsure, or disconnected. Attitudinal metrics catch what is happening emotionally underneath the workflow. They are usually **leading indicators** — they reveal smaller emotional problems before larger business problems appear later. Trust may weaken before retention drops; confidence may fall before abandonment rises; frustration may grow before support tickets increase.

## When attitudinal metrics matter most

Especially during onboarding, fintech workflows, healthcare experiences, AI-assisted systems, automation workflows, and enterprise software — environments where emotional confidence often matters as much as usability. A workflow may technically function correctly while users still hesitate to rely on it fully.

## The nine attitudinal metrics (v1.32)

`reference.md` carries the per-metric summary table — one row per metric with definition, when to use, common mistakes. The nine metrics:

Appeal · Brand Score · Desirability · Expectations · Feeling · Loyalty · Satisfaction · Sentiment · Usefulness

## Read the reference first

Before answering, read `reference.md` — it carries the per-metric summary table for all nine attitudinal metrics, why attitudinal signals are leading indicators, the four sub-attributes (Trust, Confidence, Satisfaction, Desirability) with what each reveals, and the patterns that emerge when attitudinal metrics combine with behavioral and performance metrics.

## How to apply

1. **Pick the metric that matches the question.** Trust is not the same as Satisfaction. Confidence is not the same as Loyalty. Use the per-metric table in `reference.md` to match the user's question to the right attribute.

2. **Recognize attitudinal as leading indicators.** When the user is in pre-launch or early-launch territory, attitudinal metrics surface emotional friction before behavioral and performance numbers move. Helio is the canonical Glare path for capturing these as leading indicators before product ships.

3. **Pair attitudinal with behavioral and performance.** A single emotional score rarely explains the full experience. Combine: high completion + low confidence = trust gap; strong engagement + rising frustration = hidden friction; low error rates + weak satisfaction = workflow fatigue. Hand off to `glare-ux-metrics-stack` once two or more metrics are in play.

4. **Watch for AI-specific attitudinal failures.** AI recommendations can increase activity while trust drops; AI guidance can speed up workflows while confidence weakens. When AI is in the experience, an attitudinal metric is non-optional and should pair with at least one Intelligence-type signal once that sub-skill exists.

5. **Use the four sub-attributes diagnostically.** Trust (safe to rely on?), Confidence (sure about what I'm doing?), Satisfaction (how do I feel after?), Desirability (am I drawn to it?). When the user is debugging a soft "users seem unhappy," walk these four to find the actual signal.

## Handoffs

- For the broader UX Metrics framework and the four metric TYPES, route to `glare-ux-metrics`.
- For the four parts of any UX metric (Attribute, Data Type, Collection, Benchmark), route to `glare-ux-metrics-what-is`.
- For Behavioral metrics (what users do), route to `glare-ux-metrics-behavioral`.
- For Performance metrics (efficiency and reliability), route to `glare-ux-metrics-performance`.
- For combining attitudinal + behavioral + performance into a Design Stack, route to `glare-ux-metrics-stack`.
- For Define-stage metric picking on a specific decision, route to `glare-define-ux-metrics`.
- For mapping a UX metric upward to product KPI to business KPI, route to `glare-lead-mapping`.
- For Design Signals as the layer that turns metrics into decisions, route to `glare-design-signals`.
