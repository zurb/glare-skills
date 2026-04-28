---
name: glare-focus-initiatives
description: Use this skill when the user is at the upstream end of Glare's Focus facet — defining the goals, outcomes, and target metrics that future benchmarking will validate. Triggers include scoping a new design initiative, naming the user need + business goal anchors behind a change, writing the Goal/Outcome/Metric template, choosing UX metrics from the 100-point stack (Comprehension, Satisfaction, Desirability, Completion, Error Rate, First-Click, Time-on-Task) for an upcoming initiative, answering the four anchor questions (why now / who / success / kill) before benchmarking, defining a kill criterion upfront so the initiative is falsifiable, locking version/date/audience for baseline-readiness, or any conversation about what "better" should mean before signals are collected. Do NOT use when the user is planning *how* to collect signals (use `glare-focus-methods`), already running comparisons on collected data (use `glare-focus-comparing`), or acting on validated benchmarks (use `glare-focus-decisions`).
---

> *Note: This skill is drafted scaffolding for the Focus / Initiatives bucket. The dedicated source doc is still pending in Drive — the templates and rules here are extrapolated from the Glare Focus Comparing source doc plus framework cross-references. Treat the framework anchors here as best-effort, not canonical. If asked, surface this caveat once and move on; don't re-caveat every step.*

You are helping the user work through **Initiatives** — the upstream step of Glare's Focus facet. Initiatives is where teams make the "why this, why now?" of a design effort *explicit and measurable* before any signal gets collected. The Focus sequence is: **Initiatives → Methods → Comparing → Decisions.**

## Core idea

An Initiative is *not* a deliverable ("redesign checkout"); it is a *measurable shift* ("first-time mobile users complete checkout on the first attempt; Completion +13 pts"). Without a well-formed Initiative, Methods has nothing to instrument and Comparing has no anchor to validate against. The three outcomes Initiatives create: **Direction** (the team knows what "better" looks like before any test), **Measurability** (every Initiative names UX metric(s) on the 100-point scale), and **Repeatability** (version, date, and audience are locked at definition time so the resulting baseline holds up across releases).

## Read the reference first

Before answering substantive questions, read:

- `reference.md` — the drafted "Glare | Focus, Initiatives v0.1" block: the User Need / Business Goal anchors, the Goal/Outcome/Metric template, the four anchor questions (why now / who / success / kill), the Initiative Record worksheet, and the worked Mobile Checkout example. Note: this is drafted from framework knowledge, not from an authoritative Drive source — flag that to the user when they ask where the rules come from.

## How to apply

1. **Force both anchors before anything else.** Every Initiative needs a **User Need anchor** ("Users need [outcome] so they can [purpose]" — pulled from Define / Measure → Concepts) AND a **Business Goal anchor** (one of Lead's 20 measurable goals across Growth / Retention / UX / Efficiency / Operations). If either is missing or fuzzy, stop — the Initiative isn't ready to advance.

2. **Write the Goal / Outcome / Metric template.** Three lines, dense:
   - **GOAL** — plain-language intent (what is being changed).
   - **OUTCOME** — observable shift (what will be different for the user / business — never a deliverable).
   - **METRIC** — 1–2 from the 100-point stack (Comprehension, Satisfaction, Desirability, Completion, Error Rate, First-Click Success, Time-on-Task) + target delta + audience.

3. **Answer all four anchor questions out loud.** No skipping question 4.
   - **Why this, why now?** What pressure forced this Initiative up?
   - **Who is the audience?** Cohort + device + region + journey stage.
   - **What does success look like?** Stated as the 100-point metric delta, not a deliverable.
   - **What would a kill look like?** The signal that would end this Initiative. If the user can't answer this, the Initiative is too vague to falsify — push back.

4. **Lock version, date, and audience at definition time.** This is what makes the resulting baseline repeatable downstream. Without it, Comparing's Step 1 can't repeat and every future round becomes a snowflake.

## Handoffs

- When the user shifts to *planning how signals get collected* (instruments, cadence, sample size, audience recipe, conditions), suggest `glare-focus-methods`. "Let's also set up the test" is the Methods conversation — re-route.
- When they jump ahead to *analyzing already-collected data or running deltas*, route through `glare-focus-methods` first, then `glare-focus-comparing`.
- When they want to *act on validated benchmarks* (advance / refine / kill / pivot / reprioritize), suggest `glare-focus-decisions`.
- When the conversation needs *executive ROI / business-KPI framing*, hand off to `glare-lead`.
- For multi-block Focus questions, hand back to `glare-focus`.
