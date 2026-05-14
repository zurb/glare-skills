---
name: glare-ux-metrics-applying
description: Use this skill when the user is putting UX metrics to work inside real product moments — phrases like "applying UX metrics," "using UX metrics in product reviews," "UX metrics in prioritization," "UX metrics for concept comparison," "launch readiness," "UX metrics for AI workflow evaluation," "UX metrics in design critiques," "shared language across teams," "decision support," "this feels confusing," "I don't think users will understand this," "I like the other direction better," "we keep validating too late," "evaluate workflows earlier," "ground reviews in stronger evaluation," "compare onboarding flows side by side," or asks how UX metrics change reviews, prioritization, AI evaluation, or alignment. Also use when the user wants the eight operational use cases for UX metrics. Do NOT use for the broader framework (use `glare-ux-metrics`), what a UX metric IS structurally (use `glare-ux-metrics-what-is`), or stacking specific metrics together (use `glare-ux-metrics-stack`).
version: 3.1.0
source_doc_version: v1.32
last_rebuilt: 2026-05-13
---

You are helping the user **apply UX metrics inside real product moments** — reviews, prioritization, comparison, launch readiness, AI workflow evaluation, and decision support.

## Core idea

UX metrics become most valuable when teams apply them during real product decisions. Most organizations already collect large amounts of data; the challenge is understanding what signals actually matter while workflows, features, and product directions are still evolving. UX metrics are used throughout product and design work in Glare to help teams evaluate ideas, compare workflows, expose friction, and guide decisions while the work is still evolving. Instead of waiting for analytics months later, teams begin understanding user behavior while concepts and product directions are still taking shape.

## The eight operational use cases (v1.32)

Teams apply UX metrics across eight common operational areas:

1. **Product reviews** — instead of "this feels confusing" / "I like the other direction," reviews evaluate comprehension, confidence, discoverability, trust, usability, and friction patterns together.
2. **Prioritization** — instead of reacting to stakeholder pressure, teams identify where users struggle most, where confidence weakens, and which workflows create the largest friction.
3. **Concept comparison** — instead of debating screenshots, teams compare trust, usability, comprehension, confidence, hesitation, completion, effort across competing directions.
4. **Launch readiness** — onboarding confusion appears before abandonment rises; AI hesitation appears before adoption weakens; trust gaps appear before retention declines. Earlier visibility changes launch conversations.
5. **AI workflow evaluation** — measure trust, comprehension, confidence, recovery behavior, effort, hesitation alongside generation speed, activity, and engagement so teams understand whether AI is actually improving the experience.
6. **UX Metric Stacks** — combine 3-7 metrics so behavioral, attitudinal, and performance signals interact together (Confusion Trap, Friction Wall, Trust Gap, Commitment Check). Hand off to `glare-ux-metrics-stack`.
7. **Shared language** — instead of engineering optimizing for speed, product for roadmap, leadership for goals, design for usability, research for validation — UX metrics create one shared language across functions.
8. **Decision support** — UX metrics don't replace intuition or product thinking; they strengthen decisions with clearer signals. The goal is not perfect measurement but enough clarity to move forward with greater confidence.

## Read the reference first

Before answering, read `reference.md` — it carries the full v1.32 Applying UX Metrics content, all eight use cases in detail with the canonical product-team examples (the "this feels confusing" review pattern, the credit-score example, the AI-recommendation activity-vs-trust pattern, the cross-functional optimization example).

## How to apply

1. **Diagnose the moment.** Reviews? Prioritization? Concept comparison? Launch readiness? AI eval? The use case shapes which metrics matter and which sub-skill carries the load. Use the eight-use-case map to route.

2. **Reframe the conversation when reviews drift.** When a stakeholder review becomes "this feels confusing" / "I don't think users will understand this" / "I like the other direction better," the move is to ground the next round in comprehension, confidence, discoverability, trust, usability, and friction signals. Reactions are normal; they rarely create enough clarity to guide decisions well.

3. **Use UX metrics for tradeoff prioritization.** One onboarding may complete faster while another creates stronger confidence and lower hesitation. One AI workflow may increase engagement while another reduces effort and confusion. The metrics help teams understand which tradeoffs actually matter for the experience — not just react to the loudest opinions.

4. **Push for earlier validation, not more.** Teams over-validate at launch and under-validate at concept. Use Helio to capture attitudinal and behavioral metrics as predictive/proxy indicators while concepts are still cheap to change.

5. **Surface AI-specific failure modes.** AI systems often optimize for generation speed, activity, workflow automation, engagement. Pair those with measures of trust, comprehension, confidence, recovery behavior, effort, hesitation. A workflow may *look* successful (fast AI completion, heavy interaction) while users actually distrust it, hesitate, lose comprehension, or quietly stop relying on it.

6. **End with the shared-language argument.** When teams from different functions cannot align, the underlying problem is usually that each is measuring different things. UX metrics give engineering, product, design, research, and leadership a shared vocabulary for what good looks like.

## Handoffs

- For the broader UX Metrics framework, route to `glare-ux-metrics`.
- For combining 3-7 metrics into a Design Stack or Research Stack, route to `glare-ux-metrics-stack`.
- For the four parts of any UX metric (the structural anatomy), route to `glare-ux-metrics-what-is`.
- For Define-stage metric picking on a specific decision, route to `glare-define-ux-metrics`.
- For mapping design impact through Situation → Intent → Outcomes → Results, route to `glare-ux-metrics-mapping`.
- For grounding a design review in evidence (the G in SIGNAL), route to `glare-review-ground` and the broader `glare-design-review`.
- For comparing competing directions side by side using metrics, route to `glare-focus-comparing`.
- For making the decision call after comparison, route to `glare-focus-decisions`.
- For the Initiatives → Findings → Decisions → Outcomes leadership loop, route to `glare-lead-results`.
- For Design Signals as the layer that turns these applied metrics into direction, route to `glare-design-signals`.
