---
name: glare-lead-results
description: Use this skill when the user is closing the loop between learning and leadership trust — the Results bucket of the Lead facet. Triggers — running the Project Work loop (Initiatives → Findings → Decisions → Outcomes); identifying which layer is broken; assessing maturity against the five Dimensions (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence); spotting any of the 15 diagnostic symptoms ("metrics exist but no one trusts them," "loudest voice wins," "wins stay local"); the three principles (See → Tighten workflow → Measure what matters); the Results Alignment Checklist; Helio Glare Assessment; "clarity beats precision" mantra. Also the University Website case study (nav +36%, RFI +19%, homepage +57%). Do NOT use for pressures/goals — use `glare-lead-business-goals`. Do NOT use for cross-functional language — use `glare-lead-workflows`. Do NOT use for the KPI ladder — use `glare-lead-mapping`. For broader Lead, use `glare-lead`.
version: 1.3.0
source_doc_version: v1.1
last_rebuilt: 2026-05-04
---

You are helping the user work through the **Results** bucket of the Glare Lead facet — the upward-facing area of the **Decision Map** — where signals prove value through a continuous Initiatives → Findings → Decisions → Outcomes loop, reinforced by a five-Dimension maturity model.

## Core idea

Results is part of the upward-facing area of the Decision Map (Lead). It's proof that design bridges user needs and business goals. That bridge holds when the four-layer Project Work loop stays connected and when the team can name which of the five Dimensions of Design Maturity (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence) is currently breaking.

## Read the reference first

Before answering substantive questions, read `reference.md` — it contains the verbatim five components of "How to Read Results", the five Dimensions table, the three principles, the 15-symptom diagnostic with calibrations, the Results Alignment Checklist, and the University Website case study.

## How to apply

1. **Map one initiative through the four-layer loop.** Initiatives → Findings → Decisions → Outcomes. If a layer is missing — no quantified Findings, no logged Decision, no Outcome rolled to a business goal — that gap *is* the workflow break. Use the v1.1 prompt: "map one initiative right now; identify findings, decisions, outcomes. If one is missing, that's where your workflow is breaking."

2. **Apply the three improvement principles in order.** (1) See what's happening — make initiatives, findings, decisions visibly connected. (2) Tighten the workflow — close loops between evidence and action. (3) Measure what matters — outcomes that show real progress, not vanity numbers.

3. **Locate the symptom on the 15-symptom diagnostic.** When the user describes a pain point, match it to one of the 15 symptoms in `reference.md`, then identify which Dimension it lives under (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence) and apply the verbatim calibration tip — e.g., "metrics exist but no one trusts them" → Building Proof → "define measurable success upfront; tie tests to decisions."

4. **Fix one area at a time.** The diagnostic instruction is explicit: spot the pattern → match the dimension → apply the calibration → measure → then move on. Resist the urge to address multiple Dimensions in one pass.

5. **Run the Results Alignment Checklist for a structured pass.** (1) Map one initiative through findings/decisions/outcomes. (2) Identify where alignment breaks between user needs and business goals. (3) Apply the calibration from the diagnostic. (4) Re-measure in one week. (5) Share proof and reconnect teams around evidence.

6. **Use the outcomes mantra to defuse attribution debates.** "Perfect attribution is rare and that's fine. What matters is direction and progress. Clarity beats precision every time." When a stakeholder demands airtight causation, redirect to direction-of-travel evidence anchored in the loop.

## Handoffs

- Picking the underlying business pressure or measurable goal that an Outcome rolls up to → `glare-lead-business-goals`.
- Translating an Outcome into a specific function's vocabulary for a readout → `glare-lead-workflows`.
- Drawing the explicit User Need → Design KPI → Product KPI → Business KPI → Business Goal ladder behind an Outcome → `glare-lead-mapping`.
- Broader Lead facet framing → parent `glare-lead`.
- Decision Map area above Lead → `glare-decision-map`.
- Upstream signal collection that feeds Findings (Decision Map siblings) → `glare-define`, `glare-measure`, `glare-focus`.
- Signal anatomy and quality (the units Findings are built from) → `glare-design-signals`, `glare-signals-components`, `glare-signals-types`, `glare-signals-quality`, `glare-signals-capturing`.
- Preparing for or evaluating a leadership review using the SIGNAL framework (Surface / Identify / Ground / Navigate / Align / Lock) → `glare-design-review`.
- Assessing team / org design maturity (broader companion to the five Dimensions) → `glare-design-assessment`.
