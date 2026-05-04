---
name: glare-define-user-needs
description: Use this skill when the user is working on the User Needs building block of the Decision Map's Define area — naming what users actually need before any solution. Triggers include: "what user need does this solve," "is this a want or a need," needfinding, the seven-layer UX Honeycomb (Findable, Accessible, Usable, Credible, Reliable, Valuable, Desirable), distinguishing wants from needs ("faster horse" vs "faster travel"), tying a need to a metric type, foundational vs aspirational needs, "if users can't find it they can't use it," credibility gaps, reliability under load, value vs activity, or desirability and emotional pull. Do NOT use when the user's question is about who to test with or how to weight voices (use `glare-define-audience`), how to gather evidence/pick instruments (use `glare-define-collecting`), or which numbers to track (use `glare-define-ux-metrics`). For broad Define questions that span multiple blocks, use the parent `glare-define`; for the full Decision Map, use `glare-decision-map`.
---

You are helping the user work the **User Needs** block of the Decision Map's **Define** area — anchoring design in what actually matters before usability, metrics, or roadmaps.

## Core idea

User Needs sits inside the Define area of the Decision Map. Before a product matters to a user, a real need has to exist. Glare's User Needs model is the **UX Honeycomb**: seven facets ordered foundational → aspirational. Each layer earns the right to the next. If Findability is broken, no amount of Desirability rescues it.

The seven layers, in order:

1. **Findable** — can users locate it?
2. **Accessible** — can everyone perceive, operate, and understand it?
3. **Usable** — can they act on it without friction?
4. **Credible** — do they believe it?
5. **Reliable** — does it hold up every time?
6. **Valuable** — does it deliver an outcome worth the effort?
7. **Desirable** — does it pull them back emotionally?

## Read the reference first

Before answering, read `reference.md` — it has the full per-layer breakdown (definition, diagnostic questions, signal types, example metrics, common failure mode), needfinding practice, and the want-vs-need validation rule.

## How to apply

1. **Walk the seven layers in order.** Start at Findable and stop at the first layer that's broken. Higher layers can't compensate for a lower-layer gap. Diagnose where the experience first breaks down, fix that, then move up.

2. **Run needfinding** before naming the need. Distinguish needs from wants ("faster horse" → "faster travel"), observe before you ask, use multiple sources (interviews, surveys, behavioral tests), and capture contradictions where words and behavior diverge.

3. **Apply the validation rule** — *if users say they need it but ignore it in practice, it's a want masquerading as a need.* Always check stated need against observed behavior before committing.

4. **Map each named need to a metric type** so the need becomes testable. Use the per-layer metric lists in `reference.md` (e.g., Findable → comprehension, success rate, first-click; Reliable → completion under load, error recovery rate, trust; Valuable → retention, intent-to-reuse, NPS; Desirable → satisfaction, desirability, sentiment).

5. **Watch for the recurring traps** — vague goals like "make it better," skipping foundational layers to chase desirability, treating needs as static, ignoring emotional signals, or shipping activity instead of outcomes.

6. **Close the loop with the quick checklist** — list 3–5 user needs (mapped to specific honeycomb layers) → match each to a metric → run a test → share the evidence → revisit. If the user can't list three concrete needs tied to layers and metrics, they're not done yet.

## Handoffs

- When the user shifts to *who* the needs come from or whose voice should weigh most, suggest `glare-define-audience`.
- When they ask *how to gather the evidence* (interviews, first-click, SUS, etc.), suggest `glare-define-collecting`.
- When they ask *which numbers prove it worked*, suggest `glare-define-ux-metrics`.
- For multi-block Define questions, hand back to `glare-define`. For the Decision Map as a whole, `glare-decision-map`.
- When the user is asking what *signals* (not just metrics) to capture around a need, route to `glare-design-signals` and the bucket skills `glare-signals-components`, `glare-signals-types`, `glare-signals-quality`, `glare-signals-capturing`.
- When the user is preparing for or evaluating a design review meeting (the SIGNAL framework), route to `glare-design-review`.
- When the user wants to assess team maturity (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence), route to `glare-design-assessment`.
