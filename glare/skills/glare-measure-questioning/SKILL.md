---
name: glare-measure-questioning
description: Use this skill when the user is drafting, critiquing, or organizing research questions in the Decision Map's Measure area. Triggers include sorting questions into the four types — **People** (habits/behaviors), **Process** (steps/friction), **Product** (clarity/usefulness), **Problem** (barriers); choosing a Mode of Questioning — **Exploratory** (early discovery), **Evaluative** (does this design work?), **Comparative** (which version wins?); running the bias check (leading? echoing internal assumptions? emotionally loaded? jargon-heavy?); promoting open-ended research questions into testable ones (e.g., "Do people like our homepage?" → "Can users find pricing info on the homepage within 5 seconds?"); aligning each question to a UX metric family — Behavioral, Attitudinal, Performance, Perceptual; matching questions to techniques like First Click Testing, Heatmaps, Clickstream, Surveys; running the 8-step v1.1 process; building a Question Library; or using the Glare Questioning Canvas. Do NOT use when the user is still anchoring intent (use `glare-measure-concepts`), forming a "we believe..." hunch (use `glare-measure-hunches`), translating data into signals (use `glare-measure-findings`), or asking about the four-move loop holistically (use `glare-measure`). For the full Decision Map, use `glare-decision-map`. For the outcome-keyed Need / Use / Prefer / Adopt signal-type taxonomy (different question than the UX-metric families), use `glare-signals-types`.
version: 1.3.0
source_doc_version: v1.1
last_rebuilt: 2026-05-04
---

You are helping the user work through the **Questioning** move of the Decision Map's **Measure** area — sharpening hunches into neutral, testable prompts that yield usable signals.

## Core idea

Questioning sits inside the Measure area of the Decision Map. Weak questions stall in indecision; strong questions expose where users struggle, what they value, and whether the design works. Questioning aligns metrics to intent through four question types, three modes (Exploratory / Evaluative / Comparative), and an 8-step refinement process.

Note on taxonomies: the **Behavioral / Attitudinal / Performance / Perceptual** families used here are *UX-metric* families — what kind of number a question yields. Glare also catalogs an outcome-keyed *signal-type* taxonomy — **Need / Use / Prefer / Adopt** — that asks a different question (which kind of decision the resulting signal informs). Both exist; if the user is asking which family of metric a question maps to, stay here; if they're asking what kind of signal coverage they're missing, route to `glare-signals-types`.

## Read the reference first

Before answering substantive questions, read `reference.md` — it contains the verbatim Questioning v1.0 and v1.1 material, the four question types, the modes, the 8-step process, the bias check, the testable-question criteria, and the metric-and-technique mapping tables.

## How to apply

1. **Clarify the initiative (Step 1).** Ask: what are we trying to learn, improve, or validate? What decision will this inform? Where in the process are we — exploration, prototyping, post-launch? Who needs the insight, and what's the risk if we get it wrong? In v1.1, this becomes "clarify the concept" — surface assumptions and what success looks like if the hunch is right.

2. **Sort questions into the four types.** **People** (habits/preferences/behaviors — "How often do users complete this workflow?"); **Process** (steps + friction — "What steps do users take to upload a file?"); **Product** (clarity/usefulness — "Do users understand the purpose of this page?"); **Problem** (barriers — "What prevents users from completing checkout?"). People + Process give context; Product + Problem give clarity.

3. **Pick a Mode of Questioning (v1.1).** **Exploratory** — early discovery, no firm hypotheses, "What should we learn or improve?", yields patterns and unmet needs. **Evaluative** — mid-cycle, designs exist, "Does this design work for users?", yields clarity/comprehension/usability metrics. **Comparative** — late-stage, choosing between directions, "Which version performs better?", yields confidence and proof of improvement.

4. **Write open-ended research questions, then translate to testable ones (Steps 4–5).** Run the bias check on every draft: is it leading? Echoing internal assumptions? Emotionally loaded or too technical? A testable question defines a gap, points to observable behavior or perception, and can be measured and acted upon. Weak: *"Do people like our homepage?"* Strong: *"Can users find pricing info on the homepage within 5 seconds?"*

5. **Align each question to a UX metric family and technique (Steps 6 & 8).** Behavioral (heatmaps, clickstream, first-click); Attitudinal (surveys, satisfaction, sentiment); Performance (task success, time on task, error rate); Perceptual (comprehension — v1.1 addition). Mapping examples: "Can users locate pricing within 5 seconds?" → First Click Testing; "Do users understand the page purpose?" → Survey + Heatmap; "What stops checkout?" → Clickstream + Task Success.

6. **Prioritize, refine, and integrate (Step 7 + workflow).** Filter by Gap Size, Impact, Feasibility, and Confidence — questions at the intersection of large-gap + high-impact + feasible rise to top. Make it a routine: weekly Discovery Review, pair every sprint task with at least one measurable question, post-test reflection on which questions produced usable signals, share the question alongside the answer, and grow a reusable Question Library.

## Handoffs

- Once questions are bias-checked, metric-aligned, and matched to techniques, hand off to `glare-measure-findings` to translate the resulting data into signals.
- If the underlying hunch is vague or non-falsifiable, route back to `glare-measure-hunches`.
- If there's no clear concept, route back to `glare-measure-concepts`.
- For the four-move loop overview, use `glare-measure`. For the Decision Map as a whole, `glare-decision-map`.
- When the user is asking what *signals* the questions should produce — six-part anatomy (design intuition + UX metric + user need + context + business goal + direction) and outcome-keyed Need / Use / Prefer / Adopt coverage — route to `glare-design-signals` and the bucket skills `glare-signals-components`, `glare-signals-types`, `glare-signals-quality`, `glare-signals-capturing`.
- When the user is preparing for or evaluating a design review meeting (the SIGNAL framework), route to `glare-design-review`.
- When the user wants to assess team maturity (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence), route to `glare-design-assessment`.
