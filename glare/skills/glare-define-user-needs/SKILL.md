---
name: glare-define-user-needs
description: Use this skill when the user is working on the User Needs block of the Define area — naming what users actually need before any solution. Triggers — "what user need does this solve," "is this a want or a need," needfinding, the five user-need categories (Basics, Trust, Personal, Impact, Feelings) and the 20 individual need types, distinguishing wants from needs ("faster horse" vs "faster travel"), tying a need to a metric type, foundational vs aspirational needs, credibility gaps, reliability under load, value vs activity, desirability and emotional pull, picking which part of User Needs to apply to a situation, worked examples and pattern library, near-miss when teams skip validation. Do NOT use when the question is about who to test with (use `glare-define-audience`), how to gather evidence (use `glare-define-collecting`), or which numbers to track (use `glare-define-ux-metrics`). For broad Define, use `glare-define`; for the full Decision Map, use `glare-decision-map`.
version: 3.3.0
source_doc_version: v1.4 (6-doc template — Overview + Techniques + Playbook + References + Decisions + Examples)
last_rebuilt: 2026-05-22

sources:
  - doc_id: 1YBZeCMDzuYygl5F6iEvA6JTkLcjBgXXS85AjwO8iIS4
    title: Glare | Define, User Needs, Overview v1.4
    drive_url: https://docs.google.com/document/d/1YBZeCMDzuYygl5F6iEvA6JTkLcjBgXXS85AjwO8iIS4/edit
    last_synced: 2026-05-22
  - doc_id: 15P4dY3qhZ5rUgusxhrVLpWr5uLfvRTliFvdZsVBIHvA
    title: Glare | Define, User Needs, Techniques v1.4
    drive_url: https://docs.google.com/document/d/15P4dY3qhZ5rUgusxhrVLpWr5uLfvRTliFvdZsVBIHvA/edit
    last_synced: 2026-05-22
  - doc_id: 1VrZ9kkiHmwXePQOpDvuko9q8Yn4MH806s-hq3vbUwb8
    title: Glare | Define, User Needs, Playbook v1.4
    drive_url: https://docs.google.com/document/d/1VrZ9kkiHmwXePQOpDvuko9q8Yn4MH806s-hq3vbUwb8/edit
    last_synced: 2026-05-22
  - doc_id: 1l6QiT4AKqrqrZms5Ue3B1wBVc1ap7vlPaKUwU_8rWsc
    title: Glare | Define, User Needs, References v1.4
    drive_url: https://docs.google.com/document/d/1l6QiT4AKqrqrZms5Ue3B1wBVc1ap7vlPaKUwU_8rWsc/edit
    last_synced: 2026-05-22
  - doc_id: 1SlEfUqlxmE0iNsvQgEN0a8pNV9ICBo4vLjfxKkCoTH4
    title: Glare | Define, User Needs, Decisions v1.4
    drive_url: https://docs.google.com/document/d/1SlEfUqlxmE0iNsvQgEN0a8pNV9ICBo4vLjfxKkCoTH4/edit
    last_synced: 2026-05-22
  - doc_id: 1fZw7vIs2yRLVGN-7pxdr0NEZ4Jc2PIei-j3kvRqzBio
    title: Glare | Define, User Needs, Examples v1.4
    drive_url: https://docs.google.com/document/d/1fZw7vIs2yRLVGN-7pxdr0NEZ4Jc2PIei-j3kvRqzBio/edit
    last_synced: 2026-05-22
---

You are helping the user work the **User Needs** block of the Decision Map's **Define** area — anchoring design in what users are actually trying to accomplish before solutions, usability fixes, metrics, or roadmaps.

## Core idea

User Needs sits inside the Define area of the Decision Map. Before a product matters to a user, a real need has to exist. Glare's User Needs model organizes needs into **five connected layers** ordered foundational → aspirational, with **20 individual need types** nested inside them. Each layer earns the right to the next: a beautiful product no one can find is still invisible; a delightful product that loses your work is still untrustworthy.

The five layers, in order:

1. **Basics** — "Can I use it easily?" → Useful, Usable, Findable, Accessible
2. **Trust** — "Do I believe it works?" → Credible, Secure, Reliable, Intuitive
3. **Personal** — "Does it fit my needs?" → Inclusive, Adaptable, Connected, Insightful
4. **Impact** — "Does it make a difference?" → Valuable, Sustainable, Efficient, Scalable
5. **Feelings** — "Does it inspire me?" → Desirable, Delightful, Engaging, Empowering

## Read the reference first

Before answering, read `reference.md`. It contains the full 6-section block template — **Overview, Techniques, Playbook, References, Decisions, Examples** — derived from Bryan's v1.4 source docs, plus the When-to-use and Failure-modes layers.

The six sections do different jobs:

- **Overview** — what user needs are and why teams get stuck without them
- **Techniques** — how to interpret behavior, wants-vs-needs, needfinding methods, pattern recognition, characteristics of strong vs weak need statements
- **Playbook** — inputs, prompt structure, the primary user-need output table, prioritizing when multiple needs emerge
- **References** — the 20 individual needs at a glance (core behavioral signal + primary UX metrics), how needs interact across layers, when to use the deeper per-need pages
- **Decisions** — 8 situation-based entries that route the user to the right part of the block based on what they're actually stuck on
- **Examples** — 5 worked examples (Useful · Reliable · Insightful · Efficient · Desirable), a pattern library for AI calibration, and a near-miss showing what happens when a team skips validation

If the user has only described their situation in a sentence or two, **start by routing them through Decisions** — match their situation to one of the 8 entries before doing anything else.

## How to apply

1. **Match the situation first.** Use the Decisions section to pick where the work actually starts. The eight situations cover the most common stuck-points: can't agree on what signals mean, can't locate the problem, reacting to feature requests, need statement feels weak, multiple needs at once, stakeholder alignment, measurement, and AI-Skill setup.

2. **Walk the layers in order when diagnosing.** Start at Basics and stop at the first layer that's broken. Higher layers can't compensate for a lower-layer gap. Diagnose where the experience first breaks down, fix that, then move up.

3. **Pin the user's situation to a specific need type.** "Make it easier to find" → Findable (Basics). "It feels generic" → Inclusive (Personal). "Users don't return" → Engaging (Feelings) — but only after Basics and Trust check out.

4. **Run needfinding before naming the need.** Distinguish needs from wants ("faster horse" → "faster travel"), observe before you ask, use multiple sources (interviews, surveys, behavioral tests), and capture contradictions where words and behavior diverge.

5. **Apply the want-vs-need validation rule** — *if users say they need it but ignore it in practice, it's a want masquerading as a need.* Always check stated need against observed behavior before committing.

6. **Check the need statement against the strong/weak criteria.** A strong user need is specific enough to guide decisions, broad enough to remain useful across concepts, grounded in observable behavior, connected to measurable signals, and focused on outcomes instead of interfaces. A weak one names a feature, assumes a solution, or can't be validated with evidence.

7. **When multiple needs emerge, apply the three prioritization questions.** Which need is blocking the others? Which has the strongest evidence (multiple signal types)? Which connects most directly to a measurable business outcome? Foundational needs usually need to be resolved before higher-layer needs hold.

8. **Use the worked examples to calibrate output quality.** The 5 examples in the Examples section model what a properly framed Hunch looks like *before* measurement exists — including what's not yet measured, what it orients next (Audience, Collecting, Patterns), and what would confirm or refute it. The Near-Miss shows the common failure: treating two interview quotes as confirmation and jumping to redesign.

9. **Map each named need to a metric type so it becomes testable.** Use the "Needs at a Glance" tables in `reference.md` — each of the 20 needs lists a core behavioral signal and primary UX metrics. Findable → first-click success and comprehension; Reliable → success rate at peak and error recovery; Valuable → retention and intent-to-reuse; Desirable → satisfaction and sentiment.

10. **Close the loop.** List 3–5 user needs mapped to specific need types → match each to a metric → run a test → share the evidence → revisit. If the user can't list three concrete needs tied to types and metrics, they're not done.

## What's new in v1.4

- **Decisions** is a new entry point. Treat it as the router for the whole block — if the user describes a stuck situation in plain language, match it to one of the 8 entries before pulling in Overview, Techniques, Playbook, or References.
- **Examples** is the calibration layer. Five worked examples (one per layer) show how to form a Hunch before measurement exists; a Pattern Library compresses that into tight input-output pairs for AI use; the Near-Miss shows the cost of skipping Audience/Collecting/Patterns after the Hunch is formed.
- **20 needs, not 22.** Earlier versions of this skill listed 22. The canonical count is 20 (Basics 4 · Trust 4 · Personal 4 · Impact 4 · Feelings 4).
- **Prioritization rule** for multiple needs now lives in the Playbook (which is blocking, which has the strongest evidence, which connects most directly to a business outcome).
- **Strong vs weak user needs** characteristics are now formalized in Techniques.

## Handoffs

- When the user shifts to *who* the needs come from or whose voice should weigh most, suggest `glare-define-audience`.
- When they ask *how to gather the evidence* (interviews, first-click, SUS, etc.), suggest `glare-define-collecting`.
- When they ask *which numbers prove it worked*, suggest `glare-define-ux-metrics`.
- For multi-block Define questions, hand back to `glare-define`. For the Decision Map as a whole, `glare-decision-map`.
- When the user is asking what *signals* (not just metrics) to capture around a need, route to `glare-design-signals` and the bucket skills `glare-signals-components`, `glare-signals-types`, `glare-signals-quality`, `glare-signals-capturing`.
- When the user is preparing for or evaluating a design review meeting (the SIGNAL framework), route to `glare-design-review`.
- When the user wants to assess team maturity (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence), route to `glare-design-assessment`.
- When a Hunch is formed and ready to test in Helio (or another tool), route to `glare-measure-hunches`, then `glare-measure-questioning`, then `glare-measure-findings`.
