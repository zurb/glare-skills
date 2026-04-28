---
name: glare-lead-workflows
description: Use this skill when the user is translating design signals into the language of a specific business function — the Workflows bucket of the Glare Lead facet. The bucket ships eight named cross-functional templates (Sales, Marketing, Product, Engineering, Strategy, Operations, Finance, Legal), each with its own top metrics, questions to ask, measurement approach, jargon glossary, and "where design creates lift" angle. Triggers include preparing a readout for one of those eight functions; naming the lift design creates inside one of them; running the workflow Quick Test (friction-free success → adoption/retention move → metric the function already tracks); doing the 30-minute Quick Exercise of picking one function and mapping a single metric into it; or borrowing the function's vocabulary (pipeline, CAC, PMF, velocity, market share, handle time, LTV, compliance rate) instead of design jargon. Do NOT use for choosing the underlying business pressure or measurable goal — invoke `glare-lead-business-goals`. Do NOT use for the full User Need → Design KPI → Product KPI → Business KPI → Business Goal ladder — invoke `glare-lead-mapping`. Do NOT use for the Initiatives → Findings → Decisions → Outcomes loop or maturity diagnostic — invoke `glare-lead-results`. For broader Lead facet framing, invoke parent `glare-lead`.
---

You are helping the user work through the **Workflows** bucket of the Glare Lead facet — the eight cross-functional rails design signals must travel to gain weight inside an org. Each function has its own per-function template (Sales, Marketing, Product, Engineering, Strategy, Operations, Finance, Legal) with metrics, questions, measurement approach, jargon, and a lift opportunity.

## Core idea

Every company runs on workflows already in motion whether design is in the room or not. Design gets sidelined when it can't prove influence on those flows; signals only travel when they're translated into each function's existing metrics, questions, and lift opportunities.

## Read the reference first

Before answering substantive questions, read `reference.md` — it contains the per-function detail (top metrics, questions, how to measure, lift opportunity, jargon glossary, focus/show signal chain, and a fast example) plus the Quick Exercise and Quick Test. Each section is the verbatim-distilled v1.0 doc for that function.

## How to apply

1. **Pick the receiving function.** A signal lands differently in a Finance review than in an Engineering retro. Force the user to name a single primary audience, then open that function's section in `reference.md`.

2. **Borrow the function's vocabulary, don't import yours.** Reframe the design signal in terms of the function's top metrics — Sales hears "trial-to-paid conversion lifted X%", not "task completion went 55→85". Each section lists the 5 jargon terms to mirror back ("pipeline" / "CAC" / "PMF" / "velocity" / "market share" / "handle time" / "LTV" / "compliance rate").

3. **Name the lift opportunity.** Each function has an explicit "where design creates lift" angle. Anchor the readout to that angle so the function sees the signal as something that improves their number, not extra work.

4. **Ask the function's questions back to them.** Use the 3 questions in each section to invite the function into diagnosis — this is what turns a one-way readout into a workflow that loops design signals into their decision cycles.

5. **Build the signal chain.** Each section gives the Design KPI → Product KPI → Business KPI ladder for that function. Use it to show the line from a usability metric to the function's headline number.

6. **Run the Workflows Quick Test.** Workflow impact is real only if all three are yes: (a) Did users succeed without friction? (b) Did adoption or retention improve? (c) Did it move a metric this function already tracks? If the third answer is no, you're still doing a design report, not a workflow handoff.

7. **Use the 30-minute Quick Exercise to start small.** Pick one function this week, ask their three questions, map one of their top metrics to a design signal, share a quick test. Treat this as the on-ramp — don't try to translate to all eight functions at once.

## Function-by-function quick reference

| Function | Top metrics | Lift opportunity |
|---|---|---|
| Sales | pipeline growth, conversion rates, quota attainment | trial friction → smooth onboarding that accelerates revenue recognition |
| Marketing | lead quality, campaign ROI, CAC | sharper messaging and stronger campaign performance from user signals |
| Product | feature adoption, retention, product–market fit | feature hunches → early proof of adoption and retention |
| Engineering | velocity, rework costs, defect rates | catching usability failures before they consume sprints/production cycles |
| Strategy | market share, innovation rate, competitive differentiation | de-risking innovation by proving desirability and differentiation early |
| Operations | efficiency, support costs, internal adoption speed | design fixes become operational savings and smoother processes |
| Finance | revenue growth, margin, ROI | making design ROI visible and defensible |
| Legal | compliance, liability cost, risk exposure | preventing legal exposure by simplifying risky experiences (consent, accessibility) |

See `reference.md` for the per-function questions, measurement approach, signal chain, jargon, and a worked example for each row.

## Handoffs

- Choosing the underlying business pressure or measurable goal → `glare-lead-business-goals`.
- Building the full Chain of Proof ladder → `glare-lead-mapping`.
- Initiatives → Findings → Decisions → Outcomes loop, maturity diagnostic → `glare-lead-results`.
- Broader Lead facet framing → parent `glare-lead`.
- Upstream signal collection → `glare-define`, `glare-measure`, `glare-focus`.
