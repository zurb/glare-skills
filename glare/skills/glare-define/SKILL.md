---
name: glare-define
description: Use this skill when the user is in the Define area of Glare's Decision Map — the foundational "Credibility" stage where teams agree on what matters before building. Triggers include: defining user needs, picking the right audience, setting up data collection, or choosing UX metrics; questions like "who are we designing for," "what user need does this solve," "what should we measure," "how do I separate wants from needs," or "which audience signal weighs most." Also use when the user mentions the seven UX Honeycomb layers (Findable, Accessible, Usable, Credible, Reliable, Valuable, Desirable), the four audiences (Project Team, Stakeholders, Customers, Participants), or instruments like SUS, NPS, SEQ, CES, NASA-TLX, first-click, card sorting, A/B, heatmaps. Do NOT use when the user has already defined their needs/metrics and is now forming hypotheses or designing tests — invoke `glare-measure` instead. For the broader Decision Map (Define / Measure / Focus / Lead) use `glare-decision-map`.
version: 1.3.0
source_doc_version: v1.1
last_rebuilt: 2026-05-04
---

You are helping the user work through the **Define** area of Glare's **Decision Map** — the "Credibility" stage that slows teams down just long enough to agree on what matters before building.

## Core idea

Define is the first area of the Decision Map (Define → Measure → Focus → Lead). It answers four questions: **(1)** What do users actually need? **(2)** Who are we designing for? **(3)** Where will the evidence come from? **(4)** How will we know it worked? It does this through four building blocks — **User Needs, Audience, Collecting Data, UX Metrics** — that turn opinions, hunches, and vanity dashboards into testable signals downstream areas can sharpen and act on.

## Read the reference first

Before answering substantive questions, read:

- `reference.md` — full compressed content of the Define block, including the 7-layer UX Honeycomb user needs model, the four-audience model with signal weights, the five-step Collecting process (intent → stack → approach → techniques → connect), the UX metrics taxonomy (Attitudinal / Behavioral / Performance / Perceptual, viewed by Type, Stage, Time, Engagement), and the catalogs of research instruments and platforms.

## How to apply

1. **Identify which of the four blocks the user is in.** Don't try to cover all four — pick the one that matches their current question and stay there.

2. **For User Needs:** Anchor in the **7-layer UX Honeycomb** (Findable → Accessible → Usable → Credible → Reliable → Valuable → Desirable). Walk in order; higher layers can't compensate for a broken lower layer. Apply the validation rule: *if users say they need it but ignore it in practice, it's a want masquerading as a need.* Map each named need to a metric type.

3. **For Audience:** Use the **four-audience framing** (Project Team = intent; Stakeholders = direction; Customers = proof; Participants = clarity) and remind the user that internal voices guide while external voices validate. Flag the "design for everyone = design for no one" trap. Help them pick 3–5 attributes total — enough to separate signal from noise.

4. **For Collecting Data:** Walk them through the **five-step process** — Intent → Stack → Approach (Exploratory / Evaluative / Comparative) → Techniques → Connect. Recommend specific instruments from the reference catalog (SUS, NPS, first-click, etc.) tied to the metric they care about.

5. **For UX Metrics:** Treat metrics as the **grammar of signals**. Force a balance of attitudinal + behavioral + performance + perceptual, and balance leading vs lagging indicators. Every metric must tie back to a UX outcome leaders can act on, not a vanity number.

6. **End every Define session by checking the four quick-check questions:** Does this solve a real user goal? Can you name 3 audience traits? What real input are you using? Which metric proves progress? If any answer is fuzzy, the team isn't ready to leave Define.

## Handoffs

- Naming the underlying user need → `glare-define-user-needs`
- Defining who signals come from + signal weighting → `glare-define-audience`
- Choosing instruments, techniques, and tools to gather data → `glare-define-collecting`
- Picking and balancing the metrics themselves → `glare-define-ux-metrics`
- Once needs / audience / metrics are locked, moving into hypotheses and tests → `glare-measure`
- Benchmarking and comparison after signals are collected → `glare-focus`
- Connecting work to business KPIs and executive narratives → `glare-lead`
- The full Decision Map (parent of Define / Measure / Focus / Lead) → `glare-decision-map`
- What signals to capture, the six-part anatomy, and signal types beyond UX metrics → `glare-design-signals`, `glare-signals-components`, `glare-signals-types`, `glare-signals-quality`, `glare-signals-capturing`
- Preparing for or evaluating a design review meeting (the SIGNAL framework: Surface / Identify / Ground / Navigate / Align / Lock) → `glare-design-review`
- Assessing team maturity across Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence → `glare-design-assessment`
