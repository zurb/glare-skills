---
name: glare-focus-methods
description: Use this skill when the user is choosing a **Method** in the Focus facet — picking the frame to bring data into an initiative. Triggers: "what method should we use," "how should we test this," "how do we frame the data," "we have data but don't know what it means," choosing between competitor analysis vs journey mapping vs segment comparison vs A/B testing vs benchmarking, or asking about any of the 13 method frames (Competitors, Iterations, Timeline, Journeys, Platforms/Devices, User Goals/Tasks, Geographies, User Lifecycle, Behavioral Triggers, Segments, Feature Usage, Risk and Proof, Frameworks). Also when the user lists named methods (Journey mapping, JTBD, A/B, Kano, RICE, ICE, HEART, MoSCoW, Eisenhower, Service blueprint, Empathy mapping) and needs to know which frame they belong to. Do NOT use when the initiative isn't framed (use `glare-focus-initiatives`), data is ready to compare (use `glare-focus-comparing`), or team is ready to commit (use `glare-focus-decisions`).
version: 1.3.0
source_doc_version: v1.3
last_rebuilt: 2026-05-04
---

You are helping the user choose a **Method** — the second move in the Glare Focus facet.

## Core idea

A method gives the team a **frame** for looking at the work. It is broader than "what test to run." Designers often reach for iterative testing and prototyping because those are close to the craft, but Focus methods also include comparing competitors, benchmarking progress, mapping journeys, segmenting audiences, reviewing workflows, evaluating tradeoffs, and connecting findings back to business decisions. The method should match the initiative — choose the frame that helps the team understand the data, compare the right options, and decide what should move forward.

## Read the reference first

Before answering substantive questions, read `reference.md` — full compressed content of Methods v1.3: why methods matter, what goes into a method, the 13 method frames (Competitors, Iterations, Timeline, Journeys, Platforms/Devices, User Goals/Tasks, Geographies/Regions, User Lifecycle, Behavioral Triggers, Segments, Feature Usage, Risk and Proof, Frameworks) with their named methods, the 5-step method-selection process, what comes out of a method, and where methods work best.

## How to apply

1. **Start with the decision, not the test.** Don't ask "what test should we run?" — ask "what frame would help us understand this work clearly?" The method is a way to organize evidence around a decision.

2. **Confirm the initiative is framed.** Methods can organize evidence but cannot fix a poorly framed problem. If the user need, business goal, audience, or objective is unclear, route back to `glare-focus-initiatives`.

3. **Run the 5-step selection process:**
   - **Name the initiative objective** (increase adoption, reduce friction, improve trust, sharpen positioning, simplify a journey, decide which concept deserves more investment).
   - **Identify the decision** the team needs to make next (which concept, which journey moment, which version, which audience, which competitor gap, which direction).
   - **Look at the data you already have.** Review existing signals, findings, UX metrics, comments, analytics, stakeholder input. The team may already have enough to frame the decision.
   - **Choose the frame that fits the decision.** Issue spans steps → journey frame. Market context matters → competitor frame. Timing matters → timeline frame. Different users respond differently → segment frame. Choosing between ideas → iteration/comparison frame.
   - **Define what gets compared.** Make the comparison explicit — concepts, versions, audiences, journey moments, competitors, lifecycle stages, platforms/devices, features, risks, time periods.

4. **Pick from the 13 frames** and route the user to named methods inside each:
   - **Competitors** — Competitive analysis, Competitor UX benchmark, Reverse impact mapping, Feature comparison matrix, Positioning comparison.
   - **Iterations** — A/B testing, Design test loop, Rapid concept testing, MVP prototype, Variant comparison, Before-and-after testing.
   - **Timeline** — Eisenhower Matrix, MoSCoW, Opportunity Solution Tree, Now/Next/Later, Roadmap sequencing, Impact vs. effort.
   - **Journeys** — Journey mapping, Service blueprint, Funnel review, Drop-off mapping, Touchpoint analysis.
   - **Platforms/Devices** — Device comparison, Cross-platform mapping, Responsive review, Channel comparison, Accessibility device review.
   - **User Goals/Tasks** — Task analysis, Importance and satisfaction framework, JTBD mapping, Goal friction mapping.
   - **Geographies/Regions** — Localization review, Market readiness review, Cultural context mapping, Regional benchmark.
   - **User Lifecycle** — Simple/Lovable/Complete, MVO/MMP/MLP, Lifecycle stage mapping, Adoption path review, Retention moment analysis.
   - **Behavioral Triggers** — EAST Framework, UX impact mapping, Trigger mapping, Habit loop mapping, Nudge analysis.
   - **Segments** — Empathy mapping, JTBD, Segment comparison, Role-based journey review, Cohort signal review.
   - **Feature Usage** — Opportunity scoring, Kano Model, Weighted scoring, Frequency vs. importance matrix.
   - **Risk and Proof** — Four Big Risks, HATS survey, Proof of Concept, Smoke test, Pilot review, Expert review.
   - **Frameworks** — 5Ds, 5W1H, HEART Framework, ICE Scoring, KPI Trees, RICE, SUS Testing, Spotlight Framework, Value vs. Complexity Quadrant, XYZ Hypothesis.

5. **Hand off to `glare-focus-comparing`** once the method has produced data — the next move is placing signals side by side using a shared metric.

## Handoffs

- Reframing the initiative if scope is unclear → `glare-focus-initiatives`
- Placing signals side by side once data is collected → `glare-focus-comparing`
- Turning evidence into a clear next move → `glare-focus-decisions`
- Upstream: clarifying user need or audience → `glare-define`
- Upstream: turning hunches into testable signals → `glare-measure`
- Connecting decisions to business outcomes → `glare-lead`
- The whole Focus flow → `glare-focus`
- The Define → Measure → Focus → Lead chain → `glare-decision-map`
