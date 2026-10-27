# Situations — Agent Operations

**Block:** Define · Situations
**Audience:** AI Skills (not practitioners)
**Source:** Glare | Define, Situations, Agent Operations v1.1 (Drive doc `13amawUhlHjLuO6XEBGDenzVCIqn-UE5DDuIUIiQ0DF4`)
**Last synced:** 2026-05-26

This file is operating instructions for a Skill working with the Situations block, **not** practitioner reference content. The highest-leverage rules (Required Inputs minimums, the 11-field Situation Output Contract, Confidence Thresholds, Routing Logic, Escalation triggers, Guardrails) are duplicated into `SKILL.md` so they load even if this file is not consulted; the full prescriptive detail lives here.

Practitioner reference content (Overview, Techniques, Playbook, References, Decisions, Examples) lives in `reference.md`.

---

<!-- DERIVED FROM: 13amawUhlHjLuO6XEBGDenzVCIqn-UE5DDuIUIiQ0DF4 — Glare | Define, Situations, Agent Operations v1.1 -->

## Runtime Flow

```
Inputs
  ↓
Validation Rules
  ↓
Confidence Evaluation
  ↓
Lens Application
  ↓
Convergence Check
  ↓
Output Contract
  ↓
Escalation Conditions
  ↓
Next Workflow State
```

### What this block is trying to solve

Situations Skills interpret signals gathered across User Needs, Audience, and Collecting and determine whether those signals are converging on a recurring condition that can be **named as a situation** and carried into Measure.

The Skill is not trying to prove a situation. It is trying to determine whether enough evidence exists across enough sources and lenses to form a situation statement — and if so, what that situation is and what the team should do next.

**The output is always directional, not conclusive.** Conclusive outputs require validation that happens in Measure.

---

## Required Inputs

**Minimum for an observation:**

- At least two distinct input types from the Playbook inputs table
- At least one behavioral signal — something users did, not just something they said
- Workflow context explaining where in the product the condition is appearing

**Minimum for a named situation:**

- Signals from at least two distinct sources
- Convergence across at least **two of the four lenses**
- The condition appearing across more than one user, session, or audience segment
- All four situation parts identifiable: trigger, goal, friction, and what success means

**Minimum for a validated situation:**

- Cross-source reinforcement across behavioral, attitudinal, and performance signals
- Lens convergence confirmed across at least three of the four lenses
- Situation appearing consistently across at least two audience segments
- Contradiction visibility — competing explanations have been considered and addressed

**If minimum inputs are not present, the Skill routes to Collecting before attempting to name a situation.**

---

## Output Contract — The Primary Situation Output

Outputs must follow the **Primary Situation Output** structure defined in the Playbook. The Skill is **not permitted** to produce free-form summaries that omit required fields.

**Required output fields (11):**

1. **Situation Name** — short, descriptive label teams can use as shared vocabulary
2. **Summary** — concise explanation of the recurring condition and the context
3. **Trigger** — the condition, pressure, or goal that sets the situation in motion
4. **What users are trying to do** — the progress the user is seeking in this specific context
5. **What stands in their way** — the friction, uncertainty, or constraint shaping behavior
6. **What success means here** — how the user defines resolution; what failure costs them
7. **Evidence** — the converging signals across lenses and sources
8. **Audience** — which audience segments the situation appears in
9. **Why it matters** — operational, user, or business impact
10. **Lenses applied** — which of the four lenses surfaced the situation and where they converged
11. **UX Metrics** — metrics most useful for validating whether the situation is improving over time

**Output requirements:**

- Preserve evidence visibility — cite which inputs and lenses support which claims
- Explain reasoning — do not state situation conclusions without showing the convergence path
- Maintain signal separation — do not merge distinct inputs into a single undifferentiated claim
- Expose uncertainty — if the situation is an observation, label it as an observation
- Connect outputs to observable behavior — do not substitute assumptions for evidence
- Name which lenses converged and where they pointed to the same condition

**Prohibited output behaviors:**

- Naming a situation from a single lens or a single source
- Recommending design responses before the situation is validated
- Inferring emotional intent without behavioral evidence
- Flattening conflicting signals into a single clean narrative
- Hiding ambiguity to produce a more confident-sounding situation statement
- Overstating confidence relative to the evidence and lens coverage available
- Collapsing multiple distinct situations into one to reduce complexity

---

## Confidence Thresholds

| State | Meaning | Allowed Output |
|---|---|---|
| **Weak signal** | Insufficient evidence to identify a recurring condition | Route to Collecting. Do not attempt to name a situation. |
| **Possible condition** | Early directional signal from one lens or one source | Note the direction. Flag as an observation. Do not name a situation. |
| **Emerging situation** | Two lenses pointing to the same condition, across at least two sources | Draft a situation statement. Flag remaining gaps. State what would confirm or refute it. |
| **Named situation** | Consistent multi-source, multi-lens evidence with all four situation parts identified | Produce a full structured output. Route to Measure or Hunches. |
| **Validated situation** | Cross-source reinforcement across three or more lenses and two or more audience segments | Produce a full output. Route to Findings or Concepts. |

Confidence must remain visible in the output. The Skill must not upgrade confidence to produce a cleaner result.

---

## Classification Constraints

The block uses 9 named situation types (Comprehension breakdown, Trust gap, Effort mismatch, Relevance failure, Habit formation gap, Expectation mismatch, Decision loop, Organizational blind spot, Signal credibility breakdown — see References).

**The Skill should:**

- Allow overlapping situation types when evidence supports multiple recurring conditions simultaneously
- Preserve layered conditions — a workflow may contain both a comprehension breakdown and a trust gap at the same time
- Maintain unresolved classification when evidence does not clearly separate competing situation types
- Allow parallel interpretations when lenses point in more than one direction
- Check every named situation against all four lenses before finalizing classification

**The Skill should not:**

- Force a single situation type when evidence supports more than one
- Collapse multiple distinct situations into one to produce a cleaner output
- Name a situation from a single lens when a second lens might contradict or refine it
- Treat a symptom — a drop-off point, a satisfaction score — as a situation without examining the conditions surrounding it

---

## Failure Modes

| Failure | Operational Risk |
|---|---|
| **Symptom named as situation** | Drop-off or friction point treated as the situation rather than as a signal pointing toward the underlying condition |
| **Single-lens classification** | Situation named from one lens without checking whether a second lens confirms or contradicts it |
| **Proxy treated as production** | Testing results used to name a situation without checking whether By Stage confirms the condition holds in production |
| **Satisfaction treated as retention** | High satisfaction scores used to dismiss a habit formation situation without checking By Engagement activity layer signals |
| **Single-audience framing** | Situation named from one audience segment and assumed to apply broadly without cross-segment verification |
| **Weak evidence promoted** | Observation promoted to named situation without meeting the minimum evidence requirements |
| **Stakeholder assumption treated as signal** | Internal framing of a condition — "this is edge case behavior" — treated as behavioral evidence rather than a classification to test |
| **Situation collapsed prematurely** | Multiple distinct recurring conditions merged into one situation to produce a simpler output, obscuring the full picture |

When a failure mode is detected, the Skill **preserves competing interpretations** rather than resolving to the more confident-sounding situation.

---

## Transition Logic

| Condition | Route to | Purpose |
|---|---|---|
| Evidence is weak or from a single source | **Collecting** | Strengthen signals before attempting to name a situation |
| One lens shows a pattern but a second has not been applied | **Techniques** | Apply the second lens before naming, to check for convergence or contradiction |
| Situation is emerging but cause is unclear | **Hunches** | Structure interpretation before committing to a situation statement |
| Situation is named but audience coverage is incomplete | **Audience** | Verify whether the situation appears consistently across segments before moving to Measure |
| Situation is named and evidence is strong | **Hunches or Concepts** | Move into Measure with a stable situation statement as the anchor |
| Situation is validated and sensemaking is needed | **Findings** | Turn the named situation into usable understanding for the team |
| Stakeholder alignment is missing | **Reviews** | Ground cross-functional conversations in the situation statement |
| Organizational conditions are contributing to the situation | **Workflows** | Evaluate whether systemic factors outside the product experience are sustaining the condition |

Transitions should remain reversible. If new evidence changes interpretation after a transition, the Skill should support returning to Situations.

---

## Escalation Logic

**Escalate when:**

- Evidence remains contradictory after applying two or more lenses
- Confidence stays below the emerging situation threshold after multiple input types are present
- Multiple situation types remain equally plausible with comparable evidence
- Business impact of the decision is high and lens convergence is incomplete
- The situation appears in one audience segment but not others, with no explanation for the divergence
- A stakeholder assumption is the only available framing for the condition

**Escalation outputs must:**

- Preserve uncertainty visibly — do not resolve before escalating
- Explain which situation interpretations remain unresolved and why
- Identify specifically what evidence or lens coverage is missing
- Recommend next collecting or interpretation steps rather than defaulting to a direction
- Label the output state clearly — unresolved ambiguity, conflicting lenses, or insufficient signals

---

## Ambiguity Handling

Ambiguity is operationally normal in Situations workflows. Most inputs arrive without full lens coverage, across incomplete audience ranges, or with conflicting signals.

**The Skill should:**

- Preserve uncertainty visibly throughout the output
- Maintain competing situation interpretations when evidence supports more than one type
- Identify specifically what evidence or lens application is missing and what it would resolve
- Explain interpretation gaps rather than filling them with assumptions
- Recommend next validation steps as part of every ambiguous output

**The Skill should not:**

- Force a situation name to produce a more coherent output
- Optimize for narrative smoothness over interpretive accuracy
- Collapse uncertainty into confidence when lens convergence does not support it
- Remove contradictory evidence because it complicates the situation statement

---

## Guardrails

Hard operational boundaries. Apply to every Situations output regardless of confidence state, input quality, or workflow context.

| Guardrail | What it prevents |
|---|---|
| **Never name a situation from a single lens** | Premature classification before convergence is established |
| **Preserve conflicting lens evidence** | Premature resolution of competing situation interpretations |
| **Preserve unresolved ambiguity** | False confidence in outputs with incomplete lens coverage or source diversity |
| **Expose evidence sources and lenses** | Untraceable claims that cannot be evaluated or challenged by the team |
| **Separate observation from situation** | Conflation of a signal or symptom with the condition producing it |
| **Never recommend solutions before situation validation** | Premature direction-locking before the situation is stable enough for Measure |
| **Never replace behavior with assumptions** | Inference about conditions substituted for observable evidence |
| **Never collapse multiple situations prematurely** | Loss of important distinctions between concurrent recurring conditions |

Guardrails prioritize interpretive accuracy over output smoothness. **A less confident but more accurate situation statement is always preferred.**

---

## Multi-Agent Workflows

Situations Skills may operate as part of a larger multi-agent workflow:

- **The Observation Skill** reviews collected signals across all four lenses and identifies recurring conditions without yet naming them
- **The Interpretation Skill** applies lens convergence logic to determine whether an observation meets the threshold for a named situation
- **The Naming Skill** produces the full structured situation output using the four-part format
- **The Validation Skill** evaluates confidence thresholds, checks audience coverage, and routes to the appropriate next block

Each Skill should receive the full evidence base — not a summarized version — so interpretation remains grounded in observable signals rather than a compressed narrative.

---

## Human Judgment

Human judgment remains responsible for:

- Prioritization across competing situations when evidence is roughly equal
- Strategic tradeoffs between named situations and business constraints
- Organizational context the Skill cannot observe — team dynamics, political context, timing
- Decisions about which situations are worth carrying into Measure given current resource and momentum
- Judgment about whether a named situation reflects the full scope of what is actually happening
- Leadership decisions about which conditions to invest in addressing

The goal is stronger operational decision support through calibrated Skill behavior — **not replacement** of the judgment that makes decisions consequential.

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-26 -->

## Which rules are promoted into SKILL.md

The following rules are duplicated into `SKILL.md` so they load on every invocation:

- **Required inputs minimums** — observation / named situation / validated situation thresholds
- **5-state confidence model** — Weak signal → Possible condition → Emerging situation → Named situation → Validated situation
- **11-field Primary Situation Output schema**
- **Top-priority routing rules** — weak evidence → Collecting; one lens only → Techniques; named situation with strong evidence → Hunches/Concepts; validated → Findings
- **Top-priority escalation triggers** — contradictory evidence after 2+ lenses; confidence below Emerging despite multiple inputs; equally plausible situations; high business impact + incomplete convergence
- **Top-priority guardrails** — never name from a single lens; never collapse situations; never name symptom as situation

The full Classification Constraints (9 named situation types), full Transition Logic table, Multi-Agent Workflows architecture, Skill Boundaries, and Human Judgment scope are consulted when the Skill needs to handle ambiguity, route a multi-Skill workflow, or recognize a boundary it shouldn't cross.

<!-- /ADDED -->
