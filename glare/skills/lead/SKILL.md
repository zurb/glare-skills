---
name: lead
description: Use this skill when the user is connecting design work to business impact — the Lead facet of Glare's Decision Map (formerly "Show" in v1.0). Triggers include proving ROI on design, building executive narratives, mapping Design KPIs to Product KPIs to Business KPIs, anchoring work to business pressures (Growth, Retention, UX, Efficiency, Operations), translating signals into the language of Sales / Marketing / Product / Engineering / Strategy / Ops / Finance / Legal, or running an Initiatives → Findings → Decisions → Outcomes loop. Also use when the user mentions the Chain of Proof (User Need → Design KPI → Product KPI → Business KPI → Business Goal), the five Lead Dimensions (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence), the 9 business pressures + 20 measurable goals, or the 15-symptom diagnostic. Do NOT use for early signal collection — invoke `glare:define`, `glare:measure`, or `glare:focus` instead.
version: 3.1.0
source_doc_version: v1.0
last_rebuilt: 2026-05-13
---

You are helping the user work through the **Lead** facet of Glare — the upward-facing area of the **Decision Map** that turns design work into evidence leadership trusts. (Define, Measure, Focus, and Lead are the four facets of the Decision Map; Lead is the one that points upward toward the business.)

## Core idea

Lead is the upward-facing area of the Decision Map. It translates user signals into the language executives use: revenue, retention, churn, efficiency, market share. It does this through a five-rung **Chain of Proof** — *User Need → Design KPI → Product KPI → Business KPI → Business Goal* — organized around four pillars (**Business Goals, Workflows, Mapping, Results**) and reinforced by a maturity model with five **Dimensions** (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence).

## Read the reference first

Before answering substantive questions, read:

- `reference.md` — full compressed content of the Lead block, including the four pillars, the 20 measurable goals mapped to 9 business pressures (Growth, Retention, User Experience, Efficiency, Operations), the 8 cross-functional workflow templates (Sales, Marketing, Product, Engineering, Strategy, Operations, Finance, Legal), the Mapping ladder, the Results loop, and the 15-symptom diagnostic from the v1.1 Results / Dimensions doc.

## How to apply

1. **Diagnose where the user is on the Chain of Proof.** If they have a UX metric but can't name the Product KPI it ties to, that's the gap. If they have a Product KPI but no Business KPI, that's the next gap. Don't move to executive language until each rung is named.

2. **Use the Quick Test for every metric the user proposes** as evidence: *(a) Does it prove the design works for users? (b) Does it show adoption or retention at the product level? (c) Does it connect to growth, churn, or revenue at the business level?* All three must be yes for the metric to count as a **signal**, not a vanity number.

3. **Anchor to the 9 business pressures.** Push the user to name which pressure (Growth, Retention, UX, Efficiency, Operations) the work serves. Then map to one of the 20 measurable goals from the reference (e.g., "Reduce churn → Achieve product–market fit").

4. **For cross-functional translation, use the workflow templates.** Each function (Sales, Marketing, Product, etc.) has its own metrics, questions, measurement approach, and lift opportunity. When the user is preparing a readout, frame the same signal in the receiving function's language — design ROI lands differently in a Finance review than in an Engineering retro.

5. **For maturity / org diagnosis, use the five Dimensions and 15-symptom diagnostic.** Help the user pinpoint whether the alignment between user needs and business goals is breaking at Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, or Scaling Influence — then prescribe the corresponding next move.

6. **Push from outputs to outcomes.** A pillar of Lead is that most teams stop at outputs (wireframes, prototypes, polished UI) and stall when leaders ask "Did it work?" If the user is delivering an artifact, force the question: *what outcome did this drive, and how is it visible to leadership?*

## Critical rules

- **Every rung of the Chain of Proof must be named** — User Need → Design KPI → Product KPI → Business KPI → Business Goal; don't jump to executive language until every rung is filled in.
- **A metric must pass the three-part Quick Test to count as a signal** — (a) proves design works for users, (b) shows adoption or retention at the product level, (c) connects to growth, churn, or revenue at the business level; one missing answer makes it a vanity number.
- **Anchor every initiative to one of the 9 business pressures** — Growth, Retention, UX, Efficiency, or Operations; work without a named pressure won't survive an executive review.
- **Translate signals into the receiving function's language** — design ROI lands differently in a Finance review than an Engineering retro; use the workflow template for Sales, Marketing, Product, Engineering, Strategy, Ops, Finance, or Legal.
- **Outputs aren't outcomes** — wireframes and prototypes don't answer "did it work"; force the outcome question on every artifact and make the result visible to leadership.

## Function-by-function quick reference

When the conversation narrows to a receiving function, drop into `glare:lead-workflows` for the full per-function template. At a glance:

| Function | Where design creates lift |
|---|---|
| Sales | Trial friction → smooth onboarding that accelerates revenue recognition |
| Marketing | Sharper messaging and stronger campaign performance from user signals |
| Product | Feature hunches → early proof of adoption and retention |
| Engineering | Catching usability failures before they consume sprints/production cycles |
| Strategy | De-risking innovation by proving desirability and differentiation early |
| Operations | Design fixes become operational savings and smoother processes |
| Finance | Making design ROI visible and defensible |
| Legal | Preventing legal exposure by simplifying risky experiences (consent, accessibility) |

## Handoffs

- Picking the underlying business pressure / measurable goal → `glare:lead-business-goals`
- Translating signals into a specific function's vocabulary (Sales, Marketing, Product, Engineering, Strategy, Ops, Finance, Legal) → `glare:lead-workflows`
- Drawing the full User Need → Design KPI → Product KPI → Business KPI → Business Goal ladder → `glare:lead-mapping`
- Initiatives → Findings → Decisions → Outcomes loop, maturity diagnostic, 15-symptom checks → `glare:lead-results`
- Parent area above this facet (Define / Measure / Focus / Lead together) → `glare:decision-map`
- Upstream signal collection (siblings under the Decision Map) → `glare:define`, `glare:measure`, `glare:focus`
- Signal anatomy and quality (the building blocks Lead translates) → `glare:design-signals`, plus bucket-level: `glare:signals-components`, `glare:signals-types`, `glare:signals-quality`, `glare:signals-capturing`
- Preparing for or evaluating a leadership review using the SIGNAL framework (Surface / Identify / Ground / Navigate / Align / Lock) → `glare:design-review`
- Assessing team / org design maturity → `glare:design-assessment`
