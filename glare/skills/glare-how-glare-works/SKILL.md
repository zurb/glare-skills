---
name: glare-how-glare-works
description: Use this skill when the user wants the conceptual tour of how Glare actually works as a system — questions like "how does Glare work," "what are the parts of Glare," "explain Design Signals + Decision Map + Design Review + Design Assessment," "how do the four components fit together," "show me the loop," "what is the Decision Map," "what are the five dimensions," or "how does Glare hold across teams over time." Also use when the user is comparing Glare to other frameworks/processes and wants the architecture, or when they need to see how prompts → Skills → signals → reviews → decisions → outcomes → assessment connect as a continuous loop. Do NOT use when the user wants to actually try it on a live decision (use `glare-create-first-signal`) or when they want the AI workflow specifics (use `glare-ai-workflows`).
---

You are giving the user the **system tour** of Glare — how the four connected components work together to move ideas into decisions and decisions into outcomes.

## Core idea

Glare is built around four parts that connect: **Design Signals** (the unit of clarity), **Decision Map** (how decisions take shape across Define / Measure / Focus / Lead), **Design Review** (where signals get applied in real time), and **Design Assessment** (how the system holds across the org over time, scored across five dimensions). Each part feeds the next; the loop builds rather than resets.

## Read the reference first

Before answering, read `reference.md` — full breakdown of all four components, the Decision Map's four areas (Define, Measure, Focus, Lead), the five dimensions (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence), what a strong vs. weak Design Review looks like, and the closing loop diagram (prompts → Skills → signals → reviews → decisions → outcomes → assessment).

## How to apply

1. **Diagnose what altitude the user is at.** Are they (a) asking what Glare is at all (route to `glare-get-started` first), (b) wanting the architecture tour (this skill), or (c) wanting to start working (route to `glare-create-first-signal`)? This skill is for (b) — the conceptual tour.

2. **Lead with the four components.** Don't explain in any other order:
   - **Design Signals** — the unit of clarity. What turns a hunch into something concrete.
   - **Decision Map** — how decisions take shape. Define / Measure / Focus / Lead. Not stages; teams move back and forth.
   - **Design Review** — where signals get applied. The moment work is presented and a decision is expected.
   - **Design Assessment** — how decisions move through the system over time. Diagnoses where the work is breaking.

3. **Show the loop, not the list.** Always close the tour with the loop: prompt → Skill → signal → review → decision → outcome → assessment. The output of one step becomes the input of the next. Each loop builds on the last; nothing resets.

4. **For the Decision Map specifically**, explain the four areas and emphasize they are not phases:
   - **Define** — what problem are we solving? what matters here?
   - **Measure** — how is this performing? what are users showing us?
   - **Focus** — which direction is stronger? what should move forward?
   - **Lead** — what do we commit to? how does it connect to outcomes?

5. **For the Design Assessment**, walk through the **five dimensions** and what each one diagnoses (Organizing Work / Managing Complexity / Building Proof / Guiding Decisions / Scaling Influence). Emphasize that the assessment is about **patterns over time**, not single moments — it shows where signals are being created consistently, where decisions are landing vs. drifting, and where the system is holding.

6. **Resist over-explaining any one component.** When a user gets curious about a specific part, hand off — don't try to teach it all in this skill.

## Handoffs

- Working through a real first signal → `glare-create-first-signal`
- Going deeper on what a signal *is* and how it's structured → `glare-design-signals`
- Going deeper on Design Review specifically → `glare-design-review`
- Going deeper on Design Assessment / the five dimensions → `glare-design-assessment`
- Going deeper on a Decision Map area → `glare-define`, `glare-measure`, `glare-focus`, `glare-lead`
- AI workflow specifics (prompts vs. Skills vs. agents) → `glare-ai-workflows`
- Term lookup → `glare-glossary`
