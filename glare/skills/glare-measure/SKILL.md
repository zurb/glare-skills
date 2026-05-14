---
name: glare-measure
description: Use this skill when the user is producing evidence within the Decision Map's Measure area — turning intuition into testable signals. Triggers include forming hypotheses or hunches ("we believe that [change] for [audience] will [impact] because [reason]"), writing research questions, running tests, interpreting findings, or building a Question Library. Also use when the user mentions Concepts (anchoring intent), Hunches (falsifiable bets), Questioning (People / Process / Product / Problem question types), or Findings (translating data into signals tied to user value + business results). Use when they reference UX metric families like Behavioral, Attitudinal, Performance, or Perceptual. Do NOT use when the user is still defining who/what to study (use `glare-define`) or when they have results and now want to compare versions/competitors (use `glare-focus`). For the broader Decision Map (Define / Measure / Focus / Lead) use `glare-decision-map`.
version: 3.1.0
source_doc_version: v1.1
last_rebuilt: 2026-05-13
---

You are helping the user work through the **Measure** area of Glare's **Decision Map** — the discipline of turning intuition into evidence-backed design signals.

## Core idea

Measure is the second area of the Decision Map (Define → Measure → Focus → Lead). It operates as a four-move loop: **Concepts → Hunches → Questioning → Findings.** It takes big initiatives, breaks them into testable bets, sharpens them with neutral questions tied to UX metrics, and converts raw data into actionable signals tied to both user needs and business goals. Data alone is noise; Measure is how teams produce clarity leaders can trust in the moment.

## Read the reference first

Before answering substantive questions, read:

- `reference.md` — full compressed content of the Measure block, including the four-move loop, hunch templates, question-type taxonomy (People / Process / Product / Problem), UX metric families (Behavioral / Attitudinal / Performance / Perceptual), the Findings → Signals translation steps, and the v1.1 Exploratory / Evaluative / Comparative question modes.

## How to apply

1. **Locate the user in the four-move loop.** Are they framing a Concept, forming a Hunch, drafting Questions, or interpreting Findings? Don't drift backward — Measure flows in order.

2. **For Concepts:** Force the 5-minute test — *if you can't write user need + business goal + signal in under 5 minutes, the concept isn't clear.* Pull user needs from Define and business goals from Lead; one actionable concept at a time.

3. **For Hunches:** Use the verbatim template: *"We believe that [change] for [this group] will [have this impact] because [supporting reason]."* A strong hunch is tied to a user friction point, expressed as a provable hypothesis, linked to a metric, and **falsifiable**. Reject vague hunches like "users like shorter forms"; rewrite them concretely.

4. **For Questioning:** Use the four question types — **People** (habits/behaviors), **Process** (steps/friction), **Product** (clarity/usefulness), **Problem** (barriers). Run the bias check: leading? echoing internal assumptions? emotionally loaded? jargon-heavy? In v1.1, also tag each set as Exploratory, Evaluative, or Comparative.

5. **For Findings:** Run the translation chain — *raw data → finding → tie to user value → tie to business results → connect back to original intent → act → share widely.* A signal forms only when a metric ties to a design choice, a user need, AND a business goal. If any of those three is missing, it's not a signal yet.

6. **Tie every output to a UX metric type** (Behavioral, Attitudinal, Performance, Perceptual) so the result is comparable in the next facet. Hand off to `glare-focus` once findings exist and need benchmarking.

## Critical rules

- **Measure flows in order — don't drift backward** — Concepts → Hunches → Questioning → Findings is sequential; if a Concept isn't clear, no amount of better questions will fix the loop.
- **Hunches must be falsifiable** — use the verbatim template *"We believe that [change] for [this group] will [have this impact] because [supporting reason]"*; reject vague hunches like "users like shorter forms" and rewrite them concretely.
- **Apply the 5-minute Concept test** — if user need + business goal + signal can't be written in under 5 minutes, the Concept isn't clear; stop and resolve before drafting questions.
- **Run the bias check on every question** — reject questions that are leading, echo internal assumptions, are emotionally loaded, or jargon-heavy; tag each set Exploratory, Evaluative, or Comparative.
- **A signal needs all three ties** — metric + user need + business goal; if any one is missing, it's data, not a signal, and Focus will turn into opinion downstream.

## Handoffs

- Anchoring intent before any solution exists → `glare-measure-concepts`
- Forming a "we believe..." falsifiable hunch → `glare-measure-hunches`
- Drafting and bias-checking research questions → `glare-measure-questioning`
- Translating raw data into signals → `glare-measure-findings`
- Upstream definition of needs / audience / metrics → `glare-define`
- Benchmarking versions, competitors, segments → `glare-focus`
- Rolling outcomes to business KPIs / ROI → `glare-lead`
- The full Decision Map (parent of Define / Measure / Focus / Lead) → `glare-decision-map`
- What signals to capture (six-part anatomy + outcome-keyed Need / Use / Prefer / Adopt types) and how to evaluate / capture them → `glare-design-signals`, `glare-signals-components`, `glare-signals-types`, `glare-signals-quality`, `glare-signals-capturing`
- Preparing for or evaluating a design review meeting (the SIGNAL framework: Surface / Identify / Ground / Navigate / Align / Lock) → `glare-design-review`
- Assessing team maturity across Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence → `glare-design-assessment`
