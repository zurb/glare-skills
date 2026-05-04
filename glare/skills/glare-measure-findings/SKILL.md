---
name: glare-measure-findings
description: Use this skill when the user is in the Findings move of the Decision Map's Measure area — turning raw data into evidence-backed signals. Triggers include translating drop-off rates, survey scores, heatmaps, or task-success numbers into a finding; tying a finding to a user need (comprehension, usefulness, satisfaction, clarity, trust); tying a finding to a business result (conversion, retention, efficiency, revenue); cross-checking a finding against the original concept or hunch; writing a recommendation tied to both a user metric and a business metric (e.g., "Simplifying payment options will increase completion and lower error rate"); or running the full chain *raw data → finding → user value → business results → connect back to intent → act → share*. Also use when the user is sitting on metrics that "don't tell us anything yet," debating without evidence, or struggling to decide whether a result is a signal or noise. Do NOT use when the user is anchoring intent before any data exists (use `glare-measure-concepts`), forming a "we believe..." hunch (use `glare-measure-hunches`), drafting research questions (use `glare-measure-questioning`), or asking about the four-move loop holistically (use `glare-measure`). For the full Decision Map, use `glare-decision-map`. For the six-part signal anatomy and signal-quality checks, use the Design Signals skills (`glare-signals-components`, `glare-signals-quality`).
version: 1.3.0
source_doc_version: v1.1
last_rebuilt: 2026-05-04
---

You are helping the user work through the **Findings** move of the Decision Map's **Measure** area — closing the loop by translating raw data into design signals tied to both user value and business outcomes.

## Core idea

Findings is the closing move inside the Measure area of the Decision Map. Data alone (drop-offs, survey scores) only tells you what happened. A Finding becomes evidence when it ties to a design choice, a user need, AND a business goal — at that point it becomes a Signal that tells the team what to do next. The Design Signals section gives this signal a fuller anatomy (design intuition + UX metric + user need + context + business goal + direction) and an outcome-keyed type (Need / Use / Prefer / Adopt) — Findings is where the team first names the signal; the Signals skills are where it gets stress-tested.

## Read the reference first

Before answering substantive questions, read `reference.md` — it contains the verbatim Findings v1.0 material and the worked checkout example, plus the relevant translation steps surfaced inside the Concepts module.

## How to apply

1. **Translate data into a finding (Step 1).** Pair the metric with its source and describe the behavior. Ask: what are users doing or struggling with, and how do we know? *Data: 48% drop-off at the payment step (checkout analytics). Finding: Analytics show nearly half of users abandon checkout when choosing a payment option.*

2. **Tie the finding to user value (Step 2).** Map it to a specific user need — comprehension, usefulness, satisfaction, clarity, or trust. Ask: which user need does this reveal or threaten? *User Value: Clarity — users need payment choices to be simple and error-free.*

3. **Tie the finding to business results (Step 3).** Link it to a metric leadership cares about — conversion, retention, efficiency, revenue. Ask: if we fix this, how does it move the business? *Reducing abandonment increases conversion and revenue.*

4. **Connect back to the original intent (Step 4).** Cross-check the finding against the concept and the hunch that prompted the test. *If it doesn't answer them, it's noise.* A finding that doesn't tie back is data that should be set aside.

5. **Act on the signal (Step 5).** Write the recommendation tied to both a user metric and a business metric. Worked example: *Signal: Simplifying payment options will increase completion (business metric) and lower error rate (user metric).* If you cannot name both metrics in the recommendation, it isn't a signal yet — return to Step 2 or 3.

6. **Share widely.** A signal sitting in one person's notebook is wasted. Findings close the loop — research → signals → action — only when they reach the people who can act on them. Pair the signal with the question that produced it (the v1.1 Questioning practice) so context travels with the answer.

## Handoffs

- If the data was generated from poorly framed questions, route back to `glare-measure-questioning` to refine and re-test.
- If a finding doesn't tie to any current concept or hunch, escalate back to `glare-measure-concepts` or `glare-measure-hunches` — the underlying intent or bet may need to be re-stated.
- For the four-move loop overview or to orchestrate across buckets, use `glare-measure`. For the Decision Map as a whole, `glare-decision-map`.
- Once signals exist and the user wants to benchmark or compare versions/competitors, hand off to the Focus area (`glare-focus`).
- When the user wants to formalize the finding as a full Design Signal — six-part anatomy, outcome-keyed Need / Use / Prefer / Adopt coverage, signal-quality check, end-to-end capture workflow — route to `glare-design-signals`, `glare-signals-components`, `glare-signals-types`, `glare-signals-quality`, `glare-signals-capturing`.
- When the user is preparing for or evaluating a design review meeting (the SIGNAL framework), route to `glare-design-review`.
- When the user wants to assess team maturity (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence), route to `glare-design-assessment`.
