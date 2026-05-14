---
name: glare-ux-metrics-system
description: Use this skill when the user is treating UX metrics as a connected system rather than isolated scores — phrases like "measurement system," "UX metrics as a system," "metrics work together," "metrics form patterns," "operational measurement," "shared visibility across teams," "different dashboards different conclusions," "we have lots of dashboards but no clarity," "measurement breaks down across the org," "Confusion Trap," "Friction Wall," "Trust Gap," "high completion long time on task," "strong engagement weak trust," or asks how to evolve from isolated dashboards to a shared measurement system. Also use when wrestling with org-wide measurement fragmentation or wanting to understand the four measurement areas as one connected system. Do NOT use for the four metric TYPES at the framework level (use `glare-ux-metrics`), per-metric definitions (use the type sub-skills), or stacking specific metrics (use `glare-ux-metrics-stack`).
version: 3.1.0
source_doc_version: v1.32
last_rebuilt: 2026-05-13
---

You are helping the user run UX Metrics as a **connected operational system** — not as a scoreboard, and not as isolated dashboards.

## Core idea

UX Metrics work best when they operate as a connected system. A single metric shows one small part of the experience. When metrics work together, teams begin to see patterns — where users get confused, where trust breaks down, where workflows create friction, where ideas gain momentum, where experiences improve over time. The challenge is that organizations measure differently across teams (product on speed, leadership on revenue, design on usability, research on behavior, engineering on quality). Each group has useful information, but the signals stay disconnected. The measurement system rebuilds that shared visibility so the org argues from the same evidence.

## The chain that turns isolated numbers into operating memory

> metrics → form patterns → create signals → help teams interpret what is happening → guide stronger decisions

Examples of metrics explaining each other (the v1.32 canonical pairs):

- **High completion + long time on task** → friction
- **Strong engagement + weak trust** → hesitation
- **Low errors + low confidence** → hidden confusion

The metrics begin explaining each other. Instead of looking at isolated scores, teams begin seeing the *shape* of the experience.

## The three recurring patterns (v1.32)

When teams compare metrics together, three patterns repeat across products and systems:

- **Confusion Traps** — users complete a task while still feeling lost. Completion stays high; comprehension, clarity, and confidence weaken underneath. Common in onboarding, navigation changes, dashboard redesigns, AI-assisted workflows.
- **Friction Walls** — users understand what they are trying to do, but the workflow slows them down. Time on task increases, effort rises, frustration builds. Common when workflows become too complex, navigation harder to scan, onboarding asks too much, or AI recommendations create extra steps.
- **Trust Gaps** — the workflow technically functions, but users stop feeling safe or confident. Especially important in fintech, AI systems, healthcare, onboarding, and automation workflows. Users continue using the product while trust slowly weakens underneath.

## The four measurement areas (the system itself)

UX Metrics inside Glare are organized into four connected measurement areas:

- **Attitudinal** — how users feel (trust, satisfaction, desirability, sentiment, expectations)
- **Behavioral** — what users do (completion, engagement, effort, comprehension, usability)
- **Performance** — outcomes and efficiency (completion rate, error rate, drop-off rate, click-through rate, time on task)
- **Intelligence** — whether AI helps users move forward (recommendation quality, prompt effectiveness, AI guidance usefulness, workflow assistance, confidence calibration)

Each area is useful alone. The system value comes from running all four together so patterns surface that no single area would expose.

## Read the reference first

Before answering, read `reference.md` — it carries the full v1.32 Measurement System content, including all three patterns in detail, the org-fragmentation diagnosis ("different dashboards, different conclusions"), the four measurement areas, and the operating-memory framing.

## How to apply

1. **Diagnose whether the team has a system or a scoreboard.** Ask whether metrics are reviewed in isolation (one number per dashboard, one team per dashboard) or whether they are looked at together with explicit connections drawn between Attitudinal, Behavioral, Performance, and Intelligence. A scoreboard creates reactivity. A system creates patterns.

2. **Use the three patterns as a diagnostic checklist.** When the user describes confusion, walk through Confusion Trap → Friction Wall → Trust Gap. Match the symptoms — completion-high-but-confidence-low (Confusion Trap), time-on-task-rising-with-effort (Friction Wall), continued-use-but-weakening-trust (Trust Gap).

3. **Surface the org-fragmentation cost.** Without shared measurement, teams argue over different versions of the same experience. One team thinks the release went well because engagement increased. Another team sees lower confidence, rising support requests, slower task completion, and more onboarding hesitation. Naming the fragmentation is the first step to fixing it.

4. **Push for AI-workflow visibility.** AI-assisted workflows are where measurement systems matter most — recommendations change dynamically, experiences adapt constantly, output scales quickly, and teams test more ideas than they can evaluate. Without a system, teams cannot tell whether AI is improving the experience or simply increasing activity.

5. **Frame the system as operational memory.** Strong measurement systems are not one-time reports. They become how teams repeatedly evaluate product direction together. Over time the system recognizes recurring friction, repeated hesitation, weak onboarding patterns, trust breakdowns, and workflows that consistently perform better. That memory is the point.

## Handoffs

- For the broader UX Metrics framework, route to `glare-ux-metrics`.
- For combining specific 3-7 metrics into Design Stacks or Research Stacks, route to `glare-ux-metrics-stack`.
- For mapping design impact across Situation → Intent → Outcomes → Results, route to `glare-ux-metrics-mapping`.
- For the eight operational use cases inside reviews, prioritization, comparison, etc., route to `glare-ux-metrics-applying`.
- For each metric type's per-metric definitions, route to `glare-ux-metrics-attitudinal`, `glare-ux-metrics-behavioral`, `glare-ux-metrics-performance`.
- For the AI-acceleration argument behind why measurement matters now, route to `glare-ux-metrics-why`.
- For the four parts of any UX metric, route to `glare-ux-metrics-what-is`.
- For Building Proof as an organizational maturity dimension, route to `glare-assessment-building-proof`. For the broader assessment, route to `glare-design-assessment`.
- For Design Signals as the layer that turns this measurement system into decisions, route to `glare-design-signals`.
