---
name: glare-define
description: Use this skill when the user is in the Define area of Glare's Decision Map — the "Credibility" stage where teams agree on what matters before building. Triggers — defining user needs, picking audience, recognizing recurring patterns, setting up data collection, or choosing UX metrics; questions like "who are we designing for," "what user need does this solve," "wants vs needs," "what pattern are we seeing," "pattern library," "patterns," "engagement up but trust down." Also use when the user mentions the five user-need categories (Basics, Trust, Personal, Impact, Feelings); the four audiences (Project Team, Stakeholders, Customers, Participants); the four pattern types (User, Workflow, Signal, AI Workflow); the three UX metric types (Attitudinal, Behavioral, Performance); or instruments like SUS, NPS, SEQ, NASA-TLX, first-click, card sorting, A/B, heatmaps. Do NOT use when needs/metrics are set and the user is forming hypotheses — invoke `glare-measure`. For the broader Decision Map use `glare-decision-map`.
version: 3.1.0
source_doc_version: v1.1 + patterns v1.0
last_rebuilt: 2026-05-13
---

You are helping the user work through the **Define** area of Glare's **Decision Map** — the "Credibility" stage that slows teams down just long enough to agree on what matters before building.

## Core idea

Define is the first area of the Decision Map (Define → Measure → Focus → Lead). It answers five questions: **(1)** What do users actually need? **(2)** Who are we designing for? **(3)** What recurring situations keep producing the same behavior? **(4)** Where will the evidence come from? **(5)** How will we know it worked? It does this through five building blocks — **User Needs, Audience, Patterns, Collecting Data, UX Metrics** — that turn opinions, hunches, and vanity dashboards into testable signals downstream areas can sharpen and act on. Patterns is the newest block (v1.0, added 2026-05-11): it helps teams recognize recurring situations before weak decisions gain momentum, which matters more now that AI is generating outputs faster than teams can evaluate them.

## Read the reference first

Before answering substantive questions, read:

- `reference.md` — full compressed content of the Define block, including the five user-need categories (Basics, Trust, Personal, Impact, Feelings) with all 22 individual need types nested under them; the four-audience model with signal weights; the **four pattern types** (User, Workflow, Signal, AI Workflow); the five-step Collecting process (Intent → Stack → Approach → Techniques → Connect); the UX metrics taxonomy (Attitudinal / Behavioral / Performance), and the catalogs of techniques, instruments, and platforms.

## How to apply

1. **Identify which of the five blocks the user is in.** Don't try to cover all five — pick the one that matches their current question and stay there. The fifth block, Patterns, is new in v2.3 — use it whenever the user is describing recurring situations, signal tradeoffs, or AI-accelerated workflow breakdowns rather than a single need, audience, instrument, or metric.

2. **For User Needs:** Anchor in the **five-category stack** (Basics → Trust → Personal → Impact → Feelings). Walk in order; higher categories can't compensate for a broken lower one. When the user names a specific need (e.g., "findable," "secure," "engaging"), pin it to its category and to a metric. Apply the validation rule: *if users say they need it but ignore it in practice, it's a want masquerading as a need.*

3. **For Audience:** Use the **four-voice frame** (Project Team = intent; Stakeholders = direction; Customers = proof; Participants = clarity) and remind the user that internal voices guide while external voices validate. Flag the "design for everyone = design for no one" trap. Help them pick 3–5 attributes total — enough to separate signal from noise.

4. **For Patterns:** Pin the recurring **situation**, not just the behavior — situations create meaning, so the same metric can mean five different things. Match the user's description to one of the four pattern types: **User Patterns** (hesitation, abandonment, comparison paralysis), **Workflow Patterns** (review cycles, late validation, siloed optimization), **Signal Patterns** (engagement up while trust down, usability up while retention weak), **AI Workflow Patterns** (faster output, weaker evaluation, overproduction). Patterns matter more now because AI accelerates output faster than evaluation — patterns slow the team just enough to interpret the signal before momentum scales a weak decision.

5. **For Collecting Data:** Walk them through the **five-step process** — Intent → Stack → Approach (Exploratory / Evaluative / Comparative) → Techniques → Connect. Recommend specific instruments from the reference catalog (SUS, NPS, first-click, etc.) tied to the metric they care about.

6. **For UX Metrics:** Treat metrics as the **grammar of signals**. Force a balance of attitudinal + behavioral + performance, and balance leading vs lagging indicators. Every metric must tie back to a UX outcome leaders can act on, not a vanity number. Helio appears throughout as the way to capture attitudinal and behavioral signals as leading indicators before product ships.

7. **End every Define session by checking the five quick-check questions:** Does this solve a real user goal? Can you name 3 audience traits? What recurring pattern keeps showing up around this situation? What real input are you using? Which metric proves progress? If any answer is fuzzy, the team isn't ready to leave Define.

## Critical rules

- **Stay in one block per turn** — don't try to cover User Needs, Audience, Patterns, Collecting, and UX Metrics in a single answer; pick the block that matches the user's question and hold there.
- **Reject wants masquerading as needs** — if users say they need it but ignore it in practice, it's a want, not a need; the five-category stack (Basics → Trust → Personal → Impact → Feelings) must be walked in order.
- **Never design for everyone** — internal voices guide and external voices validate; force 3–5 audience attributes before signal collection, or you'll get noise.
- **Every metric must tie to a UX outcome** — vanity numbers fail the test; require attitudinal + behavioral + performance balance and a tie back to a user need leaders can act on.
- **Don't leave Define with fuzzy answers** — if the five quick-check questions (real goal, 3 traits, recurring pattern, real input, proving metric) can't all be answered cleanly, the team isn't ready for Measure.

## Handoffs

- Naming the underlying user need → `glare-define-user-needs`
- Defining who signals come from + signal weighting → `glare-define-audience`
- Recognizing recurring situations (User / Workflow / Signal / AI Workflow patterns) → `glare-define-patterns`
- Choosing instruments, techniques, and tools to gather data → `glare-define-collecting`
- Picking and balancing the metrics themselves → `glare-define-ux-metrics`
- Once needs / audience / metrics are locked, moving into hypotheses and tests → `glare-measure`
- Benchmarking and comparison after signals are collected → `glare-focus`
- Connecting work to business KPIs and executive narratives → `glare-lead`
- The full Decision Map (parent of Define / Measure / Focus / Lead) → `glare-decision-map`
- What signals to capture, the six-part anatomy, and signal types beyond UX metrics → `glare-design-signals`, `glare-signals-components`, `glare-signals-types`, `glare-signals-quality`, `glare-signals-capturing`
- Preparing for or evaluating a design review meeting (the SIGNAL framework: Surface / Identify / Ground / Navigate / Align / Lock) → `glare-design-review`
- Assessing team maturity across Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence → `glare-design-assessment`
