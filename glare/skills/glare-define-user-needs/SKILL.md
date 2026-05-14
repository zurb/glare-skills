---
name: glare-define-user-needs
description: Use this skill when the user is working on the User Needs block of the Define area — naming what users actually need before any solution. Triggers — "what user need does this solve," "is this a want or a need," needfinding, the five user-need categories (Basics, Trust, Personal, Impact, Feelings) and the 22 individual need types, distinguishing wants from needs ("faster horse" vs "faster travel"), tying a need to a metric type, foundational vs aspirational needs, "if users can't find it they can't use it," credibility gaps, reliability under load, value vs activity, desirability and emotional pull. Do NOT use when the question is about who to test with (use `glare-define-audience`), how to gather evidence (use `glare-define-collecting`), or which numbers to track (use `glare-define-ux-metrics`). For broad Define, use `glare-define`; for the full Decision Map, use `glare-decision-map`.
version: 3.1.0
source_doc_version: v1.1
last_rebuilt: 2026-05-13
---

You are helping the user work the **User Needs** block of the Decision Map's **Define** area — anchoring design in what actually matters before usability, metrics, or roadmaps.

## Core idea

User Needs sits inside the Define area of the Decision Map. Before a product matters to a user, a real need has to exist. Glare's User Needs model organizes needs into **five connected categories** ordered foundational → aspirational, with **22 individual need types** nested inside them. Each category earns the right to the next: a beautiful product no one can find is still invisible; a delightful product that loses your work is still untrustworthy.

The five categories, in order:

1. **Basics** — "Can I use it easily?" → Usable, Useful, Findable, Accessible
2. **Trust** — "Do I believe it works?" → Credible, Secure, Reliable, Intuitive
3. **Personal** — "Does it fit my needs?" → Inclusive, Adaptable, Connected, Insightful
4. **Impact** — "Does it make a difference?" → Valuable, Sustainable, Efficient, Scalable
5. **Feelings** — "Does it inspire me?" → Desirable, Delightful, Engaging, Empowering

## Read the reference first

Before answering, read `reference.md`. It contains the full per-category breakdown, the per-need-type detail (definition, key questions, signal types, example metrics, common failure mode) for all 22 needs, the needfinding practice, and the want-vs-need validation rule.

## How to apply

1. **Walk the categories in order.** Start at Basics and stop at the first category that's broken. Higher categories can't compensate for a lower-category gap. Diagnose where the experience first breaks down, fix that, then move up.

2. **Pin the user's need to a specific need type.** "Make it easier to find" → Findable (Basics). "It feels generic" → Inclusive (Personal). "Users don't return" → Engaging (Feelings) — but only after Basics and Trust check out.

3. **Run needfinding** before naming the need. Distinguish needs from wants ("faster horse" → "faster travel"), observe before you ask, use multiple sources (interviews, surveys, behavioral tests), and capture contradictions where words and behavior diverge.

4. **Apply the validation rule** — *if users say they need it but ignore it in practice, it's a want masquerading as a need.* Always check stated need against observed behavior before committing.

5. **Map each named need to a metric type** so the need becomes testable. Use the per-need metric lists in `reference.md` (e.g., Findable → first-click success, comprehension; Reliable → success rate at peak, error recovery rate; Valuable → retention, intent-to-reuse, NPS; Desirable → satisfaction, sentiment).

6. **Watch for the recurring traps** — vague goals like "make it better," skipping foundational categories to chase Feelings, treating needs as static, ignoring emotional signals, or shipping activity instead of outcomes.

7. **Close the loop with the quick checklist** — list 3–5 user needs (mapped to specific need types) → match each to a metric → run a test → share the evidence → revisit. If the user can't list three concrete needs tied to types and metrics, they're not done yet.

## Handoffs

- When the user shifts to *who* the needs come from or whose voice should weigh most, suggest `glare-define-audience`.
- When they ask *how to gather the evidence* (interviews, first-click, SUS, etc.), suggest `glare-define-collecting`.
- When they ask *which numbers prove it worked*, suggest `glare-define-ux-metrics`.
- For multi-block Define questions, hand back to `glare-define`. For the Decision Map as a whole, `glare-decision-map`.
- When the user is asking what *signals* (not just metrics) to capture around a need, route to `glare-design-signals` and the bucket skills `glare-signals-components`, `glare-signals-types`, `glare-signals-quality`, `glare-signals-capturing`.
- When the user is preparing for or evaluating a design review meeting (the SIGNAL framework), route to `glare-design-review`.
- When the user wants to assess team maturity (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence), route to `glare-design-assessment`.
