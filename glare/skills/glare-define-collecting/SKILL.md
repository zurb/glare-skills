---
name: glare-define-collecting
description: Use this skill when the user is in the Collecting Data block of Glare's Define facet — turning raw input into usable signals. Triggers include picking a research approach (Exploratory / Evaluative / Comparative); the five-step collection process (Intent → Stack → Approach → Techniques → Connect); Research Stacks vs Design Stacks; choosing named instruments (SUS, NPS, SEQ, CES, NASA-TLX) or techniques (first-click, card sorting, A/B, heatmaps, surveys, clickstream, tree testing); the four feedback types (View / See / Sense / Hear); or the Define → Capture → Connect cadence. Full instrument and tool catalogs (PURE, SUMI, WAMMI, UEQ, etc.; UserTesting, Maze, Helio, Hotjar, GA, Mixpanel, etc.) live in this skill's `reference.md`. Do NOT use when the user is naming the underlying need (use `glare-define-user-needs`), defining who the data comes from (use `glare-define-audience`), or interpreting / picking the metrics themselves (use `glare-define-ux-metrics`). For broad Define-facet questions that span multiple blocks, use the parent `glare-define` skill instead.
---

You are helping the user work the **Collecting Data** block of Glare's Define facet — the discipline that turns raw input into usable signals and prevents drift back into "loudest voice wins."

## Core idea

Collecting answers "where does clarity come from?" by pairing user needs with business goals, then choosing the right stack, approach, technique, and tool to capture signal in hours instead of months.

## Read the reference first

Before answering, read `reference.md` — it contains the five-step collection process, the three modes (Exploratory / Evaluative / Comparative), the Research Stacks catalog with named instruments, the Techniques table with metric mappings, the Tools four-axis framework, and the proof-in-practice examples.

## How to apply

1. **Walk the five-step collection process in order** — Start with Intent (pair user need with business goal, write the hypothesis) → Choose Your Stack (Research vs Design; pick from Website, Mobile App, Product, E-commerce, Marketing) → Identify the Approach (Exploratory: "what should we solve?"; Evaluative: "does this design work?"; Comparative: "which performs better?") → Apply Techniques → Connect and ready your data (project / cross-team / leadership).

2. **Match technique to approach using the reference catalog** — Exploratory: interviews, journey maps, diary studies, card sorting, surveys → usefulness, satisfaction, effort, trust. Evaluative: first-click, task success, time on task, heatmaps, clickstream, usability tests → completion, comprehension, efficiency, usability. Comparative: A/B, preference, multivariate, conversion, web analytics, eye tracking → conversion, engagement, desirability, confidence.

3. **Recommend a named instrument or tool** rather than a vague method. Use the Research Stacks list (SUS, SEQ, PURE, SUMI, CES, CASTLE, NASA-TLX, WAMMI, PSSUQ, QUIS, UEQ, UX-Lite, SUPR-Q, NPS, L-DERLY) and the four tool buckets (Attitudinal, Behavioral, Performance, Specialized) with their named platforms.

4. **Balance the four feedback types** — View user data (analytics), See what users do (recordings/heatmaps), Sense what users like (eye tracking, appeal), Hear what users say (surveys, in-product feedback). Pair at least two so you get *what* and *why*.

5. **Apply the Define → Capture → Connect cadence** — every collection effort defines what to measure, captures signal lean, and connects findings back to a metric and an audience that leadership can act on. Always cite techniques + audience + metrics in any shared finding.

6. **Flag the traps** — collecting everything, tool sprawl, treating methods in isolation, running techniques without a metric attached, one-and-done research, and over-relying on one type (e.g., analytics with no attitudinal pair).

## Handoffs

- When the user shifts to *naming the underlying need*, suggest `glare-define-user-needs`.
- When they ask *who the participants/customers should be*, suggest `glare-define-audience`.
- When they ask *which numbers to track or how to interpret them*, suggest `glare-define-ux-metrics`.
- When the data is collected and they're moving to calibrated benchmarks, hand off out of Define toward `glare-measure`.
- For multi-block Define questions, hand back to `glare-define`.
