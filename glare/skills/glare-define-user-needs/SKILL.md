---
name: glare-define-user-needs
description: Use this skill when the user is working on the User Needs block of the Define area — naming what users actually need before any solution, OR formatting a completed User Needs output for a specific audience. Triggers — "what user need does this solve," "is this a want or a need," needfinding, the 5 user-need categories (Basics, Trust, Personal, Impact, Feelings) and the 20 individual need types, wants vs needs, tying a need to a metric type, credibility gaps, "Glarify this," format triggers (message/deck/board/script/doc/brief/roadmap/experiment/business case), Understanding Strength (Emerging/Building/Stable), agent operations runtime contract. Do NOT use when the question is about who to test with (use `glare-define-audience`), how to gather evidence (use `glare-define-collecting`), or which numbers to track (use `glare-define-ux-metrics`). For broad Define, use `glare-define`.
version: 3.6.0
source_doc_version: v1.4 (8-doc template — Overview + Techniques + Playbook + References + Decisions + Examples + Formats + Agent Operations)
last_rebuilt: 2026-06-23

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
  - doc_id: 1NtO0POY1yBSyalJUkRbjt16ESjRbVp0t5kFcv3acdQQ
    title: Glare | Define, User Needs, Agent Operations v1.4
    drive_url: https://docs.google.com/document/d/1NtO0POY1yBSyalJUkRbjt16ESjRbVp0t5kFcv3acdQQ/edit
    last_synced: 2026-05-22
  - doc_id: 14fwcm9Qhpi64TaC3bKR4R3D7sNgmkfqa558EUpJ_a5c
    title: Glare | Define, User Needs, Formats v1.4
    drive_url: https://docs.google.com/document/d/14fwcm9Qhpi64TaC3bKR4R3D7sNgmkfqa558EUpJ_a5c/edit
    last_synced: 2026-06-23
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

## Files to read

This skill ships three files alongside `SKILL.md`. Read them in this order:

1. **`agent-operations.md` first.** Runtime contract for **producing** the artifact — output schema, confidence labels, input minimums, transition rules, escalation triggers, guardrails. Governs how a User Need output is *made*.
2. **`formats.md` — only when the user is packaging an existing output for delivery.** Runtime contract for **Glarifying** — the 4-step resolution sequence (Understanding Strength → Purpose → Audience → Format), the 9 format types, compatibility matrices, and a second layer of Agent Operations governing formatting. Triggered by requests like "Glarify this," "format this as," "turn this into a slide," or naming any specific format.
3. **`reference.md` third.** Six practitioner sections — Overview, Techniques, Playbook, References, Decisions, Examples — plus the When-to-use and Failure-modes layers. The content the practitioner is working *with*.

The highest-leverage rules from both AO layers are duplicated into "Operating rules" below so they bind even without consulting the files.

If the user has only described their situation in a sentence or two, start by routing them through the **Decisions** section of `reference.md` — match their situation to one of the 8 entries before doing anything else.

## Operating rules

These are the binding rules from `agent-operations.md`. They apply on every invocation regardless of whether the full file is read.

### Required inputs — what's needed before classifying

| To produce... | Need at minimum |
|---|---|
| A Hunch | ≥2 distinct input types; ≥1 behavioral signal; workflow context |
| An emerging need | ≥3 distinct input types; repeated behavioral evidence across users/sessions; ≥1 measurable signal |
| A validated pattern | Cross-source reinforcement (behavioral + attitudinal + performance); measurable recurrence over time; competing explanations considered |

If minimums are not met, **route to Collecting** instead of classifying.

### Output Contract — the Primary User Need Output schema

Every user-need output uses these 10 fields, in this order:

1. **Category** (one of the five layers)
2. **User Need** (one of the 20)
3. **Summary**
4. **Evidence**
5. **User Behaviors**
6. **User Roadblocks**
7. **Why It Matters**
8. **Why It Fails**
9. **Suggestions**
10. **UX Metrics**

The full content for each field, plus the short-form summary format and the Multiple User Needs summary table, are specified in the Playbook section of `reference.md`.

### Confidence labels — required vocabulary

Every output carries one of these six labels. Do not invent alternatives.

- **Weak signal** — insufficient evidence; route to Collecting
- **Possible pattern** — early directional signal from 1-2 inputs; flag as speculative
- **Hunch** — repeated but incomplete evidence; name the need, state what would confirm/refute
- **Emerging need** — consistent multi-source evidence; produce structured output, flag remaining gaps
- **Recurring signal** — measurable recurring behavior; produce full output, route to Signals or Metrics
- **Validated pattern** — cross-source reinforcement with measurable recurrence; produce full output, route to Experiments or Reviews

Do not upgrade confidence to produce a cleaner result.

### Prohibited output behaviors

- Recommending solutions before the Hunch is validated
- Inferring emotional intent without behavioral evidence
- Flattening conflicting signals into a single clean narrative
- Hiding ambiguity to produce a more confident-sounding output
- Overstating confidence relative to the evidence available
- Collapsing multiple distinct needs into one category unnecessarily

### Escalation — when to stop and surface to a human

Escalate (don't auto-resolve) when:

- Evidence remains contradictory after Collecting
- Confidence stays below Hunch threshold after ≥2 input types are present
- Multiple need interpretations remain equally plausible
- Business impact is high and evidence quality is weak
- The only available input is a stakeholder assumption

Escalation outputs must preserve uncertainty visibly, name the unresolved interpretations, identify what evidence is missing, and recommend next Collecting steps — not default to a direction.

### Formats (Glarify) — the second runtime contract

When the user has a completed User Need output and asks to share it, present it, or format it, the Formats layer applies. Resolve four variables **in order** before producing any formatted output:

| Step | Variable | Values |
|---|---|---|
| 1 | **Understanding Strength** | Emerging (early signals) · Building (multiple sources) · Stable (cross-source confirmed). Governs tone and which purposes the output can honestly serve. |
| 2 | **Purpose** | Inform · Align · Decide · Prioritize · Validate · Hand Off |
| 3 | **Audience (reader)** | Product team · Designer · Researcher · Product leader · Executive · Cross-functional |
| 4 | **Format** | Messages · Decks · Boards · Scripts · Docs · Brief · Roadmap · Experiment · Business Case |

**Every formatted output must include a visible Understanding Strength signal phrase early (first sentence or labeled field).** Emerging: "Early signals suggest..." · Building: "Evidence is building across..." · Stable: "This need is well-supported..." Never bury or omit.

**Prohibited on Formats:** presenting Emerging as Stable · omitting the signal phrase · using Brief/Business Case for Emerging without framing the ask as further investigation · formatting Multiple Needs into Messages or Boards without splitting · adding evidence not in the source output.

Full compatibility matrices (output type × format, understanding × purpose) and per-format structural rules live in `formats.md`.

## How to apply

1. **Match the situation first.** Use the Decisions section of `reference.md` to pick where the work actually starts. The eight situations cover the most common stuck-points: can't agree on what signals mean, can't locate the problem, reacting to feature requests, need statement feels weak, multiple needs at once, stakeholder alignment, measurement, and AI-Skill setup.

2. **Check inputs against the minimums above** before classifying. If thin, route to Collecting and say so explicitly.

3. **Walk the layers in order when diagnosing.** Start at Basics and stop at the first layer that's broken. Higher layers can't compensate for a lower-layer gap.

4. **Pin the user's situation to a specific need type.** "Make it easier to find" → Findable (Basics). "It feels generic" → Inclusive (Personal). "Users don't return" → Engaging (Feelings) — but only after Basics and Trust check out.

5. **Run needfinding before naming the need.** Distinguish needs from wants ("faster horse" → "faster travel"), observe before you ask, use multiple sources, capture contradictions.

6. **Apply the want-vs-need validation rule** — *if users say they need it but ignore it in practice, it's a want masquerading as a need.* Check stated need against observed behavior before committing.

7. **Check the need statement against the strong/weak criteria** in the Techniques section of `reference.md`.

8. **When multiple needs emerge, apply the three prioritization questions** from the Playbook: which is blocking the others, which has the strongest evidence, which connects most directly to a measurable business outcome.

9. **Use the worked examples in `reference.md`** to calibrate output quality. The 5 examples model what a properly framed Hunch looks like *before* measurement exists. The Near-Miss shows the common failure: treating two interview quotes as confirmation and jumping to redesign.

10. **Produce the output using the 10-field schema above**, label the confidence state, and route to the next block per the Transition Logic table in `agent-operations.md`.

## What's new in v3.4.0

- **Agent Operations** added as a 7th source doc and split out into its own file (`agent-operations.md`). The other six practitioner sections remain in `reference.md`.
- **Operating rules section** added to this file so the binding rules (input minimums, output schema, confidence labels, prohibited behaviors, escalation triggers) bind on every invocation regardless of whether `agent-operations.md` is read.
- **Files to read** instruction updated to load `agent-operations.md` before `reference.md`.

Earlier v1.4 changes (carried over from v3.3.0): Decisions added as a router for the block; Examples added with 5 worked examples + Pattern Library + Near-Miss; canonical 20-need count locked in (was incorrectly 22 in older revisions); strong-vs-weak need-statement characteristics formalized; three-question prioritization rule added.

## Handoffs

- When the user shifts to *who* the needs come from or whose voice should weigh most, suggest `glare-define-audience`.
- When they ask *how to gather the evidence* (interviews, first-click, SUS, etc.), suggest `glare-define-collecting`.
- When they ask *which numbers prove it worked*, suggest `glare-define-ux-metrics`.
- For multi-block Define questions, hand back to `glare-define`. For the Decision Map as a whole, `glare-decision-map`.
- When the user is asking what *signals* (not just metrics) to capture around a need, route to `glare-design-signals` and the bucket skills `glare-signals-components`, `glare-signals-types`, `glare-signals-quality`, `glare-signals-capturing`.
- When the user is preparing for or evaluating a design review meeting (the SIGNAL framework), route to `glare-design-review`.
- When the user wants to assess team maturity (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence), route to `glare-design-assessment`.
- When a Hunch is formed and ready to test in Helio (or another tool), route to `glare-measure-hunches`, then `glare-measure-questioning`, then `glare-measure-findings`.
