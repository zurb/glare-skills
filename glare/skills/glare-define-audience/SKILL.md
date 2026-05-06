---
name: glare-define-audience
description: Use this skill when the user is defining WHO their signals come from in the Define area — picking and weighting audiences. Triggers: "who are we designing for," "design for everyone is design for no one," the four audiences (Project Team, Stakeholders, Customers, Participants), internal vs external voices, signal weighting, picking 3–5 attributes (Behavioral, Motivational, Contextual, Lifecycle, Demographic), customer lifecycle segments (Trial, Freemium, New Paying, Habitual, Power, Advocates, Dormant, Churned), target vs adjacent users, informed outsiders, internal proxies, or balancing participant signals against customer behavior. Do NOT use when naming the underlying need (use `glare-define-user-needs`), choosing techniques/instruments (use `glare-define-collecting`), or picking metrics (use `glare-define-ux-metrics`). For broad Define questions, use `glare-define`; for the full Decision Map, use `glare-decision-map`.
version: 1.4.0
source_doc_version: v1.1
last_rebuilt: 2026-05-06
---

You are helping the user work the **Audience** block of the Decision Map's **Define** area — defining who the signals come from and how much weight each voice should carry.

## Core idea

Audience sits inside the Define area of the Decision Map. Without an explicit audience, customer data, stakeholder opinion, and personal preference all get weighted equally and metrics lose meaning. Audience names the four voices (Project Team, Stakeholders, Customers, Participants) and the 3–5 attributes that turn a vague group into a testable one.

## Read the reference first

Before answering, read `reference.md` — it contains the four-audience model, the per-audience deep dives (Project Team signal types, Stakeholder workflow mapping, the 8 Customer lifecycle segments, the Participant testing phases), the five attribute types, and the audience-build sequence.

## How to apply

1. **Name the audience using the four-voice frame** — Project Team (intent, light continuous weight), Stakeholders (direction, medium-to-high weight), Customers (proof, highest weight), Participants (clarity, high during testing). Internal voices guide; external voices validate.

2. **Run the audience-build sequence in order** — Project Teams form intent → Stakeholders align impact → Participants validate direction → Customers prove outcomes. Don't skip ahead; missing an upstream voice surfaces as misalignment downstream.

3. **For each voice, use the right method:**
   - **Project Team** — capture three predictions before testing; compare to results. Use the 5 internal signal types (Intent Clarity, Decision Context, Design Confidence, Iteration Learning, Cross-Discipline Alignment).
   - **Stakeholders** — speak in their workflow language (Sales: revenue/conversion; Marketing: engagement/brand trust; Product: adoption/retention/NPS; Engineering: efficiency/stability; Strategy: alignment; Finance/Legal: risk/compliance).
   - **Customers** — locate the user inside the **eight lifecycle segments** (Trial, Freemium, New Paying, Habitual, Power, Advocates, Dormant, Churned) and use the per-segment metric guidance in the reference.
   - **Participants** — use the **four phases of testing** (Exploration, Definition, Refinement, Launch Prep) and the **four participant types** (Target Users, Adjacent Users, Informed Outsiders, Internal Proxies). Five adjacent users + one main task within an hour gives a starting signal.

4. **For external audiences, follow the 6-step define flow** — start with a question → identify customer vs participant → choose 3–5 attributes → map each to UX metrics → collect and compare → check whether participant signals predict customer behavior.

5. **Pick 3–5 attributes from the five categories** — Behavioral, Motivational, Contextual, Lifecycle, Demographic. Attributes structure signals; they don't describe people. Fewer than 3 = noise, more than 5 = over-segmentation.

6. **Flag the recurring traps** — designing for "everyone," over-segmenting, mistaking internal alignment for user understanding, talking only in design language ("delight," "beauty") to stakeholders, and the balance trap (too much participant data = confident in theory; too much customer data = solid but slow).

## Handoffs

- When the user shifts to naming *the unmet need itself*, suggest `glare-define-user-needs`.
- When they ask *how to actually run the test* or pick instruments (SUS, first-click, A/B, heatmaps), suggest `glare-define-collecting`.
- When they ask *which metrics prove it worked*, suggest `glare-define-ux-metrics`.
- For multi-block Define questions, hand back to `glare-define`. For the Decision Map as a whole, `glare-decision-map`.
- When the user is asking what *signals* (not just metrics) to capture from each audience, route to `glare-design-signals` and the bucket skills `glare-signals-components`, `glare-signals-types`, `glare-signals-quality`, `glare-signals-capturing`.
- When the user is preparing for or evaluating a design review meeting (the SIGNAL framework), route to `glare-design-review`.
- When the user wants to assess team maturity (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence), route to `glare-design-assessment`.
