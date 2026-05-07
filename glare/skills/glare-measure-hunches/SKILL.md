---
name: glare-measure-hunches
description: Use this skill when the user is forming a Hunch in the Measure area — turning instinct into a falsifiable, testable hypothesis. Triggers — writing or critiquing a "we believe..." statement, the hunch template *"We believe that [change] for [audience] will [impact] because [reason]"*, the belief primer *"We believe users need ___ so they can ___"*, checking falsifiability, strengthening weak hunches (e.g., "users like shorter forms" → "removing two steps will increase completion because users drop off at step 3"), spark techniques (Empathy Mapping, Customer Journey, Stakeholder Interviews, Competitive Analysis, Expert Audit). Also when tying an instinct to a UX metric (completion rate, task time, drop-off). Do NOT use when intent isn't defined (use `glare-measure-concepts`), moving into questions (use `glare-measure-questioning`), interpreting data (use `glare-measure-findings`), or wanting the loop overview (use `glare-measure`). For the Decision Map, use `glare-decision-map`.
version: 1.3.0
source_doc_version: v1.1
last_rebuilt: 2026-05-04
---

You are helping the user work through the **Hunches** move of the Decision Map's **Measure** area — turning a shaped instinct into a falsifiable hypothesis that downstream questions and findings can confirm or kill.

## Core idea

Hunches sits inside the Measure area of the Decision Map. A Hunch is an informed guess: *"We believe there is something important here, and we are ready to test it."* A strong hunch is tied to a user friction, expressed as a clear hypothesis, linked to a metric, and **falsifiable** — it could be wrong, and that's the point.

## Read the reference first

Before answering substantive questions, read `reference.md` — it contains the verbatim Hunches material, the belief and hypothesis templates, the spark techniques, and the weak-vs-strong examples.

## How to apply

1. **Start with context (Step 1).** Tie the hunch to a business goal, a design principle, or a specific user-journey moment. Ask: what are we designing, who for, and what do we already know? Hunch-building is shared work — bring it into standups, sketch sessions, or research reviews. The first hunch won't be the last.

2. **Capture initial assumptions (Step 2)** using the spark techniques: Survey Data, Ideation Sketching, Empathy Mapping, Customer Journey Framework, Stakeholder Interviews, Customer Feedback, Data Analytics, Competitive Analysis, Expert Audit. Pick the one that fits the evidence already on hand.

3. **Spot opportunities on the problem, not the solution (Step 3).** Ask: what feels clunky or confusing? Where are unmet needs? Where can we add value or reduce effort? If the user is naming features, redirect to friction.

4. **Form the hunch in two passes (Step 4).** First write the belief statement: *"We believe users need ___ so they can ___."* Then promote it to a design hypothesis using the verbatim template: *"We believe that [this change] for [this group] will [have this impact] because [supporting reason]."*
   - Weak: "We believe users like shorter forms."
   - Stronger: "We believe removing two steps from the signup form for first-time users will increase completion rates because users drop off at step 3."

5. **Pressure-test for falsifiability.** Ask: what behavior would confirm or disprove this? What would have to be true? How will we know? If no observation could refute the hunch, it isn't one — it's an opinion. Reject and rewrite.

6. **Translate into questions and link to a UX metric (Step 5).** Bind the hunch to completion rate, task time, drop-off, or a comparable metric so results become signals, not opinions. Treat the next round of evidence as input to refine the hunch, not as a final verdict — keep the learning loop alive post-launch.

## Handoffs

- Once the hunch is concretely worded, falsifiable, and metric-linked, hand off to `glare-measure-questioning` to draft the open-ended and testable research questions.
- If the user has no clear concept underneath the hunch, send them back to `glare-measure-concepts` to pass the 5-minute test first.
- If they already have data and want to interpret it, route to `glare-measure-findings`.
- For the full four-move loop or orchestration across buckets, use `glare-measure`. For the Decision Map as a whole, `glare-decision-map`.
- When the user is asking what *signals* would test or sharpen this hunch (six-part anatomy, outcome-keyed Need / Use / Prefer / Adopt coverage), route to `glare-design-signals` and the bucket skills `glare-signals-components`, `glare-signals-types`, `glare-signals-quality`, `glare-signals-capturing`.
- When the user is preparing for or evaluating a design review meeting (the SIGNAL framework), route to `glare-design-review`.
- When the user wants to assess team maturity (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence), route to `glare-design-assessment`.
