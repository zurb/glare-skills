---
name: glare-lead-mapping
description: Use this skill when the user is drawing the ladder from user need to business goal — the Mapping bucket of the Lead facet. Triggers: building or auditing a Chain of Proof (User Need → Design KPI → Product KPI → Business KPI → Goal); naming UX metrics as "connective tissue" between product and business metrics; working upward from a Design KPI or downward from a goal; the Five Steps to Map (Align on Goals → Understand Workflows → Map the Chain → Share → Keep Visible) or the Make-It-Practical routine (Define Goal → Connect Workflow → Build Chain → Share Story → Refresh Data); the Quick Checklist; the onboarding-to-revenue example (55%→85% completion → trial-to-paid doubled → pipeline +25%). Do NOT use for picking the pressure/goal — use `glare-lead-business-goals`. Do NOT use for cross-functional language — use `glare-lead-workflows`. Do NOT use for the Initiatives → Findings → Decisions → Outcomes loop — use `glare-lead-results`. For broader Lead, use `glare-lead`.
version: 1.3.0
source_doc_version: v1.1
last_rebuilt: 2026-05-04
---

You are helping the user work through the **Mapping** bucket of the Glare Lead facet — the upward-facing area of the **Decision Map** — which turns outputs into outcomes by connecting user needs at the bottom to business goals at the top.

## Core idea

Mapping is part of the upward-facing area of the Decision Map (Lead). It draws a single visible line — the five-rung **Chain of Proof** — from what people are trying to get done up to the pressure leadership already tracks, with UX metrics serving as the connective tissue that keeps the chain credible and explainable.

## Read the reference first

Before answering substantive questions, read `reference.md` — it contains the verbatim five rungs, the v1.1 Five Steps to Map, the Make-It-Practical routine, the Quick Checklist, the reflection questions, and the onboarding-to-revenue worked example.

## How to apply

1. **Anchor the rungs explicitly.** The chain is fixed: (1) User Need → (2) User Outcome / Design KPI → (3) Product Outcome / Product KPI → (4) Business Outcome / Business KPI → (5) Business Goal. Make the user fill in each rung by name; an unnamed rung is the failure point.

2. **Decide which direction to work.** Upward from a user need: talk to UX research, customer success, support. Downward from a goal: talk to PMs, analytics, finance. The reference's "How to Use This Map" guidance dictates the right collaborators for each direction.

3. **Use UX metrics as connective tissue.** When a Product KPI moves, the Design KPI explains *why* ("retention dropped because comprehension fell"). When a Business KPI moves, the Design + Product KPIs make it *credible* ("revenue grew because adoption increased, fueled by higher task success"). Without the UX rung, leaders only see lagging indicators.

4. **Run the v1.1 Five Steps when building a new map.** Align on Business Goals → Understand the Workflows → Map the Chain of Proof → Share Across Teams → Keep It Visible. Treat Mapping as a living process, not a one-time deck — embed it in dashboards, OKR reviews, roadmap decks.

5. **Use the Make-It-Practical routine for an in-flight project.** Define the Goal → Connect the Workflow → Build the Chain → Share the Story → Refresh the Data (quarterly or after each launch). Pair with the Quick Checklist (defined business goal? UX metrics connected to product/business KPIs? chain visible to every function? story refreshed?).

6. **Check alignment before you ship the map.** If you can't connect the Design KPI to a business outcome, the signal won't resonate — go back and find the missing rung instead of defending the chain in front of leadership. Use the canonical onboarding-to-revenue example as a template for what a complete chain looks like.

## Handoffs

- Picking the underlying business pressure or measurable goal that anchors rung 5 → `glare-lead-business-goals`.
- Translating a single rung into a specific function's vocabulary → `glare-lead-workflows`.
- Initiatives → Findings → Decisions → Outcomes loop, maturity diagnostic → `glare-lead-results`.
- Broader Lead facet framing → parent `glare-lead`.
- Decision Map area above Lead → `glare-decision-map`.
- Upstream signal collection (Decision Map siblings) → `glare-define`, `glare-measure`, `glare-focus`.
- Signal anatomy and quality (the units the chain links) → `glare-design-signals`, `glare-signals-components`, `glare-signals-types`, `glare-signals-quality`, `glare-signals-capturing`.
- Preparing for or evaluating a leadership review (SIGNAL framework — Surface / Identify / Ground / Navigate / Align / Lock) → `glare-design-review`.
- Assessing team / org design maturity → `glare-design-assessment`.
