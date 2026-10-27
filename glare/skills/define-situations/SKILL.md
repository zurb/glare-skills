---
name: define-situations
description: Use this skill when the user is interpreting collected signals to identify recurring conditions — the new 4th block of Define that replaces the archived Patterns block. Triggers — "I have signals but can't see a pattern," "what does this drop-off mean," "are these signals telling the same story," the four lenses (By Type, By Time, By Stage, By Engagement), Observe → Interpret → Name cadence, the 9 named situation types (Comprehension breakdown, Trust gap, Effort mismatch, Habit formation gap, Decision loop, Organizational blind spot, etc.), four-part situation structure (trigger/goal/friction/success), Primary Situation Output, situation strength checklist, JTBD vs situations, agent operations runtime contract. Do NOT use when naming the underlying need (use `glare:define-user-needs`), defining who data comes from (use `glare:define-audience`), or gathering evidence (use `glare:define-collecting`). For broad Define, use `glare:define`. Replaces `glare:define-patterns`.
version: 1.1.0
source_doc_version: v1.0/v1.1 (7-doc template — Overview + Techniques + Playbook + References + Decisions + Examples + Agent Operations)
last_rebuilt: 2026-05-26

sources:
  - doc_id: 1nWSOndBCKFkKafk1bZGA6Q-w__7EM1SQK_TJKOj4TOw
    title: Glare | Define, Situations, Overview v1.0/v1.1
    drive_url: https://docs.google.com/document/d/1nWSOndBCKFkKafk1bZGA6Q-w__7EM1SQK_TJKOj4TOw/edit
    last_synced: 2026-05-26
  - doc_id: 1r3Jm5VGxd_CsQePq8uxUp3j0NatUmqv5wlEhm0g0Dfc
    title: Glare | Define, Situations, Techniques v1.1
    drive_url: https://docs.google.com/document/d/1r3Jm5VGxd_CsQePq8uxUp3j0NatUmqv5wlEhm0g0Dfc/edit
    last_synced: 2026-05-26
  - doc_id: 1CBrqIA3Cw0qtWkATZn7358MOrKR72Vzjs5KoTBWqp60
    title: Glare | Define, Situations, Playbook v1.1
    drive_url: https://docs.google.com/document/d/1CBrqIA3Cw0qtWkATZn7358MOrKR72Vzjs5KoTBWqp60/edit
    last_synced: 2026-05-26
  - doc_id: 1bMrKYQST1X3OlxtORMcrVZI0y1UNGydrtifedCSIH6c
    title: Glare | Define, Situations, References v1.0
    drive_url: https://docs.google.com/document/d/1bMrKYQST1X3OlxtORMcrVZI0y1UNGydrtifedCSIH6c/edit
    last_synced: 2026-05-26
  - doc_id: 1vGYahVHTqOyjMJM_9ajIeEqHvJTzy2cCKdkdWAmFF70
    title: Glare | Define, Situations, Decisions v1.0
    drive_url: https://docs.google.com/document/d/1vGYahVHTqOyjMJM_9ajIeEqHvJTzy2cCKdkdWAmFF70/edit
    last_synced: 2026-05-26
  - doc_id: 1gJc_GGlM1__TjpQmPfRDNsW8dN3Nr3Ni9ylXIQYboc8
    title: Glare | Define, Situations, Examples v1.0
    drive_url: https://docs.google.com/document/d/1gJc_GGlM1__TjpQmPfRDNsW8dN3Nr3Ni9ylXIQYboc8/edit
    last_synced: 2026-05-26
  - doc_id: 13amawUhlHjLuO6XEBGDenzVCIqn-UE5DDuIUIiQ0DF4
    title: Glare | Define, Situations, Agent Operations v1.1
    drive_url: https://docs.google.com/document/d/13amawUhlHjLuO6XEBGDenzVCIqn-UE5DDuIUIiQ0DF4/edit
    last_synced: 2026-05-26
---

You are helping the user work the **Situations** block of the Decision Map's **Define** area — the new 4th block of Define, where recurring conditions become visible across the signals collected in User Needs, Audience, and Collecting. **Situations replaces the archived Patterns block.**

## Core idea

Most teams collect signals. Few understand the conditions that created them. A metric tells you what happened. A situation tells you what was happening around the user when it happened, what they were trying to accomplish, what stood in their way, and why the same breakdown keeps showing up across different sessions, audiences, and product areas.

A situation has **four parts**: trigger, what users are trying to do, what stands in their way, what success means. When the same four-part pattern shows up repeatedly across different users and sessions, a situation has emerged. **One data point is an observation. A recurring situation is a design signal.**

Situations sits after User Needs, Audience, and Collecting. It is where Define closes — the block that turns isolated signals into stable, shared context Measure can test against.

## Files to read

This skill ships two files alongside `SKILL.md`. Read in this order:

1. **`agent-operations.md` first.** Runtime contract for working with Situations — required inputs minimums for observation / named situation / validated situation, the 11-field Primary Situation Output schema, 5-state confidence model, routing logic, escalation triggers, guardrails. Operating instructions, not reference content. The highest-leverage rules are duplicated into "Operating rules" below.
2. **`reference.md` second.** Six practitioner sections — Overview, Techniques, Playbook, References, Decisions, Examples — plus When-to-use and Failure-modes. Read for the four lenses, the Observe → Interpret → Name cadence, the 9 named situation types, the signal-to-situation mapping, the situations-by-product-context catalog, the situation strength checklist, and the 4 worked Examples.

If the user has only described their situation in a sentence or two, start by routing them through the **Decisions** section of `reference.md` — match their situation to one of the 8 entries.

## Operating rules

Binding rules from `agent-operations.md`. They apply on every invocation regardless of whether the full file is read.

### Required inputs — what's needed before naming a situation

| To produce... | Need at minimum |
|---|---|
| **An observation** | ≥2 distinct input types; ≥1 behavioral signal; workflow context |
| **A named situation** | Signals from ≥2 sources; convergence across **≥2 of the 4 lenses**; condition appears across more than one user/session/audience segment; all 4 situation parts identifiable (trigger / goal / friction / success) |
| **A validated situation** | Cross-source reinforcement across behavioral + attitudinal + performance; lens convergence across **≥3 of the 4 lenses**; consistent across ≥2 audience segments; competing explanations considered |

If minimums are not met, **route to Collecting** before attempting to name a situation.

### Output Contract — Primary Situation Output schema

Every situation output uses these 11 fields. The Skill is not permitted to produce free-form summaries that omit required fields.

1. **Situation Name**
2. **Summary**
3. **Trigger** — condition that sets the situation in motion
4. **What users are trying to do**
5. **What stands in their way**
6. **What success means here**
7. **Evidence** — converging signals across lenses and sources
8. **Audience** — which segments the situation appears in
9. **Why it matters** — operational, user, or business impact
10. **Lenses applied** — which of the 4 surfaced the situation and where they converged
11. **UX Metrics** — for validating whether the situation is improving over time

### Confidence states — required vocabulary

Every output carries one of these five labels.

- **Weak signal** — insufficient evidence; route to Collecting
- **Possible condition** — early directional signal from one lens or one source; note the direction, flag as observation
- **Emerging situation** — two lenses pointing to the same condition across ≥2 sources; draft a statement, flag gaps
- **Named situation** — multi-source multi-lens evidence with all 4 parts identified; produce full output, route to Measure or Hunches
- **Validated situation** — cross-source reinforcement across ≥3 lenses and ≥2 audience segments; produce full output, route to Findings or Concepts

Do not upgrade confidence to produce a cleaner result.

### Prohibited output behaviors

- Naming a situation from a single lens or a single source
- Recommending design responses before the situation is validated
- Inferring emotional intent without behavioral evidence
- Flattening conflicting signals into a single clean narrative
- Hiding ambiguity to produce a more confident-sounding situation statement
- Collapsing multiple distinct situations into one to reduce complexity
- Treating a symptom (drop-off point, satisfaction score) as a situation without examining the conditions surrounding it

### Routing rules

| Condition | Route to |
|---|---|
| Evidence weak or from a single source | **Collecting** |
| One lens shows a pattern but a second has not been applied | **Techniques** (apply second lens) |
| Situation emerging but cause unclear | **Hunches** |
| Situation named but audience coverage incomplete | **Audience** (verify across segments) |
| Situation named with strong evidence | **Hunches or Concepts** (move into Measure) |
| Situation validated and sensemaking needed | **Findings** |
| Stakeholder alignment missing | **Reviews** |
| Organizational conditions contributing | **Workflows** |

### Top-priority escalation triggers

- Evidence remains contradictory after 2+ lenses applied
- Confidence stays below Emerging despite multiple input types present
- Multiple situation types equally plausible with comparable evidence
- Business impact is high and lens convergence is incomplete
- Situation appears in one audience segment but not others, with no explanation for the divergence
- A stakeholder assumption is the only available framing

### Top-priority guardrails

- **Never name a situation from a single lens.** One lens = observation. Two converging lenses = situation.
- **Never collapse multiple situations** to produce a cleaner output.
- **Never name a symptom** (drop-off point, satisfaction score) **as the situation.** The situation is the *condition* producing the symptom.

## How to apply

1. **Identify the entry point using Decisions.** Match the user's stuck-state to one of the 8 entries in `reference.md` Decisions (signals exist but no pattern visible, pattern visible but situation not named, multiple situations emerging, etc.).

2. **Apply at least two lenses.** Pick from By Type, By Time, By Stage, By Engagement based on what the user is asking. The full lens table and pairing guidance are in `reference.md` Techniques.

3. **Look for convergence.** A pattern in one lens is an observation. Two lenses converging on the same condition is a situation.

4. **Cross-check against the 9 situation types.** Use the signal-to-situation mapping in `reference.md` References to identify which named type the converging evidence most likely points to.

5. **Draft the situation statement using the 11-field schema.** All four situation parts (trigger / goal / friction / success) must be identifiable. If any part is missing, the situation isn't ready.

6. **Verify across audience segments.** A situation visible in only one segment is an audience-specific finding, not yet a named situation. Route to Audience if needed.

7. **Apply the situation strength checklist** before moving to Measure. A situation that cannot satisfy at least 4 of the 5 checklist questions is an observation, not yet a named situation.

8. **For multiple situations, apply the three prioritization questions** from the Playbook: which is blocking the others, which has the strongest evidence, which connects most directly to a business outcome.

9. **Use the worked Examples to calibrate output quality.** The 4 worked cases (Onboarding Completion Trap, Satisfied Non-Returner, Testing Environment Gap, Stakeholder Override Loop) model how convergence gets named into specific situation statements. The Common Traps table catches the most frequent misreads.

10. **Route per the table above**, with a specific statement of what to do next — not a generic "more research is needed."

## Important architectural context

- **Situations replaces Patterns.** Bryan archived the Patterns block in the Define area; Situations is the new 4th block. The old `glare:define-patterns` skill is deprecated and should redirect here.
- **Situations ≠ User Needs.** User Needs names the category (Basics, Trust, Personal, Impact, Feelings). Situations names the specific context inside that category — how the need manifests under specific conditions.
- **Situations ≠ Jobs to Be Done.** JTBD treats the situation as background. Situations inverts that — the conditions around the need *are* the unit of analysis. JTBD helps you write the User Needs block. Situations is what comes after you collect evidence and recurring conditions emerge.
- **Source docs reference "patterns" too.** When the source uses "pattern" as a generic noun (a recurring observation), that's not the same as the deprecated Patterns block. The Decision Map block is Situations.

## Saving to Ray

Optional. If the Ray MCP is connected (its tools include `list_projects` and `create_situation`), offer to save the framed situation to the project's Decision Map in Ray. If it isn't, skip this section: nothing else in the skill depends on it.

- `create_situation` with `statement` (the framed problem) and `status: active`; set `resolved` later with `update_situation`.
- Link the user needs and audiences it involves in `links` (relation `references`). Hunches written against it link back with `addresses`.

Pick the project with `list_projects` and ask when more than one could fit; don't create a project unasked. Call `list_situations` first so nothing is saved twice, and save only wording the person has approved.

## Handoffs

- When the user shifts to naming the underlying need, suggest `glare:define-user-needs`.
- When they ask who the data should come from or how to weight sources, suggest `glare:define-audience`.
- When they need to gather more evidence before they can name a situation, suggest `glare:define-collecting`.
- When they ask which UX metrics to use to track whether a situation is improving, suggest `glare:define-ux-metrics`.
- For multi-block Define questions, hand back to `glare:define`. For the Decision Map as a whole, `glare:decision-map`.
- When a situation is named and the team is ready to form hypotheses, route to `glare:measure-hunches`.
- When a situation is validated and the team is ready to test design concepts against it, route to `glare:measure-concepts`.
- When the team is preparing to bring the situation to a design review or stakeholder review, route to `glare:design-review`.
- When the team is asking what signals (not just metrics) to capture around a situation, route to `glare:design-signals`.
- When the team is assessing maturity across dimensions, route to `glare:design-assessment`.

**Deprecated skill:** `glare:define-patterns` — if the user invokes it or references it, redirect to this skill.
