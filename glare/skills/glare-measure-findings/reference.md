# Reference — Glare Measure: Findings

Verbatim extraction of the Findings-relevant sections of `measure-compressed.md`.

NOTE: Findings has the thinnest dedicated module in v1.0; much of the Findings flow is also described inside the Concepts module ("Step 3 — Findings → Turning Data into Signals") and the v1.1 Questioning transitions table. Both are included below.

---

## Glare | Measure, Findings v1.0

Findings are the final move of Measure: they turn raw data into design signals tied to both user value and business outcomes.

- **Why findings matter**: Data alone (drop-offs, survey scores) only tells what happened. Findings make data evidence — connecting it to user needs and business goals so every metric ties back to intent.
- **What a finding is**: An observation turned into direction; takes patterns from research and connects them to a design choice. A strong finding is: tied to a design decision; linked to a user need; connected to a business goal; expressed as a clear, actionable design signal.
- **Step 1 — Translate Data Into Findings**. Pair the metric with its source and describe the behavior. Ask: what are users doing/struggling with, and how do we know? Example — Data: 48% drop-off at payment step (checkout analytics). Finding: Analytics show nearly half of users abandon checkout when choosing a payment option.
- **Step 2 — Tie to User Value**. Map finding to a specific user need (comprehension, usefulness, satisfaction, clarity, trust). Ask: which user need does this reveal or threaten? Example — User Value: Clarity, users need payment choices to be simple and error-free.
- **Step 3 — Tie to Business Results**. Link to a business metric leadership cares about (conversion, retention, efficiency, revenue). Ask: if we fix this, how does it move the business? Example — Reducing abandonment increases conversion and revenue.
- **Step 4 — Connect Back to Intent**. Cross-check the finding against the original concept/hunch. If it doesn't answer it, it's noise. Example — Hunch: "Simplifying payment will reduce abandonment." Finding confirms hunch and validates concept.
- **Step 5 — Act on Signals**. Write recommendation tied to both user and business metrics. Worked example:
  - Data: 48% drop-off at payment (checkout analytics)
  - Finding: Confusing payment options cause abandonment
  - User Need: Clarity — choose payment without errors
  - Business Goal: Reduce abandonment → increase conversion
  - **Signal**: Simplifying payment options will increase completion (business metric) and lower error rate (user metric).
- **Why this matters**: UX metrics tell you what happened; signals tell you what to do next. Without findings, teams stall in debates; with them, ideas earn their way forward fast. Findings close the loop — research → signals → action.

---

## When to use

- When the user is turning raw data into evidence-backed signals — drop-off rates, survey scores, heatmaps, task-success numbers.
- When tying a finding to a user need (comprehension, usefulness, satisfaction, clarity, trust).
- When tying a finding to a business result (conversion, retention, efficiency, revenue).
- When cross-checking findings against the concept or hunch.
- When following the chain raw data → finding → user value → business results → act.
- When deciding signal vs noise — "metrics don't tell us anything yet."

**Don't use when** anchoring intent (use `glare-measure-concepts`), forming a hunch (`glare-measure-hunches`), drafting questions (`glare-measure-questioning`), or asking about the loop (`glare-measure`).

## Findings as described inside Concepts v1.0

- **Step 3 — Findings → Turning Data into Signals**. Inputs: measurement data. Outputs: signals tied to business and customer outcomes. A signal forms when metrics tie to a design choice, a user need, and a business goal. Process: translate data → findings → tie to user value → tie to business results → connect back to intent → act → share widely.
- **From Intent to Signals (summary loop)**: (1) Concepts define intent, (2) Ideation produces hunches & questions, (3) Findings turn data into signals — shrinking big initiatives into focused efforts and replacing debate with evidence.

---

## Findings within the Questioning v1.1 transitions

- Element-to-Questioning mapping: Findings (emerging patterns → questioning supplies the input).
- Next-step transitions: Questioning→Findings (collect & analyze through metrics) → Findings→Signals (combine metrics into patterns proving impact).
- Workflow integration practice: "Share the questions, not just the answers" — include the question that led to a finding.

---

## Supporting framing (from Overview)

- *Findings* call-outs: spot patterns that reveal blockers; translate data into actionable signals; align user and business needs; share to build trust.

---

## Key terms (Findings-relevant)

- **Finding** — An observation translated into direction, linked to a user need, business goal, and design decision.
- **Signal** — Evidence-backed recommendation that tells the team what to do next; the output of the Measure loop. Replaces opinion-based debate.
- **Vanity metrics** — Metrics disconnected from intent; what concepts/signals are designed to avoid.
- **UX Metric Types** — Behavioral (what users do), Attitudinal (what they think/feel), Performance (how efficiently they succeed), Perceptual (what they understand).

## Failure modes

These are common ways this skill goes wrong in practice:

- **Finding = data.** Reporting "drop-off is 40%" as a finding. That's data — the finding adds the user need it ties to, the business result it implies, and the recommended action.
- **Finding without a user need.** Numbers without a "what users were trying to do" connection produce dashboards, not direction. Always name the user need the finding touches.
- **Finding that doesn't loop back to the Concept.** Each finding should be testable against the original Concept's intent. Findings that drift produce parallel stories that never converge.
- **Confusing noise for signal.** Acting on a small movement in a metric before checking sample size, comparison baseline, or whether the metric is leading or lagging. Use the four UX metric filters before treating a finding as actionable.

