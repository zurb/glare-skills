---
name: glare-measure-questioning
description: Use this skill when the user is drafting, critiquing, or organizing research questions in the Measure area. Triggers — sorting questions into the four types — **People** (habits/behaviors), **Process** (steps/friction), **Product** (clarity/usefulness), **Problem** (barriers); choosing a Mode — **Exploratory**, **Evaluative**, **Comparative**; the bias check (leading? loaded? jargon-heavy?); promoting open questions into testable ones (e.g., "Do people like our homepage?" → "Can users find pricing within 5 seconds?"); aligning to a UX metric family — Behavioral, Attitudinal, Performance, Perceptual; the Glare Questioning Canvas; building a reusable Question Library. Do NOT use when anchoring intent (use `glare-measure-concepts`), forming a hunch (use `glare-measure-hunches`), translating data (use `glare-measure-findings`), or asking about the loop (use `glare-measure`). For the Decision Map, use `glare-decision-map`. For Need / Use / Prefer / Adopt, use `glare-signals-types`.
version: 2.2.1
source_doc_version: v1.1 (Questioning) — refreshed 2026-05-11
last_rebuilt: 2026-05-11
---

You are helping the user work through the **Questioning** move of the Decision Map's **Measure** area — sharpening hunches into neutral, testable prompts that yield usable signals.

## Core idea

Questioning sits inside the Measure area of the Decision Map. Weak questions stall in indecision; strong questions expose where users struggle, what they value, and whether the design works. Questioning aligns metrics to intent through four question types, three modes (Exploratory / Evaluative / Comparative), and an 8-step refinement process. It is the bridge in the rhythm **Concepts → Hunches → Questions → Findings**.

Note on taxonomies: the **Behavioral / Attitudinal / Performance / Perceptual** families used here are *UX-metric* families from the Questioning v1.1 source doc — what kind of number a question yields. Glare also catalogs an outcome-keyed *signal-type* taxonomy — **Need / Use / Prefer / Adopt** — that asks a different question (which kind of decision the resulting signal informs). Both exist; if the user is asking which family of metric a question maps to, stay here; if they're asking what kind of signal coverage they're missing, route to `glare-signals-types`.

## Read the reference first

Before answering substantive questions, read `reference.md` — it contains the verbatim Questioning v1.1 material, the four question types, the modes, the 8-step process, the bias check, the testable-question criteria, the metric-and-technique mapping tables, the 5 integration routines, the Question Library concept, and the source-doc note about the Perceptual → Intelligence taxonomy shift in v1.32 UX Metrics.

## How to apply

Source-doc structure: **Getting Started → Begin Questioning → Make It Practical → See It in Action → Apply and Evolve**.

1. **Clarify the concept (Step 1).** Surface assumptions and what success looks like if the hunch is right. Ask: what assumptions are we making? what part of this concept do we most need to understand? what would success look like?

2. **Identify knowledge gaps (Step 2).** Turn hunches upside down — what's untested, where confidence is weak, what would surprise you if false.

3. **Define learning goals (Step 3) by picking a Mode.** **Exploratory** — early discovery, "What should we learn or improve?", yields patterns/context/unmet needs. **Evaluative** — mid-cycle, designs exist, "Does this design work for users?", yields clarity/comprehension/usability metrics. **Comparative** — late-stage, choosing between directions, "Which version performs better?", yields confidence and proof of improvement.

4. **Write open-ended research questions, then translate to testable ones (Steps 4–5).** Run the bias check on every draft: is it leading? Echoing internal assumptions? Emotionally loaded or too technical? A testable question (1) defines a gap, (2) points to observable behavior or perception, (3) can be measured and acted upon. Weak: *"Do people like our homepage?"* Strong: *"Can users find pricing info on the homepage within 5 seconds?"*

5. **Sort questions across the 4 types.** **People** (habits/preferences/behaviors); **Process** (steps + friction); **Product** (clarity/usefulness); **Problem** (barriers). People + Process give context; Product + Problem give clarity.

6. **Align each question to a UX metric family and technique (Steps 6 & 8).** Behavioral (first-click, task success — "Where do users click first?"); Attitudinal (surveys, satisfaction scoring — "How confident do users feel?"); Performance (time on task, error rate — "How long does checkout take?"); Perceptual (comprehension — "Do users understand this page?"). *Helio note —* behavioral and attitudinal techniques can run directly in Helio as leading indicators before product reaches real traffic.

7. **Prioritize, refine, and integrate (Step 7 + workflow routines).** Filter by Gap Size, Impact, Feasibility, and Confidence — questions at the intersection of large-gap + high-impact + feasible rise to the top. Then build it into the team rhythm with the 5 routines (see below).

## 5 routines for integrating questioning into workflow

1. **Weekly Discovery Review** — frame the week's assumptions into testable questions.
2. **Sprint Planning** — pair every major task with at least one measurable question, visible on the board.
3. **Post-Test Reflection** — review which questions produced usable signals; refine the broad or biased ones.
4. **Share the Questions, Not Just the Answers** — when reporting findings, include the question that led to them so others can replicate.
5. **Build a Question Library** — collect well-framed, tested questions in a shared workspace and reuse them across projects for consistency.

## Handoffs

- Once questions are bias-checked, metric-aligned, and matched to techniques, hand off to `glare-measure-findings` to translate the resulting data into signals.
- If the underlying hunch is vague or non-falsifiable, route back to `glare-measure-hunches`.
- If there's no clear concept, route back to `glare-measure-concepts`.
- For the four-move loop overview, use `glare-measure`. For the Decision Map as a whole, `glare-decision-map`.
- If the user crosses into UX-metric framework work, route to `glare-ux-metrics` (v1.32 uses **Attitudinal · Behavioral · Performance · Intelligence** as the 4 types — Perceptual content has merged into Behavioral). Inside Questioning, the v1.1 wording (Perceptual) is preserved.
- When the user is asking what *signals* the questions should produce — six-part anatomy (design intuition + UX metric + user need + context + business goal + direction) and outcome-keyed Need / Use / Prefer / Adopt coverage — route to `glare-design-signals` and the bucket skills `glare-signals-components`, `glare-signals-types`, `glare-signals-quality`, `glare-signals-capturing`.
- When the user is preparing for or evaluating a design review meeting (the SIGNAL framework), route to `glare-design-review`.
- When the user wants to assess team maturity (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence), route to `glare-design-assessment`.
