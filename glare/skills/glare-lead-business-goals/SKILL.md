---
name: glare-lead-business-goals
description: Use this skill when the user is anchoring design work to the pressures executives already track — the Business Goals bucket of the Glare Lead facet, part of the Decision Map's Lead area. Triggers include picking which business pressure a project serves (Growth, Retention, User Experience, Efficiency, Operations), choosing among the 20 measurable goals (e.g., "Reduce churn → Achieve product–market fit", "Lower support costs → Reduce support costs", "Prove launch success → Support strategic product launches"), distinguishing the three layers of KPIs (Design KPIs like task completion / error rate / time on task; Product KPIs like adoption / retention / engagement; Business KPIs like revenue growth / churn / LTV), running the three-question Quick Test to decide whether a metric is a true signal vs. a vanity number, or calling out anti-patterns (vanity metrics, correlation-as-causation, reporting without connecting). Do NOT use for cross-functional translation of those goals into Sales / Marketing / Product / Eng / Strategy / Ops / Finance / Legal language — invoke `glare-lead-workflows`. Do NOT use for drawing the full User Need → Design KPI → Product KPI → Business KPI → Business Goal ladder — invoke `glare-lead-mapping`. Do NOT use for the Initiatives → Findings → Decisions → Outcomes loop or the maturity diagnostic — invoke `glare-lead-results`. For the broader Lead facet overview, invoke parent `glare-lead`.
version: 1.3.0
source_doc_version: v1.0
last_rebuilt: 2026-05-04
---

You are helping the user work through the **Business Goals** bucket of the Glare Lead facet — the upward-facing area of the **Decision Map** that anchors design to the pressures leadership already tracks so design becomes a lever, not decoration.

## Core idea

Business Goals is part of the upward-facing area of the Decision Map (Lead). A metric only matters when it's tied to intent. Business Goals stacks three layers of KPIs (Design → Product → Business) and routes them to one of nine business pressures via 20 named goals, so every signal can be defended as proof of impact rather than a number on a dashboard.

## Read the reference first

Before answering substantive questions, read `reference.md` — it contains the verbatim Three Layers of Goals, the full 20 goals × 9 pressures map, the Quick Test, and the explicit pitfalls to avoid.

## How to apply

1. **Name the layer first.** Ask which of the three layers the user's metric lives in: Design KPI (task completion, error rate, time on task), Product KPI (feature usage, retention, engagement), or Business KPI (revenue growth, churn reduction, LTV). If the user can't classify it, that's the first thing to fix.

2. **Route to one of the 9 business pressures.** The pressures are Growth, Retention, User Experience, Efficiency, Operations (with Strategy / Finance / Risk implied through the workflow lens). Force a single primary pressure — work that "serves all of them" usually serves none.

3. **Pick a measurable goal from the 20.** Each pressure has four named goals tied to a strategic outcome (e.g., Growth: "Attract new customers → Drive revenue growth"; Efficiency: "Lower support costs → Reduce support costs"; Operations: "Lead with evidence → Make informed design decisions"). Use the verbatim pairing in `reference.md` so the user inherits the leadership-facing phrasing.

4. **Run the Quick Test on every candidate metric.** A metric is a true *signal* only if all three are yes: (a) Does it prove the design works for users? (b) Does it show adoption or retention at the product level? (c) Does it connect to growth, churn, or revenue at the business level? If any answer is no, it's a vanity metric or a partial signal — name the missing rung.

5. **Flag the three pitfalls explicitly.** Watch for: chasing vanity metrics (clicks/pageviews not tied to adoption or retention), mistaking correlation for causation, and reporting numbers without connecting them to outcomes. If you see one, call it out by name.

6. **Stop at the goal — don't draw the full ladder here.** Once the pressure and goal are named and the metric passes the Quick Test, hand off. Drawing the explicit User Need → Design KPI → Product KPI → Business KPI → Business Goal chain belongs in `glare-lead-mapping`. Translating the goal into a specific function's language belongs in `glare-lead-workflows`.

## Handoffs

- Cross-functional translation of the goal → `glare-lead-workflows`.
- Building the five-rung Chain of Proof → `glare-lead-mapping`.
- Initiatives → Findings → Decisions → Outcomes loop, maturity diagnostic → `glare-lead-results`.
- Broader Lead facet framing → parent `glare-lead`.
- Decision Map area above Lead → `glare-decision-map`.
- Upstream signal collection (Decision Map siblings) → `glare-define`, `glare-measure`, `glare-focus`.
- Signal anatomy and quality (the building blocks anchored here) → `glare-design-signals`, `glare-signals-components`, `glare-signals-types`, `glare-signals-quality`, `glare-signals-capturing`.
- Preparing for or evaluating a leadership review (SIGNAL framework — Surface / Identify / Ground / Navigate / Align / Lock) → `glare-design-review`.
- Assessing team / org design maturity → `glare-design-assessment`.
