---
name: glare-ux-metrics-mapping
description: Use this skill when the user is connecting UX metrics to business outcomes — phrases like "mapping design impact," "design impact," "connect UX to business," "UX metrics to business outcomes," "Situation — Intent — Outcomes — Results," "design impact creates pull," "leading vs lagging indicators," "trust may weaken before retention drops," "AI hesitation before adoption weakens," "translate user needs into business outcomes," "we improved UX but leadership doesn't see it," "we keep getting watered down in stakeholder review," or asks how UX metrics influence adoption, retention, conversion, support reduction, or operational efficiency. Also use when preparing a leadership readout that needs the UX-to-business chain. Do NOT use for the broader UX Metrics framework (use `glare-ux-metrics`), the technical Chain of Proof (use `glare-lead-mapping`), or proving design impact at the org-readiness level (use `glare-proving-design-impact`).
version: 2.2.0
source_doc_version: v1.32
last_rebuilt: 2026-05-10
---

You are helping the user **map design impact** through UX metrics — connecting user behavior, emotional signals, workflow performance, and operational outcomes into one clearer system.

## Core idea

Design work often struggles to connect clearly to business impact. Product teams may improve onboarding, usability, and navigation, but leadership still asks — did it improve the business? Mapping design impact uses UX metrics as the *translation layer* between user behavior and business signals. Instead of design living separately from product or business conversations, teams begin connecting user behavior, emotional signals, workflow performance, operational outcomes, and business results into one system. As AI increases product velocity, this matters more — teams launch more experiments and AI-assisted features than they can consistently evaluate.

## The four-stage chain (v1.32)

Design impact rarely comes from one isolated screen or one launch moment. It builds through layers of leverage across workflows, systems, and decisions over time. Teams evaluate impact across four connected stages, aligned with the four facets of the Decision Map:

- **Situation (Define)** — understand the situation surrounding the work. What triggered the problem, where users struggle, what friction exists, what users are trying to achieve. UX metrics define what signals are worth measuring inside the workflow.
- **Intent (Measure)** — shape user behavior intentionally through onboarding, navigation, workflows, AI recommendations, interaction design. UX metrics evaluate whether the design intent is actually working — confidence, comprehension, usability, effort, trust, hesitation.
- **Outcomes (Focus)** — compare outcomes across the experience. The focus shifts from producing outputs toward identifying which workflows actually create stronger user outcomes. UX metrics enable consistent comparison across competing workflows.
- **Results (Lead)** — connect workflow improvements to larger business outcomes — adoption, retention, conversion, support reduction, operational efficiency. Design becomes less about isolated screens and more about shaping product direction, organizational alignment, and long-term business momentum.

As teams move from Situation to Results, the number of users involved decreases but the business stakes get higher.

## Strong design impact creates pull

Many teams try to *push* design value into the organization after the work is complete. Stakeholder reviews become difficult because business goals are fuzzy, success was never clearly measured, workflow friction was never made visible, and teams debate opinions instead of signals. Strong ideas slowly get watered down. Stronger teams work differently — they begin with a business moment (onboarding, activation, conversion, workflow efficiency, trust in AI) then use UX metrics to expose hesitation, friction, weak comprehension, rising effort, and trust gaps. The friction becomes measurable, so teams can align around visible evidence instead of assumptions. The design decisions are *pulled* from visible workflow problems instead of pushed into the org afterward.

## Leading indicators vs lagging indicators

Business metrics are often **lagging indicators** — they appear after workflows are released, onboarding is already struggling, users have already abandoned, support requests have increased, or adoption has slowed. By the time retention drops, the underlying experience problems may already be embedded across the system. UX metrics often act as **leading indicators** — they identify earlier signals like confusion, hesitation, weak confidence, frustration, rising effort, workflow fatigue. This gives teams a chance to improve workflows before larger downstream problems spread.

## Read the reference first

Before answering, read `reference.md` — it carries the full v1.32 Mapping Design Impact content, including the four-stage chain in detail, the Design Signals as bridge framing, the design-needs-its-own-signals argument, the leading vs lagging pattern, and the chain user-need → design KPI → product KPI → business KPI.

## How to apply

1. **Lead with Situation, not solution.** Many teams jump to interfaces, metrics, AI workflows, or experiments without understanding the situation. Without context, design impact rarely happens. Start by understanding what triggered the problem, what users are trying to achieve, what friction exists, and what progress or success actually looks like.

2. **Use the four stages as a chain.** Walk Situation → Intent → Outcomes → Results explicitly. Each stage has different UX metrics — Situation needs metrics that name what is worth measuring; Intent needs metrics that evaluate confidence/comprehension/effort/trust; Outcomes needs metrics that compare workflows; Results needs metrics that connect to adoption/retention/conversion/support/efficiency.

3. **Convert metrics into pull.** When the user is preparing for stakeholder review, do not lead with the design solution — lead with the measurable workflow problem. Hesitation at step 3 of onboarding (Behavioral) + low confidence (Attitudinal) + rising support tickets (Performance) creates pull for a redesign far better than a presentation of new screens.

4. **Use leading-indicator language deliberately.** Trust may weaken before retention drops. Onboarding confusion may appear before conversion declines. Rising effort may slow adoption over time. AI hesitation may reduce long-term usage confidence. Naming UX metrics as leading indicators is the strongest argument for measuring earlier.

5. **Tie to specific business outcomes, not abstractions.** "Better UX" lands less than "comprehension may influence onboarding completion → trust may influence long-term retention → workflow effort may influence operational efficiency → discoverability may influence adoption." Use the canonical chains from the v1.32 source.

## Handoffs

- For the broader UX Metrics framework and the four metric TYPES, route to `glare-ux-metrics`.
- For the technical Chain of Proof (User Need → Design KPI → Product KPI → Business KPI → Goal), route to `glare-lead-mapping`.
- For proving design impact at the org-readiness level (with leadership stories, not just metrics), route to `glare-proving-design-impact`.
- For applying UX metrics inside reviews, prioritization, comparison, launch readiness, AI workflow evaluation, route to `glare-ux-metrics-applying`.
- For combining metrics into a stack to expose friction, route to `glare-ux-metrics-stack`.
- For Design Signals as the bridge between metrics and business impact, route to `glare-design-signals` and `glare-signals-components`.
- For Define-stage user-need naming, route to `glare-define-user-needs`.
- For business goals and pressures (Growth, Retention, UX, Efficiency, Operations), route to `glare-lead-business-goals`.
- For the Decision Map as a whole, route to `glare-decision-map`.
