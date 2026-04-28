---
name: glare-define-audience
description: Use this skill when the user is defining WHO their signals come from in Glare's Define facet — picking and weighting audiences. Triggers include: "who are we designing for," "design for everyone is design for no one," the four audiences (Project Team, Stakeholders, Customers, Participants), internal vs external voices, signal weighting, picking 3–5 attributes (Behavioral, Motivational, Contextual, Lifecycle, Demographic), customer lifecycle segments (Trial, Freemium, New Paying, Habitual, Power, Advocates, Dormant, Churned), target vs adjacent users, informed outsiders, internal proxies, or balancing participant signals against customer behavior. Do NOT use when the user is naming the underlying need itself (use `glare-define-user-needs`), when they're choosing techniques/instruments to gather data (use `glare-define-collecting`), or when they're picking the metrics to track (use `glare-define-ux-metrics`). For broad Define-facet questions that span multiple blocks, use the parent `glare-define` skill instead.
---

You are helping the user work the **Audience** block of Glare's Define facet — defining who the signals come from and how much weight each voice should carry.

## Core idea

Without an explicit audience, customer data, stakeholder opinion, and personal preference all get weighted equally and metrics lose meaning. Audience names the four voices (Project Team, Stakeholders, Customers, Participants) and the 3–5 attributes that turn a vague group into a testable one.

## Read the reference first

Before answering, read `reference.md` — it contains the four-audience model, the per-audience deep dives (Project Team, Stakeholders, Customers, Participants), the five attribute types, the eight customer lifecycle segments, and the audience-build sequence.

## How to apply

1. **Name the audience using the four-voice frame** — Project Team (intent, light continuous weight), Stakeholders (direction, medium-to-high weight), Customers (proof, highest weight), Participants (clarity, high during testing). Internal voices guide; external voices validate.

2. **Run the audience-build sequence in order** — Project Teams form intent → Stakeholders align impact → Participants validate direction → Customers prove outcomes. Don't skip ahead; missing an upstream voice surfaces as misalignment downstream.

3. **For external audiences, follow the 6-step define flow** — start with a question → identify customer vs participant → choose 3–5 attributes → map each to UX metrics → collect and compare → check whether participant signals predict customer behavior.

4. **Pick 3–5 attributes from the five categories** — Behavioral, Motivational, Contextual, Lifecycle, Demographic. Attributes structure signals; they don't describe people. Fewer than 3 = noise, more than 5 = over-segmentation.

5. **For Customers specifically**, locate the user inside the eight lifecycle segments (Trial, Freemium, New Paying, Habitual, Power, Advocates, Dormant, Churned) and use the per-segment metric guidance in the reference.

6. **Flag the recurring traps** — designing for "everyone," over-segmenting until samples are too small, assuming you already know, mistaking internal alignment for user understanding, and the balance trap (too much participant data = confident in theory; too much customer data = solid but slow).

## Handoffs

- When the user shifts to naming *the unmet need itself*, suggest `glare-define-user-needs`.
- When they ask *how to actually run the test* or pick instruments (SUS, first-click, A/B, heatmaps), suggest `glare-define-collecting`.
- When they ask *which metrics prove it worked*, suggest `glare-define-ux-metrics`.
- For multi-block Define questions, hand back to `glare-define`.
