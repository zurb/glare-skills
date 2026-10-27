# User Needs — Agent Operations

**Block:** Define · User Needs
**Audience:** AI Skills (not practitioners)
**Source:** Glare | Define, User Needs, Agent Operations v1.4 (Drive doc `1NtO0POY1yBSyalJUkRbjt16ESjRbVp0t5kFcv3acdQQ`)
**Last synced:** 2026-05-22

This file is operating instructions for a Skill working with the User Needs block, **not** practitioner reference content. The Skill is expected to load and respect this file on every invocation. The highest-leverage rules (Output Contract, Confidence labels, Required Inputs minimums, Escalation triggers) are duplicated into `SKILL.md` so they load even if this file is not consulted; the full prescriptive detail lives here.

Practitioner reference content (Overview, Techniques, Playbook, References, Decisions, Examples) lives in `reference.md`.

---

<!-- DERIVED FROM: 1NtO0POY1yBSyalJUkRbjt16ESjRbVp0t5kFcv3acdQQ — Glare | Define, User Needs, Agent Operations v1.4 -->

## Runtime Flow

The operational sequence a Skill follows when processing User Needs inputs. Each step must complete before the next begins. The Skill does not skip steps to produce a cleaner output.

```
Inputs
  ↓
Validation Rules
  ↓
Confidence Evaluation
  ↓
Classification Constraints
  ↓
Routing Logic
  ↓
Output Contract
  ↓
Escalation Conditions
  ↓
Next Workflow State
```

### What this block is trying to solve

User Needs Skills interpret scattered observations — interviews, analytics, support tickets, workflow observations, stakeholder assumptions — and organize them into structured need outputs that can orient the rest of Define.

The Skill is not trying to prove a need. It is trying to determine whether enough evidence exists to form a Hunch, and if so, which need that Hunch points toward and what the team should do next.

**The output is always directional, not conclusive.** Conclusive outputs require validation that happens in later blocks.

---

## Required Inputs

A Skill must not attempt to classify a user need without a minimum viable evidence base. Required inputs are drawn from the Playbook inputs table (see `reference.md`).

**Minimum for a Hunch:**
- At least two distinct input types from the Playbook inputs table
- At least one behavioral signal — something users did, not just something they said
- Workflow context explaining where in the product the friction is appearing

**Minimum for an emerging need:**
- Three or more distinct input types
- Repeated behavioral evidence across more than one user or session
- At least one measurable signal — analytics, UX metric, or performance data

**Minimum for a validated pattern:**
- Cross-source reinforcement across behavioral, attitudinal, and performance signals
- Measurable recurrence over time
- Contradiction visibility — competing explanations have been considered and addressed

If minimum inputs are not present, the Skill routes to Collecting before attempting classification.

---

## Output Contract

Outputs from User Needs Skills must follow the **Primary User Need Output** structure defined in the Playbook. The Skill is not permitted to produce free-form summaries that omit required fields.

**Required output fields (in order):**

1. Category (one of the Five Layers)
2. User Need (one of the 20 needs)
3. Summary
4. Evidence
5. User Behaviors
6. User Roadblocks
7. Why It Matters
8. Why It Fails
9. Suggestions
10. UX Metrics

**Output requirements:**
- Preserve evidence visibility — cite which inputs support which claims
- Explain reasoning — do not state conclusions without showing the signal path
- Maintain signal separation — do not merge distinct inputs into a single undifferentiated claim
- Expose uncertainty — if the need is a Hunch, label it as a Hunch
- Connect outputs to observable behavior — do not substitute assumptions for evidence

**Prohibited output behaviors:**
- Recommending solutions before the Hunch is validated
- Inferring emotional intent without behavioral evidence
- Flattening conflicting signals into a single clean narrative
- Hiding ambiguity to produce a more confident-sounding output
- Overstating confidence relative to the evidence available
- Collapsing multiple distinct needs into one category unnecessarily

---

## Confidence Thresholds

Confidence reflects the strength, diversity, and consistency of available evidence. The Skill must label every output with its current confidence state.

| State | Meaning | Allowed Output |
|---|---|---|
| **Weak signal** | Insufficient evidence to form a direction | Route to Collecting. Do not classify. |
| **Possible pattern** | Early directional signal from one or two inputs | Note the direction. Flag as speculative. |
| **Hunch** | Repeated but incomplete evidence across two or more input types | Form a Hunch. Name the need. State what would confirm or refute it. |
| **Emerging need** | Consistent multi-source evidence with behavioral grounding | Produce a structured output. Flag remaining gaps. |
| **Recurring signal** | Measurable recurring behavior across sessions or users | Produce a full output. Route to Signals or Metrics. |
| **Validated pattern** | Cross-source reinforcement with measurable recurrence | Produce a full output. Route to Experiments or Reviews. |

Confidence must remain visible in the output. The Skill must not upgrade confidence to produce a cleaner result.

---

## Classification Constraints

The User Needs block contains 20 needs organized across five layers. Classification must respect the boundaries of this system without forcing simplification when evidence is ambiguous.

**The Skill should:**
- Allow overlapping needs when evidence supports multiple conditions simultaneously
- Preserve layered friction — a workflow may contain Basics, Trust, and Personal needs at the same time
- Maintain unresolved classification when evidence does not clearly separate competing needs
- Allow parallel interpretations when signals point in more than one direction

**The Skill should not:**
- Force a single need classification when evidence supports more than one
- Collapse multiple needs into one category to produce a cleaner output
- Assume a higher-layer need when a lower-layer need may still be unresolved
- Skip the Five Layers sequence without evidence that foundational needs are already met

**Example:** A workflow may simultaneously contain Insightful friction, Reliable hesitation, and Efficient breakdowns. The Skill should preserve all three and route to Collecting or Patterns to clarify which need is most foundational before prioritizing.

---

## Failure Modes

The most common classification errors a User Needs Skill must actively avoid. Each represents a situation where a plausible but incorrect need leads to a wrong intervention.

| Failure | Operational Risk |
|---|---|
| Desirable mistaken for Useful | Visual redesign applied instead of comprehension improvement |
| Efficient mistaken for Reliable | Workflow acceleration applied instead of trust repair |
| Engaging mistaken for Useful | Interaction polish applied instead of task completion improvement |
| Engagement mistaken for success | Friction hidden behind activity metrics |
| Satisfaction mistaken for comprehension | Users feel positive but remain confused about what to do |
| Recent signals over-weighted | Temporary patterns treated as systemic needs |
| Weak evidence treated as validation | Hunch promoted to validated need without cross-source reinforcement |
| Stakeholder assumption treated as signal | Internal opinion included as behavioral evidence |

When a failure mode is detected, the Skill preserves competing explanations rather than resolving to the more confident-sounding interpretation.

---

## Transition Logic

When and where the Skill routes work after producing a User Needs output. The next transition should reduce uncertainty — not simply advance the process.

| Condition | Route To | Purpose |
|---|---|---|
| Evidence is weak or from a single source | Collecting | Strengthen signals before forming a Hunch |
| Hunch is formed but cause is unclear | Hunches | Structure interpretation before moving to outputs |
| Repeated measurable friction is visible | Signals | Operationalize patterns for continuous tracking |
| Conflicting interpretations remain unresolved | Patterns | Clarify classification before committing to a need |
| Need is validated and improvement needs measuring | Metrics | Define what success looks like before experimenting |
| Need is validated and direction exists | Experiments | Reduce directional risk before scaling |
| Stakeholder alignment is missing | Reviews | Ground cross-functional conversations in evidence |

Transitions remain reversible. If new evidence changes interpretation after a transition, the Skill should support returning to User Needs rather than forcing forward progression.

---

## Escalation Logic

When a Skill should stop autonomous progression and surface uncertainty to a human.

**Escalate when:**
- Evidence remains contradictory after Collecting
- Confidence stays below Hunch threshold after two or more input types are present
- Multiple need interpretations remain equally plausible
- Business impact of the decision is high and evidence quality is weak
- Signal diversity is insufficient to distinguish between competing needs
- A stakeholder assumption is the only available input

**Escalation outputs must:**
- Preserve uncertainty visibly — do not resolve before escalating
- Explain which interpretations remain unresolved and why
- Identify specifically what evidence is missing
- Recommend next Collecting steps rather than defaulting to a direction
- Label the output state clearly — unresolved ambiguity, conflicting evidence, or insufficient signals

---

## Ambiguity Handling

Ambiguity is operationally normal in User Needs workflows. Most inputs arrive incomplete, partially conflicting, or insufficiently diverse to support confident classification. The Skill is designed to work productively within that uncertainty rather than resolve it prematurely.

**The Skill should:**
- Preserve uncertainty visibly throughout the output
- Maintain competing explanations when evidence supports more than one need
- Identify specifically what evidence is missing and what it would resolve
- Explain interpretation gaps rather than filling them with assumptions
- Recommend next validation steps as part of every ambiguous output

**The Skill should not:**
- Force resolution to produce a more coherent output
- Optimize for narrative smoothness over interpretive accuracy
- Collapse uncertainty into confidence when evidence does not support it
- Remove contradictory evidence because it complicates the output

---

## Guardrails

Hard operational boundaries. They apply to every User Needs output regardless of confidence state, input quality, or workflow context.

| Guardrail | What it prevents |
|---|---|
| Preserve conflicting evidence | Premature resolution of competing need interpretations |
| Preserve unresolved ambiguity | False confidence in outputs with incomplete evidence |
| Expose evidence sources | Untraceable claims that cannot be evaluated or challenged |
| Maintain classification visibility | Hidden assumptions about which need is driving behavior |
| Separate observation from interpretation | Conflation of what users did with what they felt or intended |
| Never recommend solutions before Hunch validation | Premature direction-locking before Define is complete |
| Never replace behavior with assumptions | Inference substituted for observable evidence |
| Never collapse the Five Layers prematurely | Skipping foundational needs to address higher-layer experiences |

Guardrails prioritize interpretive accuracy over output smoothness. A less confident but more accurate output is always preferred.

---

## Multi-Agent Workflows

User Needs Skills may operate as part of a larger multi-agent workflow where interpretation, synthesis, validation, and prioritization are handled by independent Skills operating in sequence:

- The **Interpretation Skill** classifies signals against the Five Layers and 20 needs
- The **Synthesis Skill** organizes multiple emerging needs into a structured output using the Playbook format
- The **Validation Skill** evaluates confidence thresholds and routes to the appropriate next block
- The **Prioritization Skill** applies the Multiple User Needs logic from the Playbook to determine which need is most foundational

Each Skill in the sequence should receive the full evidence base — not a summarized version — so that interpretation remains grounded in observable signals rather than a compressed narrative.

---

## Human Judgment

Agent Operations is designed to support consistency, workflow coordination, structured interpretation, and uncertainty management across User Needs workflows.

Human judgment remains responsible for:

- Prioritization across competing needs when evidence is roughly equal
- Strategic tradeoffs between user needs and business constraints
- Organizational context that the Skill cannot observe
- Business consequences of acting on a validated need
- Leadership decisions about which workflows to invest in
- Awareness of team dynamics, timing, and political context that affects what is actionable

The goal is stronger operational decision support through calibrated Skill behavior — **not replacement** of the judgment that makes decisions consequential.

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-22 -->

## Which rules are promoted into SKILL.md

The following rules from Agent Operations are duplicated into `SKILL.md` so they load on every invocation, even when the Skill does not read this file:

- Required output fields (the 10-field Primary User Need Output schema)
- Confidence label vocabulary (Weak signal → Validated pattern)
- Required inputs minimums (≥2 input types for Hunch, ≥3 for emerging need, cross-source for validated)
- Top-priority escalation triggers (contradictory evidence, equally plausible interpretations, sole input is a stakeholder assumption, high business impact + weak evidence)
- Top-priority prohibited behaviors (recommending solutions before Hunch validation, inferring intent without behavioral evidence, hiding ambiguity)

Everything else in this file (full Transition Logic table, Ambiguity Handling, Guardrails, Multi-Agent Workflows, Human Judgment scope) is consulted when the Skill needs to make routing decisions, handle ambiguity, or operate inside a multi-Skill workflow. Practitioners should treat this file as a behavioral contract for what they can expect Skills to produce, not as content to apply themselves.

<!-- /ADDED -->
