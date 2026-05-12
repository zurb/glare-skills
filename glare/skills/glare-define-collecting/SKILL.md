---
name: glare-define-collecting
description: Use this skill when the user is in the Collecting Data block of the Define area — turning raw input into usable signals. Triggers — picking a research approach (Exploratory / Evaluative / Comparative); the five-step process (Intent → Stack → Approach → Techniques → Connect); Research Stacks vs Design Stacks; named instruments (SUS, NPS, SEQ, CES, NASA-TLX) or the 12 techniques (First Click, Task Success, Time on Task, A/B, Multivariate, Heatmaps, Clickstream, Web Analytics, Conversion Rate, Eye Tracking, Card Sorting, Surveys); the four feedback types (View / See / Sense / Hear); the Define → Capture → Connect cadence. Tool catalogs (PURE, SUMI, WAMMI, UEQ; UserTesting, Maze, Helio, Hotjar, GA, Mixpanel) live in `reference.md`. Do NOT use when naming the need (use `glare-define-user-needs`), defining who data comes from (use `glare-define-audience`), or picking metrics (use `glare-define-ux-metrics`). For broad Define, use `glare-define`; for the Decision Map, `glare-decision-map`.
version: 3.0.0
source_doc_version: v1.1 + canonical-28 constraint
last_rebuilt: 2026-05-11
---

You are helping the user work the **Collecting Data** block of the Decision Map's **Define** area — the discipline that turns raw input into usable signals and prevents drift back into "loudest voice wins."

## Core idea

Collecting Data sits inside the Define area of the Decision Map. It answers "where does clarity come from?" by pairing user needs with business goals, then choosing the right stack, approach, technique, and tool to capture signal in hours instead of months.

## Read the reference first

Before answering, read `reference.md` — it contains the five-step collection process, the three modes (Exploratory / Evaluative / Comparative), the **12 techniques** with usage guidance, the Research Stacks catalog, the Tools four-axis framework, the three-tier sharing model, and the proof-in-practice examples.

## Critical rules

**Canonical metric constraint.** When recommending or naming UX metrics — including the metric a technique or instrument should target — use only the 28 canonical metrics listed in `glare-ux-metrics-attitudinal`, `glare-ux-metrics-behavioral`, and `glare-ux-metrics-performance`. Do not invent metric names or use legacy names not in this list. If the situation needs a metric that's not in the canonical list, flag it explicitly as "outside the canonical 28" and explain why.

Canonical 28:

- Attitudinal (9) — Appeal, Brand Score, Desirability, Expectations, Feeling, Loyalty, Satisfaction, Sentiment, Usefulness.
- Behavioral (8) — Completion, Comprehension, Effort, Engagement, Frequency, Intent, Success, Usability.
- Performance (11) — Abandonment Rate, Bounce Rate, Click-Through Rate, Completion Rate, Drop-off Rate, Error Frequency, Error Rate, Recency, Session Duration, Time on Task, Visit Frequency.
- Intelligence — in development; the v1.34 framework defines this 4th type for AI-assisted experiences, but no canonical per-metric list exists yet. Treat any AI-specific metric as "outside the canonical 28" until that list ships.

Some technique tables in `reference.md` use legacy or shorthand terms (Efficiency, Trust, Conversion, Visual Attention, Conversion Rate, Confidence, Drop-Off). When you recommend a metric, translate to a canonical name (e.g., Drop-Off → Drop-off Rate; Efficiency → Time on Task or Completion Rate, depending on intent; Trust → Loyalty or Sentiment) or flag the term as outside the canonical 28.

## How to apply

1. **Walk the five-step collection process in order** — Start with Intent (pair user need with business goal, write the hypothesis) → Choose Your Stack (Research vs Design; pick from Website, Mobile App, Product, E-commerce, Marketing) → Identify the Approach (Exploratory: "what should we solve?"; Evaluative: "does this design work?"; Comparative: "which performs better?") → Apply Techniques → Connect and ready your data (project / cross-team / leadership).

2. **Match technique to approach using the 12-technique catalog** — Exploratory: Card Sorting, Surveys & Questionnaires, interviews, journey maps. Evaluative: First Click, Task Success Rate, Time on Task, Heatmaps, Clickstream, usability tests. Comparative: A/B, Multivariate, Conversion Rate Analysis, Eye Tracking, Web Analytics.

3. **Recommend a named instrument or tool** rather than a vague method. Use the Research Stacks list (SUS, SEQ, PURE, SUMI, CES, CASTLE, NASA-TLX, WAMMI, PSSUQ, QUIS, UEQ, UX-Lite, SUPR-Q, NPS, L-DERLY) and the four tool buckets (Attitudinal, Behavioral, Performance, Specialized) with their named platforms.

4. **Balance the four feedback types** — View user data (analytics), See what users do (recordings/heatmaps), Sense what users like (eye tracking, appeal), Hear what users say (surveys, in-product feedback). Pair at least two so you get *what* and *why*.

5. **Apply the Define → Capture → Connect cadence** — every collection effort defines what to measure, captures signal lean, and connects findings back to a metric and an audience that leadership can act on. Always cite techniques + audience + metrics in any shared finding.

6. **Use the three-tier sharing model** — Project-Level Feedback (within team, in collection tools), Cross-Team Insights (Findings or Glare workspace by concept/metric), Leadership Rollups (key signals + sources in roadmap reviews).

7. **Flag the traps** — collecting everything, tool sprawl, treating methods in isolation, running techniques without a metric attached, one-and-done research, and over-relying on one type (e.g., analytics with no attitudinal pair).

## Handoffs

- When the user shifts to *naming the underlying need*, suggest `glare-define-user-needs`.
- When they ask *who the participants/customers should be*, suggest `glare-define-audience`.
- When they ask *which numbers to track or how to interpret them*, suggest `glare-define-ux-metrics`.
- When the data is collected and they're moving to calibrated benchmarks, hand off out of Define toward `glare-measure`.
- For multi-block Define questions, hand back to `glare-define`. For the Decision Map as a whole, `glare-decision-map`.
- When the user is asking what *signals* to capture (not just which instruments) and how to structure them, route to `glare-design-signals` and the bucket skills `glare-signals-components`, `glare-signals-types`, `glare-signals-quality`, `glare-signals-capturing`.
- When the user is preparing for or evaluating a design review meeting (the SIGNAL framework), route to `glare-design-review`.
- When the user wants to assess team maturity (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence), route to `glare-design-assessment`.
