# Glare | Focus, Initiatives — Drafted (no source doc available)

> This block is **drafted from framework knowledge**, not from a dedicated Drive source doc. It extrapolates from `focus-compressed.md` (Comparing v1.1), the `glare-focus` parent skill, and vocabulary established in Measure (`measure-compressed.md`) and Lead (`lead-compressed.md`). Treat as best-effort scaffolding until an authoritative "Glare | Focus, Initiatives" source lands.

## What this block is about

In Glare v1.0, **Initiatives** is the upstream step of the Focus facet (sequence: Initiatives → Methods → Comparing → Decisions). Initiatives is where teams make the "why this, why now?" of a design effort *explicit and measurable* before any signal is collected. Per the Comparing doc: "Initiatives — define goals/outcomes; benchmarking validates whether each one is achieved." Without a well-formed Initiative, Methods has nothing to instrument and Comparing has no anchor to validate against.

## Glare | Focus, Initiatives v0.1 (drafted)

**What an Initiative is.** A focused design effort framed by a user need, a business goal, and a target outcome that future benchmarking will validate. Initiatives sit between the broader Concept work in Measure (which produces hunches and questions) and the operational Methods step that follows. An Initiative is *not* a deliverable ("redesign checkout"); it is a *measurable shift* ("increase checkout completion on mobile from 62% to 75% by Q3").

**Three outcomes Initiatives create:**
- **Direction** — the team knows what "better" looks like before any test runs.
- **Measurability** — every Initiative names the UX metric(s) Comparing will later move on a 100-point scale.
- **Repeatability** — version, date, and audience are recorded at definition time, so the Initiative produces a baseline that holds up across releases.

### Anchors — User Need + Business Goal

Per the Glare signal model (carried forward from Measure), every Initiative requires both anchors. Without them, the work produces motion without direction.

- **User Need anchor.** Pulled from Define (or Measure → Concepts). Frame as: "Users need [outcome] so they can [purpose]." Example: "Users need to choose a payment method without errors so they can finish checkout in one session."
- **Business Goal anchor.** Pulled from Lead → Business Goals (one of the 20 measurable goals across Growth / Retention / UX / Efficiency / Operations). Frame as: "[Reduce/grow/improve] [business KPI] in service of [strategic pressure]." Example: "Reduce payment-step abandonment to drive revenue growth."

If either anchor is missing or fuzzy, the Initiative is not ready to advance to Methods.

### The Goal / Outcome / Metric Template

Every Initiative writes one of these. Tight, three-line, dense.

```
GOAL:    [Plain-language intent — what the team is trying to change]
OUTCOME: [Observable shift — what will be different for the user / business]
METRIC:  [One or two UX metrics from the 100-point stack:
          Comprehension, Satisfaction, Desirability, Completion,
          Error Rate, First-Click Success, Time-on-Task]
         + target delta and audience
```

Worked example:
```
GOAL:    Make payment selection easier on mobile checkout.
OUTCOME: First-time mobile users complete checkout without restarting.
METRIC:  Completion (target +13 pts: 62 → 75 / mobile, first-time, US)
         Error Rate (target −8 pts on payment step)
```

### The Four Anchor Questions (must be answered before benchmarking)

The Comparing doc requires baselines tied to a goal; Initiatives is where those answers are produced. A team is not allowed to start Methods until all four are written down:

1. **Why this, why now?** What pressure (user friction, business KPI, competitive gap, leadership ask) made this Initiative rise to the top?
2. **Who is the audience?** Cohort, segment, device, journey stage. This is the audience Methods will recruit and Comparing will normalize against.
3. **What does success look like?** Stated as the metric delta on the 100-point scale, not as a deliverable.
4. **What would a kill look like?** What signal would tell us this Initiative isn't worth advancing? (Per Big Idea #12, *kill* is a legitimate Decision move; it has to be defined upfront, not retrofitted.)

If question 4 can't be answered, the Initiative is too vague to falsify and will produce vanity outcomes.

### Initiative Record — Worksheet

| Field | Action | Output |
|---|---|---|
| User Need | Pull from Define / Measure → Concepts. Write one sentence. | Anchored intent. |
| Business Goal | Pull from Lead → 20 measurable goals. Tie to one of 9 pressures. | Strategic relevance. |
| Outcome | State the observable shift — not the deliverable. | Falsifiable target. |
| Metric(s) | 1–2 from the 100-point stack + target delta + audience. | Methods can instrument; Comparing can baseline. |
| Anchor Q's | Answer all four (why now / who / success / kill). | Initiative is benchmarking-ready. |
| Version, Date, Audience | Record at definition time. | Repeatable baseline downstream. |

**Quick Checklist:** user need + business goal anchored; outcome stated as a shift; metric(s) on the 100-point scale with target delta; audience defined; "what a kill looks like" written down; version/date/audience captured.

### See It in Action — Mobile Checkout Initiative

A retail product team has six months of analytics showing 38% of first-time mobile users abandon at the payment step. Leadership wants conversion lift. Past attempts ran without a defined Initiative — three redesigns shipped, no one could say which moved the metric.

Initiative record (drafted in 20 minutes):
- **User Need:** "First-time mobile users need to pick a payment method without errors so they can finish checkout in one session." (from Define)
- **Business Goal:** "Reduce payment-step abandonment → drive revenue growth." (from Lead, Growth bucket)
- **Outcome:** First-time mobile users in the US complete checkout on the first attempt.
- **Metric:** Completion +13 pts (62 → 75), Error Rate −8 pts. Audience: first-time mobile / US.
- **Anchor Q's:**
  1. Why now? Q3 revenue plan depends on mobile conversion.
  2. Who? First-time mobile users, US, iOS + Android.
  3. Success? Completion ≥75 / Error Rate ≤22 in the v2 benchmark.
  4. Kill? If v2 lands within ±2 pts of baseline on both metrics, kill the redesign track and route the problem to a different Initiative (likely payment-provider integration, owned by Engineering).
- **Version / Date / Audience:** v1 baseline / 2026-04-22 / first-time mobile US (n≥120).

This Initiative is now ready to hand to Methods, which will design the cadence and instruments to collect the v1 baseline and the v2 comparison.

### Next Steps from Initiatives

- → **Methods** — design how the named metrics get collected for v1 baseline and future iterations.
- → **Comparing** — once data lands, validate against the outcome and metric targets defined here.
- → **Decisions** — closes the loop by reporting whether the Initiative's outcome was achieved, partially achieved, or missed (and which decision-move to make).

## Key terms

- **Initiative** — a focused design effort framed by user need + business goal + target outcome + measurable UX metric(s); the anchor for everything Methods, Comparing, and Decisions do downstream.
- **User Need anchor / Business Goal anchor** — the two required framings for every Initiative; pulled from Define and Lead respectively.
- **Outcome** — the observable shift the Initiative is supposed to produce; never a deliverable.
- **Goal/Outcome/Metric template** — the three-line definition every Initiative writes before advancing.
- **Four Anchor Questions** — why now / who / success / kill; all four must be answered before benchmarking is allowed.
- **Kill criterion** — the upfront definition of what signal would end the Initiative; required for falsifiability.
- **100-point UX metric stack** — Comprehension, Satisfaction, Desirability, Completion, Error Rate, First-Click Success, Time-on-Task; the metrics an Initiative chooses from.
- **Baseline-readiness** — Initiative has named version, date, and audience so Comparing's Step 1 can repeat reliably.
