---
name: glare-define
description: Use this skill when the user is in the Define area of Glare's Decision Map — the "Credibility" stage where teams agree on what matters before building. Triggers — defining user needs, picking audience, gathering evidence, naming recurring situations, or choosing UX metrics; questions like "who are we designing for," "what user need does this solve," "wants vs needs," "what situation are we in," "the same condition keeps showing up," "engagement up but trust down." Also use when the user mentions the five user-need categories (Basics, Trust, Personal, Impact, Feelings); the four audience source types or four audience types; the four Situations lenses (By Type, By Time, By Stage, By Engagement); the three UX metric types (Attitudinal, Behavioral, Performance); or instruments like SUS, NPS, SEQ. Do NOT use when needs/metrics are set and the user is forming hypotheses — invoke `glare-measure`. For the broader Decision Map use `glare-decision-map`.
version: 3.5.0
source_doc_version: v1.4 (User Needs) + v1.2 (Audience, Collecting) + v1.0/v1.1 (Situations); v1.1 catalog for UX Metrics
last_rebuilt: 2026-05-26
---

You are helping the user work through the **Define** area of Glare's **Decision Map** — the "Credibility" stage that slows teams down just long enough to agree on what matters before building.

## Core idea

Define is the first area of the Decision Map (Define → Measure → Focus → Lead). It answers five questions: **(1)** What do users actually need? **(2)** Who are we learning from and how much do we trust each source? **(3)** How do we gather the right evidence? **(4)** What recurring situations keep producing the same behavior across users and sessions? **(5)** How will we know it worked? It does this through five building blocks — **User Needs, Audience, Collecting, Situations, UX Metrics** — that turn opinions, hunches, and vanity dashboards into testable signals that downstream areas can sharpen and act on.

**Important: Patterns was archived and replaced with Situations.** The 5th block of Define is now Situations (one level more concrete than User Needs — captures how a need manifests inside a specific context). The old `glare-define-patterns` skill is deprecated; route to `glare-define-situations` instead.

## Read the reference first

Before answering substantive questions, read:

- `reference.md` — full compressed content of the Define block, including the five user-need categories (Basics, Trust, Personal, Impact, Feelings) with all 20 individual need types; the four source types + four audience types with credibility model; the five-step Collecting process (Intent → Stack → Approach → Techniques → Connect); the four Situations lenses (By Type, By Time, By Stage, By Engagement) with the 9 named situation types; the UX metrics taxonomy (Attitudinal / Behavioral / Performance); and catalogs of techniques, instruments, and platforms.

## How to apply

1. **Identify which of the five blocks the user is in.** Don't try to cover all five — pick the one that matches their current question and stay there. **Situations is the newest block** (replaces Patterns); use it whenever the user is describing recurring conditions, signal convergence, or trying to interpret what a metric means in context.

2. **For User Needs:** Anchor in the **five-category stack** (Basics → Trust → Personal → Impact → Feelings) with **20 individual need types** nested inside. Walk in order; higher categories can't compensate for a broken lower one. Apply the validation rule: *if users say they need it but ignore it in practice, it's a want masquerading as a need.*

3. **For Audience:** Use the **four-source-type frame** (Helio = highest credibility for design; CRM = medium; Advertising = low for design; Internal Assumption = lowest) paired with the **four-audience-type frame** (Project Team = intent; Stakeholders = direction; Customers = proof; Participants = clarity). Output is the **Audience Definition Card** with a High/Medium/Low credibility rating.

4. **For Collecting:** Walk them through the **five-step process** — Start with Intent → Choose Your Stack → Identify the Approach (Exploratory / Evaluative / Comparative) → Apply the Techniques → Connect and Ready Your Data. Output is the **Collection Brief** (14 fields). Pair at least two of the four feedback types (View / See / Sense / Hear). Show Your Sources rule on every shared finding.

5. **For Situations:** Apply at least two of the **four lenses** (By Type, By Time, By Stage, By Engagement) and look for convergence. **One lens = observation. Two converging lenses = situation.** Match to one of the **9 named situation types** (Comprehension breakdown, Trust gap, Effort mismatch, Relevance failure, Habit formation gap, Expectation mismatch, Decision loop, Organizational blind spot, Signal credibility breakdown). Output is the **Primary Situation Output** (11 fields) including all four situation parts: trigger / goal / friction / what success means.

6. **For UX Metrics:** Treat metrics as the **grammar of signals**. Force a balance of attitudinal + behavioral + performance, and balance leading vs lagging indicators. Every metric must tie back to a UX outcome leaders can act on, not a vanity number.

7. **End every Define session by checking the quick-check questions:** Does this solve a real user goal? Is the audience defined with source and credibility? Is the collection effort structured into a Collection Brief? What recurring situation is producing this signal? Which metric proves progress? If any answer is fuzzy, the team isn't ready to leave Define.

## Critical rules

- **Stay in one block per turn** — don't try to cover User Needs, Audience, Collecting, Situations, and UX Metrics in a single answer; pick the block that matches the user's question and hold there.
- **Reject wants masquerading as needs** — if users say they need it but ignore it in practice, it's a want, not a need; the five-category stack must be walked in order.
- **Match source type to decision** — Helio audience groups for design credibility; advertising segments are for reach, not understanding.
- **Show Your Sources** — every Collection finding requires technique + audience + metrics. Without them, findings are opinions.
- **Two lenses minimum for Situations** — one lens is an observation, not a situation. A pattern in one lens is a starting point; convergence across two is what makes it nameable.
- **Every metric must tie to a UX outcome** — vanity numbers fail the test; require attitudinal + behavioral + performance balance.

## Handoffs

- Naming the underlying user need → `glare-define-user-needs`
- Defining who signals come from + signal weighting + credibility → `glare-define-audience`
- Choosing instruments, techniques, and tools to gather data → `glare-define-collecting`
- Recognizing recurring situations and naming them through the four lenses → `glare-define-situations` *(replaces deprecated `glare-define-patterns`)*
- Picking and balancing the metrics themselves → `glare-define-ux-metrics`
- Once needs / audience / metrics are locked, moving into hypotheses and tests → `glare-measure`
- Benchmarking and comparison after signals are collected → `glare-focus`
- Connecting work to business KPIs and executive narratives → `glare-lead`
- The full Decision Map (parent of Define / Measure / Focus / Lead) → `glare-decision-map`
- What signals to capture, the six-part anatomy, and signal types beyond UX metrics → `glare-design-signals`, `glare-signals-components`, `glare-signals-types`, `glare-signals-quality`, `glare-signals-capturing`
- Preparing for or evaluating a design review meeting (the SIGNAL framework) → `glare-design-review`
- Assessing team maturity across Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence → `glare-design-assessment`

**Deprecated:** `glare-define-patterns` — route to `glare-define-situations` instead.
